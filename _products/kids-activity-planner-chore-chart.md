# Kids Activity Planner & Chore Chart — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with point calculations, reward tracking, and rotation formulas built in. Designed for families with kids ages 4-12. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Kids / Family Members

**Purpose:** Profile for each child in the family. Stores age, interests, point balances, and links to their chores, activities, and screen time records.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Name | Title | Child's name |
| Age | Number | Current age |
| Birth Date | Date | For auto-updating age |
| Grade | Select | Pre-K / K / 1st / 2nd / 3rd / 4th / 5th / 6th / 7th / 8th |
| Photo | Files & media | Kid's photo for dashboard |
| Total Points | Number | Running point balance (earned - spent) |
| Points This Week | Number | Points earned this week |
| Weekly Points Goal | Number | Target points per week |
| Goal Progress | Formula | `if(prop("Weekly Points Goal") == 0, "No goal set", format(round(prop("Points This Week") / prop("Weekly Points Goal") * 100)) + "%")` |
| Streak (weeks meeting goal) | Number | Consecutive weeks hitting point goal |
| Interests | Multi-select | Sports / Art / Music / Reading / Science / Cooking / Animals / Gaming / Building / Dance / Nature / Crafts |
| Allergies/Restrictions | Text | Food allergies, activity restrictions |
| Personality Notes | Text | What motivates them, what triggers resistance |
| Linked Chores | Relation | -> Chores database |
| Linked Activities | Relation | -> Activities database |
| Linked Screen Time | Relation | -> Screen Time database |
| Chores Completed This Week | Rollup | Count of linked Chores where Status = Done AND this week |
| Active Activities | Rollup | Count of linked Activities where Status = Active |
| Notes | Text | Current goals, behavior observations |

**Views:**

- **Family Dashboard** — Gallery with Photo, showing Points, Streak, Goal Progress
- **All Kids** — Table with full details
- **Points Leaderboard** — Sorted by Points This Week descending (friendly competition)

---

### 2. Chores / Responsibilities

**Purpose:** Every chore assignment for every child. Tracks daily/weekly completion, point values, and whether it was done without reminders. Drives the reward system.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Chore | Title | Specific task name (e.g., "Make bed", "Feed the dog") |
| Assigned To | Relation | -> Kids database |
| Child Name | Rollup | From Assigned To relation |
| Category | Select | Morning Routine / After School / Evening / Kitchen / Pets / Cleaning / Laundry / Outdoor / Homework / Self-Care |
| Frequency | Select | Daily / Weekdays / Weekends / Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday / Weekly |
| Day | Select | Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday / Any |
| Time of Day | Select | Morning / After School / Before Dinner / After Dinner / Bedtime |
| Point Value | Number | Points earned for completion |
| Bonus Points | Number | Extra points if done without reminder |
| Total Points Possible | Formula | `prop("Point Value") + prop("Bonus Points")` |
| Status | Select | Assigned / In Progress / Done / Skipped / Helped |
| Done Without Reminder | Checkbox | Initiative bonus! |
| Points Earned | Formula | `if(prop("Status") == "Done", if(prop("Done Without Reminder"), prop("Point Value") + prop("Bonus Points"), prop("Point Value")), 0)` |
| Date | Date | Date this chore entry is for |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Quality | Select | Excellent / Good / Needs Redo / N/A |
| Time Limit (min) | Number | Expected time to complete |
| Age Appropriate | Text | Minimum age for this chore |
| Teaching Notes | Text | How to teach this chore, steps broken down |
| Notes | Text | Any issues, adjustments needed |
| Verified By | Select | Mom / Dad / Self / Other |
| Tags | Multi-select | Earns Extra / Team Chore / Independent / New / Mastered |

**Views:**

- **Today's Chores** — Filter: Day = today's day OR Frequency = Daily, grouped by Child Name
- **This Week** — Table, grouped by Day, filtered to current week
- **By Child** — Table, grouped by Child Name, showing Status
- **Chore Chart** — Board, grouped by Status (To Do / Done)
- **Not Done** — Filter: Status = Assigned or Skipped
- **By Category** — Table, grouped by Category
- **Points Summary** — Table showing Chore, Points Earned, grouped by Child
- **Weekly Scoreboard** — Table grouped by Week, showing total Points Earned per child
- **Master Chore List** — All unique chores (for rotation planning)
- **Morning Routine** — Filter: Category = Morning Routine, today, by child
- **Evening Routine** — Filter: Category = Evening, today, by child

---

### 3. Activities / Classes

**Purpose:** Tracks all extracurricular activities, classes, sports, and scheduled events for each child. Includes schedules, costs, locations, and logistics. Prevents over-scheduling and manages the family calendar.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Activity Name | Title | Name of class or activity |
| Child | Relation | -> Kids database |
| Child Name | Rollup | From Child relation |
| Category | Select | Sports / Art / Music / Dance / Academic / Social / Religious / Outdoor / Camps / Scouts / Language / Martial Arts / Other |
| Status | Select | Active / On Break / Considering / Ended / Waitlisted |
| Day(s) | Multi-select | Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday |
| Time | Text | Start and end time (e.g., "4:00-5:30 PM") |
| Location | Text | Address or facility name |
| Instructor/Coach | Text | Contact name |
| Contact Info | Text | Phone/email for instructor or facility |
| Season | Select | Year-Round / Fall / Winter / Spring / Summer / Semester |
| Start Date | Date | When this activity begins |
| End Date | Date | When it ends |
| Cost | Number (USD) | Total cost for the session/season |
| Cost Per Month | Formula | `if(and(not(empty(prop("Start Date"))), not(empty(prop("End Date")))), round(prop("Cost") / max(dateBetween(prop("End Date"), prop("Start Date"), "months"), 1)), prop("Cost"))` |
| Payment Due | Date | Next payment date |
| Paid | Checkbox | Current session paid? |
| Equipment Needed | Text | What gear/supplies are required |
| Carpool | Text | Carpool details/partners |
| Transportation | Select | Parent Drive / Carpool / Bus / Walk / Bike |
| Child Enthusiasm | Select | Loves It / Likes It / Neutral / Resistant / Wants to Quit |
| Parent Priority | Select | High (keep) / Medium / Low (could drop) / Trial |
| Conflicts With | Text | Any scheduling conflicts |
| Notes | Text | Performance notes, upcoming events, recitals |
| Tags | Multi-select | Competition / Recital Coming / Registration Due / Equipment Needed / Scholarship |

**Views:**

- **Active Activities** — Table, grouped by Child Name, filtered to Status = Active
- **Weekly Schedule** — Table, grouped by Day(s), filtered to Active
- **By Category** — Table, grouped by Category
- **Cost Overview** — Table showing Activity, Cost, Cost Per Month (total family spend)
- **Calendar** — Calendar view by Start Date
- **Considering** — Filter: Status = Considering (for family discussion)
- **By Enthusiasm** — Table, grouped by Child Enthusiasm (spot burnout)
- **Payment Due** — Filter: Paid = false, sorted by Payment Due
- **Upcoming Events** — Filter: Tags contains Recital or Competition

---

### 4. Screen Time Tracker

**Purpose:** Logs daily screen time per child with types of usage and earned vs. free time distinction. Makes screen time rules visible and quantifiable — the chart is the rule, not the parent.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry | Title | "[Child] — [Date]" or brief description |
| Child | Relation | -> Kids database |
| Child Name | Rollup | From Child relation |
| Date | Date | Which day |
| Day Type | Select | School Day / Weekend / Holiday / Sick Day |
| Daily Limit (min) | Number | Allowed minutes for this day type |
| Earned Time (min) | Number | Extra minutes earned through chores/reading/activity |
| Total Allowed | Formula | `prop("Daily Limit (min)") + prop("Earned Time (min)")` |
| Actual Used (min) | Number | Minutes actually used |
| Remaining | Formula | `prop("Total Allowed") - prop("Actual Used (min)")` |
| Over Limit | Formula | `if(prop("Actual Used (min)") > prop("Total Allowed"), true, false)` |
| Over By | Formula | `if(prop("Over Limit"), format(prop("Actual Used (min)") - prop("Total Allowed")) + " min over", "Within limit")` |
| Content Type | Multi-select | Educational / TV Show / Movie / Gaming / YouTube / Social Media / Creative (drawing apps) / Reading App / Video Call / Homework |
| Device | Select | iPad / Computer / TV / Phone / Gaming Console / Kindle |
| Quality | Select | Educational / Creative / Passive / Social / Mixed |
| Notes | Text | What they watched/played, any concerns |
| Earned By | Text | How extra time was earned (e.g., "30 min reading = 15 min extra") |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Weekly Total | Number | Total minutes this week (update during review) |
| Weekly Limit | Number | Maximum weekly minutes |

**Views:**

- **Today** — Filter: Date = today, grouped by Child Name
- **This Week** — Table, grouped by Child Name, showing daily Actual Used
- **Over Limit** — Filter: Over Limit = true (conversations needed)
- **By Child** — Table, grouped by Child Name, sorted by Date descending
- **Content Log** — Table showing Content Type and Quality
- **Calendar** — Calendar view by Date
- **Weekly Summary** — Table, grouped by Week, showing Weekly Total per child

---

### 5. Meal Rotation (Picky Eaters)

**Purpose:** Manages family meals with picky eater considerations. Tracks which foods each child accepts, rotates meals to prevent fatigue, and builds toward introducing new foods gradually.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Meal/Food | Title | Name of dish or food item |
| Meal Type | Select | Breakfast / Lunch / Dinner / Snack |
| Category | Select | Protein / Grain / Vegetable / Fruit / Dairy / Combo Meal / Treat |
| Child Acceptance | Multi-select | [Child 1 name] / [Child 2 name] / [Child 3 name] / Everyone / No One Yet |
| Acceptance Level | Select | Loves / Likes / Tolerates / Will Eat If Hungry / Refuses / New (untried) |
| Prep Time | Select | No Prep / 5 min / 15 min / 30 min / 45 min / 1 hr+ |
| Allergen Free | Multi-select | Dairy-Free / Gluten-Free / Nut-Free / Egg-Free / Soy-Free |
| Nutrition | Multi-select | High Protein / Iron-Rich / Calcium / Fiber / Vitamin C / Omega-3 |
| Last Served | Date | When this was most recently made |
| Days Since Served | Formula | `if(empty(prop("Last Served")), "Never served", format(dateBetween(now(), prop("Last Served"), "days")) + " days")` |
| Times Served (month) | Number | How often this month |
| Rotation Status | Formula | `if(empty(prop("Last Served")), "Add to rotation", if(dateBetween(now(), prop("Last Served"), "days") > 14, "Due for rotation", if(dateBetween(now(), prop("Last Served"), "days") > 7, "Can serve again", "Recently served")))` |
| Introduction Strategy | Text | For new foods: how to introduce (e.g., "serve alongside safe food") |
| Serving Notes | Text | How to prepare/present for maximum acceptance |
| Recipe Link | URL | Link to recipe if applicable |
| Tags | Multi-select | Quick / Batch Cookable / Freezer Friendly / Lunch Box / Road Trip / Restaurant Order / Safe Food |

**Views:**

- **All Foods** — Table, grouped by Meal Type
- **Accepted by Everyone** — Filter: Child Acceptance contains "Everyone"
- **Safe Foods** — Filter: Tags contains Safe Food (guaranteed eats)
- **Due for Rotation** — Filter: Rotation Status = "Due for rotation"
- **New Foods to Try** — Filter: Acceptance Level = New (untried)
- **By Acceptance** — Board, grouped by Acceptance Level
- **Breakfast Options** — Filter: Meal Type = Breakfast AND (Acceptance Level = Loves or Likes)
- **Lunch Box Ideas** — Filter: Tags contains Lunch Box, sorted by Last Served
- **Quick Meals (< 15 min)** — Filter: Prep Time = No Prep or 5 min or 15 min
- **Allergen-Safe** — Filter by relevant allergen tags
- **This Week's Plan** — Manual curation from Due for Rotation view

---

## DASHBOARD

> Create this as the top-level page. The whole family can see it — or display it on a shared tablet in the kitchen. Shows today's chores, activity schedule, screen time status, and point standings.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  FAMILY HQ                                   Today: Tuesday       |
+------------------------------------------------------------------+
|  POINT STANDINGS                                                  |
|  [Linked view -> Kids, Gallery with Photo and Points]             |
|                                                                    |
|  Emma: 47 pts (Goal: 50)    Jack: 38 pts (Goal: 40)             |
|  Streak: 3 weeks            Streak: 1 week                       |
|                                                                    |
+----------------------------------+-------------------------------+
|  TODAY'S CHORES                  |  TODAY'S SCHEDULE              |
|  [Linked view -> Chores,         |  [Linked view -> Activities,   |
|   today, grouped by child]       |   today's day, Active]        |
|                                  |                               |
|  Emma:                           |  3:30 - Emma: Piano           |
|  [ ] Make bed (2 pts)           |  4:00 - Jack: Soccer          |
|  [ ] Set table (3 pts)          |  5:30 - Both: Swim class      |
|  [ ] Homework (5 pts)           |                               |
|                                  |                               |
|  Jack:                           |                               |
|  [ ] Make bed (2 pts)           |                               |
|  [ ] Feed dog (3 pts)           |                               |
|  [ ] Pick up toys (2 pts)       |                               |
+----------------------------------+-------------------------------+
|  SCREEN TIME TODAY               |  DINNER OPTIONS               |
|  [Linked view -> Screen Time,    |  [Linked view -> Meal         |
|   today]                         |   Rotation, Due for Rotation, |
|                                  |   Dinner, Accepted by         |
|  Emma: 22/45 min used           |   Everyone]                   |
|  Jack: 30/30 min used (done!)   |                               |
+----------------------------------+-------------------------------+
|  REWARDS AVAILABLE                                                |
|  10 pts: Extra 15 min screen time                                |
|  20 pts: Choose dinner / movie night pick                         |
|  50 pts: New book / small toy                                     |
|  100 pts: Special outing / bigger reward                          |
+------------------------------------------------------------------+
```

---

## POINTS & REWARDS SYSTEM

### Point Values by Chore Difficulty

| Difficulty | Base Points | Bonus (no reminder) | Examples |
|---|---|---|---|
| Easy | 1-2 | +1 | Make bed, put shoes away, clear plate |
| Medium | 3-4 | +2 | Set/clear table, feed pet, tidy room |
| Hard | 5-7 | +3 | Load dishwasher, fold laundry, homework without complaint |
| Extra | 8-10 | +5 | Help cook dinner, deep clean room, yard work |

### Earning Extra Screen Time

| Activity | Screen Time Earned |
|---|---|
| 30 min reading | +15 min |
| Complete all daily chores | +10 min |
| Chores done without reminder | +5 min |
| Physical activity (30+ min) | +15 min |
| Help a sibling | +10 min |
| Practice instrument (20 min) | +10 min |

### Reward Menu (customize per family)

| Points | Reward Options |
|---|---|
| 10 | Extra 15 min screen time / Stay up 15 min later / Choose breakfast |
| 20 | Choose dinner / Movie night pick / Skip one chore |
| 30 | Friend sleepover / Special dessert / Extra allowance |
| 50 | New book or small toy / Special 1-on-1 outing with parent |
| 75 | Choose a family activity / Bigger purchase ($10-15) |
| 100 | Major reward (movie theater, special event, $20 item) |

---

## KEY FORMULA REFERENCE

### Points Earned per Chore

```
if(
  prop("Status") == "Done",
  if(
    prop("Done Without Reminder"),
    prop("Point Value") + prop("Bonus Points"),
    prop("Point Value")
  ),
  0
)
```

### Weekly Goal Progress (Kids)

```
if(
  prop("Weekly Points Goal") == 0,
  "No goal set",
  format(round(prop("Points This Week") / prop("Weekly Points Goal") * 100)) + "%"
)
```

### Screen Time Remaining

```
prop("Total Allowed") - prop("Actual Used (min)")
```

### Over Limit Detection

```
if(
  prop("Actual Used (min)") > prop("Total Allowed"),
  true,
  false
)
```

### Meal Rotation Status

```
if(
  empty(prop("Last Served")),
  "Add to rotation",
  if(
    dateBetween(now(), prop("Last Served"), "days") > 14,
    "Due for rotation",
    if(
      dateBetween(now(), prop("Last Served"), "days") > 7,
      "Can serve again",
      "Recently served"
    )
  )
)
```

### Activity Cost Per Month

```
if(
  and(not(empty(prop("Start Date"))), not(empty(prop("End Date")))),
  round(prop("Cost") / max(dateBetween(prop("End Date"), prop("Start Date"), "months"), 1)),
  prop("Cost")
)
```

### Total Allowed Screen Time

```
prop("Daily Limit (min)") + prop("Earned Time (min)")
```

---

## SCREEN TIME RULES (customizable)

### Default Daily Limits

| Day Type | Suggested Limit | Notes |
|---|---|---|
| School Day | 30-45 min | After homework and chores |
| Weekend | 60-90 min | Can be split morning/afternoon |
| Holiday/Break | 60-120 min | More flexibility, still has a cap |
| Sick Day | Flexible | Comfort takes priority |

### Quality Tiers

- **Tier 1 (unlimited/doesn't count):** Educational apps (approved), creative tools (drawing, music), video calls with family
- **Tier 2 (counts toward limit):** TV shows, YouTube (curated), age-appropriate gaming
- **Tier 3 (special permission):** Social media (age 10+), unrestricted YouTube, mature-rated content

---

## QUICK-START GUIDE

### Step 1 — Add Your Kids (5 minutes)

- Open the **Kids** database
- Add each child with Age, Grade, Interests
- Set a Weekly Points Goal (start low — they can always earn more)
- Write Personality Notes (what motivates each child — crucial for the reward system working)

### Step 2 — Create the Chore List (15 minutes)

- Open the **Chores** database
- Add age-appropriate chores for each child
- Assign Point Values (see Point Values table above)
- Set Frequency and Time of Day
- Write Teaching Notes for new or complex chores
- Start with 3-4 chores per child per day (don't overwhelm)

### Step 3 — Set Up Activities (10 minutes)

- Open **Activities** and add all current extracurricular activities
- Include Day(s), Time, Location, and Cost
- Note Child Enthusiasm — this matters more than parent preference
- Calculate total weekly activity load — more than 3-4 per child may be over-scheduled

### Step 4 — Define Screen Time Rules (10 minutes)

- Open **Screen Time** and set Daily Limit for each day type
- Discuss with kids: what earns extra time?
- Create today's entry for each child
- Post the rules somewhere visible (the dashboard serves this purpose)

### Step 5 — Build the Meal Rotation (15 minutes)

- Open **Meal Rotation** and add 20-30 foods/meals your family eats
- Mark Child Acceptance for each item honestly
- Identify "Safe Foods" (guaranteed acceptance from all kids)
- Add 5-10 "New" foods you'd like to introduce gradually

### Step 6 — Create the Family Dashboard

- Build the top-level page following the Dashboard Layout
- Consider displaying on a family tablet in the kitchen
- Pin to sidebar for parent access on phone

### Step 7 — Introduce to Kids

- Family meeting: explain the point system and reward menu together
- Let kids weigh in on rewards (buy-in matters)
- Start with a "soft launch" week where you track but don't penalize
- Celebrate early wins loudly — the system works through positive reinforcement, not punishment

### Daily Rhythm

**Morning:**

- Kids check "Today's Chores" for morning routine
- Parent verifies completion and checks "Done"

**After School:**

- Check activity schedule for the day
- Complete after-school chores before screen time
- Log any screen time used

**Evening:**

- Complete evening chores
- Parent marks all done/not done
- Calculate daily points together
- Quick wins: "You earned 12 points today! 3 more days like this and you hit your weekly goal."

**Weekly (Sunday, 10 minutes):**

- Tally weekly points
- Check if Weekly Points Goal was met (update Streak)
- Let kids "spend" points on rewards from the menu
- Reset "Points This Week" for new week
- Review screen time totals — any patterns to address?

### Pro Tips

- The "Done Without Reminder" bonus is the secret weapon. It incentivizes initiative without nagging. Kids learn that self-starting is literally worth more.
- Never take away earned points as punishment. Points are earned through labor — removing them teaches that effort doesn't matter. Use a separate consequence system for behavior.
- Rotate chores monthly so no child is permanently stuck with the worst job. Rotation also builds competence across all household tasks.
- The Meal Rotation prevents the "we always eat chicken nuggets" trap. When meals cycle through a 2-week rotation, kids get variety without the nightly negotiation.
- For picky eaters: use the "Introduction Strategy" field. Repeated low-pressure exposure (serve alongside safe food, no requirement to eat) works. It takes 10-15 exposures before most kids accept a new food.
- Screen time limits only work when they're predictable. Kids who know their limit in advance argue less than kids told "that's enough" arbitrarily.
- Adjust point goals upward gradually. Start easy (70% achievable), then raise the bar as habits form. Constant failure kills motivation.
- The Activity "Enthusiasm" field prevents burnout. If a child is "Resistant" for 3+ weeks, it's time for a conversation about continuing. Forced activities build resentment, not skills.
