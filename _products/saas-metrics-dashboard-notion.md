# SaaS Metrics Dashboard — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with MRR, churn, LTV, and CAC formulas built in. Monthly snapshots create a time series for trend analysis. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Monthly Snapshots

**Purpose:** One entry per month capturing all key SaaS metrics at that point in time. This is your time-series database — each row is a monthly photograph of your business. Over time, this creates the trend data that drives fundraising decks and board reports.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Month | Title | Format: "YYYY-MM" (e.g., "2026-05") |
| Date | Date | First day of the month |
| MRR | Number (USD) | Monthly Recurring Revenue at end of month |
| ARR | Formula | `prop("MRR") * 12` |
| New MRR | Number (USD) | MRR from new customers acquired this month |
| Expansion MRR | Number (USD) | MRR from upgrades/upsells of existing customers |
| Churned MRR | Number (USD) | MRR lost from cancellations (positive number) |
| Contraction MRR | Number (USD) | MRR lost from downgrades (positive number) |
| Net New MRR | Formula | `prop("New MRR") + prop("Expansion MRR") - prop("Churned MRR") - prop("Contraction MRR")` |
| MRR Growth Rate | Number | Month-over-month MRR growth % (manual — compare to prior month) |
| Total Customers | Number | Active paying customers at end of month |
| New Customers | Number | Customers acquired this month |
| Churned Customers | Number | Customers lost this month |
| Customer Churn Rate | Formula | `if(prop("Total Customers") == 0, 0, round(prop("Churned Customers") / (prop("Total Customers") + prop("Churned Customers")) * 10000) / 100)` |
| Revenue Churn Rate | Formula | `if(prop("MRR") == 0, 0, round(prop("Churned MRR") / (prop("MRR") + prop("Churned MRR")) * 10000) / 100)` |
| Net Revenue Retention | Formula | `if((prop("MRR") - prop("Net New MRR")) == 0, 0, round((prop("MRR") - prop("New MRR")) / (prop("MRR") - prop("Net New MRR")) * 10000) / 100)` |
| ARPU | Formula | `if(prop("Total Customers") == 0, 0, round(prop("MRR") / prop("Total Customers") * 100) / 100)` |
| LTV | Formula | `if(prop("Customer Churn Rate") == 0, 0, round(prop("ARPU") / (prop("Customer Churn Rate") / 100) * 100) / 100)` |
| Total Spend (Sales + Marketing) | Number (USD) | All customer acquisition spend this month |
| CAC | Formula | `if(prop("New Customers") == 0, 0, round(prop("Total Spend (Sales + Marketing)") / prop("New Customers") * 100) / 100)` |
| LTV:CAC Ratio | Formula | `if(prop("CAC") == 0, 0, round(prop("LTV") / prop("CAC") * 10) / 10)` |
| CAC Payback (months) | Formula | `if(prop("ARPU") == 0, 0, round(prop("CAC") / prop("ARPU") * 10) / 10)` |
| Monthly Burn | Number (USD) | Total monthly expenses |
| Revenue | Number (USD) | Total revenue collected this month (may differ from MRR due to annual plans) |
| Gross Margin % | Number | (Revenue - COGS) / Revenue * 100 |
| Cash Balance | Number (USD) | Bank balance at end of month |
| Runway (months) | Formula | `if(prop("Monthly Burn") == 0, 999, if(prop("Revenue") >= prop("Monthly Burn"), 999, round(prop("Cash Balance") / (prop("Monthly Burn") - prop("Revenue")) * 10) / 10))` |
| Trial Starts | Number | Free trial signups this month |
| Trial Conversions | Number | Trials that converted to paid |
| Trial Conversion Rate | Formula | `if(prop("Trial Starts") == 0, 0, round(prop("Trial Conversions") / prop("Trial Starts") * 10000) / 100)` |
| Notes | Text | Context: product launches, pricing changes, market events |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")` |

**Views:**

- **Monthly Timeline** — Table, sorted by Date descending (main view — your monthly record)
- **Growth Metrics** — Table showing Month, MRR, Net New MRR, MRR Growth Rate, Total Customers
- **Unit Economics** — Table showing Month, ARPU, LTV, CAC, LTV:CAC, CAC Payback
- **Churn Analysis** — Table showing Month, Customer Churn Rate, Revenue Churn Rate, Net Revenue Retention
- **Financial Health** — Table showing Month, Revenue, Monthly Burn, Cash Balance, Runway
- **By Quarter** — Table, grouped by Quarter
- **Acquisition** — Table showing Month, New Customers, Trial Starts, Trial Conversion Rate, CAC

---

### 2. Customers

**Purpose:** Individual customer records for cohort analysis, churn prediction, and expansion opportunity tracking. Each customer links to their plan, MRR contribution, and lifecycle events.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Customer Name | Title | Company or individual name |
| Email | Email | Primary contact |
| Plan | Select | Free / Starter / Growth / Pro / Enterprise / Custom |
| MRR | Number (USD) | Their current monthly payment |
| Status | Select | Trial / Active / At Risk / Churned / Paused / Delinquent |
| Signup Date | Date | When they first signed up |
| Converted Date | Date | When trial converted to paid (if applicable) |
| Churned Date | Date | When they cancelled |
| Lifetime (days) | Formula | `if(prop("Status") == "Churned", dateBetween(prop("Churned Date"), prop("Signup Date"), "days"), dateBetween(now(), prop("Signup Date"), "days"))` |
| Lifetime Value | Formula | `prop("MRR") * round(prop("Lifetime (days)") / 30)` |
| Cohort Month | Formula | `formatDate(prop("Signup Date"), "YYYY-MM")` |
| Acquisition Channel | Select | Organic / Paid Search / Paid Social / Content / Referral / Partnership / Cold Outreach / Product Hunt / Marketplace |
| Company Size | Select | 1 (Solo) / 2-10 / 11-50 / 51-200 / 201-500 / 500+ |
| Industry | Select | Technology / Marketing / Finance / Healthcare / Education / E-commerce / Agency / SaaS / Other |
| Health Score | Select | Healthy / Neutral / At Risk / Critical |
| Last Login | Date | Most recent product usage |
| Days Since Login | Formula | `if(empty(prop("Last Login")), "Never", format(dateBetween(now(), prop("Last Login"), "days")) + " days")` |
| Usage Level | Select | Power User / Regular / Light / Dormant |
| NPS Score | Number | Last NPS response (1-10) |
| Expansion Potential | Select | High / Medium / Low / None |
| Annual Value | Formula | `prop("MRR") * 12` |
| Notes | Text | Key context, support history, expansion notes |
| Tags | Multi-select | Beta Tester / Case Study / Referral Source / Enterprise Lead / Feature Request |

**Views:**

- **All Customers** — Table, sorted by MRR descending
- **Active** — Filter: Status = Active, sorted by MRR descending
- **At Risk** — Filter: Status = At Risk OR Health Score = At Risk or Critical
- **By Plan** — Table, grouped by Plan
- **By Cohort** — Table, grouped by Cohort Month (for retention analysis)
- **Churned** — Filter: Status = Churned, sorted by Churned Date descending
- **Dormant** — Filter: Usage Level = Dormant AND Status = Active (churn risk)
- **Expansion Targets** — Filter: Expansion Potential = High, Status = Active
- **By Channel** — Table, grouped by Acquisition Channel
- **Top Customers** — Sorted by MRR descending, limit 20
- **Trials** — Filter: Status = Trial, sorted by Signup Date

---

### 3. Revenue Events

**Purpose:** Logs every revenue-affecting event — new subscriptions, upgrades, downgrades, cancellations, and reactivations. Creates an audit trail for MRR movements and feeds into monthly snapshot calculations.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Event | Title | Brief description (e.g., "Acme Corp upgraded to Pro") |
| Customer | Relation | -> Customers database |
| Customer Name | Rollup | From Customer relation |
| Date | Date | When this event occurred |
| Type | Select | New / Upgrade / Downgrade / Churn / Reactivation / Expansion / Contraction |
| Previous MRR | Number (USD) | MRR before this event |
| New MRR | Number (USD) | MRR after this event |
| MRR Change | Formula | `prop("New MRR") - prop("Previous MRR")` |
| Previous Plan | Select | Free / Starter / Growth / Pro / Enterprise / Custom |
| New Plan | Select | Free / Starter / Growth / Pro / Enterprise / Custom / Cancelled |
| Reason | Text | Why did this happen? (especially important for churn and downgrades) |
| Channel | Rollup | Acquisition Channel from Customer |
| Month | Formula | `formatDate(prop("Date"), "YYYY-MM")` |
| Preventable | Checkbox | Could this churn/downgrade have been prevented? |
| Recovery Action | Text | What was attempted to save/recover? |
| Tags | Multi-select | Price Sensitivity / Feature Gap / Support Issue / Competitor / Budget Cut / Bad Fit / Outgrown |

**Views:**

- **All Events** — Table, sorted by Date descending
- **This Month** — Filter: Date is current month
- **New Revenue** — Filter: Type = New or Upgrade or Expansion
- **Lost Revenue** — Filter: Type = Churn or Downgrade or Contraction
- **By Month** — Table, grouped by Month
- **Churn Reasons** — Filter: Type = Churn, grouped by Reason
- **By Type** — Table, grouped by Type
- **Preventable Losses** — Filter: Preventable = true (for retrospectives)

---

### 4. Acquisition Channels

**Purpose:** Tracks performance of each customer acquisition channel over time. Shows spend, conversions, and unit economics per channel so you can allocate budget to what works.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Channel + Month | Title | "[Channel] — [YYYY-MM]" (e.g., "Paid Search — 2026-05") |
| Channel | Select | Organic / Paid Search / Paid Social / Content / Referral / Partnership / Cold Outreach / Product Hunt / Marketplace |
| Month | Date | First day of the month being reported |
| Spend | Number (USD) | Total spend on this channel this month |
| Leads Generated | Number | Marketing qualified leads |
| Trials Started | Number | Free trial signups from this channel |
| Customers Won | Number | Paid conversions from this channel |
| Revenue Won | Number (USD) | Total MRR from customers acquired via this channel this month |
| Cost Per Lead | Formula | `if(prop("Leads Generated") == 0, 0, round(prop("Spend") / prop("Leads Generated") * 100) / 100)` |
| Cost Per Trial | Formula | `if(prop("Trials Started") == 0, 0, round(prop("Spend") / prop("Trials Started") * 100) / 100)` |
| CAC (Channel) | Formula | `if(prop("Customers Won") == 0, 0, round(prop("Spend") / prop("Customers Won") * 100) / 100)` |
| Lead-to-Customer Rate | Formula | `if(prop("Leads Generated") == 0, 0, round(prop("Customers Won") / prop("Leads Generated") * 10000) / 100)` |
| Trial-to-Paid Rate | Formula | `if(prop("Trials Started") == 0, 0, round(prop("Customers Won") / prop("Trials Started") * 10000) / 100)` |
| ROI | Formula | `if(prop("Spend") == 0, 0, round((prop("Revenue Won") * 12 - prop("Spend")) / prop("Spend") * 100))` |
| Notes | Text | Campaign details, experiments run, observations |

**Views:**

- **All Channels** — Table, sorted by Month descending
- **By Channel** — Table, grouped by Channel (compare performance across months)
- **This Month** — Filter: Month is current month
- **Best Performing** — Sorted by ROI descending
- **Spend Analysis** — Table showing Channel, Spend, CAC, ROI per month
- **Channel Comparison** — Table showing latest month for each channel side-by-side

---

### 5. Cohort Retention

**Purpose:** Monthly retention data by signup cohort. Each entry tracks what percentage of a cohort's original customers (and revenue) is still active at Month 1, Month 2, Month 3, etc. Essential for understanding true lifetime value and identifying if retention is improving over time.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Cohort Entry | Title | "[Signup Month] — Month [N]" (e.g., "2026-01 — Month 3") |
| Cohort Month | Select | 2025-07 / 2025-08 / ... / 2026-05 (signup month) |
| Months Since Signup | Number | 0, 1, 2, 3... (0 = signup month) |
| Starting Customers | Number | How many customers signed up in this cohort |
| Remaining Customers | Number | How many are still active at this point |
| Customer Retention % | Formula | `if(prop("Starting Customers") == 0, 0, round(prop("Remaining Customers") / prop("Starting Customers") * 10000) / 100)` |
| Starting MRR | Number (USD) | Total MRR from this cohort at signup |
| Current MRR | Number (USD) | Total MRR from this cohort now |
| Revenue Retention % | Formula | `if(prop("Starting MRR") == 0, 0, round(prop("Current MRR") / prop("Starting MRR") * 10000) / 100)` |
| Net Revenue Retention % | Formula | `if(prop("Starting MRR") == 0, 0, round(prop("Current MRR") / prop("Starting MRR") * 10000) / 100)` |
| Notes | Text | Observations about this cohort's behavior |

**Views:**

- **Cohort Table** — Table, grouped by Cohort Month, sorted by Months Since Signup ascending (classic cohort grid)
- **Latest Data** — Filter: most recent entry per cohort
- **By Retention Month** — Table, grouped by Months Since Signup (see retention at each month across cohorts)
- **Best Cohorts** — Sorted by Customer Retention % descending at Month 3+
- **Revenue Retention** — Table showing Cohort Month, Months Since Signup, Revenue Retention %

---

## DASHBOARD

> Create this as the top-level page. This is your investor-ready metrics dashboard — the single view that tells you whether your SaaS business is healthy.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  SAAS METRICS DASHBOARD                          May 2026         |
+--------+----------+---------+----------+---------+---------------+
|  MRR   |  Growth  |  Churn  |  LTV:CAC |  NRR   |  Runway       |
| $47.2K | +8.3%    |  3.1%   |  4.2x    | 112%   |  18 months    |
+--------+----------+---------+----------+---------+---------------+
|                                                                    |
|  MRR TREND                                                        |
|  [Linked view -> Monthly Snapshots, last 12 months,               |
|   showing MRR as timeline/chart]                                  |
|                                                                    |
|  $50K |          ..........*                                       |
|  $40K |     ....*                                                  |
|  $30K |  ..*                                                       |
|  $20K | *                                                          |
|       +---+---+---+---+---+---+---+---+---+---+---+---           |
|        Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May             |
|                                                                    |
+----------------------------------+-------------------------------+
|  THIS MONTH'S MOVEMENTS          |  UNIT ECONOMICS               |
|  New MRR: +$4,200               |  ARPU: $89                    |
|  Expansion: +$1,800             |  LTV: $2,871                  |
|  Churned: -$1,450               |  CAC: $683                    |
|  Net New: +$4,550               |  LTV:CAC: 4.2x               |
|                                  |  Payback: 7.7 months          |
+----------------------------------+-------------------------------+
|  AT-RISK CUSTOMERS               |  RECENT REVENUE EVENTS        |
|  [Linked view -> Customers,      |  [Linked view -> Revenue       |
|   At Risk or Critical]           |   Events, last 10]            |
+----------------------------------+-------------------------------+
|  CHANNEL PERFORMANCE                                              |
|  [Linked view -> Acquisition Channels, this month, showing        |
|   Channel, Spend, Customers Won, CAC, ROI]                       |
+----------------------------------+-------------------------------+
|  COHORT RETENTION SNAPSHOT       |  TRIALS PIPELINE              |
|  [Linked view -> Cohort          |  [Linked view -> Customers,   |
|   Retention, latest data]        |   Status = Trial]             |
+------------------------------------------------------------------+
```

### Summary Stat Blocks (callout blocks, 6-column layout)

- **MRR** — Current month from Monthly Snapshots
- **MoM Growth** — MRR Growth Rate from latest snapshot
- **Customer Churn** — Customer Churn Rate from latest snapshot
- **LTV:CAC** — From latest snapshot (target: 3x+)
- **NRR** — Net Revenue Retention (target: 100%+)
- **Runway** — Months of runway remaining

---

## KEY FORMULA REFERENCE

### Annual Recurring Revenue

```
prop("MRR") * 12
```

### Net New MRR

```
prop("New MRR") + prop("Expansion MRR") - prop("Churned MRR") - prop("Contraction MRR")
```

### Customer Churn Rate (monthly)

```
if(
  prop("Total Customers") == 0,
  0,
  round(
    prop("Churned Customers") / (prop("Total Customers") + prop("Churned Customers")) * 10000
  ) / 100
)
```

Note: Denominator is start-of-month customers (Total + Churned gives you start-of-month count).

### Revenue Churn Rate (monthly)

```
if(
  prop("MRR") == 0,
  0,
  round(
    prop("Churned MRR") / (prop("MRR") + prop("Churned MRR")) * 10000
  ) / 100
)
```

### Average Revenue Per User (ARPU)

```
if(
  prop("Total Customers") == 0,
  0,
  round(prop("MRR") / prop("Total Customers") * 100) / 100
)
```

### Customer Lifetime Value (LTV)

```
if(
  prop("Customer Churn Rate") == 0,
  0,
  round(prop("ARPU") / (prop("Customer Churn Rate") / 100) * 100) / 100
)
```

LTV = ARPU / Monthly Churn Rate. This assumes constant churn, which is a simplification — but it's the standard formula used by investors.

### Customer Acquisition Cost (CAC)

```
if(
  prop("New Customers") == 0,
  0,
  round(prop("Total Spend (Sales + Marketing)") / prop("New Customers") * 100) / 100
)
```

### LTV:CAC Ratio

```
if(
  prop("CAC") == 0,
  0,
  round(prop("LTV") / prop("CAC") * 10) / 10
)
```

Target: 3x or higher. Below 3x means you're spending too much to acquire customers relative to their lifetime value. Above 5x might mean you're underinvesting in growth.

### CAC Payback Period (months)

```
if(
  prop("ARPU") == 0,
  0,
  round(prop("CAC") / prop("ARPU") * 10) / 10
)
```

How many months until a new customer has paid back their acquisition cost. Target: under 12 months.

### Runway Calculation

```
if(
  prop("Monthly Burn") == 0,
  999,
  if(
    prop("Revenue") >= prop("Monthly Burn"),
    999,
    round(prop("Cash Balance") / (prop("Monthly Burn") - prop("Revenue")) * 10) / 10
  )
)
```

If revenue exceeds burn, runway is infinite (999). Otherwise: Cash / (Burn - Revenue).

### Trial Conversion Rate

```
if(
  prop("Trial Starts") == 0,
  0,
  round(prop("Trial Conversions") / prop("Trial Starts") * 10000) / 100
)
```

### Channel ROI

```
if(
  prop("Spend") == 0,
  0,
  round((prop("Revenue Won") * 12 - prop("Spend")) / prop("Spend") * 100)
)
```

Annualizes first-month MRR to estimate 12-month revenue, then calculates return on spend.

---

## BENCHMARK REFERENCE

| Metric | Seed Stage | Series A | Growth Stage |
|---|---|---|---|
| MRR Growth (MoM) | 15-20% | 10-15% | 5-10% |
| Customer Churn | <8% | <5% | <3% |
| Revenue Churn | <6% | <3% | <1% (net negative ideal) |
| NRR | >100% | >110% | >120% |
| LTV:CAC | >3x | >3x | >4x |
| CAC Payback | <18 months | <12 months | <12 months |
| Gross Margin | >60% | >70% | >80% |
| Trial Conversion | >10% | >15% | >20% |

---

## QUICK-START GUIDE

### Step 1 — Create Your First Monthly Snapshot (15 minutes)

- Open **Monthly Snapshots** and create an entry for the current month
- Fill in: MRR, Total Customers, New Customers, Churned Customers
- Fill in: New MRR, Expansion MRR, Churned MRR, Contraction MRR
- Add: Total Spend (Sales + Marketing), Monthly Burn, Cash Balance, Revenue
- All formulas will auto-calculate once inputs are provided

### Step 2 — Add Your Customers (15 minutes)

- Open the **Customers** database
- Add all current paying customers with Plan, MRR, Signup Date, and Status
- Set Acquisition Channel for each (needed for channel analysis)
- Add Health Score based on usage patterns
- Mark At Risk customers who show declining engagement

### Step 3 — Log Recent Revenue Events (10 minutes)

- Open **Revenue Events** and add the last month's subscription changes
- Include: new signups, upgrades, downgrades, and cancellations
- For churned customers: always fill in Reason and whether it was Preventable

### Step 4 — Set Up Acquisition Channels (10 minutes)

- Open **Acquisition Channels** and add one entry per active channel for this month
- Fill in Spend, Leads Generated, Trials Started, Customers Won
- CAC and ROI will auto-calculate

### Step 5 — Start Cohort Tracking (10 minutes)

- Open **Cohort Retention** and add entries for your last 3-6 months of cohorts
- For each cohort: note Starting Customers and current Remaining Customers
- Add entries at Month 1, Month 2, Month 3, etc.

### Step 6 — Build Your Dashboard

- Create the top-level page following the Dashboard Layout
- Pin to sidebar — review weekly, update monthly

### Step 7 — Monthly Rhythm

**On the 1st of every month:**
1. Create new Monthly Snapshot with all end-of-prior-month numbers
2. Update Customer statuses (mark any churned, update Health Scores)
3. Log all Revenue Events from the prior month
4. Add new Acquisition Channel entries for the prior month
5. Update Cohort Retention entries
6. Review Dashboard and note trends

### Pro Tips

- MRR Growth Rate is the single most important metric for early-stage SaaS. If you can only track one thing, track this.
- Net Revenue Retention above 100% means existing customers are growing faster than churning. This is the holy grail — it means you can grow without acquiring new customers.
- Always log churn reasons. After 20+ churn events, patterns emerge that tell you exactly what to fix in your product, pricing, or onboarding.
- LTV:CAC below 3x is a red flag. Either your product has a retention problem (fix churn) or your acquisition is too expensive (optimize channels or increase pricing).
- CAC Payback above 18 months means you're funding customer acquisition for too long before profitability. Either raise prices, reduce acquisition cost, or target better-fit customers.
- Track Health Scores weekly on your top 20 customers. Revenue concentration in at-risk accounts is existential.
- The Cohort Retention view is your most powerful fundraising asset. Improving cohorts (newer cohorts retain better than older ones) tells investors your product is getting better.
