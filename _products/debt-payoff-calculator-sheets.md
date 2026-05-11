# Debt Payoff Calculator — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Compare snowball vs. avalanche strategies, see your exact debt-free date, and track every payment along the way.

---

> **SETUP GUIDE — Get Running in 15 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 6 tabs/sheets and name them: Debt List, Snowball Plan, Avalanche Plan, Payment Schedule, Interest Saved, Milestones
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Fill in your debt details on the Debt List sheet first — everything else auto-calculates
> 6. Choose your strategy (snowball or avalanche) and follow that sheet's payment order
>
> **Tip:** Update balances on the 1st of each month. Watching numbers shrink is the best motivation.

---

---

# SHEET 1: DEBT LIST

> Enter every debt you owe. This is the master data source for all other sheets.

---

## Column Headers

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Debt Name** | **Type** | **Current Balance** | **Interest Rate (APR)** | **Minimum Payment** | **Extra Payment** | **Total Monthly Payment** | **Monthly Interest** | **Payoff Date (est.)** |

## Type (Dropdown Values)
- Credit Card
- Student Loan
- Auto Loan
- Personal Loan
- Medical Debt
- Mortgage
- HELOC
- Other

---

## Formulas

`FORMULA (G2): =E2+F2`
Total Monthly Payment = Minimum Payment + Extra Payment

`FORMULA (H2): =C2*(D2/12)`
Monthly Interest = Current Balance * (APR / 12)

`FORMULA (I2): =EDATE(TODAY(), NPER(D2/12, -G2, C2))`
Estimated Payoff Date using NPER to find number of months remaining

`FORMULA (Alternative I2 if EDATE unavailable): =TODAY() + NPER(D2/12, -G2, C2) * 30`

---

## Sample Data

| Debt Name | Type | Balance | APR | Min Payment | Extra | Total | Monthly Int | Payoff Date |
|-----------|------|---------|-----|-------------|-------|-------|-------------|-------------|
| Chase Visa | Credit Card | $8,200 | 22.99% | $205 | $0 | $205 | $157.08 | 2031-03-15 |
| Sallie Mae | Student Loan | $24,500 | 6.80% | $285 | $0 | $285 | $138.83 | 2034-08-01 |
| Honda Civic | Auto Loan | $12,300 | 5.49% | $340 | $0 | $340 | $56.28 | 2029-06-01 |
| Best Buy Card | Credit Card | $1,800 | 26.99% | $55 | $0 | $55 | $40.49 | 2028-11-01 |
| Medical Bill | Medical Debt | $3,200 | 0.00% | $150 | $0 | $150 | $0.00 | 2027-09-01 |

---

## Summary Section (Below Data)

| Metric | Value |
|--------|-------|
| **Total Debt** | $ |
| **Total Minimum Payments** | $ |
| **Total Extra Payment Budget** | $ |
| **Weighted Average Interest Rate** | % |
| **Highest Interest Rate** | % |
| **Smallest Balance** | $ |

`FORMULA (Total Debt): =SUM(C2:C20)`
`FORMULA (Weighted Avg Rate): =SUMPRODUCT(C2:C20, D2:D20) / SUM(C2:C20)`
`FORMULA (Highest Rate): =MAX(D2:D20)`
`FORMULA (Smallest Balance): =MIN(IF(C2:C20>0, C2:C20))`
(Use Ctrl+Shift+Enter for array formula on smallest balance)

---

---

# SHEET 2: SNOWBALL PLAN

> Debts ordered smallest balance to largest. Pay minimums on everything, throw all extra money at the smallest debt first. When it's paid off, roll that payment into the next smallest.

---

## Snowball Order (Auto-Sorted)

| Priority | Debt Name | Balance | APR | Min Payment | Snowball Payment | Months to Payoff | Interest Paid | Payoff Date |
|----------|-----------|---------|-----|-------------|-----------------|------------------|---------------|-------------|
| 1 | Best Buy Card | $1,800 | 26.99% | $55 | $255 | 8 | $139.42 | 2027-01-15 |
| 2 | Medical Bill | $3,200 | 0.00% | $150 | $405 | 8 | $0.00 | 2027-09-15 |
| 3 | Chase Visa | $8,200 | 22.99% | $205 | $610 | 15 | $1,341.28 | 2028-12-15 |
| 4 | Honda Civic | $12,300 | 5.49% | $340 | $950 | 14 | $482.17 | 2030-02-15 |
| 5 | Sallie Mae | $24,500 | 6.80% | $285 | $1,235 | 22 | $1,802.43 | 2031-12-15 |

---

## Snowball Payment Logic

The "Snowball Payment" column works as follows:
- Debt #1 gets: its minimum + ALL available extra payment budget
- Once Debt #1 is paid off, Debt #2 gets: its minimum + Debt #1's full payment
- Once Debt #2 is paid off, Debt #3 gets: its minimum + Debt #1's payment + Debt #2's payment
- The payment "snowballs" as each debt is eliminated

`FORMULA (Snowball Payment for Debt #1): =E2 + ExtraBudget`
`FORMULA (Snowball Payment for Debt #2): =E3 + G2_TotalPayment (after Debt 1 paid)`
`FORMULA (Months to Payoff): =NPER(D2/12, -F2, C2)`
`FORMULA (Interest Paid): =(F2 * Months) - C2`
`FORMULA (Payoff Date): =EDATE(PreviousDebtPayoffDate, MonthsToPayoff)`

---

## Snowball Summary

| Metric | Value |
|--------|-------|
| Total Months to Debt-Free | |
| Total Interest Paid (Snowball) | $ |
| Estimated Debt-Free Date | |
| Number of Debts | |

`FORMULA (Total Months): Sum of sequential months (not parallel — each debt starts when previous ends)`
`FORMULA (Total Interest): =SUM(H2:H20)`

---

---

# SHEET 3: AVALANCHE PLAN

> Debts ordered highest interest rate to lowest. Pay minimums on everything, throw all extra money at the highest-rate debt first. Mathematically optimal — saves the most money.

---

## Avalanche Order (Auto-Sorted)

| Priority | Debt Name | Balance | APR | Min Payment | Avalanche Payment | Months to Payoff | Interest Paid | Payoff Date |
|----------|-----------|---------|-----|-------------|------------------|------------------|---------------|-------------|
| 1 | Best Buy Card | $1,800 | 26.99% | $55 | $255 | 8 | $139.42 | 2027-01-15 |
| 2 | Chase Visa | $8,200 | 22.99% | $205 | $460 | 21 | $1,087.53 | 2028-10-15 |
| 3 | Sallie Mae | $24,500 | 6.80% | $285 | $745 | 39 | $2,844.19 | 2032-01-15 |
| 4 | Honda Civic | $12,300 | 5.49% | $340 | $1,085 | 12 | $356.82 | 2033-01-15 |
| 5 | Medical Bill | $3,200 | 0.00% | $150 | $1,235 | 3 | $0.00 | 2033-04-15 |

---

## Avalanche Payment Logic

Same snowball concept but debts are ordered by interest rate (highest first):
- Debt #1 (highest APR) gets: its minimum + ALL available extra payment budget
- When Debt #1 is eliminated, its full payment rolls to Debt #2 (next highest APR)
- Continue until all debts are paid

`FORMULA (Sort): =SORT(DebtList, APR_Column, FALSE)`
`FORMULA (Avalanche Payment): Same rolling logic as snowball, different order`

---

## Avalanche Summary

| Metric | Value |
|--------|-------|
| Total Months to Debt-Free | |
| Total Interest Paid (Avalanche) | $ |
| Estimated Debt-Free Date | |
| Number of Debts | |

---

---

# SHEET 4: PAYMENT SCHEDULE

> Month-by-month payment schedule showing exactly what to pay on each debt, remaining balances, and running totals.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Month #** | **Date** | **Debt Name** | **Payment Amount** | **Interest Portion** | **Principal Portion** | **Remaining Balance** | **Cumulative Paid** | **Cumulative Interest** | **Cumulative Principal** |

---

## Formulas

`FORMULA (B2): =EDATE(StartDate, A2-1)`
`FORMULA (E2): =PreviousBalance * (APR/12)`
Interest Portion = Last month's remaining balance * monthly rate

`FORMULA (F2): =D2 - E2`
Principal Portion = Payment - Interest

`FORMULA (G2): =PreviousBalance - F2`
Remaining Balance = Previous Balance - Principal Paid

`FORMULA (H2): =H1 + D2`
Cumulative Paid = Running total of all payments

`FORMULA (I2): =I1 + E2`
Cumulative Interest = Running total of interest paid

`FORMULA (J2): =J1 + F2`
Cumulative Principal = Running total of principal paid

---

## Sample Schedule (First 6 Months — Best Buy Card as Priority #1)

| Month | Date | Debt | Payment | Interest | Principal | Balance | Cum Paid | Cum Int | Cum Prin |
|-------|------|------|---------|----------|-----------|---------|----------|---------|----------|
| 1 | 2026-06-01 | Best Buy Card | $255.00 | $40.49 | $214.51 | $1,585.49 | $255.00 | $40.49 | $214.51 |
| 2 | 2026-07-01 | Best Buy Card | $255.00 | $35.66 | $219.34 | $1,366.15 | $510.00 | $76.15 | $433.85 |
| 3 | 2026-08-01 | Best Buy Card | $255.00 | $30.73 | $224.27 | $1,141.88 | $765.00 | $106.88 | $658.12 |
| 4 | 2026-09-01 | Best Buy Card | $255.00 | $25.68 | $229.32 | $912.56 | $1,020.00 | $132.56 | $887.44 |
| 5 | 2026-10-01 | Best Buy Card | $255.00 | $20.53 | $234.47 | $678.09 | $1,275.00 | $153.09 | $1,121.91 |
| 6 | 2026-11-01 | Best Buy Card | $255.00 | $15.25 | $239.75 | $438.34 | $1,530.00 | $168.34 | $1,361.66 |

---

## End-of-Debt Rollover Row

When a debt reaches $0, insert a note row:
| | | **DEBT PAID OFF** | | | | $0.00 | | | |

Next row begins the next priority debt with the rolled-over payment amount.

---

---

# SHEET 5: INTEREST SAVED

> Compare strategies side by side. See exactly how much money and time you save.

---

## Strategy Comparison

| Metric | Minimum Only | Snowball | Avalanche | Best Choice |
|--------|-------------|----------|-----------|-------------|
| Total Interest Paid | $ | $ | $ | |
| Months to Debt-Free | | | | |
| Debt-Free Date | | | | |
| Interest Saved vs. Minimums | — | $ | $ | |
| Time Saved vs. Minimums | — | months | months | |
| First Debt Eliminated | — | month # | month # | |

`FORMULA (Interest Saved): =MinimumOnlyInterest - StrategyInterest`
`FORMULA (Time Saved): =MinimumOnlyMonths - StrategyMonths`
`FORMULA (Best Choice): =IF(AvalancheInterest < SnowballInterest, "Avalanche", "Snowball")`

---

## What-If Scenarios

| Extra Monthly Payment | Snowball Debt-Free | Avalanche Debt-Free | Interest Saved (Avalanche) |
|-----------------------|-------------------|---------------------|---------------------------|
| $0 (minimums only) | | | — |
| $100 | | | $ |
| $200 | | | $ |
| $300 | | | $ |
| $500 | | | $ |
| $750 | | | $ |
| $1,000 | | | $ |

`FORMULA: Recalculate NPER for each debt with new payment amounts, sum sequentially`

---

## Interest Breakdown by Debt

| Debt Name | Interest (Min Only) | Interest (Snowball) | Interest (Avalanche) | Savings (Best) |
|-----------|--------------------|--------------------|---------------------|----------------|
| Best Buy Card | $ | $ | $ | $ |
| Chase Visa | $ | $ | $ | $ |
| Medical Bill | $ | $ | $ | $ |
| Honda Civic | $ | $ | $ | $ |
| Sallie Mae | $ | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** | **$** |

---

## Annual Interest Cost (Current)

| Year | Interest Paid | Principal Paid | Remaining Balance |
|------|--------------|---------------|-------------------|
| Year 1 | $ | $ | $ |
| Year 2 | $ | $ | $ |
| Year 3 | $ | $ | $ |
| Year 4 | $ | $ | $ |
| Year 5 | $ | $ | $ |

---

---

# SHEET 6: MILESTONES

> Celebrate every win. Debt payoff is a marathon — track your progress and reward yourself.

---

## Milestone Tracker

| Milestone | Target | Date Achieved | Reward | Notes |
|-----------|--------|---------------|--------|-------|
| First $1,000 paid off | $1,000 principal | | | |
| First debt eliminated | 1 debt at $0 | | | |
| 25% of total debt gone | $ | | | |
| Second debt eliminated | 2 debts at $0 | | | |
| 50% of total debt gone | $ | | | |
| Third debt eliminated | 3 debts at $0 | | | |
| 75% of total debt gone | $ | | | |
| Only 1 debt remaining | | | | |
| Under $10,000 total | $10,000 | | | |
| Under $5,000 total | $5,000 | | | |
| **DEBT FREE** | $0 | | | |

`FORMULA (25% Target): =SUM(OriginalBalances) * 0.25`
`FORMULA (50% Target): =SUM(OriginalBalances) * 0.50`

---

## Monthly Progress Log

| Month | Total Balance Start | Total Paid | Principal Paid | Interest Paid | Total Balance End | Debts Remaining | % Paid Off |
|-------|--------------------|-----------:|---------------:|-------------:|-----------------:|----------------:|-----------:|
| Month 1 | $ | $ | $ | $ | $ | | % |
| Month 2 | $ | $ | $ | $ | $ | | % |
| Month 3 | $ | $ | $ | $ | $ | | % |
| Month 4 | $ | $ | $ | $ | $ | | % |
| Month 5 | $ | $ | $ | $ | $ | | % |
| Month 6 | $ | $ | $ | $ | $ | | % |
| Month 7 | $ | $ | $ | $ | $ | | % |
| Month 8 | $ | $ | $ | $ | $ | | % |
| Month 9 | $ | $ | $ | $ | $ | | % |
| Month 10 | $ | $ | $ | $ | $ | | % |
| Month 11 | $ | $ | $ | $ | $ | | % |
| Month 12 | $ | $ | $ | $ | $ | | % |

`FORMULA (% Paid Off): =(OriginalTotal - CurrentBalance) / OriginalTotal * 100`

---

## Motivation Dashboard

| Metric | Value |
|--------|-------|
| Original Total Debt | $ |
| Current Total Debt | $ |
| Total Paid Off So Far | $ |
| Percentage Complete | % |
| Days Since Starting | |
| Average Paid Per Month | $ |
| Debts Fully Eliminated | / total |
| Estimated Debt-Free Date | |
| Days Remaining (est.) | |

`FORMULA (Days Since Starting): =TODAY() - StartDate`
`FORMULA (Average Per Month): =TotalPaid / DATEDIF(StartDate, TODAY(), "M")`
`FORMULA (Days Remaining): =DebtFreeDate - TODAY()`

---

---

# FORMULA REFERENCE GUIDE

---

## Core Financial Formulas

**Number of Periods (months to payoff):**
```
=NPER(rate/12, -payment, balance)
```

**Monthly Interest:**
```
=Balance * (APR / 12)
```

**Principal Portion of Payment:**
```
=Payment - (Balance * APR / 12)
```

**New Balance After Payment:**
```
=OldBalance - PrincipalPortion
```

**Total Interest Over Life of Debt (minimums only):**
```
=(MinPayment * NPER(APR/12, -MinPayment, Balance)) - Balance
```

## Snowball Sort

**Sort debts by balance ascending:**
```
=SORT(A2:I20, 3, TRUE)
```

## Avalanche Sort

**Sort debts by APR descending:**
```
=SORT(A2:I20, 4, FALSE)
```

## Rolling Payment (Snowball/Avalanche)

**Payment for current priority debt:**
```
=MinPayment + ExtraBudget + SUM(FreedUpPayments_from_eliminated_debts)
```

## Conditional Formatting Rules

**Debt paid off (green background):**
```
=G2 <= 0
```

**High interest rate (red text for APR > 20%):**
```
=D2 > 0.20
```

**Milestone achieved (gold background):**
```
=C2 <> ""
```
(Apply to Date Achieved column on Milestones sheet)

**Progress bar (in-cell using REPT):**
```
=REPT("=", ROUND(PercentPaid/10, 0)) & REPT("-", 10-ROUND(PercentPaid/10, 0))
```

---

> **NOTE:** This calculator supports up to 20 debts. For the snowball/avalanche comparison to be accurate, enter ALL debts and their true minimum payments. The "Extra Payment" on the Debt List sheet is your total discretionary amount available above all minimums — it gets allocated by the chosen strategy automatically. Update balances monthly for the most accurate projections.
