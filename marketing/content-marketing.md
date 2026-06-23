# Rejected — Content Marketing Playbook

> The Rejection Wall is the asset. Essays are the amplifier. SEO-optimized App Review guideline posts are the compounding moat. We become the canonical reference for "what does an Apple rejection look like."

---

## 1. Why content matters at rank #3

Content marketing is the only channel where work done today still produces installs in month 12. X tweets disappear in 48 hours; LinkedIn posts in two weeks; Reddit threads in a month. A well-ranked SEO post for "App Store guideline 4.3" runs for two years.

For Rejected specifically:

- **App Review terms are a goldmine.** `guideline 4.3 design spam`, `guideline 2.1 minimum functionality`, `guideline 5.1.1 PII` — high-intent, low-competition, evergreen.
- **The Rejection Wall is community-generated, SEO-friendly, and Twitter-shareable.** Each weekly entry produces a tweet, a backlink, and a deepening category page.
- **Essays anchor the brand.** Long-form "rejection-as-data" pieces give creators, journalists, and podcast hosts a reason to cite us.

---

## 2. The three content pillars

### Pillar A — The Rejection Wall (community asset)
Public web page that displays community-submitted App Review rejection emails (redacted). Updated weekly. Each entry has a "Log this in Rejected →" button. **This is the canonical asset.**

### Pillar B — Guideline-of-the-Week SEO posts
One short SEO post per week, each targeting a specific App Review guideline. Designed to rank for `app store guideline X rejection` queries.

### Pillar C — Essays (the reframe)
Long-form pieces on rejection-as-data, rejection therapy, the layoff cycle, indie hacker rejection economy. One every 10 days. Publish on rejected.app, cross-post to dev.to, Hashnode, Medium, LinkedIn.

---

## 3. The Rejection Wall (Pillar A) — full spec

### What it is
A public web page at `rejected.app/log` displaying redacted, community-submitted App Review rejection emails. Each entry shows:
- The rejection email body (PII-redacted)
- Submitting developer (handle, optional)
- App category and use case (one line)
- Apple guideline cited
- Tags: `4.3`, `4.0`, `5.1.1`, etc.
- "Log this in Rejected →" CTA → deep link into app

### Why it works
- **SEO compound:** every entry is a new page on the relevant guideline number; the category pages aggregate by guideline and accumulate authority.
- **Community asset:** developers want to share their rejections; the Wall gives them a "press" surface for it; reciprocity drives ongoing submissions.
- **Tweet-bait:** every Wall update is one tweet ("3 new rejections logged this week — gnarliest is a 4.3 on a meditation app: rejected.app/log/[id]").
- **Backlink magnet:** other dev blogs will link to specific entries as case studies. Each backlink helps the whole domain.

### Submission flow
- Simple web form: paste rejection email, optional handle, optional app context
- Manual review by founder (10 min/week)
- Auto-publish after redaction
- Submitter gets a tweet they can quote: "I'm on the Rejection Wall: rejected.app/log/[id]"

### Content cadence
- **Weeks 1–4:** seed the wall with 10 of our own + close-friend rejections so it doesn't launch empty
- **Week 4 onward:** weekly publish day (Thursday), 3–5 new entries/week
- **Month 6:** introduce category pages — `/log/guideline-4-3`, `/log/guideline-2-1`, etc. — each with all entries for that guideline

### Promotion per entry
1. Tweet from @rejectedapp with the rejection body screenshot
2. Cross-post to r/iOSProgramming if it's particularly gnarly
3. DM the submitter so they retweet
4. Include in next month's IH milestone post

---

## 4. Guideline-of-the-Week SEO posts (Pillar B)

Goal: rank in top 5 on Google for `[guideline number] app store rejection` and similar queries. Appcircle's existing piece is the competitor; we win on freshness, depth, and the call-to-action.

### The 12 guidelines to cover (priority order)

| Week | Guideline | Why this priority |
|---|---|---|
| 1 | 4.3 — Design Spam | Highest-volume rejection search term, hits indie devs hardest |
| 2 | 2.1 — Minimum Functionality | Second-highest indie rejection |
| 3 | 5.1.1 — Data Collection / Privacy | Privacy-focused devs frequently hit |
| 4 | 4.0 — Design | Broad, high-volume |
| 5 | 3.1.1 — IAP for Digital Content | Hits subscription apps |
| 6 | 5.1.5 — Location Services | Mobile-first apps |
| 7 | 4.5.4 — Push Notification Abuse | Engagement-feature apps |
| 8 | 2.3 — Accurate Metadata | Common, easy fix |
| 9 | 2.5.1 — Software Requirements | Edge-case but high SEO traction |
| 10 | 5.3 — Gaming, Gambling, Lotteries | Niche but high CPC if any monetization later |
| 11 | 4.1 — Copycats | High emotional charge, shareable |
| 12 | 3.2.2 — Unacceptable Business Models | The "I don't understand why I was rejected" rejection |

### Per-post structure (target 1,200–1,800 words)

```
# Guideline {X} — {Title} — What It Is and How to Fix Your Rejection

[1-paragraph plain-English summary of what Apple is asking for]

## The exact rejection email language
[verbatim quote of what App Review typically writes]

## Why this guideline exists
[1 paragraph — Apple's intent, the policy context]

## The three flavors of {X} rejection
[bullets — common variations of how this gets cited]

## The fix (with code where relevant)
[concrete steps, screenshots, Info.plist examples, etc.]

## Real Rejection Wall examples (live)
[3 examples from rejected.app/log/guideline-X — pulled live so the page stays fresh]

## What to do next
[CTA: log your rejection in Rejected so you have it on record when you appeal]

## Related guidelines
[internal links to other guideline posts]
```

### SEO checklist per post
- Target keyword in H1, URL slug, first paragraph
- Title under 60 chars: "Guideline 4.3 Rejection: Why Apple Rejects Your App for Design Spam"
- Meta description with action-oriented hook
- Internal links to 3+ related guideline posts
- One external authoritative link (Apple's developer documentation)
- Schema.org `Article` markup
- Open Graph image — gold "Rejected" wordmark + guideline number on cream

### Publishing cadence
- One per week, weeks 1–12 (12 posts in first quarter)
- Refresh quarterly with new Wall examples and current year stats

---

## 5. Essays (Pillar C)

Long-form pieces that anchor the brand and give journalists/podcast hosts something to cite.

### Essay calendar — Month 1–6

| # | Title | Audience | Word count | Notes |
|---|---|---|---|---|
| 1 | "The Rejection Economy" | Seg 1 + 3 | 2,500 | Pieter Levels-style data piece on the scale of rejection in tech. Layoff stats, YC accept rate, App Review reject rate, investor pass rate. The headline numbers post. |
| 2 | "I Got Rejected 247 Times in 6 Months. Here's What the Data Showed." | Seg 1 + 2 | 1,800 | Personal narrative with screenshots of the app's stats page filled in. The vulnerable founder post in essay form. |
| 3 | "How to Run a 100-Day Rejection Therapy Challenge (And Track It Like a Pro)" | Seg 5 | 1,500 | Jia Jiang anchor. SEO play for "rejection therapy challenge." |
| 4 | "Stop Counting Applications. Start Counting Rejections." | Seg 2 | 1,400 | LinkedIn-flavored reframe essay. Best of the LinkedIn long-form posts in compiled form. |
| 5 | "An Open Letter to App Review (From the 47 of Us Rejected This Week)" | Seg 1 | 1,200 | Spicy. Curated rejection emails. The Wall in essay form. |
| 6 | "I Asked 100 Laid-Off Engineers How Many Rejections They Had. Median: 67." | Seg 2 | 2,200 | The grand-slam data essay. Histogram, methodology, individual stories. Press hook. |
| 7 | "Investor Passes Are Just Categorization. Here Are 47 of Mine." | Seg 3 | 1,800 | Founder vulnerable post. List of 47 real passes with the polite-no email language. |
| 8 | "The Writer's Submission Tracker That Isn't Trapped in 2008" | Seg 4 | 1,400 | Duotrope alternative essay. Compares apps + sheets + paper, lands on Rejected. |
| 9 | "Year One — What 14,000 Rejected Users Taught Me About Failure" | All | 2,500 | Year-end milestone post (Month 12). The press hook for year 2. |

### Where to publish

Primary: **rejected.app/blog** (canonical URL, SEO accrues here)

Cross-post (with canonical link back to rejected.app):
- dev.to (segment 1)
- Hashnode (segment 1)
- Medium (segment 2, 3, 5)
- LinkedIn (segment 2, 3)
- Substack newsletter (if/when we have one)

### Promotion per essay
- Tweet thread (5–9 tweets) summarizing the essay
- LinkedIn post (long-form version of one section)
- IH or HN cross-post if the essay has a strong "ask"
- DM to 3 relevant creators ("thought you'd find this interesting")
- Newsletter swap pitch ("we just published this; want to include in next issue?")
- Reply-storm reference in X discussions over the next week

---

## 6. The marketing site (rejected.app)

The blog is part of a small marketing site. Pages:

| Page | Purpose |
|---|---|
| `/` | Landing — single CTA "Download on the App Store." Hero, screenshot grid, social proof, share-image example, tip-jar callout, GitHub link. |
| `/log` | The Rejection Wall (Pillar A) |
| `/log/guideline-4-3` etc | Per-guideline category pages |
| `/blog` | Essay index (Pillar C) |
| `/blog/[slug]` | Individual essays |
| `/week` | #RejectionWeek campaign page (launch + annual) |
| `/manifesto` | Long-form founder origin essay (the personal story from Show HN, expanded) |
| `/press` | For journalists — boilerplate, screenshots, founder bio, contact |
| `/changelog` | Public changelog (Parra-powered, ties back to product) |

### Tech
Next.js + MDX for blog. Tailwind. Vercel hosting. No analytics beyond Plausible. No email gate on any page.

### Email capture (light)
One footer signup: "Weekly Rejection Roundup — 3 best Wall entries + 1 essay link. Every Sunday." Goal: 1K subs by day 90.

---

## 7. Distribution playbook (per piece)

The default flow for every essay or Wall update:

| Hour | Action |
|---|---|
| T-0 | Publish on rejected.app |
| T+0:15 | Tweet thread from founder account |
| T+0:30 | LinkedIn post (founder) |
| T+1:00 | Cross-post to dev.to + Hashnode (or Medium for non-dev essays) |
| T+2:00 | DM to 3 creators with personal note |
| T+4:00 | Submit to relevant Reddit sub if substantive enough |
| T+8:00 | Reply to all comments on all surfaces |
| Day +1 | Hacker News submission if essay has data + personal hook |
| Day +3 | Newsletter pitch to 2 relevant publications |
| Day +7 | Quote-tweet self with key data point |
| Day +30 | Refresh promotion if performance was strong |

---

## 8. Heroes to court (content placement)

People whose syndication, citation, or guest-post slot would meaningfully amplify our essays.

| Person | Outlet | Why |
|---|---|---|
| **Adam Grant** | Wharton podcasts, his newsletter | Cited Jia Jiang. The grand-slam mention. |
| **Sahil Bloom** | Newsletter (300K+) | Resilience angle |
| **James Clear** | Atomic Habits newsletter | "Rejection as practice" |
| **Lenny Rachitsky** | Lenny's Newsletter | Product/data angle |
| **Tomasz Tunguz** | Newsletter | Founder data angle |
| **Bonnie Dilber** | LinkedIn | Layoff/job-seeker angle |
| **Becky Tuch** | Lit Mag News Substack | Writer angle |
| **Channing Allen** | Indie Hackers newsletter | Indie hacker angle |
| **Charles Wagner** | RevenueCat blog | App Review angle (we pitch a guest post: "We surveyed 100 indie devs about App Store rejection") |
| **Steve Moser** | App Review newsletter | App Review angle |

---

## 9. Measurement

| Metric | Source | 30/90/180 |
|---|---|---|
| Organic visits to rejected.app | Plausible | 500 / 4K / 15K |
| Wall entries submitted | Form analytics | 10 / 60 / 200 |
| Guideline post avg ranking | Search Console | n/a / top 10 / top 5 |
| Essay reads (avg per essay) | Plausible + Medium stats | 500 / 2K / 5K |
| Essay → App Store referral rate | UTM-tagged | 3% / 5% / 7% |
| Backlinks earned | Ahrefs free tier | 5 / 30 / 100 |
| Newsletter subs (rejected.app footer) | Mailing list | 100 / 600 / 2K |

---

## 10. Anti-patterns

- **Don't gate any content.** No email walls, no "download this PDF" forms, no popups. Brand is generosity.
- **Don't write essays that are pitch decks.** If the essay's last paragraph could be "and that's why you should buy our product," cut it. The CTA should be footer-only.
- **Don't chase search trends outside the niche.** "How to deal with rejection in dating" gets traffic but kills brand fit. Stay in: tech, founders, jobs, writing, deliberate rejection therapy.
- **Don't republish without canonical links.** Medium/dev.to/Hashnode must canonicalize to rejected.app or we cannibalize our own SEO.
- **Don't ship a guideline post without code/screenshots.** They are reference material. Walls of text without examples don't rank.
- **Don't accept Wall submissions without redaction.** PII, reviewer names, internal Apple language all get scrubbed. One leak ruins the channel.
- **Don't go quiet on the Wall.** Six weeks of no updates and the channel dies. If we can't sustain weekly, downgrade to monthly with a "State of App Review Rejection" digest format.

---

## 11. The 12-week content sprint (launch period)

| Week | Essay | Guideline post | Wall entries |
|---|---|---|---|
| 1 | "Rejection Economy" | 4.3 | 3 (seed) |
| 2 | — | 2.1 | 3 |
| 3 | "I Got Rejected 247 Times" | 5.1.1 | 4 |
| 4 | — | 4.0 | 4 |
| 5 | "100-Day Rejection Therapy" | 3.1.1 | 4 |
| 6 | — | 5.1.5 | 4 |
| 7 | "Stop Counting Applications" | 4.5.4 | 5 |
| 8 | — | 2.3 | 5 |
| 9 | "Open Letter to App Review" | 2.5.1 | 5 |
| 10 | — | 5.3 | 5 |
| 11 | "100 Laid-Off Engineers" (grand-slam) | 4.1 | 5 |
| 12 | — | 3.2.2 | 5 |

By end of quarter: 12 guideline SEO posts, 6 essays, 52 Wall entries, ~15K organic visits.
