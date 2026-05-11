# Social Media Content Planner — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked. Read the Quick-Start Guide at the bottom before entering any live content.

---

## DATABASES

---

### 1. Content Calendar

**Purpose:** Every post, reel, video, thread, story, and article you plan or publish — across every platform — lives here. This is the operational core of the system.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Title | Title | Working title or final caption headline |
| Platform | Select | Instagram / TikTok / YouTube / LinkedIn / X / Facebook / Pinterest / Threads |
| Content Type | Select | Reel / Static Post / Carousel / Story / Short-form Video / Long-form Video / Thread / Article / Newsletter / Podcast Clip |
| Content Pillar | Select | Educational / Promotional / Entertainment / Behind-the-Scenes / User-Generated / Engagement / Announcement |
| Format | Select | Tutorial / List / Opinion / Story / Review / Trend / Interview / Testimonial / Product Demo / Q&A |
| Status | Select | Idea / Brief / Scripting / Drafting / Filming / Editing / Review / Approved / Scheduled / Published / Archived |
| Publish Date | Date | Planned or actual publish date |
| Published At | Date | Exact timestamp — fill in at publish |
| Publish Month | Formula | `formatDate(prop("Publish Date"), "MMMM YYYY")` |
| Publish Week | Formula | `formatDate(prop("Publish Date"), "GGGG-[W]WW")` |
| Days Until Publish | Formula | `dateBetween(prop("Publish Date"), now(), "days")` |
| Overdue | Formula | `if(and(prop("Days Until Publish") < 0, prop("Status") != "Published", prop("Status") != "Archived"), true, false)` |
| Internal Deadline | Date | Production cutoff — set before Publish Date |
| Days Until Deadline | Formula | `dateBetween(prop("Internal Deadline"), now(), "days")` |
| Caption / Copy | Text | Full caption, script outline, or article body |
| Hook | Text | Opening line, visual hook, or first three seconds direction |
| CTA | Text | What action you want the audience to take |
| Hashtags | Text | Platform-appropriate hashtag set |
| Visual Notes | Text | Direction for graphic, thumbnail, or video cover |
| Audio / Music | Text | Sound name, track, or brief if applicable |
| Keywords | Text | SEO or search keywords for YouTube, Pinterest, LinkedIn |
| Tags | Multi-select | Evergreen / Trending / Seasonal / Repurposed / Sponsored / Series |
| Campaign | Relation | → Campaign Tracker |
| Analytics | Relation | → Analytics Log |
| Total Reach | Rollup | From linked Analytics entries — Reach field |
| Total Engagements | Rollup | From linked Analytics entries — Engagements field |
| Scheduled In | Select | Buffer / Later / Hootsuite / Sprout / Native / Manual |
| Assigned To | Person | For teams — who owns this piece |
| Review Needed | Checkbox | Flag for collaborator or approval sign-off |
| Notes | Text | Research links, references, ideas, revision notes |

**Views:**

- **Publishing Calendar** — Calendar view, date field = Publish Date
- **Content Pipeline** — Kanban, grouped by Status
- **All Content** — Table, sorted by Publish Date descending
- **This Week** — Filter: Publish Date is this week, sorted by Publish Date ascending
- **Scheduled Queue** — Filter: Status = Scheduled, sorted by Publish Date ascending
- **Overdue** — Filter: Overdue = true
- **Due in 3 Days** — Filter: Days Until Deadline <= 3 AND Status is not Scheduled or Published
- **Ideas Backlog** — Filter: Status = Idea, sorted by date created
- **Instagram** — Filter: Platform = Instagram
- **TikTok** — Filter: Platform = TikTok
- **YouTube** — Filter: Platform = YouTube
- **LinkedIn** — Filter: Platform = LinkedIn
- **X** — Filter: Platform = X
- **Published** — Filter: Status = Published, sorted by Published At descending

---

### 2. Platform Accounts

**Purpose:** One record per platform you manage. Tracks strategic context, audience benchmarks, and monthly performance so your planning stays intentional rather than reactive.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Platform | Title | Instagram / TikTok / YouTube / LinkedIn / X / etc. |
| Account Name | Text | Handle or channel name |
| Profile URL | URL | Direct link to the profile or channel |
| Active | Checkbox | Currently publishing to this platform? |
| Account Type | Select | Personal Brand / Business / Creator / Client |
| Primary Audience | Text | Who follows this account — demographics and interests |
| Content Pillars | Text | 3-5 core topic areas for this platform |
| Post Frequency Target | Select | Daily / 5x Week / 3x Week / 2x Week / Weekly / Bi-weekly |
| Best Days to Post | Text | e.g., Tuesday, Thursday, Saturday |
| Best Times to Post | Text | Peak engagement windows in your audience's timezone |
| Current Followers | Number | Update monthly |
| Follower Goal (90 days) | Number | Target follower count 90 days out |
| Avg Engagement Rate % | Number | Your current baseline — update monthly |
| Engagement Rate Goal % | Number | Target engagement rate |
| Monthly Impressions | Number | Update monthly from platform analytics |
| Monthly Link Clicks | Number | Update monthly |
| Platform Notes | Text | What's working, what to test, algorithm observations |
| Last Updated | Date | When you last refreshed the metrics on this record |

**Views:**

- **All Accounts** — Table, sorted by Active descending
- **Active Platforms** — Filter: Active = true
- **By Frequency** — Grouped by Post Frequency Target
- **Performance Overview** — Table showing Current Followers, Avg Engagement Rate %, Monthly Impressions side by side

---

### 3. Campaign Tracker

**Purpose:** Coordinate multi-post content campaigns, product launches, promotions, and ongoing content series across platforms. Each campaign groups its associated Content Calendar posts and tracks overall progress.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Campaign Name | Title | Name of the campaign, launch, or series |
| Campaign Type | Select | Product Launch / Promotion / Content Series / Brand Awareness / Event / Collab / Seasonal |
| Status | Select | Planning / Active / Paused / Complete / Cancelled |
| Priority | Select | High / Medium / Low |
| Campaign Goal | Text | What success looks like — in concrete terms |
| Primary CTA | Text | The action you want audiences to take across this campaign |
| Target Platforms | Multi-select | Instagram / TikTok / YouTube / LinkedIn / X / Facebook |
| Start Date | Date | First post goes live |
| End Date | Date | Last post or campaign wrap date |
| Duration (days) | Formula | `dateBetween(prop("End Date"), prop("Start Date"), "days")` |
| Days Remaining | Formula | `dateBetween(prop("End Date"), now(), "days")` |
| Posts in Campaign | Relation | → Content Calendar |
| Total Posts Planned | Rollup | Count of linked Content Calendar entries |
| Posts Published | Rollup | Count of linked entries where Status = Published |
| Budget | Number | Spend allocated (paid promotion, creative, tools) |
| Revenue Target | Number | Expected revenue or conversion goal if applicable |
| Landing Page / Link | URL | Campaign destination URL |
| Collab Partner | Text | If applicable — partner name and account |
| Notes | Text | Brief, key decisions, post-campaign observations |

**Views:**

- **Campaign Board** — Kanban, grouped by Status
- **Active Campaigns** — Filter: Status = Active, sorted by End Date ascending
- **Upcoming** — Filter: Status = Planning, sorted by Start Date ascending
- **Campaign Calendar** — Calendar view, date field = Start Date
- **All Campaigns** — Table, sorted by Start Date descending

---

### 4. Analytics Log

**Purpose:** Bring your performance numbers out of each platform's native dashboard and into a single searchable record. Log a snapshot for each post at 7 days and 30 days post-publish to track both early momentum and long-term performance.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | "[Post Title] — [Snapshot Date]" e.g., "Morning Routine Reel — 2026-04-16" |
| Content | Relation | → Content Calendar |
| Platform | Rollup | From linked Content Calendar entry |
| Content Type | Rollup | From linked Content Calendar entry |
| Snapshot Date | Date | Date you pulled these numbers |
| Snapshot Type | Select | 7-Day / 30-Day / 90-Day / Final |
| Impressions / Views | Number | Total impressions or video views |
| Reach | Number | Unique accounts reached |
| Profile Visits | Number | |
| Likes | Number | |
| Comments | Number | |
| Shares | Number | |
| Saves | Number | Instagram saves or YouTube saves |
| Story Replies | Number | Instagram Stories: direct replies |
| Link Clicks | Number | Bio link or in-content link clicks attributed to this post |
| Followers Gained | Number | New follows attributed to this post |
| Watch Time (min) | Number | YouTube and TikTok: total watch time |
| Avg View Duration (sec) | Number | Average time watched before exit |
| Click-Through Rate % | Number | YouTube: CTR from impressions to views |
| Conversions | Number | Sales, signups, downloads, or other goal completions |
| Revenue Attributed | Number | Revenue tied to this post (if tracked) |
| Engagements | Formula | `prop("Likes") + prop("Comments") + prop("Shares") + prop("Saves")` |
| Engagement Rate % | Formula | `round((prop("Engagements") / prop("Reach")) * 100, 2)` |
| Save Rate % | Formula | `round((prop("Saves") / prop("Reach")) * 100, 2)` |
| Share Rate % | Formula | `round((prop("Shares") / prop("Reach")) * 100, 2)` |
| Notes | Text | What drove performance, audience reactions, what to repeat or avoid |

**Views:**

- **All Analytics** — Table, sorted by Snapshot Date descending
- **Best Performers (Reach)** — Sort by Reach descending
- **Best Performers (Engagement)** — Sort by Engagement Rate % descending
- **Best Savers** — Sort by Save Rate % descending
- **By Platform** — Grouped by Platform
- **30-Day Snapshots** — Filter: Snapshot Type = 30-Day
- **Needs 30-Day Pull** — Content published 28-35 days ago without a 30-day entry (manual check view)
- **High Conversion** — Sort by Conversions descending

---

## DASHBOARD LAYOUT

```
┌──────────────────────────────────────────────────────────────────┐
│  SOCIAL MEDIA COMMAND CENTER                       April 2026    │
├────────────────┬────────────────┬────────────────┬───────────────┤
│  This Week     │  Scheduled     │  Active        │  Ideas        │
│  Publishing    │  Total         │  Campaigns     │  in Backlog   │
│      4         │     18         │      2         │     34        │
├────────────────┴────────────────┴────────────────┴───────────────┤
│  THIS WEEK'S CONTENT                                              │
│  [Linked view → Content Calendar, filter: Publish Date This Week]│
├──────────────────────────────────────────────────────────────────┤
│  CONTENT PIPELINE (by Status)                                     │
│  [Linked view → Content Calendar, Kanban by Status]              │
├──────────────────────────────────────────────────────────────────┤
│  DUE SOON — Internal deadlines within 3 days                     │
│  [Linked view → Content Calendar, filter: Days Until Deadline≤3] │
├──────────────────────────────────────────────────────────────────┤
│  ACTIVE CAMPAIGNS                                                 │
│  [Linked view → Campaign Tracker, filter: Status = Active]       │
├──────────────────────────────────────────────────────────────────┤
│  PLATFORM OVERVIEW                                                │
│  [Linked view → Platform Accounts, filter: Active = true]        │
├──────────────────────────────────────────────────────────────────┤
│  TOP PERFORMERS — Last 30 days                                    │
│  [Linked view → Analytics Log, sort: Engagement Rate % desc]     │
└──────────────────────────────────────────────────────────────────┘
```

**How to build this in Notion:**
1. Create a new Notion page and name it "Social Media Command Center"
2. Add four **Callout** blocks at the top for the four stat counters — update these manually each week or use linked database count views
3. Below each section heading, use **Linked Database** (type `/linked` in Notion) to embed filtered/sorted views of each database directly on the dashboard page
4. Each linked view should display no more than 5-8 rows to keep the dashboard scannable — click "see all" to open the full database

---

## KEY FORMULAS

### Posting Frequency (in Platform Accounts)
Track how often you're actually posting versus your target. Add this as a formula property in Platform Accounts after connecting it to Content Calendar via relation and rollup:

```
// Posts Published This Month (Rollup count → Content Calendar filtered to this platform and current month)
// Then compare to monthly target:

if(prop("Posts This Month") >= prop("Monthly Target"), "On Track",
  if(prop("Posts This Month") >= (prop("Monthly Target") * 0.75), "Slightly Behind",
  "Behind — Review Schedule"))
```

### Engagement Rate (in Analytics Log)
Measures how actively an audience interacted with a post relative to how many people it reached:

```
round((prop("Engagements") / prop("Reach")) * 100, 2)
```

**Benchmark reference:**
- Instagram: 1–3% average, 3–6% good, 6%+ excellent
- TikTok: 4–8% average, 8–15% good, 15%+ excellent
- LinkedIn: 1–2% average, 2–5% good
- YouTube: Measured by likes/views ratio — 2%+ is strong

### Save Rate % (in Analytics Log)
Saves are the highest-signal engagement action on Instagram and indicate content audiences find genuinely useful or want to return to:

```
round((prop("Saves") / prop("Reach")) * 100, 2)
```

**Benchmark:** 1%+ save rate on Instagram signals strong content value; 3%+ is exceptional.

### Share Rate % (in Analytics Log)
Shares and reposts indicate content that audiences feel compelled to send to others — the strongest organic growth signal:

```
round((prop("Shares") / prop("Reach")) * 100, 2)
```

### Content Mix % (manual calculation — use Monthly Review page)
Track what percentage of your published content falls into each pillar to avoid over-indexing on promotional content:

```
Content Pillar % = (Posts with this pillar this month / Total posts this month) × 100
```

**Recommended content mix for most creator/brand accounts:**
- Educational: 40%
- Entertainment: 25%
- Engagement (polls, Q&As, questions): 15%
- Behind-the-Scenes / Personal: 10%
- Promotional: 10% or less

Adjust these ratios based on your account type and goals. A business account during a product launch may run 25% promotional for that month.

### Days Until Publish (in Content Calendar)
Auto-flags urgency for upcoming posts:

```
dateBetween(prop("Publish Date"), now(), "days")
```

Negative values = overdue. Use this to create a filtered "Needs Attention" view.

### Overdue Flag (in Content Calendar)
Auto-detects posts that are past their publish date and not yet live:

```
if(and(prop("Days Until Publish") < 0, prop("Status") != "Published", prop("Status") != "Archived"), true, false)
```

---

## WEEKLY PLANNING TEMPLATE

Copy this block into a new Notion page at the start of each week:

```
## Week of [Date Range] — Content Plan

### Publishing This Week
| Day       | Platform   | Content Title                     | Status     |
|-----------|------------|-----------------------------------|------------|
| Monday    |            |                                   |            |
| Tuesday   |            |                                   |            |
| Wednesday |            |                                   |            |
| Thursday  |            |                                   |            |
| Friday    |            |                                   |            |
| Saturday  |            |                                   |            |
| Sunday    |            |                                   |            |

### In Production This Week
- [ ] [Post title] — [Platform] — due [date]
- [ ] [Post title] — [Platform] — due [date]
- [ ] [Post title] — [Platform] — due [date]

### Active Campaign Check-in
Campaign: [Name]
- Posts live this week:
- Posts still needed:
- On track? Y / N

### Ideas to Brief This Week
-
-

### This Week's Priority Platform
[Which platform gets the most creative energy this week, and why?]

### End-of-Week Reflection
- What published?
- What didn't get done, and why?
- Early performance signals worth noting:
- One thing to carry forward or change next week:
```

---

## MONTHLY REVIEW TEMPLATE

Copy this block into a new Notion page at the end of each month:

```
## [Month Year] — Social Media Monthly Review

### Publishing Summary
| Platform   | Target Posts | Actual Posts | Hit Target? |
|------------|-------------|--------------|-------------|
| Instagram  |             |              |             |
| TikTok     |             |              |             |
| YouTube    |             |              |             |
| LinkedIn   |             |              |             |
| X          |             |              |             |
| Total      |             |              |             |

### Content Mix This Month
| Pillar          | Posts | % of Total | Target % |
|-----------------|-------|------------|----------|
| Educational     |       |            | 40%      |
| Entertainment   |       |            | 25%      |
| Engagement      |       |            | 15%      |
| Behind-Scenes   |       |            | 10%      |
| Promotional     |       |            | 10%      |

### Best Performing Post
Title:
Platform:
Reach:
Engagement Rate %:
Why it worked:

### Worst Performing Post
Title:
Platform:
What I'd do differently:

### Platform Follower Counts — End of Month
| Platform   | Start of Month | End of Month | Change |
|------------|---------------|-------------|--------|
| Instagram  |               |             |        |
| TikTok     |               |             |        |
| YouTube    |               |             |        |
| LinkedIn   |               |             |        |
| X          |               |             |        |

### Campaign Results
Campaign:
Goal:
Result:
Key learning:

### Next Month Focus
- Primary platform:
- Content theme or series:
- One thing to test:
- One thing to stop doing:
```

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Platform Accounts
Open the **Platform Accounts** database and create one record for each platform you actively use. Fill in your handle, profile URL, current follower count, posting frequency target, content pillars, and best times to post. This is your strategic foundation — everything in the Content Calendar and Campaign Tracker connects to these records. Delete platform options from Content Calendar select lists that don't apply to you to keep the interface clean.

### Step 2 — Define Your Content Pillars
Before adding any content, decide on 3–5 content pillars per platform — the recurring topic areas your account is known for. Add these to the Platform Account records. Having defined pillars makes every content planning decision faster: instead of staring at a blank page, you're choosing which pillar to serve this week and in which format.

### Step 3 — Brain-Dump Into the Ideas Backlog
Use the **Ideas Backlog** view in the Content Calendar to capture every content idea you currently have, without filtering. Add a rough platform, content type, and pillar tag to each. Don't worry about dates yet — you're just clearing your head and building your idea inventory. A healthy backlog means you'll never sit down for a planning session with nothing to work from.

### Step 4 — Plan Your First Month
Open the **Publishing Calendar** view in the Content Calendar. Start assigning publish dates to your best ideas and moving their status to "Brief" or "Scripting." Aim to get at least two weeks of content planned before you start producing anything. Use the **Weekly Planning Template** to think through each week's schedule in detail. The calendar view will show you immediately whether your posting frequency targets are realistic given your production capacity.

### Step 5 — Set Up Active Campaigns
If you have a product launch, promotion, content series, or seasonal campaign coming up, add it to the **Campaign Tracker** now. Fill in the start and end dates, platforms, goal, and primary CTA. Then link the individual Content Calendar posts to the campaign as you create them. This gives you a bird's-eye view of multi-platform campaign execution and surfaces gaps — missing platforms, days without content, posts not yet assigned.

### Step 6 — Log Analytics on a Schedule
After a post publishes, set a reminder for 7 days and 30 days out to pull metrics from the native platform dashboard and log them in the **Analytics Log**. The first time you do this it feels like extra work. By month three, you'll have a performance database that tells you exactly which content types, formats, hooks, and posting times perform best on each platform — intelligence that would take years to build any other way. Use the monthly content mix calculation during your Monthly Review to check whether your pillar distribution is aligned with your growth goals.

---

## PLATFORM-SPECIFIC PROPERTY GUIDANCE

### Instagram
- Content Types to use: Reel, Static Post, Carousel, Story
- Key metrics to log: Reach, Saves, Shares, Link Clicks, Followers Gained
- Highest-signal metric: Save Rate % — indicates genuinely useful content
- Posting frequency benchmark: 4–7 Reels/week for growth; 3–5 feed posts/week for brand accounts

### TikTok
- Content Types to use: Short-form Video (under 60 sec), Long-form Video (1–10 min)
- Key metrics to log: Views, Watch Time, Shares, Followers Gained
- Highest-signal metric: Share Rate % and completion rate (Avg View Duration / total length)
- Posting frequency benchmark: 1–3 posts/day for aggressive growth; 5–7/week for sustainable pace

### YouTube
- Content Types to use: Long-form Video, Short-form Video (Shorts)
- Key metrics to log: Impressions, Views, Click-Through Rate %, Avg View Duration, Watch Time
- Highest-signal metric: Click-Through Rate % (CTR) from impressions — reflects thumbnail and title strength
- Posting frequency benchmark: 1–2 long-form/week; Shorts can be daily or repurposed from other platforms

### LinkedIn
- Content Types to use: Article, Thread (text post), Carousel (PDF), Static Post
- Key metrics to log: Impressions, Reactions, Comments, Shares, Profile Visits, Link Clicks
- Highest-signal metric: Comments — LinkedIn's algorithm heavily rewards comment velocity in the first hour
- Posting frequency benchmark: 3–5 posts/week; consistency matters more than volume

### X (Twitter)
- Content Types to use: Thread, Static Post (single tweet), Poll
- Key metrics to log: Impressions, Engagements, Link Clicks, Profile Visits, Follows
- Highest-signal metric: Engagements / Impressions ratio — reply rate signals resonance
- Posting frequency benchmark: 1–5 posts/day; threads 2–4 times/week for topic authority
