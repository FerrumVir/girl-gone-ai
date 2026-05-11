# Habit Tracker & Streak System — Notion Template

> Duplicate this page into your Notion workspace to get started. Both databases are pre-linked with streak formulas and completion rate calculations built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Habits (Master List)

**Purpose:** Defines every habit you're tracking — its frequency, category, streak status, and completion rates. This is the configuration layer. Each habit here connects to daily check-in entries for automatic streak and rate calculations.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Habit Name | Title | Short, specific action (e.g., "Meditate 10 min", "Walk 30 min") |
| Category | Select | Health / Fitness / Mindfulness / Productivity / Learning / Finance / Social / Creative / Self-Care |
| Frequency | Select | Daily / Weekdays / 3x Week / 4x Week / 5x Week / Weekly |
| Target Per Week | Number | How many times per week this should be done (e.g., Daily = 7) |
| Status | Select | Active / Paused / Building / Retired |
| Start Date | Date | When you began tracking this habit |
| Current Streak | Number | Consecutive completions (updated manually or via weekly review) |
| Best Streak | Number | All-time longest streak |
| Streak Status | Formula | `if(prop("Current Streak") == 0, "Reset", if(prop("Current Streak") >= prop("Best Streak"), "Personal Best!", if(prop("Current Streak") >= 21, "Locked In", if(prop("Current Streak") >= 7, "Strong", if(prop("Current Streak") >= 3, "Building", "Starting")))))` |
| This Week Completions | Number | Times completed this week (update during weekly review) |
| Weekly Rate | Formula | `if(prop("Target Per Week") == 0, 0, round(prop("This Week Completions") / prop("Target Per Week") * 100))` |
| Weekly Rate Display | Formula | `format(prop("Weekly Rate")) + "%"` |
| This Month Completions | Number | Times completed this month |
| Monthly Target | Formula | `round(prop("Target Per Week") * 4.33)` |
| Monthly Rate | Formula | `if(prop("Monthly Target") == 0, 0, round(prop("This Month Completions") / prop("Monthly Target") * 100))` |
| Monthly Rate Display | Formula | `format(prop("Monthly Rate")) + "%"` |
| Last 4 Weeks Avg | Formula | `format(round((prop("This Month Completions") / max(prop("Monthly Target"), 1)) * 100)) + "% avg"` |
| Time of Day | Select | Morning / Midday / Afternoon / Evening / Anytime |
| Duration | Select | 2 min / 5 min / 10 min / 15 min / 30 min / 1 hr / Variable |
| Difficulty | Select | Trivial / Easy / Medium / Hard / Very Hard |
| Cue | Text | Environment trigger (what starts this habit) |
| Routine | Text | The exact behavior (make it specific) |
| Reward | Text | What follows completion (immediate gratification) |
| Minimum Viable Version | Text | The smallest possible version for hard days (e.g., "1 minute of stretching") |
| Stacked After | Text | Which existing habit does this follow? (habit stacking) |
| Why | Text | Deep motivation — why this habit matters to your identity |
| Notes | Text | Tips, adjustments, obstacles encountered |
| Linked Check-ins | Relation | -> Daily Check-ins database |
| Days Active | Formula | `dateBetween(now(), prop("Start Date"), "days")` |
| Needs Attention | Formula | `if(and(prop("Status") == "Active", prop("Weekly Rate") < 50), true, false)` |

**Views:**

- **Active Habits** — Table, filtered to Status = Active, sorted by Category
- **Streak Leaderboard** — Table sorted by Current Streak descending (gamified view)
- **Morning Routine** — Filter: Time of Day = Morning AND Status = Active, sorted by Stacked After
- **Evening Routine** — Filter: Time of Day = Evening AND Status = Active
- **Needs Attention** — Filter: Needs Attention = true (below 50% weekly)
- **By Category** — Board, grouped by Category, filtered to Active
- **Habit Cards** — Gallery showing Habit Name, Current Streak, Streak Status, Weekly Rate Display
- **Building** — Filter: Status = Building (new habits getting established)
- **All Habits** — Table showing everything including Paused and Retired

---

### 2. Daily Check-ins

**Purpose:** One entry per day recording which habits were completed. This is your daily interaction point — open it, check boxes, close it. Aggregated data feeds into streak counts and completion rates.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Date | Title | Format: YYYY-MM-DD (e.g., 2026-05-06) |
| Day | Formula | `formatDate(now(), "dddd")` |
| Week Number | Formula | `"Week " + formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Habit 1 | Checkbox | (Rename to your first habit) |
| Habit 2 | Checkbox | (Rename to your second habit) |
| Habit 3 | Checkbox | (Rename to your third habit) |
| Habit 4 | Checkbox | (Rename to your fourth habit) |
| Habit 5 | Checkbox | (Rename to your fifth habit) |
| Habit 6 | Checkbox | (Rename to your sixth habit) |
| Habit 7 | Checkbox | (Rename to your seventh habit) |
| Habit 8 | Checkbox | (Rename to your eighth habit) |
| Habits Done | Formula | `(if(prop("Habit 1"), 1, 0) + if(prop("Habit 2"), 1, 0) + if(prop("Habit 3"), 1, 0) + if(prop("Habit 4"), 1, 0) + if(prop("Habit 5"), 1, 0) + if(prop("Habit 6"), 1, 0) + if(prop("Habit 7"), 1, 0) + if(prop("Habit 8"), 1, 0))` |
| Total Active | Number | Number of habits currently being tracked |
| Completion % | Formula | `if(prop("Total Active") == 0, 0, round(prop("Habits Done") / prop("Total Active") * 100))` |
| Completion Display | Formula | `format(prop("Completion %")) + "% (" + format(prop("Habits Done")) + "/" + format(prop("Total Active")) + ")"` |
| Perfect Day | Formula | `if(prop("Habits Done") == prop("Total Active"), true, false)` |
| Energy Level | Select | 1 (Crashed) / 2 (Low) / 3 (OK) / 4 (Good) / 5 (Peak) |
| Sleep (hrs) | Number | Hours slept last night |
| Day Rating | Select | Terrible / Bad / OK / Good / Great / Amazing |
| Win | Text | Best thing that happened today |
| Obstacle | Text | What got in the way of habits today? |
| Notes | Text | End of day reflection |
| Linked Habits | Relation | -> Habits master list |

**Views:**

- **Today** — Filter: Date = today (daily working view)
- **This Week** — Filter: Date is within last 7 days, sorted by Date descending
- **This Month** — Filter: Date is within current month, sorted by Date descending
- **Calendar** — Calendar view by Date
- **Perfect Days** — Filter: Perfect Day = true (celebration view)
- **Low Energy Days** — Filter: Energy Level = 1 or 2 (pattern analysis)
- **Weekly Summary** — Table grouped by Week Number, showing average Completion %
- **Monthly Summary** — Table grouped by Month
- **Heatmap View** — Gallery view showing Date and Completion Display with color coding based on percentage

---

## DASHBOARD

> Create this as the top-level page for your habit system. Open it every morning to mark today's check-in and every Sunday during your weekly review to update streaks and rates.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  HABIT TRACKER                                   Week 18, 2026    |
+----------------+--------------+----------------+-----------------+
|  Active Habits |  Weekly Rate  |  Current Best  |  Perfect Days   |
|      6         |    78%       |  21-day streak |  3 this week    |
+----------------+--------------+----------------+-----------------+
|                                                                    |
|  TODAY'S CHECK-IN                                                 |
|  [Linked view -> Daily Check-ins, Date = today]                   |
|  [ ] Meditate 10 min                                              |
|  [ ] Exercise 30 min                                              |
|  [ ] Read 20 pages                                                |
|  [ ] Journal                                                      |
|  [ ] No phone first hour                                          |
|  [ ] Drink 8 glasses water                                        |
|                                                                    |
+----------------------------------+-------------------------------+
|  STREAK BOARD                    |  WEEKLY SCORECARD             |
|  [Linked view -> Habits,         |  [Linked view -> Check-ins,   |
|   Gallery, sorted by Current     |   This Week, showing          |
|   Streak desc]                   |   Completion Display]         |
|                                  |                               |
|  Meditate: 21 days (PB!)        |  Mon: 100% (6/6)             |
|  Exercise: 14 days              |  Tue: 83% (5/6)              |
|  Read: 8 days                   |  Wed: 67% (4/6)              |
|  Journal: 5 days                |  Thu: 100% (6/6)             |
|  No phone: 3 days               |  Fri: 83% (5/6)              |
+----------------------------------+-------------------------------+
|  NEEDS ATTENTION                                                  |
|  [Linked view -> Habits, Needs Attention = true]                  |
+----------------------------------+-------------------------------+
|  THIS MONTH'S STATS              |  HABIT DESIGN                 |
|  [Linked view -> Check-ins,      |  [Linked view -> Habits,      |
|   this month, avg Completion %]  |   showing Cue/Routine/Reward] |
+------------------------------------------------------------------+
```

---

## STREAK LOGIC

### How Streaks Work

Streaks count consecutive days (or required days) a habit was completed without a miss.

**For Daily habits:** Every day counts. Miss one day = streak resets to 0.

**For frequency-based habits (3x/week, etc.):** Streak counts consecutive weeks where you hit the target. Miss a week's target = streak resets.

### Streak Status Formula

```
if(
  prop("Current Streak") == 0,
  "Reset",
  if(
    prop("Current Streak") >= prop("Best Streak"),
    "Personal Best!",
    if(
      prop("Current Streak") >= 21,
      "Locked In",
      if(
        prop("Current Streak") >= 7,
        "Strong",
        if(
          prop("Current Streak") >= 3,
          "Building",
          "Starting"
        )
      )
    )
  )
)
```

**Thresholds explained:**

- **Reset (0):** Streak was broken. No shame — reset and start again.
- **Starting (1-2):** Just getting going. Fragile. Protect it.
- **Building (3-6):** Momentum forming. The hardest phase to push through.
- **Strong (7-20):** Habit is taking hold. Missing would feel like a loss.
- **Locked In (21+):** Research suggests 21+ days begins automaticity. Still not permanent — keep tracking.
- **Personal Best:** You've never been this consistent. Celebrate.

### Updating Streaks (Weekly Review Process)

1. Open this week's Check-in entries
2. For each Active habit, count consecutive completions from today backwards
3. If the habit was done every required day since the last miss: increment Current Streak by 7 (or the relevant number of days)
4. If there was a miss: note the Current Streak, update Best Streak if Current > Best, then reset Current to the count since the last miss
5. Update "This Week Completions" on the Habits master record

---

## COMPLETION RATE FORMULAS

### Daily Completion Percentage

```
if(
  prop("Total Active") == 0,
  0,
  round(prop("Habits Done") / prop("Total Active") * 100)
)
```

### Weekly Rate (on Habits master)

```
if(
  prop("Target Per Week") == 0,
  0,
  round(prop("This Week Completions") / prop("Target Per Week") * 100)
)
```

### Monthly Rate (on Habits master)

```
if(
  prop("Monthly Target") == 0,
  0,
  round(prop("This Month Completions") / prop("Monthly Target") * 100)
)
```

### Monthly Target Calculation

```
round(prop("Target Per Week") * 4.33)
```

4.33 = average weeks per month (52 weeks / 12 months).

### Perfect Day Detection

```
if(prop("Habits Done") == prop("Total Active"), true, false)
```

### Needs Attention Flag

```
if(
  and(
    prop("Status") == "Active",
    prop("Weekly Rate") < 50
  ),
  true,
  false
)
```

Any active habit below 50% weekly completion gets flagged for review — either redesign the habit (make it easier), adjust the frequency, or consciously decide to pause it.

---

## HEATMAP-STYLE TRACKING

Notion doesn't have native heatmaps, but you can simulate one using the Gallery view of Daily Check-ins:

### Setup Instructions

1. Create a Gallery view of Daily Check-ins
2. Set card preview to "None"
3. Show properties: Date, Completion Display
4. Sort by Date ascending
5. Use the Completion % to mentally color-code:
   - 100% = Perfect Day (dark green in your mind)
   - 75-99% = Strong day (light green)
   - 50-74% = Average (yellow)
   - 25-49% = Weak day (orange)
   - 0-24% = Miss (red)

### Alternative: Weekly Heatmap Table

Create a table view grouped by Week Number showing:

- Each day's Completion % in sequence
- Weekly average as the group header
- Scan down the weeks to spot patterns (do you always dip on Wednesdays? Improve weekends?)

---

## HABIT DESIGN FRAMEWORK

For each new habit, fill in these fields on the Habits master record:

### Cue (What triggers it?)
Be hyper-specific. "After I pour my morning coffee" not "in the morning."

### Routine (What's the exact behavior?)
Define the minimum viable version AND the ideal version:

- Minimum: "Open journal and write 1 sentence"
- Ideal: "Journal for 10 minutes about yesterday's wins and today's priorities"

### Reward (What makes it satisfying?)
Immediate reward that happens right after completion. "Check the box and see the streak increment" works for some people. Others need "then I get to scroll Instagram for 5 minutes."

### Habit Stacking Formula
"After [CURRENT HABIT], I will [NEW HABIT]."
Record this in the "Stacked After" field so your daily routine sequence is clear.

---

## WEEKLY REVIEW TEMPLATE (every Sunday, 10 minutes)

1. **Score the week** — Open "This Week" view in Check-ins. Note your best and worst days. What patterns do you see?

2. **Update streaks** — For each active habit:
   - Count this week's completions
   - Update "This Week Completions" on the Habits master record
   - If streak is still alive: add to Current Streak
   - If broken: update Best Streak if needed, then reset Current Streak to days since last miss

3. **Check "Needs Attention"** — Any habit below 50%? For each:
   - Is the habit too hard? Reduce to minimum viable version for next week.
   - Is the cue broken? Change the trigger.
   - Is this habit still a priority? If not, change Status to Paused.

4. **Celebrate wins** — Note your longest active streak. Any Personal Bests? Any Perfect Days?

5. **Set next week's intention** — Which habit gets extra focus next week? Write it down.

---

## MONTHLY REVIEW TEMPLATE (first Sunday of month, add 10 minutes)

1. **Calculate monthly rates** — Update "This Month Completions" for each habit. Check Monthly Rate Display.

2. **Update Best Streaks** — If any Current Streak > Best Streak, update.

3. **Trend analysis:**
   - Which habits consistently hit 80%+? These are locked in.
   - Which habits hover around 50%? These need redesign or deprioritization.
   - Which habits are below 30%? Either fix them this month or retire them.

4. **Habit audit:**
   - Are you tracking too many? (More than 8 active habits creates willpower fatigue)
   - Add any new habits? (Only if an existing habit is "Locked In" status)
   - Retire any? (Move to Retired status — keep the data, stop tracking)

5. **Reset "This Month Completions"** to 0 on all habits for the new month.

---

## QUICK-START GUIDE

### Step 1 — Choose 3-5 Habits (not more)

- Open the **Habits** database
- Add 3-5 habits you genuinely want to build (resist adding more — you can always add later)
- For each: set Category, Frequency, Target Per Week, Time of Day
- Fill in the Cue/Routine/Reward fields — this is what makes habits stick
- Write the Minimum Viable Version for each (your "bad day" version)
- Set Status = Active

### Step 2 — Configure Your Check-in

- Open the **Daily Check-ins** database
- Rename the Habit checkbox properties to match your actual habits (Habit 1 = "Meditate 10 min", etc.)
- Set "Total Active" to match how many habits you're tracking
- Create today's entry and test that Completion % calculates correctly

### Step 3 — Start Tracking (today)

- Each day, create a new Check-in entry (or duplicate yesterday's and uncheck all boxes)
- Check boxes as you complete habits throughout the day
- Optional: note Energy Level and any Obstacles at end of day

### Step 4 — First Weekly Review (Sunday)

- After your first full week, follow the Weekly Review Template
- Update streaks and weekly completions on the Habits master records
- Check: does the system feel manageable? If not, reduce habits to 3.

### Step 5 — Build the Dashboard

- Create a new page titled "Habit Tracker"
- Add linked views as shown in the Dashboard Layout
- Pin to your sidebar for daily access

### Pro Tips

- Never start with more than 5 habits. The research is clear: willpower is limited. Start with 3, lock them in (21+ day streaks), then add one more.
- The Minimum Viable Version is your secret weapon. On bad days, do the 2-minute version. A 2-minute meditation still counts as a streak day. A single pushup still counts. Showing up matters more than intensity.
- Track for data, not for guilt. A "missed" day is data about your environment, energy, and habit design — not evidence of personal failure.
- Use the "Needs Attention" view as a weekly diagnostic. Habits below 50% are telling you something: the cue isn't working, the routine is too hard, or you don't actually care about this habit. Listen.
- The "don't break the chain" method works because loss aversion is more motivating than gain. Once you have a streak going, the desire to protect it becomes its own motivation. But if it breaks — reset immediately. Don't let shame keep you away for days.
- Habit stacking is the fastest way to build new habits. Attach every new habit to an existing anchor ("After I brush my teeth, I will...") — never leave a habit floating in abstract time.
- Monthly audits prevent habit creep. Every month, ask: "Would I add this habit today if I weren't already tracking it?" If no, retire it.
