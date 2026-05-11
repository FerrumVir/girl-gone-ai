# SEO Keyword Research Toolkit

> Complete keyword research system with tracking spreadsheets, competitor gap analysis, content cluster mapping, rank tracking, and backlink monitoring. Copy these templates into Google Sheets or Excel.

---

## SECTION 1: MASTER KEYWORD DATABASE

### Spreadsheet Structure
Create a Google Sheet with these columns:

```
| Column A | Column B | Column C | Column D | Column E | Column F | Column G | Column H | Column I | Column J | Column K |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Keyword | Monthly Volume | Keyword Difficulty | Search Intent | CPC | Current Rank | Target URL | Content Status | Priority Score | Cluster | Notes |
```

### Column Definitions & How to Fill Them

**Column A: Keyword**
```
The exact search term. One keyword per row.
Enter the keyword exactly as people search it (lowercase, natural language).
Examples: "how to start a blog", "best running shoes 2026", "keto meal plan"
```

**Column B: Monthly Search Volume**
```
Average monthly searches. Source this from:
- Google Keyword Planner (free with Google Ads account)
- Ubersuggest (free tier: 3 searches/day)
- Ahrefs / SEMrush (paid but most accurate)
- Keywords Everywhere (browser extension, affordable)

Format: whole number (e.g., 12000, 880, 45)
```

**Column C: Keyword Difficulty (KD)**
```
Score 0-100 indicating how hard it is to rank.
Source from your SEO tool (Ahrefs, SEMrush, Ubersuggest).

Scoring guide:
0-20: Easy — target these first (new sites)
21-40: Medium — achievable with good content + some backlinks
41-60: Hard — need strong site authority + excellent content
61-80: Very Hard — requires high authority site
81-100: Ultra competitive — only massive sites rank here
```

**Column D: Search Intent**
```
What the searcher actually wants. Classify every keyword:

INFO — Informational (wants to learn)
  Examples: "what is SEO", "how to bake bread", "why is my cat sneezing"
  Content type: Blog post, guide, how-to, explainer

NAV — Navigational (looking for a specific site/page)
  Examples: "gmail login", "amazon prime", "spotify download"
  Content type: Usually not targetable unless it's YOUR brand

COM — Commercial Investigation (researching before buying)
  Examples: "best laptops 2026", "mailchimp vs convertkit", "iphone 15 review"
  Content type: Comparison, review, roundup, "best of"

TXN — Transactional (ready to buy/act)
  Examples: "buy nike air max", "hire freelance writer", "sign up mailchimp"
  Content type: Product/service page, landing page, pricing page
```

**Column E: CPC (Cost Per Click)**
```
What advertisers pay for this keyword in Google Ads.
Higher CPC = higher commercial value = potentially more profitable to rank for.
Source: Google Keyword Planner or any SEO tool.
Format: $X.XX (e.g., $2.45)
```

**Column F: Current Rank**
```
Your current Google ranking position for this keyword.
Check manually (incognito mode) or use a rank tracker tool.
Format: number (e.g., 7, 23, NR for "not ranking")
Update monthly.
```

**Column G: Target URL**
```
The page on YOUR site that targets (or should target) this keyword.
One URL per keyword. If no page exists yet, write "TO CREATE."
Format: /blog/how-to-start-a-blog or full URL
```

**Column H: Content Status**
```
Where you are with the content for this keyword:
- NOT STARTED: No content exists
- PLANNED: On your content calendar
- DRAFT: Being written
- PUBLISHED: Live on site
- OPTIMIZING: Updating existing content for this keyword
- RANKING: Published and currently ranking (actively monitored)
```

**Column I: Priority Score**
```
Calculate using this formula:

Priority = (Volume / KD) x Intent Multiplier

Intent Multipliers:
- TXN (transactional): x3
- COM (commercial): x2.5
- INFO (informational): x1
- NAV (navigational): x0.5

Higher score = target this keyword first.
Format: calculated number. Sort descending to see your best opportunities.

Google Sheets formula (assuming Volume in B2, KD in C2, and Intent multiplier you manually enter in a helper column):
=B2/C2*[MULTIPLIER]
```

**Column J: Cluster**
```
Which topic cluster this keyword belongs to (see Section 4 below).
Format: Name of the pillar/cluster (e.g., "Meal Prep", "Home Office", "SEO Basics")
```

**Column K: Notes**
```
Any additional context:
- "Competitor [X] ranks #1 with weak content — opportunity"
- "Seasonal peak in January"
- "Featured snippet opportunity"
- "PAA (People Also Ask) present — target with FAQ format"
```

---

## SECTION 2: KEYWORD RESEARCH WORKFLOW

### Step-by-Step Process

**Step 1: Seed Keyword Brainstorm (10 min)**
```
List 10-20 broad topics your site/business covers:
1. [TOPIC]
2. [TOPIC]
3. [TOPIC]
...

For each topic, ask:
- What questions does my audience ask about this?
- What problems do they search for solutions to?
- What products/services do they compare?
- What beginner terms do they search?
```

**Step 2: Keyword Expansion (30 min)**
```
For each seed keyword, gather long-tail variations using:

1. Google Autocomplete: Type seed keyword, note all suggestions
2. Google "People Also Ask": Search seed keyword, expand all PAA boxes
3. Google "Related Searches": Scroll to bottom of search results
4. AnswerThePublic.com: Enter seed keyword, export all questions
5. AlsoAsked.com: Shows question clusters
6. Reddit/Quora: Search your topic, note actual language people use
7. Your own site search / FAQ / customer support tickets

Record EVERY keyword variation that's relevant — you'll filter later.
```

**Step 3: Data Collection (20 min)**
```
Paste all keywords into your SEO tool of choice.
Export data including: volume, KD, CPC, SERP features.
Paste into your master spreadsheet.
Delete duplicates.
Delete irrelevant keywords (things you'd never create content for).
```

**Step 4: Intent Classification (15 min)**
```
Go through each keyword and classify intent (INFO/NAV/COM/TXN).
Quick test: Google the keyword and look at what's ranking.
- All blog posts? = INFO
- Product pages? = TXN
- Comparison articles? = COM
- One brand dominates? = NAV
```

**Step 5: Prioritization (10 min)**
```
Calculate priority score for each keyword.
Sort by priority (highest first).
Your top 20 = your immediate content plan.
```

**Step 6: Cluster Assignment (15 min)**
```
Group keywords into topic clusters (see Section 4).
Each cluster = one pillar page + multiple supporting articles.
```

---

## SECTION 3: COMPETITOR GAP ANALYSIS

### Competitor Keyword Tracking Sheet

```
| Competitor | URL Ranking | Keyword | Their Rank | Your Rank | Gap | Opportunity |
|-----------|-------------|---------|------------|-----------|-----|-------------|
| [COMPETITOR 1] | [URL] | [KEYWORD] | [POSITION] | [YOUR POSITION or NR] | [DIFFERENCE] | [HIGH/MED/LOW] |
```

### How to Run a Competitor Gap Analysis

**Step 1: Identify 3-5 Competitors**
```
Your competitors are sites that rank for keywords you want, not necessarily business competitors.

Find them by:
1. Search your top 10 target keywords
2. Note which sites appear for multiple keywords
3. Those are your SEO competitors

List them:
Competitor 1: [URL] — Domain Authority: [DA]
Competitor 2: [URL] — Domain Authority: [DA]
Competitor 3: [URL] — Domain Authority: [DA]
```

**Step 2: Find Their Top Keywords**
```
Using Ahrefs, SEMrush, or Ubersuggest:
1. Enter competitor URL
2. Go to "Organic Keywords" or "Top Pages"
3. Export their top 100-500 keywords
4. Filter out brand keywords (their company name)
5. Filter for keywords with volume > 100
```

**Step 3: Identify Gaps**
```
A "gap" = a keyword your competitor ranks for but you DON'T.

Filter the export for:
- Keywords where they rank top 20
- Keywords where you rank 20+ or not at all
- Keywords with volume > [YOUR THRESHOLD]
- Keywords with KD < [YOUR TARGET]

These are your opportunities. They've PROVEN the keyword has traffic.
You just need to create better content.
```

**Step 4: Gap Analysis Template**
```
| Keyword | Competitor Ranking | Their Content | Your Status | Action |
|---------|-------------------|---------------|-------------|--------|
| [KW] | #3 — [COMPETITOR] | [TYPE — blog post, 1500 words] | No content | Create better/longer version |
| [KW] | #5 — [COMPETITOR] | [TYPE — listicle, 800 words] | Rank #22 | Optimize existing page |
| [KW] | #1 — [COMPETITOR] | [TYPE — comprehensive guide] | No content | Assess if you can compete |
```

**Step 5: Prioritize Actions**
```
Priority A (Quick Wins): You already rank 11-20 — optimize to push to page 1
Priority B (Content Creation): Competitor ranks with weak content — you can beat them
Priority C (Long-term): Competitor has strong content + authority — build up to this
```

---

## SECTION 4: CONTENT CLUSTER MAPPER

### What is a Content Cluster?
```
A topic cluster is:
1. ONE "Pillar Page" (comprehensive, 3000+ word guide on a broad topic)
2. MULTIPLE "Cluster Pages" (blog posts targeting specific long-tail keywords within that topic)
3. INTERNAL LINKS connecting all cluster pages to the pillar (and back)

Why it works: Google sees topical authority when you have deep coverage of a subject.
```

### Cluster Mapping Template

```
CLUSTER NAME: [BROAD TOPIC]
PILLAR PAGE:
- Title: "The Complete Guide to [TOPIC]"
- Target keyword: [PRIMARY KEYWORD — high volume, high difficulty]
- URL: /[topic]/
- Word count target: 3000-5000
- Status: [PLANNED/DRAFT/PUBLISHED]

CLUSTER PAGES:
| # | Title | Target Keyword | Volume | KD | Status | Internal Link TO Pillar | Pillar Links BACK |
|---|-------|----------------|--------|----|---------|-----------------------|-------------------|
| 1 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 2 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 3 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 4 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 5 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 6 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 7 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |
| 8 | [TITLE] | [KEYWORD] | [VOL] | [KD] | [STATUS] | Yes/No | Yes/No |

INTERNAL LINKING RULES:
- Every cluster page links to the pillar page (in introduction or relevant section)
- Pillar page links to every cluster page (in relevant sections)
- Cluster pages link to each other where relevant (but pillar is the hub)
```

### Example Cluster
```
CLUSTER: "Home Office Setup"
PILLAR: "The Complete Home Office Setup Guide (2026)"
- Keyword: "home office setup" (vol: 8,100, KD: 42)

Cluster pages:
1. "Best Ergonomic Office Chairs Under $500" — "ergonomic office chair" (vol: 4,400)
2. "How to Set Up Dual Monitors (Step by Step)" — "dual monitor setup" (vol: 2,900)
3. "Home Office Lighting Guide for Video Calls" — "home office lighting" (vol: 1,300)
4. "Standing Desk vs Sitting Desk: Which Is Better?" — "standing desk vs sitting" (vol: 1,800)
5. "Home Office Tax Deduction Guide 2026" — "home office tax deduction" (vol: 6,600)
6. "Small Space Home Office Ideas" — "small home office ideas" (vol: 3,200)
7. "Best Home Office Desks for Small Spaces" — "small office desk" (vol: 2,400)
8. "How to Soundproof Your Home Office" — "soundproof home office" (vol: 720)
```

---

## SECTION 5: RANK TRACKING LOG

### Weekly Rank Tracking Template

```
| Keyword | Week 1 | Week 2 | Week 3 | Week 4 | Change (Month) | Trend | Notes |
|---------|--------|--------|--------|--------|---------------|-------|-------|
| [KW 1] | [POS] | [POS] | [POS] | [POS] | [+/-] | [UP/DOWN/STABLE] | |
| [KW 2] | [POS] | [POS] | [POS] | [POS] | [+/-] | | |
| [KW 3] | [POS] | [POS] | [POS] | [POS] | [+/-] | | |
```

### How to Track Rankings
```
FREE methods:
1. Google Search Console (shows average position — 3-day delay)
2. Manual check (incognito mode, no personalization)
3. Whatsmyserp.com (free, limited checks)

PAID methods (recommended for 20+ keywords):
1. Ahrefs Rank Tracker
2. SEMrush Position Tracking
3. SERPRobot
4. AccuRanker

FREQUENCY:
- Top 10 priority keywords: check weekly
- All other tracked keywords: check monthly
- New content: check after 2 weeks, then weekly for 2 months
```

### Rank Tracking Interpretation Guide
```
POSITION 1-3: You're winning. Maintain content freshness, defend from competitors.
POSITION 4-10: Page 1 — optimize for CTR (better title/meta). Build 2-3 backlinks to push higher.
POSITION 11-20: So close. Add content depth, improve internal linking, get 3-5 backlinks.
POSITION 21-50: Content is indexed and somewhat relevant. Needs significant improvement or authority building.
POSITION 50+: Barely ranking. Content may need complete rewrite or your site needs more topical authority first.
NOT RANKING: Content doesn't match intent, is too thin, or site has no authority for this topic yet.

MOVEMENT PATTERNS:
- Steady climb (improving 5-10 positions/month): Strategy is working, keep going
- Volatile (jumping 10+ positions up/down): Google is testing your content — might need more signals
- Stuck at position 8-15: Classic "almost there" — usually needs backlinks to break through
- Dropped suddenly: Check if competitor published better content or if Google algorithm updated
```

---

## SECTION 6: BACKLINK TRACKER

### Backlink Tracking Sheet

```
| # | Source URL | Source Domain | DA | Link Type | Anchor Text | Target URL | Date Acquired | Status | Notes |
|---|-----------|--------------|----|-----------|-----------  |------------|---------------|--------|-------|
| 1 | [FULL URL] | [DOMAIN] | [DA] | [FOLLOW/NOFOLLOW] | [ANCHOR TEXT] | [YOUR URL] | [DATE] | [LIVE/BROKEN/REMOVED] | |
```

### Backlink Acquisition Tracker

```
OUTREACH LOG:
| Date | Target Site | Contact Name | Pitch Type | Response | Link Acquired | Follow-up Date |
|------|-------------|-------------|------------|----------|---------------|---------------|
| [DATE] | [SITE] | [NAME] | [GUEST POST/RESOURCE/BROKEN LINK] | [YES/NO/PENDING] | [YES/NO] | [DATE] |

MONTHLY SUMMARY:
- Outreach emails sent: [#]
- Responses received: [#]
- Links acquired: [#]
- Response rate: [%]
- Acquisition rate: [%]
- Best performing pitch type: [TYPE]
```

### Link Building Opportunity Types
```
1. Guest Posts: Write articles for other sites in exchange for a backlink
   → Track: sites that accept guest posts in your niche

2. Resource Pages: Get listed on "best resources for [TOPIC]" pages
   → Track: resource pages in your niche

3. Broken Link Building: Find broken links on other sites, suggest your content as replacement
   → Track: sites with relevant broken links

4. HARO / Journalist Requests: Respond to journalist queries for expert quotes
   → Track: responses submitted and links earned

5. Unlinked Mentions: Find sites that mention you without linking — ask for a link
   → Track: mentions found and conversion rate

6. Content Partnerships: Co-create content that naturally earns links
   → Track: partnership opportunities and results
```

---

## SECTION 7: MONTHLY SEO REVIEW TEMPLATE

### Monthly Report Structure
```
MONTH: [MONTH/YEAR]
SITE: [YOUR SITE]

TRAFFIC OVERVIEW:
- Organic sessions this month: [#]
- vs. last month: [+/- %]
- vs. same month last year: [+/- %]
- Top traffic pages (organic):
  1. [URL] — [SESSIONS] — [PRIMARY KEYWORD]
  2. [URL] — [SESSIONS] — [PRIMARY KEYWORD]
  3. [URL] — [SESSIONS] — [PRIMARY KEYWORD]

KEYWORD MOVEMENT:
- Keywords on Page 1: [#] (vs. [LAST MONTH])
- Keywords moved UP: [#]
- Keywords moved DOWN: [#]
- New keywords ranking: [#]
- Top climbers:
  1. [KEYWORD]: position [X] → position [Y]
  2. [KEYWORD]: position [X] → position [Y]

CONTENT PUBLISHED:
- Posts published: [#]
- Posts optimized/updated: [#]
- Total word count added: [#]
- Posts to publish next month: [LIST]

BACKLINKS:
- New backlinks acquired: [#]
- Total referring domains: [#]
- Domain Authority: [CURRENT]
- Link building activities completed: [LIST]

TECHNICAL:
- Site speed (mobile): [SCORE]
- Core Web Vitals: [PASS/FAIL]
- Indexation issues: [ANY PROBLEMS]
- Crawl errors: [ANY PROBLEMS]

PRIORITIES NEXT MONTH:
1. [ACTION — specific keyword/page/task]
2. [ACTION]
3. [ACTION]

WINS:
- [CELEBRATE WHAT WORKED]

LOSSES:
- [WHAT DIDN'T WORK — and what you'll do differently]
```

---

## SECTION 8: ON-PAGE SEO CHECKLIST (Per Page)

### Before Publishing Any Content
```
CONTENT:
- [ ] Primary keyword in title (preferably first 5 words)
- [ ] Primary keyword in H1 (only one H1 per page)
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in at least one H2
- [ ] Secondary keywords used naturally in body
- [ ] Content length meets or exceeds top competitors for this keyword
- [ ] Search intent matched (check what's ranking — match format)
- [ ] Unique value (what does YOUR content offer that #1-5 don't?)

TECHNICAL:
- [ ] URL is short and includes primary keyword (/keyword-phrase/)
- [ ] Meta title: under 60 characters, keyword + compelling
- [ ] Meta description: under 155 characters, includes keyword + CTA
- [ ] Images: alt text with keywords (naturally, not stuffed)
- [ ] Images: compressed (under 200KB each)
- [ ] Internal links: 3-5 links to related content on your site
- [ ] Internal links: existing content links BACK to this new page
- [ ] External links: 2-3 links to authoritative sources
- [ ] Mobile friendly: readable on phone without zooming
- [ ] Page speed: loads in under 3 seconds

STRUCTURE:
- [ ] H2 and H3 subheadings used logically (hierarchy)
- [ ] Short paragraphs (2-3 sentences max)
- [ ] Bullet points or numbered lists for scannable content
- [ ] Table of contents (for posts over 2000 words)
- [ ] Featured snippet optimization (answer target question directly in 40-60 words)
- [ ] FAQ schema (if targeting "People Also Ask" results)
```
