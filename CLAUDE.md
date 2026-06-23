# Rejected

Free iOS app for tracking rejections (App Store, YC, jobs, investors, lit mags, life) — built around the reframe that **rejection is data, not a verdict**. The growth loop is the share screen.

## Tech Stack
- Swift 6 / SwiftUI / SwiftData
- Parra SDK (auth, feedback, roadmap, changelog)
- StoreKit 2 (consumable tip jar — `v1.tip.1` / `v1.tip.3` / `v1.tip.10`)
- Open source — `github.com/Parra-Inc/rejected-ios`

## Project Structure
```
RejectionTrackerIosApp/
├── Sources/
│   ├── App.swift
│   ├── ContentView.swift
│   ├── RejectionTab.swift
│   ├── CreateRejectionView.swift
│   ├── CreateCategoryView.swift
│   ├── CategoryPickerView.swift
│   ├── CategorySelectControl.swift
│   ├── ShareView.swift            # The growth loop — the share screen
│   ├── DataManager.swift
│   ├── PreviewContainer.swift
│   ├── Config.swift
│   ├── Models/
│   ├── Settings Tab/
│   ├── TipJar/
│   ├── UI/
│   └── Utilities/
├── Assets.xcassets/
├── StoreKit.storekit
└── Info.plist

marketing/
├── strategy.md                    # Start here for marketing context
├── positioning.md                 # Message house, voice, against-statements
├── segments.md                    # 5 personas (indie hackers, job seekers, founders, writers, rejection-therapy)
├── brand.md                       # Voice, color, share-image spec
├── channels.md                    # Channel mix, time allocation, KPIs
├── twitter-x.md                   # Channel #1 — the viral primitive
├── communities.md                 # Channel #2 — IH, Reddit, HN, Discord, WIP
├── content-marketing.md           # Channel #3 — Rejection Wall, essays, SEO
├── product-launches.md            # Channel #4 — Show HN, Product Hunt
└── plan.md                        # Long-form playbook (KPIs, ads library, 12-month story)
```

## Brand TL;DR
- **Tagline:** Collect rejections like trophies.
- **Voice:** Defiant-optimistic. Lowercase Marc Lou + Jia Jiang reframe. Never therapy-coded, never self-pitying. See [marketing/brand.md](marketing/brand.md).
- **Colors:** Trophy gold (`#D4A24C`) on off-black ink and cream paper.
- **Pricing:** Free forever. Tip jar (consumable IAPs). No subscription. No required login.

## Marketing
- **Read first:** [marketing/strategy.md](marketing/strategy.md) — overview, narrative leverage, 12-month story.
- **Channels (priority order):** X/Twitter → Communities (IH, Reddit, HN) → Content marketing (Rejection Wall + essays) → Product launches (Show HN, PH) → LinkedIn → TikTok → Newsletter swaps → Creator outreach. Full ranking in [marketing/channels.md](marketing/channels.md).
- **Launch unlocks:**
  1. **Show HN** with the personal rejection story (Tuesday 8am PT) — see [marketing/product-launches.md](marketing/product-launches.md).
  2. **#RejectionWeek** social event (one week of public daily rejection posts) — see [marketing/plan.md](marketing/plan.md) §4 Initiative 1.
  3. **The Rejection Wall** — community-submitted App Review rejection emails as compounding SEO+social asset — see [marketing/content-marketing.md](marketing/content-marketing.md) §3.
- **What we are NOT:** journaling app, productivity app, therapy app, SaaS, submission manager. See [marketing/positioning.md](marketing/positioning.md) §6 (against statements).
- **Long-form playbook:** [marketing/plan.md](marketing/plan.md) — KPIs, ads library, weekly cadence, 12-month milestones, anti-patterns.

### Voice cheat sheet
| Yes | No |
|---|---|
| "Logged. Back to work." | "Your rejection has been saved successfully!" |
| "0 yeses today. 1 no logged." | "Stay positive and keep applying!" |
| "Applied is an aspiration. Rejected is a receipt." | "Don't let rejection define you" |
| Lowercase. Terse. Tabular numerals. Emoji as data. | Exclamation points. Wellness vocabulary. Tribe/journey/embrace. |
