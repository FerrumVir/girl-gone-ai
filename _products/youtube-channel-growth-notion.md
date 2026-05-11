# YouTube Channel Growth System — Notion Template

> Duplicate this page into your Notion workspace to get started. All eight databases are pre-linked and all formulas are pre-built. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Video Ideas Bank

**Purpose:** Every idea you've ever had — captured, scored, and prioritized so you always know what to work on next.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Video Title (Working) | Title | Working title — refine before publishing |
| Topic Category | Select | Tutorial / How-To / Review / Comparison / List / Story / Vlog / Reaction / Commentary / News / Challenge / Collab / Behind the Scenes / Q&A / Shorts / Other |
| Content Pillar | Select | Define your 3–5 main content themes and add them here (e.g., "Gear Reviews" / "Editing Tutorials" / "Industry News" / "Behind the Scenes") |
| Target Audience | Text | Who specifically is this video for? |
| Search Intent | Select | Informational / Navigational / Commercial / Entertainment |
| Estimated Search Volume | Select | High / Medium / Low / Unknown / Trending |
| Competition Level | Select | Low / Medium / High / Saturated |
| Priority Score | Select | 5 - Must Make / 4 - High Priority / 3 - Good Idea / 2 - Maybe Later / 1 - Backlog |
| Idea Stage | Select | Raw Idea / Researched / Outlined / Scripted / Ready to Film / Scheduled / Archived |
| Hook | Text | The opening 5 seconds — what makes someone stay? |
| Key Points | Text | Main talking points or segments |
| Unique Angle | Text | What makes YOUR version of this topic different? |
| Reference Videos | URL | Similar videos for research (competitor or inspiration) |
| SEO Keywords | Relation | → SEO Keyword Research database |
| Potential Sponsors | Text | Brands that would be a natural fit for this topic |
| Estimated Production Time | Select | Quick (< 4 hours) / Standard (4–8 hours) / Complex (8–20 hours) / Major (20+ hours) |
| Format | Select | Long-form (10+ min) / Medium (5–10 min) / Short (< 5 min) / YouTube Short / Live Stream |
| Evergreen | Checkbox | Will this video be relevant in 12+ months? |
| Source | Select | Audience Request / Comment / Trend / SEO Research / Personal Experience / Competitor Gap / Sponsor Request / Series / Collaboration |
| Date Added | Date | When you captured this idea |
| Notes | Text | Additional context, research links, inspiration |
| Linked Video | Relation | → Video Pipeline database (when the idea moves to production) |
| Tags | Multi-select | Viral Potential / Low Effort / High Effort / Seasonal / Series / Collaboration / Sponsored Fit / Trending |

**Views:**

- **All Ideas** — Table, sorted by Priority Score descending, then Date Added descending
- **Idea Pipeline** — Kanban, grouped by Idea Stage
- **High Priority** — Filter: Priority Score = 5 or 4, sorted by Priority Score descending
- **Evergreen Ideas** — Filter: Evergreen = true, sorted by Priority Score descending
- **By Content Pillar** — Table, grouped by Content Pillar
- **Quick Wins** — Filter: Estimated Production Time = Quick, Priority Score >= 3
- **Research Needed** — Filter: Idea Stage = Raw Idea, sorted by Priority Score descending
- **Archived** — Filter: Idea Stage = Archived

---

### 2. Video Pipeline / Production Tracker

**Purpose:** Every video in production — from scripting through publish. Your production command center.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Video Title | Title | Final or working title |
| Idea | Relation | → Video Ideas Bank (the idea this video came from) |
| Production Stage | Select | Scripting / Filming / Editing / Thumbnail & Graphics / Review / Scheduling / Published / On Hold |
| Status | Select | On Track / Behind / Blocked / Completed / Cancelled |
| Target Publish Date | Date | When you plan to publish |
| Actual Publish Date | Date | When you actually published |
| Published on Time | Formula | `if(and(not(empty(prop("Actual Publish Date"))), not(empty(prop("Target Publish Date")))), if(prop("Actual Publish Date") <= prop("Target Publish Date"), "On Time", "Late"), "")` |
| Days Until Publish | Formula | `if(empty(prop("Target Publish Date")), "No date", format(dateBetween(prop("Target Publish Date"), now(), "days")) + " days")` |
| Script Status | Select | Not Started / Drafting / First Draft / Revised / Final |
| Script Doc | URL | Link to script document |
| Filming Date | Date | |
| Filming Location | Text | |
| B-Roll Needed | Text | List of B-roll shots needed |
| Editor | Text | Who is editing this video (you or team member) |
| Edit Status | Select | Not Started / Rough Cut / Fine Cut / Color & Audio / Final |
| Edit File | URL | Link to edit project or shared drive |
| Thumbnail Status | Select | Not Started / Concepts / Designed / A/B Variant Ready / Uploaded |
| Thumbnail Designer | Text | |
| Video Length (min) | Number | Final video length |
| Format | Select | Long-form / Medium / Short / YouTube Short / Live |
| Upload Checklist | Relation | → Upload Checklist database |
| Checklist Complete | Rollup | Are all checklist items done? |
| SEO Keywords | Text | Primary and secondary keywords for this video |
| Sponsorship | Relation | → Sponsorship CRM database |
| Analytics | Relation | → Analytics Tracker database |
| Notes | Text | Production notes, blockers, creative decisions |
| Tags | Multi-select | Priority / Collab / Sponsored / Series / Evergreen / Trending / Reshoot Needed |

**Views:**

- **Production Board** — Kanban, grouped by Production Stage (your main working view)
- **All Videos** — Table, sorted by Target Publish Date ascending
- **Publishing Schedule** — Filter: Production Stage is not Published or Cancelled, sorted by Target Publish Date
- **This Week** — Filter: Target Publish Date is this week
- **Published** — Filter: Production Stage = Published, sorted by Actual Publish Date descending
- **Blocked / Behind** — Filter: Status = Behind or Blocked
- **By Month** — Table, grouped by month of Target Publish Date
- **On Hold** — Filter: Production Stage = On Hold

---

### 3. Upload Checklist

**Purpose:** A reusable pre-publish checklist that catches every detail before you hit the publish button.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Checklist Title | Title | "[Video Title] — Upload Checklist" |
| Video | Relation | → Video Pipeline database |
| Title Optimized | Checkbox | Is the title keyword-rich, compelling, and under 60 characters? |
| Description Written | Checkbox | First 2 lines contain keyword + hook. Full description with links, chapters, and CTAs |
| Tags Added | Checkbox | 10–15 relevant tags including primary keyword variations |
| Thumbnail Uploaded | Checkbox | Final thumbnail uploaded (check mobile preview) |
| End Screen Added | Checkbox | Subscribe button + next video or playlist |
| Cards Placed | Checkbox | Info cards at relevant moments (link to related videos or playlists) |
| Chapters/Timestamps | Checkbox | Timestamps in description (0:00 format) |
| Subtitles Reviewed | Checkbox | Auto-captions reviewed and corrected if needed |
| Pinned Comment | Checkbox | First comment pinned with CTA or engagement question |
| Community Post | Checkbox | Community tab post drafted/scheduled to promote the video |
| Cross-Promotion | Checkbox | Shared on Twitter/X, Instagram, TikTok, or other platforms |
| Playlist Added | Checkbox | Video added to relevant playlist(s) |
| Monetization Settings | Checkbox | Ad placements reviewed (mid-rolls at natural breaks) |
| Notification Sent | Checkbox | "Notify subscribers" checked (or scheduled notification) |
| SEO Check | Checkbox | Primary keyword in title, description (first 2 lines), and tags |
| Publish Time | Text | Optimal publish time based on your audience analytics |
| All Complete | Formula | `if(and(prop("Title Optimized"), prop("Description Written"), prop("Tags Added"), prop("Thumbnail Uploaded"), prop("End Screen Added"), prop("Cards Placed"), prop("Chapters/Timestamps"), prop("Pinned Comment"), prop("SEO Check")), true, false)` |
| Notes | Text | Anything specific to this upload |

**Views:**

- **All Checklists** — Table, sorted by creation date descending
- **Incomplete** — Filter: All Complete = false
- **By Video** — Table, grouped by Video

---

### 4. Analytics Tracker

**Purpose:** Post-publish performance tracking for every video. Log metrics at 7, 30, and 90 days to identify patterns.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Video Title | Title | Must match Video Pipeline title |
| Video | Relation | → Video Pipeline database |
| Publish Date | Rollup | From linked Video |
| Content Pillar | Text | For pattern analysis |
| Video Length (min) | Number | |
| **7-Day Metrics** | | |
| Views (7d) | Number | |
| Watch Time Hours (7d) | Number | |
| Avg View Duration (7d) | Text | Format: "4:32" |
| CTR (7d) | Number | Click-through rate as percentage |
| Impressions (7d) | Number | |
| Subscribers Gained (7d) | Number | |
| **30-Day Metrics** | | |
| Views (30d) | Number | |
| Watch Time Hours (30d) | Number | |
| Avg View Duration (30d) | Text | |
| CTR (30d) | Number | |
| Impressions (30d) | Number | |
| Subscribers Gained (30d) | Number | |
| **90-Day Metrics** | | |
| Views (90d) | Number | |
| Watch Time Hours (90d) | Number | |
| Revenue (90d) | Number (USD) | AdSense revenue from this video |
| **Performance Analysis** | | |
| Views per Impression | Formula | `if(prop("Impressions (30d)") > 0, round(prop("Views (30d)") / prop("Impressions (30d)") * 1000) / 10, 0)` |
| Performance Rating | Select | Viral / Outperformer / Average / Underperformer / Flop |
| Top Traffic Source | Select | Browse / Search / Suggested / External / Channel Page / Notification / Shorts Feed / Other |
| Top Search Terms | Text | What keywords are driving views to this video? |
| Audience Retention Notes | Text | Where do viewers drop off? Any spikes? |
| What Worked | Text | Why did this video perform the way it did? |
| What to Improve | Text | What would you do differently? |
| Thumbnail Tests | Relation | → Thumbnail A/B Testing database |
| Tags | Multi-select | Viral / Evergreen / Seasonal / Series / One-Off |

**Views:**

- **All Videos** — Table, sorted by Publish Date descending
- **Top Performers** — Filter: Performance Rating = Viral or Outperformer, sorted by Views (30d) descending
- **Underperformers** — Filter: Performance Rating = Underperformer or Flop
- **By Content Pillar** — Table, grouped by Content Pillar
- **CTR Leaderboard** — Table, sorted by CTR (30d) descending
- **Revenue Leaderboard** — Table, sorted by Revenue (90d) descending
- **Needs 30-Day Update** — Filter: Views (30d) is empty, Publish Date is more than 30 days ago
- **Needs 90-Day Update** — Filter: Views (90d) is empty, Publish Date is more than 90 days ago

---

### 5. Thumbnail A/B Testing Log

**Purpose:** Track every thumbnail change to build a data-driven understanding of what drives clicks on your channel.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Test Name | Title | "[Video] — Test [Number]" |
| Video | Relation | → Analytics Tracker database |
| Video Title | Rollup | From linked Analytics entry |
| Original Thumbnail | Files | Upload the original thumbnail image |
| Original Description | Text | Describe the original: colors, text, composition, facial expression |
| Variant Thumbnail | Files | Upload the new variant |
| Variant Description | Text | Describe the variant: what changed? |
| What Changed | Select | Text / Face / Color / Composition / Background / Style / Complete Redesign |
| Swap Date | Date | When you swapped to the variant |
| Days Running Original | Number | How many days the original ran |
| Original CTR | Number | CTR before the swap |
| Original Impressions | Number | Impressions before the swap |
| Variant CTR (7d) | Number | CTR 7 days after the swap |
| Variant CTR (30d) | Number | CTR 30 days after the swap |
| Variant Impressions (7d) | Number | |
| CTR Change | Formula | `if(and(prop("Original CTR") > 0, prop("Variant CTR (7d)") > 0), round((prop("Variant CTR (7d)") - prop("Original CTR")) * 100) / 100, 0)` |
| Winner | Select | Original / Variant / Inconclusive / Too Early |
| Result | Select | Significant Improvement / Slight Improvement / No Change / Decline |
| Hypothesis | Text | What did you expect to happen and why? |
| Learning | Text | What did this test teach you? |
| Tags | Multi-select | Face Test / Color Test / Text Test / Composition Test / Style Test |

**Views:**

- **All Tests** — Table, sorted by Swap Date descending
- **Winners** — Filter: Result = Significant Improvement or Slight Improvement
- **By What Changed** — Table, grouped by What Changed
- **Needs Follow-Up** — Filter: Winner = Too Early, Swap Date is more than 7 days ago
- **Learnings Library** — Table showing Test Name, What Changed, Winner, Learning

---

### 6. SEO Keyword Research

**Purpose:** Structured keyword research for every topic. Build a library of high-value keywords to inform your content strategy.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Keyword | Title | The exact search term |
| Search Volume | Select | High (10K+/mo) / Medium (1K–10K) / Low (100–1K) / Very Low (< 100) / Unknown |
| Competition | Select | Low / Medium / High / Very High |
| Opportunity Score | Select | 5 - Gold Mine / 4 - Strong / 3 - Decent / 2 - Tough / 1 - Avoid |
| Search Intent | Select | How-To / Review / Comparison / List / News / Entertainment / Tutorial / Troubleshooting |
| Your Current Ranking | Select | #1–3 / #4–10 / #11–20 / Not Ranking / Not Targeted Yet |
| Related Keywords | Text | Long-tail variations and related terms |
| Top Competing Videos | Text | Titles and channels currently ranking for this keyword |
| Gap / Angle | Text | What's missing from existing videos? What's your opportunity? |
| Video Ideas | Relation | → Video Ideas Bank (ideas targeting this keyword) |
| Source | Select | YouTube Search Suggest / TubeBuddy / vidIQ / Google Trends / Competitor Research / Comment Mining / Other |
| Date Researched | Date | |
| Notes | Text | |
| Tags | Multi-select | Evergreen / Trending / Seasonal / High Intent / Low Competition |

**Views:**

- **All Keywords** — Table, sorted by Opportunity Score descending
- **Gold Mine Keywords** — Filter: Opportunity Score = 5 or 4
- **Low Competition** — Filter: Competition = Low, Search Volume = Medium or High
- **Not Yet Targeted** — Filter: Your Current Ranking = Not Targeted Yet, Opportunity Score >= 3
- **By Search Intent** — Table, grouped by Search Intent
- **Trending** — Filter: Tags contains Trending

---

### 7. Sponsorship CRM

**Purpose:** Every brand deal from first contact to final payment. Never lose a sponsorship to a forgotten follow-up.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Brand Name | Title | Company or brand name |
| Contact Name | Text | Your point of contact |
| Contact Email | Email | |
| Contact LinkedIn | URL | |
| Agency | Text | If going through an agency |
| Deal Stage | Select | Lead / Pitched / Negotiation / Contracted / Content Creation / Review / Published / Paid / Lost / Declined |
| Deal Value | Number (USD) | Total compensation (cash + product value) |
| Cash Payment | Number (USD) | Cash portion |
| Product Value | Number (USD) | Value of free products received |
| Payment Terms | Select | Net 15 / Net 30 / Net 45 / Net 60 / On Publish / 50% Up Front / Custom |
| Payment Status | Select | Not Yet Due / Invoiced / Paid / Overdue / Partial |
| Invoice Sent Date | Date | |
| Payment Received Date | Date | |
| Deal Type | Select | Dedicated Video / Integration (30–60s) / Integration (60–90s) / Shorts / Affiliate / Long-term Ambassador / Product Placement / Other |
| Deliverables | Text | Exactly what you owe: video format, duration, talking points, links, social posts |
| Video | Relation | → Video Pipeline database |
| Draft Due Date | Date | When you owe the brand a draft for review |
| Publish Date | Date | Agreed publish date |
| Content Approved | Checkbox | Has the brand approved the final content? |
| Usage Rights | Text | What can the brand do with the content? Duration of rights? |
| Exclusivity | Text | Any exclusivity clauses? Competitor restrictions? |
| Contract | Files | Upload the contract or agreement |
| FTC Disclosure | Checkbox | Includes proper #ad or paid partnership disclosure |
| First Contact Date | Date | |
| Who Reached Out | Select | They Contacted Me / I Pitched Them / Mutual Introduction / Agency |
| Fit Rating | Select | 5 - Perfect Fit / 4 - Good / 3 - Acceptable / 2 - Stretch / 1 - Poor Fit |
| Notes | Text | Negotiation history, relationship notes |
| Tags | Multi-select | Repeat Partner / First Deal / Long-Term / Quick Turnaround / High Value / Low Effort |

**Views:**

- **Deal Pipeline** — Kanban, grouped by Deal Stage
- **All Deals** — Table, sorted by Publish Date ascending
- **Active Deals** — Filter: Deal Stage is Contracted or Content Creation or Review
- **Needs Follow-Up** — Filter: Deal Stage = Pitched or Negotiation, First Contact Date > 7 days ago
- **Revenue This Year** — Filter: Payment Status = Paid, Payment Received Date is this year
- **Overdue Payments** — Filter: Payment Status = Overdue or (Payment Status = Invoiced AND Invoice Sent Date > 30 days ago)
- **By Brand** — Table, sorted by Brand Name (for repeat partnership history)
- **Lost / Declined** — Filter: Deal Stage = Lost or Declined (for post-mortem analysis)

---

### 8. Revenue Tracker

**Purpose:** All income streams in one place. Know your actual earnings.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | "[Source] — [Month Year]" or "[Brand] — [Video]" |
| Date | Date | Payment or earning date |
| Revenue Source | Select | AdSense / Sponsorship / Affiliate / Merchandise / Memberships / Super Chat / Channel Memberships / Courses / Consulting / Other |
| Amount | Number (USD) | |
| Video | Relation | → Video Pipeline database (if attributable to a specific video) |
| Sponsorship | Relation | → Sponsorship CRM database (if from a brand deal) |
| Platform | Select | YouTube / Website / Gumroad / Shopify / Amazon / Other |
| Payment Method | Select | Direct Deposit / PayPal / Wire / Check / Other |
| Status | Select | Earned / Pending / Paid / Disputed |
| Notes | Text | |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")` |

**Views:**

- **All Revenue** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month
- **By Source** — Table, grouped by Revenue Source
- **By Month** — Table, grouped by Month
- **By Quarter** — Table, grouped by Quarter
- **Sponsorship Revenue** — Filter: Revenue Source = Sponsorship
- **AdSense Revenue** — Filter: Revenue Source = AdSense
- **Pending** — Filter: Status = Pending or Earned (not yet received)

---

## DASHBOARD

> Create this as the top-level Notion page. Pin it to your sidebar. This is your channel operations home base.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  YOUTUBE COMMAND CENTER                  April 2026           |
+--------------+--------------+--------------+-----------------+
|  Videos in   |  Publishing  |  Revenue     |  Sponsorship    |
|  Pipeline    |  This Month  |  This Month  |  Deals Active   |
|     6        |     4        |  $2,840      |     2           |
+--------------+--------------+--------------+-----------------+
|  PRODUCTION PIPELINE                                          |
|  [Linked view → Video Pipeline, Kanban by Production Stage]   |
+-------------------------------------------------------------+
|  UPCOMING UPLOADS                                             |
|  [Linked view → Video Pipeline, filter: Target Publish Date   |
|   is next 14 days, sorted by date ascending]                 |
+-----------------------------+-------------------------------+
|  RECENT PERFORMANCE         |  THUMBNAIL TESTS RUNNING       |
|  [Linked view → Analytics,  |  [Linked view → Thumbnail A/B, |
|   last 5 published videos]  |   filter: Winner = Too Early]  |
+-----------------------------+-------------------------------+
|  SPONSORSHIP PIPELINE                                         |
|  [Linked view → Sponsorship CRM, Kanban by Deal Stage]       |
+-------------------------------------------------------------+
|  REVENUE BY SOURCE (This Month)                               |
|  [Linked view → Revenue Tracker, grouped by Revenue Source,   |
|   filter: This Month]                                        |
+-------------------------------------------------------------+
```

### Dashboard Summary Stats

Four callout blocks side by side:

- **Videos in Pipeline** — Count from Video Pipeline where Production Stage is not Published or Cancelled
- **Publishing This Month** — Count from Video Pipeline where Target Publish Date is this month
- **Revenue This Month** — Sum from Revenue Tracker where Date is this month and Status = Paid
- **Active Sponsorships** — Count from Sponsorship CRM where Deal Stage = Contracted or Content Creation or Review

---

## KEY FORMULA REFERENCE

### Published on Time (Video Pipeline)
Tracks whether you're hitting your publish schedule. Consistency matters for the algorithm and your audience.

```
if(
  and(
    not(empty(prop("Actual Publish Date"))),
    not(empty(prop("Target Publish Date")))
  ),
  if(
    prop("Actual Publish Date") <= prop("Target Publish Date"),
    "On Time",
    "Late"
  ),
  ""
)
```

### CTR Change from Thumbnail Test
Measures the impact of a thumbnail swap. A positive number means the variant outperformed.

```
if(
  and(
    prop("Original CTR") > 0,
    prop("Variant CTR (7d)") > 0
  ),
  round((prop("Variant CTR (7d)") - prop("Original CTR")) * 100) / 100,
  0
)
```

### Views per Impression (Analytics Tracker)
A more nuanced performance metric than raw views. Shows how effectively your video converts impressions into views.

```
if(
  prop("Impressions (30d)") > 0,
  round(prop("Views (30d)") / prop("Impressions (30d)") * 1000) / 10,
  0
)
```

### Upload Checklist — All Complete
Prevents you from publishing with missing elements. Only returns true when every critical checklist item is done.

```
if(
  and(
    prop("Title Optimized"),
    prop("Description Written"),
    prop("Tags Added"),
    prop("Thumbnail Uploaded"),
    prop("End Screen Added"),
    prop("Cards Placed"),
    prop("Chapters/Timestamps"),
    prop("Pinned Comment"),
    prop("SEO Check")
  ),
  true,
  false
)
```

---

## QUICK-START GUIDE

### Step 1 — Dump Your Ideas (15 minutes)
- Open the **Video Ideas Bank** and add every video idea you currently have — from notes apps, bookmarks, voice memos, wherever they are
- Don't evaluate them yet. Just capture them with a working title and topic category
- After they're all in, go through and set Priority Score and Estimated Search Volume for each
- Your "High Priority" view now shows you what to work on next

### Step 2 — Set Up Your Production Pipeline (10 minutes)
- Open the **Video Pipeline** and add any videos currently in production
- Set the Production Stage, Target Publish Date, and link to the originating Idea
- The Kanban board is now your daily production view

### Step 3 — Create Upload Checklists (5 minutes)
- For each video in the pipeline, create a linked Upload Checklist entry
- Before every publish, work through the checklist item by item
- The "All Complete" formula tells you when you're clear to publish

### Step 4 — Seed Your Analytics (15 minutes)
- Open the **Analytics Tracker** and add your last 5–10 published videos
- Log 30-day metrics from YouTube Studio: views, watch time, CTR, avg view duration, subscribers gained
- Rate each video's performance
- Fill in "What Worked" and "What to Improve" — this becomes your strategic playbook

### Step 5 — Start Keyword Research (ongoing)
- Open the **SEO Keyword Research** database
- Add 10–20 keywords related to your content pillars
- Use YouTube Search Suggest, TubeBuddy, or vidIQ to estimate volume and competition
- Link keywords to relevant Video Ideas
- The "Gold Mine Keywords" view shows your best opportunities

### Step 6 — Set Up Sponsorship Tracking (if applicable)
- Add any active or past brand deals to the **Sponsorship CRM**
- Set deal stages, values, and key dates
- The pipeline Kanban is your sponsorship management view

### Step 7 — Initialize Revenue Tracking
- Add your last 3 months of revenue to the **Revenue Tracker** by source
- Going forward, log all income as it's earned or received
- The "By Source" and "By Month" views show your income diversification and trends

### Publishing Rhythm

**When you have an idea:**
- Add it to the Video Ideas Bank immediately — 30 seconds, working title and category only
- Come back later to score and evaluate it

**When starting a new video:**
- Move the top-priority idea from the Ideas Bank to the Video Pipeline
- Create an Upload Checklist entry linked to the video
- Set your Target Publish Date

**During production:**
- Update the Production Stage in the Pipeline as you progress
- The Kanban board should always reflect reality

**Before publishing:**
- Work through every item on the Upload Checklist
- Only publish when "All Complete" = true

**After publishing:**
- Log 7-day metrics in the Analytics Tracker
- Come back at 30 and 90 days to complete the picture
- Fill in "What Worked" and "What to Improve"

**Thumbnail testing (ongoing):**
- After a video's 7-day CTR stabilizes, consider testing a variant
- Log the test in the Thumbnail A/B Testing database
- Check results at 7 and 30 days
- Record your learning — these compound over time

### Pro Tips

- Your Content Pillars should be 3–5 topic areas that define your channel identity. Every video idea should map to a pillar. If an idea doesn't fit any pillar, either expand your pillars deliberately or save the idea for a different channel.
- The Upload Checklist is annoying for the first five uses and invaluable after that. Trust the process. Every creator forgets end screens, descriptions, or tags eventually.
- Log your "What Worked" notes while the video's performance is fresh. After 30 days, you won't remember what made that video special.
- Review your Thumbnail Testing log monthly. After 15–20 tests, patterns emerge. Most creators discover that 2–3 specific design choices account for most of their CTR variation.
- Track your "Published on Time" rate in the Video Pipeline. Consistency is one of the strongest growth signals on YouTube. If you're consistently late, adjust your production schedule rather than rushing.
- The Sponsorship CRM's "Fit Rating" property protects your channel long-term. A $5,000 deal from a brand your audience doesn't care about can cost you more in trust than it earns in revenue.
- Revenue tracking by source reveals your dependency risk. If 90% of your income is AdSense, one demonetization wave can destroy your livelihood. Diversify.
