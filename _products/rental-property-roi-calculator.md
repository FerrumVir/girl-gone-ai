# Rental Property ROI Calculator — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Analyze any rental property deal in under 10 minutes with cash-on-cash return, cap rate, cash flow projections, and side-by-side comparison of up to 5 properties.

---

> **SETUP GUIDE — Get Running in 15 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 6 tabs/sheets and name them: Deal Analyzer, Monthly Cash Flow, Expense Breakdown, 10-Year Projection, Property Comparison, Mortgage Amortization
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Start with Deal Analyzer — enter the purchase price and financing terms for your target property
> 6. Monthly Cash Flow auto-populates once Deal Analyzer is filled in
>
> **Tip:** Run three scenarios for every property: conservative (assume 10% vacancy, higher expenses), moderate, and optimistic. If the deal works on conservative numbers, it's a solid buy.

---

---

# SHEET 1: DEAL ANALYZER

> One-page summary of any property deal. The four numbers that matter: Cash-on-Cash Return, Cap Rate, Monthly Cash Flow, and Break-Even Occupancy.

---

## Property Information

| Field | Value |
|-------|-------|
| Property Address | |
| City, State, ZIP | |
| Property Type | SFR / Duplex / Triplex / Fourplex / Condo |
| Bedrooms / Bathrooms | / |
| Square Footage | |
| Year Built | |
| Listing Price | $ |
| MLS / Listing URL | |

---

## Purchase & Financing

| Item | Amount | Notes |
|------|-------:|-------|
| Purchase Price | $ | |
| Down Payment (%) | % | |
| Down Payment ($) | $ | |
| Loan Amount | $ | |
| Interest Rate | % | |
| Loan Term (years) | | |
| Monthly Mortgage Payment (P&I) | $ | |
| Closing Costs (estimate 2-5%) | $ | |
| Renovation / Rehab Budget | $ | |
| **Total Cash Invested** | **$** | |

`FORMULA (Down Payment $): =PurchasePrice * DownPaymentPct`
`FORMULA (Loan Amount): =PurchasePrice - DownPayment`
`FORMULA (Monthly Mortgage): =PMT(Rate/12, Term*12, -LoanAmount)`
`FORMULA (Total Cash Invested): =DownPayment + ClosingCosts + RehabBudget`

---

## Income

| Source | Monthly | Annual |
|--------|--------:|-------:|
| Rent (Unit 1) | $ | $ |
| Rent (Unit 2 — if multi-unit) | $ | $ |
| Rent (Unit 3 — if multi-unit) | $ | $ |
| Rent (Unit 4 — if multi-unit) | $ | $ |
| Other Income (laundry, parking, storage) | $ | $ |
| **Gross Monthly Income** | **$** | **$** |
| Vacancy Rate (%) | % | |
| Vacancy Loss | ($ ) | ($ ) |
| **Effective Gross Income** | **$** | **$** |

`FORMULA (Annual): =Monthly * 12`
`FORMULA (Vacancy Loss): =GrossIncome * VacancyRate`
`FORMULA (Effective Gross Income): =GrossIncome - VacancyLoss`

---

## Expenses (Monthly)

| Expense | Monthly | Annual | % of Rent |
|---------|--------:|-------:|:---------:|
| Property Tax | $ | $ | % |
| Insurance | $ | $ | % |
| Property Management (8-10%) | $ | $ | % |
| Maintenance Reserve (5-10%) | $ | $ | % |
| CapEx Reserve (5-10%) | $ | $ | % |
| HOA / Condo Fees | $ | $ | % |
| Utilities (if owner-paid) | $ | $ | % |
| Landscaping / Snow Removal | $ | $ | % |
| Pest Control | $ | $ | % |
| Other | $ | $ | % |
| **Total Operating Expenses** | **$** | **$** | **%** |

`FORMULA (Property Management): =EffectiveGrossIncome * 0.08`
`FORMULA (Maintenance Reserve): =EffectiveGrossIncome * 0.05`
`FORMULA (CapEx Reserve): =EffectiveGrossIncome * 0.05`
`FORMULA (% of Rent): =Expense / GrossIncome * 100`

---

## Key Metrics (Auto-Calculated)

| Metric | Value | Target |
|--------|------:|:------:|
| **Net Operating Income (NOI)** | $ | |
| **Monthly Cash Flow** | $ | > $100/door |
| **Annual Cash Flow** | $ | |
| **Cash-on-Cash Return** | % | > 8% |
| **Cap Rate** | % | 5-10% |
| **Gross Rent Multiplier (GRM)** | x | < 15 |
| **Debt Service Coverage Ratio** | x | > 1.25 |
| **Break-Even Occupancy** | % | < 85% |
| **50% Rule Check** | $ | |
| **1% Rule Check** | % | > 1% |
| **2% Rule Check** | % | > 2% (rare) |

`FORMULA (NOI): =EffectiveGrossIncome_Annual - TotalOperatingExpenses_Annual`
`FORMULA (Monthly Cash Flow): =EffectiveGrossIncome_Monthly - Expenses_Monthly - MortgagePayment`
`FORMULA (Cash-on-Cash): =AnnualCashFlow / TotalCashInvested * 100`
`FORMULA (Cap Rate): =NOI / PurchasePrice * 100`
`FORMULA (GRM): =PurchasePrice / GrossAnnualRent`
`FORMULA (DSCR): =NOI / (MortgagePayment * 12)`
`FORMULA (Break-Even Occupancy): =(Expenses + Mortgage) / GrossIncome * 100`
`FORMULA (50% Rule): =GrossRent * 0.5 - MortgagePayment (rough cash flow estimate)`
`FORMULA (1% Rule): =GrossMonthlyRent / PurchasePrice * 100`

---

---

# SHEET 2: MONTHLY CASH FLOW

> Detailed month-by-month cash flow for the first year.

---

## Monthly Cash Flow Statement

| Month | Gross Rent | - Vacancy | = Effective Income | - Expenses | - Mortgage | = Net Cash Flow | Cumulative |
|-------|----------:|---------:|-----------------:|-----------:|-----------:|---------------:|-----------:|
| 1 | $ | $ | $ | $ | $ | $ | $ |
| 2 | $ | $ | $ | $ | $ | $ | $ |
| 3 | $ | $ | $ | $ | $ | $ | $ |
| 4 | $ | $ | $ | $ | $ | $ | $ |
| 5 | $ | $ | $ | $ | $ | $ | $ |
| 6 | $ | $ | $ | $ | $ | $ | $ |
| 7 | $ | $ | $ | $ | $ | $ | $ |
| 8 | $ | $ | $ | $ | $ | $ | $ |
| 9 | $ | $ | $ | $ | $ | $ | $ |
| 10 | $ | $ | $ | $ | $ | $ | $ |
| 11 | $ | $ | $ | $ | $ | $ | $ |
| 12 | $ | $ | $ | $ | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** | **$** | **$** | **$** | |

`FORMULA (Net Cash Flow): =EffectiveIncome - Expenses - Mortgage`
`FORMULA (Cumulative): =PreviousCumulative + CurrentMonth`

---

## Cash Flow Sensitivity Analysis

| Scenario | Vacancy Rate | Monthly Cash Flow | Annual Cash Flow | CoC Return |
|----------|:-----------:|------------------:|-----------------:|---------:|
| Best Case | 3% | $ | $ | % |
| Moderate | 5% | $ | $ | % |
| Conservative | 8% | $ | $ | % |
| Worst Case | 12% | $ | $ | % |
| Break-Even | % | $0 | $0 | 0% |

`FORMULA (Break-Even Vacancy): =(GrossRent - Expenses - Mortgage) / GrossRent * 100`

---

---

# SHEET 3: EXPENSE BREAKDOWN

> Detailed expense categories with actual vs. estimated tracking.

---

## Annual Expense Detail

| Category | Estimated Monthly | Actual Monthly | Annual (Est) | Annual (Actual) | Variance |
|----------|:----------------:|:--------------:|:------------:|:---------------:|---------:|
| Property Tax | $ | $ | $ | $ | $ |
| Insurance (dwelling) | $ | $ | $ | $ | $ |
| Insurance (liability/umbrella) | $ | $ | $ | $ | $ |
| Property Management Fee | $ | $ | $ | $ | $ |
| Maintenance & Repairs | $ | $ | $ | $ | $ |
| CapEx (roof, HVAC, etc.) | $ | $ | $ | $ | $ |
| HOA / Condo Fees | $ | $ | $ | $ | $ |
| Water / Sewer | $ | $ | $ | $ | $ |
| Trash / Recycling | $ | $ | $ | $ | $ |
| Electric (common area) | $ | $ | $ | $ | $ |
| Gas (common area) | $ | $ | $ | $ | $ |
| Landscaping | $ | $ | $ | $ | $ |
| Snow Removal | $ | $ | $ | $ | $ |
| Pest Control | $ | $ | $ | $ | $ |
| Legal & Eviction Reserve | $ | $ | $ | $ | $ |
| Accounting | $ | $ | $ | $ | $ |
| Advertising (vacancy) | $ | $ | $ | $ | $ |
| Miscellaneous | $ | $ | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** | **$** | **$** |

`FORMULA (Variance): =Actual - Estimated`

---

## CapEx Reserve Calculator

| Component | Remaining Life (yrs) | Replacement Cost | Annual Reserve | Monthly Reserve |
|-----------|:--------------------:|:----------------:|--------------:|--------------:|
| Roof | | $ | $ | $ |
| HVAC System | | $ | $ | $ |
| Water Heater | | $ | $ | $ |
| Appliances | | $ | $ | $ |
| Flooring | | $ | $ | $ |
| Exterior Paint | | $ | $ | $ |
| Plumbing | | $ | $ | $ |
| Electrical | | $ | $ | $ |
| Driveway / Parking | | $ | $ | $ |
| **TOTAL CapEx Reserve** | | | **$** | **$** |

`FORMULA (Annual Reserve): =ReplacementCost / RemainingLifeYears`
`FORMULA (Monthly Reserve): =AnnualReserve / 12`

---

---

# SHEET 4: 10-YEAR PROJECTION

> Long-term returns including appreciation, mortgage paydown, and equity growth.

---

## Assumptions

| Assumption | Value | Notes |
|-----------|------:|-------|
| Annual Rent Increase | % | 2-4% typical |
| Annual Expense Increase | % | 2-3% typical |
| Annual Appreciation Rate | % | 3-5% typical (conservative) |
| Holding Period | years | |

---

## 10-Year Cash Flow Projection

| Year | Gross Rent | Vacancy | Expenses | Mortgage | Net Cash Flow | CoC Return | Equity (Paydown) | Property Value |
|------|----------:|--------:|---------:|---------:|--------------:|---------:|----------------:|--------------:|
| 1 | $ | $ | $ | $ | $ | % | $ | $ |
| 2 | $ | $ | $ | $ | $ | % | $ | $ |
| 3 | $ | $ | $ | $ | $ | % | $ | $ |
| 4 | $ | $ | $ | $ | $ | % | $ | $ |
| 5 | $ | $ | $ | $ | $ | % | $ | $ |
| 6 | $ | $ | $ | $ | $ | % | $ | $ |
| 7 | $ | $ | $ | $ | $ | % | $ | $ |
| 8 | $ | $ | $ | $ | $ | % | $ | $ |
| 9 | $ | $ | $ | $ | $ | % | $ | $ |
| 10 | $ | $ | $ | $ | $ | % | $ | $ |
| **TOTAL** | **$** | **$** | **$** | **$** | **$** | | **$** | |

`FORMULA (Rent Year N): =Year1Rent * (1 + RentIncrease)^(N-1)`
`FORMULA (Expenses Year N): =Year1Expenses * (1 + ExpenseIncrease)^(N-1)`
`FORMULA (Property Value Year N): =PurchasePrice * (1 + AppreciationRate)^N`
`FORMULA (Equity Paydown Year N): =PPMT calculations summed for the year`

---

## Total Return Summary (10-Year Hold)

| Return Component | Amount |
|-----------------|-------:|
| Total Net Cash Flow (10 years) | $ |
| Total Equity from Mortgage Paydown | $ |
| Appreciation Gain (est. sale - purchase) | $ |
| Minus: Selling Costs (6% of sale price) | ($ ) |
| Minus: Capital Gains Tax (est.) | ($ ) |
| **Net Total Profit** | **$** |
| **Total Return on Cash Invested** | **%** |
| **Average Annual Return** | **%** |
| **Internal Rate of Return (IRR)** | **%** |

`FORMULA (Appreciation Gain): =PropertyValue_Year10 - PurchasePrice`
`FORMULA (Total Return): =NetProfit / TotalCashInvested * 100`
`FORMULA (Avg Annual Return): =TotalReturn / HoldingYears`
`FORMULA (IRR): =IRR(CashFlowArray) — include -TotalCashInvested as Year 0`

---

---

# SHEET 5: PROPERTY COMPARISON

> Compare up to 5 properties side by side on every key metric.

---

## Side-by-Side Comparison

| Metric | Property 1 | Property 2 | Property 3 | Property 4 | Property 5 | BEST |
|--------|:----------:|:----------:|:----------:|:----------:|:----------:|:----:|
| **Address** | | | | | | |
| **Purchase Price** | $ | $ | $ | $ | $ | |
| **Down Payment** | $ | $ | $ | $ | $ | |
| **Total Cash Invested** | $ | $ | $ | $ | $ | |
| **Gross Monthly Rent** | $ | $ | $ | $ | $ | |
| **Monthly Mortgage** | $ | $ | $ | $ | $ | |
| **Monthly Expenses** | $ | $ | $ | $ | $ | |
| **Monthly Cash Flow** | $ | $ | $ | $ | $ | Highest |
| **Annual Cash Flow** | $ | $ | $ | $ | $ | Highest |
| **Cash-on-Cash Return** | % | % | % | % | % | Highest |
| **Cap Rate** | % | % | % | % | % | Highest |
| **Gross Rent Multiplier** | x | x | x | x | x | Lowest |
| **DSCR** | x | x | x | x | x | Highest |
| **Break-Even Occupancy** | % | % | % | % | % | Lowest |
| **1% Rule** | % | % | % | % | % | Highest |
| **10-Year Total Return** | % | % | % | % | % | Highest |
| **Neighborhood Grade** | A-F | A-F | A-F | A-F | A-F | |
| **Condition** | 1-10 | 1-10 | 1-10 | 1-10 | 1-10 | |
| **Rehab Needed?** | Y/N | Y/N | Y/N | Y/N | Y/N | |
| **OVERALL RANK** | # | # | # | # | # | |

`FORMULA (BEST for Cash Flow): =MAX(CashFlow_Row)`
`FORMULA (BEST for GRM): =MIN(GRM_Row)`
`FORMULA (BEST for Break-Even): =MIN(BreakEven_Row)`

---

## Scoring Matrix

| Criteria | Weight | Prop 1 Score | Prop 2 Score | Prop 3 Score | Prop 4 Score | Prop 5 Score |
|----------|:------:|:----------:|:----------:|:----------:|:----------:|:----------:|
| Cash-on-Cash Return | 25% | /10 | /10 | /10 | /10 | /10 |
| Monthly Cash Flow | 20% | /10 | /10 | /10 | /10 | /10 |
| Location / Tenant Quality | 20% | /10 | /10 | /10 | /10 | /10 |
| Condition / Rehab Needed | 15% | /10 | /10 | /10 | /10 | /10 |
| Appreciation Potential | 10% | /10 | /10 | /10 | /10 | /10 |
| Ease of Management | 10% | /10 | /10 | /10 | /10 | /10 |
| **Weighted Total** | **100%** | | | | | |

`FORMULA (Weighted Total): =SUMPRODUCT(Weights, Scores)`

---

---

# SHEET 6: MORTGAGE AMORTIZATION

> Full amortization schedule showing principal vs. interest breakdown and equity growth.

---

## Loan Summary

| Field | Value |
|-------|------:|
| Loan Amount | $ |
| Interest Rate | % |
| Term (months) | |
| Monthly Payment (P&I) | $ |
| Total Interest Over Life | $ |
| Total Cost of Loan | $ |

`FORMULA (Monthly Payment): =PMT(Rate/12, TermMonths, -LoanAmount)`
`FORMULA (Total Interest): =(MonthlyPayment * TermMonths) - LoanAmount`

---

## Amortization Schedule (First 24 Months Sample)

| Payment # | Date | Payment | Principal | Interest | Remaining Balance | Cumulative Interest | Equity % |
|:---------:|------|--------:|----------:|---------:|------------------:|--------------------:|---------:|
| 1 | | $ | $ | $ | $ | $ | % |
| 2 | | $ | $ | $ | $ | $ | % |
| 3 | | $ | $ | $ | $ | $ | % |
| 4 | | $ | $ | $ | $ | $ | % |
| 5 | | $ | $ | $ | $ | $ | % |
| 6 | | $ | $ | $ | $ | $ | % |
| 12 | | $ | $ | $ | $ | $ | % |
| 24 | | $ | $ | $ | $ | $ | % |
| 36 | | $ | $ | $ | $ | $ | % |
| 60 | | $ | $ | $ | $ | $ | % |
| 120 | | $ | $ | $ | $ | $ | % |
| 180 | | $ | $ | $ | $ | $ | % |
| 240 | | $ | $ | $ | $ | $ | % |
| 360 | | $ | $ | $ | $ | $ | % |

`FORMULA (Interest Portion): =RemainingBalance * (Rate/12)`
`FORMULA (Principal Portion): =MonthlyPayment - InterestPortion`
`FORMULA (Remaining Balance): =PreviousBalance - PrincipalPortion`
`FORMULA (Equity %): =(PurchasePrice - RemainingBalance) / PurchasePrice * 100`

---

## Annual Equity Summary

| Year | Principal Paid | Interest Paid | Remaining Balance | Equity (loan paydown only) | Equity + Appreciation |
|:----:|---------------:|--------------:|------------------:|---------------------------:|----------------------:|
| 1 | $ | $ | $ | $ | $ |
| 2 | $ | $ | $ | $ | $ |
| 3 | $ | $ | $ | $ | $ |
| 4 | $ | $ | $ | $ | $ |
| 5 | $ | $ | $ | $ | $ |
| 10 | $ | $ | $ | $ | $ |
| 15 | $ | $ | $ | $ | $ |
| 20 | $ | $ | $ | $ | $ |
| 25 | $ | $ | $ | $ | $ |
| 30 | $ | $ | $ | $ | $ |

`FORMULA (Annual Principal): =PPMT sum for 12 months`
`FORMULA (Equity + Appreciation): =LoanEquity + (PropertyValue_YearN - PurchasePrice)`

---

---

# FORMULA REFERENCE GUIDE

---

## Core Investment Formulas

**Monthly Mortgage (P&I):**
```
=PMT(AnnualRate/12, TermYears*12, -LoanAmount)
```

**Cash-on-Cash Return:**
```
=AnnualCashFlow / TotalCashInvested * 100
```

**Cap Rate:**
```
=NOI / PurchasePrice * 100
```

**Gross Rent Multiplier:**
```
=PurchasePrice / AnnualGrossRent
```

**Debt Service Coverage Ratio:**
```
=NOI / AnnualDebtService
```

**Break-Even Occupancy:**
```
=(OperatingExpenses + DebtService) / GrossScheduledIncome * 100
```

**Net Operating Income:**
```
=EffectiveGrossIncome - OperatingExpenses
```

**Internal Rate of Return (10-year):**
```
=IRR({-CashInvested, Year1CF, Year2CF, ..., Year10CF+SaleProceeds})
```

## Conditional Formatting

**Positive cash flow (green):**
```
=CashFlow > 0
```

**Negative cash flow (red):**
```
=CashFlow < 0
```

**CoC Return above 8% (green):**
```
=CoCReturn > 0.08
```

**DSCR below 1.25 (red warning):**
```
=DSCR < 1.25
```

**Best value in comparison (bold green):**
```
=Value = MAX(Row) or MIN(Row) depending on metric
```

---

> **NOTE:** This calculator uses standard real estate investment formulas. Always verify property tax amounts with the county assessor, insurance quotes with your agent, and rental rates with local comps (Rentometer, Zillow Rent Zestimate, or property manager input). The 50% Rule (expenses eat ~50% of gross rent) is a quick screening tool, not a substitute for detailed analysis. Always run conservative numbers — the best deals still work when you assume the worst.
