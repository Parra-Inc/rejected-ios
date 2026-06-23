# Rejected — Brand Guide

> Slightly defiant. Optimistic without being saccharine. The friend who texts "lol Apple rejected me again, gonna be a great week" — not the one who texts "ugh I'm so over this."

---

## 1. Identity

### Name
**Rejected** — a single word, blunt, on the nose. The whole concept is owning the label, so the app name reclaims it.

- Display: `Rejected`
- Bundle ID: `com.parra.rejectiontrackerios` (legacy — rename to `com.parra.rejected` if/when we can without breaking installs)
- Repo: `github.com/Parra-Inc/rejected-ios`
- Domain: `rejected.app` preferred. Fallbacks: `getrejected.app`, `rejectedapp.com`, `logtheno.com`

### Tagline
**"Collect rejections like trophies."**

### Three rotating taglines (per surface)
1. "Get told no on the record."
2. "The trophy case for the no's."
3. "Rejection is data. Track it."

---

## 2. Voice & tone

### The frame
We sound like the **defiant-optimistic friend** in your DMs at 11 PM. Not a coach. Not a therapist. Not a brand.

### Voice principles

| Principle | What it looks like |
|---|---|
| **Terse over verbose** | "Logged." not "Your rejection has been successfully recorded." |
| **Receipts over feelings** | Specific numbers, dates, categories. Not "you're doing great." |
| **Defiant over self-pitying** | "Best week of the year." (after 0 yeses) — not "tough week, hang in there." |
| **Lowercase comfortable** | Tweets and notifications can be lowercase. The marketing site can be too. |
| **No exclamation points** | Almost ever. The voice is dry, not cheery. |
| **Emoji as data, not decoration** | 🤠 47 🍎 11 ✅ — yes. ✨🌟amazing!💫 — no. |
| **Cursing OK where natural** | "shit week, 14 logged" lands. "Holy moly that's a lot!" does not. Use sparingly and never in copy that App Review will read. |

### Voice cheat sheet

| Do | Don't |
|---|---|
| "Logged. Back to work." | "Your rejection has been saved successfully!" |
| "Streak: 12." | "Way to go — you're on a roll!" |
| "Best week of the year." | "Don't get discouraged!" |
| "Applied is an aspiration. Rejected is a receipt." | "Stay positive and keep applying!" |
| "0 yeses. 14 no's logged." | "We believe in you!" |
| "97% of what I ship flops. 100% gets logged." | "Embrace the journey of entrepreneurship." |

### Words we use
log · receipt · trophy case · streak · no · on the record · ship · back to work · collected · data · evidence · proof · the grind · reframe · pile · stack · trophy · scoreboard

### Words we avoid
journey · embrace · healing · processing · wellness · mindfulness · resilience-as-a-noun · "you've got this" · warrior · tribe (prefer "crowd," "audience") · manifest · authentic · vibes-with-a-capital-V

---

## 3. Visual identity

### Color palette

Black and white are the brand colors. Color is used sparingly to mark category, status, and one accent (the 🤠 share moment).

#### Brand — Trophy Gold
The hero accent. Used for the streak badge, the share screen frame, and the brand mark on web.

| Token | Hex | Use |
|---|---|---|
| `rjPrimary` | `#D4A24C` | Trophy gold — streak badges, primary CTAs, brand mark |
| `rjPrimaryDark` | `#A87F30` | Pressed state, secondary use on light bg |
| `rjPrimaryLight` | `#FBF3E0` | Tint backgrounds, selected pills |

#### Foundation — Off-black + off-white
The product reads as a "ledger" — terminal-like, archival, taken-seriously.

| Token | Hex | Use |
|---|---|---|
| `rjInk` | `#0E0E0E` | Primary text, primary surfaces in dark mode |
| `rjPaper` | `#FAF8F4` | Light mode background (warm off-white, slight cream) |
| `rjMutedInk` | `#5C5C5C` | Secondary text |
| `rjMutedPaper` | `#EDE9E2` | Card backgrounds in light mode |

#### Category accents
Used only on category pills, never on text or chrome.

| Category | Hex | Emoji |
|---|---|---|
| Job | `#3A6EA5` | 💼 |
| Investor | `#7A4FB8` | 💸 |
| YC | `#FF6B35` | 🟧 |
| App Review | `#666666` | 🍎 |
| Romantic | `#D45272` | 💔 |
| College | `#2E7D5B` | 🎓 |
| Custom | `#D4A24C` | (user picks) |

#### Status colors
We don't use red/green for outcomes (no win/lose framing). We use a single "logged" color (gold) and gray for everything past.

### Typography
System fonts only (SF Pro on iOS, ui-sans-serif on web). No custom fonts shipping in app or on marketing site.

- **Numerals are tabular** wherever they count things (streak, total, per-category counts). Use `.monospacedDigit()`.
- **Headlines are blunt:** large, weight 700, tight tracking. Marketing site headlines use `text-5xl font-bold tracking-tight`.
- **Body is regular.** No italics for emphasis (use weight).

### App icon
- Trophy mark in trophy gold on off-black background, rounded corners
- The trophy is a slightly absurd cup-style trophy with a small label that reads "NO" — readable at 1024px, recognizable as a trophy shape at 60px
- Single accent color (gold). No gradients. No drop shadows beyond what iOS adds.

### Marketing site visual rules
- One headline at a time
- Black + cream + gold; nothing else
- Screenshots are the only photography (the product is the photography)
- No stock founder-with-laptop imagery
- No team carousels (the brand is the product, not the people)
- One CTA per page: "Download on the App Store"

---

## 4. The share image (the most important asset we ship)

The share screen is the growth loop. Its visual design is more important than the app icon.

### Anatomy
```
┌─────────────────────────────────────┐
│                                     │
│         REJECTED                    │ ← brand mark, top-left, gold
│                                     │
│         🤠                          │ ← cowboy emoji, centered
│         turn that frown             │
│         upside down                 │ ← tagline, sentence case
│                                     │
│         147 rejections collected    │ ← user's stats, tabular nums
│         last: 2 hours ago           │
│         top: jobs 64 · inv 31       │
│                                     │
│         rejected.app                │ ← footer, small
└─────────────────────────────────────┘
   1080 × 1350 (4:5 — IG / FB sweet spot)
   also export 1080 × 1920 (Stories)
   and 1200 × 675 (X/LinkedIn link preview)
```

### Design rules for the share image
- **Cream background, ink type, gold accent.** Always.
- **The 🤠 stays.** It is the brand. People will recognize it.
- **Tabular numerals** for the stats line.
- **Username does not appear on the image.** The image is the user's flex; we don't tag the app on it visually (the footer URL is enough).
- **Watermark is single-line text**, no logo lockup.

### Alternative frames (Pro tier, future)
- 🏴‍☠️ "no's are doubloons"
- 🪦 "graveyard of yeses i didn't get"
- 📜 "the scroll of receipts"

Keep Pro frames optional. The 🤠 is canon.

---

## 5. Naming conventions

### In-app strings
- The thing logged is a **rejection** (noun) or a **no** (casual)
- The action is **log** (verb) — never "save," "add," "record"
- The history is the **trophy case** or the **stack** (both fine)
- The number is the **streak** (when contextually "ongoing") or the **count** (when historical)
- Categories are **categories** (not "tags," not "types")
- The tip jar is **the tip jar** (lowercase, definite article, never "support the developer")

### Tip jar copy
- $0.99: ☕️ "buy me a coffee" — `v1.tip.1`
- $2.99: 🍕 "buy me a slice" — `v1.tip.3`
- $9.99: 🎉 "throw me a party" — `v1.tip.10`

Each label is lowercase, no period, emoji first.

### Empty state copy
- Home: `nothing logged yet. go get a no.`
- Stats: `your trophy case is empty. that's the bad news. the good news is you can fix it in five seconds.`
- Categories: `no custom categories yet. the defaults cover most. add your own when you have a specific tribe of no's.`

### Confirmation copy
- After log: `logged. back to work.`
- After tip: `appreciated. now go collect another one.`
- After share: `posted. let us know if it landed.`

---

## 6. Anti-brand examples

If you see this in our copy, it's wrong:

- "We're rooting for you on your application journey!"
- "Don't let rejection define you ✨"
- "Join a community of resilient go-getters 🚀"
- "Track your wins AND your losses!" (we are not a wins app)
- "Mindful rejection processing"
- "Your rejection coach in your pocket"
- "Turn rejections into reflections" (we do not reflect; we log and post)

If you see this, it's right:

- "Logged. Back to work."
- "0 yeses this week. 14 no's logged. Best week of the year."
- "Your 47th investor no is the same as the 1st. Both are data."
- "The trophy case for the no's."
- "Free forever. Tip if it made you smile."

---

## 7. Sourcing & references

The vibe references that make the brand legible:

- **Marc Lou's** lowercase, terse, numbers-first Twitter
- **Pieter Levels's** "97% of what I ship flops" public-failure-as-marketing
- **Death to Stock** typography (cream + ink + serif numbers)
- **MoMA Design Store** product photography minimalism
- **Liquid Death's** confident absurdism — applied with a much smaller budget and zero stunts

The vibe references to **avoid**:

- Headspace / Calm (too soft, too coach-y)
- LinkedIn brand posts (too earnest, exclamation-point-heavy)
- Notion (too pastel, too "team productivity")
- BetterHelp (literally the opposite frame from us)
