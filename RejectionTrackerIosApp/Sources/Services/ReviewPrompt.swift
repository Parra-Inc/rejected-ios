//
//  ReviewPrompt.swift
//  RejectionTrackerIosApp
//
//  Milestone-gated App Store review prompt. Asks for a rating only at a genuine
//  value moment (after the user has logged enough rejections to have adopted the
//  habit), and only when a set of UserDefaults gates all pass:
//    - the once-ever milestone prompt has not already fired
//    - at least `minInterval` has elapsed since the last prompt of any kind
//    - the value moment itself is eligible (rejection-count milestone reached)
//
//  Mirrors skimmer's ReviewPrompt shape, adapted to Rejected. There is no web
//  backend here, so the gate is entirely local (UserDefaults). Apple only
//  surfaces the in-app review sheet a few times per year, so spending the prompt
//  at a real value moment (the celebratory ShareView after the Nth rejection,
//  never at launch, onboarding, or right after the tip jar) is the whole point.
//
//  The actual `requestReview()` call must come from a SwiftUI view (it needs
//  `@Environment(\.requestReview)`); views ask this gate whether a moment is
//  eligible, then call `requestReview()` themselves and `markMilestoneFired()`.
//

import Foundation

/// Milestone-gated review gate. Stateless: all state lives in `UserDefaults`.
enum ReviewPrompt {

    /// Rejections logged before we consider the app to have proven its value.
    /// The prompt fires on the fifth logged rejection, not the first: by then the
    /// user has clearly adopted the habit and the reframe has landed.
    static let rejectionMilestone = 5

    /// Minimum time between two review prompts, even across app versions and even
    /// between the manual "Rate This App" row and the automatic milestone. Guards
    /// against asking twice in quick succession.
    static let minInterval: TimeInterval = 60 * 60 * 24 * 14 // 14 days

    /// Value moments that can justify a review prompt.
    enum Trigger {
        /// The user just logged a rejection (and dismissed the celebratory share
        /// screen). Eligible once the logged-rejection count reaches
        /// `rejectionMilestone`, and only once ever.
        case loggedRejection(count: Int)
    }

    private static let milestoneFiredKey = "rejected.review.milestoneFired"
    private static let lastPromptedAtKey = "rejected.review.lastPromptedAt"

    // MARK: - Public API

    /// Returns `true` when a review prompt should be shown for this trigger.
    /// Gated on a minimum interval since the last prompt and the trigger's own
    /// once-ever eligibility rule.
    @MainActor
    static func shouldRequest(for trigger: Trigger, defaults: UserDefaults = .standard) -> Bool {
        // Gate 1: respect the minimum interval since the last prompt of any kind
        // (manual rating row included).
        if let last = defaults.object(forKey: lastPromptedAtKey) as? Date,
           Date().timeIntervalSince(last) < minInterval {
            return false
        }

        // Gate 2: the value moment itself must be eligible.
        switch trigger {
        case .loggedRejection(let count):
            // Once ever: the celebratory ShareView fires on every rejection, so a
            // per-view flag would re-arm each time. The persistent flag makes the
            // milestone prompt fire exactly once, at the milestone.
            guard !defaults.bool(forKey: milestoneFiredKey) else { return false }
            return count >= rejectionMilestone
        }
    }

    /// Call immediately after `requestReview()` fires for the automatic milestone
    /// so the milestone never re-fires and the interval cooldown restarts.
    @MainActor
    static func markMilestoneFired(defaults: UserDefaults = .standard) {
        defaults.set(true, forKey: milestoneFiredKey)
        markPrompted(defaults: defaults)
    }

    /// Restart the interval cooldown without consuming the once-ever milestone.
    /// Call after the manual "Rate This App" row is submitted, so an automatic
    /// prompt does not fire moments later. The manual row is never gated by the
    /// milestone dedupe, so it must not set `milestoneFiredKey`.
    @MainActor
    static func markPrompted(defaults: UserDefaults = .standard) {
        defaults.set(Date(), forKey: lastPromptedAtKey)
    }

    /// Test/debug helper, re-arms the prompt completely.
    @MainActor
    static func reset(defaults: UserDefaults = .standard) {
        defaults.removeObject(forKey: milestoneFiredKey)
        defaults.removeObject(forKey: lastPromptedAtKey)
    }
}
