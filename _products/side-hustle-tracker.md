# Side Hustle Income & Expense Tracker — Google Sheets Template

> Track every dollar across all your side hustles. See which hustles actually make money, which ones drain your time, and stay ahead of quarterly taxes -- all in one spreadsheet.

---

> **SETUP GUIDE -- Get Running in 15 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 5 tabs/sheets and name them: Income Log, Expense Log, Profit by Hustle, Monthly & Quarterly Summary, Tax Estimates
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Set up dropdown lists using the values provided in each section
> 6. Start logging income and expenses immediately
>
> **Tip:** Set a weekly 10-minute reminder (Sunday evening or Monday morning) to log everything from the past week. Consistency beats perfection.

---

---

# SHEET 1: INCOME LOG

> Every dollar you earn from every hustle. Log each payment as it hits your account -- not when you do the work.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Date** | **Hustle Name** | **Client / Source** | **Description** | **Gross Amount** | **Platform Fee** | **Net Amount** | **Payment Method** | **Payment Status** | **Notes** |

---

## Hustle Name (Dropdown)

- Freelance Design
- Etsy Shop
- Rideshare
- Tutoring
- Hustle 5

> Replace these with your actual hustle names. Use Find & Replace (Ctrl+H) to rename across the entire workbook at once.

## Payment Method (Dropdown)

- Credit Card
- Debit Card
- Cash
- Bank Transfer
- Direct Deposit
- PayPal
- Venmo
- Etsy Payments
- Fiverr
- Upwork
- Stripe
- Auto-Pay
- Other

## Payment Status (Dropdown)

- Received
- Pending
- Invoiced
- Overdue
- Partial

---

## Formulas

| Column | Formula | Description |
|--------|---------|-------------|
| G (Net Amount) | `FORMULA: =E2-F2` | Gross minus platform fee |

> Drag the Net Amount formula down as you add rows.

---

## Sample Entries

| Date | Hustle Name | Client / Source | Description | Gross Amount | Platform Fee | Net Amount | Payment Method | Payment Status | Notes |
|------|-------------|-----------------|-------------|-------------:|-------------:|-----------:|----------------|----------------|-------|
| 2026-01-05 | Freelance Design | Acme Corp | Logo redesign package | $850.00 | $0.00 | $850.00 | Bank Transfer | Received | Referred by Sarah |
| 2026-01-08 | Etsy Shop | Etsy Customer | Custom sticker bundle x3 | $47.85 | $10.05 | $37.80 | Etsy Payments | Received | Best seller this month |
| 2026-01-10 | Rideshare | Uber | Week 1 earnings | $312.40 | $78.10 | $234.30 | Direct Deposit | Received | 14 hours driving |
| 2026-01-12 | Tutoring | Marcus L. | SAT prep 2 sessions | $160.00 | $0.00 | $160.00 | Venmo | Received | |
| 2026-01-15 | Freelance Design | BrightPath Inc | Social media template set | $400.00 | $80.00 | $320.00 | Fiverr | Received | Level 2 seller fee |
| 2026-01-17 | Rideshare | Uber | Week 2 earnings | $287.60 | $71.90 | $215.70 | Direct Deposit | Received | 12.5 hours driving |
| 2026-01-20 | Etsy Shop | Etsy Customer | Planner insert digital download | $12.95 | $3.37 | $9.58 | Etsy Payments | Received | |
| 2026-01-22 | Hustle 5 | Local Market | Handmade candle batch | $95.00 | $0.00 | $95.00 | Cash | Received | Farmers market booth |
| 2026-01-25 | Tutoring | Emily R. | College essay review | $80.00 | $0.00 | $80.00 | PayPal | Pending | First session free promo |
| 2026-01-28 | Freelance Design | Oakwood LLC | Website banner ads x4 | $600.00 | $120.00 | $480.00 | Upwork | Invoiced | Due Feb 5 |

---

## Monthly Income Summary (Place below data entries)

| Month | Freelance Design | Etsy Shop | Rideshare | Tutoring | Hustle 5 | **Total Gross** | **Total Fees** | **Total Net** |
|-------|----------------:|-----------:|----------:|---------:|---------:|----------------:|---------------:|--------------:|
| January | | | | | | | | |
| February | | | | | | | | |
| March | | | | | | | | |
| April | | | | | | | | |
| May | | | | | | | | |
| June | | | | | | | | |
| July | | | | | | | | |
| August | | | | | | | | |
| September | | | | | | | | |
| October | | | | | | | | |
| November | | | | | | | | |
| December | | | | | | | | |
| **ANNUAL TOTAL** | | | | | | | | |

### Monthly Summary Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| B (Freelance Design) | `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)=ROW()-[header_offset])*('Income Log'!B:B="Freelance Design")*('Income Log'!E:E))` | Total gross for that hustle in that month |
| H (Total Gross) | `FORMULA: =SUM(B2:F2)` | Sum across all hustles for the month |
| I (Total Fees) | `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)=ROW()-[header_offset])*('Income Log'!F:F))` | Total platform fees for the month |
| J (Total Net) | `FORMULA: =H2-I2` | Gross minus fees |

---

---

# SHEET 2: EXPENSE LOG

> Every business expense for every hustle. One row per transaction. If it helps you make money, it belongs here.

---

## Column Headers

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Date** | **Hustle Name** | **Expense Category** | **Description** | **Amount** | **Payment Method** | **Receipt Saved** | **Notes** |

---

## Expense Category (Dropdown)

- Supplies & Materials
- Software & Tools
- Marketing & Advertising
- Equipment & Gear
- Vehicle / Gas / Mileage
- Education & Courses
- Professional Services
- Shipping & Packaging
- Subscriptions
- Home Office
- Travel
- Insurance
- Phone / Internet (business %)
- Meals (business-related)
- Miscellaneous

## Receipt Saved (Dropdown)

- Yes
- No
- Digital
- N/A

---

## Sample Entries

| Date | Hustle Name | Expense Category | Description | Amount | Payment Method | Receipt Saved | Notes |
|------|-------------|------------------|-------------|-------:|----------------|---------------|-------|
| 2026-01-03 | Freelance Design | Software & Tools | Adobe Creative Cloud monthly | $54.99 | Credit Card | Digital | Annual plan |
| 2026-01-05 | Etsy Shop | Supplies & Materials | Sticker paper 500 sheets | $34.50 | Debit Card | Yes | Bulk order from Amazon |
| 2026-01-05 | Etsy Shop | Shipping & Packaging | Mailer envelopes x200 | $18.99 | Debit Card | Yes | |
| 2026-01-07 | Rideshare | Vehicle / Gas / Mileage | Gas fill-up | $52.30 | Credit Card | Yes | 87 miles this week |
| 2026-01-08 | Freelance Design | Marketing & Advertising | Fiverr promoted gigs | $25.00 | Fiverr | Digital | |
| 2026-01-10 | Tutoring | Education & Courses | SAT prep materials updated edition | $42.00 | Credit Card | Digital | Amazon eBook |
| 2026-01-12 | Hustle 5 | Supplies & Materials | Candle wax 10lb block | $28.75 | Cash | Yes | Craft store |
| 2026-01-12 | Hustle 5 | Supplies & Materials | Fragrance oils x6 | $36.00 | Cash | Yes | |
| 2026-01-14 | Rideshare | Vehicle / Gas / Mileage | Gas fill-up | $48.70 | Credit Card | Yes | 92 miles this week |
| 2026-01-15 | All Hustles | Software & Tools | Google Workspace monthly | $7.99 | Credit Card | Digital | Business email |
| 2026-01-15 | All Hustles | Phone / Internet (business %) | Phone bill (40% business) | $28.00 | Auto-Pay | Digital | $70 total, 40% business use |
| 2026-01-20 | Etsy Shop | Marketing & Advertising | Etsy Ads budget January | $30.00 | Etsy Payments | Digital | |
| 2026-01-22 | Hustle 5 | Miscellaneous | Farmers market booth fee | $25.00 | Cash | Yes | Weekly fee |
| 2026-01-25 | Freelance Design | Subscriptions | Canva Pro monthly | $12.99 | Credit Card | Digital | |
| 2026-01-28 | All Hustles | Professional Services | QuickBooks Self-Employed | $15.00 | Credit Card | Digital | Monthly subscription |

---

## Expenses by Category Summary (Place below data entries)

| Category | January | February | March | Q1 Total | April | May | June | Q2 Total | **YTD Total** |
|----------|--------:|--------:|------:|---------:|------:|----:|-----:|---------:|--------------:|
| Supplies & Materials | | | | | | | | | |
| Software & Tools | | | | | | | | | |
| Marketing & Advertising | | | | | | | | | |
| Equipment & Gear | | | | | | | | | |
| Vehicle / Gas / Mileage | | | | | | | | | |
| Education & Courses | | | | | | | | | |
| Professional Services | | | | | | | | | |
| Shipping & Packaging | | | | | | | | | |
| Subscriptions | | | | | | | | | |
| Home Office | | | | | | | | | |
| Travel | | | | | | | | | |
| Insurance | | | | | | | | | |
| Phone / Internet | | | | | | | | | |
| Meals (business) | | | | | | | | | |
| Miscellaneous | | | | | | | | | |
| **TOTAL** | | | | | | | | | |

### Expense Summary Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| B2 (Jan - Supplies) | `FORMULA: =SUMPRODUCT((MONTH('Expense Log'!A:A)=1)*('Expense Log'!C:C="Supplies & Materials")*('Expense Log'!E:E))` | Total for that category in that month |
| E2 (Q1 Total) | `FORMULA: =SUM(B2:D2)` | Sum of Jan + Feb + Mar |
| J2 (YTD Total) | `FORMULA: =SUM(B2,C2,D2,F2,G2,H2)` | Sum of all months to date |

---

## Expenses by Hustle Summary

| Hustle Name | January | February | March | Q1 Total | April | May | June | Q2 Total | **YTD Total** |
|-------------|--------:|--------:|------:|---------:|------:|----:|-----:|---------:|--------------:|
| Freelance Design | | | | | | | | | |
| Etsy Shop | | | | | | | | | |
| Rideshare | | | | | | | | | |
| Tutoring | | | | | | | | | |
| Hustle 5 | | | | | | | | | |
| All Hustles (shared) | | | | | | | | | |
| **TOTAL** | | | | | | | | | |

### Hustle Expense Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| B2 (Jan - Freelance Design) | `FORMULA: =SUMPRODUCT((MONTH('Expense Log'!A:A)=1)*('Expense Log'!B:B="Freelance Design")*('Expense Log'!E:E))` | Total expenses for that hustle in that month |

---

---

# SHEET 3: PROFIT BY HUSTLE

> The truth sheet. See exactly how much each hustle earns after expenses -- and what your real hourly rate is.

---

## Column Headers

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Hustle Name** | **Total Gross Revenue** | **Total Platform Fees** | **Total Net Revenue** | **Total Expenses** | **Net Profit** | **Hours Worked** | **Effective Hourly Rate** |

---

## Formulas

| Column | Formula | Description |
|--------|---------|-------------|
| B (Total Gross Revenue) | `FORMULA: =SUMIF('Income Log'!B:B,A2,'Income Log'!E:E)` | Sum all gross income for this hustle |
| C (Total Platform Fees) | `FORMULA: =SUMIF('Income Log'!B:B,A2,'Income Log'!F:F)` | Sum all platform fees for this hustle |
| D (Total Net Revenue) | `FORMULA: =B2-C2` | Gross minus fees |
| E (Total Expenses) | `FORMULA: =SUMIF('Expense Log'!B:B,A2,'Expense Log'!E:E)` | Sum all expenses for this hustle |
| F (Net Profit) | `FORMULA: =D2-E2` | Net revenue minus expenses |
| G (Hours Worked) | Manual entry | Track your hours weekly |
| H (Effective Hourly Rate) | `FORMULA: =IF(G2>0,F2/G2,0)` | Profit per hour worked |

---

## Data Rows

| Hustle Name | Total Gross Revenue | Total Platform Fees | Total Net Revenue | Total Expenses | Net Profit | Hours Worked | Effective Hourly Rate |
|-------------|--------------------:|--------------------:|------------------:|---------------:|-----------:|-------------:|----------------------:|
| Freelance Design | $1,850.00 | $200.00 | $1,650.00 | $92.98 | $1,557.02 | 28 | $55.61 |
| Etsy Shop | $60.80 | $13.42 | $47.38 | $83.49 | -$36.11 | 8 | -$4.51 |
| Rideshare | $600.00 | $150.00 | $450.00 | $101.00 | $349.00 | 26.5 | $13.17 |
| Tutoring | $240.00 | $0.00 | $240.00 | $42.00 | $198.00 | 6 | $33.00 |
| Hustle 5 | $95.00 | $0.00 | $95.00 | $89.75 | $5.25 | 10 | $0.53 |
| **TOTALS** | **$2,845.80** | **$363.42** | **$2,482.38** | **$409.22** | **$2,073.16** | **78.5** | **$26.41** |

---

## Shared Expenses Allocation

> Expenses tagged "All Hustles" are shared costs. Allocate them proportionally based on revenue or split evenly.

| Allocation Method | Formula | Description |
|-------------------|---------|-------------|
| Revenue-based split | `FORMULA: =('Expense Log Shared Total')*(D2/D7)` | Each hustle pays proportional to its net revenue |
| Even split | `FORMULA: =('Expense Log Shared Total')/5` | Divide equally among all active hustles |

### Shared Expenses This Period

| Category | Monthly Amount | Allocation |
|----------|---------------:|------------|
| Google Workspace | $7.99 | Split by revenue |
| Phone / Internet (business %) | $28.00 | Split by revenue |
| QuickBooks Self-Employed | $15.00 | Split by revenue |
| **Total Shared** | **$50.99** | |

---

## Profitability Analysis

| Metric | Freelance Design | Etsy Shop | Rideshare | Tutoring | Hustle 5 |
|--------|----------------:|-----------:|----------:|---------:|---------:|
| Revenue Share % | | | | | |
| Expense Ratio | | | | | |
| Profit Margin % | | | | | |
| Hourly Rate Rank | | | | | |
| Verdict | | | | | |

### Analysis Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| Revenue Share % | `FORMULA: =D2/D$7` | This hustle's share of total net revenue |
| Expense Ratio | `FORMULA: =E2/D2` | Expenses as % of net revenue |
| Profit Margin % | `FORMULA: =F2/D2` | Profit as % of net revenue |

---

---

# SHEET 4: MONTHLY & QUARTERLY SUMMARY

> The big picture. Track monthly totals and quarterly trends to see if you're growing or stalling.

---

## Monthly Summary

| Month | Gross Income | Platform Fees | Net Income | Total Expenses | **Net Profit** | Hours Worked | Avg Hourly Rate |
|-------|------------:|-------------:|-----------:|---------------:|---------------:|-------------:|----------------:|
| January | | | | | | | |
| February | | | | | | | |
| March | | | | | | | |
| **Q1 Total** | | | | | | | |
| April | | | | | | | |
| May | | | | | | | |
| June | | | | | | | |
| **Q2 Total** | | | | | | | |
| July | | | | | | | |
| August | | | | | | | |
| September | | | | | | | |
| **Q3 Total** | | | | | | | |
| October | | | | | | | |
| November | | | | | | | |
| December | | | | | | | |
| **Q4 Total** | | | | | | | |
| **ANNUAL TOTAL** | | | | | | | |

### Monthly Summary Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| B2 (Jan Gross) | `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)=1)*('Income Log'!E:E))` | Total gross income for the month |
| C2 (Jan Fees) | `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)=1)*('Income Log'!F:F))` | Total platform fees for the month |
| D2 (Jan Net Income) | `FORMULA: =B2-C2` | Gross minus fees |
| E2 (Jan Expenses) | `FORMULA: =SUMPRODUCT((MONTH('Expense Log'!A:A)=1)*('Expense Log'!E:E))` | Total expenses for the month |
| F2 (Jan Net Profit) | `FORMULA: =D2-E2` | Net income minus expenses |
| G2 (Hours) | Manual entry or `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)=1)*('Profit by Hustle'!G:G))` | Total hours across hustles |
| H2 (Avg Hourly) | `FORMULA: =IF(G2>0,F2/G2,0)` | Profit per hour |
| Q1 Total row | `FORMULA: =SUM(B2:B4)` | Sum of Jan + Feb + Mar |

---

## Month-Over-Month Growth

| Month | Net Profit | Change from Previous | % Change | Trend |
|-------|----------:|-----------------:|----------:|-------|
| January | | | | |
| February | | | | |
| March | | | | |
| April | | | | |
| May | | | | |
| June | | | | |
| July | | | | |
| August | | | | |
| September | | | | |
| October | | | | |
| November | | | | |
| December | | | | |

### Growth Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| C3 (Feb change) | `FORMULA: =B3-B2` | This month minus last month |
| D3 (% change) | `FORMULA: =IF(B2>0,(B3-B2)/B2,0)` | Percentage change |
| E (Trend) | `FORMULA: =IF(C3>0,"Up",IF(C3<0,"Down","Flat"))` | Simple trend indicator |

---

## Quarterly Revenue by Hustle

| Quarter | Freelance Design | Etsy Shop | Rideshare | Tutoring | Hustle 5 | **Total** |
|---------|----------------:|-----------:|----------:|---------:|---------:|---------:|
| Q1 (Jan-Mar) | | | | | | |
| Q2 (Apr-Jun) | | | | | | |
| Q3 (Jul-Sep) | | | | | | |
| Q4 (Oct-Dec) | | | | | | |
| **Annual** | | | | | | |

### Quarterly Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| B2 (Q1 Freelance) | `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)>=1)*(MONTH('Income Log'!A:A)<=3)*('Income Log'!B:B="Freelance Design")*('Income Log'!G:G))` | Net revenue for Q1 for that hustle |

---

---

# SHEET 5: TAX ESTIMATES

> Stay ahead of the IRS. Calculate estimated quarterly tax payments so April doesn't hurt.

---

## Tax Rate Configuration

| Setting | Value | Notes |
|---------|------:|-------|
| **Federal Income Tax Rate** | 22% | Your marginal tax bracket (check IRS tax tables) |
| **State Income Tax Rate** | 5% | Your state rate. Enter 0% for: AK, FL, NV, NH, SD, TN, TX, WA, WY |
| **Self-Employment Tax Rate** | 15.3% | Standard SE tax rate (12.4% Social Security + 2.9% Medicare) |
| **SE Tax Deduction Factor** | 50% | You deduct half of SE tax from income (IRS allows this) |
| **Combined Effective Rate** | | `FORMULA: =B1+B2+(B3*B4)` |

> **Important:** These estimates are for quarterly payment planning, not professional tax advice. Consult a tax professional for your specific situation.

---

## Quarterly Tax Estimate Calculator

| Quarter | Months | Gross Income | Deductible Expenses | Net Self-Employment Income | SE Tax | Income Tax (Federal) | Income Tax (State) | **Total Estimated Tax** |
|---------|--------|------------:|-------------------:|---------------------------:|-------:|---------------------:|-------------------:|------------------------:|
| Q1 | Jan-Mar | | | | | | | |
| Q2 | Apr-Jun | | | | | | | |
| Q3 | Jul-Sep | | | | | | | |
| Q4 | Oct-Dec | | | | | | | |
| **Annual** | | | | | | | | |

### Tax Estimate Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| C2 (Q1 Gross) | `FORMULA: =SUMPRODUCT((MONTH('Income Log'!A:A)>=1)*(MONTH('Income Log'!A:A)<=3)*('Income Log'!E:E))` | Total gross income for Q1 |
| D2 (Q1 Expenses) | `FORMULA: =SUMPRODUCT((MONTH('Expense Log'!A:A)>=1)*(MONTH('Expense Log'!A:A)<=3)*('Expense Log'!E:E))` | Total deductible expenses for Q1 |
| E2 (Net SE Income) | `FORMULA: =C2-D2` | Gross minus deductible expenses |
| F2 (SE Tax) | `FORMULA: =E2*0.153` | Self-employment tax (15.3%) |
| G2 (Federal Income Tax) | `FORMULA: =(E2-(F2*0.5))*0.22` | Taxable income x federal rate (after SE deduction) |
| H2 (State Income Tax) | `FORMULA: =(E2-(F2*0.5))*0.05` | Taxable income x state rate |
| I2 (Total Estimated Tax) | `FORMULA: =F2+G2+H2` | Sum of all three taxes |

---

## IRS Quarterly Payment Deadlines

| Quarter | Income Period | Payment Deadline | Form |
|---------|--------------|------------------|------|
| Q1 | Jan 1 - Mar 31 | April 15 | 1040-ES |
| Q2 | Apr 1 - May 31 | June 15 | 1040-ES |
| Q3 | Jun 1 - Aug 31 | September 15 | 1040-ES |
| Q4 | Sep 1 - Dec 31 | January 15 (next year) | 1040-ES |

---

## Payment Tracker

| Quarter | Amount Owed | Amount Paid | Date Paid | Confirmation # | Status | Remaining Balance |
|---------|------------:|------------:|-----------|----------------|--------|------------------:|
| Q1 | | | | | Unpaid | |
| Q2 | | | | | Unpaid | |
| Q3 | | | | | Unpaid | |
| Q4 | | | | | Unpaid | |
| **Annual Total** | | | | | | |

### Payment Tracker Formulas

| Cell | Formula | Description |
|------|---------|-------------|
| B2 (Amount Owed) | `FORMULA: ='Tax Estimate Calculator'!I2` | Pulls from quarterly estimate |
| G2 (Remaining) | `FORMULA: =B2-C2` | Owed minus paid |

### Status (Dropdown)

- Paid
- Unpaid
- Partial
- Overpaid

---

## Deductions Checklist

> Don't leave money on the table. Review this list quarterly and make sure you're tracking every deduction you're entitled to.

| Deduction | Tracking? | Est. Annual Value | Notes |
|-----------|-----------|------------------:|-------|
| Home office (dedicated space) | Yes / No / N/A | | Simplified: $5/sq ft up to 300 sq ft |
| Internet (business %) | Yes / No / N/A | | Track % of time used for business |
| Phone (business %) | Yes / No / N/A | | Same as internet |
| Vehicle mileage (IRS rate) | Yes / No / N/A | | 2026 rate: check IRS.gov annually |
| Software subscriptions | Yes / No / N/A | | Adobe, Canva, domain hosting, etc. |
| Equipment under $2,500 | Yes / No / N/A | | Section 179 immediate deduction |
| Equipment over $2,500 | Yes / No / N/A | | Depreciate over useful life |
| Professional development | Yes / No / N/A | | Courses, books, certifications |
| Business insurance | Yes / No / N/A | | Liability, E&O, professional |
| Health insurance (self-employed) | Yes / No / N/A | | Deducted on Form 1040, not Schedule C |
| Retirement contributions | Yes / No / N/A | | SEP-IRA or Solo 401(k) |
| Business meals (50%) | Yes / No / N/A | | Must have documented business purpose |
| Shipping & packaging | Yes / No / N/A | | Materials, postage, labels |
| Marketing & advertising | Yes / No / N/A | | Paid ads, promoted listings, business cards |
| Professional services | Yes / No / N/A | | Accountant, lawyer, bookkeeper |
| Bank & platform fees | Yes / No / N/A | | Stripe, PayPal, Etsy, marketplace fees |

---

## Annual Tax Summary

| Line Item | Amount | Notes |
|-----------|-------:|-------|
| Total Gross Income (all hustles) | | `FORMULA: =SUM('Monthly & Quarterly Summary'!B:B)` |
| Total Platform Fees | | `FORMULA: =SUM('Monthly & Quarterly Summary'!C:C)` |
| Total Net Revenue | | `FORMULA: =SUM('Monthly & Quarterly Summary'!D:D)` |
| Total Deductible Expenses | | `FORMULA: =SUM('Monthly & Quarterly Summary'!E:E)` |
| **Net Self-Employment Income** | | `FORMULA: =B3-B4` |
| Self-Employment Tax | | `FORMULA: =B5*0.153` |
| SE Tax Deduction (50%) | | `FORMULA: =B6*0.5` |
| Adjusted Gross SE Income | | `FORMULA: =B5-B7` |
| Federal Income Tax Estimate | | `FORMULA: =B8*[your bracket]` |
| State Income Tax Estimate | | `FORMULA: =B8*[your state rate]` |
| **Total Estimated Tax Liability** | | `FORMULA: =B6+B9+B10` |
| Total Quarterly Payments Made | | From payment tracker |
| **Remaining Tax Owed / Refund** | | `FORMULA: =B11-B12` |

---

---

# REFERENCE: WORKFLOW & TIPS

---

## Weekly Workflow (5-10 minutes)

- Log all income received this week in the Income Log
- Log all business expenses in the Expense Log
- Update the "Hours Worked" column in Profit by Hustle (manual entry)
- Check the Profit by Hustle sheet to see your current standings

## Monthly Workflow (15-20 minutes)

- Review the Monthly & Quarterly Summary -- are totals populating correctly?
- Review expenses by category -- are you spending more than expected anywhere?
- Check your effective hourly rate per hustle -- is any hustle not worth your time?
- Review the Tax Estimates sheet -- are you on track for quarterly payments?

## Quarterly Workflow (30 minutes)

- Review quarterly profit and tax estimates
- Make estimated tax payment before the IRS deadline
- Log the payment in the Tax Estimates payment tracker
- Evaluate: Which hustles to grow? Which to cut?
- Review the Deductions Checklist -- are you tracking everything?

## Annual Workflow

- Export the full spreadsheet for your tax preparer
- Duplicate the workbook for the new year (File > Make a copy)
- Adjust tax rates if your bracket changed
- Set new income goals per hustle

---

## Pro Tips

**Log income on payday, not when you work.** Track when money actually hits your account -- that's what matters for tax purposes.

**Save receipts digitally.** Take photos of physical receipts and store them in a Google Drive folder organized by month. The "Receipt Saved" column in the Expense Log reminds you to do this.

**Track mileage separately.** If you drive for a hustle (rideshare, deliveries, client visits), keep a mileage log. The IRS mileage rate is often more valuable than actual gas expenses. Use a free mileage app like Stride or MileIQ.

**Separate business and personal.** Consider a separate checking account or credit card for hustle expenses. This makes logging dramatically easier and cleaner at tax time.

**Don't forget platform fees.** The Income Log tracks gross vs. net income specifically because platform fees (Etsy, Fiverr, Upwork, Uber) can eat 10-30% of your gross. Your real income is the net number.

**Review hourly rates honestly.** The Profit by Hustle sheet calculates your effective hourly rate per hustle. If a hustle pays $8/hour after expenses, you need to decide whether the non-financial benefits (flexibility, skill building, growth potential) justify continuing.

**Make a copy before tax season.** Duplicate the entire spreadsheet before making any changes for the new year. Your accountant will want the complete, unmodified record.

---

## Common Questions

**Q: How many hustles can I track?**
A: The template comes with 5 slots. You can add more by copying the structure and extending the SUMIF formulas. Most people track 2-4 hustles.

**Q: Should I track personal expenses here?**
A: No. This tracker is specifically for business income and expenses. Use a personal budget tracker for personal finances.

**Q: What counts as a business expense?**
A: Anything ordinary and necessary for your hustle. The Expense Category list covers the most common deductions. When in doubt, save the receipt and ask your tax preparer.

**Q: Do I need to file quarterly taxes?**
A: If you expect to owe $1,000 or more in taxes from self-employment income for the year, the IRS expects quarterly estimated payments. The Tax Estimates sheet helps you calculate these.

**Q: Can I share this with my accountant?**
A: Yes. Share the Google Sheet directly (Share > add their email) or export to Excel/PDF. The organized structure makes your accountant's job much easier -- which may save you money on preparation fees.

**Q: How do I handle expenses shared across hustles?**
A: Tag them as "All Hustles" in the Hustle Name column. The Profit by Hustle sheet has a shared expense allocation section that splits them proportionally by revenue or evenly.

**Q: What if a hustle is losing money?**
A: The Profit by Hustle sheet makes this immediately visible. A negative Net Profit with a low or negative hourly rate is your signal to either cut expenses, raise prices, or shut down that hustle. Give new hustles 3-6 months of data before deciding.
