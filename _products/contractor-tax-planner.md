# Contractor & Freelancer Tax Planner — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Estimate quarterly taxes, track deductions, log mileage, organize 1099 income, and categorize write-offs all in one place.

---

> **SETUP GUIDE — Get Running in 20 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 8 tabs/sheets and name them: Income Tracker, Expense Tracker, Quarterly Estimates, Deduction Categories, Mileage Log, Home Office, Annual Summary, Dashboard
> 3. Copy each section below into its corresponding sheet
> 4. Enter the formulas as documented (all formulas are marked with `FORMULA:`)
> 5. Start by entering your tax bracket and filing status in Quarterly Estimates
> 6. Log all income and expenses as they occur throughout the year
>
> **Tip:** Set aside 25-30% of every payment you receive into a separate savings account for taxes. This planner helps you calculate the exact amount, but having a tax savings buffer prevents April surprises.

---

---

# SHEET 1: INCOME TRACKER

> Log every payment received from clients. This feeds your quarterly tax calculations.

---

## Column Headers

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Date Received** | **Client/Payer** | **Invoice #** | **Description** | **Gross Amount** | **Platform Fees** | **Net Received** | **1099 Expected?** | **Quarter** |

---

## Sample Entries

| Date | Client | Invoice # | Description | Gross | Fees | Net | 1099? | Quarter |
|------|--------|-----------|-------------|-------|------|-----|-------|---------|
| 2026-01-08 | Acme Corp | INV-101 | Web design retainer - Jan | $3,000.00 | $0 | $3,000.00 | Yes | Q1 |
| 2026-01-15 | Jane Smith | INV-102 | Logo design | $1,200.00 | $0 | $1,200.00 | No (<$600) | Q1 |
| 2026-01-22 | Upwork Client | — | Content writing project | $850.00 | $85.00 | $765.00 | Yes (platform) | Q1 |
| 2026-02-01 | Acme Corp | INV-103 | Web design retainer - Feb | $3,000.00 | $0 | $3,000.00 | Yes | Q1 |

`FORMULA: Net Received = Gross Amount - Platform Fees`
`FORMULA: Quarter = IF(MONTH(A2)<=3,"Q1",IF(MONTH(A2)<=6,"Q2",IF(MONTH(A2)<=9,"Q3","Q4")))`

---

## Income Summary by Quarter

| Quarter | Gross Income | Platform Fees | Net Income | # of Payments | # of 1099 Payers |
|---------|-------------|--------------|-----------|--------------|-----------------|
| Q1 (Jan-Mar) | $ | $ | $ | | |
| Q2 (Apr-Jun) | $ | $ | $ | | |
| Q3 (Jul-Sep) | $ | $ | $ | | |
| Q4 (Oct-Dec) | $ | $ | $ | | |
| **ANNUAL** | **$** | **$** | **$** | | |

`FORMULA: =SUMIFS(E:E, I:I, "Q1")`

---

## 1099 Payer Tracking

| Client/Payer | EIN (if known) | Total Paid to You | 1099 Received? | Amount on 1099 | Matches? |
|-------------|---------------|-------------------|---------------|---------------|---------|
| | | $ | Yes/No | $ | Yes/No |
| | | $ | Yes/No | $ | Yes/No |
| | | $ | Yes/No | $ | Yes/No |

---

---

# SHEET 2: EXPENSE TRACKER

> Every business expense. Categorized for Schedule C filing.

---

## Column Headers

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Date** | **Vendor/Payee** | **Description** | **Amount** | **Schedule C Category** | **Payment Method** | **Receipt Saved?** | **Quarter** | **Notes** |

---

## Schedule C Categories (Dropdown)

| Category | IRS Line | What Counts |
|----------|----------|-------------|
| Advertising & Marketing | Line 8 | Ads, website hosting, business cards, SEO, social media ads |
| Car & Truck (actual method) | Line 9 | Gas, maintenance, insurance, depreciation (business %) |
| Commissions & Fees | Line 10 | Platform fees, referral fees, payment processing |
| Contract Labor | Line 11 | Subcontractors, virtual assistants, freelancers you hire |
| Insurance | Line 15 | Professional liability, business insurance |
| Interest | Line 16 | Business credit card interest, business loan interest |
| Legal & Professional | Line 17 | Accountant, attorney, tax prep, bookkeeper |
| Office Expense | Line 18 | Supplies, postage, printing, desk supplies |
| Rent or Lease | Line 20 | Office rent, coworking space, equipment leases |
| Repairs & Maintenance | Line 21 | Computer repair, equipment maintenance |
| Supplies | Line 22 | Materials consumed by the business |
| Taxes & Licenses | Line 23 | Business licenses, state/local business taxes |
| Travel | Line 24a | Airfare, hotel, rental car, transportation (business) |
| Meals | Line 24b | Business meals with clients/prospects (50% deductible) |
| Utilities | Line 25 | Phone, internet (business portion) |
| Software & Subscriptions | Line 27a | SaaS, apps, digital tools, cloud storage |
| Education & Training | Line 27a | Courses, certifications, conferences, books |
| Equipment (Section 179) | Line 13 | Computer, camera, furniture (may elect to expense) |
| Health Insurance | Line 29* | Self-employed health insurance premiums |
| Retirement Contributions | Sch 1* | SEP-IRA, Solo 401(k) contributions |
| Home Office | Form 8829 | See Home Office sheet |

---

## Sample Entries

| Date | Vendor | Description | Amount | Category | Payment | Receipt? | Quarter | Notes |
|------|--------|-------------|--------|----------|---------|----------|---------|-------|
| 2026-01-03 | Adobe | Creative Cloud | $59.99 | Software & Subscriptions | Credit Card | Yes | Q1 | Monthly |
| 2026-01-05 | WeWork | Coworking - January | $250.00 | Rent or Lease | Bank Transfer | Yes | Q1 | |
| 2026-01-08 | Amazon | External monitor | $329.99 | Equipment (Section 179) | Credit Card | Yes | Q1 | For design work |
| 2026-01-12 | Restaurant | Lunch with client (Acme) | $52.80 | Meals | Credit Card | Yes | Q1 | 50% deductible |

---

## Quarterly Expense Summary

| Category | Q1 | Q2 | Q3 | Q4 | **Annual Total** |
|----------|----|----|----|----|-----------------|
| Advertising & Marketing | $ | $ | $ | $ | $ |
| Car & Truck | $ | $ | $ | $ | $ |
| Commissions & Fees | $ | $ | $ | $ | $ |
| Contract Labor | $ | $ | $ | $ | $ |
| Insurance | $ | $ | $ | $ | $ |
| Legal & Professional | $ | $ | $ | $ | $ |
| Office Expense | $ | $ | $ | $ | $ |
| Rent or Lease | $ | $ | $ | $ | $ |
| Software & Subscriptions | $ | $ | $ | $ | $ |
| Education & Training | $ | $ | $ | $ | $ |
| Travel | $ | $ | $ | $ | $ |
| Meals (100% — deduct 50% on return) | $ | $ | $ | $ | $ |
| Utilities | $ | $ | $ | $ | $ |
| Equipment | $ | $ | $ | $ | $ |
| Other | $ | $ | $ | $ | $ |
| **TOTAL EXPENSES** | **$** | **$** | **$** | **$** | **$** |

`FORMULA: =SUMIFS(D:D, H:H, "Q1", E:E, "Advertising & Marketing")`

---

---

# SHEET 3: QUARTERLY ESTIMATES

> Calculate your estimated quarterly tax payments to avoid underpayment penalties.

---

## Your Tax Profile

| Field | Value | Notes |
|-------|-------|-------|
| Filing Status | Single / MFJ / MFS / HoH | |
| Federal Tax Bracket (est.) | % | Use marginal rate for your income level |
| State Tax Rate | % | Enter 0 if no state income tax |
| Self-Employment Tax Rate | 15.3% | Fixed (12.4% SS + 2.9% Medicare) |
| SE Tax Applies To | 92.35% of net profit | Fixed per IRS |
| Additional Medicare Tax | 0.9% | If income > $200K single / $250K MFJ |

---

## Quarterly Tax Calculation

| Line | Description | Q1 | Q2 | Q3 | Q4 | Annual |
|------|-------------|----|----|----|----|--------|
| 1 | Gross Income | $ | $ | $ | $ | $ |
| 2 | Total Deductible Expenses | $ | $ | $ | $ | $ |
| 3 | **Net Profit (Line 1 - Line 2)** | **$** | **$** | **$** | **$** | **$** |
| 4 | SE Tax Base (Line 3 * 0.9235) | $ | $ | $ | $ | $ |
| 5 | Self-Employment Tax (Line 4 * 0.153) | $ | $ | $ | $ | $ |
| 6 | SE Tax Deduction (Line 5 * 0.5) | $ | $ | $ | $ | $ |
| 7 | Adjusted Income (Line 3 - Line 6) | $ | $ | $ | $ | $ |
| 8 | Federal Income Tax (Line 7 * bracket %) | $ | $ | $ | $ | $ |
| 9 | State Income Tax (Line 7 * state %) | $ | $ | $ | $ | $ |
| 10 | **Total Tax Liability (Lines 5+8+9)** | **$** | **$** | **$** | **$** | **$** |
| 11 | **Quarterly Payment Due** | **$** | **$** | **$** | **$** | |

`FORMULA: Line 3 = Line 1 - Line 2`
`FORMULA: Line 4 = Line 3 * 0.9235`
`FORMULA: Line 5 = Line 4 * 0.153`
`FORMULA: Line 6 = Line 5 * 0.5`
`FORMULA: Line 7 = Line 3 - Line 6`
`FORMULA: Line 8 = Line 7 * Federal_Rate`
`FORMULA: Line 9 = Line 7 * State_Rate`
`FORMULA: Line 10 = Line 5 + Line 8 + Line 9`
`FORMULA: Line 11 = Cumulative Line 10 up to this quarter / quarters elapsed (annualized method)`

---

## Payment Tracking

| Quarter | Period | Due Date | Amount Owed | Amount Paid | Date Paid | Confirmation # | Over/Under |
|---------|--------|----------|-------------|-------------|-----------|----------------|-----------|
| Q1 | Jan 1 - Mar 31 | April 15, 2026 | $ | $ | | | $ |
| Q2 | Apr 1 - Jun 30 | June 16, 2026 | $ | $ | | | $ |
| Q3 | Jul 1 - Sep 30 | Sep 15, 2026 | $ | $ | | | $ |
| Q4 | Oct 1 - Dec 31 | Jan 15, 2027 | $ | $ | | | $ |
| **TOTAL** | | | **$** | **$** | | | **$** |

`FORMULA: Over/Under = Amount Paid - Amount Owed (positive = overpaid)`

---

## Tax Savings Account Target

| Metric | Value |
|--------|-------|
| Estimated Annual Tax | $ |
| Suggested Monthly Set-Aside | $ |
| Suggested % of Each Payment | % |
| Current Tax Savings Balance | $ |
| Next Payment Due | $ on [date] |
| Surplus / Shortfall | $ |

`FORMULA: Monthly Set-Aside = Estimated Annual Tax / 12`
`FORMULA: % of Payment = Estimated Annual Tax / Estimated Annual Income * 100`

---

---

# SHEET 4: DEDUCTION CATEGORIES

> Detailed reference for what qualifies in each category, with limits and rules.

---

## Deduction Quick Reference

| Category | Deduction % | Annual Limit | Documentation Needed | Common Mistakes |
|----------|-------------|-------------|---------------------|-----------------|
| Advertising | 100% | None | Receipts, invoices | Including personal social media costs |
| Car (Standard Mileage) | $0.70/mile* | None | Mileage log required | Not tracking commute vs. business |
| Car (Actual Method) | Business % | None | All receipts + log | Mixing personal/business without log |
| Meals (Business) | 50% | None | Receipt + who/why | Not noting business purpose |
| Travel | 100% | None | Receipts | Mixing personal days into business trip |
| Home Office | Actual or Simplified | $1,500 (simplified) | Measurements, bills | Using shared-use rooms |
| Health Insurance | 100% | Net SE income | Premium statements | Claiming if eligible for employer plan |
| Retirement (SEP-IRA) | 100% | 25% of net or $69K* | Contribution statement | Exceeding limits |
| Equipment (Sec 179) | 100% | $1,220,000* | Receipt, date placed in service | Not electing 179 on return |
| Education | 100% | None | Receipt, relevance | Courses for new career (not deductible) |

*Check current year IRS limits — these change annually.

---

## Often-Overlooked Deductions

| Deduction | Category | Typical Amount | Notes |
|-----------|----------|---------------|-------|
| Internet (business %) | Utilities | $30-80/mo | Based on % of business use |
| Phone (business %) | Utilities | $30-60/mo | Based on % of business use |
| Bank/processing fees | Commissions & Fees | Varies | Stripe, PayPal, Square fees |
| Domain renewals | Advertising | $10-50/yr each | Per business website |
| Professional memberships | Taxes & Licenses | Varies | Industry associations |
| Business use of car insurance | Car & Truck | Business % | If using actual method |
| Continuing education | Education | Varies | Must relate to current business |
| Client gifts | Other | $25 max/person | Per recipient per year |
| Business books/resources | Education | Varies | Must relate to business |
| Coworking day passes | Rent or Lease | $15-40/visit | Keep receipts |

---

---

# SHEET 5: MILEAGE LOG

> IRS requires contemporaneous records. Log every business trip.

---

## Column Headers

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Date** | **Destination** | **Business Purpose** | **Starting Odometer** | **Ending Odometer** | **Total Miles** | **Deduction Amount** | **Round Trip?** | **Notes** |

---

## IRS Standard Mileage Rate

| Year | Rate per Mile |
|------|-------------|
| 2026 | $0.70* |

*Update at start of each year from IRS.gov

---

## Sample Entries

| Date | Destination | Purpose | Start | End | Miles | Deduction | Round Trip | Notes |
|------|-------------|---------|-------|-----|-------|-----------|-----------|-------|
| 2026-01-06 | Client office - Acme Corp | Project meeting | 45,230 | 45,254 | 24 | $16.80 | Yes | Quarterly review |
| 2026-01-10 | Office Depot | Business supplies | 45,254 | 45,261 | 7 | $4.90 | Yes | Printer ink |
| 2026-01-15 | Networking event downtown | Business networking | 45,261 | 45,283 | 22 | $15.40 | Yes | Chamber event |
| 2026-01-20 | Post office | Ship client package | 45,283 | 45,289 | 6 | $4.20 | Yes | |

`FORMULA: Total Miles = Ending - Starting`
`FORMULA: Deduction Amount = Total Miles * IRS Rate`

---

## Quarterly Mileage Summary

| Quarter | Total Trips | Total Miles | Total Deduction |
|---------|------------|-------------|----------------|
| Q1 | | | $ |
| Q2 | | | $ |
| Q3 | | | $ |
| Q4 | | | $ |
| **ANNUAL** | | | **$** |

---

## Standard Mileage vs. Actual Method Comparison

| Method | Annual Amount | Better By |
|--------|-------------|-----------|
| Standard Mileage (miles * rate) | $ | |
| Actual Expenses (gas, insurance, repairs, depreciation * business %) | $ | |
| **Use This Method:** | | $ |

---

---

# SHEET 6: HOME OFFICE

> Calculate your home office deduction using either method.

---

## Method 1: Simplified Method

| Field | Value |
|-------|-------|
| Dedicated Office Square Footage | sq ft |
| Rate | $5 per sq ft |
| Maximum | 300 sq ft ($1,500) |
| **Your Deduction** | **$** |

`FORMULA: Deduction = MIN(Square Footage * 5, 1500)`

---

## Method 2: Actual Expense Method

### Step 1: Calculate Business Percentage

| Field | Value |
|-------|-------|
| Total Home Square Footage | sq ft |
| Dedicated Office Square Footage | sq ft |
| **Business Use Percentage** | **%** |

`FORMULA: Business % = Office Sq Ft / Total Sq Ft * 100`

### Step 2: Calculate Deductible Expenses

| Expense | Annual Amount | Business % | Deductible Amount |
|---------|-------------|-----------|-------------------|
| Rent OR Mortgage Interest | $ | % | $ |
| Property Taxes | $ | % | $ |
| Homeowner's/Renter's Insurance | $ | % | $ |
| Utilities (electric, gas, water) | $ | % | $ |
| Internet | $ | % | $ |
| Repairs (whole home) | $ | % | $ |
| Repairs (office only) | $ | 100% | $ |
| Depreciation (if owned) | $ | % | $ |
| **TOTAL HOME OFFICE DEDUCTION** | | | **$** |

`FORMULA: Deductible Amount = Annual Amount * Business %`

---

### Method Comparison

| | Simplified | Actual |
|--|-----------|--------|
| Deduction Amount | $ | $ |
| Documentation Required | Minimal | Extensive |
| **Recommended Method** | | |

---

## Home Office Qualification Checklist

- [ ] Space is used REGULARLY for business
- [ ] Space is used EXCLUSIVELY for business (no dual-use)
- [ ] Space is your principal place of business OR used to meet clients
- [ ] If employee (W-2), space is for employer's convenience (rare for remote workers to qualify)

---

---

# SHEET 7: ANNUAL SUMMARY

> Year-end tax preparation summary. Print this for your accountant.

---

## Tax Return Data Summary — Tax Year [YEAR]

### Income (Schedule C, Line 1)

| Source | Amount |
|--------|--------|
| Total Gross Receipts | $ |
| Returns/Allowances | ($ ) |
| **Net Gross Income** | **$** |

### Expenses by Schedule C Line

| Line | Category | Amount |
|------|----------|--------|
| 8 | Advertising | $ |
| 9 | Car & Truck Expenses | $ |
| 10 | Commissions and Fees | $ |
| 11 | Contract Labor | $ |
| 13 | Depreciation / Section 179 | $ |
| 15 | Insurance (business) | $ |
| 16a | Mortgage Interest | $ |
| 16b | Other Interest | $ |
| 17 | Legal & Professional | $ |
| 18 | Office Expense | $ |
| 20a | Rent (vehicles/equipment) | $ |
| 20b | Rent (other business property) | $ |
| 21 | Repairs & Maintenance | $ |
| 22 | Supplies | $ |
| 23 | Taxes & Licenses | $ |
| 24a | Travel | $ |
| 24b | Meals (enter 100%, IRS applies 50%) | $ |
| 25 | Utilities | $ |
| 27a | Other Expenses | $ |
| 30 | Home Office Deduction | $ |
| | **TOTAL EXPENSES** | **$** |
| | **NET PROFIT (Income - Expenses)** | **$** |

---

### Other Deductions (Not on Schedule C)

| Deduction | Amount | Where it Goes |
|-----------|--------|---------------|
| Self-Employed Health Insurance | $ | Schedule 1, Line 17 |
| 1/2 Self-Employment Tax | $ | Schedule 1, Line 15 |
| SEP-IRA / Solo 401(k) | $ | Schedule 1, Line 16 |
| **Total Above-the-Line Deductions** | **$** | |

---

### Quarterly Tax Payments Made

| Quarter | Federal (1040-ES) | State | Total |
|---------|-------------------|-------|-------|
| Q1 | $ | $ | $ |
| Q2 | $ | $ | $ |
| Q3 | $ | $ | $ |
| Q4 | $ | $ | $ |
| **TOTAL PAID** | **$** | **$** | **$** |

---

### 1099 Forms Received

| Payer | Amount Reported | Matches Your Records? |
|-------|----------------|----------------------|
| | $ | Yes / No (explain) |
| | $ | Yes / No |
| | $ | Yes / No |
| **TOTAL 1099 INCOME** | **$** | |

---

---

# SHEET 8: DASHBOARD

> Quick-reference tax planning view.

---

## Year-to-Date Summary

| Metric | YTD Amount |
|--------|-----------|
| Gross Income | $ |
| Total Expenses | $ |
| Net Profit | $ |
| Estimated Tax Liability | $ |
| Taxes Paid So Far | $ |
| **Still Owed** | **$** |
| Next Payment Due | [date] |
| Effective Tax Rate | % |

`FORMULA: Effective Rate = Total Tax / Net Profit * 100`

---

## Monthly Income vs. Expenses

| Month | Income | Expenses | Net Profit | Tax Set-Aside (30%) |
|-------|--------|----------|-----------|---------------------|
| Jan | $ | $ | $ | $ |
| Feb | $ | $ | $ | $ |
| Mar | $ | $ | $ | $ |
| Apr | $ | $ | $ | $ |
| May | $ | $ | $ | $ |
| Jun | $ | $ | $ | $ |
| Jul | $ | $ | $ | $ |
| Aug | $ | $ | $ | $ |
| Sep | $ | $ | $ | $ |
| Oct | $ | $ | $ | $ |
| Nov | $ | $ | $ | $ |
| Dec | $ | $ | $ | $ |

---

## Deduction Maximizer

| Deduction Area | Current Claim | Max Possible | Gap | Action |
|---------------|--------------|-------------|-----|--------|
| Home Office | $ | $ | $ | |
| Mileage | $ | $ | $ | Log all trips |
| Retirement | $ | $ | $ | Contribute by Dec 31 |
| Health Insurance | $ | $ | $ | |
| Education | $ | $ | $ | |

---

## Key Dates

| Date | Event | Status |
|------|-------|--------|
| April 15 | Q1 Estimated Tax Due | |
| April 15 | Tax Return Due (or extension) | |
| June 16 | Q2 Estimated Tax Due | |
| September 15 | Q3 Estimated Tax Due | |
| October 15 | Extended Return Due | |
| December 31 | Last Day for Retirement Contributions (most) | |
| January 15 | Q4 Estimated Tax Due | |
| January 31 | 1099s Should Arrive | |

---

---

# FORMULA REFERENCE GUIDE

---

## Self-Employment Tax

```
SE_Tax_Base = Net_Profit * 0.9235
SE_Tax = SE_Tax_Base * 0.153
SE_Deduction = SE_Tax * 0.5
```

## Quarterly Estimate (Annualized Method)

```
Q1_Tax = (Q1_Net_Profit * 4) * Total_Rate / 4
Q2_Tax = ((Q1+Q2_Profit) * 2) * Total_Rate / 4
```

## Mileage Deduction

```
Annual_Mileage_Deduction = Total_Business_Miles * IRS_Rate
```

## Home Office (Actual)

```
Business_Pct = Office_SqFt / Home_SqFt
Deduction = (Rent + Utilities + Insurance + Repairs) * Business_Pct
```

## Effective Tax Rate

```
=Total_Tax_Paid / Net_Profit * 100
```

---

> **DISCLAIMER:** This tax planner is an organizational tool for freelancers and independent contractors. It provides estimates based on simplified calculations and does not account for all tax credits, phaseouts, AMT, or special situations. Tax laws change annually. Always consult a qualified CPA or tax professional for filing. The IRS standard mileage rate, contribution limits, and other thresholds should be verified at IRS.gov for the current tax year.
