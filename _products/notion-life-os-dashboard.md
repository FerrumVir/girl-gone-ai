# Life OS Dashboard — Notion Template

> Duplicate this page into your Notion workspace to get started. All six databases are pre-linked with relations and rollups. The master dashboard pulls live data from every sub-system. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Goals & OKRs

**Purpose:** Top-level goal-setting system using the OKR framework. Annual goals cascade into quarterly objectives, each with measurable key results. Every project and habit in the system can link back to a goal, giving you automatic progress visibility.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Goal Name | Title | Clear, outcome-oriented statement |
| Goal Type | Select | Annual Goal / Quarterly Objective / Key Result |
| Parent Goal | Relation | -> Goals & OKRs (self-referential for cascade) |
| Life Area | Select | Career / Health / Finance / Relationships / Learning / Creative / Spiritual / Personal |
| Status | Select | Not Started / In Progress / At Risk / Completed / Abandoned |
| Priority | Select | P1 (Must) / P2 (Should) / P3 (Could) |
| Quarter | Select | Q1 / Q2 / Q3 / Q4 / Annual |
| Year | Select | 2025 / 2026 / 2027 |
| Start Date | Date | When work begins |
| Target Date | Date | Deadline for completion |
| Progress % | Number | Manual 0-100 or driven by Key Results |
| Target Value | Number | Numeric target for measurable goals |
| Current Value | Number | Current progress toward Target Value |
| Calculated Progress | Formula | `if(prop("Target Value") == 0, prop("Progress %"), round(prop("Current Value") / prop("Target Value") * 100))` |
| On Track | Formula | `if(prop("Status") == "Completed", "Done", if(prop("Calculated Progress") >= (dateBetween(now(), prop("Start Date"), "days") / max(dateBetween(prop("Target Date"), prop("Start Date"), "days"), 1) * 100), "On Track", "Behind"))` |
| Linked Projects | Relation | -> Projects database |
| Linked Habits | Relation | -> Habits database |
| Project Count | Rollup | Count of Linked Projects |
| Active Projects | Rollup | Count where Status != Completed |
| Key Results | Rollup | Count of child Goals where Goal Type = Key Result |
| Completed KRs | Rollup | Count of child Goals where Status = Completed |
| KR Completion Rate | Formula | `if(prop("Key Results") == 0, "N/A", format(round(prop("Completed KRs") / prop("Key Results") * 100)) + "%")` |
| Notes | Text | Context, motivation, success criteria |
| Review Date | Date | Next scheduled review |

**Views:**

- **Annual Vision** — Table, filtered to Goal Type = Annual Goal, grouped by Life Area
- **This Quarter** — Table, filtered to current Quarter + Year, sorted by Priority
- **OKR Tree** — Table, grouped by Parent Goal (shows cascade)
- **By Life Area** — Board, grouped by Life Area, filtered to current quarter
- **At Risk** — Filter: On Track = "Behind" AND Status = In Progress
- **Completed** — Filter: Status = Completed, sorted by Target Date descending
- **Timeline** — Timeline view, showing Start Date to Target Date

---

### 2. Projects

**Purpose:** Active projects and initiatives across all life areas. Each project links to a goal (the "why") and contains tasks (the "how"). Projects are the bridge between high-level vision and daily action.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Project Name | Title | Descriptive, action-oriented name |
| Goal | Relation | -> Goals & OKRs database |
| Life Area | Select | Career / Health / Finance / Relationships / Learning / Creative / Spiritual / Personal |
| Status | Select | Backlog / Active / In Progress / Waiting / On Hold / Completed / Cancelled |
| Priority | Select | P1 / P2 / P3 / P4 (Someday) |
| Start Date | Date | When project begins |
| Due Date | Date | Target completion |
| Completed Date | Date | Actual completion date |
| Days Remaining | Formula | `if(prop("Status") == "Completed", "Done", if(empty(prop("Due Date")), "No deadline", format(dateBetween(prop("Due Date"), now(), "days")) + " days"))` |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Completed", prop("Status") != "Cancelled"), true, false)` |
| Total Tasks | Number | Total task count (manual or via sub-page) |
| Completed Tasks | Number | Completed task count |
| Progress % | Formula | `if(prop("Total Tasks") == 0, 0, round(prop("Completed Tasks") / prop("Total Tasks") * 100))` |
| Next Action | Text | Very next physical action to move forward |
| Next Action Date | Date | When next action is due |
| Energy Required | Select | High / Medium / Low |
| Time Estimate | Select | 15min / 30min / 1hr / 2hr / Half-day / Full-day / Multi-day |
| Tags | Multi-select | Solo / Collaborative / Creative / Administrative / Research / Technical |
| Notes | Text | Project context, resources, links |
| Linked Habits | Relation | -> Habits (habits that support this project) |

**Views:**

- **Active Projects** — Board, grouped by Status, filtered to exclude Completed/Cancelled
- **By Life Area** — Table, grouped by Life Area, sorted by Priority
- **This Week's Focus** — Filter: Status = Active or In Progress, Priority = P1 or P2, sorted by Due Date
- **Overdue** — Filter: Overdue = true
- **Completed** — Filter: Status = Completed, sorted by Completed Date descending
- **Timeline** — Timeline view with Start Date to Due Date
- **Waiting On** — Filter: Status = Waiting

---

### 3. Habits

**Purpose:** Master list of all habits you're tracking. Each habit defines frequency, links to goals, and connects to Daily Check-ins for streak calculation and completion rate analytics.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Habit Name | Title | Short, clear action (e.g., "Meditate 10min") |
| Category | Select | Health / Fitness / Mindfulness / Learning / Productivity / Finance / Social / Creative |
| Frequency | Select | Daily / Weekdays / 3x Week / Weekly / Bi-weekly |
| Goal | Relation | -> Goals & OKRs |
| Project | Relation | -> Projects |
| Status | Select | Active / Paused / Retired |
| Start Date | Date | When you started this habit |
| Current Streak | Number | Updated via check-in system |
| Best Streak | Number | All-time longest streak |
| Streak Status | Formula | `if(prop("Current Streak") >= prop("Best Streak"), "Personal Best!", if(prop("Current Streak") >= 7, "Strong", if(prop("Current Streak") >= 3, "Building", if(prop("Current Streak") >= 1, "Started", "Broken"))))` |
| This Week | Number | Completions this week (manual or rollup) |
| Weekly Target | Number | Based on Frequency (e.g., Daily = 7) |
| Weekly Rate | Formula | `if(prop("Weekly Target") == 0, "N/A", format(round(prop("This Week") / prop("Weekly Target") * 100)) + "%")` |
| This Month | Number | Completions this month |
| Monthly Target | Number | Expected completions this month |
| Monthly Rate | Formula | `if(prop("Monthly Target") == 0, "N/A", format(round(prop("This Month") / prop("Monthly Target") * 100)) + "%")` |
| Time of Day | Select | Morning / Afternoon / Evening / Anytime |
| Duration | Select | 5min / 10min / 15min / 30min / 1hr / Variable |
| Difficulty | Select | Easy / Medium / Hard |
| Cue/Trigger | Text | What initiates this habit (environment design) |
| Reward | Text | What follows completion (habit loop) |
| Notes | Text | Tips, why this matters, adjustments |

**Views:**

- **Active Habits** — Table, filtered to Status = Active, grouped by Category
- **Morning Routine** — Filter: Time of Day = Morning, Status = Active
- **Evening Routine** — Filter: Time of Day = Evening, Status = Active
- **Streaks Board** — Gallery view showing Habit Name, Current Streak, Best Streak, Streak Status
- **By Goal** — Table, grouped by Goal
- **Needs Attention** — Filter: Weekly Rate < 50% AND Status = Active
- **Paused** — Filter: Status = Paused

---

### 4. Daily Check-ins

**Purpose:** Daily log that records habit completions, energy levels, mood, and daily priorities. This is where streaks get calculated and patterns emerge over time. One entry per day.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Date | Title | Today's date (format: YYYY-MM-DD) |
| Day of Week | Formula | `formatDate(now(), "dddd")` |
| Energy Level | Select | 1 (Crashed) / 2 (Low) / 3 (Moderate) / 4 (Good) / 5 (Peak) |
| Mood | Select | Excellent / Good / Neutral / Low / Terrible |
| Sleep Hours | Number | Hours of sleep last night |
| Sleep Quality | Select | Deep / Good / Light / Restless / Insomnia |
| Top 3 Priorities | Text | Three most important outcomes for today |
| Priorities Completed | Number | How many of the 3 were finished (0-3) |
| Win of the Day | Text | One accomplishment worth celebrating |
| Habit 1 | Checkbox | (Rename to your first habit) |
| Habit 2 | Checkbox | (Rename to your second habit) |
| Habit 3 | Checkbox | (Rename to your third habit) |
| Habit 4 | Checkbox | (Rename to your fourth habit) |
| Habit 5 | Checkbox | (Rename to your fifth habit) |
| Habit 6 | Checkbox | (Rename to your sixth habit) |
| Habits Completed | Formula | `(if(prop("Habit 1"), 1, 0) + if(prop("Habit 2"), 1, 0) + if(prop("Habit 3"), 1, 0) + if(prop("Habit 4"), 1, 0) + if(prop("Habit 5"), 1, 0) + if(prop("Habit 6"), 1, 0))` |
| Total Habits | Number | Number of active habits being tracked |
| Completion Rate | Formula | `if(prop("Total Habits") == 0, "N/A", format(round(prop("Habits Completed") / prop("Total Habits") * 100)) + "%")` |
| Gratitude | Text | Three things you're grateful for |
| Reflection | Text | End-of-day notes, lessons, observations |
| Exercise | Checkbox | Did you exercise today? |
| Exercise Type | Select | Strength / Cardio / Yoga / Walk / Sport / Rest Day |
| Water (glasses) | Number | Glasses of water consumed |
| Screen Time (hrs) | Number | Optional tracking |
| Week Number | Formula | `formatDate(prop("Date"), "W")` |

**Views:**

- **Today** — Filter: Date = today (single entry working view)
- **This Week** — Filter: Date is within last 7 days, sorted descending
- **This Month** — Filter: Date is within current month
- **Calendar** — Calendar view by Date
- **Energy Patterns** — Table showing Date, Energy Level, Sleep Hours, Sleep Quality, sorted descending
- **Low Energy Days** — Filter: Energy Level = 1 or 2 (pattern analysis)
- **High Performance** — Filter: Completion Rate >= 80% AND Priorities Completed >= 2

---

### 5. Finances

**Purpose:** Transaction log and financial overview. Tracks income, expenses, savings, and investments with automatic monthly rollups for budget-vs-actual comparison and net worth trending.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Transaction | Title | Brief description of income or expense |
| Date | Date | Transaction date |
| Type | Select | Income / Expense / Transfer / Investment / Savings |
| Category | Select | Salary / Freelance / Side Hustle / Housing / Utilities / Food / Transport / Health / Entertainment / Shopping / Education / Subscriptions / Insurance / Debt Payment / Savings / Investment / Gifts / Travel / Other |
| Amount | Number (USD) | Positive for income, positive for expenses (Type distinguishes) |
| Account | Select | Checking / Savings / Credit Card / Cash / Investment / Business |
| Payment Method | Select | Auto-pay / Manual / Cash / Transfer |
| Recurring | Checkbox | Is this a recurring transaction? |
| Frequency | Select | Weekly / Bi-weekly / Monthly / Quarterly / Annual / One-time |
| Budget Category | Select | Needs / Wants / Savings-Investments (50/30/20 framework) |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")` |
| Notes | Text | Additional context |
| Receipt | Files & media | Upload receipt images |
| Tags | Multi-select | Tax Deductible / Business / Personal / Reimbursable / Planned / Unplanned |

**Views:**

- **All Transactions** — Table, sorted by Date descending
- **This Month** — Filter: Date is current month, sorted by Date descending
- **Income** — Filter: Type = Income, grouped by Category
- **Expenses** — Filter: Type = Expense, grouped by Category
- **By Month** — Table, grouped by Month property
- **Recurring** — Filter: Recurring = true, sorted by Category
- **50/30/20 Split** — Table, grouped by Budget Category, filtered to Type = Expense, current month
- **Tax Deductible** — Filter: Tags contains Tax Deductible

---

### 6. Knowledge Base

**Purpose:** Personal wiki and reference library using progressive summarization. Captures notes, articles, highlights, ideas, and learnings organized by topic with review scheduling to ensure knowledge compounds over time.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Title | Title | Note or resource name |
| Type | Select | Note / Article / Book Summary / Course Notes / Idea / Quote / Reference / Template |
| Source | URL | Where it came from (optional) |
| Author | Text | Original author |
| Topic | Multi-select | Productivity / Business / Psychology / Health / Technology / Finance / Philosophy / Science / Creativity / Leadership / Communication / Other |
| Life Area | Select | Career / Health / Finance / Relationships / Learning / Creative / Spiritual / Personal |
| Status | Select | Inbox / Processing / Summarized / Evergreen / Archive |
| Summary Layer 1 | Text | Bold passages (progressive summarization) |
| Summary Layer 2 | Text | Highlighted within bold (key insights) |
| Summary Layer 3 | Text | Executive summary in your own words |
| Actionable | Checkbox | Contains something you should act on |
| Action Item | Text | What to do with this knowledge |
| Related Notes | Relation | -> Knowledge Base (self-referential for linking) |
| Linked Goal | Relation | -> Goals & OKRs |
| Created | Created time | Auto-populated |
| Last Edited | Last edited time | Auto-populated |
| Review Date | Date | When to revisit this note |
| Review Interval | Select | 1 week / 2 weeks / 1 month / 3 months / 6 months / 1 year |
| Times Reviewed | Number | How many times you've revisited |
| Review Overdue | Formula | `if(and(not(empty(prop("Review Date"))), prop("Review Date") < now(), prop("Status") != "Archive"), true, false)` |
| Tags | Multi-select | Evergreen / Fleeting / Framework / Mental Model / How-to / Case Study / Research |

**Views:**

- **Inbox** — Filter: Status = Inbox, sorted by Created descending
- **All Notes** — Table, sorted by Last Edited descending
- **By Topic** — Table, grouped by Topic
- **Evergreen Notes** — Filter: Status = Evergreen
- **Review Queue** — Filter: Review Overdue = true, sorted by Review Date ascending
- **Actionable** — Filter: Actionable = true, sorted by Created descending
- **Recently Added** — Sorted by Created descending, limit 20
- **Search** — Table with all properties visible for full-text searching

---

## MASTER DASHBOARD

> Create this as the top-level page. Pin it to your sidebar. It is your single entry point to the entire Life OS. Check it every morning and update it every evening.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  LIFE OS COMMAND CENTER                         Week 18, 2026     |
+----------------+--------------+---------------+------------------+
|  Active Goals  |  Projects    |  Habit Rate   |  Monthly Spend   |
|     6          |  4 in prog   |  78% this wk  |  $2,340 / $3,500 |
+----------------+--------------+---------------+------------------+
|                                                                    |
|  TODAY'S CHECK-IN                                                  |
|  [Linked view -> Daily Check-ins, filter: Date = today]           |
|  Energy: ___  Mood: ___  Top 3: ___                               |
|                                                                    |
+----------------------------------+-------------------------------+
|  THIS QUARTER'S GOALS            |  ACTIVE PROJECTS              |
|  [Linked view -> Goals & OKRs,   |  [Linked view -> Projects,    |
|   filter: current quarter,       |   filter: Status = Active      |
|   showing progress bars]         |   or In Progress]             |
+----------------------------------+-------------------------------+
|  HABIT STREAKS                                                    |
|  [Linked view -> Habits, Gallery, showing streak status]          |
|  Meditate: 12 days | Exercise: 8 days | Read: 21 days            |
+----------------------------------+-------------------------------+
|  FINANCIAL SNAPSHOT              |  KNOWLEDGE INBOX              |
|  [Linked view -> Finances,       |  [Linked view -> Knowledge    |
|   this month summary]            |   Base, filter: Status=Inbox] |
|  Income: $5,200                  |  3 notes to process           |
|  Expenses: $2,340                |                               |
|  Savings Rate: 55%               |                               |
+----------------------------------+-------------------------------+
|  OVERDUE & ATTENTION NEEDED                                       |
|  [Linked view -> Projects where Overdue = true]                   |
|  [Linked view -> Goals where On Track = "Behind"]                 |
|  [Linked view -> Knowledge Base where Review Overdue = true]      |
+------------------------------------------------------------------+
```

### Summary Stat Blocks (callout blocks in 4-column layout)

- **Goals on Track** — Count from Goals where On Track != "Behind" for current quarter
- **Project Progress** — Average Progress % across Active projects
- **Weekly Habit Rate** — Average of all active habits' Weekly Rate
- **Net Income** — This month's Income minus Expenses

---

## GOAL CASCADE SYSTEM

The goal cascade ensures that daily actions connect to life-level vision:

```
Annual Goal (1 year)
  -> Quarterly Objective (3 months)
    -> Key Results (measurable milestones)
      -> Projects (the work to achieve key results)
        -> Tasks (daily/weekly actions within projects)
          -> Habits (recurring behaviors that support goals)
```

### How to Use It

1. Set 3-5 Annual Goals across your Life Areas
2. For each Annual Goal, create 2-3 Quarterly Objectives (use the Parent Goal relation)
3. For each Objective, define 2-4 Key Results with Target Values
4. Link existing or new Projects to the relevant Key Results
5. Link relevant Habits to Goals they support
6. During weekly reviews, update Current Value on Key Results and check On Track status

### Goal Progress Formula (explained)

```
if(
  prop("Target Value") == 0,
  prop("Progress %"),
  round(prop("Current Value") / prop("Target Value") * 100)
)
```

If you set a numeric target (e.g., "Read 24 books"), progress auto-calculates from Current Value / Target Value. If no numeric target, use the manual Progress % field.

### On Track Detection Formula

```
if(
  prop("Status") == "Completed",
  "Done",
  if(
    prop("Calculated Progress") >= (
      dateBetween(now(), prop("Start Date"), "days") /
      max(dateBetween(prop("Target Date"), prop("Start Date"), "days"), 1) * 100
    ),
    "On Track",
    "Behind"
  )
)
```

Compares your actual progress against where you should be based on elapsed time. If you're 50% through the time period, you should be at least 50% done.

---

## HABIT STREAK SYSTEM

### Streak Status Formula

```
if(
  prop("Current Streak") >= prop("Best Streak"),
  "Personal Best!",
  if(
    prop("Current Streak") >= 7,
    "Strong",
    if(
      prop("Current Streak") >= 3,
      "Building",
      if(
        prop("Current Streak") >= 1,
        "Started",
        "Broken"
      )
    )
  )
)
```

### Weekly Completion Rate

```
if(
  prop("Weekly Target") == 0,
  "N/A",
  format(round(prop("This Week") / prop("Weekly Target") * 100)) + "%"
)
```

### Daily Completion Rate (in Check-ins)

```
if(
  prop("Total Habits") == 0,
  "N/A",
  format(
    round(prop("Habits Completed") / prop("Total Habits") * 100)
  ) + "%"
)
```

### How Streaks Work

- Each day when you fill out your Daily Check-in, mark habits as complete
- At end of week, update the "This Week" count on each Habit record
- If a habit was done every required day, increment Current Streak
- If missed, reset Current Streak to 0 (update Best Streak first if current > best)
- Use the "Needs Attention" view to spot habits dropping below 50% weekly

---

## FINANCE ROLLUPS

### Monthly Savings Rate

Calculate manually from the "This Month" view:
```
Savings Rate = (Total Income - Total Expenses) / Total Income * 100
```

### 50/30/20 Budget Check

Using the Budget Category property:
- **Needs** (50%): Housing, utilities, groceries, insurance, minimum debt payments
- **Wants** (30%): Entertainment, dining out, shopping, subscriptions, travel
- **Savings/Investments** (20%): Emergency fund, retirement, investments, extra debt payments

The "50/30/20 Split" view groups expenses by these categories so you can see at a glance whether you're within budget for each bucket.

### Quarter-over-Quarter Formula

```
"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")
```

Groups transactions by quarter for trend analysis during quarterly reviews.

---

## KEY FORMULA REFERENCE

### Project Days Remaining

```
if(
  prop("Status") == "Completed",
  "Done",
  if(
    empty(prop("Due Date")),
    "No deadline",
    format(dateBetween(prop("Due Date"), now(), "days")) + " days"
  )
)
```

### Project Overdue Detection

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Completed",
    prop("Status") != "Cancelled"
  ),
  true,
  false
)
```

### Knowledge Base Review Overdue

```
if(
  and(
    not(empty(prop("Review Date"))),
    prop("Review Date") < now(),
    prop("Status") != "Archive"
  ),
  true,
  false
)
```

### Habits Completed Counter (Daily Check-in)

```
(if(prop("Habit 1"), 1, 0) +
 if(prop("Habit 2"), 1, 0) +
 if(prop("Habit 3"), 1, 0) +
 if(prop("Habit 4"), 1, 0) +
 if(prop("Habit 5"), 1, 0) +
 if(prop("Habit 6"), 1, 0))
```

---

## WEEKLY REVIEW TEMPLATE

Use this every Sunday (15-20 minutes):

1. **Review Goals** — Open "This Quarter" view. Update Current Value on any Key Results that advanced. Flag anything "Behind."
2. **Review Projects** — Open "Active Projects" view. Update task counts. Move completed projects to Done. Set Next Action for each.
3. **Update Habits** — Transfer daily check-in completions to habit "This Week" counts. Update streaks. Celebrate Personal Bests.
4. **Financial Check** — Open "This Month" finance view. Categorize any uncategorized transactions. Check 50/30/20 balance.
5. **Knowledge Review** — Open "Review Queue" view. Spend 5 minutes revisiting flagged notes. Set next Review Date.
6. **Plan Next Week** — Set top priorities for next week in a new daily check-in or project notes.

---

## QUICK-START GUIDE

### Step 1 — Define Your Life Areas and Goals

- Open the **Goals & OKRs** database
- Add 3-5 Annual Goals across different Life Areas
- For your top priority goal, add 2-3 Quarterly Objectives with Key Results
- Set Target Values for anything measurable

### Step 2 — Add Your Active Projects

- Open the **Projects** database
- Add everything you're currently working on (keep it to 5-7 active maximum)
- Link each project to the Goal it supports
- Set Status, Priority, and Due Date
- Write the Next Action for each

### Step 3 — Set Up Your Habits

- Open the **Habits** database
- Add 3-6 habits you want to track (start small — you can add more later)
- Link each habit to a Goal if relevant
- Set Frequency, Time of Day, and Weekly/Monthly Targets
- Rename the checkbox properties in Daily Check-ins to match your habits

### Step 4 — Start Daily Check-ins

- Create today's entry in **Daily Check-ins**
- Each morning: set Energy Level, Top 3 Priorities
- Throughout the day: mark habit checkboxes as completed
- Each evening: note Win of the Day, Gratitude, Reflection

### Step 5 — Add Financial Baseline

- Open **Finances** and add all recurring transactions (rent, salary, subscriptions)
- Mark them as Recurring and set Frequency
- Add this month's transactions so far
- Going forward, log expenses daily or do a batch entry twice per week

### Step 6 — Seed Your Knowledge Base

- Open **Knowledge Base** and add 5-10 notes from your existing systems
- Set Status = Inbox for anything not yet processed
- Process inbox items by adding Summary Layers and setting Review Dates
- Link notes to relevant Goals

### Step 7 — Build Your Dashboard

- Create a new top-level page titled "Life OS"
- Add linked database views as shown in the Dashboard Layout section
- Add four callout blocks at the top for summary stats
- Pin to your Notion sidebar

### Step 8 — Establish Rhythms

**Daily (5 minutes morning, 3 minutes evening):**
- Morning: Open dashboard, check priorities, note energy level
- Evening: Mark habits, record win, write reflection

**Weekly (15-20 minutes, Sunday):**
- Follow the Weekly Review Template above

**Monthly (30 minutes, first of month):**
- Review monthly habit rates and update Best Streaks
- Review financial summary and 50/30/20 split
- Process knowledge inbox fully
- Adjust goals if needed

**Quarterly (1 hour):**
- Score Key Results (0-100%)
- Set new Quarterly Objectives
- Retire completed/irrelevant habits, add new ones
- Review and update Annual Goals

### Pro Tips

- Do not try to use all six databases from day one. Start with Goals + Projects + Daily Check-ins. Add Habits in week 2, Finances in week 3, Knowledge Base in week 4.
- The system works best when you interact with it daily, even if only for 2 minutes. A perfect system you ignore is worse than a rough system you actually use.
- Use Notion template buttons to create new Daily Check-ins with one click — pre-fill the date and habit checkboxes.
- Keep the "Overdue & Attention Needed" section of your dashboard visible. If something lives there for more than a week, either do it, reschedule it, or delete it.
- Your weekly review is the single most important habit in this system. Protect it. Without reviews, databases become graveyards.
- The Knowledge Base is not a collector — it's a thinker. Only save things you plan to act on or revisit. Process inbox weekly; never let it grow past 15 items.
