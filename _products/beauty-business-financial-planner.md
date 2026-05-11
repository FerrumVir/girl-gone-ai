# Beauty Business Financial Planner — Spreadsheet Template

> This spreadsheet includes 7 sheets for complete financial management of your beauty business. Copy the structure into Google Sheets or Excel.

---

## SHEET 1: PRICING CALCULATOR

**Purpose:** Calculate profitable pricing for every service using real cost data.

### Columns

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | Service Name | Text | Name of the service |
| B | Category | Text | Facial / Lash / Brow / Wax / Peel / Body / Add-On |
| C | Duration (min) | Number | Active service time |
| D | Buffer (min) | Number | Cleanup/prep time between clients |
| E | Total Time Block (min) | Formula | `=C2+D2` |
| F | Product Cost | Currency | Products/supplies used per service |
| G | Disposables Cost | Currency | Gloves, cotton, sheets, etc. per service |
| H | Total COGS | Formula | `=F2+G2` |
| I | Desired Hourly Rate | Currency | What you want to earn per hour worked |
| J | Labor Cost | Formula | `=I2*(E2/60)` |
| K | Overhead Per Hour | Currency | Rent + utilities + insurance / monthly hours worked |
| L | Overhead Allocation | Formula | `=K2*(E2/60)` |
| M | Total Cost | Formula | `=H2+J2+L2` |
| N | Profit Margin Target | Percentage | Desired profit margin (20-40%) |
| O | Minimum Price | Formula | `=M2/(1-N2)` |
| P | Current Price | Currency | What you currently charge |
| Q | Actual Margin | Formula | `=(P2-M2)/P2` |
| R | Price Adjustment Needed | Formula | `=IF(P2<O2, O2-P2, 0)` |
| S | Revenue Per Hour | Formula | `=P2/(E2/60)` |

### Overhead Calculator (Side Panel)

| Item | Monthly Cost |
|------|-------------|
| Rent/Booth Rent | $ |
| Utilities | $ |
| Insurance (liability) | $ |
| Software/Subscriptions | $ |
| Marketing/Ads | $ |
| Education/Training | $ |
| Equipment Depreciation | $ |
| Supplies (non-service) | $ |
| Phone/Internet | $ |
| Licensing/Dues | $ |
| **Total Monthly Overhead** | `=SUM` |
| Hours Worked Per Month | Number |
| **Overhead Per Hour** | `=Total/Hours` |

### Example Data Row

| Service | Cat | Dur | Buf | Block | Prod$ | Disp$ | COGS | Rate | Labor | OH/hr | OH Alloc | Total$ | Margin% | Min Price | Current | Actual% | Adj | Rev/Hr |
|---------|-----|-----|-----|-------|-------|-------|------|------|-------|-------|----------|--------|---------|-----------|---------|---------|-----|--------|
| Classic Facial | Facial | 60 | 15 | 75 | $12 | $3 | $15 | $75 | $93.75 | $18.50 | $23.13 | $131.88 | 25% | $175.83 | $150 | 12% | $25.83 | $120 |
| Hydrafacial | Facial | 75 | 15 | 90 | $35 | $5 | $40 | $75 | $112.50 | $18.50 | $27.75 | $180.25 | 25% | $240.33 | $250 | 28% | $0 | $166.67 |
| Lash Full Set | Lash | 120 | 15 | 135 | $18 | $4 | $22 | $75 | $168.75 | $18.50 | $41.63 | $232.38 | 25% | $309.83 | $280 | 17% | $29.83 | $124.44 |
| Brow Lamination | Brow | 45 | 10 | 55 | $8 | $2 | $10 | $75 | $68.75 | $18.50 | $16.96 | $95.71 | 25% | $127.61 | $120 | 20% | $7.61 | $130.91 |

---

## SHEET 2: MONTHLY PROFIT & LOSS (P&L)

### Revenue Section

| Row | Category | Jan | Feb | Mar | Apr | ... | Dec | YTD Total |
|-----|----------|-----|-----|-----|-----|-----|-----|-----------|
| 1 | Service Revenue | | | | | | | `=SUM(B1:M1)` |
| 2 | Add-On Revenue | | | | | | | `=SUM(B2:M2)` |
| 3 | Retail Product Sales | | | | | | | `=SUM(B3:M3)` |
| 4 | Tips | | | | | | | `=SUM(B4:M4)` |
| 5 | Gift Card Sales | | | | | | | `=SUM(B5:M5)` |
| 6 | Other Income | | | | | | | `=SUM(B6:M6)` |
| 7 | **TOTAL REVENUE** | `=SUM(B1:B6)` | | | | | | |

### Cost of Goods Sold (COGS)

| Row | Category | Jan | Feb | ... | Dec | YTD Total |
|-----|----------|-----|-----|-----|-----|-----------|
| 8 | Service Products/Supplies | | | | | |
| 9 | Retail Products (wholesale) | | | | | |
| 10 | Disposables | | | | | |
| 11 | **TOTAL COGS** | `=SUM(B8:B10)` | | | | |
| 12 | **GROSS PROFIT** | `=B7-B11` | | | | |
| 13 | **Gross Margin %** | `=B12/B7` | | | | |

### Operating Expenses

| Row | Category | Jan | Feb | ... | Dec | YTD Total |
|-----|----------|-----|-----|-----|-----|-----------|
| 14 | Rent / Booth Rent | | | | | |
| 15 | Utilities | | | | | |
| 16 | Insurance | | | | | |
| 17 | Marketing & Advertising | | | | | |
| 18 | Software & Subscriptions | | | | | |
| 19 | Education & Training | | | | | |
| 20 | Equipment & Tools | | | | | |
| 21 | Phone & Internet | | | | | |
| 22 | Travel (work-related) | | | | | |
| 23 | Professional Services (CPA, legal) | | | | | |
| 24 | Licensing & Permits | | | | | |
| 25 | Laundry & Cleaning | | | | | |
| 26 | Office Supplies | | | | | |
| 27 | Miscellaneous | | | | | |
| 28 | **TOTAL EXPENSES** | `=SUM(B14:B27)` | | | | |

### Bottom Line

| Row | Category | Jan | Feb | ... | Dec | YTD Total |
|-----|----------|-----|-----|-----|-----|-----------|
| 29 | **NET PROFIT (before tax)** | `=B12-B28` | | | | |
| 30 | **Net Margin %** | `=B29/B7` | | | | |
| 31 | Owner's Pay | | | | | |
| 32 | Tax Set-Aside (25-30%) | `=B29*0.30` | | | | |
| 33 | **Retained Profit** | `=B29-B31-B32` | | | | |

---

## SHEET 3: EXPENSE TRACKER

**Purpose:** Log every business expense for accurate P&L and tax deductions.

### Columns

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | Date | Date | When the expense occurred |
| B | Vendor/Payee | Text | Where you spent (Amazon, Ulta Pro, landlord, etc.) |
| C | Description | Text | What you bought |
| D | Category | Dropdown | Matches P&L categories above |
| E | Amount | Currency | Total spent |
| F | Payment Method | Dropdown | Business Card / Debit / Cash / Venmo / Transfer |
| G | Receipt | Checkbox | Do you have the receipt saved? |
| H | Tax Deductible | Checkbox | Is this a business write-off? |
| I | Notes | Text | Additional details |
| J | Month | Formula | `=TEXT(A2,"MMMM")` |
| K | Quarter | Formula | `="Q"&ROUNDUP(MONTH(A2)/3,0)` |

### Category Dropdown Options
- Rent/Booth Rent
- Utilities
- Insurance
- Products & Supplies
- Retail Inventory
- Disposables
- Marketing & Ads
- Software & Subscriptions
- Education & Training
- Equipment & Tools
- Phone & Internet
- Travel
- Professional Services
- Licensing & Permits
- Laundry & Cleaning
- Office Supplies
- Meals (business)
- Miscellaneous

### Summary Pivot (Auto-Calculated)

| Category | Jan | Feb | Mar | ... | YTD |
|----------|-----|-----|-----|-----|-----|
| (Each category) | `=SUMIFS(Amount, Category, [cat], Month, "January")` | | | | |
| **TOTAL** | | | | | |

---

## SHEET 4: DAILY REVENUE LOG

**Purpose:** Quick daily entry for income tracking that feeds the monthly P&L.

### Columns

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | Date | Date | Service date |
| B | Client | Text | Client name |
| C | Service(s) | Text | What services were performed |
| D | Service Revenue | Currency | Service price collected |
| E | Add-Ons | Currency | Add-on service revenue |
| F | Retail Sales | Currency | Products sold |
| G | Tips | Currency | Tips received |
| H | Discount Given | Currency | Any discounts applied |
| I | Total Collected | Formula | `=D2+E2+F2+G2-H2` |
| J | Payment Method | Dropdown | Cash / Card / Venmo / Zelle / CashApp / Gift Card |
| K | Notes | Text | Cancellations, no-shows, etc. |

### Daily Summary Row (Bottom of each day)

```
Daily Total: =SUMIF(Date, [today], Total Collected)
Services Today: =COUNTIF(Date, [today])
Avg Ticket: =Daily Total / Services Today
```

### Weekly Summary

| Metric | Formula |
|--------|---------|
| Weekly Revenue | `=SUMIFS(Total Collected, Date, ">="&weekstart, Date, "<="&weekend)` |
| Weekly Services | `=COUNTIFS(Date, ">="&weekstart, Date, "<="&weekend)` |
| Avg Daily Revenue | `=Weekly Revenue / days worked` |
| Best Day | `=MAX of daily totals` |
| Tips Total | `=SUMIFS(Tips, Date range)` |

---

## SHEET 5: TAX PREPARATION

**Purpose:** Quarterly estimated tax calculations and year-end summary for your CPA.

### Quarterly Estimated Taxes

| Quarter | Gross Revenue | Total Expenses | Net Profit | Tax Rate | Estimated Tax Due | Due Date |
|---------|--------------|----------------|------------|----------|-------------------|----------|
| Q1 (Jan-Mar) | `=SUM from P&L` | `=SUM from P&L` | `=Revenue-Expenses` | 25-30% | `=Net*Rate` | Apr 15 |
| Q2 (Apr-Jun) | | | | | | Jun 15 |
| Q3 (Jul-Sep) | | | | | | Sep 15 |
| Q4 (Oct-Dec) | | | | | | Jan 15 (next year) |

### Tax Deduction Categories (Year-End Summary)

| Category | Annual Total | Notes |
|----------|-------------|-------|
| Rent (Schedule C, Line 20b) | `=SUM from expense tracker` | OR home office deduction |
| Supplies (Line 22) | | Products, disposables |
| Insurance (Line 15) | | Liability, health (if self-employed) |
| Utilities (Line 25) | | If you pay separately from rent |
| Advertising (Line 8) | | Social media ads, printing, website |
| Education (Line 27a) | | Courses, certifications, conferences |
| Professional Services (Line 17) | | CPA, legal, bookkeeper |
| Vehicle/Travel (Line 24a) | | Mileage or actual expenses |
| Software (Line 27a) | | Booking software, Canva, etc. |
| Equipment (depreciation) | | Large purchases over $2,500 |
| Licensing (Line 23) | | State license, permits |
| Phone/Internet (Line 25) | | Business % of personal phone |
| **TOTAL DEDUCTIONS** | | |

### Mileage Tracker (Sub-Section)

| Date | Purpose | From/To | Miles | Rate | Deduction |
|------|---------|---------|-------|------|-----------|
| | | | | $0.70/mi (2026 rate) | `=Miles*Rate` |

### Home Office Deduction (if applicable)

| Item | Value |
|------|-------|
| Total Home Square Footage | |
| Office Square Footage | |
| Percentage | `=Office/Total` |
| Annual Rent/Mortgage | |
| Annual Utilities | |
| Annual Internet | |
| Home Office Deduction | `=Percentage * (Rent+Utilities+Internet)` |

---

## SHEET 6: FINANCIAL GOALS & KPIs

**Purpose:** Monthly goal tracking and key performance indicators.

### Monthly KPIs

| Metric | Target | Jan | Feb | Mar | ... | Dec |
|--------|--------|-----|-----|-----|-----|-----|
| Gross Revenue | $6,000 | | | | | |
| Net Profit | $3,500 | | | | | |
| Total Appointments | 80 | | | | | |
| Average Ticket | $85 | | | | | |
| Retail Sales | $500 | | | | | |
| New Clients | 8 | | | | | |
| Rebook Rate | 75% | | | | | |
| No-Show Rate | <5% | | | | | |
| Revenue Per Hour | $100 | | | | | |
| Product Cost % | <15% | | | | | |

### Annual Goals

| Goal | Target | Current | Progress | Deadline |
|------|--------|---------|----------|----------|
| Annual Revenue | $72,000 | | `=Current/Target` | Dec 31 |
| Save for equipment upgrade | $3,000 | | | Aug 31 |
| Build 3-month emergency fund | $10,500 | | | Jun 30 |
| Raise prices by 15% | All services | | | Mar 1 |
| Hit $100 avg ticket | $100 | | | Sep 30 |

### Break-Even Calculator

| Item | Value | Formula |
|------|-------|---------|
| Monthly Fixed Costs | $2,800 | Sum of rent, insurance, subscriptions, etc. |
| Average Service Price | $125 | From pricing calculator |
| Average COGS per Service | $15 | From pricing calculator |
| Contribution Margin | $110 | `=Price - COGS` |
| Break-Even Services/Month | 26 | `=Fixed Costs / Contribution Margin` |
| Break-Even Revenue | $3,182 | `=Break-Even Services * Avg Price` |
| Break-Even Days (at 4 clients/day) | 6.4 days | `=Break-Even Services / 4` |

---

## SHEET 7: PRODUCT INVENTORY & COST TRACKER

**Purpose:** Track professional and retail product inventory, costs, and reorder points.

### Columns

| Column | Header | Format | Description |
|--------|--------|--------|-------------|
| A | Product Name | Text | Full product name |
| B | Brand | Text | Manufacturer/brand |
| C | Type | Dropdown | Professional (back bar) / Retail (for sale) / Disposable |
| D | Size | Text | oz, ml, count, etc. |
| E | Wholesale Cost | Currency | What you pay |
| F | Retail Price | Currency | What you sell for (retail items only) |
| G | Markup % | Formula | `=IF(F2>0, (F2-E2)/E2*100, "N/A")` |
| H | Uses Per Unit | Number | How many services you get from one unit |
| I | Cost Per Use | Formula | `=E2/H2` |
| J | Current Stock | Number | Units on hand |
| K | Reorder Point | Number | Minimum before reordering |
| L | Needs Reorder | Formula | `=IF(J2<=K2, "REORDER", "OK")` |
| M | Supplier | Text | Where to reorder |
| N | Last Ordered | Date | When you last purchased |
| O | Monthly Usage | Number | Average units used per month |
| P | Monthly Cost | Formula | `=O2*E2` |

### Inventory Summary

| Category | Total Products | Monthly Spend | Annual Spend |
|----------|---------------|---------------|--------------|
| Professional/Back Bar | `=COUNTIF(Type,"Professional")` | `=SUMIF` | `=Monthly*12` |
| Retail | `=COUNTIF(Type,"Retail")` | | |
| Disposables | `=COUNTIF(Type,"Disposable")` | | |
| **TOTAL** | | | |

---

## QUICK-START GUIDE

### Step 1: Calculate Your Overhead
Fill in the Overhead Calculator on Sheet 1 with your actual monthly costs. This gives you your true cost per hour which is essential for pricing.

### Step 2: Price Your Services
Enter every service in the Pricing Calculator. Be honest about product costs and time. If your Current Price is below the Minimum Price, you need a price increase.

### Step 3: Start Logging Daily
Beginning today, enter every transaction in the Daily Revenue Log. This takes 2 minutes at the end of each day and gives you accurate monthly data.

### Step 4: Track Expenses Weekly
Save all receipts (photo them immediately). Enter expenses weekly into the Expense Tracker. Categorize correctly for tax time.

### Step 5: Review Monthly
At the end of each month, complete the P&L using data from your Daily Revenue Log and Expense Tracker. Compare to your KPI targets.

### Step 6: Pay Quarterly Taxes
Use the Tax Preparation sheet to calculate estimated quarterly payments. Set aside 25-30% of net profit automatically.
