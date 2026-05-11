# Pregnancy & Baby Tracker — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with milestone tracking, appointment scheduling, and growth measurement formulas built in. Covers pregnancy through baby's first year. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Weekly Milestones (Pregnancy)

**Purpose:** Week-by-week pregnancy tracker from Week 4 through Week 40. Pre-populated with fetal development milestones, common symptoms, and weekly prompts. Your journal through pregnancy.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Week | Title | "Week [N]" (e.g., "Week 12") |
| Week Number | Number | 4 through 40 |
| Trimester | Formula | `if(prop("Week Number") <= 13, "First Trimester", if(prop("Week Number") <= 27, "Second Trimester", "Third Trimester"))` |
| Date Range | Text | Calendar dates for this week (fill in based on due date) |
| Baby Size | Text | Fun size comparison (e.g., "Lemon", "Avocado", "Butternut Squash") |
| Baby Development | Text | What's developing this week (pre-filled with medical milestones) |
| Your Body | Text | Common physical changes this week |
| Symptoms | Multi-select | Nausea / Fatigue / Food Aversions / Cravings / Heartburn / Back Pain / Insomnia / Swelling / Braxton Hicks / Round Ligament Pain / Frequent Urination / Mood Swings / Headaches / Congestion |
| Symptom Notes | Text | Your specific experience this week |
| Energy Level | Select | Low / Medium / High / Variable |
| Mood | Select | Happy / Anxious / Emotional / Calm / Overwhelmed / Excited / Nervous |
| Cravings | Text | What you're craving this week |
| Aversions | Text | What you can't stand right now |
| Weight | Number | Current weight (optional — no judgment) |
| Blood Pressure | Text | If tracking (format: 120/80) |
| Bump Photo | Files & media | Weekly bump photo |
| Doctor Notes | Text | Anything from this week's appointment |
| Questions for Next Appt | Text | Things to ask at next visit |
| To-Do This Week | Text | Prep tasks relevant to this stage |
| Journal Entry | Text | Free-form weekly thoughts and feelings |
| Highlight | Text | Best moment of this week |
| Partner Notes | Text | Notes for/from partner |
| Status | Select | Upcoming / Current / Completed / Skipped |

**Views:**

- **Current Week** — Filter: Status = Current (single entry working view)
- **Full Timeline** — Table, sorted by Week Number ascending
- **By Trimester** — Table, grouped by Trimester
- **Symptom Tracker** — Table showing Week, Symptoms, Energy Level, Mood
- **Bump Gallery** — Gallery view with Bump Photo, sorted by Week Number
- **Journal** — Table showing Week, Journal Entry, Highlight
- **Completed** — Filter: Status = Completed

---

### 2. Appointments

**Purpose:** All prenatal and postnatal appointments — OB visits, ultrasounds, lab work, specialist consultations, and pediatric visits. Tracks questions to ask, results received, and follow-up needed.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Appointment | Title | Type + provider (e.g., "20-Week Anatomy Scan — Dr. Martinez") |
| Date | Date | Appointment date and time |
| Type | Select | Routine OB / Ultrasound / Lab Work / Glucose Test / Non-Stress Test / Specialist / Lactation / Pediatrician / Postpartum / Emergency / Other |
| Provider | Text | Doctor/midwife name |
| Location | Text | Office/hospital address |
| Status | Select | Scheduled / Completed / Rescheduled / Cancelled |
| Week (Pregnancy) | Number | What pregnancy week this falls in |
| Questions to Ask | Text | Prepared list of questions for this visit |
| Results/Notes | Text | What was discussed, findings, instructions |
| Test Results | Text | Lab values, measurements, etc. |
| Follow-Up Needed | Checkbox | Requires action after appointment |
| Follow-Up Action | Text | What needs to happen |
| Follow-Up Date | Date | When to follow up |
| Next Appointment | Date | When the next visit is scheduled |
| Cost | Number (USD) | Co-pay or out-of-pocket |
| Insurance Filed | Checkbox | Has claim been submitted |
| Documents | Files & media | Ultrasound photos, lab results, forms |
| Baby Related | Checkbox | Is this for baby (vs. pregnancy/mom) |
| Baby Age at Appt | Text | For postnatal — "2 weeks", "2 months", etc. |
| Vaccines Given | Text | For pediatric well-visits |
| Growth Percentiles | Text | Height/weight/head percentiles from visit |
| Tags | Multi-select | Urgent / Routine / Milestone / Insurance Issue |

**Views:**

- **Upcoming** — Filter: Status = Scheduled, sorted by Date ascending
- **All Appointments** — Table, sorted by Date descending
- **Prenatal** — Filter: Baby Related = false, sorted by Date
- **Pediatric** — Filter: Baby Related = true, sorted by Date
- **Calendar** — Calendar view by Date
- **Needs Follow-Up** — Filter: Follow-Up Needed = true AND Status = Completed
- **Lab Results** — Filter: Type = Lab Work or Glucose Test, showing Test Results
- **Ultrasounds** — Filter: Type = Ultrasound, showing Documents

---

### 3. Baby Gear Checklist

**Purpose:** Everything you need for baby — organized by category, priority, and budget. Tracks what you own, what's on your registry, and what still needs purchasing. Prevents duplicate purchases and over-buying.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Item | Title | Specific product name |
| Category | Select | Nursery / Feeding / Diapering / Clothing / Bath / Travel / Safety / Play / Health / Postpartum / Hospital Bag |
| Priority | Select | Essential / Important / Nice-to-Have / Luxury / Skip |
| Status | Select | Need / On Registry / Purchased / Received / Borrowed / Hand-Me-Down / Skipping |
| Quantity Needed | Number | How many you need |
| Quantity Have | Number | How many you currently have |
| Brand/Product | Text | Specific brand and model chosen |
| Where to Buy | Text | Store or website |
| Product URL | URL | Link to product |
| Price | Number (USD) | Cost per item |
| Total Cost | Formula | `prop("Price") * prop("Quantity Needed")` |
| Purchased | Checkbox | Already bought |
| Registry | Select | Amazon / Target / Babylist / Buy Buy Baby / Not on Registry |
| Need By | Select | Before Birth / First Month / Month 2-3 / Month 4-6 / Month 6-12 / When Needed |
| Size | Text | Size if applicable (NB, 0-3M, etc.) |
| Condition | Select | New / Used / Either |
| Notes | Text | Why this one, alternatives, reviews read |
| Received From | Text | Who gifted this (for thank-you notes) |
| Thank You Sent | Checkbox | Have you sent the thank-you? |
| Tags | Multi-select | Splurge / Budget Pick / Secondhand OK / Gender Neutral / Registry Item / Must Research |

**Views:**

- **Full Checklist** — Table, grouped by Category
- **Still Need** — Filter: Status = Need, sorted by Priority
- **Registry Items** — Filter: Status = On Registry, grouped by Registry
- **By Priority** — Table, grouped by Priority
- **Essential Only** — Filter: Priority = Essential
- **Need Before Birth** — Filter: Need By = Before Birth, Status != Purchased/Received
- **Budget Summary** — Table showing Category, sum of Total Cost
- **Thank-You Tracker** — Filter: Received From is not empty, showing Thank You Sent
- **Hospital Bag** — Filter: Category = Hospital Bag

---

### 4. Feeding & Sleep Log

**Purpose:** Daily tracking for newborn feeding (breast, bottle, solids) and sleep patterns. Reveals patterns over time — when baby eats best, sleep regressions, and growth spurt indicators. One entry per feeding or sleep session.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry | Title | Auto: "[Date] — [Type]" or brief note |
| Date | Date | Date and time |
| Baby Age | Text | Weeks/months old (e.g., "6 weeks", "4 months") |
| Type | Select | Breastfeed / Bottle (Breast Milk) / Bottle (Formula) / Solids / Snack / Sleep / Nap / Wake |
| Side | Select | Left / Right / Both / N/A (for breastfeeding) |
| Duration (min) | Number | How long for feeds or sleep |
| Amount (oz) | Number | For bottles — ounces consumed |
| Food/Notes | Text | For solids: what was offered. For feeds: latch notes, issues |
| Sleep Start | Text | Time baby fell asleep |
| Sleep End | Text | Time baby woke |
| Sleep Location | Select | Crib / Bassinet / Carrier / Stroller / Car / Co-sleep / Swing / Arms |
| Night Wakes | Number | Number of times baby woke (for overnight entries) |
| Diaper | Select | Wet / Dirty / Both / Dry |
| Diaper Notes | Text | Color, consistency (for newborn health tracking) |
| Mood Before | Select | Calm / Fussy / Crying / Drowsy / Alert / Playful |
| Mood After | Select | Content / Fussy / Still Hungry / Asleep / Playful |
| Spit Up | Checkbox | Did baby spit up? |
| New Food Introduced | Text | If introducing solids — what was new today |
| Reaction | Select | Loved It / Accepted / Rejected / Allergic Reaction / N/A |
| Notes | Text | Observations, concerns, wins |
| Day Number | Formula | `formatDate(prop("Date"), "D")` |
| Week | Formula | `formatDate(prop("Date"), "W")` |

**Views:**

- **Today's Log** — Filter: Date = today, sorted by Date descending
- **All Entries** — Table, sorted by Date descending
- **Feeds Only** — Filter: Type = Breastfeed or Bottle (any), sorted by Date
- **Sleep Only** — Filter: Type = Sleep or Nap, sorted by Date
- **By Week** — Table, grouped by Week
- **Night Log** — Filter: Sleep entries between 7pm-7am
- **New Foods** — Filter: New Food Introduced is not empty (for allergen tracking)
- **Reactions** — Filter: Reaction = Allergic Reaction (critical tracking)
- **Calendar** — Calendar view by Date
- **Diaper Log** — Filter: Diaper is not empty, sorted by Date

---

### 5. Growth & Milestones (Baby)

**Purpose:** Tracks baby's physical growth (weight, length, head circumference) and developmental milestones from birth through 12 months. Aligned with AAP developmental guidelines.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Milestone | Title | Name of measurement or milestone |
| Date | Date | When observed or measured |
| Type | Select | Measurement / Motor / Language / Social / Cognitive / Self-Care |
| Category | Select | Growth Check / Gross Motor / Fine Motor / Communication / Problem Solving / Personal-Social |
| Age at Milestone | Text | Baby's age (e.g., "2 months", "6 months") |
| Weight (lbs) | Number | Current weight |
| Length (in) | Number | Current length/height |
| Head Circumference (in) | Number | Head measurement |
| Weight Percentile | Number | From pediatrician |
| Length Percentile | Number | From pediatrician |
| Head Percentile | Number | From pediatrician |
| Expected Age Range | Text | When this milestone typically occurs (e.g., "4-6 months") |
| Achieved | Checkbox | Has baby reached this milestone? |
| Status | Select | Not Yet / Emerging / Achieved / Advanced / Concern |
| Notes | Text | Details, observations, funny moments |
| Photo/Video | Files & media | Capture the moment |
| Source | Select | Parent Observation / Pediatrician / Therapist |
| Discussed with Doctor | Checkbox | Mentioned at an appointment? |
| Tags | Multi-select | First Time / Celebration / Concern / Ahead of Schedule / Right on Time |

**Views:**

- **All Milestones** — Table, sorted by Date descending
- **Growth Chart** — Filter: Type = Measurement, sorted by Date ascending (for plotting)
- **Developmental** — Filter: Type != Measurement, grouped by Category
- **Achieved** — Filter: Achieved = true, sorted by Date
- **Upcoming** — Filter: Status = Not Yet or Emerging
- **Concerns** — Filter: Status = Concern (bring to pediatrician)
- **By Age** — Table, grouped by Age at Milestone
- **Photo Gallery** — Gallery view with Photo/Video
- **Motor Milestones** — Filter: Type = Motor
- **Language Milestones** — Filter: Type = Language

---

## DASHBOARD

> Create this as the top-level page. During pregnancy, it shows your weekly progress and upcoming appointments. After birth, it shifts to feeding/sleep patterns and milestone tracking.

### Dashboard Layout — Pregnancy Mode

```
+------------------------------------------------------------------+
|  PREGNANCY TRACKER                            Due: August 15, 2026 |
+----------------+--------------+----------------+-----------------+
|  Current Week  |  Trimester   |  Days Until    |  Next Appt      |
|  Week 24       |  Second      |  Due: 112 days |  Jun 2 (OB)     |
+----------------+--------------+----------------+-----------------+
|                                                                    |
|  THIS WEEK                                                        |
|  [Linked view -> Weekly Milestones, Status = Current]             |
|  Baby is the size of: Corn on the cob                             |
|  Development: Lungs developing surfactant...                      |
|  Your body: Belly button popping, round ligament pain...          |
|                                                                    |
+----------------------------------+-------------------------------+
|  UPCOMING APPOINTMENTS           |  TO-DO BEFORE BABY            |
|  [Linked view -> Appointments,   |  [Checklist of prep tasks     |
|   next 4 upcoming]               |   for current trimester]      |
+----------------------------------+-------------------------------+
|  BUMP PHOTOS                     |  GEAR STILL NEEDED            |
|  [Linked view -> Milestones,     |  [Linked view -> Gear,        |
|   Gallery with Bump Photo]       |   Status = Need, Priority =   |
|                                  |   Essential, Need By = Before  |
|                                  |   Birth]                      |
+----------------------------------+-------------------------------+
|  SYMPTOM PATTERN                                                  |
|  [Linked view -> Weekly Milestones, showing Symptoms and Energy]  |
+------------------------------------------------------------------+
```

### Dashboard Layout — Baby Mode (after birth)

```
+------------------------------------------------------------------+
|  BABY TRACKER                                 Born: Aug 10, 2026   |
+----------------+--------------+----------------+-----------------+
|  Baby Age      |  Feeds Today |  Sleep Last    |  Next Appt      |
|  6 weeks       |  8 feeds     |  Night: 4.5hr |  Well-visit 8wk |
+----------------+--------------+----------------+-----------------+
|                                                                    |
|  TODAY'S LOG                                                      |
|  [Linked view -> Feeding & Sleep, Date = today]                   |
|  + Quick entry buttons: Feed | Sleep | Diaper                     |
|                                                                    |
+----------------------------------+-------------------------------+
|  RECENT MILESTONES               |  GROWTH CHART                 |
|  [Linked view -> Milestones,     |  [Linked view -> Milestones,  |
|   last 5 achieved]               |   Type = Measurement, last 5] |
|                                  |  Weight: 9.2 lbs (45th %)     |
|                                  |  Length: 21.5 in (60th %)     |
+----------------------------------+-------------------------------+
|  UPCOMING MILESTONES             |  NEXT APPOINTMENT             |
|  [Linked view -> Milestones,     |  [Linked view -> Appointments,|
|   Status = Emerging or Not Yet,  |   next upcoming]              |
|   expected for current age]      |                               |
+----------------------------------+-------------------------------+
|  FEEDING PATTERN (last 7 days)                                    |
|  [Linked view -> Feeding log, feeds only, grouped by day]         |
+------------------------------------------------------------------+
```

---

## PRE-POPULATED MILESTONE CHECKLIST

### Motor Milestones (pre-fill in Growth & Milestones database)

| Milestone | Expected Age | Category |
|---|---|---|
| Lifts head briefly while on tummy | 0-1 month | Gross Motor |
| Follows objects with eyes | 1-2 months | Fine Motor |
| Holds head steady unsupported | 2-4 months | Gross Motor |
| Brings hands together | 3-4 months | Fine Motor |
| Rolls tummy to back | 3-5 months | Gross Motor |
| Reaches for and grasps toys | 4-5 months | Fine Motor |
| Rolls back to tummy | 4-6 months | Gross Motor |
| Sits without support | 5-7 months | Gross Motor |
| Transfers objects between hands | 6-7 months | Fine Motor |
| Crawls | 6-10 months | Gross Motor |
| Pulls to stand | 8-10 months | Gross Motor |
| Pincer grasp (thumb + finger) | 8-10 months | Fine Motor |
| Cruises along furniture | 9-12 months | Gross Motor |
| Stands alone | 10-14 months | Gross Motor |
| First steps | 10-15 months | Gross Motor |

### Language/Social Milestones

| Milestone | Expected Age | Category |
|---|---|---|
| First social smile | 6-8 weeks | Social |
| Coos and gurgles | 2-3 months | Communication |
| Laughs out loud | 3-4 months | Social |
| Responds to own name | 5-7 months | Communication |
| Babbles (ba-ba, da-da) | 6-8 months | Communication |
| Waves bye-bye | 8-10 months | Social |
| Says "mama" or "dada" meaningfully | 10-12 months | Communication |
| Points to desired objects | 10-12 months | Communication |
| Follows simple instructions | 12+ months | Cognitive |

---

## KEY FORMULA REFERENCE

### Trimester Calculation

```
if(
  prop("Week Number") <= 13,
  "First Trimester",
  if(
    prop("Week Number") <= 27,
    "Second Trimester",
    "Third Trimester"
  )
)
```

### Gear Total Cost

```
prop("Price") * prop("Quantity Needed")
```

### Feeding Duration Display (for daily summaries)

Sum Duration (min) for all feeds today. Divide by number of feeds for average session length.

### Sleep Total (manual calculation)

From Sleep entries: sum all Duration (min) entries of Type = Sleep or Nap for the past 24 hours. Divide by 60 for total hours.

---

## QUICK-START GUIDE

### Step 1 — Set Your Due Date and Populate Weeks (15 minutes)

- Open **Weekly Milestones** and create entries for Week 4 through Week 40
- Fill in Date Range for each week based on your due date
- Pre-fill Baby Size, Baby Development, and Your Body from a pregnancy resource (BabyCenter, What to Expect, etc.)
- Mark past weeks as Completed, current week as Current

### Step 2 — Add All Known Appointments (10 minutes)

- Open **Appointments** and add all scheduled prenatal visits
- Standard schedule: monthly until 28 weeks, bi-weekly 28-36, weekly 36-40
- Add known ultrasound dates (typically 8-week dating, 20-week anatomy)
- Add glucose test (24-28 weeks)
- Set Questions to Ask for your next appointment

### Step 3 — Build Your Gear Checklist (15 minutes)

- Open **Baby Gear Checklist**
- Add items by category (start with Essentials only)
- Mark what you already have, what's on your registry, and what to buy
- Set "Need By" timeline for each category
- Don't buy everything at once — many items aren't needed until months after birth

### Step 4 — Start Weekly Journaling (ongoing)

- Each week, open your current Week entry
- Log Symptoms, Energy Level, Mood
- Write a brief Journal Entry
- Take a Bump Photo (you'll cherish these later)
- Mark the previous week as Completed

### Step 5 — After Baby Arrives: Switch to Baby Mode

- Start logging in **Feeding & Sleep Log** from day one (nurses may even start this in hospital)
- Log every feed (time, duration/amount, side) and sleep session
- Don't stress about catching every one — patterns emerge even with imperfect data
- Pre-populate **Growth & Milestones** with the milestone checklist above

### Step 6 — Track Growth (at each pediatrician visit)

- After every well-visit, add a Measurement entry in **Growth & Milestones**
- Record Weight, Length, Head Circumference, and Percentiles
- Note any concerns raised or milestones confirmed

### Step 7 — Celebrate Milestones

- When baby achieves a new milestone, mark it in the database
- Add Date, a Photo/Video, and any Notes about the moment
- Check "Upcoming" view to know what to watch for next

### Pro Tips

- The Feeding & Sleep Log is most valuable in the first 3 months when you're sleep-deprived and can't remember when the last feed was. Keep Notion open on your phone.
- Don't compare milestone timing to other babies. The "Expected Age Range" is wide on purpose — normal development has enormous variation. Only flag "Concern" if your pediatrician does.
- The Gear Checklist should be edited aggressively. After baby arrives, add notes about what you actually used vs. what collected dust. This helps friends and future pregnancies.
- Bump photos shot in the same location/outfit each week create beautiful progression images. Set a weekly reminder.
- Use the "Questions for Next Appt" field throughout the week. You WILL forget what you wanted to ask once you're in the exam room.
- The Feeding & Sleep Log reveals patterns after 2-3 weeks of data. Don't try to analyze it daily — look at weekly trends instead.
- Thank-You tracking in the Gear Checklist prevents the awful realization 3 months later that you never thanked Aunt Linda for the stroller.
- Growth Percentiles are not rankings. 10th percentile is just as healthy as 90th. What matters is consistent growth on YOUR baby's curve, not which curve they're on.
