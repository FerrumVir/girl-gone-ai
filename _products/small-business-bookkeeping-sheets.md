# Small Business Bookkeeping System
## Complete Financial Management for Freelancers & Small Businesses

---

> **SETUP GUIDE — Get Running in 30 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 9 tabs/sheets and name them: Income, Expenses, Invoices, Tax Categories, Quarterly Taxes, P&L, Balance Sheet, Cash Flow, Receipts & Mileage
> 3. Copy each section below into its corresponding sheet
> 4. Enter the formulas as documented (all formulas are marked with `FORMULA:`)
> 5. Enter your business information in the Balance Sheet (starting balances)
> 6. Start entering today's income and expenses — the system builds from here
>
> **Tip:** Set a weekly reminder (Friday afternoon or Monday morning) to enter any transactions you haven't logged during the week. Consistency beats perfection.

---

---

# SHEET 1: INCOME TRACKER

> Every dollar that comes into the business. Enter each payment as it's received.

---

## Column Headers

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Date** | **Client / Source** | **Invoice #** | **Description** | **Amount** | **Payment Method** | **Income Category** | **Notes** |

## Income Categories (Dropdown)

- Service Revenue
- Product Sales
- Retainer / Recurring
- Affiliate / Commission
- Consulting
- Speaking / Teaching
- Licensing / Royalties
- Refund (negative amount)
- Other Income

## Payment Methods (Dropdown)

- Bank Transfer / ACH
- Check
- Credit Card
- PayPal
- Stripe
- Venmo
- Cash
- Zelle
- Wire Transfer
- Other

---

## Sample Entries

| Date | Client / Source | Invoice # | Description | Amount | Payment Method | Income Category | Notes |
|------|----------------|-----------|-------------|--------|----------------|-----------------|-------|
| 2026-01-05 | Acme Corp | INV-001 | Website redesign - Phase 1 | $3,500.00 | Bank Transfer | Service Revenue | 50% deposit |
| 2026-01-12 | Smith & Co | INV-002 | Monthly SEO retainer - January | $2,000.00 | Stripe | Retainer / Recurring | |
| 2026-01-18 | Amazon Associates | — | January affiliate commissions | $342.50 | Bank Transfer | Affiliate / Commission | |

---

## Summary Section (Place below data entries)

### Monthly Income Summary

| Month | Service Revenue | Product Sales | Retainer | Affiliate | Other | **Monthly Total** |
|-------|----------------|---------------|----------|-----------|-------|--------------------|
| January | | | | | | |
| February | | | | | | |
| March | | | | | | |
| April | | | | | | |
| May | | | | | | |
| June | | | | | | |
| July | | | | | | |
| August | | | | | | |
| September | | | | | | |
| October | | | | | | |
| November | | | | | | |
| December | | | | | | |
| **Year Total** | | | | | | |

`FORMULA: Use SUMIFS to sum Amount column where Month matches AND Income Category matches`
`Example: =SUMIFS(E:E, A:A, ">="&DATE(2026,1,1), A:A, "<"&DATE(2026,2,1), G:G, "Service Revenue")`

---

---

# SHEET 2: EXPENSE TRACKER

> Every dollar that goes out. Enter each expense as it occurs.

---

## Column Headers

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Date** | **Vendor / Payee** | **Description** | **Amount** | **Payment Method** | **Tax Category** | **Receipt?** | **Receipt Location** | **Notes** |

## Tax Categories (Dropdown — Mapped to IRS Schedule C)

| Tax Category | Schedule C Line | Description |
|-------------|-----------------|-------------|
| Advertising & Marketing | Line 8 | Ads, social media ads, business cards, signage, sponsorships |
| Car & Truck Expenses | Line 9 | Gas, maintenance, insurance (or use standard mileage rate) |
| Commissions & Fees | Line 10 | Platform fees, subcontractor commissions, referral fees |
| Contract Labor | Line 11 | Subcontractors, freelancers (1099 workers) |
| Insurance | Line 15 | Business insurance, professional liability, health (if self-employed) |
| Interest | Line 16a/b | Business loan interest, business credit card interest |
| Legal & Professional | Line 17 | Attorney fees, accountant, bookkeeper, consultant fees |
| Office Expense | Line 18 | Supplies, postage, printing, stationery |
| Rent / Lease | Line 20a/b | Office rent, equipment leases, coworking space |
| Repairs & Maintenance | Line 21 | Equipment repairs, website maintenance |
| Supplies | Line 22 | Materials and supplies consumed by the business |
| Taxes & Licenses | Line 23 | Business licenses, state taxes, permits |
| Travel | Line 24a | Airfare, hotel, transportation for business travel |
| Meals | Line 24b | Business meals (50% deductible) |
| Utilities | Line 25 | Internet, phone, electricity (business portion) |
| Software & Subscriptions | Other Expenses | SaaS tools, software, digital subscriptions |
| Education & Training | Other Expenses | Courses, books, conferences, certifications |
| Equipment | Depreciation/179 | Computers, cameras, tools, furniture (may be depreciated) |
| Home Office | Form 8829 | Rent/mortgage, utilities, insurance (business % of home) |
| Bank & Processing Fees | Other Expenses | Bank fees, payment processing fees (Stripe, PayPal) |
| Shipping & Delivery | Other Expenses | Postage, courier, shipping supplies |
| Dues & Memberships | Other Expenses | Professional associations, trade organizations |
| Other Expense | Other Expenses | Anything not covered above |

---

## Sample Entries

| Date | Vendor | Description | Amount | Payment | Tax Category | Receipt? | Receipt Location | Notes |
|------|--------|-------------|--------|---------|--------------|----------|------------------|-------|
| 2026-01-03 | Adobe | Creative Cloud monthly | $59.99 | Credit Card | Software & Subscriptions | Yes | Google Drive/Receipts/Jan | Annual plan |
| 2026-01-05 | WeWork | January coworking space | $350.00 | Bank Transfer | Rent / Lease | Yes | Google Drive/Receipts/Jan | |
| 2026-01-08 | Staples | Printer paper, ink | $47.82 | Credit Card | Office Expense | Yes | Photo/Jan-08-staples | |
| 2026-01-10 | Restaurant | Client lunch - Smith & Co | $68.40 | Credit Card | Meals | Yes | Photo/Jan-10-lunch | 50% deductible |

---

## Monthly Expense Summary

| Month | Advertising | Contract Labor | Office | Software | Rent | Travel | Meals | Insurance | Other | **Monthly Total** |
|-------|------------|----------------|--------|----------|------|--------|-------|-----------|-------|--------------------|
| January | | | | | | | | | | |
| February | | | | | | | | | | |
| March | | | | | | | | | | |
| April | | | | | | | | | | |
| May | | | | | | | | | | |
| June | | | | | | | | | | |
| July | | | | | | | | | | |
| August | | | | | | | | | | |
| September | | | | | | | | | | |
| October | | | | | | | | | | |
| November | | | | | | | | | | |
| December | | | | | | | | | | |
| **Year Total** | | | | | | | | | | |

`FORMULA: =SUMIFS(D:D, A:A, ">="&DATE(2026,1,1), A:A, "<"&DATE(2026,2,1), F:F, "Advertising & Marketing")`

---

---

# SHEET 3: INVOICE LOG

> Track every invoice from creation through payment.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Invoice #** | **Client** | **Description** | **Amount** | **Date Sent** | **Due Date** | **Date Paid** | **Status** | **Days Outstanding** | **Notes** |

## Status Options (Dropdown)
- Draft
- Sent
- Overdue
- Paid
- Partial
- Cancelled
- Written Off

`FORMULA for Days Outstanding: =IF(H2="Paid", G2-E2, IF(H2="Cancelled","—", TODAY()-E2))`
`FORMULA for auto-Overdue: =IF(AND(H2="Sent", F2<TODAY()), "OVERDUE", H2)`

---

## Sample Entries

| Invoice # | Client | Description | Amount | Date Sent | Due Date | Date Paid | Status | Days Out | Notes |
|-----------|--------|-------------|--------|-----------|----------|-----------|--------|----------|-------|
| INV-001 | Acme Corp | Website redesign Phase 1 | $3,500 | 2026-01-02 | 2026-01-17 | 2026-01-05 | Paid | 3 | Paid early |
| INV-002 | Smith & Co | SEO Retainer - Jan | $2,000 | 2026-01-01 | 2026-01-16 | 2026-01-12 | Paid | 11 | |
| INV-003 | Acme Corp | Website redesign Phase 2 | $3,500 | 2026-01-20 | 2026-02-04 | — | Sent | 12 | Follow up Feb 1 |
| INV-004 | Jones LLC | Consulting - Q1 | $5,000 | 2026-01-25 | 2026-02-09 | — | Sent | 7 | |

---

## Accounts Receivable Aging Summary

| Aging Bucket | Count | Total Amount |
|-------------|-------|-------------|
| Current (0-30 days) | | $ |
| 31-60 days | | $ |
| 61-90 days | | $ |
| 90+ days | | $ |
| **Total Outstanding** | | **$** |

`FORMULA: =SUMIFS(D:D, H:H, "Sent", I:I, "<=30")`
`FORMULA: =SUMIFS(D:D, H:H, "Sent", I:I, ">30", I:I, "<=60")`

---

---

# SHEET 4: TAX CATEGORY SUMMARY

> Auto-generated from the Expense Tracker. Use this for tax preparation.

---

## Annual Tax Category Summary — [YEAR]

| Schedule C Line | Category | Annual Total | Q1 | Q2 | Q3 | Q4 |
|----------------|----------|-------------|----|----|----|----|
| Line 1 | **Gross Income** | | | | | |
| Line 8 | Advertising | | | | | |
| Line 9 | Car & Truck | | | | | |
| Line 10 | Commissions & Fees | | | | | |
| Line 11 | Contract Labor | | | | | |
| Line 15 | Insurance | | | | | |
| Line 16 | Interest | | | | | |
| Line 17 | Legal & Professional | | | | | |
| Line 18 | Office Expense | | | | | |
| Line 20 | Rent / Lease | | | | | |
| Line 21 | Repairs & Maintenance | | | | | |
| Line 22 | Supplies | | | | | |
| Line 23 | Taxes & Licenses | | | | | |
| Line 24a | Travel | | | | | |
| Line 24b | Meals (enter 100%, deduct 50%) | | | | | |
| Line 25 | Utilities | | | | | |
| Line 27 | Other Expenses | | | | | |
| | Software & Subscriptions | | | | | |
| | Education & Training | | | | | |
| | Equipment (Section 179 / Depreciation) | | | | | |
| | Bank & Processing Fees | | | | | |
| | Shipping & Delivery | | | | | |
| | Dues & Memberships | | | | | |
| | Home Office (Form 8829) | | | | | |
| | **Total Expenses** | | | | | |
| | **Net Profit (Income - Expenses)** | | | | | |

`FORMULA: Each row pulls from Expense Tracker using SUMIFS on Tax Category column`
`FORMULA: Gross Income pulls from Income Tracker total`
`FORMULA: Net Profit = Gross Income - Total Expenses`

---

---

# SHEET 5: QUARTERLY TAX ESTIMATES

> Calculates your estimated quarterly tax payments.

---

## Your Tax Information

| Field | Value |
|-------|-------|
| **Filing Status** | [ ] Single [ ] Married Filing Jointly [ ] Head of Household |
| **Federal Tax Bracket (estimated)** | [X]% |
| **State Tax Rate (if applicable)** | [X]% |
| **Self-Employment Tax Rate** | 15.3% (on 92.35% of net self-employment income) |

---

## Quarterly Estimate Calculation

| | Q1 (Jan-Mar) | Q2 (Apr-Jun) | Q3 (Jul-Sep) | Q4 (Oct-Dec) | **Annual** |
|--|-------------|-------------|-------------|-------------|------------|
| **Gross Income** | | | | | |
| **Total Expenses** | | | | | |
| **Net Profit** | | | | | |
| **SE Tax Base (92.35%)** | | | | | |
| **Self-Employment Tax** | | | | | |
| **Adjusted Net Income** | | | | | |
| **Federal Income Tax** | | | | | |
| **State Income Tax** | | | | | |
| **Total Estimated Tax** | | | | | |
| **Quarterly Payment Due** | | | | | |

`FORMULA: SE Tax Base = Net Profit * 0.9235`
`FORMULA: Self-Employment Tax = SE Tax Base * 0.153`
`FORMULA: Adjusted Net Income = Net Profit - (Self-Employment Tax / 2)`
`FORMULA: Federal Income Tax = Adjusted Net Income * Federal Tax Bracket %`
`FORMULA: Quarterly Payment = Total Estimated Tax / 4 (or cumulative method)`

---

## Payment Due Dates

| Quarter | Period | Due Date | Amount Due | Paid? | Date Paid | Confirmation # |
|---------|--------|----------|-----------|-------|-----------|----------------|
| Q1 | Jan-Mar | April 15 | $ | [ ] | | |
| Q2 | Apr-Jun | June 15 | $ | [ ] | | |
| Q3 | Jul-Sep | September 15 | $ | [ ] | | |
| Q4 | Oct-Dec | January 15 (next year) | $ | [ ] | | |

---

> **IMPORTANT NOTE:** These estimates are approximations based on your entered data. They do not account for all possible deductions, credits, or tax situations. Consult a tax professional for precise tax planning. These estimates are designed to help you avoid underpayment penalties by making reasonable quarterly payments throughout the year.

---

---

# SHEET 6: PROFIT & LOSS STATEMENT

> Auto-generated from Income and Expense trackers. No manual entry needed.

---

## Profit & Loss Statement — [BUSINESS NAME]

### For the Period: [Month/Quarter/Year]

| | Jan | Feb | Mar | Q1 Total | Apr | May | Jun | Q2 Total | Jul | Aug | Sep | Q3 Total | Oct | Nov | Dec | Q4 Total | **Year Total** |
|--|-----|-----|-----|----------|-----|-----|-----|----------|-----|-----|-----|----------|-----|-----|-----|----------|----------------|
| **REVENUE** | | | | | | | | | | | | | | | | | |
| Service Revenue | | | | | | | | | | | | | | | | | |
| Product Sales | | | | | | | | | | | | | | | | | |
| Retainer / Recurring | | | | | | | | | | | | | | | | | |
| Affiliate / Commission | | | | | | | | | | | | | | | | | |
| Other Income | | | | | | | | | | | | | | | | | |
| **Total Revenue** | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| **COST OF GOODS SOLD** | | | | | | | | | | | | | | | | | |
| Materials / Supplies | | | | | | | | | | | | | | | | | |
| Contract Labor (direct) | | | | | | | | | | | | | | | | | |
| **Total COGS** | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| **GROSS PROFIT** | | | | | | | | | | | | | | | | | |
| **Gross Margin %** | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| **OPERATING EXPENSES** | | | | | | | | | | | | | | | | | |
| Advertising & Marketing | | | | | | | | | | | | | | | | | |
| Software & Subscriptions | | | | | | | | | | | | | | | | | |
| Office Expense | | | | | | | | | | | | | | | | | |
| Rent / Lease | | | | | | | | | | | | | | | | | |
| Insurance | | | | | | | | | | | | | | | | | |
| Legal & Professional | | | | | | | | | | | | | | | | | |
| Travel | | | | | | | | | | | | | | | | | |
| Meals (50%) | | | | | | | | | | | | | | | | | |
| Utilities | | | | | | | | | | | | | | | | | |
| Education & Training | | | | | | | | | | | | | | | | | |
| Bank & Processing Fees | | | | | | | | | | | | | | | | | |
| Equipment / Depreciation | | | | | | | | | | | | | | | | | |
| Other Expenses | | | | | | | | | | | | | | | | | |
| **Total Operating Expenses** | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | |
| **NET PROFIT** | | | | | | | | | | | | | | | | | |
| **Net Profit Margin %** | | | | | | | | | | | | | | | | | |

`FORMULA: Each cell references the Income or Expense tracker using SUMIFS`
`FORMULA: Gross Profit = Total Revenue - Total COGS`
`FORMULA: Gross Margin % = Gross Profit / Total Revenue * 100`
`FORMULA: Net Profit = Gross Profit - Total Operating Expenses`
`FORMULA: Net Profit Margin % = Net Profit / Total Revenue * 100`

---

---

# SHEET 7: BALANCE SHEET

> Track what you own, what you owe, and what's left.

---

## Balance Sheet — [BUSINESS NAME]
### As of [DATE]

### ASSETS

| Asset | Description | Amount |
|-------|-------------|--------|
| **Current Assets** | | |
| Cash (Business Checking) | [Bank name, account] | $ |
| Cash (Business Savings) | [Bank name, account] | $ |
| Accounts Receivable | Outstanding invoices (from Invoice Log) | $ |
| Inventory | Products on hand | $ |
| Prepaid Expenses | Subscriptions/insurance paid in advance | $ |
| **Total Current Assets** | | **$** |
| | | |
| **Fixed Assets** | | |
| Equipment | Computer, camera, tools | $ |
| Furniture | Desk, chair, shelving | $ |
| Vehicle (business portion) | | $ |
| Less: Accumulated Depreciation | | ($ ) |
| **Total Fixed Assets** | | **$** |
| | | |
| **TOTAL ASSETS** | | **$** |

### LIABILITIES

| Liability | Description | Amount |
|-----------|-------------|--------|
| **Current Liabilities** | | |
| Accounts Payable | Bills due within 30 days | $ |
| Credit Card Balance | Business credit card(s) | $ |
| Sales Tax Payable | Collected, not yet remitted | $ |
| Estimated Tax Payable | Quarterly estimates due | $ |
| **Total Current Liabilities** | | **$** |
| | | |
| **Long-Term Liabilities** | | |
| Business Loan | [Lender, terms] | $ |
| Equipment Financing | [Lender, terms] | $ |
| **Total Long-Term Liabilities** | | **$** |
| | | |
| **TOTAL LIABILITIES** | | **$** |

### EQUITY

| | Amount |
|--|--------|
| Owner's Equity (beginning of year) | $ |
| Plus: Net Profit (year to date) | $ |
| Less: Owner's Draws/Distributions | ($ ) |
| **Total Equity** | **$** |

### BALANCE CHECK

| | Amount |
|--|--------|
| Total Assets | $ |
| Total Liabilities + Equity | $ |
| **Difference (should be $0)** | **$** |

`FORMULA: Difference = Total Assets - (Total Liabilities + Total Equity)`
`If this is not $0, there is an entry error to find and correct.`

---

---

# SHEET 8: CASH FLOW PROJECTIONS

> Forward-looking 6-month cash flow. Your early warning system.

---

## 6-Month Cash Flow Projection

**Starting Cash Balance:** $[AMOUNT]
**Safety Threshold:** $[MINIMUM — e.g., $5,000] (system flags months below this)

| | Month 1 | Month 2 | Month 3 | Month 4 | Month 5 | Month 6 |
|--|---------|---------|---------|---------|---------|---------|
| **Month** | [Name] | [Name] | [Name] | [Name] | [Name] | [Name] |
| | | | | | | |
| **CASH IN** | | | | | | |
| Expected Client Payments | $ | $ | $ | $ | $ | $ |
| Retainer Income | $ | $ | $ | $ | $ | $ |
| Product Sales (estimated) | $ | $ | $ | $ | $ | $ |
| Other Income | $ | $ | $ | $ | $ | $ |
| **Total Cash In** | **$** | **$** | **$** | **$** | **$** | **$** |
| | | | | | | |
| **CASH OUT** | | | | | | |
| Rent / Lease | $ | $ | $ | $ | $ | $ |
| Payroll / Contractors | $ | $ | $ | $ | $ | $ |
| Software & Subscriptions | $ | $ | $ | $ | $ | $ |
| Insurance | $ | $ | $ | $ | $ | $ |
| Marketing / Advertising | $ | $ | $ | $ | $ | $ |
| Utilities | $ | $ | $ | $ | $ | $ |
| Loan Payments | $ | $ | $ | $ | $ | $ |
| Estimated Tax Payments | $ | $ | $ | $ | $ | $ |
| Equipment Purchases | $ | $ | $ | $ | $ | $ |
| Other Expenses | $ | $ | $ | $ | $ | $ |
| Owner's Draw | $ | $ | $ | $ | $ | $ |
| **Total Cash Out** | **$** | **$** | **$** | **$** | **$** | **$** |
| | | | | | | |
| **NET CASH FLOW** | **$** | **$** | **$** | **$** | **$** | **$** |
| **ENDING CASH BALANCE** | **$** | **$** | **$** | **$** | **$** | **$** |
| **Below Safety Threshold?** | | | | | | |

`FORMULA: Net Cash Flow = Total Cash In - Total Cash Out`
`FORMULA: Ending Cash Balance = Starting Balance (or previous month ending) + Net Cash Flow`
`FORMULA: Below Threshold = IF(Ending Balance < Safety Threshold, "WARNING", "OK")`

---

### How to Use This

1. Fill in known recurring expenses (rent, subscriptions, insurance, loan payments)
2. Fill in confirmed expected income (signed contracts, retainer clients, recurring revenue)
3. Estimate variable income and expenses based on recent months
4. Review the ending cash balance for each month
5. If any month shows "WARNING," take action NOW: invoice early, delay non-essential expenses, or arrange a credit facility
6. Update monthly as actuals replace estimates

---

---

# SHEET 9: RECEIPT ORGANIZER & MILEAGE TRACKER

---

## Receipt Log

| Date | Vendor | Amount | Expense Category | Storage Location | Linked Expense Row | Notes |
|------|--------|--------|-----------------|-----------------|-------------------|-------|
| [Date] | [Vendor] | $[Amount] | [Category] | [e.g., Google Drive/Receipts/Jan/vendor-date.pdf] | [Row # in Expense Tracker] | |
| [Date] | [Vendor] | $[Amount] | [Category] | [Photo: phone-receipts/2026-01-08.jpg] | [Row #] | |

**Storage Options:**
- Google Drive folder: `/Business/Receipts/[Year]/[Month]/`
- Phone photos: organized by date in a dedicated album
- Email receipts: labeled/tagged in email and referenced here
- Physical: filed by month in accordion folder, referenced as "Physical/[Month]"

---

## Mileage Tracker

**IRS Standard Mileage Rate (2026):** $[0.XX] per mile
*(Check IRS.gov for current year rate — update this number each January)*

| Date | Destination | Business Purpose | Starting Odometer | Ending Odometer | Miles | Deduction Value |
|------|------------|-----------------|-------------------|-----------------|-------|----------------|
| [Date] | [Destination] | [Purpose — e.g., client meeting, supplier pickup] | [Start] | [End] | | |
| [Date] | [Destination] | [Purpose] | [Start] | [End] | | |
| [Date] | [Destination] | [Purpose] | [Start] | [End] | | |

`FORMULA: Miles = Ending Odometer - Starting Odometer`
`FORMULA: Deduction Value = Miles * IRS Standard Rate`

### Annual Mileage Summary

| | Total |
|--|-------|
| **Total Business Miles** | |
| **IRS Standard Rate** | $0.XX |
| **Total Mileage Deduction** | $ |
| **Trips Logged** | |
| **Average Miles per Trip** | |

---

---

# MONTHLY BOOKKEEPING WORKFLOW

> Follow this checklist weekly or monthly to keep your books current.

---

## Weekly (15 minutes)

- [ ] Enter all income received this week into Income Tracker
- [ ] Enter all expenses from this week into Expense Tracker
- [ ] Assign tax categories to any uncategorized expenses
- [ ] Log any new invoices sent in the Invoice Log
- [ ] Update status on any invoices that were paid this week
- [ ] Log business miles driven this week in Mileage Tracker
- [ ] File/upload any new receipts and log in Receipt Organizer

## Monthly (30 minutes — on the 1st of each month)

- [ ] Reconcile: compare bank statement totals to your Income and Expense trackers
- [ ] Review Invoice Log — follow up on any overdue invoices
- [ ] Review P&L for the completed month — are you profitable?
- [ ] Update Balance Sheet — adjust cash balances, accounts receivable, liabilities
- [ ] Update Cash Flow Projections — shift forward one month, add new month 6
- [ ] Log any Retainer entries for the new month
- [ ] Review upcoming estimated tax payment dates

## Quarterly (1 hour)

- [ ] Calculate and pay estimated quarterly taxes
- [ ] Review year-to-date P&L — are you on track for annual goals?
- [ ] Review expense trends — any categories growing faster than revenue?
- [ ] Update Cash Flow Projections with any new information
- [ ] Back up your spreadsheet (download a copy to local storage)

## Annually (2-3 hours — in January)

- [ ] Run full-year Tax Category Summary for the completed year
- [ ] Generate full-year P&L
- [ ] Generate year-end Balance Sheet
- [ ] Compile Mileage Tracker annual summary
- [ ] Provide all reports to your accountant (or use for self-filing)
- [ ] Create a new copy of the spreadsheet for the new year
- [ ] Set up new year with starting balances from prior year-end
- [ ] Update IRS mileage rate for the new year
- [ ] Review and update tax bracket estimate for the new year

---

---

# FORMULA REFERENCE GUIDE

> All key formulas in plain English. Copy these into Google Sheets.

---

## Income Tracker Formulas

**Monthly total for a specific category:**
```
=SUMIFS(E:E, MONTH(A:A), [month number], YEAR(A:A), [year], G:G, "Service Revenue")
```

**Year-to-date total income:**
```
=SUMIFS(E:E, A:A, ">="&DATE(2026,1,1), A:A, "<="&TODAY())
```

## Expense Tracker Formulas

**Monthly total for a specific tax category:**
```
=SUMIFS(D:D, MONTH(A:A), [month number], YEAR(A:A), [year], F:F, "Software & Subscriptions")
```

## Invoice Aging

**Total outstanding 0-30 days:**
```
=SUMIFS(D:D, H:H, "<>Paid", H:H, "<>Cancelled", I:I, "<=30")
```

## P&L Auto-Population

**Revenue line (e.g., January Service Revenue):**
```
=SUMIFS(Income!E:E, MONTH(Income!A:A), 1, YEAR(Income!A:A), 2026, Income!G:G, "Service Revenue")
```

**Expense line (e.g., January Software):**
```
=SUMIFS(Expenses!D:D, MONTH(Expenses!A:A), 1, YEAR(Expenses!A:A), 2026, Expenses!F:F, "Software & Subscriptions")
```

## Cash Flow

**Ending balance:**
```
=Previous Month Ending Balance + This Month Net Cash Flow
```

**Threshold check:**
```
=IF(Ending Balance < Safety Threshold, "WARNING", "OK")
```

## Mileage

**Deduction value per trip:**
```
=Miles * IRS_Rate
```

**Annual total deduction:**
```
=SUM(Deduction Value column)
```

---

> **DISCLAIMER:** This bookkeeping system is a financial management tool for small businesses. It is not a substitute for professional accounting, tax, or legal advice. Tax laws vary by jurisdiction and change over time. Consult a qualified tax professional or CPA for tax planning, compliance, and filing. This system is designed to organize your financial data so you — and your accountant — can make informed decisions.
