# Rejected — Product Launches Playbook

> Show HN, Product Hunt, Hacker Newsletter, Indie Hackers Launches, MakerLog. Each one is a 24-hour spike + a long tail. Required once at launch, repeatable per major feature.

---

## 1. Why product launches matter at rank #4

A successful Show HN or Product Hunt launch is one of the few moments where a single day's work produces installs for the next 12 months (App Store best-seller momentum + backlinks + ongoing PH category placement). The "I built this after my 50th rejection" angle is **native** to these surfaces — the audience there celebrates that exact arc.

We are not launching once. We are launching three times in the first six months:
1. **v1.0 launch** (Week 1) — the big one. Show HN + Product Hunt + Hacker Newsletter + Indie Hackers Launches.
2. **Feature relaunch** (Month 3–4) — when Pro tier ships, OR when "Year in Rejection" export ships. Whichever is bigger.
3. **Milestone relaunch** (Month 6) — "10K rejections logged" with the public data report.

---

## 2. Launch surfaces ranked

| Surface | Reach (peak) | Audience fit | Effort | Repeatability |
|---|---|---|---|---|
| **Show HN** | 5K–50K visits in 24h | Seg 1 + 3 | Very high (one-shot) | Once per major version |
| **Product Hunt** | 2K–20K visits in 24h | Seg 1 + 3 + general | High (build hunter network) | Once per feature |
| **Indie Hackers Launches** | 500–5K visits | Seg 1 | Medium | Per release |
| **Hacker Newsletter** | 1K–5K visits when included | Seg 1 + 3 | Low (pitch only) | Per feature |
| **Lobste.rs Show** | 200–2K visits | Seg 1 deep tech | Low | Once |
| **MakerLog / WIP launches** | 100–1K visits | Seg 1 | Low | Per release |
| **r/SideProject launch** | 500–3K visits | Seg 1 | Low | Per release (~quarterly cap) |
| **BetaList / Launching Next** | 100–500 visits | Generic | Low | Once each |

---

## 3. The v1.0 launch week — full sequence

Lock the date 4–6 weeks out. Every channel synchronizes to this week.

### The week-of timeline

| Day | Time | Action |
|---|---|---|
| **Sat (D-2)** | — | Final QA pass, fix the screenshot grid, lock the App Store listing. Test deep links from rejected.app to the App Store. |
| **Sun (D-1)** | — | Pre-write all 7 daily seed posts for Rejection Week. Schedule the Day-7 IH/Reddit posts. Notify 5 friends to upvote Show HN tomorrow 8am PT. |
| **Mon (D0)** | 8:00 AM PT | Show HN goes live (see §4) |
| **Mon (D0)** | 8:15 AM PT | IH launch post (see communities.md §3) |
| **Mon (D0)** | 8:30 AM PT | r/SideProject post |
| **Mon (D0)** | 9:00 AM PT | X launch thread (see twitter-x.md §5) |
| **Mon (D0)** | 9:30 AM PT | LinkedIn launch post (founder vulnerable version) |
| **Mon (D0)** | All day | HN comment response marathon |
| **Tue (D+1)** | 12:01 AM PT | **Product Hunt launch goes live** (see §5) |
| **Tue (D+1)** | 12:30 AM PT | Maker comment, hunter intro, founder PH responses begin |
| **Tue (D+1)** | 7:00 AM PT | Lobste.rs Show cross-post |
| **Tue (D+1)** | 9:00 AM PT | r/iOSProgramming + r/swift cross-posts |
| **Tue (D+1)** | All day | PH comment marathon + X amplification of "we're #X on PH today" updates |
| **Wed (D+2)** | — | Indie Hackers Launches submission |
| **Wed (D+2)** | — | Hacker Newsletter pitch email |
| **Thu (D+3)** | — | MakerLog post + r/cscareerquestions post |
| **Fri (D+4)** | — | Rejection Week mid-week recap thread + LinkedIn data post |
| **Sat (D+5)** | — | TestFlight feedback collection from PH commenters |
| **Sun (D+6)** | — | "Launch week recap" essay + thread with install count + tip count |

---

## 4. Show HN — the post

### The post itself

Already drafted in plan.md §4.5 and communities.md §4. Reproduced for convenience:

> **Show HN: I built an iOS app for collecting rejections like trophies**
>
> Background: I'm an indie developer. Last year my app was rejected by App Review 11 times for guideline 4.3 (design spam) on a totally original idea — eventually I gave up. The same year I applied to YC and got rejected without an interview. Then I got laid off.
>
> I started keeping a list of every no — Apple, YC, jobs, investors — because it was the only way to make the volume feel like progress instead of pain.
>
> A year later I cleaned up the list, turned it into an iOS app, and open-sourced it. It's called Rejected. Free, no sign-in, no subscription. You log a category, title, and note. You get stats and a share screen.
>
> Source: github.com/Parra-Inc/rejected-ios
> App Store: [link]
>
> Built with SwiftUI, SwiftData, StoreKit 2, and Parra (open-source iOS SDK).
>
> Things I want feedback on:
> 1. Is the share screen too cheerful? (🤠 emoji might be too much.)
> 2. Should I add Apple-rejection-specific fields (guideline number, reviewer name)?
> 3. Tip jar vs. light Pro tier (CSV export, custom icons) — which is the indie-friendly move?
>
> Happy to answer anything about App Review, Parra, or living through 100+ rejections this year.

### Logistics

| Item | Detail |
|---|---|
| **Timing** | Tuesday 8:00 AM Pacific (peak HN intake) — though Mon for Rejected because we want PH on Tue |
| **Pre-coordination** | 5 friends agree to upvote organically in first 30 min — do NOT use a ring |
| **Comment response SLA** | Every comment within 1h for first 6h, every 2h for next 6h, every 4h after |
| **Heroes to notify** | @dang (mod awareness only), @mijustin, @marc_louvion, @stevemoser, @csallen — heads-up, not asks |
| **Success bar** | 150+ upvotes, front page top half, 5K visits to rejected.app, 500 installs in 48h |

### If it flops
- Do not resubmit within 90 days
- Diagnose: was the title weak? was the personal story missing? did the timing collide with bigger news?
- Rewrite with a deeper personal narrative, wait 90 days, try Tuesday again

---

## 5. Product Hunt — full plan

PH is the second-biggest single-day reach surface. Tuesday-Thursday launches outperform Monday and Friday.

### Pre-launch (start 4 weeks out)

1. **Find a hunter** (someone with PH karma to do the actual post). Options:
   - @marc_louvion (best fit, known for indie iOS launches)
   - @yongfook
   - @leevy
   - @kpcb (Kunal Patel)
   - If no hunter, founder posts directly — works fine for high-quality submissions
2. **Build the PH ship page** (PH gives you a pre-launch page where you collect upvote-pledges)
3. **DM your network** — 50 personal messages: "I'm launching Rejected on PH Tuesday — would mean a lot if you could upvote in the morning. Here's the link to subscribe to the launch alert: [PH ship URL]"
4. **Coordinate 30 confirmed first-hour upvoters** (this is the make-or-break number)
5. **Build a 5-image gallery** for the PH page (similar but not identical to App Store screenshots)
6. **Pre-write maker comment** (see template below)
7. **Pre-write 10 anticipated FAQ answers** so responses ship within 60 sec

### The PH launch post

| Field | Content |
|---|---|
| **Name** | Rejected |
| **Tagline (60 char)** | Collect rejections like trophies |
| **Description (260 char)** | Job rejections, App Store rejections, YC rejections, life rejections — track every "no" and share the wins. Free iOS app. No sign-in, no subscription. Open source. |
| **Topics** | iOS, Productivity, Open Source, Health & Fitness (for the rejection-therapy angle) |
| **Gallery** | 1 hero image (the share screen), 5 product screenshots, 1 GIF of the add flow |

### The maker comment (post at 12:05 AM PT on launch day)

> Hey PH 👋 — Rejected is the iOS app I needed last year and couldn't find.
>
> Background: in 2025 my app got rejected by Apple 11 times. I got rejected by YC three times. I got laid off and rejected by 23 employers before I started my own thing. I started keeping a list of every no because the volume started to feel like proof I tried, not proof I sucked.
>
> Then I built the app for it.
>
> What it does:
> – Log a rejection in 5 sec (category, title, note)
> – Stats card (total, last, top categories, streak)
> – Share screen with the 🤠 frame ("turn that frown upside down")
> – Tip jar ($0.99 ☕️ / $2.99 🍕 / $9.99 🎉) — completely optional
> – No sign-in. No subscription. Data on-device. Open source on GitHub.
>
> Built with SwiftUI + SwiftData + StoreKit 2 + Parra.
>
> Three things I want feedback on:
> 1. Is the 🤠 too cheerful?
> 2. Should we add App Review-specific fields (guideline number, reviewer name)?
> 3. $2.99/yr Pro tier (export, widgets, custom icons) — right move or betrayal of the free-forever brand?
>
> Drop your wildest rejection of 2026 in the comments and I'll add the funniest one to the demo data.
>
> Open source: github.com/Parra-Inc/rejected-ios
> Hello: rejected.app

### During-launch playbook

| Hour | Action |
|---|---|
| 0:00 | Launch goes live (PT midnight) |
| 0:05 | Maker comment posted |
| 0:30 | DM your 30 first-hour upvoters with the link |
| 1:00 | First X update — "Live on PH 🎉 [link]" |
| 6:00 | X update with current rank |
| 9:00 | Founder live in PH comments — respond to every comment <30 min |
| 12:00 | Lunchtime X update |
| 16:00 | Founder offers TestFlight invites to PH commenters |
| 19:00 | "8 hours left, currently #X" rallying post |
| 23:30 | Final push tweet |
| 24:00 | Launch closes. Capture final rank. |

### Success bar

- Top 5 of the day → great
- Top 10 → solid, expected
- Top 20 → average
- Outside top 20 → do not relaunch within 90 days

If we hit top 5, PH features us in their daily and weekly newsletters — that's another 1K–5K visits over the following week.

---

## 6. Indie Hackers Launches

IH has a Launches surface separate from the main feed. Lower-volume than HN/PH but high-quality audience.

- Submit within 24h of PH/HN launch
- Title: "Rejected — collect rejections like trophies"
- Description: identical to PH description
- Upvotes from the IH community (the same crowd we engaged in plan §4.4)
- The IH Launches feature surfaces in Channing's weekly newsletter if it lands

---

## 7. Hacker Newsletter pitch

After Show HN, pitch HN founder/editor:

> Subject: Show HN earlier this week — Rejected (free iOS app for tracking rejections)
>
> Hey [name] — I'm the founder of Rejected, a free iOS app for tracking rejections (App Store, YC, jobs, investors). Show HN earlier this week hit [N] upvotes; the comment thread had some genuinely great responses from indie devs.
>
> If you're looking for an "I built this because I needed it" story for next week's issue, I think the post would resonate with your audience.
>
> Show HN: [link]
> App Store: [link]
>
> Happy to write a custom 100-word blurb if useful.
>
> – [founder]

---

## 8. Per-launch creative checklist

| Asset | Spec | Where used |
|---|---|---|
| App icon | 1024×1024 PNG | App Store, PH, IH |
| 5 portrait screenshots | 1290×2796 (iPhone 17 Pro) | App Store |
| Hero image | 1080×1080 PNG | PH gallery, share previews |
| Demo GIF | 800×600, <5 sec, <8MB | PH gallery, marketing site |
| Maker portrait (optional) | 400×400 | PH maker card |
| Open Graph card | 1200×630 | Marketing site, link previews |
| 60-sec demo video | 1080p, captions burned in | PH gallery, marketing site landing |

Build all assets once during pre-launch week. Reuse for every subsequent launch with minor tweaks.

---

## 9. Re-launch playbook (Month 3–4 and Month 6)

Each re-launch needs a **new hook** — we can't re-launch v1.0. Acceptable hooks:

| Hook | Reason for re-launch |
|---|---|
| Pro tier ships | "Rejected adds 'Founder Mode' and 'Job Mode' field templates" |
| Year-in-Rejection export | "Generate your personal Year in Rejection report" (Spotify-Wrapped-style image) |
| Localization | "Now in 10 languages" (Jia Jiang's TED talk is in 39 — partial overlap is a real story) |
| Widgets | "Rejection widget on your home screen" |
| Apple Watch app | If we ship one — strong PH hook |
| 10K rejections logged | "Public data report — what 14,000 people taught us about rejection" |

Each re-launch should hit:
- Product Hunt re-launch (PH allows once per major version)
- Show HN with the new feature (but not re-pitching the same product)
- IH Launches re-submission
- Newsletter pitch

---

## 10. Measurement

| Metric | Source | v1.0 target | Re-launch target |
|---|---|---|---|
| Show HN upvotes | HN | 150+ | n/a (skip if no new tech angle) |
| PH rank (day of) | PH | Top 5 | Top 10 |
| Total launch-day visits | Plausible | 8K | 4K |
| Launch-day installs | App Store Connect | 500 | 300 |
| Launch-week installs | App Store Connect | 1,500 | 1,000 |
| Newsletter pickups | Manual | 3 | 2 |
| Tip-jar conversions launch week | App Store Connect | 30 | 15 |
| Followers added (X) launch week | X analytics | 500 | 200 |

---

## 11. Anti-patterns

- **Don't launch on a Monday or Friday.** Tuesday/Wednesday/Thursday are PH peaks. HN is fine any weekday but Tuesday 8am PT is best.
- **Don't pitch press the same day.** TC, The Verge, etc. ignore launch-day pitches. Pitch them with a "we just launched and here's what we learned in week 1" angle on Day 7.
- **Don't ring-vote.** Both HN and PH detect and demote. The 30 first-hour upvoters must vote organically (logged in from their own IP/device).
- **Don't pre-launch on PH without telling your hunter.** They lose ranking if you frontrun their post.
- **Don't run paid launches.** PH offers a "boost" — skip. Paid traffic doesn't compound the way organic does.
- **Don't launch a v1.0.1 the day after PH.** Save the next launch for a substantial new hook 90+ days out.
- **Don't ignore comments to chase a "rank" goal.** Comment response quality drives sustained PH placement, and is what wins the Hacker Newsletter pitch the next week.
- **Don't pitch every blog under the sun.** Five well-targeted, personalized pitches beat fifty cold press blasts.

---

## 12. The single-tweet pre-launch checklist

48 hours before launch, do this:

- [ ] App is on App Store live ✅
- [ ] rejected.app is up with all 5 screenshots and a working App Store deep link
- [ ] PH ship page has 100+ upvote pledges
- [ ] 5 HN friends notified for 8am PT Tuesday
- [ ] PH hunter (if not founder) briefed and ready
- [ ] All 7 Rejection Week seed posts written
- [ ] Show HN post saved as draft
- [ ] Maker comment saved as draft
- [ ] Launch-day calendar blocked end-to-end
- [ ] Wife/family/cat informed you'll be unreachable Mon-Tue
- [ ] Coffee
