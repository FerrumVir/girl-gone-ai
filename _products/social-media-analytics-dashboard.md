# Social Media Analytics Dashboard — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Track performance across Instagram, TikTok, YouTube, and X (Twitter) all in one place.

---

> **SETUP GUIDE — Get Running in 15 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 7 tabs/sheets and name them: Instagram, TikTok, YouTube, X (Twitter), Cross-Platform Summary, Content Log, Dashboard
> 3. Copy each section below into its corresponding sheet
> 4. Enter the formulas as documented (all formulas are marked with `FORMULA:`)
> 5. Start by entering this week's data — the dashboard builds from historical entries
> 6. Update weekly for best trend analysis (daily optional for serious creators)
>
> **Tip:** Set a Sunday evening or Monday morning reminder to log last week's numbers. Consistency in tracking beats perfection.

---

---

# SHEET 1: INSTAGRAM ANALYTICS

> Track posts, stories, reels, and overall account growth.

---

## Account Overview (Update Weekly)

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Week Starting** | **Followers** | **New Followers** | **Unfollows** | **Net Growth** | **Growth Rate %** | **Profile Visits** | **Website Clicks** |

`FORMULA: Net Growth = New Followers - Unfollows`
`FORMULA: Growth Rate = Net Growth / Previous Week Followers * 100`

---

## Post Performance Tracker

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Date** | **Post Type** | **Content Topic** | **Likes** | **Comments** | **Saves** | **Shares** | **Reach** | **Impressions** | **Engagement Rate** | **Best Performing?** | **Notes** |

## Post Type (Dropdown)
- Single Image
- Carousel
- Reel
- Story
- Live
- Collab Post

`FORMULA: Engagement Rate = (Likes + Comments + Saves + Shares) / Reach * 100`
`FORMULA: Best Performing = IF(J2 > AVERAGE(J:J), "YES", "")`

---

## Instagram Benchmarks

| Metric | Industry Average | Your Average | Your Best | Goal |
|--------|-----------------|-------------|-----------|------|
| Engagement Rate (Feed) | 1.5-3.5% | | | |
| Engagement Rate (Reels) | 3-8% | | | |
| Reach Rate | 20-35% | | | |
| Save Rate | 1-3% | | | |
| Share Rate | 0.5-2% | | | |
| Story Completion Rate | 70-85% | | | |

---

## Monthly Summary

| Month | Posts | Reels | Stories | Avg Engagement | Top Post Type | Net Follower Growth | Total Reach |
|-------|-------|-------|---------|---------------|---------------|--------------------:|-------------|
| January | | | | | | | |
| February | | | | | | | |
| March | | | | | | | |
| April | | | | | | | |
| May | | | | | | | |
| June | | | | | | | |
| July | | | | | | | |
| August | | | | | | | |
| September | | | | | | | |
| October | | | | | | | |
| November | | | | | | | |
| December | | | | | | | |

---

---

# SHEET 2: TIKTOK ANALYTICS

> Track video performance, follower growth, and virality metrics.

---

## Account Overview (Update Weekly)

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| **Week Starting** | **Followers** | **Net Growth** | **Growth Rate %** | **Total Video Views (week)** | **Profile Views** | **Unique Viewers** |

---

## Video Performance Tracker

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Date** | **Video Topic** | **Sound Used** | **Hashtags** | **Views** | **Likes** | **Comments** | **Shares** | **Saves** | **Watch Time (avg)** | **Completion Rate %** | **Engagement Rate** | **Viral?** |

`FORMULA: Engagement Rate = (Likes + Comments + Shares + Saves) / Views * 100`
`FORMULA: Viral = IF(E2 > AVERAGE(E:E)*5, "VIRAL", IF(E2 > AVERAGE(E:E)*2, "HIT", ""))`

---

## TikTok Benchmarks

| Metric | Average Creator | Top 10% Creators | Your Average | Goal |
|--------|----------------|-----------------|-------------|------|
| Engagement Rate | 3-6% | 10%+ | | |
| Completion Rate | 30-50% | 70%+ | | |
| Views/Follower Ratio | 0.1-0.5x | 1x+ | | |
| Share Rate | 0.5-2% | 3%+ | | |
| Save Rate | 1-3% | 5%+ | | |

---

## Trending Analysis

| Week | Top Sound Used | Top Hashtag | Best Performing Niche/Topic | Best Post Time | Views Multiple vs. Avg |
|------|--------------|-------------|---------------------------|---------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

---

## Monthly Summary

| Month | Videos Posted | Total Views | Avg Views | Top Video Views | Avg Engagement | Net Followers | Viral Videos |
|-------|-------------|-------------|-----------|----------------|---------------|--------------|-------------|
| January | | | | | | | |
| February | | | | | | | |
| March | | | | | | | |
| April | | | | | | | |
| May | | | | | | | |
| June | | | | | | | |
| July | | | | | | | |
| August | | | | | | | |
| September | | | | | | | |
| October | | | | | | | |
| November | | | | | | | |
| December | | | | | | | |

---

---

# SHEET 3: YOUTUBE ANALYTICS

> Track videos, shorts, subscribers, and revenue metrics.

---

## Channel Overview (Update Weekly)

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Week Starting** | **Subscribers** | **Net Sub Growth** | **Total Views (week)** | **Watch Hours** | **Avg View Duration** | **Impressions** | **CTR %** |

`FORMULA: CTR = (Views / Impressions) * 100`

---

## Video Performance Tracker

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Publish Date** | **Title** | **Type** | **Views (48hr)** | **Views (7d)** | **Views (30d)** | **Likes** | **Comments** | **CTR %** | **Avg View Duration** | **Retention %** | **Revenue** |

## Type (Dropdown)
- Long-form
- Short
- Live
- Premiere

---

## YouTube Benchmarks

| Metric | Small Channel (<10K) | Medium (10-100K) | Large (100K+) | Your Average | Goal |
|--------|---------------------|------------------|--------------|-------------|------|
| CTR | 4-8% | 5-10% | 6-12% | | |
| Avg View Duration | 3-5 min | 5-8 min | 8-12 min | | |
| Retention Rate | 30-40% | 40-55% | 50-65% | | |
| Sub Conversion | 1-3% | 2-5% | 3-7% | | |
| Views/Sub Ratio | 0.1-0.3x | 0.2-0.5x | 0.3-1x | | |

---

## Revenue Tracker (If Monetized)

| Month | Ad Revenue | Memberships | Super Chats | Affiliate | Sponsorships | **Total** |
|-------|-----------|-------------|-------------|-----------|-------------|-----------|
| January | $ | $ | $ | $ | $ | $ |
| February | $ | $ | $ | $ | $ | $ |
| March | $ | $ | $ | $ | $ | $ |
| April | $ | $ | $ | $ | $ | $ |
| May | $ | $ | $ | $ | $ | $ |
| June | $ | $ | $ | $ | $ | $ |
| July | $ | $ | $ | $ | $ | $ |
| August | $ | $ | $ | $ | $ | $ |
| September | $ | $ | $ | $ | $ | $ |
| October | $ | $ | $ | $ | $ | $ |
| November | $ | $ | $ | $ | $ | $ |
| December | $ | $ | $ | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** | **$** | **$** | **$** |

---

---

# SHEET 4: X (TWITTER) ANALYTICS

> Track tweets, engagement, follower growth, and reach.

---

## Account Overview (Update Weekly)

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| **Week Starting** | **Followers** | **Net Growth** | **Impressions** | **Profile Visits** | **Mentions** | **Link Clicks** |

---

## Post Performance Tracker

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Date** | **Post Type** | **Content/Topic** | **Impressions** | **Likes** | **Reposts** | **Replies** | **Bookmarks** | **Link Clicks** | **Engagement Rate** |

## Post Type (Dropdown)
- Text Only
- Image
- Video
- Thread
- Poll
- Quote Post

`FORMULA: Engagement Rate = (Likes + Reposts + Replies + Bookmarks) / Impressions * 100`

---

## X Benchmarks

| Metric | Average | Top Performer | Your Average | Goal |
|--------|---------|--------------|-------------|------|
| Engagement Rate | 1-3% | 5%+ | | |
| Reply Rate | 0.2-0.5% | 1%+ | | |
| Repost Rate | 0.3-1% | 2%+ | | |
| Link CTR | 0.5-2% | 3%+ | | |
| Impressions/Follower | 0.05-0.2x | 0.5x+ | | |

---

## Monthly Summary

| Month | Posts | Threads | Avg Impressions | Avg Engagement | Top Post Impressions | Net Followers | Total Link Clicks |
|-------|-------|---------|----------------|---------------|---------------------|--------------|-------------------|
| January | | | | | | | |
| February | | | | | | | |
| March | | | | | | | |
| April | | | | | | | |
| May | | | | | | | |
| June | | | | | | | |

---

---

# SHEET 5: CROSS-PLATFORM SUMMARY

> Compare performance across all platforms side-by-side.

---

## Weekly Cross-Platform Snapshot

| Metric | Instagram | TikTok | YouTube | X | **Total** |
|--------|-----------|--------|---------|---|-----------|
| Followers | | | | | |
| Net Growth This Week | | | | | |
| Growth Rate % | | | | | |
| Content Published | | | | | |
| Total Reach/Views | | | | | |
| Avg Engagement Rate | | | | | |
| Website/Link Clicks | | | | | |
| Best Content Type | | | | | |

---

## Monthly Growth Comparison

| Month | IG Followers | TT Followers | YT Subscribers | X Followers | Total Audience | Best Platform |
|-------|-------------|-------------|---------------|-------------|---------------|--------------|
| January | | | | | | |
| February | | | | | | |
| March | | | | | | |
| April | | | | | | |
| May | | | | | | |
| June | | | | | | |

`FORMULA: Total Audience = IG + TT + YT + X`
`FORMULA: Best Platform = INDEX(platforms, MATCH(MAX(growth_rates), growth_rates, 0))`

---

## Content Repurposing Tracker

| Original Content | Platform | Repurposed To | Platform | Performance Comparison | Worth Repurposing? |
|-----------------|----------|--------------|----------|----------------------|-------------------|
| | | | | | Yes/No |
| | | | | | Yes/No |
| | | | | | Yes/No |

---

---

# SHEET 6: CONTENT LOG

> Master log of all content published across platforms.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Date** | **Platform** | **Content Type** | **Topic/Hook** | **Content Pillar** | **Hashtags/Keywords** | **Engagement Rate** | **Reach** | **Link/CTA** | **Learnings** |

## Content Pillars (Dropdown — Customize)
- Educational
- Entertaining
- Inspirational
- Behind-the-Scenes
- Product/Service
- Community/UGC
- Trending/Timely
- Personal Story

---

## Best Performing Content Analysis

| Rank | Date | Platform | Topic | Why It Worked | Engagement Rate | Replicate? |
|------|------|----------|-------|--------------|----------------|-----------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

---

# SHEET 7: DASHBOARD

> At-a-glance metrics for quick weekly review.

---

## This Week's Highlights

| Metric | This Week | Last Week | Change | Trend |
|--------|-----------|-----------|--------|-------|
| Total Audience (all platforms) | | | | |
| Total Content Published | | | | |
| Average Engagement Rate | | | | |
| Total Reach/Impressions | | | | |
| Website Clicks | | | | |
| Best Platform This Week | | | | |
| Top Content Piece | | | | |

`FORMULA: Change = This Week - Last Week`
`FORMULA: Trend = IF(Change>0, "Up", IF(Change<0, "Down", "Flat"))`

---

## 90-Day Trends (Sparklines)

| Metric | Last 12 Weeks Trend | Current | 90-Day Avg |
|--------|--------------------:|--------:|-----------:|
| Total Followers | [sparkline] | | |
| Avg Engagement | [sparkline] | | |
| Weekly Reach | [sparkline] | | |
| Content Volume | [sparkline] | | |

```
=SPARKLINE(last_12_weeks_data, {"charttype","line";"color","#6366f1"})
```

---

## Platform Health Scorecard

| Platform | Growth | Engagement | Consistency | Reach | Overall Score |
|----------|--------|-----------|-------------|-------|--------------|
| Instagram | /10 | /10 | /10 | /10 | /40 |
| TikTok | /10 | /10 | /10 | /10 | /40 |
| YouTube | /10 | /10 | /10 | /10 | /40 |
| X | /10 | /10 | /10 | /10 | /40 |

---

---

# CHARTS & VISUALIZATIONS

> Create these charts for visual performance tracking.

---

## Recommended Charts

1. **Follower Growth (All Platforms)** — Line chart, one line per platform, weekly data points
2. **Engagement Rate Trends** — Line chart comparing engagement across platforms over time
3. **Content Type Performance** — Bar chart showing avg engagement by content type
4. **Best Posting Times** — Heatmap showing engagement by day of week and time
5. **Platform Reach Comparison** — Stacked bar chart, weekly total reach by platform
6. **Growth Rate Comparison** — Line chart, weekly growth rate % by platform

---

---

# FORMULA REFERENCE GUIDE

---

## Universal Engagement Formula

**Standard Engagement Rate:**
```
=(Likes + Comments + Shares + Saves) / Reach * 100
```

**Growth Rate:**
```
=(Current_Followers - Previous_Followers) / Previous_Followers * 100
```

## Conditional Formatting Rules

**Engagement Rate (green if above average):**
```
=J2 > AVERAGE($J:$J)
```

**Growth Rate (red if negative):**
```
=E2 < 0
```

**Viral Detection:**
```
=IF(Views > AVERAGE(Views_Column)*5, "VIRAL", IF(Views > AVERAGE(Views_Column)*2, "HIT", ""))
```

## Cross-Platform Calculations

**Total Audience:**
```
=IG_Followers + TT_Followers + YT_Subscribers + X_Followers
```

**Best Platform (by growth rate):**
```
=INDEX({"Instagram","TikTok","YouTube","X"}, MATCH(MAX(growth_rates), growth_rates, 0))
```

**Content Consistency Score:**
```
=Posts_This_Week / Target_Posts_Per_Week * 10
```

---

> **NOTE:** Platform algorithms and metrics change frequently. Benchmark data provided is based on 2025-2026 averages and should be updated as industry standards evolve. Focus on YOUR trends over time rather than comparing to universal benchmarks.
