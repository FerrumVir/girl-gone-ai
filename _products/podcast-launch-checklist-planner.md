# Podcast Launch & Management System — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with production workflow tracking, guest pipeline management, and publishing checklists built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Episodes

**Purpose:** Master record for every episode — planned, in production, and published. Tracks the full lifecycle from concept to live, with performance metrics after publishing.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Episode Title | Title | Working or final title |
| Episode Number | Number | Sequential episode number |
| Season | Select | Season 1 / Season 2 / Season 3 / Bonus / Trailer / Mini-series |
| Status | Select | Idea / Outlined / Scheduled / Recording / Editing / Review / Scheduled to Publish / Published / Shelved |
| Format | Select | Solo / Interview / Co-hosted / Panel / Q&A / Narrative / Minisode / Bonus |
| Topic | Text | Core topic or angle |
| Category | Multi-select | Business / Marketing / Productivity / Interviews / Storytelling / Education / News / Personal / Behind-the-Scenes |
| Guest | Relation | -> Guest Pipeline database |
| Guest Name | Rollup | From Guest relation |
| Recording Date | Date | When it was/will be recorded |
| Edit Deadline | Date | When editing must be complete |
| Publish Date | Date | Scheduled or actual publish date |
| Days Until Publish | Formula | `if(empty(prop("Publish Date")), "No date", if(prop("Publish Date") < now(), "Published", format(dateBetween(prop("Publish Date"), now(), "days")) + " days"))` |
| Duration (min) | Number | Final episode length in minutes |
| File Size (MB) | Number | Final audio file size |
| Outline | Text | Episode structure: hook, segments, key points, CTA |
| Key Takeaways | Text | 3-5 main points listeners will get |
| Show Notes | Text | Full show notes for publishing |
| Timestamps | Text | Formatted timestamps for description |
| Transcript | Checkbox | Has transcript been generated? |
| Links & Resources | Text | URLs mentioned in episode |
| Call to Action | Text | What should listeners do after this episode? |
| Episode URL | URL | Published episode link |
| Apple Podcasts URL | URL | Direct Apple link for sharing |
| Spotify URL | URL | Direct Spotify link |
| Downloads (7 day) | Number | First 7-day download count |
| Downloads (30 day) | Number | 30-day download count |
| Downloads (total) | Number | All-time downloads |
| Performance | Formula | `if(prop("Downloads (7 day)") == 0, "No data", if(prop("Downloads (7 day)") > prop("Avg 7 Day Downloads"), "Above Average", "Below Average"))` |
| Avg 7 Day Downloads | Number | Your show's 7-day average (update monthly) |
| Rating/Reviews Mentioned | Text | Any reviews that referenced this episode |
| Repurposed | Multi-select | Blog Post / Newsletter / Twitter Thread / Instagram Reel / YouTube / TikTok / LinkedIn / Audiogram |
| Notes | Text | Production notes, feedback, lessons learned |
| Tags | Multi-select | Evergreen / Timely / Viral Potential / Sponsor-Friendly / Portfolio Piece / Needs Update |

**Views:**

- **Production Pipeline** — Board, grouped by Status (main working view)
- **All Episodes** — Table, sorted by Episode Number descending
- **Publishing Queue** — Filter: Status = Scheduled to Publish, sorted by Publish Date ascending
- **Recording Schedule** — Filter: Status = Scheduled or Recording, sorted by Recording Date
- **Ideas Backlog** — Filter: Status = Idea, sorted by date added
- **Published** — Filter: Status = Published, sorted by Publish Date descending
- **By Performance** — Table, sorted by Downloads (7 day) descending
- **Calendar** — Calendar view by Publish Date
- **With Guests** — Filter: Guest is not empty
- **Needs Editing** — Filter: Status = Recording (recording done, needs edit)
- **Evergreen Content** — Filter: Tags contains Evergreen
- **Repurposing Queue** — Filter: Status = Published AND Repurposed is empty

---

### 2. Guest Pipeline

**Purpose:** Manages the full guest lifecycle — from dream list through outreach, booking, recording, and post-episode relationship maintenance. Tracks communication history and avoids double-booking or lost outreach.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Guest Name | Title | Full name |
| Email | Email | Primary contact |
| Website | URL | Personal or business site |
| LinkedIn | URL | Profile URL |
| Twitter/X | URL | Handle for tagging/sharing |
| Instagram | URL | For cross-promotion |
| Status | Select | Dream List / Researching / Outreach Sent / Follow-Up / Confirmed / Scheduled / Recorded / Published / Declined / No Response |
| Priority | Select | A-List (hard to get) / Strong Target / Good Fit / Maybe / Cold |
| Expertise | Text | What they're known for, what angle to pursue |
| Why This Guest | Text | What value they bring to YOUR audience specifically |
| Audience Overlap | Select | High / Medium / Low / Unknown |
| Their Audience Size | Select | 1K-10K / 10K-50K / 50K-100K / 100K-500K / 500K+ / Unknown |
| Outreach Date | Date | When first message was sent |
| Outreach Method | Select | Email / DM / Mutual Introduction / Agent/Manager / In Person / Reply to Content |
| Follow-Up Date | Date | When to follow up |
| Follow-Up Count | Number | How many follow-ups sent |
| Response Date | Date | When they responded |
| Confirmed Date | Date | When booking was locked |
| Recording Date | Date | Scheduled recording date/time |
| Time Zone | Select | ET / CT / MT / PT / GMT / CET / AEST / Other |
| Prep Doc Sent | Checkbox | Sent pre-interview prep document? |
| Calendar Invite Sent | Checkbox | Sent calendar invite with link? |
| Recording Link | URL | Zoom/Riverside/Squadcast link |
| Linked Episodes | Relation | -> Episodes database |
| Episode Published | Rollup | Status of linked episode |
| Thank You Sent | Checkbox | Post-recording thank you sent? |
| Asset Pack Sent | Checkbox | Sent them shareable assets (audiogram, quote cards)? |
| Would Invite Back | Checkbox | Worth booking again? |
| Referrals | Text | Other guests they could connect you with |
| Notes | Text | Relationship context, mutual connections, conversation style |
| Tags | Multi-select | Author / Founder / Creator / Expert / Celebrity / Friend / Mutual Connection / Repeat Guest |

**Views:**

- **Pipeline Board** — Board, grouped by Status
- **All Guests** — Table, sorted by Guest Name
- **Outreach Queue** — Filter: Status = Researching (ready to pitch)
- **Awaiting Response** — Filter: Status = Outreach Sent or Follow-Up
- **Follow-Up Due** — Filter: Follow-Up Date <= today AND Status = Outreach Sent or Follow-Up
- **Confirmed & Scheduled** — Filter: Status = Confirmed or Scheduled, sorted by Recording Date
- **Prep Needed** — Filter: Status = Scheduled AND Prep Doc Sent = false
- **Dream List** — Filter: Status = Dream List, sorted by Priority
- **Published** — Filter: Status = Published
- **Re-invite** — Filter: Would Invite Back = true (for future seasons)
- **Needs Thank You** — Filter: Status = Recorded AND Thank You Sent = false
- **By Priority** — Table, grouped by Priority

---

### 3. Production Workflow

**Purpose:** Checklist-driven workflow for each episode's production process. Pre-built templates cover pre-recording prep, recording day, post-production, and publishing steps. Ensures consistent quality across every episode.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Task | Title | Specific production step |
| Episode | Relation | -> Episodes database |
| Episode Title | Rollup | From Episode relation |
| Phase | Select | Pre-Production / Recording Day / Post-Production / Publishing / Promotion |
| Status | Select | Not Started / In Progress / Done / Skipped / Blocked |
| Assigned To | Select | Host / Editor / VA / Guest / Producer |
| Due Date | Date | When this step must be completed |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Done", prop("Status") != "Skipped"), true, false)` |
| Priority | Select | Critical / Important / Nice-to-Have |
| Time Estimate (min) | Number | How long this step takes |
| Depends On | Text | Which tasks must be done first |
| Notes | Text | How to do this step, standards to meet |
| Template Task | Checkbox | Is this part of the standard template? |
| Order | Number | Sequence within the phase (1, 2, 3...) |

**Views:**

- **By Episode** — Table, grouped by Episode Title, sorted by Phase then Order
- **All Tasks** — Table, sorted by Due Date
- **Overdue** — Filter: Overdue = true
- **By Phase** — Table, grouped by Phase
- **This Week** — Filter: Due Date is this week
- **Template** — Filter: Template Task = true (master checklist to duplicate)
- **By Assignee** — Table, grouped by Assigned To
- **Blocked** — Filter: Status = Blocked

### Standard Production Checklist (Template Tasks)

**Pre-Production:**
1. Finalize episode topic and angle
2. Research guest (if interview)
3. Write episode outline (hook, segments, key points, CTA)
4. Send prep document to guest
5. Test recording equipment
6. Schedule recording in calendar
7. Send calendar invite with recording link

**Recording Day:**
8. Pre-flight: test mic, headphones, recording software
9. Brief guest on format (if interview)
10. Record intro separately
11. Record main content/interview
12. Record outro and CTA
13. Save raw files with proper naming convention
14. Quick backup to cloud storage

**Post-Production:**
15. Edit: remove ums, long pauses, mistakes
16. Level audio and normalize volume
17. Add intro/outro music and transitions
18. Insert sponsor reads (if applicable)
19. Export final MP3 at proper specs (128kbps, mono or stereo)
20. Generate transcript
21. Create timestamps
22. Quality check: listen through beginning, middle, end
23. Get host/producer review

**Publishing:**
24. Write episode title (compelling, SEO-friendly)
25. Write show notes with timestamps and links
26. Create episode description for podcast apps
27. Select/create episode cover art (if unique per episode)
28. Upload to hosting platform
29. Schedule publish date/time
30. Verify RSS feed updates
31. Check episode appears on Apple Podcasts, Spotify

**Promotion:**
32. Create social media announcement posts
33. Create audiogram/video clip
34. Send to email list
35. Send shareable assets to guest
36. Cross-post clips to YouTube/TikTok
37. Update website/blog with episode page
38. Engage with early comments/reviews

---

### 4. Publishing Checklist

**Purpose:** Per-platform publishing requirements and settings. Ensures every episode is properly distributed with consistent metadata across all platforms.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Platform | Title | Distribution platform name |
| Episode | Relation | -> Episodes database |
| Episode Title | Rollup | From Episode relation |
| Status | Select | Not Started / Submitted / Live / Issue |
| Title Optimized | Checkbox | Title is within character limits and SEO-optimized |
| Description Added | Checkbox | Full show notes in description |
| Tags/Categories Set | Checkbox | Proper categories and tags selected |
| Cover Art | Checkbox | Episode art meets platform specs |
| Transcript Uploaded | Checkbox | Transcript available on platform |
| Link Verified | Checkbox | Episode link tested and working |
| Published Date | Date | When confirmed live on this platform |
| Notes | Text | Platform-specific requirements or issues |

### Platform Specs (Reference)

| Platform | Title Limit | Description | Art Specs | Notes |
|---|---|---|---|---|
| Apple Podcasts | 255 chars | 4,000 chars | 3000x3000 px, JPG/PNG | Title should not include show name |
| Spotify | 200 chars | 4,000 chars | 3000x3000 px, JPG/PNG | Spotify polls available |
| YouTube | 100 chars | 5,000 chars | 1280x720 px thumbnail | Upload full video or audiogram |
| Website | No limit | Full HTML | Any size | Include player embed |

---

### 5. Analytics Tracker

**Purpose:** Monthly performance metrics across all platforms. Tracks downloads, subscribers, reviews, and growth rate. Shows which episodes and strategies drive growth.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Month | Title | "YYYY-MM" format |
| Date | Date | First of the month |
| Total Downloads | Number | All-platform downloads this month |
| Unique Listeners | Number | If available from hosting platform |
| New Subscribers | Number | Net new subscribers this month |
| Total Subscribers | Number | Cumulative subscriber count |
| Growth Rate | Formula | `if(prop("Total Subscribers") == 0, 0, round(prop("New Subscribers") / (prop("Total Subscribers") - prop("New Subscribers")) * 10000) / 100)` |
| Episodes Published | Number | How many episodes went live this month |
| Downloads Per Episode | Formula | `if(prop("Episodes Published") == 0, 0, round(prop("Total Downloads") / prop("Episodes Published")))` |
| Apple Rating | Number | Current Apple Podcasts rating (1-5) |
| Apple Reviews (new) | Number | New reviews this month |
| Total Reviews | Number | Cumulative reviews |
| Spotify Followers | Number | Spotify follower count |
| YouTube Subs | Number | If publishing to YouTube |
| Top Episode | Text | Best-performing episode this month |
| Top Episode Downloads | Number | Download count for top episode |
| Revenue | Number (USD) | Sponsorship/monetization revenue this month |
| Revenue Per Download | Formula | `if(prop("Total Downloads") == 0, 0, round(prop("Revenue") / prop("Total Downloads") * 10000) / 100)` |
| CPM | Formula | `if(prop("Total Downloads") == 0, 0, round(prop("Revenue") / prop("Total Downloads") * 1000 * 100) / 100)` |
| Notes | Text | What worked, what didn't, strategy changes |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")` |

**Views:**

- **Monthly Timeline** — Table, sorted by Date descending
- **Growth Metrics** — Table showing Month, Total Downloads, Subscribers, Growth Rate
- **Revenue** — Table showing Month, Revenue, CPM, Revenue Per Download
- **By Quarter** — Table, grouped by Quarter
- **Performance** — Table showing Downloads Per Episode, Top Episode each month

---

## DASHBOARD

> Create this as the top-level page. Your podcast command center showing production status, upcoming recordings, and growth metrics.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  PODCAST HQ                                     May 2026          |
+--------+----------+-----------+-----------+----------+-----------+
|  Total |  Monthly |  Avg Per  |  Reviews  |  Pending |  Growth   |
|  Eps:47|  DL: 8.2K|  Ep: 1.7K|  43 total |  3 in    |  +12%     |
|        |          |           |           |  queue   |  MoM      |
+--------+----------+-----------+-----------+----------+-----------+
|                                                                    |
|  PRODUCTION PIPELINE                                              |
|  [Linked view -> Episodes, Board grouped by Status]               |
|                                                                    |
|  Idea  |  Outlined  |  Recording  |  Editing  |  Publishing      |
|  ----  |  --------  |  ---------  |  -------  |  ----------      |
|  Ep 51 |  Ep 50     |  Ep 49      |  Ep 48    |  Ep 47           |
|  Ep 52 |            |             |           |                   |
|  Ep 53 |            |             |           |                   |
|                                                                    |
+----------------------------------+-------------------------------+
|  THIS WEEK                       |  GUEST PIPELINE               |
|  [Linked view -> Production      |  [Linked view -> Guests,      |
|   Workflow, Due Date this week]  |   Confirmed + Scheduled]      |
|                                  |                               |
|  Mon: Edit Ep 48                |  May 15: Sarah Chen           |
|  Wed: Record Ep 49 w/guest     |  May 22: James Park           |
|  Fri: Publish Ep 47            |  Jun 3: Maria Lopez           |
+----------------------------------+-------------------------------+
|  OVERDUE TASKS                   |  PROMOTION TODO               |
|  [Linked view -> Production      |  [Linked view -> Production   |
|   Workflow, Overdue = true]      |   Workflow, Phase = Promotion, |
|                                  |   Status != Done]             |
+----------------------------------+-------------------------------+
|  ANALYTICS (Last 3 Months)                                        |
|  [Linked view -> Analytics, last 3 months, showing Downloads,     |
|   Growth Rate, Top Episode]                                       |
+------------------------------------------------------------------+
```

---

## KEY FORMULA REFERENCE

### Episode Performance vs. Average

```
if(
  prop("Downloads (7 day)") == 0,
  "No data",
  if(
    prop("Downloads (7 day)") > prop("Avg 7 Day Downloads"),
    "Above Average",
    "Below Average"
  )
)
```

### Days Until Publish

```
if(
  empty(prop("Publish Date")),
  "No date",
  if(
    prop("Publish Date") < now(),
    "Published",
    format(dateBetween(prop("Publish Date"), now(), "days")) + " days"
  )
)
```

### Production Task Overdue

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Done",
    prop("Status") != "Skipped"
  ),
  true,
  false
)
```

### Subscriber Growth Rate

```
if(
  prop("Total Subscribers") == 0,
  0,
  round(prop("New Subscribers") / (prop("Total Subscribers") - prop("New Subscribers")) * 10000) / 100
)
```

### Revenue CPM (Cost Per Mille)

```
if(
  prop("Total Downloads") == 0,
  0,
  round(prop("Revenue") / prop("Total Downloads") * 1000 * 100) / 100
)
```

### Downloads Per Episode

```
if(
  prop("Episodes Published") == 0,
  0,
  round(prop("Total Downloads") / prop("Episodes Published"))
)
```

---

## GUEST OUTREACH TEMPLATES

### Cold Pitch (Email)

```
Subject: [Specific topic] — guest spot on [Show Name]?

Hi [Name],

I host [Show Name], a podcast about [topic] with [audience size/description].

I loved your [specific work/post/talk] about [topic], and I think my audience
would get massive value from hearing your perspective on [specific angle].

The format is [format description], typically [duration], and I handle all
editing and promotion. Past guests include [1-2 notable names if applicable].

Would you be open to a [duration] conversation sometime in [timeframe]?

[Your name]
[Show link]
```

### Follow-Up (7 days later)

```
Subject: Re: [Original subject]

Hi [Name],

Just floating this back up — I know inboxes are brutal.

Quick version: I'd love to have you on [Show Name] to discuss [angle].
[One sentence on why your audience specifically needs this].

If the timing isn't right, no worries at all — happy to revisit later.

[Your name]
```

### Booking Confirmation

```
Subject: Confirmed! [Show Name] recording — [Date]

Hi [Name],

We're locked in! Here are the details:

Date: [Date]
Time: [Time + timezone]
Duration: [Duration]
Recording link: [Zoom/Riverside link]
Format: [Solo interview / panel / etc.]

I'll send a brief prep doc 3 days before with topic angles and a few
starter questions (no need to prepare scripted answers — the best
conversations are natural).

Tech needs: Quiet room, headphones (earbuds are fine), and a stable
internet connection. I'll handle all the editing.

Looking forward to it!

[Your name]
```

### Post-Recording Thank You

```
Subject: You were fantastic — thank you!

Hi [Name],

That was a great conversation — my audience is going to love it.

Here's what happens next:
- I'll edit and produce the episode over the next [timeframe]
- I'll send you the final episode + shareable assets before it goes live
- Publish date: [approximate date]

When it's live, I'll tag you on socials. If you share it with your
audience too (totally optional), it helps both our communities discover
each other.

Thank you again — let me know if there's anything I can do for you.

[Your name]
```

---

## QUICK-START GUIDE

### Step 1 — Plan Your First Episodes (15 minutes)

- Open the **Episodes** database
- Add 5-10 episode ideas with Topic, Format, and Category
- Pick your first 3 episodes and move them to "Outlined" status
- Write an Outline for episode 1: hook, main points, CTA
- Set a Recording Date and Publish Date for episode 1

### Step 2 — Set Up Your Guest Pipeline (10 minutes)

- Open **Guest Pipeline** and add 10-15 potential guests
- Categorize: Dream List (reach goals), Strong Targets (achievable), Good Fits (easy gets)
- For your first outreach batch: pick 3-5 "Good Fit" guests
- Write Why This Guest for each (what specific value for YOUR audience)

### Step 3 — Create Your Production Template (10 minutes)

- Open **Production Workflow**
- Add all template tasks from the Standard Production Checklist above
- Mark each as "Template Task" = true
- For your first episode, duplicate the template tasks and link to Episode 1
- Set Due Dates working backwards from your Publish Date

### Step 4 — Record Your First Episode

- Follow the Production Workflow tasks in order
- Use the Recording Day checklist to ensure quality
- Save raw files immediately to cloud backup

### Step 5 — Publish and Distribute

- Follow Post-Production and Publishing phase tasks
- Write compelling Show Notes with timestamps
- Upload to hosting platform (Buzzsprout, Riverside, Transistor, etc.)
- Verify episode appears on Apple Podcasts and Spotify
- Create initial social media announcement

### Step 6 — Start Tracking Analytics

- After your first month, create your first Analytics entry
- Record Total Downloads, Subscribers, and any reviews
- Set up monthly habit: first of each month, add new analytics entry
- After 3+ months, calculate your Avg 7 Day Downloads for the Performance formula

### Step 7 — Build Your Dashboard

- Create the top-level page following the Dashboard Layout
- Pin to sidebar for daily production reference

### Weekly Podcast Workflow

**Monday:** Plan and outline next episode
**Tuesday-Wednesday:** Record (schedule guests mid-week when energy is high)
**Thursday:** Edit current episode in production
**Friday:** Publish, promote, send guest assets
**Weekend:** Batch-create social content for the following week

### Pro Tips

- Batch record when possible. Recording 2-3 episodes in one session creates a buffer so you're never scrambling to publish on deadline. Aim to be 2-3 episodes ahead of your publish schedule.
- The Guest Pipeline is a numbers game. Expect a 20-30% response rate on cold outreach. Send 10 pitches to get 2-3 bookings. Always have more guests in pipeline than episodes planned.
- Update "Avg 7 Day Downloads" monthly. This is your benchmark for identifying breakout episodes (study what worked) and underperformers (study what didn't).
- Timestamps in show notes are non-negotiable. They improve listener experience, SEO, and make episodes shareable by segment.
- The Repurposing Queue view is where most podcast growth happens. Every episode should become at least 3 social media posts. If you're not repurposing, you're wasting 90% of your content's potential reach.
- Guest episodes typically outperform solo episodes for downloads (guests share with their audience). Plan your content calendar with this in mind — alternate solo and guest episodes for variety while leveraging guest distribution.
- The "Would Invite Back" field on guests builds your bench. After 20+ episodes, you'll have a reliable roster of guests who are great on mic, promote the episode, and whose audience overlaps with yours.
