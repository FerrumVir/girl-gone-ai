# Monthly Budget Dashboard for Couples — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Manage your shared finances while keeping individual spending autonomy.

---

> **SETUP GUIDE — Get Running in 20 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 8 tabs/sheets and name them: Monthly Budget, Shared Expenses, Individual Allowances, Savings Goals, Debt Payoff, Bills Calendar, Net Worth, Dashboard
> 3. Copy each section below into its corresponding sheet
> 4. Enter the formulas as documented (all formulas are marked with `FORMULA:`)
> 5. Fill in your combined household income first, then fixed expenses
> 6. Decide on your split method (50/50, proportional, or custom) and enter it in the Budget sheet
>
> **Tip:** Have a monthly "money date" — sit down together on the 1st to review last month and plan the next. Keep it positive and goal-focused.

---

---

# SHEET 1: MONTHLY BUDGET

> Your master budget showing combined income, shared expenses, and allocation to each partner.

---

## Household Income

| Source | Partner A | Partner B | Combined |
|--------|-----------|-----------|----------|
| Salary/Wages (after tax) | $ | $ | $ |
| Side Income | $ | $ | $ |
| Investment Income | $ | $ | $ |
| Other Income | $ | $ | $ |
| **Total Income** | **$** | **$** | **$** |

`FORMULA: Combined = Partner A + Partner B`

---

## Split Method

| Setting | Value |
|---------|-------|
| **Split Method** | [ ] 50/50 [ ] Proportional [ ] Custom |
| **Partner A Contribution %** | % |
| **Partner B Contribution %** | % |
| **Partner A Monthly Contribution** | $ |
| **Partner B Monthly Contribution** | $ |

`FORMULA (Proportional): Partner A % = Partner A Income / Combined Income * 100`
`FORMULA: Partner A Contribution = Total Shared Expenses * Partner A %`

---

## Monthly Budget Summary

| Category | Budgeted | Actual | Remaining | Status |
|----------|----------|--------|-----------|--------|
| **SHARED EXPENSES** | | | | |
| Housing (Rent/Mortgage) | $ | $ | $ | |
| Utilities | $ | $ | $ | |
| Groceries | $ | $ | $ | |
| Transportation | $ | $ | $ | |
| Insurance | $ | $ | $ | |
| Subscriptions (shared) | $ | $ | $ | |
| Dining Out (together) | $ | $ | $ | |
| Household Items | $ | $ | $ | |
| Pet Care | $ | $ | $ | |
| **Total Shared** | **$** | **$** | **$** | |
| | | | | |
| **SAVINGS & DEBT** | | | | |
| Emergency Fund | $ | $ | $ | |
| Savings Goal 1 | $ | $ | $ | |
| Savings Goal 2 | $ | $ | $ | |
| Debt Payment (extra) | $ | $ | $ | |
| **Total Savings/Debt** | **$** | **$** | **$** | |
| | | | | |
| **INDIVIDUAL ALLOWANCES** | | | | |
| Partner A Personal | $ | $ | $ | |
| Partner B Personal | $ | $ | $ | |
| **Total Individual** | **$** | **$** | **$** | |
| | | | | |
| **GRAND TOTAL** | **$** | **$** | **$** | |
| **Leftover/Buffer** | | | **$** | |

`FORMULA: Remaining = Budgeted - Actual`
`FORMULA: Status = IF(Actual > Budgeted, "OVER", IF(Actual > Budgeted*0.9, "WATCH", "OK"))`
`FORMULA: Leftover = Combined Income - Grand Total Actual`

---

---

# SHEET 2: SHARED EXPENSES

> Log every shared expense. Both partners enter transactions here.

---

## Column Headers

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| **Date** | **Description** | **Category** | **Amount** | **Paid By** | **Split** | **Partner A Owes** | **Partner B Owes** |

## Category (Dropdown)
- Housing
- Utilities
- Groceries
- Transportation
- Insurance
- Subscriptions
- Dining Out
- Household Items
- Pet Care
- Medical (shared)
- Gifts (shared)
- Travel (shared)
- Other Shared

## Paid By (Dropdown)
- Partner A
- Partner B
- Joint Account

## Split (Dropdown)
- 50/50
- Proportional
- Partner A 100%
- Partner B 100%
- Custom

`FORMULA (50/50): Partner A Owes = IF(E2="Partner B", D2*0.5, 0)`
`FORMULA (50/50): Partner B Owes = IF(E2="Partner A", D2*0.5, 0)`
`FORMULA (Proportional): Partner A Owes = IF(E2="Partner B", D2*PartnerA%, 0)`

---

## Sample Entries

| Date | Description | Category | Amount | Paid By | Split | A Owes | B Owes |
|------|-------------|----------|--------|---------|-------|--------|--------|
| 2026-01-03 | Whole Foods groceries | Groceries | $127.43 | Partner A | 50/50 | $0 | $63.72 |
| 2026-01-05 | Electric bill | Utilities | $89.00 | Joint Account | N/A | $0 | $0 |
| 2026-01-07 | Date night dinner | Dining Out | $78.50 | Partner B | 50/50 | $39.25 | $0 |
| 2026-01-10 | Dog food & vet | Pet Care | $215.00 | Partner A | Proportional | $0 | $92.45 |

---

## Monthly Settlement

| | Partner A | Partner B |
|--|-----------|-----------|
| Total Paid for Shared Expenses | $ | $ |
| Should Have Paid (per split) | $ | $ |
| **Difference (+ = overpaid)** | **$** | **$** |
| **Settlement:** | [Partner X owes Partner Y: $___] | |

`FORMULA: Settlement = ABS(Difference_A) (paid from underpayer to overpayer)`

---

---

# SHEET 3: INDIVIDUAL ALLOWANCES

> Each partner's personal spending — no judgment zone.

---

## Partner A — Personal Budget

| Category | Monthly Allowance | Spent | Remaining |
|----------|------------------|-------|-----------|
| Clothing & Shopping | $ | $ | $ |
| Hobbies & Entertainment | $ | $ | $ |
| Personal Care | $ | $ | $ |
| Dining/Coffee (solo) | $ | $ | $ |
| Gifts (personal) | $ | $ | $ |
| Subscriptions (personal) | $ | $ | $ |
| Other | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** |

---

## Partner B — Personal Budget

| Category | Monthly Allowance | Spent | Remaining |
|----------|------------------|-------|-----------|
| Clothing & Shopping | $ | $ | $ |
| Hobbies & Entertainment | $ | $ | $ |
| Personal Care | $ | $ | $ |
| Dining/Coffee (solo) | $ | $ | $ |
| Gifts (personal) | $ | $ | $ |
| Subscriptions (personal) | $ | $ | $ |
| Other | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** |

`FORMULA: Remaining = Monthly Allowance - Spent`

---

## Personal Spending Log

| Date | Partner | Description | Category | Amount |
|------|---------|-------------|----------|--------|
| | A/B | | | $ |
| | A/B | | | $ |
| | A/B | | | $ |

---

---

# SHEET 4: SAVINGS GOALS

> Track progress toward shared and individual financial goals.

---

## Active Savings Goals

| Goal | Type | Target Amount | Current Balance | Monthly Contribution | Progress % | Months to Goal | Target Date | On Track? |
|------|------|--------------|----------------|---------------------|-----------|---------------|-------------|-----------|
| Emergency Fund | Shared | $ | $ | $ | % | | | |
| Vacation Fund | Shared | $ | $ | $ | % | | | |
| House Down Payment | Shared | $ | $ | $ | % | | | |
| Wedding Fund | Shared | $ | $ | $ | % | | | |
| Partner A: [Goal] | Individual | $ | $ | $ | % | | | |
| Partner B: [Goal] | Individual | $ | $ | $ | % | | | |

`FORMULA: Progress % = Current Balance / Target Amount * 100`
`FORMULA: Months to Goal = (Target Amount - Current Balance) / Monthly Contribution`
`FORMULA: On Track = IF(Target Date - TODAY() > Months to Goal * 30, "YES", "BEHIND")`

---

## Monthly Savings Tracker

| Month | Emergency | Vacation | Down Payment | Wedding | Partner A | Partner B | **Total Saved** |
|-------|-----------|----------|-------------|---------|-----------|-----------|-----------------|
| January | $ | $ | $ | $ | $ | $ | $ |
| February | $ | $ | $ | $ | $ | $ | $ |
| March | $ | $ | $ | $ | $ | $ | $ |
| April | $ | $ | $ | $ | $ | $ | $ |
| May | $ | $ | $ | $ | $ | $ | $ |
| June | $ | $ | $ | $ | $ | $ | $ |
| July | $ | $ | $ | $ | $ | $ | $ |
| August | $ | $ | $ | $ | $ | $ | $ |
| September | $ | $ | $ | $ | $ | $ | $ |
| October | $ | $ | $ | $ | $ | $ | $ |
| November | $ | $ | $ | $ | $ | $ | $ |
| December | $ | $ | $ | $ | $ | $ | $ |
| **TOTAL** | **$** | **$** | **$** | **$** | **$** | **$** | **$** |

---

## Savings Rate

| Metric | Value |
|--------|-------|
| Combined Monthly Income | $ |
| Total Monthly Savings | $ |
| **Savings Rate %** | **%** |
| Recommended Minimum (20%) | $ |
| Gap (+ = exceeding, - = below) | $ |

`FORMULA: Savings Rate = Total Savings / Combined Income * 100`

---

---

# SHEET 5: DEBT PAYOFF

> Track all debts and plan your payoff strategy.

---

## Debt Overview

| Debt Name | Type | Balance | Interest Rate | Min Payment | Extra Payment | Total Payment | Payoff Date (est.) | Whose Debt? |
|-----------|------|---------|--------------|-------------|--------------|---------------|--------------------|-------------|
| | Credit Card / Student / Auto / Mortgage / Personal / Medical | $ | % | $ | $ | $ | | Shared / A / B |
| | | $ | % | $ | $ | $ | | |
| | | $ | % | $ | $ | $ | | |
| | | $ | % | $ | $ | $ | | |
| | | $ | % | $ | $ | $ | | |
| **TOTAL** | | **$** | | **$** | **$** | **$** | | |

`FORMULA: Total Payment = Min Payment + Extra Payment`
`FORMULA: Payoff Date = complex amortization (use online calculator, enter result)`

---

## Payoff Strategy

| Method | Description | Best For |
|--------|-------------|----------|
| **Avalanche** | Pay highest interest rate first | Saving the most money overall |
| **Snowball** | Pay smallest balance first | Building motivation with quick wins |
| **Hybrid** | Pay off one small debt, then switch to avalanche | Balance of motivation + savings |

**Your Chosen Strategy:** [ ] Avalanche [ ] Snowball [ ] Hybrid

---

## Debt Payoff Tracker (Monthly)

| Month | Debt 1 Balance | Debt 2 Balance | Debt 3 Balance | Debt 4 Balance | Total Debt | Paid Off This Month |
|-------|---------------|---------------|---------------|---------------|-----------|---------------------|
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

---

## Debt-Free Date Projection

| Scenario | Monthly Extra Payment | Projected Debt-Free Date | Total Interest Saved vs. Minimums |
|----------|----------------------|--------------------------|----------------------------------|
| Minimums Only | $0 | | — |
| Current Plan | $ | | $ |
| Aggressive (+$200/mo) | $ | | $ |
| Ultra Aggressive (+$500/mo) | $ | | $ |

---

---

# SHEET 6: BILLS CALENDAR

> Never miss a bill. See what's due and when at a glance.

---

## Monthly Bills Schedule

| Due Date | Bill | Amount | Auto-Pay? | Account | Status | Notes |
|----------|------|--------|-----------|---------|--------|-------|
| 1st | Rent/Mortgage | $ | Yes/No | | Paid/Upcoming | |
| 3rd | Car Insurance | $ | Yes/No | | Paid/Upcoming | |
| 5th | Internet | $ | Yes/No | | Paid/Upcoming | |
| 7th | Streaming (Netflix) | $ | Yes/No | | Paid/Upcoming | |
| 10th | Electric | $ | Yes/No | | Paid/Upcoming | |
| 12th | Phone (Partner A) | $ | Yes/No | | Paid/Upcoming | |
| 12th | Phone (Partner B) | $ | Yes/No | | Paid/Upcoming | |
| 15th | Car Payment | $ | Yes/No | | Paid/Upcoming | |
| 15th | Health Insurance | $ | Yes/No | | Paid/Upcoming | |
| 18th | Water/Trash | $ | Yes/No | | Paid/Upcoming | |
| 20th | Student Loan (A) | $ | Yes/No | | Paid/Upcoming | |
| 22nd | Credit Card | $ | Yes/No | | Paid/Upcoming | |
| 25th | Gas/Energy | $ | Yes/No | | Paid/Upcoming | |
| 28th | Subscriptions | $ | Yes/No | | Paid/Upcoming | |
| | **TOTAL MONTHLY BILLS** | **$** | | | | |

---

## Annual/Semi-Annual Bills

| Month Due | Bill | Amount | Frequency | Notes |
|-----------|------|--------|-----------|-------|
| January | Car Registration | $ | Annual | |
| March | Tax Prep | $ | Annual | |
| April | Taxes Owed | $ | Annual | |
| June | Car Insurance (6-mo) | $ | Semi-Annual | |
| July | Amazon Prime | $ | Annual | |
| November | HOA (annual) | $ | Annual | |
| December | Holiday Budget | $ | Annual | |
| | **TOTAL ANNUAL** | **$** | | |
| | **Monthly Set-Aside** | **$** | | |

`FORMULA: Monthly Set-Aside = Total Annual / 12`

---

---

# SHEET 7: NET WORTH

> Track your combined net worth monthly. Watch it grow over time.

---

## Assets

| Asset | Partner A | Partner B | Joint | Total |
|-------|-----------|-----------|-------|-------|
| **Cash & Savings** | | | | |
| Checking Account(s) | $ | $ | $ | $ |
| Savings Account(s) | $ | $ | $ | $ |
| Emergency Fund | | | $ | $ |
| **Investments** | | | | |
| 401(k) / 403(b) | $ | $ | | $ |
| IRA / Roth IRA | $ | $ | | $ |
| Brokerage Account | $ | $ | $ | $ |
| HSA | $ | $ | | $ |
| **Property** | | | | |
| Home (Zillow est.) | | | $ | $ |
| Vehicle 1 | $ | | | $ |
| Vehicle 2 | | $ | | $ |
| Other Property | | | $ | $ |
| **TOTAL ASSETS** | **$** | **$** | **$** | **$** |

---

## Liabilities

| Liability | Partner A | Partner B | Joint | Total |
|-----------|-----------|-----------|-------|-------|
| Mortgage | | | $ | $ |
| Student Loans | $ | $ | | $ |
| Car Loan 1 | $ | | | $ |
| Car Loan 2 | | $ | | $ |
| Credit Cards | $ | $ | $ | $ |
| Personal Loans | $ | $ | | $ |
| Other Debt | $ | $ | $ | $ |
| **TOTAL LIABILITIES** | **$** | **$** | **$** | **$** |

---

## Net Worth Calculation

| | Amount |
|--|--------|
| Total Assets | $ |
| Total Liabilities | ($ ) |
| **NET WORTH** | **$** |

---

## Monthly Net Worth Tracking

| Month | Total Assets | Total Liabilities | Net Worth | Change | % Change |
|-------|-------------|-------------------|-----------|--------|----------|
| January | $ | $ | $ | $ | % |
| February | $ | $ | $ | $ | % |
| March | $ | $ | $ | $ | % |
| April | $ | $ | $ | $ | % |
| May | $ | $ | $ | $ | % |
| June | $ | $ | $ | $ | % |
| July | $ | $ | $ | $ | % |
| August | $ | $ | $ | $ | % |
| September | $ | $ | $ | $ | % |
| October | $ | $ | $ | $ | % |
| November | $ | $ | $ | $ | % |
| December | $ | $ | $ | $ | % |

`FORMULA: Change = This Month Net Worth - Last Month Net Worth`
`FORMULA: % Change = Change / ABS(Last Month Net Worth) * 100`

---

---

# SHEET 8: DASHBOARD

> At-a-glance financial health for your household.

---

## Monthly Snapshot

| Metric | Value | Status |
|--------|-------|--------|
| Combined Income | $ | |
| Total Expenses (Shared + Individual) | $ | |
| Total Saved This Month | $ | |
| Savings Rate | % | |
| Budget Remaining | $ | |
| Overspent Categories | | |
| Settlement Owed (who owes whom) | | |

---

## Financial Health Indicators

| Indicator | Target | Current | Status |
|-----------|--------|---------|--------|
| Emergency Fund | 3-6 months expenses | $ / $ goal | |
| Savings Rate | 20%+ | % | |
| Debt-to-Income Ratio | <36% | % | |
| Bills Paid On Time | 100% | % | |
| Net Worth Trend | Increasing | | |

`FORMULA: Debt-to-Income = Total Monthly Debt Payments / Combined Monthly Income * 100`

---

## Goals Progress

| Goal | Progress Bar | % Complete | ETA |
|------|-------------|-----------|-----|
| Emergency Fund | [=====-----] | % | |
| Savings Goal 1 | [===-------] | % | |
| Savings Goal 2 | [==========] | % | |
| Debt Free | [======----] | % | |

---

---

# FORMULA REFERENCE GUIDE

---

## Budget Formulas

**Proportional Split:**
```
=Partner_A_Income / Combined_Income
```

**Category Status:**
```
=IF(Actual > Budgeted, "OVER", IF(Actual > Budgeted*0.9, "WATCH", "OK"))
```

**Leftover:**
```
=Combined_Income - SUM(All_Actual_Spending)
```

## Settlement Calculation

**Who Owes Whom:**
```
=IF(A_Paid > A_Should_Pay, "B owes A: $"&TEXT(A_Paid-A_Should_Pay,"0.00"), "A owes B: $"&TEXT(B_Paid-B_Should_Pay,"0.00"))
```

## Savings

**Months to Goal:**
```
=(Target - Current) / Monthly_Contribution
```

**Savings Rate:**
```
=Total_Monthly_Savings / Combined_Income * 100
```

## Net Worth

**Monthly Change:**
```
=This_Month_NW - Last_Month_NW
```

## Conditional Formatting

**Over Budget (red):**
```
=Actual > Budgeted
```

**On Track (green):**
```
=Actual <= Budgeted * 0.9
```

---

> **NOTE:** This budget system is designed for couples who want transparency with autonomy. Customize the split method and individual allowances to match your relationship's financial philosophy. There is no single "right" way to split finances — the best system is one you both agree on and use consistently.
