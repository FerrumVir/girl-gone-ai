# Personal Finance & Budget Planner — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with budget formulas, savings projections, and debt payoff calculations built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Accounts

**Purpose:** Master list of every financial account — checking, savings, credit cards, investments, loans. Provides the foundation for net worth tracking and transaction categorization.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Account Name | Title | Bank + account type (e.g., "Chase Checking", "Vanguard Roth IRA") |
| Institution | Text | Bank or brokerage name |
| Account Type | Select | Checking / Savings / Credit Card / Investment / Retirement / Brokerage / Cash / Crypto / HSA / Loan / Mortgage / Student Loan / Auto Loan / Other |
| Category | Select | Asset / Liability |
| Balance | Number (USD) | Current balance (positive for assets, positive for debt amounts) |
| Last Updated | Date | When balance was last refreshed |
| Interest Rate | Number | APR/APY (percentage) |
| Monthly Payment | Number (USD) | Minimum monthly payment (for liabilities) |
| Credit Limit | Number (USD) | For credit cards |
| Utilization | Formula | `if(and(prop("Account Type") == "Credit Card", prop("Credit Limit") > 0), format(round(prop("Balance") / prop("Credit Limit") * 100)) + "%", "N/A")` |
| Auto-pay | Checkbox | Is this on auto-pay? |
| Due Date | Number | Day of month payment is due (1-31) |
| Purpose | Text | What this account is for (e.g., "Emergency fund", "Vacation savings") |
| Login URL | URL | Quick access to online banking |
| Notes | Text | Account numbers (last 4 only), contact info |
| Tags | Multi-select | Primary / Joint / Business / Tax-Advantaged / High-Yield / Rewards / Inactive |

**Views:**

- **All Accounts** — Table, sorted by Category then Account Type
- **Assets** — Filter: Category = Asset, sorted by Balance descending
- **Liabilities** — Filter: Category = Liability, sorted by Interest Rate descending
- **Net Worth Summary** — Table showing all accounts with balances
- **Credit Cards** — Filter: Account Type = Credit Card, showing Balance, Limit, Utilization
- **Needs Update** — Filter: Last Updated is more than 7 days ago
- **Payment Calendar** — Table, sorted by Due Date

---

### 2. Transactions

**Purpose:** Every income and expense entry. The operational center of your budget — where money flows in and out. Categorized for budget tracking with monthly and category rollups.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Description | Title | What the transaction was (payee or source) |
| Date | Date | Transaction date |
| Type | Select | Income / Expense / Transfer |
| Amount | Number (USD) | Always positive (Type distinguishes direction) |
| Category | Select | Salary / Freelance / Side Hustle / Investment Income / Refund / Housing / Utilities / Groceries / Dining Out / Transportation / Gas / Insurance / Healthcare / Subscriptions / Phone / Internet / Entertainment / Shopping / Clothing / Personal Care / Education / Gifts / Travel / Pets / Kids / Debt Payment / Savings Transfer / Investment Transfer / Charity / Taxes / Misc |
| Budget Bucket | Select | Needs / Wants / Savings-Investments / Income |
| Account | Relation | -> Accounts database |
| Account Name | Rollup | From Account relation |
| Payment Method | Select | Debit / Credit Card / Cash / Check / Auto-Pay / Transfer / Venmo / Zelle |
| Recurring | Checkbox | Is this a regular recurring transaction? |
| Frequency | Select | Weekly / Bi-weekly / Monthly / Quarterly / Semi-annual / Annual / One-time |
| Planned | Checkbox | Was this budgeted/expected? |
| Essential | Checkbox | Is this a true need vs. want? |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")` |
| Year | Formula | `formatDate(prop("Date"), "YYYY")` |
| Day of Week | Formula | `formatDate(prop("Date"), "dddd")` |
| Tax Deductible | Checkbox | Relevant for tax filing |
| Receipt | Files & media | Photo of receipt |
| Notes | Text | Additional context |
| Tags | Multi-select | Impulse / Planned / Negotiable / Fixed / Variable / One-time / Reimbursable |

**Views:**

- **All Transactions** — Table, sorted by Date descending
- **This Month** — Filter: Date is current month, sorted by Date descending
- **Income** — Filter: Type = Income, sorted by Date descending
- **Expenses** — Filter: Type = Expense, sorted by Date descending
- **By Category** — Table, grouped by Category (with sum of Amount)
- **By Month** — Table, grouped by Month
- **Recurring** — Filter: Recurring = true, sorted by Category
- **50/30/20 View** — Table, grouped by Budget Bucket, filtered to Type = Expense, current month
- **Unplanned Spending** — Filter: Planned = false AND Type = Expense (budget busters)
- **Tax Deductible** — Filter: Tax Deductible = true
- **Calendar** — Calendar view by Date
- **Large Expenses** — Filter: Amount > $100 AND Type = Expense, sorted by Amount descending
- **By Account** — Table, grouped by Account Name

---

### 3. Monthly Budgets

**Purpose:** Monthly budget planning and actual-vs-planned tracking. One entry per category per month. Set your budget at the start of each month, then compare against actual spending as the month progresses.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Budget Line | Title | "[Month] — [Category]" (e.g., "May 2026 — Groceries") |
| Month | Select | January / February / March / April / May / June / July / August / September / October / November / December |
| Year | Select | 2025 / 2026 / 2027 |
| Category | Select | Housing / Utilities / Groceries / Dining Out / Transportation / Gas / Insurance / Healthcare / Subscriptions / Phone / Internet / Entertainment / Shopping / Clothing / Personal Care / Education / Gifts / Travel / Pets / Kids / Debt Payment / Savings / Investment / Charity / Misc |
| Budget Bucket | Select | Needs / Wants / Savings-Investments |
| Budgeted | Number (USD) | How much you planned to spend |
| Actual | Number (USD) | How much you actually spent (update throughout month) |
| Variance | Formula | `prop("Budgeted") - prop("Actual")` |
| Variance % | Formula | `if(prop("Budgeted") == 0, 0, round((prop("Actual") - prop("Budgeted")) / prop("Budgeted") * 100))` |
| Status | Formula | `if(prop("Actual") == 0, "No spend yet", if(prop("Variance") < 0, "Over Budget", if(prop("Variance") == 0, "On Budget", if(prop("Actual") / prop("Budgeted") > 0.85, "Almost at limit", "On Track"))))` |
| Fixed/Variable | Select | Fixed / Variable / Semi-variable |
| Notes | Text | Adjustments, unusual expenses, context |

**Views:**

- **This Month** — Filter: current month + year, sorted by Budget Bucket then Category
- **Over Budget** — Filter: Status = "Over Budget"
- **By Bucket (50/30/20)** — Table, grouped by Budget Bucket, showing sum of Budgeted and Actual
- **Monthly Comparison** — Table, same category across months (for trend spotting)
- **All Months** — Table, grouped by Month + Year
- **Fixed Costs** — Filter: Fixed/Variable = Fixed
- **Variable Costs** — Filter: Fixed/Variable = Variable (where you have control)

---

### 4. Savings Goals

**Purpose:** Tracks multiple concurrent savings goals with target amounts, timelines, and monthly contributions. Shows projected completion dates and whether you're on track.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Goal Name | Title | Specific goal (e.g., "Emergency Fund", "Europe Trip", "Down Payment") |
| Target Amount | Number (USD) | How much you need |
| Current Amount | Number (USD) | How much you've saved so far |
| Progress % | Formula | `if(prop("Target Amount") == 0, 0, round(prop("Current Amount") / prop("Target Amount") * 100))` |
| Progress Display | Formula | `"$" + format(prop("Current Amount")) + " / $" + format(prop("Target Amount")) + " (" + format(prop("Progress %")) + "%)"` |
| Remaining | Formula | `prop("Target Amount") - prop("Current Amount")` |
| Monthly Contribution | Number (USD) | How much you add per month |
| Months to Goal | Formula | `if(prop("Monthly Contribution") == 0, 999, ceil(prop("Remaining") / prop("Monthly Contribution")))` |
| Projected Completion | Formula | `if(prop("Monthly Contribution") == 0, "No contributions set", if(prop("Remaining") <= 0, "Goal reached!", format(prop("Months to Goal")) + " months (" + format(dateAdd(now(), prop("Months to Goal"), "months")) + ")"))` |
| Target Date | Date | When you want to reach this goal |
| On Track | Formula | `if(prop("Remaining") <= 0, "Complete!", if(empty(prop("Target Date")), "No deadline", if(dateBetween(prop("Target Date"), now(), "months") >= prop("Months to Goal"), "On Track", "Behind — increase contributions")))` |
| Priority | Select | Critical / High / Medium / Low / Flexible |
| Account | Relation | -> Accounts database (which savings account holds this) |
| Category | Select | Emergency Fund / House / Car / Travel / Education / Wedding / Baby / Retirement / Freedom Fund / Business / Other |
| Status | Select | Active / Paused / Completed / Cancelled |
| Start Date | Date | When you started saving |
| Last Contribution | Date | When you last added money |
| Contribution History | Text | Monthly log of additions |
| Notes | Text | Strategy, milestones, motivation |
| Tags | Multi-select | Automated / Manual / Joint / Tax-Free / Matching |

**Views:**

- **Active Goals** — Filter: Status = Active, sorted by Priority
- **Progress Board** — Gallery showing Goal Name, Progress Display, Projected Completion
- **By Priority** — Table, grouped by Priority
- **Completed** — Filter: Status = Completed (celebration view!)
- **Behind Schedule** — Filter: On Track = "Behind — increase contributions"
- **By Category** — Table, grouped by Category
- **Contribution Calendar** — Table showing Last Contribution dates

---

### 5. Debt Payoff Tracker

**Purpose:** Manages all debts with snowball and avalanche payoff strategies. Tracks each debt's balance, rate, minimum payment, and extra payment allocation. Calculates total interest costs and payoff timelines for both methods.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Debt Name | Title | Lender + type (e.g., "Chase Visa", "Sallie Mae Student Loan") |
| Account | Relation | -> Accounts database |
| Type | Select | Credit Card / Student Loan / Auto Loan / Personal Loan / Medical / Mortgage / HELOC / Buy Now Pay Later / Other |
| Original Balance | Number (USD) | Starting balance when you began payoff |
| Current Balance | Number (USD) | What you owe right now |
| Interest Rate (APR) | Number | Annual percentage rate |
| Minimum Payment | Number (USD) | Required monthly minimum |
| Extra Payment | Number (USD) | Additional monthly payment above minimum |
| Total Monthly | Formula | `prop("Minimum Payment") + prop("Extra Payment")` |
| Monthly Interest | Formula | `round(prop("Current Balance") * (prop("Interest Rate (APR)") / 100 / 12) * 100) / 100` |
| Principal This Month | Formula | `prop("Total Monthly") - prop("Monthly Interest")` |
| Months to Payoff | Formula | `if(prop("Total Monthly") <= prop("Monthly Interest"), 999, ceil(prop("Current Balance") / (prop("Total Monthly") - prop("Monthly Interest"))))` |
| Payoff Date | Formula | `if(prop("Months to Payoff") >= 999, "Payment too low!", format(dateAdd(now(), prop("Months to Payoff"), "months")))` |
| Total Interest Remaining | Formula | `round((prop("Months to Payoff") * prop("Total Monthly")) - prop("Current Balance"))` |
| Progress % | Formula | `if(prop("Original Balance") == 0, 0, round((prop("Original Balance") - prop("Current Balance")) / prop("Original Balance") * 100))` |
| Progress Display | Formula | `format(prop("Progress %")) + "% paid off ($" + format(prop("Original Balance") - prop("Current Balance")) + " eliminated)"` |
| Snowball Order | Number | Rank by balance (1 = lowest balance) |
| Avalanche Order | Number | Rank by interest rate (1 = highest rate) |
| Status | Select | Active / Paid Off / Deferred / Forbearance / Consolidated |
| Due Date | Number | Day of month payment is due |
| Auto-Pay | Checkbox | Is minimum on auto-pay? |
| Last Payment Date | Date | When you last paid |
| Last Updated | Date | When balance was last refreshed |
| Notes | Text | Payoff strategy notes, negotiation history |
| Tags | Multi-select | Priority / Tax Deductible / Consolidation Candidate / Negotiated Rate / Promotional APR |

**Views:**

- **All Debts** — Table, sorted by Interest Rate descending
- **Snowball Order** — Table, sorted by Current Balance ascending (pay smallest first)
- **Avalanche Order** — Table, sorted by Interest Rate descending (pay highest rate first)
- **Progress** — Gallery showing Debt Name, Progress Display, Payoff Date
- **Active** — Filter: Status = Active
- **Paid Off** — Filter: Status = Paid Off (celebrate!)
- **Payment Schedule** — Table showing Due Date, Total Monthly, sorted by Due Date
- **By Type** — Table, grouped by Type
- **High Interest** — Filter: Interest Rate > 15% (attack these first)

---

## DASHBOARD

> Create this as the top-level page. Your single view of financial health — net worth, budget status, savings progress, and debt payoff at a glance.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  FINANCIAL COMMAND CENTER                        May 2026          |
+----------+----------+----------+----------+----------+-----------+
|  Net     |  Monthly |  Savings |  Debt    |  Savings |  Budget   |
|  Worth   |  Income  |  Rate    |  Total   |  Goals   |  Status   |
| $47,200  |  $6,200  |  32%     | $18,400  |  4 active|  On Track |
+----------+----------+----------+----------+----------+-----------+
|                                                                    |
|  NET WORTH SNAPSHOT                                               |
|  Assets: $65,600 | Liabilities: $18,400 | Net: $47,200           |
|  [Linked view -> Accounts, showing Balance by Category]           |
|                                                                    |
+----------------------------------+-------------------------------+
|  THIS MONTH'S BUDGET             |  SAVINGS GOALS                |
|  [Linked view -> Monthly Budget, |  [Linked view -> Savings      |
|   current month, by Bucket]      |   Goals, Active, showing      |
|                                  |   Progress Display]           |
|  Needs: $2,100 / $2,400         |                               |
|  Wants: $680 / $900             |  Emergency: 72% ($14.4K/$20K) |
|  Savings: $1,980 / $2,000       |  Europe: 45% ($2.7K/$6K)     |
|                                  |  Down Payment: 18% ($9K/$50K) |
+----------------------------------+-------------------------------+
|  DEBT PAYOFF PROGRESS            |  RECENT TRANSACTIONS          |
|  [Linked view -> Debt Tracker,   |  [Linked view -> Transactions,|
|   Active debts, showing          |   last 10 entries]            |
|   Progress Display and           |                               |
|   Payoff Date]                   |                               |
+----------------------------------+-------------------------------+
|  BUDGET ALERTS                   |  UPCOMING BILLS               |
|  [Linked view -> Monthly Budget, |  [Linked view -> Transactions,|
|   Status = "Over Budget"]        |   Recurring, this month,      |
|                                  |   not yet paid]               |
+------------------------------------------------------------------+
```

### Summary Stat Blocks (6-column layout)

- **Net Worth** — Sum of Asset balances minus Sum of Liability balances
- **Monthly Income** — Sum of Transactions where Type = Income, current month
- **Savings Rate** — (Income - Expenses) / Income * 100 for current month
- **Total Debt** — Sum of Current Balance across all active debts
- **Active Savings Goals** — Count where Status = Active
- **Budget Status** — "On Track" if no categories Over Budget, else "Check Budget"

---

## 50/30/20 BUDGET FRAMEWORK

### The Rule

- **50% Needs:** Housing, utilities, groceries, insurance, minimum debt payments, transportation
- **30% Wants:** Dining out, entertainment, shopping, subscriptions, travel, hobbies
- **20% Savings/Investments:** Emergency fund, retirement, extra debt payments, savings goals

### How to Use It

1. Calculate your after-tax monthly income
2. Multiply by 0.50, 0.30, and 0.20 to get each bucket's limit
3. Assign each Budget Category to a Budget Bucket (Needs/Wants/Savings)
4. Track spending against bucket limits, not just individual categories
5. Use the "50/30/20 View" in Transactions to see real-time bucket totals

### Budget Status Formula (Monthly Budgets)

```
if(
  prop("Actual") == 0,
  "No spend yet",
  if(
    prop("Variance") < 0,
    "Over Budget",
    if(
      prop("Variance") == 0,
      "On Budget",
      if(
        prop("Actual") / prop("Budgeted") > 0.85,
        "Almost at limit",
        "On Track"
      )
    )
  )
)
```

---

## DEBT PAYOFF FORMULAS

### Monthly Interest Accrual

```
round(prop("Current Balance") * (prop("Interest Rate (APR)") / 100 / 12) * 100) / 100
```

### Principal Applied This Month

```
prop("Total Monthly") - prop("Monthly Interest")
```

If your total payment is $200 and interest is $45, you're paying down $155 of principal.

### Months to Payoff

```
if(
  prop("Total Monthly") <= prop("Monthly Interest"),
  999,
  ceil(prop("Current Balance") / (prop("Total Monthly") - prop("Monthly Interest")))
)
```

If your payment doesn't exceed the monthly interest, you'll never pay it off (returns 999).

### Total Remaining Interest

```
round((prop("Months to Payoff") * prop("Total Monthly")) - prop("Current Balance"))
```

Total you'll pay minus the principal = total interest cost. This number motivates extra payments.

### Snowball vs. Avalanche Comparison

**Snowball Method:**
- Order debts by Current Balance (smallest first)
- Pay minimums on all debts except the smallest
- Throw all extra money at the smallest balance
- When smallest is paid off, roll its payment into the next smallest
- Advantage: Quick psychological wins from eliminating debts

**Avalanche Method:**
- Order debts by Interest Rate (highest first)
- Pay minimums on all debts except the highest-rate
- Throw all extra money at the highest-rate debt
- When it's paid off, roll its payment into the next highest rate
- Advantage: Minimizes total interest paid (mathematically optimal)

Use both views (Snowball Order, Avalanche Order) to compare. The difference in total interest is your cost of choosing snowball for the psychological benefits.

---

## SAVINGS GOAL FORMULAS

### Months to Goal

```
if(
  prop("Monthly Contribution") == 0,
  999,
  ceil(prop("Remaining") / prop("Monthly Contribution"))
)
```

### Projected Completion Date

```
if(
  prop("Monthly Contribution") == 0,
  "No contributions set",
  if(
    prop("Remaining") <= 0,
    "Goal reached!",
    format(prop("Months to Goal")) + " months"
  )
)
```

### On Track Check

```
if(
  prop("Remaining") <= 0,
  "Complete!",
  if(
    empty(prop("Target Date")),
    "No deadline",
    if(
      dateBetween(prop("Target Date"), now(), "months") >= prop("Months to Goal"),
      "On Track",
      "Behind — increase contributions"
    )
  )
)
```

Compares months until your target date against months needed at current contribution rate.

---

## KEY FORMULA REFERENCE

### Net Worth (manual calculation)

```
Sum of all Asset balances - Sum of all Liability balances
```

Calculate monthly and track the trend. Net worth going up consistently (even slowly) means your system is working.

### Savings Rate

```
(Total Monthly Income - Total Monthly Expenses) / Total Monthly Income * 100
```

Target: 20%+ (per 50/30/20 rule). Track monthly for trend analysis.

### Credit Card Utilization

```
if(
  and(prop("Account Type") == "Credit Card", prop("Credit Limit") > 0),
  format(round(prop("Balance") / prop("Credit Limit") * 100)) + "%",
  "N/A"
)
```

Keep below 30% for credit score health. Below 10% is ideal.

### Budget Variance

```
prop("Budgeted") - prop("Actual")
```

Positive = under budget (good). Negative = over budget (investigate).

### Debt Progress

```
if(
  prop("Original Balance") == 0,
  0,
  round((prop("Original Balance") - prop("Current Balance")) / prop("Original Balance") * 100)
)
```

---

## QUICK-START GUIDE

### Step 1 — Add All Accounts (10 minutes)

- Open the **Accounts** database
- Add every financial account: checking, savings, credit cards, investments, loans
- Set current Balance, Interest Rate, and Account Type
- Mark Category as Asset or Liability
- Set Last Updated to today

### Step 2 — Calculate Your Net Worth (2 minutes)

- Sum all Asset balances
- Sum all Liability balances
- Net Worth = Assets - Liabilities
- Write this number down. This is your starting point.

### Step 3 — Set Up Monthly Budget (15 minutes)

- Open **Monthly Budgets** and create entries for this month
- Add one entry per spending category you want to track
- Assign each to a Budget Bucket (Needs/Wants/Savings)
- Set Budgeted amounts based on your income and the 50/30/20 rule
- Don't guess — use last month's bank statements to estimate realistically

### Step 4 — Add Recurring Transactions (10 minutes)

- Open **Transactions** and add all known recurring expenses
- Include: rent/mortgage, utilities, subscriptions, insurance, loan payments
- Mark as Recurring = true with Frequency
- This becomes your "bills" reference and helps you budget accurately

### Step 5 — Create Savings Goals (10 minutes)

- Open **Savings Goals** and add 2-4 active goals
- Start with Emergency Fund if you don't have one (target: 3-6 months of expenses)
- Set Target Amount, Current Amount, and Monthly Contribution
- Link each goal to its savings Account

### Step 6 — Set Up Debt Payoff (if applicable)

- Open **Debt Payoff Tracker** and add all debts
- Enter Original Balance, Current Balance, Interest Rate, and Minimum Payment
- Assign Snowball Order (by balance) and Avalanche Order (by rate)
- Decide your strategy and allocate Extra Payment to the priority debt

### Step 7 — Start Tracking Transactions (daily, 3 minutes)

- Log expenses daily (or batch 2-3 times per week)
- Required: Description, Date, Type, Amount, Category
- Mark Budget Bucket for each expense
- Update Monthly Budget "Actual" amounts weekly

### Step 8 — Build Your Dashboard

- Create the top-level page following the Dashboard Layout
- Pin to sidebar for daily reference

### Monthly Financial Rhythm

**Weekly (5 minutes, Sunday):**
- Log any un-entered transactions
- Update Monthly Budget "Actual" for each category
- Check budget status — any categories approaching limit?

**Monthly (20 minutes, 1st of month):**
- Update all Account balances
- Calculate net worth (compare to last month)
- Review previous month's budget — where did you overspend? Underspend?
- Set up new month's budget (duplicate last month, adjust as needed)
- Add monthly contribution to savings goals
- Update debt balances after payments
- Calculate savings rate for the month

**Quarterly (30 minutes):**
- Review savings goal progress — on track?
- Review debt payoff progress — adjust strategy?
- Look at spending trends across 3 months — any categories creeping up?
- Adjust budget allocations based on actual patterns

### Pro Tips

- Update Account balances every Monday. Stale balances make your net worth number meaningless and reduce motivation to check the dashboard.
- The "Unplanned Spending" view is your most honest view. After 3 months, you'll see exactly how much impulse spending actually costs you — and it's always more than you think.
- Savings Rate is the single most important metric for building wealth. Income doesn't matter if you spend all of it. Track this monthly and try to improve it by 1% each quarter.
- For debt payoff: if the total interest difference between snowball and avalanche is less than $500, use snowball. The psychological wins are worth more than $500 in sustained motivation.
- Set savings contributions to auto-transfer on payday. "Pay yourself first" is a cliche because it works — money you never see is money you don't miss.
- The 50/30/20 rule is a starting point, not a law. If you're aggressively paying debt or saving for a house, 60/20/20 or 50/20/30 might be more appropriate. Customize.
- Review "Recurring" transactions quarterly. Subscriptions creep. Cancel anything you haven't used in 30 days.
- Your budget should feel slightly uncomfortable but achievable. Too generous and you won't save. Too restrictive and you'll abandon it. The sweet spot is "I have to think about purchases but I'm not suffering."
