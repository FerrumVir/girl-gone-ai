# Small Business Tax Deduction Tracker — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Track every business deduction as it happens, organized by IRS Schedule C categories, so you walk into tax season fully prepared instead of scrambling for receipts.

---

> **SETUP GUIDE — Get Running in 15 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 6 tabs/sheets and name them: Expense Log, Quarterly Summary, Mileage Log, Home Office Calculator, Estimated Tax Payments, Year-End Report
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Start logging expenses immediately — even if you're catching up on past months
> 6. Set a weekly 10-minute appointment to enter receipts (Sunday evening works well)
>
> **Tip:** Take a photo of every receipt with your phone and save to a "Receipts" folder in Google Drive. Reference the filename in the Receipt column for instant audit protection.

---

---

# SHEET 1: EXPENSE LOG

> Every business expense goes here. One row per transaction. This is your audit-ready paper trail.

---

## Column Headers

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Date** | **Vendor/Payee** | **Description** | **Category (Schedule C Line)** | **Amount** | **Payment Method** | **Business Purpose** | **Receipt Reference** | **Notes** |

---

## Category Dropdown (Maps to Schedule C)

| Category | Schedule C Line | Examples |
|----------|:--------------:|---------|
| Advertising & Marketing | 8 | Facebook ads, business cards, website hosting |
| Car & Truck Expenses | 9 | Gas, maintenance (if using actual method) |
| Commissions & Fees | 10 | Platform fees, referral payments |
| Contract Labor | 11 | Subcontractors, freelancers hired |
| Depreciation | 13 | Equipment, computers (over $2,500) |
| Insurance (Business) | 15 | Liability, E&O, professional insurance |
| Interest (Business Loans) | 16a | Business credit card interest, SBA loan |
| Legal & Professional Services | 17 | Attorney, CPA, bookkeeper |
| Office Expense | 18 | Printer ink, paper, desk supplies |
| Rent or Lease (Business) | 20b | Coworking space, equipment lease |
| Repairs & Maintenance | 21 | Equipment repair, software fixes |
| Supplies | 22 | Materials used for client work |
| Taxes & Licenses | 23 | Business license, state registration |
| Travel | 24a | Flights, hotels, conference travel |
| Meals (Business) | 24b | Client meals, conference meals (50% deductible) |
| Utilities | 25 | Business phone, internet (business %) |
| Education & Training | Other | Courses, books, certifications |
| Software & Subscriptions | Other | SaaS tools, design software, cloud storage |
| Health Insurance | Other | Self-employed health insurance (Form 1040) |
| Retirement Contributions | Other | SEP-IRA, Solo 401(k) |
| Bank & Merchant Fees | Other | Stripe fees, PayPal fees, wire transfers |
| Postage & Shipping | Other | Client deliveries, USPS, FedEx |

---

## Payment Method (Dropdown)
- Business Credit Card
- Business Debit Card
- Business Checking
- Personal Card (reimburse)
- Cash
- PayPal/Venmo
- ACH/Wire

---

## Sample Entries

| Date | Vendor | Description | Category | Amount | Method | Purpose | Receipt | Notes |
|------|--------|-------------|----------|-------:|--------|---------|---------|-------|
| 2026-01-03 | Adobe | Creative Cloud monthly | Software & Subscriptions | $54.99 | Business CC | Design tool for client projects | adobe-jan-2026.pdf | |
| 2026-01-05 | WeWork | January coworking | Rent or Lease | $350.00 | ACH | Dedicated workspace | wework-inv-jan.pdf | |
| 2026-01-08 | Staples | Printer ink + paper | Office Expense | $67.43 | Business Debit | Print client contracts | staples-010826.jpg | |
| 2026-01-12 | Delta Airlines | Flight to client meeting | Travel | $289.00 | Business CC | Client kickoff in Austin | delta-conf.pdf | |
| 2026-01-12 | Marriott | 2-night hotel for meeting | Travel | $342.00 | Business CC | Client kickoff | marriott-010826.pdf | |
| 2026-01-15 | Upwork | Platform fee on payment | Commissions & Fees | $45.20 | Deducted from payout | Client delivery fee | upwork-inv.pdf | |

---

---

# SHEET 2: QUARTERLY SUMMARY

> Totals by category for each quarter. Matches directly to Schedule C lines.

---

## Quarterly Expense Totals

| Category (Schedule C Line) | Q1 (Jan-Mar) | Q2 (Apr-Jun) | Q3 (Jul-Sep) | Q4 (Oct-Dec) | **Annual Total** |
|---------------------------|-------------:|-------------:|-------------:|-------------:|-----------------:|
| Advertising (Line 8) | $ | $ | $ | $ | $ |
| Car & Truck (Line 9) | $ | $ | $ | $ | $ |
| Commissions (Line 10) | $ | $ | $ | $ | $ |
| Contract Labor (Line 11) | $ | $ | $ | $ | $ |
| Depreciation (Line 13) | $ | $ | $ | $ | $ |
| Insurance (Line 15) | $ | $ | $ | $ | $ |
| Interest (Line 16a) | $ | $ | $ | $ | $ |
| Legal/Professional (Line 17) | $ | $ | $ | $ | $ |
| Office Expense (Line 18) | $ | $ | $ | $ | $ |
| Rent/Lease (Line 20b) | $ | $ | $ | $ | $ |
| Repairs (Line 21) | $ | $ | $ | $ | $ |
| Supplies (Line 22) | $ | $ | $ | $ | $ |
| Taxes & Licenses (Line 23) | $ | $ | $ | $ | $ |
| Travel (Line 24a) | $ | $ | $ | $ | $ |
| Meals — 50% (Line 24b) | $ | $ | $ | $ | $ |
| Utilities (Line 25) | $ | $ | $ | $ | $ |
| Other Expenses (Line 27) | $ | $ | $ | $ | $ |
| **TOTAL DEDUCTIONS** | **$** | **$** | **$** | **$** | **$** |

`FORMULA (Q1 Advertising): =SUMIFS(ExpenseLog!E:E, ExpenseLog!D:D, "Advertising*", ExpenseLog!A:A, ">="&DATE(2026,1,1), ExpenseLog!A:A, "<="&DATE(2026,3,31))`

`FORMULA (Annual Total): =SUM(Q1:Q4) for each row`

---

## Income Summary (for tax calculation)

| Quarter | Gross Revenue | Expenses | Net Profit | Effective Tax Rate | Estimated Tax Due |
|---------|-------------:|---------:|-----------:|-------------------:|-----------------:|
| Q1 | $ | $ | $ | % | $ |
| Q2 | $ | $ | $ | % | $ |
| Q3 | $ | $ | $ | % | $ |
| Q4 | $ | $ | $ | % | $ |
| **ANNUAL** | **$** | **$** | **$** | | **$** |

`FORMULA (Net Profit): =GrossRevenue - Expenses`
`FORMULA (Estimated Tax): =NetProfit * EffectiveTaxRate`

---

---

# SHEET 3: MILEAGE LOG

> Track every business mile driven. The IRS standard mileage rate for 2026 is $0.67/mile (check IRS.gov annually for current rate).

---

## IRS Mileage Rate Settings

| Setting | Value |
|---------|-------|
| Current Year IRS Rate | $0.67/mile |
| Method Used | [ ] Standard Mileage [ ] Actual Expenses |

---

## Mileage Log

| Date | Destination | Business Purpose | Starting Odometer | Ending Odometer | Total Miles | Deduction Amount |
|------|-------------|-----------------|:-----------------:|:---------------:|:-----------:|:----------------:|
| | | | | | | $ |
| | | | | | | $ |
| | | | | | | $ |
| | | | | | | $ |
| | | | | | | $ |

`FORMULA (Total Miles): =EndingOdometer - StartingOdometer`
`FORMULA (Deduction Amount): =TotalMiles * IRSRate`

---

## Sample Mileage Entries

| Date | Destination | Purpose | Start | End | Miles | Deduction |
|------|-------------|---------|:-----:|:---:|:-----:|:---------:|
| 2026-01-08 | Client office, 123 Main St | Project kickoff meeting | 45,231 | 45,256 | 25 | $16.75 |
| 2026-01-15 | Office Depot | Purchase supplies for client | 45,302 | 45,310 | 8 | $5.36 |
| 2026-01-22 | Networking event, Hilton | Industry networking | 45,410 | 45,438 | 28 | $18.76 |
| 2026-02-03 | Post office | Ship client deliverables | 45,512 | 45,516 | 4 | $2.68 |

---

## Monthly & Annual Mileage Summary

| Month | Total Business Miles | Deduction Amount |
|-------|:--------------------:|-----------------:|
| January | | $ |
| February | | $ |
| March | | $ |
| April | | $ |
| May | | $ |
| June | | $ |
| July | | $ |
| August | | $ |
| September | | $ |
| October | | $ |
| November | | $ |
| December | | $ |
| **ANNUAL TOTAL** | | **$** |

`FORMULA (Monthly Total): =SUMIFS(Miles, Month(Date), MonthNumber)`
`FORMULA (Monthly Deduction): =MonthlyMiles * IRSRate`

---

## Mileage vs. Actual Expenses Comparison

| Method | Annual Amount | Notes |
|--------|:------------:|-------|
| Standard Mileage (miles * rate) | $ | Simpler, usually better for older cars |
| Actual Expenses (gas + insurance + depreciation + maintenance) | $ | Better for expensive/new vehicles |
| **Use Whichever Is Higher** | **$** | |

---

---

# SHEET 4: HOME OFFICE CALCULATOR

> Calculate your home office deduction using both IRS methods. Use whichever gives the larger deduction.

---

## Method 1: Simplified Method

| Input | Value |
|-------|------:|
| Home Office Square Footage (max 300 sq ft) | sq ft |
| IRS Rate per Square Foot | $5.00 |
| **Simplified Deduction** | **$** |

`FORMULA (Simplified): =MIN(SquareFootage, 300) * 5`
Maximum deduction under simplified method: $1,500

---

## Method 2: Actual Expense Method

### Step A: Calculate Business Percentage

| Measurement | Value |
|-------------|------:|
| Total Home Square Footage | sq ft |
| Dedicated Office Square Footage | sq ft |
| **Business Use Percentage** | **%** |

`FORMULA (Business %): =OfficeSquareFootage / TotalHomeSquareFootage * 100`

### Step B: Home Expenses (Annual)

| Expense | Annual Amount | Business Portion |
|---------|:------------:|:---------------:|
| Mortgage Interest OR Rent | $ | $ |
| Property Tax | $ | $ |
| Homeowner's/Renter's Insurance | $ | $ |
| Utilities (electric, gas, water) | $ | $ |
| Internet Service | $ | $ |
| Home Repairs & Maintenance | $ | $ |
| Depreciation of Home (owners only) | $ | $ |
| Security System | $ | $ |
| **TOTAL** | **$** | **$** |

`FORMULA (Business Portion): =AnnualAmount * BusinessUsePercentage`

### Step C: Direct Expenses (100% Deductible)

| Expense | Amount |
|---------|-------:|
| Office furniture (used only in office) | $ |
| Office-only repairs/paint | $ |
| Dedicated office phone line | $ |
| **Total Direct Expenses** | **$** |

### Step D: Total Actual Method Deduction

| Line Item | Amount |
|-----------|-------:|
| Indirect Expenses (Business Portion) | $ |
| + Direct Expenses | $ |
| **= Total Actual Method Deduction** | **$** |

---

## Comparison

| Method | Deduction Amount | Use This One? |
|--------|:----------------:|:------------:|
| Simplified | $ | |
| Actual Expense | $ | |
| **HIGHER (USE THIS)** | **$** | YES |

`FORMULA (Winner): =MAX(Simplified, ActualMethod)`

---

---

# SHEET 5: ESTIMATED TAX PAYMENTS

> Calculate quarterly estimated tax payments to avoid underpayment penalties.

---

## Quarterly Estimated Tax Calculator

| Input | Value |
|-------|------:|
| Projected Annual Net Profit | $ |
| Federal Tax Bracket (marginal) | % |
| State Tax Rate | % |
| Self-Employment Tax Rate | 14.13% |
| **Total Effective Rate** | **%** |
| **Annual Tax Estimate** | **$** |
| **Quarterly Payment** | **$** |

`FORMULA (Total Rate): =FederalRate + StateRate + SERate`
`FORMULA (Annual Tax): =NetProfit * TotalRate`
`FORMULA (Quarterly Payment): =AnnualTax / 4`

---

## Payment Schedule & Tracker

| Quarter | Period | Due Date | Amount Due | Date Paid | Confirmation # | Status |
|:-------:|--------|----------|:----------:|-----------|:--------------:|:------:|
| Q1 | Jan 1 - Mar 31 | April 15 | $ | | | Paid/Due |
| Q2 | Apr 1 - May 31 | June 15 | $ | | | Paid/Due |
| Q3 | Jun 1 - Aug 31 | September 15 | $ | | | Paid/Due |
| Q4 | Sep 1 - Dec 31 | January 15 (next year) | $ | | | Paid/Due |
| **TOTAL** | | | **$** | | | |

---

## Safe Harbor Rules

| Rule | Requirement | Your Status |
|------|-------------|:-----------:|
| Pay 100% of last year's tax | Total quarterly = last year's total | Met / Not Met |
| OR Pay 90% of this year's tax | Estimated payments cover 90%+ | Met / Not Met |
| 110% rule (AGI > $150K) | Must pay 110% of last year's tax | Met / Not Met |

If you meet either safe harbor rule, you avoid underpayment penalties.

---

## Mid-Year Adjustment

| Metric | Beginning of Year Estimate | Mid-Year Actual | Adjusted Estimate |
|--------|:-------------------------:|:---------------:|:-----------------:|
| Annual Revenue | $ | $ (annualized) | $ |
| Annual Expenses | $ | $ (annualized) | $ |
| Net Profit | $ | $ | $ |
| Tax Due | $ | $ | $ |
| Quarterly Payment (remaining) | $ | $ | $ |

`FORMULA (Annualized): =YTD_Amount / MonthsElapsed * 12`
`FORMULA (Remaining Quarterly): =(AdjustedAnnualTax - AmountAlreadyPaid) / RemainingQuarters`

---

---

# SHEET 6: YEAR-END REPORT

> One-page summary to hand to your CPA or use for self-filing. All numbers organized by Schedule C line.

---

## Business Information

| Field | Value |
|-------|-------|
| Business Name | |
| Owner Name | |
| EIN or SSN | |
| Business Type | Sole Prop / Single-Member LLC |
| Accounting Method | Cash / Accrual |
| Tax Year | |

---

## Income Summary

| Source | Amount |
|--------|-------:|
| Gross Revenue (1099 income + direct payments) | $ |
| Returns & Allowances | ($ ) |
| **Net Revenue** | **$** |

---

## Expense Summary (by Schedule C Line)

| Line | Category | Annual Total |
|:----:|----------|:------------:|
| 8 | Advertising | $ |
| 9 | Car & Truck Expenses | $ |
| 10 | Commissions & Fees | $ |
| 11 | Contract Labor | $ |
| 13 | Depreciation | $ |
| 15 | Insurance | $ |
| 16a | Interest (mortgage/business) | $ |
| 17 | Legal & Professional | $ |
| 18 | Office Expense | $ |
| 20b | Rent or Lease | $ |
| 21 | Repairs & Maintenance | $ |
| 22 | Supplies | $ |
| 23 | Taxes & Licenses | $ |
| 24a | Travel | $ |
| 24b | Meals (at 50%) | $ |
| 25 | Utilities | $ |
| 27a | Other (itemize below) | $ |
| 30 | Home Office Deduction | $ |
| | **TOTAL EXPENSES** | **$** |

---

## Other Expenses Detail (Line 27a)

| Description | Amount |
|-------------|-------:|
| Software & Subscriptions | $ |
| Education & Training | $ |
| Bank & Merchant Fees | $ |
| Postage & Shipping | $ |
| Dues & Memberships | $ |
| **Total Other Expenses** | **$** |

---

## Net Profit Calculation

| Line Item | Amount |
|-----------|-------:|
| Net Revenue | $ |
| - Total Expenses | ($ ) |
| **= Net Profit (Loss)** | **$** |
| Self-Employment Tax (14.13%) | $ |
| Federal Income Tax (at bracket) | $ |
| State Income Tax | $ |
| **Estimated Total Tax Liability** | **$** |
| - Quarterly Payments Made | ($ ) |
| **= Balance Due / (Refund)** | **$** |

---

## Above-the-Line Deductions (Form 1040, not Schedule C)

| Deduction | Amount | Notes |
|-----------|-------:|-------|
| Self-Employed Health Insurance | $ | 100% deductible |
| SEP-IRA / Solo 401(k) | $ | Up to 25% of net profit |
| 1/2 Self-Employment Tax | $ | Automatic deduction |
| Student Loan Interest | $ | Up to $2,500 |
| **Total Above-the-Line** | **$** | |

---

---

# FORMULA REFERENCE GUIDE

---

## Expense Tracking

**Category total by quarter:**
```
=SUMIFS(Amount, Category, "Advertising*", Date, ">="&QuarterStart, Date, "<="&QuarterEnd)
```

**Annual total for category:**
```
=SUMIF(Category, "Advertising*", Amount)
```

**Monthly total all expenses:**
```
=SUMIFS(Amount, MONTH(Date), MonthNumber)
```

## Mileage

**Mileage deduction:**
```
=TotalBusinessMiles * IRSMileageRate
```

## Home Office

**Business use percentage:**
```
=OfficeSquareFeet / TotalSquareFeet
```

**Actual method deduction:**
```
=SUM(IndirectExpenses) * BusinessPct + SUM(DirectExpenses)
```

## Estimated Tax

**Quarterly payment:**
```
=NetProfit * (FedRate + StateRate + 0.1413) / 4
```

## Conditional Formatting

**Expense over $500 (highlight for review):**
```
=E2 > 500
```

**Missing receipt (red):**
```
=AND(E2 > 75, H2 = "")
```

**Quarterly payment overdue (red):**
```
=AND(F2 = "", TODAY() > DueDate)
```

**Category over budget (orange):**
```
=CategoryTotal > CategoryBudget
```

---

> **NOTE:** This tracker is designed for sole proprietors and single-member LLCs filing Schedule C. If you have an S-Corp, partnership, or C-Corp, the categories still apply but your filing forms differ. The IRS requires receipts for any expense over $75, but best practice is to save all receipts. Meals are 50% deductible for regular business meals. Keep this spreadsheet updated weekly — 10 minutes every Sunday saves 10+ hours at tax time. Always consult a CPA for your specific tax situation.
