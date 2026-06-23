# Rejected — Marketing Plan

> Collect rejections like trophies.

A pocket trophy case for the no's. Built for indie hackers, job seekers, founders, writers, and anyone running a rejection-therapy challenge. The growth loop is the share screen — every saved rejection becomes a reason to brag in public.

---

## 0. Snapshot

- **Product:** Rejected — iOS app to log rejections (App Store, YC, jobs, investors, dates, lit mags, life). Add a category, title, and note. Get stats (total rejections, last rejection, top categories) and a share screen with copy that turns the frown upside down.
- **Stack:** Swift 6 / SwiftUI / SwiftData / Parra SDK / StoreKit 2 (consumable tips).
- **Pricing:** Free with a tip jar ($0.99 ☕️ / $2.99 🍕 / $9.99 🎉). No subscription. No paywall. No login required (Parra optional auth).
- **Repo:** github.com/Parra-Inc/rejected-ios (open-source SwiftUI/Parra reference app).
- **Bundle:** `com.parra.rejectiontrackerios` (rename pending — see "Naming").

### Why this app, why now

1. **2026 is the year of the rejection.** CNBC ran a feature in January on the "1,000 rejections challenge" — Gabriella Carr's TikTok series that turned into a movement. Jia Jiang's *100 Days of Rejection* TED talk has crossed 10.5M views in 39 languages and the #rejectiontherapy hashtag has 100M+ views on TikTok.
2. **Tech layoffs keep mounting.** layoffs.fyi and Crunchbase both show 138,837+ tech workers laid off in 2026 alone (Oracle alone cut 30K). The Slate piece "I had a dream job in tech everyone wanted" went viral in April. Job seekers are submitting hundreds of applications for 4 responses (Medium, "I Sent 340 Applications Through LinkedIn Easy Apply").
3. **YC rejection is content.** Summer 2025 acceptance hit 0.6% — the lowest on record. 39,800+ apps rejected per cycle. Founders are publishing their YC rejection emails on X for likes.
4. **Indie hackers brag about flop count.** Pieter Levels (@levelsio) openly says "97% of what I ship flops." Marc Lou (@marc_louvion) built his audience on "I got fired everywhere → $47K/mo." The flex is the failure rate.

There is no first-class iOS app for this. Duotrope and Submittable serve writers only and are web-first. The "1,000 rejections" people are using Notes, Google Sheets, and TikTok captions. Rejected is the native, gorgeous, shareable home for the no's.

---

## 1. Positioning

### One-liner
**Rejected — Collect rejections like trophies.**

### Three taglines (use across surfaces)
1. **Get told no on the record.** Every rejection logged is proof you tried.
2. **The trophy case for the no's.** Job rejections, App Store rejections, YC rejections, life rejections.
3. **Rejection is data. Track it.** Then go get one more.

### Elevator
> Rejected is a small iOS app that turns the worst part of doing hard things into a streak you're proud of. Log a rejection in 5 seconds — pick a category, give it a name, drop a note. Get a stats card, a share sheet, and a little dose of "back to work" energy. Free forever. Tip the developer if it made you smile.

### What we are not
- Not a productivity app. No tasks, no goals, no Notion-style bloat.
- Not a journaling app. Rejections only.
- Not a SaaS. No cloud login required, no subscription, no AI summarizer.
- Not a therapist. We are vibes and stats.

---

## 2. Audience segments

We are deliberately niche-stacking. One app, five overlapping tribes, all of whom already share rejection-content for free.

### Segment 1 — Indie hackers shipping fast
- **Who:** Solo devs on X with avatars holding babies or laptops, ship cycles of <2 weeks, audience of 500–50K.
- **Where they live:** X/Twitter "build in public," Indie Hackers, r/SideProject, r/IndieDev, MicroConf Slack, /r/EntrepreneurRideAlong, WIP.co.
- **Their pain:** App Store rejection 4.3 design / 4.0 metadata / 2.1 minimum functionality / 5.1.1 PII. Stripe app review. Product Hunt #4 finish.
- **Existing behavior:** Already posting "DAY 47 — Apple rejected me again 🥲" with screenshots.
- **Our hook:** "Add this rejection to the trophy case. Streak: 12."
- **Heroes to court:** @marc_louvion, @levelsio, @theo (t3.gg), @yongfook, @dvassallo, @anthilemoon, @KP, @mijustin, @rosiesherry, @cjz.

### Segment 2 — Job seekers in the tech layoff wave
- **Who:** Recently laid-off SWEs, designers, PMs, recruiters. The "open to work" crowd on LinkedIn. r/cscareerquestions regulars. People posting "Day 90 of unemployment" updates.
- **Where they live:** LinkedIn (the long-post epicenter), r/cscareerquestions, r/jobs, r/recruitinghell, r/layoffs, Tech Twitter, TikTok career-coach side.
- **Their pain:** 340 LinkedIn Easy-Apply submissions → 4 responses. Ghost interviews. "We've decided to move forward with other candidates" copy-paste rejections.
- **Existing behavior:** Already screenshotting rejection emails for LinkedIn engagement. Already counting applications in Notion.
- **Our hook:** "Log the no. You're closer to the yes."
- **Heroes to court:** @careercoachjoyce (TikTok), @aprilrinne, @hannahmorgan, Liz Ryan, Jeremy Schifeling, @bencjessen, Bonnie Dilber (LinkedIn), Madeline Mann (Self Made Millennial).

### Segment 3 — Founders pitching investors
- **Who:** Pre-seed and seed founders raising. YC applicants, accelerator applicants, anyone with a deck.
- **Where they live:** X, LinkedIn, Visible.vc community, OnDeck Slack, founder Twitter, signal.nfx, foundercollective.
- **Their pain:** "I'm going to pass" emails from 47 investors in a row. The polite no. The radio-silent no.
- **Existing behavior:** Tracking outreach in Airtable / Visible. Tweeting "got my 50th no this week."
- **Our hook:** "Track the no's. Run a tighter raise next time."
- **Heroes to court:** @gtmichaelseibel, @harryhurst, @nikitabier, @JenniferLi (a16z), @bgurley, @amyhoy, @sahillavingia, founder podcasts (Lenny, This Week in Startups, BG2).

### Segment 4 — Writers, artists, creators submitting work
- **Who:** Fiction writers, poets, screenwriters, photographers, journalists, comedians submitting to lit mags, festivals, columns, anthologies.
- **Where they live:** Duotrope, Submittable, The Submission Grinder, r/writing, r/PubTips, Twitter writing community, NYC Midnight Discord, Reedsy.
- **Their pain:** Submission shoebox. 80% form-letter rejections. No iOS-native tracker.
- **Existing behavior:** Color-coded Google Sheets. Duotrope's web tracker. Some still use paper.
- **Our hook:** "A rejection a week. A submission a day. Native, beautiful, fast."
- **Heroes to court:** Becky Tuch (Lit Mag News), @litmaglab, @anneanthropy, @kjdellantonia, Submission Grinder, The Sub Club Substack.

### Segment 5 — Rejection therapy challengers
- **Who:** People deliberately seeking rejection. The Jia Jiang reading group. Gabriella Carr followers. 100 / 365 / 1,000 day challenge people.
- **Where they live:** TikTok (#rejectiontherapy 100M+ views), YouTube, Instagram Reels, r/decidingtobebetter, r/selfimprovement, r/getmotivated.
- **Their pain:** No way to track 100 days of rejection in one place. Currently using their camera roll.
- **Existing behavior:** Posting daily rejection clips to TikTok.
- **Our hook:** "The official tracker for your 100-day challenge."
- **Heroes to court:** Jia Jiang directly (jiajiang.com — he sells a Rejection Therapy deck!), Gabriella Carr (TikTok 1,000 rejections), Mel Robbins, Sahil Bloom, James Clear, Tim Ferriss community.

---

## 3. Naming, store listing, App Store optimization

### Naming
The repo and bundle use `RejectionTrackerIosApp` / `com.parra.rejectiontrackerios`. Ship the App Store name as:

- **Display name:** `Rejected`
- **Subtitle:** `Collect rejections like trophies`
- **Promo text:** `Job rejections, App Store rejections, YC rejections, life rejections — track every "no" and share the wins.`

### App Store keywords (100 char limit)
```
rejection,job tracker,rejection therapy,journal,career,layoff,job search,indie hacker,startup,founder
```

### Long description (drop into ASC)
> Every "no" is proof you tried. Rejected is the trophy case for your rejections — App Store rejections, job rejections, YC rejections, investor passes, lit mag form letters, and the everyday no's that come with shipping work in the world.
>
> Log a rejection in 5 seconds. Pick a category (or make your own — Job, Investor, YC, Romantic, College, Apple Review, anything). Add a title. Add a note. Watch your stats grow.
>
> Built for the people who keep going:
> • Indie hackers getting rejected by App Review
> • Job seekers running through the layoff gauntlet
> • Founders pitching investor #87
> • Writers submitting to lit mags
> • Anyone running Jia Jiang's 100-day rejection challenge
>
> Free forever. No subscription. No sign-in required. Tip the developer if it made you smile.
>
> Made with 🖤 by Parra. Open source on GitHub.

### What's New (launch)
> v1.0 — Rejected is live. Log your no's, see your stats, share the streak. Built for the rejection-therapy era.

### Categories
- Primary: **Productivity**
- Secondary: **Lifestyle**

### Screenshots (5, portrait, iPhone 17 Pro)
1. **Headline shot.** Stats card showing "Total Rejections 147 · Last Rejection: 2 hours ago · Top: Job 64 / Investor 31 / App Review 22." Caption: **"Collect rejections like trophies."**
2. **Add flow.** Category picker open (YC, Job, Investor, App Review, Romantic, College). Caption: **"Log a no in 5 seconds."**
3. **Share screen.** The 🤠 cowboy frame with "Turn that frown upside down." Caption: **"Brag about the grind."**
4. **History list.** A long, dense feed of rejections. Caption: **"Receipts for every attempt."**
5. **Tip jar.** ☕️ 🍕 🎉. Caption: **"Free forever. Tip if it helps."**

---

## 4. Five marketing initiatives

The 80/20: Initiative 1 (Rejection Week) is the unlock. Everything else compounds off it.

---

### Initiative 1 — "Rejection Week" social event

A one-week, hashtag-driven challenge built for organic share velocity. This is the launch.

**The premise:** From Monday to Sunday, share one rejection per day. Anything counts. Tag #RejectionWeek and (optionally) the app. The single most public rejection wins a $500 prize and gets featured.

**Mechanics:**
- Pre-week: pre-write seven post templates ourselves (job rejection, App Store rejection, investor pass, college rejection, dating rejection, contest rejection, "polite no" from a customer). Post them ourselves Day -7 through Day -1 to seed the format.
- Day 0: launch post — "It's #RejectionWeek. Share 1 rejection a day for 7 days. Public ones get the most love. I'll repost the best."
- Daily: quote-retweet the best 5 posts each day on X, share top 3 to LinkedIn, top 3 to Instagram Stories.
- Friday: feature the wildest rejection in a thread.
- Sunday: announce the winner; ship a v1.0.1 update with their rejection seeded in the demo data ("inspired by @username").

**Why it works:** This format already exists. People share rejections for engagement. We're just naming it, putting a hashtag on it, and giving them an app to log inside. The TikTok #rejectiontherapy hashtag proves the demand.

**Distribution channels:**
- X: 3 posts/day from main account + 7 friends willing to amplify Day 1.
- LinkedIn: long-form post Day 1 — "Why I'm running Rejection Week" (job-seeker angle).
- Indie Hackers: forum post Day 1 — "Rejection Week is on — share your App Store rejections."
- Reddit: r/SideProject (Day 1), r/Entrepreneur (Day 3), r/jobs (Day 4), r/writing (Day 5), r/cscareerquestions (Day 6).
- TikTok: 7 short videos, one per day, reading the funniest rejection submitted to that day's hashtag.
- Newsletter swap: pre-arrange mentions in Indie Hackers (Saturday digest), Newsletter for Founders (@nathanbarry crowd), Lit Mag News (Becky Tuch), Sub Club.

**KPIs:**
- 500 #RejectionWeek posts by Sunday across X + LinkedIn.
- 10K App Store impressions Mon–Sun.
- 1K installs (rough target — Rejection Week posts → app icon awareness → search install).
- 1 piece of press pickup (TechCrunch / The Verge / Fast Company is unrealistic; aim for an indie founder podcast, Indie Hackers homepage feature, Hacker Newsletter mention).

---

### Initiative 2 — App Store rejection support (content marketing for iOS devs)

The fastest growth surface inside our own audience: indie iOS devs who get rejected by App Review every week and tweet about it.

**The content engine:**
- "Apple Rejected My App Today" weekly blog post on a marketing subdomain (rejected.app/log). Each post documents a real App Review rejection sent by a real dev (with permission), then ends with: "Logged in Rejected."
- "Guideline of the Week" — short SEO posts for `4.3 design spam`, `2.1 minimum functionality`, `5.1.1 data collection`, `4.0 design`, `4.5.4 push abuse`, `3.1.1 IAP for digital content`. These are some of the highest-volume App Review search terms. Source: Appcircle's "Top App Store Rejections" piece is on page 1 for these and gets ranked organically.
- "Indie Dev Rejection Wall" — a public page (web) that shows community-submitted App Review rejection emails (redacted). Updated weekly. Each entry has a "Log this in Rejected →" button. Becomes the de-facto reference page for "what does an Apple rejection look like."

**Distribution:**
- Each post: post to X with a screenshot, cross-post to Indie Hackers, syndicate to dev.to and Hashnode.
- Outreach to App Review newsletter (@stevemoser, RevenueCat blog, Adapty blog, Phiture). Pitch one guest post to RevenueCat on "We surveyed 100 indie devs about App Store rejection."
- App Review Discord servers (RevenueCat's, Indie Apps Catalyst, iOS Dev Happy Hour).

**Heroes to court (real handles):**
- @stroughtonsmith (Steve Troughton-Smith)
- @mhdhejazi (Adapty)
- @jacobeiting (RevenueCat founder)
- @david_smith (Underscore David)
- @christianselig (Apollo founder — famously rejected/killed)
- @gruber (Daring Fireball, long shot)
- @PaulHudson (Hacking with Swift)
- @AlexHay (Indie Apps Catalyst)

**KPIs:** 5 posts in 4 weeks. 10K cumulative blog reads. 500 backlinks/clicks to App Store from rejected.app. 50 community-submitted rejections in the public wall by week 8.

---

### Initiative 3 — LinkedIn long-post empire (layoff / job-seeker angle)

LinkedIn is the largest unlock and the most underpriced. Tech-layoff posts routinely hit 1M+ impressions in 2026. Our angle is sincere, not snarky.

**Cadence:** Three long-form posts per week from the founder account, plus daily engagement on layoff-themed posts.

**Post templates (5 evergreen formats):**

1. **Counter-intuitive frame.** "I'm jealous of people with 50 job rejections. Here's why."
2. **Tactical receipt.** "I tracked every job rejection for 90 days. The pattern that emerged."
3. **Vulnerable founder post.** "I got rejected from 23 jobs before I started my own thing. Here are all 23."
4. **Service post.** "I built a free iOS app for the 138,837 of us laid off in 2026. No sign-in. No subscription. Just log the no's. [link]"
5. **Community spotlight.** "@bonniedilber posted yesterday about 100 applications, 4 responses. Here's what I'd track to find your signal: [thread]"

**The grand-slam post (week 2):** "I asked 100 laid-off engineers how many rejections they had. The median was 67. Here's the histogram." Pair with a screenshot of the Rejected stats card filled in with the median. This is the share-bait post.

**Heroes to court / engage with daily (real handles):**
- Bonnie Dilber (Talent Acq leader at Zapier, 600K+ LinkedIn)
- Liz Ryan (Human Workplace)
- Madeline Mann (Self Made Millennial)
- Jerry Lee (Wonsulting)
- Adam Grant (long shot — he loves the rejection-therapy angle, has written about Jia Jiang)
- Justin Welsh (LinkedIn solopreneur archetype)
- Hannah Morgan (Career Sherpa)
- Andrew Yeung (NYC tech events)
- Lara Acosta (LinkedIn growth)
- Tessa White (The Job Doctor)

**Cold DMs (10/week):** Personal note to laid-off tech workers actively posting. "Saw your post — I built a free app for tracking exactly what you're going through. No catch, no email. Just a link. Would love your feedback if you try it: [link]." Goal is 1 reply in 10 → ambassador.

**KPIs:** 100K LinkedIn impressions/month. 1 post above 100K. 500 followers added/month. 200 app installs from LinkedIn directly (tracked via UTM on rejected.app/li).

---

### Initiative 4 — Indie Hackers community partnership

IH is still the highest-quality concentration of our segment 1 audience (indie hackers). The audience is small but every reader builds an app.

**The play:**
1. **Launch post on IH:** "I built an app for tracking rejection (it's open source on top of @parra)." Long-form. Include the share image. Pin in #showcase.
2. **Weekly Roundup pitch:** Email Channing Allen / James Beshara / current IH editor with the angle: "Indie hacker built an app for the rejections you all post about anyway. Free. Open source. Built on Parra."
3. **Sponsor a single IH newsletter:** $500–1,500 depending on current rates. One-time.
4. **IH milestone posts:** Post every install milestone (100, 1K, 10K) with "here's what worked" transparency. The IH crowd rewards that.
5. **Friday Q&A:** Volunteer to host an AMA — "I'm the founder of Rejected. AMA about open-sourcing a SwiftUI app and the marketing playbook." Cross-promotes the Parra SDK too.
6. **WIP.co partnership:** Post daily progress on wip.co for 30 days. WIP's audience is dense with indie devs and the #ship channel celebrates each release.

**Heroes to court:**
- @csallen (Indie Hackers founder)
- @rosiesherry (IH community)
- @mijustin (Justin Jackson, MegaMaker)
- @marc_louvion (Marc Lou)
- @yongfook (Bannerbear)
- @jonpalmer (WIP.co)
- @KP (Kevon — Marketing for Engineers)

**KPIs:** Top-10 on IH for launch week. 200 IH-driven installs. 1 weekly-roundup feature.

---

### Initiative 5 — Show HN launch with a personal rejection story

Hacker News is unpredictable but the right post can deliver 5K+ installs in 24 hours. The angle has to be earnest, not promotional.

**The post:**

> Show HN: I built an iOS app for collecting rejections like trophies
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

**Launch timing:** Tuesday 8:00 AM Pacific (peak HN). Coordinate 5 friends to upvote in the first 30 minutes (organic, no rings). Respond to every comment within 1 hour for 6 hours.

**Cross-post same day to:**
- Lobste.rs (Show)
- r/SideProject (Show post)
- r/iOSProgramming
- r/swift
- Indie Hackers #showcase
- Reddit r/Entrepreneur
- HN sub-comments on relevant "App Store rejection" / "layoff" stories from the week

**Heroes to amplify:** ping (with no ask, just a heads-up) — @dang (HN mod, for awareness), @mijustin, @marc_louvion, @stevemoser, @csallen.

**KPIs:** Front page of HN (≥150 upvotes). 5K visits to rejected.app. 1.5K App Store impressions. 500 installs in 48 hours.

---

## 5. Channel-by-channel cadence

| Channel | Frequency | Owner | Format |
|---|---|---|---|
| X / Twitter | 3/day | Founder | 1 build-update, 1 rejection screenshot, 1 reply-storm in @marc_louvion / @levelsio threads |
| LinkedIn | 3/week long form, 5/day engagement | Founder | Layoff angle, job-seeker angle, founder vulnerability |
| Indie Hackers | 1 post/week + daily comments | Founder | Build updates, milestones, helpful threads |
| Reddit | 1 post/week (rotate subs) | Founder | r/SideProject, r/IndieDev, r/cscareerquestions, r/jobs, r/Entrepreneur, r/writing, r/PubTips, r/getmotivated |
| TikTok | 3 short videos/week | Founder | "POV: opening Rejected app after the 23rd no" / "Day 47/100 rejection therapy" / reading viewer-submitted rejections |
| Newsletter | 1 swap/month | Founder | Sub Club, Lit Mag News, Newsletter for Founders, Indie Hackers digest, Bootstrapped Founder |
| YouTube creators | Pitch 5/month | Founder | Theo (t3.gg), Marc Lou, ThePrimeagen, Sean Allen, Paul Hudson — "review my SwiftUI app" |
| Podcast pitches | 2/month | Founder | Indie Hackers, Bootstrapped Founder, Build Your SaaS, Out of Beta, Career Contessa, Free Time |
| Email outreach | 10 DMs/week | Founder | Laid-off creators, writer-tracker users on Duotrope forums, YC reapplicants |

---

## 6. Pricing strategy

### Today
- **Free forever.** Full app.
- **Tip jar:** $0.99 ☕️ / $2.99 🍕 / $9.99 🎉 (consumable IAPs already shipped — `v1.tip.1`, `v1.tip.3`, `v1.tip.10`).
- **Login:** Parra `ParraOptionalAuthWindow` — no login required. Data lives in SwiftData on device.

### Why this is right for now
The premise of the app is generosity. Charging would betray it. The audience is people in a low-resource moment (laid off, between rounds, getting rejected). A subscription would be the wrong note.

The tip jar is on the share screen — the moment of catharsis after logging a no. That's the right trigger. ShareView.swift already does this.

### Future "Pro" experiment (post-10K MAU)
Consider an optional Pro tier at **$2.99/year** (annual only, deliberately under the noise threshold). Pro unlocks:
- CSV/PDF export of your rejection log (great for "year in review" posts)
- Custom category icons + colors beyond the default emoji/favicon set
- Widgets (count, last rejection time, streak)
- iCloud sync across devices
- "Founder mode" — pitch tracking fields (investor name, check size, stage)
- "Job mode" — application tracking fields (company, role, salary band, recruiter)

Keep all core features free forever. Pro is for power users. Forecast: 2–3% conversion of MAU at $2.99/yr is sustainable side-project revenue without changing the brand.

### Anti-patterns we will not do
- No paywall on the home screen.
- No "premium share frames."
- No ads.
- No login requirement.
- No upsell modal on first open.

---

## 7. Ads library

Copy and screenshot specs for each post. Use these verbatim or as templates.

---

### A. X / Twitter — viral templates

**A1. The screenshot reply-bait.**
> Apple rejected my app for the 11th time.
>
> Guideline 4.3 — "design spam" — on an app that didn't exist before I built it.
>
> Logged in Rejected. Streak: 11.
> [screenshot of stats card]

**A2. The flex.**
> 0 yeses this week
> 14 no's logged
>
> Best week of the year.

**A3. The Marc Lou format.**
> indie hackers: how many App Store rejections this year?
>
> me: 17 🥲
>
> reply with yours, I'll add the highest to the demo data of my app

**A4. The list post (high RT).**
> Things I tracked in 2026:
> – 87 investor passes
> – 64 job rejections
> – 11 Apple rejections
> – 3 YC rejections
> – 1 polite no from my mom on a co-sign
>
> All of it in one place: [link]

**A5. The Jia Jiang nod.**
> Jia Jiang spent 100 days asking for rejection and gave a 10M-view TED talk about it.
>
> Most of us get 100 rejections without trying.
>
> The least we can do is log them.

**A6. The Levels.io format.**
> 97% of what I ship flops.
>
> 100% of what I ship gets logged.

**A7. The Build-in-public daily.**
> Day 32 building Rejected (open source SwiftUI app for tracking rejections):
>
> Today: tip jar polish. 99¢ ☕️ / $2.99 🍕 / $9.99 🎉
> Open rate on share screen: 41%.
> Tips received yesterday: 4.
>
> Building in public.

---

### B. LinkedIn long-form posts

**B1. The vulnerable founder.**
> I got rejected from 23 jobs before I started my own thing. Here are all 23.
>
> 1. Senior iOS — Stripe (no response, 2024)
> 2. Staff Engineer — Notion (rejected after take-home)
> 3. Founding Engineer — Vercel (final round, "not the right fit")
> 4. iOS — Airbnb (auto-rejected)
> 5. Tech Lead — Linear (closed the role)
> ... [continue with 18 more]
>
> What I learned:
>
> • The rejection volume is a feature of effort, not a bug of you.
> • "Not the right fit" almost never means what you think.
> • Tracking the no's takes the sting out. Each one becomes data.
> • The 24th try was a yes. I started a company. We make a free iOS app for tracking exactly this.
>
> If you're job-hunting in 2026: keep going. Log the no's somewhere you can see them. They are proof you tried.
>
> Free app, no sign-in, no subscription: [link]

**B2. The data post.**
> I asked 100 laid-off engineers how many job rejections they'd had since October.
>
> Median: 67.
> Mean: 92.
> Max: 340.
> Min: 4 ("I gave up").
>
> Median number of "we'll keep you in mind" emails per person: 12.
> Median number of ghost interviews: 3.
>
> If 67 feels like a lot — it's the middle of the pack.
>
> If you've sent fewer than 30 applications, the data says you haven't really started.
>
> If you've sent more than 200, take a break for a week.
>
> [image: histogram screenshot from Rejected app]
>
> I built a free iOS app to track this. Comments below.

**B3. The reframe.**
> Stop counting the jobs you applied to.
> Start counting the rejections you collected.
>
> "Applied" is an aspiration.
> "Rejected" is a receipt.
>
> Receipts compound. Aspirations evaporate.
>
> [link to Rejected app]

**B4. The service post (linkbait, on-brand).**
> 138,837 tech workers were laid off in 2026.
>
> I'm one of them. So I built a free iOS app to track rejections, because I needed it.
>
> No sign-in. No subscription. No data leaves your phone unless you choose to share.
>
> If it helps one person feel less alone in the rejection pile, the build was worth it.
>
> Link in comments.

---

### C. Show HN draft (already drafted above in Initiative 5)

Use the version in §4.5 verbatim. Post Tuesday 8:00 AM PT.

---

### D. Indie Hackers long-post

> **I built an app for the part of indie hacking nobody talks about.**
>
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

---

### E. Reddit posts (per sub)

**E1. r/SideProject**
> Title: I built an iOS app for collecting rejections like trophies (open source)
> Body: [short version of the IH post. Direct link to GitHub. Link to App Store in comments per sub rules.]

**E2. r/cscareerquestions**
> Title: Free iOS app I built for the layoff cycle — track every job rejection, no sign-in
> Body: Hey r/cscareerquestions, I'm a laid-off iOS dev. I built a free app for the rejection pile because I needed it. No subscription, no sign-up, nothing leaves your phone. [link]. Happy to take feedback. AMA about App Review or job-search rejection tracking.

**E3. r/jobs**
> Title: After 87 rejections I started tracking them. Sharing the free tool I built.
> Body: Long-form, sincere, mention 340 applications → 4 responses, link in comments.

**E4. r/Entrepreneur**
> Title: I logged every investor rejection for 6 months. Here's what I learned (and the free tool I built).
> Body: List of patterns — "polite passes are 80% of replies, no-replies are 60% of total." Tool link in body.

**E5. r/writing**
> Title: Native iOS submission tracker (free, no sign-in) — alternative to Duotrope shoebox
> Body: For fiction/poetry submitters specifically. Compare to Duotrope and The Submission Grinder. Note the rejection-as-trophy framing.

**E6. r/getmotivated**
> Title: Jia Jiang gave a TED talk about 100 rejections. I built an app for it. (Free.)
> Body: Quote his stat (10.5M views, 100M+ hashtag views), credit him, link to app, link to his TED talk.

---

### F. TikTok scripts (15-30 sec)

**F1.** "POV: you open Rejected on the morning after Apple kills your app for the 11th time." [Open phone, tap +, choose 🍎 Apple Review, type 'Guideline 4.3', save, stats card jumps from 10 → 11, fade out with 🤠 share screen.]

**F2.** Reading viewer rejections. "Y'all sent these in. Here are my top 3 rejection stories of the week." [Read three submitted no's, log each one in the app on screen.]

**F3.** Day 47/100 of rejection therapy. "Today I asked the barista for a free refill of espresso. She said no. Logged." [App reaction shot.]

**F4.** Dueting Jia Jiang's TED clip. "He did 100. We're going to do 1,000. Track it here." [Show the stats card hitting 100, then 500, then 1000 — fake demo data.]

**F5.** Layoff support. "If you were laid off this year, this app is for you. It's free. No catch." [30 second sincere talking head + app demo.]

---

### G. Email outreach templates

**G1. To creators (Jia Jiang, Gabriella Carr, Madeline Mann, Marc Lou).**
> Subject: built you something
>
> Hi [name],
>
> I'm a big fan of [specific work]. I built a free iOS app for tracking rejections — partly inspired by [their thing]. No catch, no sign-in, no money for me unless someone tips.
>
> If it would be useful for [your audience / your 100-day project / your followers], I'd love to send you a TestFlight link and hear your honest take. If not, no worries — wanted you to have it either way.
>
> [link]
>
> – Ian

**G2. To newsletter operators (Sub Club, Lit Mag News, Newsletter for Founders, Bootstrapped Founder).**
> Subject: rejection-tracking iOS app for [your readers]
>
> [Brief intro. One-line on app. Two angles for their audience. Offer a discount, an interview, or a co-branded post. Don't ask for inclusion — ask "is this interesting to you?".]

---

## 8. Metrics & milestones

### Vanity → real

| Metric | 30 days | 90 days | 180 days |
|---|---|---|---|
| App Store installs | 1,500 | 8,000 | 30,000 |
| MAU | 600 | 3,500 | 14,000 |
| Tips received | 30 | 200 | 800 |
| Tip revenue | $90 | $600 | $2,400 |
| Newsletter signups (on rejected.app) | 200 | 1,500 | 6,000 |
| #RejectionWeek mentions | 500 | 1,500 | 4,000 |
| X followers | +500 | +3,000 | +10,000 |
| LinkedIn followers | +500 | +4,000 | +15,000 |
| Press / pod / newsletter mentions | 3 | 12 | 30 |
| App Store rating | 4.6 | 4.7 | 4.7+ |

### Health metrics
- Share screen open rate after first save: ≥45%
- D7 retention: ≥25% (low for a utility, fine for rejection-tracking — usage is event-driven)
- Median rejections per user (lifetime): ≥6 by day 30
- Crash-free sessions: ≥99.7%

---

## 9. Risks & objections (and answers)

| Objection | Response |
|---|---|
| "Is this just a journal app?" | No — rejection-only. Single-purpose. Shareable. |
| "Why would I pay to track failures?" | You don't. It's free. Tip if you want. |
| "Isn't this making fun of pain?" | The framing is earnest. Read Jia Jiang's book. The whole movement is about reclaiming rejection. |
| "Can't I just use Notes?" | You can. The whole pitch is that the stats card and the share moment make it stick. |
| "What about Android?" | Not yet. iOS-first. The audience (indie devs, founders, US tech workers) is iOS-heavy. |
| "What about privacy?" | Data lives on-device. No required login. Tip jar uses StoreKit (Apple). Optional Parra account if user wants feedback/roadmap features. |

---

## 10. The 12-month story

- **Month 1:** Launch. Rejection Week. Show HN. 1.5K installs.
- **Month 2-3:** LinkedIn long-post empire ramps. First creator collab (one of: Madeline Mann, Gabriella Carr, Marc Lou). 8K installs.
- **Month 4-6:** Pro tier experiment ($2.99/yr). Year-in-review export feature. Launch on Product Hunt with the "I logged 247 rejections in 6 months" angle. 30K installs.
- **Month 7-9:** Localize for 5 languages (Spanish, Portuguese, German, French, Japanese). Pitch a Substack on the rejection economy. Court Adam Grant for a single mention. 100K installs.
- **Month 10-12:** Year-end "Rejection Roundup" — a public, anonymized data report. "The state of rejection in 2026: what 14,000 people taught me about saying no." That report is the press hook for year 2.

---

## Appendix A — Real handles & links to engage week 1

- Jia Jiang — https://www.jiajiang.com — sells the Rejection Therapy card deck. Email him.
- Rejection Therapy — https://www.rejectiontherapy.com
- Marc Lou — @marc_louvion on X — https://www.indiehackers.com/marclou
- Pieter Levels — @levelsio on X — https://levels.io
- Madeline Mann — Self Made Millennial (TikTok, YouTube, LinkedIn)
- Bonnie Dilber — Talent at Zapier (LinkedIn 600K)
- Becky Tuch — Lit Mag News on Substack
- Channing Allen — @csallen — Indie Hackers
- Rosie Sherry — @rosiesherry — Indie Hackers community
- Justin Jackson — @mijustin — MegaMaker, Build Your SaaS
- Paul Hudson — Hacking with Swift
- Steve Troughton-Smith — @stroughtonsmith
- Theo Browne — @theo (t3.gg) — YouTube indie dev
- Sahil Bloom — newsletter on resilience
- James Clear — newsletter (Atomic Habits angle on rejection as practice)
- Adam Grant — Wharton, has cited Jia Jiang in writing
- The Submission Grinder — thegrinder.diabolicalplots.com — writer community
- Indie Hackers — indiehackers.com — submit launch
- WIP.co — daily build-in-public log
- layoffs.fyi — data source for LinkedIn posts
- Crunchbase Layoffs Tracker — data source

---

## Appendix B — Domain & web presence

- **Primary domain:** rejected.app (check availability — fallback: getrejected.app, rejectedapp.com, logtheno.com)
- **Subpages:**
  - `/` — landing, single CTA "Download on the App Store"
  - `/log` — public, community-submitted App Review rejection wall (Initiative 2)
  - `/week` — Rejection Week landing page (Initiative 1)
  - `/manifesto` — long-form essay on why we built it (the founder personal story from Show HN)
  - `/press` — for journalists
- **Email capture:** "Get the weekly rejection roundup — 3 best stories submitted this week."

---

# THIS WEEK: #1 action

**Lock the launch date for Rejection Week, post the kickoff thread on X Monday 9:00 AM PT, and DM Marc Lou (@marc_louvion), Madeline Mann, and Becky Tuch (Lit Mag News) the same morning with a TestFlight link.**

Concretely, by Friday:
1. Pick a Monday 4–6 weeks out and write it on the wall.
2. Pre-write the seven daily seed posts (one per segment: indie dev, job seeker, founder, writer, rejection-therapy, college, dating). Schedule them to drop self-published Day -7 through Day -1.
3. Send three DMs Monday morning with a personal note, a TestFlight link, and a single ask: "would you share this with your audience during the week of [date]?"
4. Put rejected.app/week up as a single-screen landing page with the seven-day calendar.

Everything else compounds off this one week.
