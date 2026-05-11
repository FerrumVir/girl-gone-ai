# Personal Finance Dashboard — Complete Money Management System

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Accounts

**Purpose:** Every financial account you own — assets and liabilities — forming the foundation of your net worth calculation.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Account Name | Title | Descriptive name — e.g. "Chase Checking" or "Roth IRA — Fidelity" |
| Institution | Text | Bank, brokerage, or lender name |
| Account Type | Select | Checking / Savings / High-Yield Savings / Money Market / Credit Card / Student Loan / Auto Loan / Mortgage / Personal Loan / 401(k) / Roth IRA / Traditional IRA / Brokerage / HSA / 529 Plan / Crypto / Property / Vehicle / Other Asset / Other Liability |
| Category | Select | Cash / Investment / Retirement / Debt / Property / Vehicle / Other |
| Asset or Liability | Select | Asset / Liability |
| Current Balance | Number (USD) | Current balance as of last update |
| Last Updated | Date | When you last verified this balance |
| Interest Rate % | Number | APY for savings/investments, APR for debt |
| Minimum Payment | Number (USD) | Monthly minimum for debt accounts |
| Credit Limit | Number (USD) | For credit cards |
| Utilization % | Formula | `if(and(prop("Account Type") == "Credit Card", prop("Credit Limit") > 0), round((prop("Current Balance") / prop("Credit Limit")) * 100), 0)` |
| Account Number (last 4) | Text | Last 4 digits for identification (never store full account numbers) |
| Login URL | URL | Quick link to your online banking login |
| Auto-Pay Enabled | Checkbox | Is auto-pay set up for this account? |
| Status | Select | Active / Closed / Frozen / Dormant |
| Notes | Text | Account-specific notes, terms, contact info |
| Monthly Contribution | Number (USD) | How much you add to this account monthly (for savings/investment) |
| Linked Transactions | Relation | -> Transactions database |
| Linked Goals | Relation | -> Goals database (which savings goal is this account funding?) |
| Tags | Multi-select | Primary / Joint / Emergency Fund / Taxable / Tax-Advantaged / High-Priority Debt |

**Views:**

- **All Accounts** — Table, sorted by Category then Account Name
- **Assets** — Filter: Asset or Liability = Asset, sorted by Current Balance descending
- **Liabilities** — Filter: Asset or Liability = Liability, sorted by Current Balance descending
- **Net Worth Summary** — Table showing Account Name, Category, Asset or Liability, Current Balance — with sum at bottom
- **By Category** — Table, grouped by Category, with sum of Current Balance per group
- **Debt Overview** — Filter: Asset or Liability = Liability, showing Account Name, Balance, Interest Rate, Minimum Payment
- **Credit Cards** — Filter: Account Type = Credit Card, showing Utilization %
- **Needs Update** — Filter: Last Updated is more than 30 days ago

---

### 2. Transactions

**Purpose:** Every dollar in and every dollar out. Your spending and income log with category tracking and budget-vs-actual analysis.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Description | Title | What you bought or received — e.g. "Whole Foods — groceries" |
| Date | Date | Transaction date |
| Amount | Number (USD) | Positive for income, positive for expenses (use Direction to distinguish) |
| Direction | Select | Income / Expense / Transfer |
| Category | Select | Housing / Utilities / Groceries / Dining Out / Transportation / Gas / Insurance / Healthcare / Medications / Clothing / Personal Care / Entertainment / Streaming / Fitness / Education / Gifts / Donations / Travel / Pet / Childcare / Home Maintenance / Subscriptions / Business Expense / Savings Transfer / Investment / Debt Payment / Miscellaneous |
| Sub-Category | Text | More specific — e.g. "Electric bill" under Utilities |
| Account | Relation | -> Accounts database (which account was used) |
| Account Name | Rollup | Account Name from linked Account |
| Payment Method | Select | Debit Card / Credit Card / Cash / Bank Transfer / Venmo / Zelle / PayPal / Check / Auto-Pay |
| Recurring | Checkbox | Is this a recurring transaction (monthly bill, subscription)? |
| Essential | Checkbox | Is this a need (true) or a want (false)? |
| Budget Amount | Number (USD) | Your monthly budget for this category |
| Notes | Text | Receipt details, who you were with, reason for purchase |
| Tax Deductible | Checkbox | Flag for tax-relevant expenses |
| Reimbursable | Checkbox | Should someone reimburse you for this? |
| Reimbursed | Checkbox | Has the reimbursement been received? |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Day of Week | Formula | `formatDate(prop("Date"), "dddd")` |
| Year | Formula | `formatDate(prop("Date"), "YYYY")` |

**Views:**

- **All Transactions** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month, sorted by Date descending
- **By Category (This Month)** — Filter: Date is this month, Direction = Expense, grouped by Category, with sum of Amount
- **Income** — Filter: Direction = Income, sorted by Date descending
- **Expenses** — Filter: Direction = Expense, sorted by Date descending
- **Monthly Summary** — Table, grouped by Month, with sum of Amount (filtered by Direction for income and expense totals)
- **Recurring** — Filter: Recurring = true, sorted by Category
- **Tax Deductible** — Filter: Tax Deductible = true, grouped by Year
- **Needs vs Wants** — Filter: Direction = Expense, grouped by Essential (true/false), with sum of Amount
- **By Payment Method** — Grouped by Payment Method
- **Calendar** — Calendar view, by Date
- **Unreimbursed** — Filter: Reimbursable = true AND Reimbursed = false

---

### 3. Goals

**Purpose:** Every financial goal you're working toward — with progress tracking, monthly contributions, and projected completion dates.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Goal Name | Title | Specific name — e.g. "Emergency Fund (6 months)" |
| Category | Select | Emergency Fund / Down Payment / Vacation / Car / Wedding / Education / Retirement Milestone / Debt Freedom / Moving / Home Renovation / Investment Target / Other |
| Priority | Select | Critical / High / Medium / Low |
| Status | Select | Active / Paused / Completed / Abandoned |
| Target Amount | Number (USD) | Total amount you need to reach |
| Current Amount | Number (USD) | How much you've saved/accumulated so far |
| Remaining | Formula | `prop("Target Amount") - prop("Current Amount")` |
| Progress % | Formula | `if(prop("Target Amount") > 0, round((prop("Current Amount") / prop("Target Amount")) * 100), 0)` |
| Monthly Contribution | Number (USD) | How much you're adding each month |
| Months to Goal | Formula | `if(prop("Monthly Contribution") > 0, ceil(prop("Remaining") / prop("Monthly Contribution")), 0)` |
| Projected Completion | Formula | `if(prop("Monthly Contribution") > 0, dateAdd(now(), prop("Months to Goal"), "months"), now())` |
| Target Date | Date | When you want to reach this goal (your desired deadline) |
| On Track | Formula | `if(empty(prop("Target Date")), "No deadline", if(prop("Projected Completion") <= prop("Target Date"), "ON TRACK", "BEHIND"))` |
| Start Date | Date | When you started working on this goal |
| Funding Account | Relation | -> Accounts database (where is this money being saved?) |
| Notes | Text | Strategy, milestones, motivation notes |
| Last Updated | Date | When you last updated the Current Amount |

**Views:**

- **All Goals** — Table, sorted by Priority then Goal Name
- **Active Goals** — Filter: Status = Active, sorted by Progress % descending
- **Goal Progress Board** — Gallery view showing Goal Name, Progress %, Remaining, Projected Completion
- **Behind Schedule** — Filter: On Track = "BEHIND", Status = Active
- **By Category** — Table, grouped by Category
- **Completed** — Filter: Status = Completed

---

### 4. Investments

**Purpose:** Your investment portfolio broken down by individual holding — stocks, ETFs, bonds, crypto, real estate — with performance and allocation tracking.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Holding Name | Title | Ticker symbol or name — e.g. "VTI — Vanguard Total Stock Market" |
| Account | Relation | -> Accounts database (which brokerage/retirement account) |
| Account Name | Rollup | From Account relation |
| Asset Class | Select | US Stocks / International Stocks / Bonds / REITs / Crypto / Commodities / Cash Equivalent / Individual Stock / Other |
| Investment Type | Select | ETF / Index Fund / Mutual Fund / Individual Stock / Bond / Bond Fund / REIT / Crypto / CD / Treasury / Other |
| Shares/Units | Number | Number of shares or units owned |
| Cost Basis Per Share | Number (USD) | Average price you paid per share |
| Total Cost Basis | Formula | `prop("Shares/Units") * prop("Cost Basis Per Share")` |
| Current Price Per Share | Number (USD) | Current market price per share |
| Current Value | Formula | `prop("Shares/Units") * prop("Current Price Per Share")` |
| Gain/Loss ($) | Formula | `prop("Current Value") - prop("Total Cost Basis")` |
| Gain/Loss (%) | Formula | `if(prop("Total Cost Basis") > 0, round(((prop("Current Value") - prop("Total Cost Basis")) / prop("Total Cost Basis")) * 100 * 100) / 100, 0)` |
| Dividend Yield % | Number | Annual dividend yield percentage |
| Annual Dividend | Formula | `prop("Current Value") * (prop("Dividend Yield %") / 100)` |
| Expense Ratio % | Number | Fund expense ratio (for ETFs and mutual funds) |
| Purchase Date | Date | When you bought this holding (or first purchase date) |
| Target Allocation % | Number | What percentage of your portfolio this should be |
| Actual Allocation % | Number | Manually update during portfolio reviews (current value / total portfolio value) |
| Allocation Drift | Formula | `abs(prop("Target Allocation %") - prop("Actual Allocation %"))` |
| Rebalance Needed | Formula | `if(prop("Allocation Drift") > 5, "REBALANCE", "OK")` |
| Tax Status | Select | Taxable / Tax-Deferred (401k, Traditional IRA) / Tax-Free (Roth) / Tax-Advantaged (HSA) |
| Auto-Invest | Checkbox | Is this holding part of an automatic investment? |
| Last Updated | Date | When you last updated the current price |
| Notes | Text | Investment thesis, why you hold this, research notes |

**Views:**

- **All Holdings** — Table, sorted by Asset Class then Holding Name
- **Portfolio Summary** — Table showing Holding Name, Current Value, Gain/Loss, Actual Allocation %, Target Allocation %
- **By Asset Class** — Table, grouped by Asset Class, with sum of Current Value per group
- **By Account** — Table, grouped by Account Name, with sum of Current Value
- **Performance** — Table sorted by Gain/Loss (%) descending
- **Needs Rebalancing** — Filter: Rebalance Needed = "REBALANCE"
- **Dividend Income** — Table showing holdings with Dividend Yield > 0, sorted by Annual Dividend descending
- **By Tax Status** — Table, grouped by Tax Status

---

### 5. Subscriptions

**Purpose:** Every recurring charge across all your accounts — audited, tracked, and evaluated for whether it's still worth paying.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Service Name | Title | Name of the subscription — e.g. "Netflix" |
| Category | Select | Streaming Video / Streaming Music / Software / Cloud Storage / News/Media / Fitness / Food Delivery / Gaming / Education / Productivity / Finance / Health / Insurance / Membership / Other |
| Monthly Cost | Number (USD) | Monthly charge (if billed annually, divide by 12) |
| Annual Cost | Formula | `prop("Monthly Cost") * 12` |
| Billing Cycle | Select | Monthly / Quarterly / Semi-Annual / Annual |
| Actual Charge | Number (USD) | What you're actually billed per cycle |
| Payment Method | Select | Credit Card / Debit Card / Bank Transfer / PayPal / Apple Pay |
| Account | Relation | -> Accounts database (which card/account is being charged) |
| Account Name | Rollup | From Account relation |
| Start Date | Date | When you first subscribed |
| Next Renewal | Date | Next billing date |
| Days Until Renewal | Formula | `if(empty(prop("Next Renewal")), 0, dateBetween(prop("Next Renewal"), now(), "days"))` |
| Cancellation Deadline | Date | Last day to cancel before next charge (if different from renewal) |
| Auto-Renew | Checkbox | Does this renew automatically? |
| Status | Select | Active / Paused / Cancelled / Free Trial / Considering |
| Usage Frequency | Select | Daily / Several Times a Week / Weekly / A Few Times a Month / Rarely / Never |
| Value Assessment | Select | Essential / Worth It / Questionable / Cancel |
| Last Reviewed | Date | When you last evaluated whether to keep this subscription |
| Shared With | Text | Who else uses this subscription (partner, family, etc.) |
| Login URL | URL | Quick access to manage or cancel |
| Cancel URL | URL | Direct link to cancellation page (save this — some services bury it) |
| Notes | Text | What you use it for, alternatives considered, cancellation terms |

**Views:**

- **All Subscriptions** — Table, sorted by Category then Service Name
- **Active** — Filter: Status = Active, sorted by Monthly Cost descending
- **Monthly Cost Summary** — Filter: Status = Active, with sum of Monthly Cost (your total monthly subscription spend)
- **By Category** — Table, grouped by Category, with sum of Monthly Cost per group
- **Cancel Candidates** — Filter: Value Assessment = Questionable OR Cancel
- **Rarely Used** — Filter: Usage Frequency = Rarely or Never, Status = Active
- **Upcoming Renewals** — Sorted by Next Renewal ascending, filter: next 30 days
- **Free Trials** — Filter: Status = Free Trial (don't forget to cancel before you're charged)
- **Subscription Cards** — Gallery view, grouped by Value Assessment
- **By Payment Method** — Grouped by Account Name

---

## DASHBOARD

> Create this as a Notion page that pulls from all five databases using linked views and summary blocks.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  FINANCIAL COMMAND CENTER             April 2026              |
+-------------------------------------------------------------+
|                     NET WORTH: $47,250                        |
|        Assets: $82,300    |    Liabilities: $35,050           |
|                Change from last month: +$1,420                |
+--------------+--------------+--------------+-----------------+
|  Monthly     |  Savings     |  Portfolio   |  Subscription    |
|  Spending    |  Rate        |  Value       |  Spend           |
|  $3,450      |  22%         |  $18,700     |  $187/mo         |
+--------------+--------------+--------------+-----------------+
|  NET WORTH TRACKER                                           |
|  [Monthly snapshot table — see Net Worth Tracking section]   |
+-------------------------------------------------------------+
|  GOAL PROGRESS                                               |
|  [Linked view -> Goals, filter: Status = Active,             |
|   Gallery view showing Progress %, Projected Completion]     |
+-----------------------------+-------------------------------+
|  SPENDING THIS MONTH        |  UPCOMING BILLS                |
|  [Linked view -> Transact., |  [Linked view -> Transact.,   |
|   filter: this month,       |   filter: Recurring = true,   |
|   grouped by Category,      |   next 14 days]               |
|   sum of Amount]            |                               |
+-----------------------------+-------------------------------+
|  DEBT OVERVIEW                                               |
|  [Linked view -> Accounts, filter: Liability,                |
|   showing Balance, Interest Rate, Minimum Payment]           |
+-------------------------------------------------------------+
|  INVESTMENT PORTFOLIO                                        |
|  [Linked view -> Investments, grouped by Asset Class,        |
|   sum of Current Value, Gain/Loss]                           |
+-----------------------------+-------------------------------+
|  SUBSCRIPTION AUDIT         |  NEEDS ATTENTION               |
|  [Linked view -> Subs,      |  [Goals: Behind Schedule]      |
|   filter: Cancel Candidates] |  [Accounts: Needs Update]     |
|                              |  [Investments: Rebalance]     |
+-----------------------------+-------------------------------+
```

### Net Worth Tracking

Create a separate Notion database or table for monthly net worth snapshots:

| Date | Total Assets | Total Liabilities | Net Worth | Change | Notes |
|---|---|---|---|---|---|
| April 1, 2026 | $82,300 | $35,050 | $47,250 | +$1,420 | Bonus deposited, extra mortgage payment |
| March 1, 2026 | $80,500 | $34,670 | $45,830 | +$980 | Steady month |
| Feb 1, 2026 | $79,200 | $34,350 | $44,850 | +$1,150 | Tax refund received |
| Jan 1, 2026 | $77,500 | $33,800 | $43,700 | — | Starting point |

**How to take a monthly snapshot:**
1. On the 1st of each month, open the Accounts database
2. Update the Current Balance for every account (takes 5-10 minutes)
3. Sum all Asset balances and all Liability balances
4. Add a new row to the Net Worth table with the totals
5. Calculate the change from last month

Over 12 months, this table becomes the single most valuable financial document you own.

---

## DEBT PAYOFF PLANNER

### How to Use the Debt Payoff Planner

1. Open the **Accounts** database and filter to "Liabilities"
2. For each debt, ensure you have: Current Balance, Interest Rate %, and Minimum Payment
3. Choose your payoff strategy below
4. Enter your total monthly debt payment budget (all minimums + any extra you can contribute)

### Strategy Comparison

**Snowball Method (Behavioral Motivation):**
- Pay minimums on all debts
- Put all extra money toward the smallest balance first
- When the smallest debt is paid off, roll that payment into the next smallest
- **Best for:** People who need motivational wins to stay committed

**Avalanche Method (Mathematical Optimal):**
- Pay minimums on all debts
- Put all extra money toward the highest interest rate first
- When the highest-rate debt is paid off, roll that payment into the next highest
- **Best for:** People who are motivated by saving the most money on interest

### Debt Payoff Tracking Table

| Debt Name | Balance | Interest Rate | Min Payment | Snowball Order | Avalanche Order | Projected Payoff |
|---|---|---|---|---|---|---|
| [Smallest balance first] | | | | 1 | | |
| [Next smallest] | | | | 2 | | |
| [Next smallest] | | | | 3 | | |
| [Highest rate first] | | | | | 1 | |

### Monthly Debt Payment Log

| Month | Debt Name | Payment | Extra Payment | Remaining Balance | Notes |
|---|---|---|---|---|---|
| | | | | | |

### Payoff Projection Formula

For a simplified payoff estimate per debt:

```
Months to payoff = -log(1 - (rate * balance / payment)) / log(1 + rate)

Where:
- rate = monthly interest rate (APR / 12 / 100)
- balance = current balance
- payment = monthly payment toward this debt
```

For a quick approximation without the formula:
- Divide your balance by your monthly payment (ignoring interest)
- Add 15-30% to account for interest charges
- Example: $5,000 balance / $200/month = 25 months + ~5 months interest = ~30 months

---

## KEY FORMULA REFERENCE

### Net Worth Calculation
```
Net Worth = Sum of all Asset balances - Sum of all Liability balances
```
Use the "Net Worth Summary" view in the Accounts database. Sum the Asset group and subtract the Liability group.

### Savings Rate
```
Savings Rate = (Monthly Income - Monthly Expenses) / Monthly Income * 100

Target benchmarks:
- 10% = foundational (minimum viable)
- 15-20% = solid (standard recommendation)
- 25-35% = aggressive (early retirement track)
- 50%+ = financial independence pursuit
```

### Credit Card Utilization (Accounts database)
```
if(
  and(
    prop("Account Type") == "Credit Card",
    prop("Credit Limit") > 0
  ),
  round((prop("Current Balance") / prop("Credit Limit")) * 100),
  0
)

Target: Keep below 30% for healthy credit score. Below 10% is ideal.
```

### Goal Progress (Goals database)
```
Progress % = round((Current Amount / Target Amount) * 100)

Months to Goal = ceil(Remaining / Monthly Contribution)

On Track = if Projected Completion <= Target Date then "ON TRACK" else "BEHIND"
```

### Investment Gain/Loss (Investments database)
```
Gain/Loss ($) = Current Value - Total Cost Basis
Gain/Loss (%) = ((Current Value - Total Cost Basis) / Total Cost Basis) * 100

Allocation Drift = abs(Target Allocation % - Actual Allocation %)
Rebalance trigger: Drift > 5 percentage points
```

### Subscription Burn Rate
```
Total Monthly Subscription Spend = Sum of Monthly Cost where Status = Active
Annual Subscription Spend = Total Monthly * 12

Ask yourself: "Would I buy this subscription again today at this price?"
If the answer is no, cancel it.
```

---

## FINANCIAL CALENDAR

Set up these recurring reminders in Notion or your calendar app:

### Monthly
- [ ] 1st: Update all account balances and take net worth snapshot
- [ ] 1st: Review last month's spending by category
- [ ] 1st: Verify all recurring bills were paid correctly
- [ ] 1st: Update savings goal progress
- [ ] 15th: Mid-month spending check — are you on track?

### Quarterly
- [ ] Update investment prices and review portfolio allocation
- [ ] Rebalance portfolio if any asset class is >5% off target
- [ ] Review and audit all subscriptions — cancel anything scored "Cancel" or "Questionable"
- [ ] Update debt payoff tracker with new balances
- [ ] Estimated tax payment due (if self-employed): Jan 15, April 15, June 15, Sept 15

### Semi-Annual
- [ ] Review insurance policies — are your coverages still appropriate?
- [ ] Check credit report (free at annualcreditreport.com)
- [ ] Review and update beneficiaries on retirement and investment accounts
- [ ] Evaluate savings goals — any adjustments needed?

### Annual
- [ ] Year-end net worth calculation and year-over-year comparison
- [ ] Review investment performance against benchmarks
- [ ] Tax document preparation (W-2, 1099s, deduction records)
- [ ] Set financial goals for the new year
- [ ] Review and update estate planning documents
- [ ] Open enrollment review for health insurance and benefits
- [ ] Maximize retirement account contributions before deadlines

---

## QUICK-START GUIDE

### Step 1 — Enter Your Accounts (10 minutes)
- Open the **Accounts** database
- Add every account you have: checking, savings, credit cards, loans, investment/retirement accounts
- For each account enter: Account Name, Institution, Account Type, Category, Asset or Liability, and Current Balance
- For debts: add Interest Rate % and Minimum Payment
- This gives you an instant net worth calculation

### Step 2 — Set Your Financial Goals (5 minutes)
- Open the **Goals** database
- Add 2-5 financial goals you're actively working toward
- For each: enter Target Amount, Current Amount, and Monthly Contribution
- Link each goal to its Funding Account
- The template will calculate your projected completion date automatically

### Step 3 — Enter Your Investments (5 minutes)
- Open the **Investments** database
- Add each holding: name/ticker, shares, cost basis per share, current price per share
- Set Asset Class and Investment Type for each
- Enter your Target Allocation % for each asset class
- Link each holding to its Account

### Step 4 — Audit Your Subscriptions (10 minutes)
- Open the **Subscriptions** database
- Add every recurring charge you can find (check your credit card and bank statements for the last 3 months)
- Enter Monthly Cost, Billing Cycle, and Next Renewal date for each
- Rate each subscription's Usage Frequency and Value Assessment
- Immediately cancel anything rated "Cancel"

### Step 5 — Start Logging Transactions (ongoing)
- Open the **Transactions** database
- Begin logging your daily spending and income
- Categorize each transaction and link it to the Account used
- You don't need to backfill months of history — start today and build forward

### Step 6 — Set Up Your Dashboard
- Pin the Dashboard page to your Notion sidebar
- Take your first net worth snapshot and enter it in the Net Worth table
- This is your monthly financial review home base

### Pro Tips

- The single most valuable habit: update your net worth on the 1st of every month. After 6 months, you'll have a trendline that tells you more about your financial health than any budgeting app ever will.
- Use the "Needs vs Wants" transaction view at the end of each month to calculate your needs:wants ratio. A healthy target is 50/30/20 (needs/wants/savings).
- When you find a subscription you forgot about, don't just cancel it — note how long you were paying for it without using it. That number is your "subscription awareness tax" and it will motivate you to do regular audits.
- For investments, update prices quarterly, not daily. Checking too often leads to anxiety-driven decisions. The Rebalance Needed formula will tell you when action is actually required.
- Set your Emergency Fund goal to 3-6 months of essential expenses (use your "Needs" spending total from the Transactions database). This is the first goal to complete — it protects everything else.
- Use the Tax Deductible filter in Transactions religiously throughout the year. Come tax season, your deduction documentation is already done.
- If you have a partner, schedule a monthly "money date" — review the dashboard together for 15 minutes on the 1st of each month. Shared visibility eliminates most financial conflict in relationships.
