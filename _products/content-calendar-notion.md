# Content Creator Editorial Calendar — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked. Review the Quick-Start Guide at the bottom before entering live content.

---

## DATABASES

---

### 1. Content Master Database

**Purpose:** Every piece of content you create, plan, or publish — across all platforms — lives here.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Title | Title | Working or final title of the piece |
| Platform | Select | YouTube / Instagram / TikTok / Blog / Newsletter / Twitter-X / LinkedIn / Pinterest / Podcast |
| Content Type | Select | Long-form Video / Short-form Video / Reel / Static Post / Carousel / Story / Blog Post / Newsletter / Thread / Podcast Episode / Infographic |
| Format | Select | Tutorial / Review / Vlog / Interview / List / Story / Opinion / Case Study / Behind-the-Scenes / UGC-Response |
| Status | Select | Idea / Research / Scripting / Drafting / Filming / Editing / Review / Scheduled / Published / Archived |
| Priority | Select | High / Medium / Low |
| Publish Date | Date | Scheduled or actual publish date |
| Published At | Date | Actual publish timestamp (fill in on publish) |
| Month | Formula | `formatDate(prop("Publish Date"), "MMMM YYYY")` |
| Week | Formula | `formatDate(prop("Publish Date"), "W")` |
| Topic / Series | Multi-select | Productivity / Finance / Travel / Tutorial / Personal / Collab / Sponsored / Series Name |
| Tags | Multi-select | Evergreen / Trending / Seasonal / SEO / Repurposed |
| Hook | Text | The opening line or visual hook |
| Key Message | Text | The one thing viewers/readers should take away |
| CTA | Text | What you want the audience to do (subscribe, click, buy, reply) |
| Script / Draft | Text | Full script, outline, or blog draft |
| Thumbnail Notes | Text | Visual direction or reference for thumbnail/cover image |
| Notes | Text | Research links, references, ideas, feedback |
| Deadline | Date | Internal deadline (before publish date) |
| Days Until Deadline | Formula | `dateBetween(prop("Deadline"), now(), "days")` |
| Sponsor / Brand Deal | Text | Brand name if sponsored |
| Sponsored | Checkbox | Is this paid/sponsored content? |
| Repurposed From | Relation | → Content Master Database (self-referential) |
| Repurposed Into | Relation | → Content Master Database (self-referential) |
| Analytics | Relation | → Analytics Log |
| Total Views | Rollup | From linked Analytics entries |
| Total Engagements | Rollup | From linked Analytics entries |
| Assigned To | Person | For teams with multiple creators |
| Review Needed | Checkbox | Flag for collaborator or editor review |

**Views:**
- **All Content** — Table, sorted by Publish Date descending
- **Content Pipeline** — Kanban, grouped by Status
- **Calendar** — Calendar view, date field = Publish Date
- **This Week** — Filter: Publish Date is this week
- **This Month** — Filter: Publish Date is this month
- **Scheduled Queue** — Filter: Status = Scheduled, sorted by Publish Date ascending
- **Published** — Filter: Status = Published
- **Ideas Bank** — Filter: Status = Idea
- **Needs Work** — Filter: Days Until Deadline <= 3 AND Status is not Scheduled/Published

---

### 2. Platform Tracker

**Purpose:** Platform-level strategy, goals, and performance benchmarks.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Platform | Title | YouTube / Instagram / TikTok / Blog / Newsletter / etc. |
| Active | Checkbox | Currently publishing to this platform? |
| Handle / URL | URL | Your profile link |
| Current Followers | Number | Update monthly |
| Follower Goal (Q) | Number | Quarterly follower target |
| Post Frequency | Select | Daily / 3x Week / 2x Week / Weekly / Bi-weekly / Monthly |
| Best Times to Post | Text | Peak engagement windows |
| Content Pillars | Text | 3-5 main topics for this platform |
| Current Strategy Notes | Text | What's working, what to test |
| Notes | Text | |

---

### 3. Repurposing Tracker

**Purpose:** Map how one piece of content becomes many.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Original Piece | Title | Name of the source content |
| Source Platform | Select | Where the original lives |
| Source Link | URL | Link to original published piece |
| Derivative 1 | Text | First repurposed format/platform |
| Derivative 1 Status | Select | Idea / In Progress / Done |
| Derivative 2 | Text | |
| Derivative 2 Status | Select | Idea / In Progress / Done |
| Derivative 3 | Text | |
| Derivative 3 Status | Select | Idea / In Progress / Done |
| Derivative 4 | Text | |
| Derivative 4 Status | Select | Idea / In Progress / Done |
| Derivative 5 | Text | |
| Derivative 5 Status | Select | Idea / In Progress / Done |
| Repurpose Priority | Select | High / Medium / Low |
| Notes | Text | |

**Example repurposing map:**
```
YouTube Long-form Video (30 min)
  → YouTube Short (60 sec highlight)
  → Instagram Reel (30 sec hook clip)
  → TikTok (same reel or variation)
  → Blog post (transcript + expanded)
  → Newsletter (summary + key takeaways)
  → Twitter/X thread (5-7 tweet breakdown)
  → Pinterest infographic (stats or steps)
  → LinkedIn post (professional angle)
```

---

### 4. Analytics Log

**Purpose:** Track performance metrics for every published piece over time.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | "[Content Title] — [Date Snapshot]" |
| Content | Relation | → Content Master Database |
| Platform | Rollup | From Content |
| Snapshot Date | Date | When you pulled these numbers |
| Days Since Publish | Formula | `dateBetween(prop("Snapshot Date"), prop("Publish Date Rollup"), "days")` |
| Views / Impressions | Number | |
| Watch Time (min) | Number | YouTube: total watch time |
| Avg View Duration | Number | YouTube: average view duration in seconds |
| Click-through Rate | Number | YouTube: CTR % |
| Likes | Number | |
| Comments | Number | |
| Shares / Reposts | Number | |
| Saves | Number | |
| Followers Gained | Number | Attributed to this piece |
| Link Clicks | Number | Bio link or in-content link clicks |
| Conversions | Number | Sales, signups, or other goal completions |
| Revenue Attributed | Number | If applicable |
| Engagement Rate % | Formula | `round(((prop("Likes") + prop("Comments") + prop("Shares / Reposts") + prop("Saves")) / prop("Views / Impressions")) * 100, 2)` |
| Notes | Text | What drove performance? What to repeat or avoid? |

**Views:**
- **All Analytics** — Table, sorted by Snapshot Date descending
- **Best Performers** — Sort by Views descending
- **By Platform** — Grouped by Platform
- **High Engagement** — Sort by Engagement Rate % descending
- **Conversion Tracking** — Sort by Conversions descending

---

### 5. Content Idea Bank

**Purpose:** Capture ideas the moment they arrive, without cluttering your active content pipeline.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Idea | Title | Quick idea description |
| Platform Fit | Multi-select | Which platforms could this work for? |
| Type | Select | Tutorial / Story / Opinion / Review / List / etc. |
| Inspiration Source | Text | Where did this idea come from? |
| Reference Links | URL | Competitor content, articles, or examples |
| Urgency | Select | Evergreen / Timely / Seasonal |
| Season / Event | Text | If tied to a date or event |
| Promoted to Pipeline | Checkbox | Flip when added to Content Master |
| Notes | Text | |

**Views:**
- **All Ideas** — Table, sorted by date created
- **Ready to Develop** — Filter: Promoted to Pipeline = false, sorted by Urgency
- **Evergreen Bank** — Filter: Urgency = Evergreen
- **Seasonal Ideas** — Filter: Urgency = Seasonal

---

## DASHBOARD

### Weekly Planning View

```
┌─────────────────────────────────────────────────────────┐
│  CONTENT HQ                              April 2024     │
├──────────────┬──────────────┬──────────────┬────────────┤
│  This Week   │  Scheduled   │  Ideas Bank  │ Publishing │
│  Publishing  │   Total      │    Total     │  Streak    │
│      3       │     12       │     47       │  14 days   │
├──────────────┴──────────────┴──────────────┴────────────┤
│  THIS WEEK'S CONTENT                                     │
│  [Linked view → Content Master, filter: This Week]      │
├─────────────────────────────────────────────────────────┤
│  CONTENT PIPELINE                                        │
│  [Linked view → Content Master, Kanban by Status]       │
├─────────────────────────────────────────────────────────┤
│  DUE SOON (3 days)                                      │
│  [Linked view → Content, filter: Days Until Deadline≤3] │
├─────────────────────────────────────────────────────────┤
│  TOP PERFORMING (last 30 days)                          │
│  [Linked view → Analytics, sort: Views desc]            │
├─────────────────────────────────────────────────────────┤
│  REPURPOSING OPPORTUNITIES                              │
│  [Linked view → Repurposing Tracker, In Progress]       │
└─────────────────────────────────────────────────────────┘
```

---

## PLANNING TEMPLATES

### Weekly Planning Template
Copy this into a Notion page each Monday:

```
## Week of [Date] — Content Plan

### Publishing This Week
| Day       | Platform     | Title                    | Status    |
|-----------|-------------|--------------------------|-----------|
| Monday    |             |                          |           |
| Tuesday   |             |                          |           |
| Wednesday |             |                          |           |
| Thursday  |             |                          |           |
| Friday    |             |                          |           |
| Saturday  |             |                          |           |
| Sunday    |             |                          |           |

### In Production This Week
- [ ] [Content piece] — deadline [date]
- [ ] [Content piece] — deadline [date]
- [ ] [Content piece] — deadline [date]

### Ideas to Develop
-
-

### Repurposing in Progress
-
-

### This Week's Goal
[One sentence: what does a successful content week look like?]

### Reflection (fill in on Friday)
- What published?
- What didn't get done and why?
- What early signals look promising?
- What to carry forward or change next week?
```

---

### Monthly Planning Template
Copy this at the start of each month:

```
## [Month Year] Content Plan

### Monthly Theme / Focus
[What is the overarching theme or campaign this month?]

### Publishing Goals by Platform
| Platform    | Target # | Actual | Notes |
|-------------|----------|--------|-------|
| YouTube     |          |        |       |
| Instagram   |          |        |       |
| TikTok      |          |        |       |
| Blog        |          |        |       |
| Newsletter  |          |        |       |

### Hero Content This Month
[1-2 big pieces that anchor the month]

### Growth Focus
[What metric or platform are you prioritizing for growth?]

### Collaboration / Sponsorship
[Any planned collabs or brand deals?]

### End-of-Month Review
- Total pieces published:
- Best performing piece:
- Biggest lesson:
- Carries into next month:
```

---

## CONTENT CREATION CHECKLISTS

### Pre-Production Checklist
- [ ] Idea validated (searched for similar content, confirmed demand)
- [ ] Title / headline written (with keywords)
- [ ] Hook written (first 3 seconds / first sentence)
- [ ] Outline or script complete
- [ ] Research done, sources noted
- [ ] CTA decided
- [ ] Thumbnail / cover image direction noted
- [ ] Deadline set in database

### Post-Production Checklist
- [ ] Edited and reviewed
- [ ] Thumbnail / graphic created
- [ ] Description / caption written with keywords
- [ ] Hashtags selected (platform-appropriate)
- [ ] Links updated (bio link, pinned comment, etc.)
- [ ] Scheduled in platform or native scheduler
- [ ] Status updated to "Scheduled" in Notion

### Post-Publish Checklist (within 1 hour of publishing)
- [ ] Share to Stories / cross-post where appropriate
- [ ] Respond to early comments
- [ ] Pin top comment (YouTube / Instagram)
- [ ] Share in community / newsletter teaser
- [ ] Note publish time in database

### 30-Day Analytics Pull
- [ ] Log views, engagement, saves, clicks in Analytics Log
- [ ] Note any outlier performance (high or low)
- [ ] Identify repurposing opportunities
- [ ] Add lessons to Platform Tracker notes

---

## QUICK-START GUIDE

### Step 1 — Customize Your Platforms
- Open the **Platform Tracker** and add only the platforms you actively use
- Fill in your handle, current follower count, posting frequency, and content pillars for each
- Delete platform options from the Content Master select list that don't apply to you

### Step 2 — Populate Your Ideas Bank
- Before adding anything to your pipeline, brain-dump all current content ideas into the **Idea Bank**
- Don't filter yourself — capture everything, then sort by priority
- Ideas marked "Promoted to Pipeline" can then be moved into the Content Master

### Step 3 — Set Up Your Month
- Use the **Monthly Planning Template** to define your publishing goals per platform
- Add your confirmed content pieces to the Content Master Database with Publish Dates
- The Calendar view will immediately show your publishing schedule visually

### Step 4 — Use the Pipeline View Daily
- Every day, open the Kanban view (Content Pipeline) to see what's in each stage
- Move cards forward as you complete production stages
- If a card sits in one column for more than 3 days, something is blocked — investigate

### Step 5 — Track Analytics Monthly
- One month after each piece publishes, add an Analytics Log entry
- This habit builds a performance baseline and shows you what to repeat

### Step 6 — Repurpose Systematically
- After a piece performs well, open the Repurposing Tracker and map out derivative content
- Repurposing is where content creators multiply output without multiplying effort

### Pro Tips
- Use the "Hook" property to force yourself to write your hook before anything else — it clarifies the whole piece
- Keep your Ideas Bank in the habit of being large. Great ideas often come in clusters; capture them all
- Use Tags like "Evergreen" to flag content that can be reshared or promoted long after publish date
- For sponsored content, use the Sponsored checkbox and Sponsor field — useful for tracking brand deal history
- If you have a team or editor, use the "Review Needed" checkbox and "Assigned To" property to manage handoffs
