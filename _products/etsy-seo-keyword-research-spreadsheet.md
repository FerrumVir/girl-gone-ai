# Etsy SEO Keyword Research Spreadsheet — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Research, organize, and deploy high-ranking keywords for your Etsy listings with data-driven strategies instead of guesswork.

---

> **SETUP GUIDE — Get Running in 25 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 6 tabs/sheets and name them: Keyword Database, Listing Optimizer, Title Builder, Tag Tracker, A/B Test Log, Seasonal Calendar
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Start by entering 20-30 seed keywords related to your products
> 6. Use Etsy search bar autocomplete, eRank, Marmalead, or Sale Samurai for research data
>
> **Tip:** Etsy allows 13 tags per listing. Each tag can be up to 20 characters. Your title has 140 characters max. Use this spreadsheet to make every character count.

---

---

# SHEET 1: KEYWORD DATABASE

> Your master keyword research repository. Every keyword you discover goes here with scoring data.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| **Keyword** | **Search Volume** | **Competition** | **Listing Count** | **Avg Reviews (Top 10)** | **Opportunity Score** | **Category** | **Keyword Type** | **Character Count** | **Used In Listing** | **Notes** |

---

## Search Volume (Dropdown/Scale)
- Very High (10,000+ monthly searches estimated)
- High (5,000-10,000)
- Medium (1,000-5,000)
- Low (500-1,000)
- Very Low (under 500)

## Competition (Dropdown/Scale)
- Very High (100,000+ listings)
- High (50,000-100,000 listings)
- Medium (10,000-50,000 listings)
- Low (1,000-10,000 listings)
- Very Low (under 1,000 listings)

## Keyword Type (Dropdown)
- Seed (broad, 1-2 words)
- Long-tail (3+ words, specific)
- Attribute (color, material, size)
- Occasion (gift for, wedding, birthday)
- Style (minimalist, boho, vintage)
- Seasonal (Christmas, Halloween, summer)
- Problem-solving (organizer for, holder for)

---

## Formulas

`FORMULA (Opportunity Score - F2):`
```
=IF(B2="Very High",5,IF(B2="High",4,IF(B2="Medium",3,IF(B2="Low",2,1)))) * IF(C2="Very Low",5,IF(C2="Low",4,IF(C2="Medium",3,IF(C2="High",2,1))))
```
Score range: 1-25. Higher = better opportunity (high volume + low competition).

`FORMULA (Character Count - I2): =LEN(A2)`

---

## Opportunity Score Guide

| Score | Rating | Priority |
|:-----:|--------|----------|
| 20-25 | Excellent | Use immediately in titles and tags |
| 15-19 | Good | Strong tag candidate |
| 10-14 | Average | Use if relevant, don't force it |
| 5-9 | Below Average | Only use if highly relevant to product |
| 1-4 | Poor | Skip — too competitive for the volume |

---

## Sample Keyword Data

| Keyword | Volume | Competition | Listings | Avg Reviews | Score | Category | Type | Chars |
|---------|--------|-------------|:--------:|:-----------:|:-----:|----------|------|:-----:|
| personalized gift | Very High | Very High | 2,400,000 | 12,500 | 5 | Gifts | Seed | 18 |
| custom name necklace | High | High | 350,000 | 4,200 | 8 | Jewelry | Long-tail | 20 |
| minimalist gold ring | Medium | Medium | 85,000 | 1,800 | 9 | Jewelry | Style | 20 |
| dog mom wine glass | Medium | Low | 8,500 | 450 | 12 | Drinkware | Long-tail | 18 |
| camping mug enamel | Low | Very Low | 2,100 | 120 | 8 | Drinkware | Attribute | 18 |
| teacher appreciation gift | High | Medium | 120,000 | 2,100 | 12 | Gifts | Occasion | 26 |
| bridesmaid proposal box | High | Low | 12,000 | 890 | 16 | Wedding | Occasion | 23 |
| adhd planner adult | Medium | Low | 5,400 | 340 | 12 | Planners | Problem | 18 |

---

---

# SHEET 2: LISTING OPTIMIZER

> Optimize each listing's title, tags, description, and attributes for maximum search visibility.

---

## Listing Optimization Worksheet

### Listing Details

| Field | Value |
|-------|-------|
| Listing Title | |
| Listing URL | |
| Product Category | |
| Primary Keyword | |
| Current Views/Week | |
| Current Favorites/Week | |
| Current Conversion Rate | |

---

### Tag Optimization (13 Tags Max)

| Tag # | Tag (max 20 chars) | Char Count | Opportunity Score | Search Volume | In Title? | Notes |
|:------:|-------------------|:----------:|:-----------------:|:-------------:|:---------:|-------|
| 1 | | | | | Y/N | Primary keyword |
| 2 | | | | | Y/N | |
| 3 | | | | | Y/N | |
| 4 | | | | | Y/N | |
| 5 | | | | | Y/N | |
| 6 | | | | | Y/N | |
| 7 | | | | | Y/N | |
| 8 | | | | | Y/N | |
| 9 | | | | | Y/N | |
| 10 | | | | | Y/N | |
| 11 | | | | | Y/N | |
| 12 | | | | | Y/N | |
| 13 | | | | | Y/N | |

`FORMULA (Char Count): =LEN(B2)`

---

### Tag Strategy Rules

| Rule | Explanation |
|------|-------------|
| No repeating words across tags | Etsy indexes each word once; "dog gift" and "dog lover" = wasted "dog" slot |
| Use all 13 tags | Empty tag slots = missed ranking opportunities |
| Mix keyword types | Combine seed + long-tail + attribute + occasion tags |
| Multi-word tags preferred | "custom name necklace" > "custom" as a single tag |
| Match tag to title phrase | Having a tag that matches a title phrase boosts relevance |
| Include misspellings? | No — Etsy handles common misspellings automatically |

---

### Listing SEO Score

| Factor | Max Points | Your Score | Notes |
|--------|:----------:|:----------:|-------|
| Title uses primary keyword in first 40 chars | 20 | /20 | Most important |
| All 13 tags filled | 15 | /15 | |
| Tags match title phrases | 15 | /15 | |
| No repeated words across tags | 10 | /10 | |
| Category and attributes set correctly | 10 | /10 | |
| Description uses keywords naturally (first 160 chars) | 10 | /10 | |
| Long-tail keywords included | 10 | /10 | |
| Seasonal/occasion keywords (if applicable) | 10 | /10 | |
| **TOTAL** | **100** | **/100** | |

---

---

# SHEET 3: TITLE BUILDER

> Construct SEO-optimized titles using a formula-based approach.

---

## Etsy Title Formula

**Structure:** `[Primary Keyword] [Secondary Keyword] [Attribute] [Occasion/Use Case] [Personalization Note]`

**Max Characters:** 140

---

## Title Building Worksheet

| Component | Your Text | Character Count |
|-----------|-----------|:--------------:|
| Primary Keyword (most searched) | | |
| Secondary Keyword | | |
| Attribute (material, color, size) | | |
| Occasion / Use Case | | |
| Personalization Note | | |
| Separator Characters (commas, pipes, dashes) | | |
| **TOTAL** | | **/140** |

`FORMULA (Total Chars): =SUM(C2:C7)`
`FORMULA (Chars Remaining): =140 - TotalChars`

---

## Title Examples by Category

| Category | Title Example | Chars | Keywords Hit |
|----------|--------------|:-----:|:------------:|
| Jewelry | Custom Name Necklace, Personalized Gold Nameplate, Minimalist Dainty Chain, Birthday Gift for Her | 96 | 8 |
| Home Decor | Personalized Family Name Sign, Rustic Wood Wall Art, Housewarming Gift, Farmhouse Living Room Decor | 100 | 9 |
| Digital | ADHD Daily Planner Printable, Adult ADHD Organizer, Minimalist To Do List, Instant Download PDF | 91 | 8 |
| Clothing | Dog Mom Sweatshirt, Funny Dog Lover Crewneck, Pet Parent Gift, Unisex Oversized Pullover | 87 | 7 |

---

## Title Optimization Rules

| Rule | Do | Don't |
|------|-----|-------|
| Front-load keywords | Put most important keyword first | Bury primary keyword at the end |
| Use natural language | "Custom Name Necklace" | "Necklace Custom Name Gold Gift" |
| Include attributes | Mention material/color/size | Leave out searchable details |
| Add occasion keywords | "Birthday Gift for Mom" | Assume people know it's giftable |
| Use separators wisely | Commas or pipes between phrases | No separators (run-on mess) |
| Fill the space | Use close to 140 characters | Stop at 60 characters |

---

---

# SHEET 4: TAG TRACKER

> Monitor which tags are performing across all your listings. Track changes over time.

---

## Tag Performance Dashboard

| Tag | # Listings Using | Avg Views/Week | Avg Favorites/Week | Avg Conversion | Score | Keep/Drop |
|-----|:----------------:|---------------:|-------------------:|:--------------:|:-----:|:---------:|
| | | | | % | | |
| | | | | % | | |
| | | | | % | | |
| | | | | % | | |
| | | | | % | | |

`FORMULA (Score): Use Opportunity Score from Keyword Database`
`FORMULA (Keep/Drop): =IF(AND(AvgViews > MedianViews, Conversion > 1%), "KEEP", "TEST REPLACEMENT")`

---

## Tag Changelog

| Date | Listing | Old Tag | New Tag | Reason | Views Before | Views After (2 weeks) | Result |
|------|---------|---------|---------|--------|:------------:|:---------------------:|--------|
| | | | | | /wk | /wk | Better/Worse/Same |
| | | | | | /wk | /wk | |
| | | | | | /wk | /wk | |

---

## Tag Usage Matrix (All Listings)

| Tag | Listing 1 | Listing 2 | Listing 3 | Listing 4 | Listing 5 | Total Uses |
|-----|:---------:|:---------:|:---------:|:---------:|:---------:|:----------:|
| [keyword 1] | X | | X | | | 2 |
| [keyword 2] | X | X | | X | | 3 |
| [keyword 3] | | X | X | X | X | 4 |

Use this matrix to avoid over-using the same tags and ensure variety across your shop.

---

---

# SHEET 5: A/B TEST LOG

> Track listing experiments to find what actually drives more views, favorites, and sales.

---

## Active Tests

| Test # | Listing | Variable Tested | Version A | Version B | Start Date | End Date | Metric Tracked |
|:------:|---------|----------------|-----------|-----------|------------|----------|:-------------:|
| 1 | | Title | | | | | Views |
| 2 | | Primary Photo | | | | | Click Rate |
| 3 | | Price | | | | | Conversion |
| 4 | | Tags (set of 13) | | | | | Views |
| 5 | | Description | | | | | Conversion |

---

## Test Results

| Test # | Version A Result | Version B Result | Winner | Confidence | Action Taken | Date Applied |
|:------:|:----------------:|:----------------:|:------:|:----------:|:-------------|:------------:|
| 1 | views/wk | views/wk | A/B | High/Med/Low | | |
| 2 | clicks/wk | clicks/wk | A/B | High/Med/Low | | |
| 3 | sales/wk | sales/wk | A/B | High/Med/Low | | |

---

## A/B Testing Rules

| Rule | Details |
|------|---------|
| Test one variable at a time | Never change title AND tags simultaneously |
| Minimum test duration | 2 weeks (14 days) for statistical relevance |
| Minimum traffic | 100+ views during test period |
| Document everything | Screenshot both versions before changing |
| Seasonal awareness | Don't test during holiday spikes — results will be skewed |
| Statistical confidence | Need 20%+ difference with 100+ views to be meaningful |

---

## Test Ideas Backlog

| Priority | Variable | Hypothesis | Expected Impact |
|:--------:|----------|-----------|:---------------:|
| 1 | Title keyword order | Primary keyword first = more views | +15% views |
| 2 | Thumbnail background | White vs. lifestyle = higher CTR | +10% CTR |
| 3 | Price ending | $24.99 vs. $25.00 vs. $24 | +5% conversion |
| 4 | Free shipping vs. lower price | Baked-in shipping = more sales | +20% conversion |
| 5 | Video vs. no video | First image as video = longer engagement | +10% favorites |

---

---

# SHEET 6: SEASONAL KEYWORD CALENDAR

> Plan keyword rotations around seasonal demand. Swap tags 4-6 weeks before each season peaks.

---

## 12-Month Keyword Season Map

| Month | Upcoming Season/Event | Swap Tags By | Keywords to Add | Keywords to Remove |
|-------|----------------------|:------------:|-----------------|-------------------|
| January | Valentine's Day | Jan 5 | valentine gift, galentine, anniversary | christmas, holiday, stocking stuffer |
| February | Spring / Easter | Feb 15 | spring decor, easter gift, pastel | valentine, galentine |
| March | Mother's Day | Mar 15 | mom gift, mother's day, gift for mom | easter, spring break |
| April | Graduation / Summer | Apr 15 | graduation gift, class of 2026, teacher gift | mother's day |
| May | Father's Day / Wedding | May 10 | dad gift, father's day, groomsman | graduation, teacher |
| June | Summer / July 4th | Jun 1 | summer, patriotic, outdoor, camping | father's day, wedding |
| July | Back to School | Jul 15 | back to school, teacher, student | summer, patriotic, 4th of july |
| August | Fall / Halloween | Aug 15 | fall decor, halloween, autumn, pumpkin | back to school, summer |
| September | Halloween / Thanksgiving | Sep 15 | halloween costume, trick or treat, thanksgiving | fall (keep), back to school |
| October | Holiday / Christmas | Oct 15 | christmas gift, holiday, stocking stuffer | halloween, trick or treat |
| November | Christmas / Hanukkah | Nov 1 | gift for him, gift for her, personalized gift | thanksgiving |
| December | Valentine's Day (early) | Dec 26 | new year, resolution, valentine (late month) | christmas, holiday |

---

## Seasonal Revenue Patterns

| Season | % of Annual Revenue | Peak Weeks | Prep Actions |
|--------|:-------------------:|:----------:|:-------------|
| Valentine's (Jan 15 - Feb 14) | % | 2 | Add romantic/gift keywords |
| Spring/Easter (Mar - Apr) | % | 3 | Add pastel/spring keywords |
| Mother's Day (Apr 15 - May 12) | % | 2 | Add mom/her keywords |
| Summer (Jun - Aug) | % | 8 | Add seasonal/outdoor keywords |
| Back to School (Jul - Aug) | % | 3 | Add student/teacher keywords |
| Halloween (Sep - Oct) | % | 4 | Add spooky/costume keywords |
| Holiday Season (Nov - Dec) | % | 8 | Add gift/christmas keywords |
| Off-Season (Jan, early Sep) | % | 6 | Focus on evergreen keywords |

---

## Evergreen Keywords (Never Remove)

| Keyword | Why It Works Year-Round |
|---------|------------------------|
| personalized | Top Etsy search term always |
| custom | Signals handmade/unique |
| handmade | Core Etsy buyer motivation |
| unique gift | Year-round gifting demand |
| [your niche] | Category-defining term |
| [your material] | Attribute searchers use always |

---

---

# FORMULA REFERENCE GUIDE

---

## Keyword Scoring

**Opportunity Score (1-25):**
```
=VolumeScore * CompetitionScore
```
Where Volume: Very High=5, High=4, Medium=3, Low=2, Very Low=1
And Competition: Very Low=5, Low=4, Medium=3, High=2, Very High=1

**Tag priority sort:**
```
=SORT(KeywordRange, OpportunityScoreColumn, FALSE)
```

## Title Optimization

**Character count:**
```
=LEN(A2)
```

**Characters remaining:**
```
=140 - LEN(A2)
```

**Word count:**
```
=LEN(TRIM(A2)) - LEN(SUBSTITUTE(TRIM(A2)," ","")) + 1
```

## Performance Tracking

**Conversion rate:**
```
=Sales / Views * 100
```

**Views per tag (approximate):**
```
=TotalListingViews / 13
```

**A/B test difference:**
```
=(VersionB - VersionA) / VersionA * 100
```

## Conditional Formatting Rules

**High opportunity score (green, score 15+):**
```
=F2 >= 15
```

**Over 20 characters (red — tag too long):**
```
=LEN(A2) > 20
```

**Title over 140 characters (red):**
```
=LEN(TitleCell) > 140
```

**Duplicate tag warning (orange):**
```
=COUNTIF(TagRange, B2) > 1
```

---

> **NOTE:** Etsy's search algorithm changes frequently. This spreadsheet gives you a systematic framework for keyword research regardless of algorithm updates. The core principle remains: match what buyers type into search with what your listing says. Update your keyword database monthly, swap seasonal tags 4-6 weeks before demand peaks, and always test changes rather than assuming. Free tools like eRank (limited) and Etsy's own search bar autocomplete are your best research starting points.
