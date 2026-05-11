# Beauty Influencer Content Calendar & Strategy Planner — Notion Template

> Duplicate this template into your Notion workspace. All databases are pre-linked. Includes posting schedule, brand deal tracker, engagement analytics, and 90-day content pipeline.

---

## DATABASES

---

### 1. Content Calendar

**Purpose:** Plan, schedule, and track every piece of content across all platforms.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Content Title | Title | Descriptive name for the post/video |
| Platform | Multi-select | Instagram Feed / Instagram Reels / Instagram Stories / TikTok / YouTube / YouTube Shorts / Pinterest / Twitter/X / Blog |
| Content Pillar | Select | Tutorial / Review / GRWM / Transformation / Behind-the-Scenes / Personal / Trending / Collab / Promotional |
| Status | Select | Idea / Scripted / Filmed / Edited / Scheduled / Published / Repurposed |
| Publish Date | Date | Scheduled or actual publish date |
| Publish Time | Text | Optimal posting time (e.g., "12:00 PM CT") |
| Caption | Text | Full caption copy |
| Hashtags | Text | Hashtag set to use |
| Hook | Text | First line/first 3 seconds |
| CTA | Text | Call to action (comment, save, share, link in bio, etc.) |
| Audio/Sound | Text | Trending audio or original |
| Brand Deal | Relation | -> Brand Deals database (if sponsored) |
| Products Featured | Text | Products mentioned or shown |
| Affiliate Links | Text | Any affiliate links used |
| Content File | Files & media | Upload the actual content file |
| Thumbnail | Files & media | Custom thumbnail if applicable |
| Performance | Relation | -> Analytics database |
| Repurposed From | Relation | -> Content Calendar (self-relation) |
| Notes | Text | Additional context, filming notes |

**Views:**
- **This Week** — Table filtered: Publish Date is within this week, sorted by date/time
- **Content Board** — Board view grouped by Status (Kanban-style pipeline)
- **Monthly Calendar** — Calendar view by Publish Date
- **By Platform** — Table grouped by Platform
- **By Pillar** — Table grouped by Content Pillar
- **Ideas Backlog** — Filter: Status = Idea, sorted by Created date
- **Needs Filming** — Filter: Status = Scripted
- **Needs Editing** — Filter: Status = Filmed
- **Ready to Post** — Filter: Status = Scheduled
- **Published (Last 30 Days)** — Filter: Status = Published AND Publish Date within past 30 days
- **Sponsored Content** — Filter: Brand Deal is not empty

---

### 2. Brand Deals

**Purpose:** Track partnerships, negotiations, deliverables, and income from brand collaborations.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Brand Name | Title | Company/brand name |
| Contact Person | Text | Name + title of your contact |
| Contact Email | Email | Primary contact email |
| Status | Select | Pitched / Negotiating / Contracted / In Progress / Delivered / Paid / Declined / Ghosted |
| Deal Type | Select | Gifted / Paid Post / Affiliate / Ambassador / UGC / Long-Term / Event |
| Platform(s) | Multi-select | Where content will be posted |
| Deliverables | Text | Exactly what's required (number of posts, stories, etc.) |
| Rate | Number (USD) | Total payment for the deal |
| Payment Terms | Select | Net 15 / Net 30 / Net 45 / Net 60 / Upon Delivery / Upfront |
| Invoice Sent | Date | When invoice was submitted |
| Payment Received | Date | When payment cleared |
| Payment Status | Formula | `if(not empty(prop("Payment Received")), "Paid", if(not empty(prop("Invoice Sent")), "Invoiced", "Pending"))` |
| Usage Rights | Select | 3 months / 6 months / 1 year / Perpetual / None specified |
| Exclusivity | Text | Any competitor exclusivity terms |
| Start Date | Date | Campaign start |
| Deadline | Date | Content due date |
| Contract | Files & media | Upload signed contract |
| Content Links | Text | Links to published deliverables |
| Linked Content | Relation | -> Content Calendar |
| Performance Notes | Text | How the sponsored content performed |
| Would Work Again | Checkbox | Good experience, open to future deals |
| Notes | Text | Communication notes, special terms |

**Views:**
- **Active Deals** — Filter: Status = Contracted or In Progress
- **Pipeline** — Board view grouped by Status
- **Revenue This Month** — Filter: Payment Received within this month
- **Revenue This Year** — Filter: Payment Received within this year, showing sum of Rate
- **Upcoming Deadlines** — Filter: Deadline is within next 14 days, sorted by Deadline
- **Awaiting Payment** — Filter: Invoice Sent is not empty AND Payment Received is empty
- **Gifted (No Pay)** — Filter: Deal Type = Gifted
- **All Brands** — Table sorted by Brand Name

---

### 3. Analytics Tracker

**Purpose:** Log performance metrics for published content to identify what works.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Content | Relation | -> Content Calendar |
| Platform | Rollup | Platform from linked Content |
| Content Pillar | Rollup | Content Pillar from linked Content |
| Date Published | Rollup | Publish Date from linked Content |
| Views/Impressions | Number | Total views or impressions |
| Reach | Number | Unique accounts reached |
| Likes | Number | Total likes/hearts |
| Comments | Number | Total comments |
| Saves | Number | Total saves/bookmarks |
| Shares | Number | Total shares/sends |
| Engagement Rate | Formula | `if(prop("Reach") > 0, (prop("Likes") + prop("Comments") + prop("Saves") + prop("Shares")) / prop("Reach") * 100, 0)` |
| Follower Change | Number | Net followers gained/lost (+ or -) |
| Profile Visits | Number | Profile visits driven by this content |
| Link Clicks | Number | Link clicks (if applicable) |
| Watch Time | Number | Average watch time in seconds (video) |
| Completion Rate | Number | Percentage who watched to end (video) |
| Revenue Generated | Number (USD) | Affiliate sales, brand deal allocation, etc. |
| Top Performing | Formula | `if(prop("Engagement Rate") >= 8, "Viral", if(prop("Engagement Rate") >= 5, "High", if(prop("Engagement Rate") >= 3, "Average", "Low")))` |
| Notes | Text | What worked, what didn't, audience feedback |

**Views:**
- **Last 7 Days** — Filter: Date Published within past 7 days, sorted by Engagement Rate descending
- **Last 30 Days** — Filter: Date Published within past 30 days
- **Top Performers** — Filter: Top Performing = "Viral" or "High", sorted by Views descending
- **By Platform** — Table grouped by Platform, showing averages
- **By Pillar** — Table grouped by Content Pillar, showing averages
- **Revenue Content** — Filter: Revenue Generated > 0

---

### 4. Engagement Tasks

**Purpose:** Daily engagement activities to maintain community and grow following.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Task | Title | Description of engagement activity |
| Date | Date | When to complete |
| Platform | Select | Instagram / TikTok / YouTube / Twitter / All |
| Type | Select | Reply to Comments / DM Responses / Community Engagement / Networking / Collaboration Outreach |
| Duration | Number | Minutes to spend |
| Completed | Checkbox | Mark when done |
| Notes | Text | Accounts engaged with, conversations started |

**Views:**
- **Today** — Filter: Date = today
- **This Week** — Filter: Date is within this week
- **Daily Checklist** — Board grouped by Type, filter: today

---

## CONTENT PILLARS & RATIO

### Pillar Definitions

| Pillar | Description | % of Content | Example |
|--------|-------------|--------------|---------|
| Tutorial | Teaching a skill or technique | 25% | "How to contour for round faces" |
| Review | Honest product opinions | 20% | "Testing the new Rare Beauty blush" |
| GRWM | Get-ready-with-me / routine | 15% | "Morning skincare + makeup routine" |
| Transformation | Before/after or dramatic change | 15% | "Turning myself into a 90s supermodel" |
| Behind-the-Scenes | Creator life, process, real moments | 10% | "What filming a brand deal actually looks like" |
| Personal | Non-beauty content showing personality | 5% | "Weekend vlog, life update" |
| Trending | Jumping on current trends adapted to beauty | 5% | "[Trending sound] but make it beauty" |
| Promotional | Sponsored, affiliate, product launch | 5% | "Partnered with [Brand] for..." |

---

## WEEKLY POSTING SCHEDULE

### Minimum Cadence

| Day | Instagram | TikTok | Stories |
|-----|-----------|--------|---------|
| Monday | Reels (Tutorial) | 1 video | 5-8 slides |
| Tuesday | Feed Carousel | 1 video | 5-8 slides |
| Wednesday | Reels (GRWM/Review) | 1-2 videos | 5-8 slides |
| Thursday | — | 1 video | 5-8 slides |
| Friday | Reels (Trending/Fun) | 1-2 videos | 5-8 slides |
| Saturday | Feed (Personal/BTS) | 1 video | 3-5 slides |
| Sunday | — (batch film day) | — | 3-5 slides |

### Optimal Posting Times (Beauty Niche)

| Platform | Best Times | Notes |
|----------|-----------|-------|
| Instagram Reels | 9 AM, 12 PM, 6 PM | Test within these windows |
| Instagram Feed | 11 AM, 1 PM, 7 PM | Tue/Wed/Fri perform best |
| TikTok | 7 AM, 12 PM, 5 PM, 9 PM | Post when YOUR analytics say |
| YouTube | Saturday 9 AM, Tuesday 3 PM | Depends on content type |
| Pinterest | 8 PM, 2 PM | Saturday + Friday best |

---

## 90-DAY CONTENT PIPELINE

### Month 1 — Foundation Building

**Week 1-2 Theme:** Introduce/Reintroduce Yourself
- Day 1: "What I do + why I started" (Reels)
- Day 2: "My current skincare/makeup routine" (TikTok)
- Day 3: "5 things you don't know about me" (Carousel)
- Day 5: "My ride-or-die products" (TikTok)
- Day 7: "Why I'm the person to follow for [niche]" (Reels)
- Day 8: "Recreating my most viral look" (TikTok)
- Day 10: "Honest opinion on trending product" (Review)
- Day 12: "Day in my life as a beauty creator" (BTS)
- Day 14: "Q&A — Ask me anything" (Stories + Reels)

**Week 3-4 Theme:** Establish Expertise
- Tutorial series (3 parts): "The basics of [your specialty]"
- Product comparison: "[Drugstore] vs. [High-end]"
- Myth-busting: "Stop believing this about [topic]"
- Transformation: Dramatic before/after content
- Trend participation: Adapt 2-3 current trends to beauty
- Behind-the-scenes: "How I film my content" (BTS)
- Community engagement: Duet/stitch a follower's question

### Month 2 — Growth Push

**Week 5-6 Theme:** Collaboration & Community
- Collaboration post with another creator
- "React to my followers' routines" (engagement driver)
- Controversial take: "Unpopular beauty opinion"
- Tutorial: Response to most-asked question from Month 1
- Start a recurring series (e.g., "Swatch Saturday" or "Try-On Tuesday")
- Brand pitch outreach (reach out to 5-10 brands)
- Go LIVE at least once (Q&A, GRWM, or tutorial)

**Week 7-8 Theme:** Value & Virality
- Create a shareable graphic/carousel (save-worthy content)
- Film 3 videos using trending audios in your niche
- "Things I stopped doing in my routine + why" (educational)
- Series continuation from Week 5-6
- Throwback/progress post showing your own beauty journey
- Stitch/duet a trending beauty video with your take
- Review a product everyone is talking about (timely)

### Month 3 — Monetization & Scale

**Week 9-10 Theme:** Revenue Building
- Launch/promote affiliate links with genuine recommendations
- Film UGC-style content to attract brand deals
- "Products worth the hype vs. not" — high engagement format
- Create a lead magnet (free guide/checklist) for email list
- Pitch 5 brands with your media kit + performance stats
- Post your first paid collaboration (or announce you're open)
- Repost top-performing content from Month 1-2 on a new platform

**Week 11-12 Theme:** System & Sustainability
- Batch film 2 weeks of content in one day
- Repurpose top TikToks as Reels (and vice versa)
- Audit analytics: double down on what's working
- Plan next quarter's content pillars based on data
- Nurture brand relationships (send results, propose next collab)
- Celebrate a milestone with followers (engagement post)
- Set new goals for next 90 days

---

## DAILY ENGAGEMENT CHECKLIST

### Morning (15 minutes)
- [ ] Reply to all comments from last 24 hours
- [ ] Respond to all DMs
- [ ] Post 2-3 Stories
- [ ] Engage with 10 accounts in your niche (meaningful comments)

### Midday (10 minutes)
- [ ] Check if any content is trending — boost with Stories if so
- [ ] Post planned content
- [ ] Reply to new comments within first hour of posting
- [ ] Share to Stories with engagement sticker

### Evening (10 minutes)
- [ ] Engage with 10 more accounts (different from morning)
- [ ] Reply to comments on latest post
- [ ] Check trending sounds/formats for tomorrow
- [ ] Post evening Stories (personal, relatable content)

---

## BRAND DEAL RATE CARD

### Base Rates (Adjust Based on Your Metrics)

| Deliverable | Micro (5K-25K) | Mid (25K-100K) | Macro (100K-500K) |
|-------------|----------------|----------------|---------------------|
| Instagram Feed Post | $200-500 | $500-2,000 | $2,000-7,500 |
| Instagram Reel | $300-750 | $750-3,000 | $3,000-10,000 |
| Instagram Story Set (3-5) | $150-350 | $350-1,500 | $1,500-5,000 |
| TikTok Video | $250-600 | $600-2,500 | $2,500-8,000 |
| YouTube Integration (60-90s) | $500-1,500 | $1,500-5,000 | $5,000-15,000 |
| YouTube Dedicated Video | $1,000-3,000 | $3,000-10,000 | $10,000-30,000 |
| Blog Post | $200-500 | $500-1,500 | $1,500-3,000 |
| UGC Only (no posting) | $150-400 | $200-500 | N/A |

### Add-On Pricing

| Add-On | Rate |
|--------|------|
| Usage rights (3 months) | +25% of base rate |
| Usage rights (6 months) | +50% of base rate |
| Usage rights (perpetual) | +100% of base rate |
| Whitelisting/boosting | +30% of base rate |
| Exclusivity (30 days) | +25% of base rate |
| Exclusivity (90 days) | +50% of base rate |
| Rush delivery (under 7 days) | +25-50% of base rate |
| Additional revision round | $100-300 per round |
| Raw footage/B-roll | +$200-500 |

---

## QUICK-START GUIDE

### Step 1: Set Up Your Content Pillars
Decide which pillars make sense for your niche and audience. Assign percentages. Plan at least 2 weeks of content before posting.

### Step 2: Fill the Ideas Backlog
Brainstorm 30+ content ideas and add them to the Content Calendar with Status = Idea. Use trending sounds, audience questions, and competitor analysis for inspiration.

### Step 3: Establish Your Schedule
Pick your posting days and times. Consistency matters more than frequency. Commit to what you can sustain.

### Step 4: Batch Create
Set aside one day per week for filming. Script 5-7 videos, film them all, then edit throughout the week. Move content through the Status pipeline.

### Step 5: Track Everything
After 48 hours, log performance in the Analytics Tracker for every published post. After 30 days, review which pillars, formats, and platforms are performing best.

### Step 6: Pitch Brands
Once you have 30+ days of consistent content and analytics data, build your media kit and start pitching. Use the Brand Deals database to track every conversation.
