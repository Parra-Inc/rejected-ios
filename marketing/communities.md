# Rejected — Communities Playbook

> Indie Hackers, Reddit (segment-specific subs), Hacker News (Show HN), WIP.co, lit mag forums, Discord servers. Pre-existing concentrations of our audience. Long-form sincerity converts at 10x ad rate.

---

## 1. Why communities are rank #2

Each community below already hosts a dense concentration of one or more of our segments. They reward earnest, specific, useful, long-form content — which is exactly the brand voice. And every community post can produce a one-day install spike PLUS a six-month long tail in search.

The cost is **founder time and reputation**, not dollars. Both are bounded by good behavior — show up, be helpful, give before you take, do not spam.

---

## 2. Community map

| Community | Segment fit | Audience size | Founder effort | Best format |
|---|---|---|---|---|
| **Indie Hackers** | Seg 1 (indie hackers) | 200K+ active | High — be present weekly | Launch post, milestone updates, AMA, sponsored newsletter |
| **Hacker News (Show HN)** | Seg 1 + 3 | 5M+ daily readers | Very high one-shot | Show HN post (Tuesday 8am PT), comment response marathon |
| **Lobste.rs** | Seg 1 (deep tech) | 50K daily | Low | Cross-post Show HN with `show` tag |
| **r/SideProject** | Seg 1 | 100K members | Low–medium | Launch post + GitHub link, App Store in comments |
| **r/IndieDev** | Seg 1 | 50K members | Low | Launch + monthly milestone |
| **r/iOSProgramming** | Seg 1 (dev-deep) | 70K | Medium | Technical writeup angle (SwiftUI + SwiftData + Parra integration) |
| **r/cscareerquestions** | Seg 2 (job seekers) | 1M+ members | High — must follow self-promo rules | Helpful long-form post, link in comments |
| **r/jobs** | Seg 2 | 2M members | Medium | Personal story post, free tool in body |
| **r/recruitinghell** | Seg 2 | 500K | Medium | Screenshot-driven post |
| **r/layoffs** | Seg 2 | 100K | Medium | Direct, sincere, "I built this because I needed it" |
| **r/Entrepreneur** | Seg 3 (founders) | 4M | Medium | Investor-pass story post |
| **r/startups** | Seg 3 | 1M | Medium | YC-rejection angle |
| **r/writing + r/PubTips** | Seg 4 (writers) | 3M / 200K | High — strict self-promo rules | Submission-tracker comparison post, mention in comments only |
| **r/getmotivated** | Seg 5 (rejection therapy) | 17M | Medium | Jia Jiang TED talk anchor |
| **r/decidingtobebetter + r/selfimprovement** | Seg 5 | 1.5M / 2M | Medium | 100-day challenge angle |
| **WIP.co** | Seg 1 (build-in-public) | 5K dedicated | Medium — daily updates required | Daily progress log for 30 days |
| **MicroConf Slack** | Seg 1 (founders) | 5K | Medium — be a member, contribute | Helpful contributions; mention only when relevant |
| **iOS Dev Happy Hour Discord** | Seg 1 | 5K+ | Low | One-time launch announcement, App Review channel chats |
| **RevenueCat Discord** | Seg 1 | 10K | Low | App Review channel, Parra/SDK channel |
| **Indie Apps Catalyst Discord** | Seg 1 | 5K | Low | Launch announcement, weekly engagement |
| **Sub Club Substack community** | Seg 4 (writers) | 10K subs | Low | Newsletter swap pitch (see channels.md) |
| **NYC Midnight Discord** | Seg 4 | 5K | Low | Annual contest cycles — pitch then |
| **OnDeck Slack (paid)** | Seg 3 | 5K+ | Medium | If founder is already a member; otherwise skip |

---

## 3. Indie Hackers playbook

IH is the highest-quality concentration of segment 1. Audience is small but every reader builds an app.

### The IH launch post (Day 0)

Use this verbatim or close. Pin in `#showcase`.

> **Title:** I built an iOS app for the part of indie hacking nobody talks about
>
> **Body:**
> Show me an indie hacker and I'll show you someone with a folder of rejection emails. App Review. Stripe. Plaid. App Store features that didn't happen. Product Hunt finishes that weren't #1. Investor passes. YC rejections. Tweets that died at 12 impressions.
>
> Every shipped app rides on a mountain of no's.
>
> I just shipped **Rejected** — a free iOS app for logging the no's. Pick a category, give it a title, drop a note. Stats card. Share screen. Tip jar. That's it.
>
> Built on:
> – SwiftUI + SwiftData
> – StoreKit 2 for the tip jar
> – Parra (open-source SDK we maintain — handles auth, feedback, roadmap, changelog)
>
> Open source: github.com/Parra-Inc/rejected-ios
> App Store: [link]
>
> Why I made it: I needed it. After 11 App Review rejections and 47 investor no's, I needed somewhere to put them where they felt like accomplishments instead of failures.
>
> Three things I want feedback on:
> 1. Should the share screen post directly to X / LinkedIn or stay as a generic ShareLink?
> 2. Tip jar at $0.99 / $2.99 / $9.99 — right ladder?
> 3. Would a $2.99/year Pro tier (CSV export, widgets, custom icons) feel right or would it betray the brand?
>
> Drop your wildest rejection in the comments and I'll add the funniest one to the demo data.

### Ongoing IH presence

- **Weekly milestone post** on the milestones board ("100 installs!" "1K installs!"). Each one is a tiny launch.
- **Daily comments** on other people's threads — 3–5/day, substantive.
- **Monthly AMA pitch** — "I'm the founder of Rejected. AMA about open-sourcing a SwiftUI app and the marketing playbook." Cross-promotes Parra SDK.
- **Weekly Roundup pitch** — email Channing Allen / current editor: "Indie hacker built an app for the rejections you all post about. Free. Open source. Built on Parra."
- **One sponsored newsletter** at launch — $500–1,500, one-time. Test rate.

### Heroes to engage on IH

- @csallen (founder)
- @rosiesherry (community)
- @mijustin
- @marc_louvion
- @yongfook
- @KP

---

## 4. Hacker News — Show HN

Single highest-leverage one-shot in the whole plan. Front page = 5K+ installs in 24h. Hacker News punishes anything that smells like marketing, so the post must be earnest, technical-adjacent, and lead with the personal story.

### The post

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

### Show HN logistics

| Item | Detail |
|---|---|
| **Timing** | Tuesday 8:00 AM Pacific (peak HN intake) |
| **Pre-coordination** | 5 friends agree to upvote organically in first 30 min (don't ring) |
| **Comment response** | Founder answers every comment within 1 hour for the first 6 hours, every 2 hours for the next 6 |
| **Cross-post same day** | Lobste.rs (Show tag), r/SideProject, r/iOSProgramming, r/swift, IH #showcase |
| **Heroes to notify (heads up, not ask)** | @dang (mod awareness), @mijustin, @marc_louvion, @stevemoser, @csallen |
| **Success bar** | 150+ upvotes, front page top half, 5K visits to rejected.app, 500 installs in 48h |

If the post doesn't hit front page by hour 4, do not re-submit. Wait 90 days, rewrite with deeper personal narrative, resubmit.

---

## 5. Reddit playbook (per-sub)

Reddit rules vary by sub. **Read each sub's self-promo rules before posting.** Most allow a free tool if the post is substantive and the link is in a comment, not the title.

### Posting rotation (one post/week)

| Week | Sub | Post template |
|---|---|---|
| 1 | r/SideProject | "I built an iOS app for collecting rejections like trophies (open source)" — short post, GitHub in body, App Store in comments |
| 2 | r/cscareerquestions | "Free iOS app I built for the layoff cycle — track every job rejection, no sign-in" — sincere, helpful, link in comments |
| 3 | r/Entrepreneur | "I logged every investor rejection for 6 months. Here's what I learned (and the free tool I built)." — data post + tool link |
| 4 | r/writing or r/PubTips | "Native iOS submission tracker (free, no sign-in) — alternative to Duotrope shoebox" — comparison post |
| 5 | r/getmotivated | "Jia Jiang gave a TED talk about 100 rejections. I built an app for it. (Free.)" — Jia anchor |
| 6 | r/jobs | "After 87 rejections I started tracking them. Sharing the free tool I built." — personal story |
| 7 | r/recruitinghell | Screenshot-heavy post of your own rejection emails, "logged 47 in 3 months" |
| 8 | r/IndieDev | Milestone post — "1K installs of my open-source Rejected app. AMA." |

### Per-post template

```
Title: [hook] — [free tool / framing]
Body:
[1-paragraph personal story or context — why you built it / what you noticed]

[1-paragraph what the app does, plain English, no marketing voice]

[3 bullet points: what's free, what's optional, what's open source]

[1 paragraph genuine ask for feedback — what would you add / change?]

[Link in a comment if the sub disallows links in body, otherwise direct]
```

### Reddit anti-patterns

- **Never link to App Store in the title.** Auto-flag for spam.
- **Never use marketing voice.** Reddit can smell a press release from orbit.
- **Never DM Reddit users about your post.** Account ban risk.
- **Engage with the sub for 2 weeks before posting.** Build a tiny comment history first. New accounts get auto-removed.
- **Reply to every comment.** Especially the negative ones. Sincerely. The audience watches how you respond.

---

## 6. WIP.co (build-in-public)

WIP is small (~5K active) but the audience is dense with our segment 1. The `#ship` channel celebrates every release; the daily log keeps you top of mind.

### 30-day WIP run (during launch)

- Post 1 update per day for 30 days. Doesn't have to be huge — "shipped v1.0.1 with confetti on the 10th tip" counts.
- Use `#ship` for releases, `#milestone` for install counts.
- Comment on 3–5 other people's updates/day. Reciprocity drives reach.

### What to log

- Daily progress on app features (Pro tier dev, share screen polish, etc.)
- Daily progress on marketing (X follower count, install count, tip count)
- Daily rejection log (eat your own dog food — log a rejection of your own in WIP)

---

## 7. Discord servers

Three servers matter at launch. Each gets a single announcement post and ongoing organic engagement.

| Server | Channel | Announcement copy |
|---|---|---|
| **iOS Dev Happy Hour** | `#show-and-tell` | "Hey all — shipped a free SwiftUI app for tracking rejections, built on @parra. Open source, no sign-in. Would love iOS dev feedback: [link]" |
| **RevenueCat** | `#app-review-hell` (or equivalent) | "Built an app specifically for indie devs getting rejected by App Review. Free, open source. App Review-rejection-specific fields shipping in v1.1. [link]" |
| **Indie Apps Catalyst** | `#shipped` | "v1.0 of Rejected just shipped. SwiftUI + SwiftData + Parra. Open source. Tip jar only. [link]" |

After the announcement, **don't keep posting**. Engage in conversations, help others, mention the app only when contextually useful (e.g., when someone posts an App Review rejection screenshot — "lol logged it on my app").

---

## 8. Niche communities (segment 4 + 5)

### Segment 4 (writers)

- **Sub Club Substack** (Becky Tuch's network) — pitch a newsletter mention with the comparison-to-Duotrope angle
- **Lit Mag News** (also Becky Tuch) — pitch a feature post: "A native iOS submission tracker for the post-Duotrope era"
- **The Submission Grinder forum** — be a useful presence first, mention only in user-help context
- **NYC Midnight Discord** — annual contest cycles; pitch ahead of each contest with the "track your contest submissions" angle
- **Reedsy newsletter** — pitch a guest post on submission tracking

### Segment 5 (rejection therapy)

The community is dispersed across TikTok comments and Reddit. The unlock is **direct creator outreach**, not community posting. See influencer notes in channels.md and email template G1 in plan.md §7.

Best community surfaces:
- r/getmotivated
- r/decidingtobebetter
- Mel Robbins' email list (if she'll trade — long shot)
- Jia Jiang's mailing list (she sells the Rejection Therapy card deck; integration pitch lives here)

---

## 9. Community KPIs (30/90/180)

| Metric | 30 | 90 | 180 |
|---|---|---|---|
| IH launch post upvotes | 50 | (one big post) | re-launch with milestones |
| IH newsletter feature | 0–1 | 1 | 2 |
| Show HN front page | 1 (launch) | 1 (launch only) | 1 re-run if v2 |
| Reddit posts published | 4 | 12 | 24 |
| Reddit post avg upvotes | 50 | 100 | 200 |
| WIP.co daily updates | 30 | 60 | 100 |
| Discord launch announcements | 3 | 3 | 5 |
| Direct community → install rate (UTM-tagged) | 5% of installs | 8% | 10% |

---

## 10. Community anti-patterns

- **Don't drop and run.** Posting and then never responding to comments kills any chance of repeat reach.
- **Don't post in 10 subs the same day.** Cross-posting in close time burns goodwill; mods notice.
- **Don't use the same post body across communities.** Tailor to each sub's audience. r/cscareerquestions and r/Entrepreneur cannot read the same post.
- **Don't pitch the Pro tier in any community post.** The brand at this stage is "free, generous, open source." Pro tier pitches read as bait-and-switch.
- **Don't ban-evade after a removal.** If a sub removes your post, message a mod respectfully, ask why, accept the answer, and don't re-post.
- **Don't try to bribe upvotes.** "Comment your rejection, I'll add to demo data" is fine. "Upvote this and I'll send you a gift card" is not.

---

## 11. The first 7 days (community checklist)

- [ ] Day -7: Make IH, Reddit, HN accounts have a comment history of 10+ helpful comments
- [ ] Day -3: Pre-draft Show HN post, IH launch post, and 5 Reddit variants
- [ ] Day -3: Notify 5 friends who will upvote Show HN organically
- [ ] Day 0 (Mon 8am PT): Show HN post live
- [ ] Day 0 (Mon 8:15am PT): IH launch post live
- [ ] Day 0 (Mon 9am PT): r/SideProject post live
- [ ] Day 0 (all day): Comment response marathon on HN
- [ ] Day 1 (Tue): Lobste.rs cross-post, r/iOSProgramming post
- [ ] Day 2 (Wed): r/cscareerquestions post
- [ ] Day 3 (Thu): r/Entrepreneur post
- [ ] Day 4 (Fri): WIP.co daily updates start (continue for 30 days)
- [ ] Day 5 (Sat): r/getmotivated post (lower competition on weekends)
- [ ] Day 7 (Sun): Discord announcements (iOS Dev Happy Hour, RevenueCat, Indie Apps Catalyst)
- [ ] Day 7 (Sun): Write IH milestone update with first-week install count
