//
//  RatingPromptSheet.swift
//  RejectionTrackerIosApp
//
//  The Settings "Rate This App" sheet: a custom 1-5 star control, entirely our
//  own UI. Five stars triggers the real system review prompt; one to four stars
//  routes to the app's private Parra feedback form instead, keeping unhappy users
//  out of the public review flow and giving them a faster path to be heard.
//  Rejected has no web backend, so there is no server-side capture: the feedback
//  form is the capture.
//
//  Mirrors skimmer's RatingPromptSheet shape, adapted to Rejected's Parra theme
//  and its Parra feedback form (in place of skimmer's mailto).
//

import Parra
import StoreKit
import SwiftUI

struct RatingPromptSheet: View {
    @Environment(\.dismiss) private var dismiss
    @Environment(\.requestReview) private var requestReview
    @Environment(\.parra) private var parra
    @Environment(\.parraAppInfo) private var parraAppInfo
    @Environment(\.parraTheme) private var parraTheme

    @State private var stars = 0
    @State private var isSubmitting = false
    @State private var feedbackForm: ParraFeedbackForm?
    @State private var showThankYou = false

    /// Trophy gold (#D4A24C) — the brand's rejection-as-trophy accent.
    private let trophyGold = Color(red: 0.831, green: 0.635, blue: 0.298)

    var body: some View {
        VStack(spacing: 24) {
            VStack(spacing: 8) {
                Text("Rate Rejected")
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundStyle(Color.primary)
                Text("Collect rejections like trophies. How's it going so far?")
                    .font(.callout)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
            }
            .padding(.top, 28)
            .padding(.horizontal, 24)

            HStack(spacing: 14) {
                ForEach(1...5, id: \.self) { i in
                    Button {
                        stars = i
                    } label: {
                        Image(systemName: i <= stars ? "star.fill" : "star")
                            .font(.system(size: 34))
                            .foregroundStyle(
                                i <= stars
                                    ? trophyGold
                                    : parraTheme.palette.secondarySeparator.toParraColor()
                            )
                    }
                    .buttonStyle(.plain)
                    .accessibilityLabel("\(i) star\(i == 1 ? "" : "s")")
                }
            }
            .sensoryFeedback(.selection, trigger: stars)

            Button {
                submit()
            } label: {
                Text("Submit")
                    .font(.headline)
                    .foregroundStyle(.white)
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 14)
                    .background(
                        stars > 0
                            ? parraTheme.palette.primary.toParraColor()
                            : parraTheme.palette.secondarySeparator.toParraColor(),
                        in: RoundedRectangle(cornerRadius: 12)
                    )
            }
            .buttonStyle(.plain)
            .disabled(stars == 0 || isSubmitting)
            .padding(.horizontal, 24)

            Spacer()
        }
        .frame(maxWidth: .infinity)
        .background(parraTheme.palette.secondaryBackground.toParraColor())
        .presentationDetents([.medium])
        .presentationDragIndicator(.visible)
        .presentParraFeedbackFormWidget(with: $feedbackForm)
        .onChange(of: feedbackForm != nil) { wasPresented, isPresented in
            // The feedback form was shown and has now been dismissed: close the
            // rating sheet behind it.
            if wasPresented && !isPresented {
                dismiss()
            }
        }
        .alert("Thanks for the feedback", isPresented: $showThankYou) {
            Button("OK") { dismiss() }
        } message: {
            Text("We read every note and use it to make Rejected better.")
        }
    }

    private func submit() {
        guard stars > 0 else { return }
        isSubmitting = true

        // Restart the milestone cooldown so an automatic prompt doesn't fire
        // moments after the user already rated here. Never consumes the once-ever
        // milestone: the manual row is not gated by it.
        ReviewPrompt.markPrompted()

        if stars == 5 {
            requestReview()
            dismiss()
        } else {
            routeToFeedback()
        }
    }

    /// Route sub-5-star sentiment to the app's private feedback form instead of
    /// the public App Store. Falls back to a thank-you alert if no feedback form
    /// is configured (never a dead-end to the store for low ratings).
    private func routeToFeedback() {
        guard let formId = parraAppInfo.application.defaultFeedbackFormId else {
            showThankYou = true
            return
        }

        Task {
            do {
                feedbackForm = try await parra.feedback.fetchFeedbackForm(
                    formId: formId
                )
            } catch {
                ParraLogger.error(error)
                showThankYou = true
            }
        }
    }
}

#Preview {
    ParraAppPreview(authState: .authenticatedPreview) {
        Color.clear
            .sheet(isPresented: .constant(true)) {
                RatingPromptSheet()
            }
    }
}
