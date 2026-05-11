# Amazon FBA Product Research Toolkit
## Product Scoring Matrix, Profit Calculator, Keyword Tracker & More

---

> **SETUP GUIDE — Get Running in 20 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 7 tabs/sheets and name them: Product Scoring Matrix, Profit Calculator, Keyword Tracker, Competitor Analysis, Supplier Comparison, Launch Checklist, Dashboard
> 3. Copy each section below into its corresponding sheet
> 4. Enter the formulas as documented (all formulas are marked with `FORMULA:`)
> 5. Start with the Product Scoring Matrix — enter 5-10 product ideas to evaluate
> 6. Use the Profit Calculator to validate your top-scoring products
>
> **Tip:** Research 20-30 product ideas before committing. The scoring matrix helps you compare objectively instead of going with gut feelings.

---

---

# SHEET 1: PRODUCT SCORING MATRIX

> Score and rank product ideas across key FBA success criteria. Higher total = better opportunity.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Product Idea** | **Category** | **Avg Price** | **Monthly Sales Est.** | **Review Count (Top 5)** | **Demand Score (1-10)** | **Competition Score (1-10)** | **Profit Margin Score (1-10)** | **Ease of Sourcing (1-10)** | **Differentiation (1-10)** | **Seasonality Risk (1-10)** | **Total Score** | **Weighted Score** | **Decision** |

## Scoring Guide

| Factor | 1-3 (Poor) | 4-6 (Average) | 7-10 (Excellent) |
|--------|-----------|--------------|-----------------|
| Demand | <100 units/mo | 100-500 units/mo | 500+ units/mo |
| Competition | >500 reviews avg | 100-500 reviews | <100 reviews avg |
| Profit Margin | <20% margin | 20-40% margin | 40%+ margin |
| Ease of Sourcing | Complex/regulated | Moderate complexity | Simple, many suppliers |
| Differentiation | Hard to improve | Some room to improve | Clear improvement opportunity |
| Seasonality Risk | Highly seasonal | Some seasonality | Year-round demand |

## Weight Settings (Customize)

| Factor | Default Weight | Your Weight |
|--------|---------------|-------------|
| Demand | 20% | |
| Competition | 25% | |
| Profit Margin | 20% | |
| Ease of Sourcing | 10% | |
| Differentiation | 15% | |
| Seasonality Risk | 10% | |

`FORMULA: Total Score = SUM(F:K)`
`FORMULA: Weighted Score = (F*weight1)+(G*weight2)+(H*weight3)+(I*weight4)+(J*weight5)+(K*weight6)`
`FORMULA: Decision = IF(M2>=7, "PURSUE", IF(M2>=5, "MAYBE", "PASS"))`

---

## Sample Entries

| Product Idea | Category | Avg Price | Monthly Sales | Reviews (Top 5) | Demand | Competition | Margin | Sourcing | Differentiation | Seasonality | Total | Weighted | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Silicone Ice Cube Tray | Kitchen | $14.99 | 3,200 | 1,200 avg | 8 | 4 | 6 | 9 | 5 | 7 | 39 | 5.8 | MAYBE |
| Bamboo Desk Organizer | Office | $24.99 | 800 | 350 avg | 6 | 6 | 7 | 8 | 7 | 9 | 43 | 6.9 | MAYBE |
| Pet Grooming Glove | Pets | $12.99 | 5,500 | 4,500 avg | 9 | 2 | 5 | 8 | 3 | 8 | 35 | 4.9 | PASS |

---

---

# SHEET 2: PROFIT CALCULATOR

> Calculate true profit per unit after ALL Amazon FBA costs.

---

## Product Cost Breakdown

| Field | Value | Notes |
|-------|-------|-------|
| **Product Name** | | |
| **ASIN / SKU** | | |
| **Selling Price** | $ | Your Amazon listing price |
| **Product Cost (per unit)** | $ | Manufacturing/wholesale cost |
| **Shipping to Amazon (per unit)** | $ | Freight/shipping divided by units |
| **Packaging Cost** | $ | Box, label, poly bag, inserts |
| **Total Landed Cost** | $ | Product + Shipping + Packaging |

---

## Amazon Fee Breakdown

| Fee Type | Amount | Formula |
|----------|--------|---------|
| **Referral Fee** | $ | Selling Price * Category % (typically 15%) |
| **FBA Fulfillment Fee** | $ | Based on size tier and weight |
| **Monthly Storage Fee** | $ | Based on cubic feet (Jan-Sep: $0.87/ft3, Oct-Dec: $2.40/ft3) |
| **Long-Term Storage Fee** | $ | If applicable (365+ days) |
| **Total Amazon Fees** | $ | Sum of all fees |

`FORMULA: Referral Fee = Selling Price * 0.15 (adjust for category)`
`FORMULA: Total Amazon Fees = Referral Fee + FBA Fee + Storage Fee + Long-Term Storage`

---

## Profit Calculation

| Metric | Value | Formula |
|--------|-------|---------|
| **Selling Price** | $ | |
| **Less: Total Landed Cost** | ($ ) | |
| **Less: Total Amazon Fees** | ($ ) | |
| **Less: PPC Ad Spend (per unit)** | ($ ) | Monthly PPC budget / monthly units sold |
| **Less: Returns/Refunds (est.)** | ($ ) | Selling Price * Return Rate % |
| **NET PROFIT PER UNIT** | **$** | |
| **Profit Margin %** | **%** | |
| **Monthly Profit (est.)** | **$** | Net Profit * Monthly Units |
| **Annual Profit (est.)** | **$** | Monthly Profit * 12 |
| **ROI %** | **%** | Net Profit / Total Landed Cost * 100 |

`FORMULA: Net Profit = Selling Price - Landed Cost - Amazon Fees - PPC - Returns`
`FORMULA: Profit Margin = Net Profit / Selling Price * 100`
`FORMULA: ROI = Net Profit / Total Landed Cost * 100`

---

## Break-Even Analysis

| Metric | Value |
|--------|-------|
| **Break-Even Units/Month** | |
| **Break-Even Revenue/Month** | $ |
| **Months to Recoup Investment** | |
| **Initial Investment Required** | $ |

`FORMULA: Break-Even Units = Fixed Costs / Net Profit Per Unit`
`FORMULA: Months to Recoup = Initial Investment / Monthly Profit`

---

## Size Tier Reference (FBA Fees)

| Size Tier | Max Weight | Max Dimensions | FBA Fee Range |
|-----------|-----------|----------------|--------------|
| Small Standard | 12 oz | 15x12x0.75 in | $3.22-$3.40 |
| Large Standard | 20 lb | 18x14x8 in | $3.86-$6.75+ |
| Small Oversize | 70 lb | 60x30 in | $9.73+ |
| Large Oversize | 150 lb | 108x max | $89.98+ |

---

---

# SHEET 3: KEYWORD TRACKER

> Track search volume, ranking, and keyword performance over time.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Keyword** | **Search Volume** | **Keyword Difficulty** | **Current Rank** | **Previous Rank** | **Rank Change** | **Relevance (1-5)** | **In Title?** | **In Bullets?** | **Notes** |

---

## Keyword Categories

| Category | Description |
|----------|-------------|
| Main Keywords | Primary product descriptors (highest volume) |
| Long-Tail Keywords | 3-5 word phrases with buyer intent |
| Competitor Keywords | Keywords competitors rank for that you don't |
| Backend Keywords | Hidden search terms in Seller Central |
| Branded Keywords | Your brand name + variations |

---

## Sample Entries

| Keyword | Search Vol | Difficulty | Rank | Prev Rank | Change | Relevance | Title? | Bullets? | Notes |
|---------|-----------|-----------|------|-----------|--------|-----------|--------|----------|-------|
| bamboo desk organizer | 12,400 | 67 | 15 | 22 | +7 | 5 | Yes | Yes | Main keyword |
| desk organizer with drawers | 8,200 | 52 | 8 | 12 | +4 | 4 | No | Yes | Long-tail |
| office desk accessories | 22,100 | 85 | 45 | — | New | 3 | No | No | Broad, hard to rank |

`FORMULA: Rank Change = Previous Rank - Current Rank (positive = improved)`

---

## Weekly Rank Tracking

| Keyword | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | Week 8 | Trend |
|---------|--------|--------|--------|--------|--------|--------|--------|--------|-------|
| [keyword 1] | | | | | | | | | |
| [keyword 2] | | | | | | | | | |
| [keyword 3] | | | | | | | | | |

`FORMULA: Trend = IF(Week8<Week1, "Improving", IF(Week8>Week1, "Declining", "Stable"))`

---

---

# SHEET 4: COMPETITOR ANALYSIS

> Deep-dive on your top 5-10 competitors for each product.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **ASIN** | **Brand** | **Product Title** | **Price** | **Rating** | **Review Count** | **Monthly Sales Est.** | **Monthly Revenue** | **Main Image Quality (1-5)** | **Listing Quality (1-5)** | **Weaknesses** | **Opportunities** |

---

## Sample Entries

| ASIN | Brand | Title | Price | Rating | Reviews | Sales/Mo | Revenue/Mo | Image | Listing | Weaknesses | Opportunities |
|------|-------|-------|-------|--------|---------|----------|-----------|-------|---------|-----------|--------------|
| B09XYZ123 | BambooLife | Bamboo Desk Organizer 5-Compartment | $27.99 | 4.3 | 1,245 | 620 | $17,354 | 4 | 3 | Poor bullets, no video | Better A+ content, video |
| B08ABC456 | DeskMaster | Large Desk Organizer Wood | $34.99 | 4.5 | 3,891 | 1,100 | $38,489 | 5 | 5 | Expensive, bulky | Smaller/cheaper option |
| B07DEF789 | OrganizeIt | Bamboo Desktop Shelf Organizer | $19.99 | 3.9 | 567 | 350 | $6,997 | 2 | 2 | Low quality images | Better images, bundle |

---

## Competitive Gap Analysis

| Feature/Element | Competitor 1 | Competitor 2 | Competitor 3 | YOUR PRODUCT |
|----------------|-------------|-------------|-------------|-------------|
| Price Point | | | | |
| Number of Images | | | | |
| A+ Content | Yes/No | Yes/No | Yes/No | |
| Video | Yes/No | Yes/No | Yes/No | |
| Bullet Points Quality | 1-5 | 1-5 | 1-5 | |
| Variation Count | | | | |
| Bundle Offer | Yes/No | Yes/No | Yes/No | |
| Warranty/Guarantee | | | | |

---

## Review Mining

| Competitor ASIN | Top Complaints (1-star) | Top Praise (5-star) | Feature Requests |
|----------------|------------------------|--------------------|--------------------|
| | | | |
| | | | |
| | | | |

---

---

# SHEET 5: SUPPLIER COMPARISON

> Compare potential suppliers side-by-side before committing to an order.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Supplier Name** | **Platform** | **Location** | **MOQ** | **Unit Price** | **Sample Cost** | **Lead Time** | **Payment Terms** | **Communication (1-5)** | **Quality Rating (1-5)** | **Certifications** | **Total Score** | **Status** |

## Platform Options (Dropdown)
- Alibaba
- Global Sources
- Made-in-China
- DHgate
- 1688
- Trade Show Contact
- Referral
- Direct Outreach

## Status Options (Dropdown)
- Researching
- Contacted
- Sample Ordered
- Sample Received
- Sample Approved
- Negotiating
- Order Placed
- Active Supplier
- Rejected

---

## Sample Entries

| Supplier | Platform | Location | MOQ | Unit Price | Sample | Lead Time | Payment | Comms | Quality | Certs | Score | Status |
|----------|----------|----------|-----|-----------|--------|-----------|---------|-------|---------|-------|-------|--------|
| Dongguan Best Co | Alibaba | Guangdong, CN | 500 | $3.20 | $50 | 25 days | 30/70 | 4 | 4 | ISO 9001 | 8 | Sample Ordered |
| Ningbo Eco Ltd | Alibaba | Zhejiang, CN | 1,000 | $2.85 | $35 | 30 days | 30/70 | 3 | 5 | FSC, ISO | 8 | Contacted |
| Vietnam Bamboo | Global Sources | Ho Chi Minh | 300 | $4.10 | $60 | 35 days | TT | 5 | 4 | None | 7 | Researching |

---

## Cost Comparison Calculator

| Cost Element | Supplier A | Supplier B | Supplier C |
|-------------|-----------|-----------|-----------|
| Unit Cost | $ | $ | $ |
| Shipping (per unit) | $ | $ | $ |
| Customs/Duty (per unit) | $ | $ | $ |
| Inspection Fee (per unit) | $ | $ | $ |
| **Total Landed Cost** | **$** | **$** | **$** |
| MOQ Total Investment | $ | $ | $ |

`FORMULA: Total Landed = Unit Cost + Shipping + Customs + Inspection`
`FORMULA: MOQ Total = Total Landed * MOQ`

---

## Supplier Communication Log

| Date | Supplier | Method | Topic | Response | Follow-Up Needed |
|------|----------|--------|-------|----------|-----------------|
| | | Email/Chat/Call | | | Yes/No |
| | | Email/Chat/Call | | | Yes/No |

---

---

# SHEET 6: LAUNCH CHECKLIST

> Step-by-step launch plan with dates and status tracking.

---

## Pre-Launch Phase (4-6 Weeks Before)

| # | Task | Due Date | Status | Owner | Notes |
|---|------|----------|--------|-------|-------|
| 1 | Finalize product design and specs | | | | |
| 2 | Place production order | | | | |
| 3 | Arrange product photography | | | | |
| 4 | Write listing copy (title, bullets, description) | | | | |
| 5 | Create A+ Content | | | | |
| 6 | Set up brand registry (if not done) | | | | |
| 7 | Create FBA shipping plan | | | | |
| 8 | Arrange freight forwarding | | | | |
| 9 | Set up PPC campaign structure | | | | |
| 10 | Research and finalize keywords | | | | |

## Launch Phase (Week 1-2)

| # | Task | Due Date | Status | Owner | Notes |
|---|------|----------|--------|-------|-------|
| 11 | List goes live — verify all content correct | | | | |
| 12 | Start PPC: Auto campaign ($20-30/day) | | | | |
| 13 | Start PPC: Manual broad match ($15-20/day) | | | | |
| 14 | Enroll in Vine (if eligible) | | | | |
| 15 | Request reviews (after 5+ orders) | | | | |
| 16 | Monitor listing daily — hijackers, suppression | | | | |
| 17 | Track keyword rankings daily | | | | |
| 18 | Adjust pricing if needed for velocity | | | | |

## Post-Launch Phase (Week 3-8)

| # | Task | Due Date | Status | Owner | Notes |
|---|------|----------|--------|-------|-------|
| 19 | Optimize PPC: add negative keywords | | | | |
| 20 | Launch exact match campaigns | | | | |
| 21 | A/B test main image | | | | |
| 22 | Respond to all customer questions | | | | |
| 23 | Analyze early reviews — quality issues? | | | | |
| 24 | Plan reorder based on velocity | | | | |
| 25 | Optimize listing based on search term report | | | | |

---

---

# SHEET 7: DASHBOARD

> At-a-glance overview of your FBA research progress.

---

## Product Pipeline Summary

| Status | Count | Products |
|--------|-------|----------|
| Researching | | |
| Scoring Complete | | |
| Profit Validated | | |
| Supplier Found | | |
| Sample Stage | | |
| Launching | | |
| Live | | |
| Rejected | | |

---

## Top Product Candidates

| Rank | Product | Weighted Score | Est. Monthly Profit | ROI % | Status |
|------|---------|---------------|--------------------|----|--------|
| 1 | | | $ | % | |
| 2 | | | $ | % | |
| 3 | | | $ | % | |
| 4 | | | $ | % | |
| 5 | | | $ | % | |

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Products Researched | |
| Products Passing Score Threshold | |
| Average Profit Margin (validated) | % |
| Average ROI (validated) | % |
| Total Estimated Monthly Profit (all live) | $ |
| Total Investment Required | $ |
| Active Suppliers | |
| Keywords Tracked | |

`FORMULA: Products Researched = COUNTA(Product Scoring Matrix!A:A) - 1`
`FORMULA: Passing Threshold = COUNTIF(Product Scoring Matrix!N:N, "PURSUE")`

---

---

# CHARTS & VISUALIZATIONS

> Create these charts from your data for quick visual insights.

---

## Recommended Charts

1. **Product Score Comparison** — Bar chart of Weighted Scores for all products evaluated
2. **Profit Margin Comparison** — Bar chart comparing margins across validated products
3. **Keyword Rank Trend** — Line chart showing weekly rank changes for top 10 keywords
4. **Competitor Price Map** — Scatter plot: Price vs. Rating for all competitors in niche
5. **Supplier Cost Comparison** — Grouped bar chart: landed cost breakdown by supplier
6. **Revenue Projection** — Line chart: projected monthly revenue for top 3 products

---

---

# FORMULA REFERENCE GUIDE

> All key formulas in plain English. Copy these into Google Sheets.

---

## Product Scoring Matrix

**Weighted Score:**
```
=(F2*$B$20)+(G2*$B$21)+(H2*$B$22)+(I2*$B$23)+(J2*$B$24)+(K2*$B$25)
```
*(Where B20:B25 contain your weight percentages)*

**Auto Decision:**
```
=IF(M2>=7, "PURSUE", IF(M2>=5, "MAYBE", "PASS"))
```

## Profit Calculator

**Net Profit Per Unit:**
```
=Selling_Price - Landed_Cost - Amazon_Fees - PPC_Per_Unit - Returns_Est
```

**ROI:**
```
=Net_Profit / Landed_Cost * 100
```

**Break-Even Units:**
```
=ROUNDUP(Fixed_Monthly_Costs / Net_Profit_Per_Unit, 0)
```

## Keyword Tracker

**Rank Change:**
```
=Previous_Rank - Current_Rank
```

**Rank Trend (sparkline):**
```
=SPARKLINE(B2:I2, {"charttype","line";"color","green"})
```

## Competitor Analysis

**Monthly Revenue:**
```
=Monthly_Sales * Price
```

**Average Market Price:**
```
=AVERAGE(D2:D10)
```

## Supplier Comparison

**Total Landed Cost:**
```
=Unit_Cost + Shipping_Per_Unit + Customs_Per_Unit + Inspection_Per_Unit
```

---

> **DISCLAIMER:** This research toolkit provides frameworks for Amazon FBA product evaluation. Actual results depend on market conditions, execution, and many external factors. Amazon's fee structure changes periodically — always verify current fees in Seller Central. Product research does not guarantee profitability. Do your due diligence and start with manageable investments.
