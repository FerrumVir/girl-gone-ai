# Fitness Coach Business Planner — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked. Review the Quick-Start Guide at the bottom before entering live content.

---

## DATABASES

---

### 1. Client Roster & Programs

**Purpose:** The master record for every client — personal details, fitness history, goals, package status, assigned program, and onboarding stage, all linked to the rest of the planner.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Client Name | Title | First and last name |
| Status | Select | Prospect / Active / On Hold / Inactive / Alumni |
| Onboarding Stage | Select | Inquiry / Intake Form Sent / Intake Form Complete / Goal Session Scheduled / Goal Session Done / Program Assigned / First Session Scheduled / Onboarded |
| Coaching Modality | Select | In-Person / Online / Hybrid |
| Start Date | Date | First paid session or program start date |
| End Date | Date | Package end or churn date (leave blank if ongoing) |
| Primary Goal | Select | Weight Loss / Muscle Gain / Strength / Athletic Performance / Endurance / Rehabilitation / General Health / Body Recomposition |
| Secondary Goal | Multi-select | Flexibility / Stress Reduction / Habit Building / Sport-Specific / Posture / Mobility |
| Experience Level | Select | Beginner / Intermediate / Advanced |
| Training Age (years) | Number | How many years they've trained consistently |
| Health Conditions / Limitations | Text | Injuries, medical conditions, movement restrictions |
| Emergency Contact | Text | Name and phone number |
| Date of Birth | Date | Used for age calculation |
| Age | Formula | `dateBetween(now(), prop("Date of Birth"), "years")` |
| Email | Email | Primary contact email |
| Phone | Phone | Primary contact number |
| Referred By | Text | Referral source or referring client name |
| Current Program | Relation | → Workout Template Library |
| Program Start Date | Date | When the current program assignment began |
| Sessions Package | Relation | → Revenue & Package Tracker (most recent active package) |
| Sessions Remaining | Rollup | From linked Revenue & Package Tracker (sessions remaining field) |
| Next Session | Date | Date of upcoming scheduled session (manual or rollup) |
| Preferred Session Days | Multi-select | Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday |
| Preferred Session Time | Select | Early Morning (5-7am) / Morning (7-9am) / Mid-Morning (9-11am) / Midday (11am-1pm) / Afternoon (1-4pm) / Late Afternoon (4-6pm) / Evening (6-8pm) |
| Session Location | Select | Home Gym / Commercial Gym / Client's Home / Outdoor / Online — Video Call / Facility |
| Gym / Facility Name | Text | Where in-person sessions are held |
| Total Sessions Completed | Rollup | Count of completed sessions from Session Schedule |
| Last Session Date | Rollup | Most recent completed session date from Session Schedule |
| Lifetime Revenue | Rollup | Sum of all payments from Revenue & Package Tracker |
| Notes | Text | Anything relevant that doesn't fit elsewhere |
| Photo / Avatar | Files | Optional client photo for visual roster |
| Intake Form Completed | Checkbox | Has the intake form been received? |
| PAR-Q Completed | Checkbox | Has the physical activity readiness questionnaire been completed? |
| Liability Waiver Signed | Checkbox | Has the waiver been signed? |
| Goals Documented | Checkbox | Have SMART goals been set and recorded? |
| Progress Photos (Baseline) | Checkbox | Has the baseline photo been taken? |

**Views:**

- **Active Clients** — Filter: Status = Active, sorted by Start Date ascending
- **Onboarding Pipeline** — Kanban, grouped by Onboarding Stage, filter: Status = Prospect or Active
- **Client Roster (All)** — Table, sorted by Client Name ascending
- **By Program** — Board, grouped by Current Program
- **Expiring Packages** — Filter: Sessions Remaining <= 3, sorted by Sessions Remaining ascending
- **Inactive Clients** — Filter: Status = Inactive or Alumni
- **Online Clients** — Filter: Coaching Modality = Online or Hybrid
- **New Clients (Last 60 Days)** — Filter: Start Date is within last 60 days

---

### 2. Workout Template Library

**Purpose:** A permanent, reusable library of programs and individual workout sessions. Build it once and assign it to as many clients as needed. Tracks which clients are currently using each program.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Program / Workout Name | Title | Descriptive name (e.g., "12-Week Hypertrophy Block A", "Full Body Beginner 3x/Week") |
| Type | Select | Full Program / Individual Workout / Warm-Up / Conditioning Block / Mobility Routine / Deload Week |
| Goal Alignment | Multi-select | Weight Loss / Muscle Gain / Strength / Athletic Performance / Endurance / Rehabilitation / General Health |
| Experience Level | Select | Beginner / Intermediate / Advanced / All Levels |
| Days Per Week | Number | Training frequency |
| Program Length (weeks) | Number | Total duration for full programs |
| Phase | Select | Foundation / Hypertrophy / Strength / Power / Peaking / Deload / Maintenance |
| Equipment Required | Multi-select | Barbell / Dumbbells / Cables / Machines / Resistance Bands / Pull-Up Bar / Bench / Kettlebells / No Equipment |
| Location | Multi-select | Commercial Gym / Home Gym / Outdoor / Minimal Equipment |
| Workout Structure | Text | Overview of session structure (e.g., "A1/A2 supersets, 3 sets each, followed by B1-B3 circuit") |
| Exercise List | Text | Full exercise prescription: exercise, sets, reps/time, tempo, rest — use structured text format |
| Coaching Notes | Text | Cues, progression notes, common mistakes to watch for |
| Progression Scheme | Text | How to advance (e.g., "Add 2.5kg when client completes all reps at RPE <8 for two consecutive sessions") |
| Deload Protocol | Text | How to deload from this program if needed |
| Created Date | Date | When the program was written |
| Last Updated | Date | Most recent revision date |
| Version | Number | Version number (start at 1.0) |
| Clients Currently Assigned | Rollup | Count of active clients on this program (from Client Roster relation) |
| Tags | Multi-select | Upper Body / Lower Body / Full Body / Push / Pull / Legs / Core / Cardio / Compound / Isolation |
| Status | Select | Active / Draft / Archived / Under Review |
| Source / Inspiration | Text | Where the programming philosophy came from |

**Views:**

- **All Programs** — Table, sorted by Program / Workout Name ascending
- **Active Programs** — Filter: Status = Active, filter: Type = Full Program
- **By Goal** — Board, grouped by Goal Alignment
- **By Experience Level** — Board, grouped by Experience Level
- **Individual Workouts Library** — Filter: Type = Individual Workout
- **Recently Updated** — Sort by Last Updated descending
- **Archived** — Filter: Status = Archived

**Example Exercise List Format:**
```
BLOCK A — COMPOUND MOVEMENTS (35 min)
A1. Barbell Back Squat — 4 x 5 @ 80% 1RM — Tempo 3-1-1 — Rest 3 min
A2. Romanian Deadlift — 4 x 8 @ RPE 7 — Tempo 3-1-1 — Rest 2 min

BLOCK B — ACCESSORY (20 min)
B1. Leg Press — 3 x 12 @ RPE 8 — Rest 90 sec
B2. Walking Lunges — 3 x 10/leg (BW or DBs) — Rest 90 sec
B3. Leg Curl (Machine) — 3 x 15 — Rest 60 sec

FINISHER — CORE (10 min)
C1. Dead Bug — 3 x 8/side — Rest 45 sec
C2. Pallof Press — 3 x 10/side — Rest 45 sec
C3. Plank — 3 x 45 sec — Rest 30 sec
```

---

### 3. Session Schedule

**Purpose:** The operational log of every session — scheduled, completed, and missed. Tracks attendance, session content, client feedback, and credit consumption.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | Auto-format: "[Client Name] — [Date] — [Session #]" |
| Client | Relation | → Client Roster & Programs |
| Client Name | Rollup | From Client (display name) |
| Session Date | Date | Date and time of session |
| Session Number | Number | Sequential session number for this client (manually entered) |
| Duration (min) | Number | Planned or actual session length |
| Session Type | Select | Strength / Conditioning / Mobility / Assessment / Deload / Cardio / Sport-Specific / Online Check-In / Goal Review |
| Location | Select | Home Gym / Commercial Gym / Client's Home / Outdoor / Online — Video Call / Facility |
| Status | Select | Scheduled / Completed / Cancelled — Client / Cancelled — Coach / No-Show / Rescheduled |
| Attended | Checkbox | Flip to true when the session is completed — triggers credit deduction logic |
| Program Used | Relation | → Workout Template Library |
| Workout Block | Text | Which block or day of the program was trained |
| Exercises Logged | Text | Actual exercises performed with sets, reps, and loads used |
| Top Sets / PRs | Text | Any personal records or notable performance milestones |
| Session Notes — Coach | Text | What the coach observed: technique, energy, form breakdown, coaching cues given |
| Session Notes — Client | Text | How the client reported feeling during and after |
| RPE (Session Average) | Number | Average rate of perceived exertion (1-10) for the session |
| Energy Level (Client) | Select | 1 — Exhausted / 2 — Low / 3 — Moderate / 4 — High / 5 — Peak |
| Session Rating (Client) | Number | Client-reported satisfaction 1-5 |
| Next Session Focus | Text | What to prioritize in the following session |
| Package | Relation | → Revenue & Package Tracker |
| Session Counted | Checkbox | Has this session been counted against the client's package? |
| Cancellation Reason | Text | Brief note if cancelled or no-show |
| Late Cancel | Checkbox | Did the client cancel within the late-cancel window? |
| Follow-Up Needed | Checkbox | Flag for any follow-up action (injury referral, program change, check-in) |
| Follow-Up Notes | Text | What follow-up is required |

**Views:**

- **All Sessions** — Table, sorted by Session Date descending
- **This Week** — Filter: Session Date is this week, sorted by Session Date ascending
- **Today** — Filter: Session Date is today, sorted by Session Date ascending
- **Upcoming** — Filter: Status = Scheduled, sorted by Session Date ascending
- **By Client** — Grouped by Client Name
- **Completed** — Filter: Status = Completed, sorted by Session Date descending
- **Cancelled / No-Shows** — Filter: Status = Cancelled — Client or No-Show
- **Needs Follow-Up** — Filter: Follow-Up Needed = true

**Weekly Session Calendar:**
```
Mon   Tue   Wed   Thu   Fri   Sat   Sun
[S1]  [S3]  [S1]  [S3]  [S2]  [S4]  —
[S2]  [S4]  [S2]  [S4]  [S3]  —     —
[S5]  —     [S5]  —     [S6]  —     —
```
*(Use Calendar View in Notion, date field = Session Date)*

---

### 4. Revenue & Package Tracker

**Purpose:** Every package sold, every payment received, and every renewal due. Real-time visibility into active recurring revenue, session credit balances, and monthly income.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Package Name | Title | Descriptive label: "[Client Name] — [Package Type] — [Start Date]" |
| Client | Relation | → Client Roster & Programs |
| Client Name | Rollup | From Client (display name) |
| Package Type | Select | 5-Session Pack / 10-Session Pack / 20-Session Pack / 30-Session Pack / Monthly Membership / 3-Month Program / 6-Month Program / Drop-In / Assessment / Custom |
| Sessions Included | Number | Total sessions purchased in this package |
| Sessions Used | Rollup | Count of Completed sessions linked from Session Schedule |
| Sessions Remaining | Formula | `prop("Sessions Included") - prop("Sessions Used")` |
| Purchase Date | Date | Date package was purchased / payment received |
| Package Start Date | Date | Date client can begin using sessions |
| Package Expiry Date | Date | Date package expires (if applicable) |
| Days Until Expiry | Formula | `dateBetween(prop("Package Expiry Date"), now(), "days")` |
| Expiring Soon | Formula | `if(prop("Days Until Expiry") <= 30 and prop("Days Until Expiry") > 0, true, false)` |
| Package Status | Select | Active / Expired / Completed / Refunded / Paused / Complimentary |
| Price Paid | Number | Total amount paid for this package |
| Price Per Session | Formula | `round(prop("Price Paid") / prop("Sessions Included"), 2)` |
| Payment Method | Select | Cash / Bank Transfer / Stripe / PayPal / Venmo / Square / Invoice |
| Payment Status | Select | Paid in Full / Deposit Paid / Balance Owing / Refunded |
| Invoice Number | Text | Reference number for your records |
| Renewal Reminder Sent | Checkbox | Have you reached out about renewing? |
| Auto-Renew | Checkbox | Is this a recurring membership that auto-renews? |
| Renewal Date | Date | Date to reach out or when auto-renewal triggers |
| Notes | Text | Payment notes, discount applied, special arrangements |

**Views:**

- **All Packages** — Table, sorted by Purchase Date descending
- **Active Packages** — Filter: Package Status = Active, sorted by Package Expiry Date ascending
- **Expiring Soon** — Filter: Expiring Soon = true, sorted by Days Until Expiry ascending
- **Low Credits** — Filter: Sessions Remaining <= 3 AND Package Status = Active
- **By Client** — Grouped by Client Name
- **Monthly Revenue** — Grouped by month of Purchase Date
- **Renewals Due** — Filter: Renewal Date is within next 30 days
- **Completed Packages** — Filter: Package Status = Completed

**Monthly Revenue Summary (example):**
```
April 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
New Package Sales:     $3,200
Active Recurring:      $1,800
Total Revenue:         $5,000
Packages Sold:         8
Avg Package Value:     $625
Sessions Delivered:    62
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 5. Client Progress Dashboard

**Purpose:** Longitudinal tracking of fitness metrics for every client. Benchmarks taken over time create the evidence of progress — essential for client retention, program adjustments, and renewals.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | "[Client Name] — [Metric Type] — [Date]" |
| Client | Relation | → Client Roster & Programs |
| Client Name | Rollup | From Client (display name) |
| Entry Date | Date | Date the measurement or test was performed |
| Entry Type | Select | Body Composition / Strength Benchmark / Cardio Benchmark / Mobility Assessment / Wellness Check-In / Body Measurements |
| Body Weight (kg) | Number | Scale weight on assessment day |
| Body Fat % | Number | Estimated or measured body fat percentage |
| Lean Mass (kg) | Formula | `round(prop("Body Weight (kg)") * (1 - prop("Body Fat %") / 100), 1)` |
| Chest (cm) | Number | Chest circumference |
| Waist (cm) | Number | Waist circumference at navel |
| Hips (cm) | Number | Hip circumference at widest |
| Left Thigh (cm) | Number | Mid-thigh circumference |
| Right Thigh (cm) | Number | Mid-thigh circumference |
| Left Arm (cm) | Number | Mid-bicep circumference |
| Right Arm (cm) | Number | Mid-bicep circumference |
| Squat 1RM (kg) | Number | Tested or estimated 1-rep max |
| Deadlift 1RM (kg) | Number | |
| Bench Press 1RM (kg) | Number | |
| Overhead Press 1RM (kg) | Number | |
| Pull-Up Max Reps | Number | Bodyweight pull-ups to failure |
| Push-Up Max Reps | Number | Bodyweight push-ups to failure |
| Plank Hold (sec) | Number | Time to failure |
| VO2 Max Estimate | Number | From ramp test, step test, or wearable |
| Resting Heart Rate | Number | Beats per minute |
| 1-Mile Run (min) | Number | |
| 1.5-Mile Run (min) | Number | |
| Vertical Jump (cm) | Number | |
| Overhead Squat Score | Select | Pass / Needs Work — Limited ankle dorsiflexion / Needs Work — Hip flexion / Needs Work — Thoracic rotation / Needs Work — Shoulder mobility |
| Sleep (avg hrs/night) | Number | Self-reported, trailing 7 days |
| Stress Level (1-10) | Number | Self-reported |
| Energy Level (1-10) | Number | Self-reported |
| Nutrition Adherence (1-10) | Number | Self-reported weekly compliance |
| Goal Progress Notes | Text | Coach's narrative assessment of progress toward stated goals |
| Photos Taken | Checkbox | Were progress photos taken this check-in? |

**Views:**

- **All Entries** — Table, sorted by Entry Date descending
- **By Client** — Grouped by Client Name, sorted by Entry Date descending
- **Strength Benchmarks** — Filter: Entry Type = Strength Benchmark
- **Body Composition** — Filter: Entry Type = Body Composition
- **Cardio Benchmarks** — Filter: Entry Type = Cardio Benchmark
- **Wellness Check-Ins** — Filter: Entry Type = Wellness Check-In
- **Recent Check-Ins (30 days)** — Filter: Entry Date is within last 30 days

---

## DASHBOARD

### Business Overview Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  FITNESS COACH HQ                                      April 2026   │
├────────────────┬───────────────┬───────────────┬────────────────────┤
│  Active        │  Sessions     │  Monthly      │  Packages          │
│  Clients       │  This Week    │  Revenue      │  Expiring Soon     │
│      24        │      31       │   $5,000      │       4            │
├────────────────┴───────────────┴───────────────┴────────────────────┤
│  TODAY'S SESSIONS                                                    │
│  [Linked view → Session Schedule, filter: Today, sort: time asc]   │
├─────────────────────────────────────────────────────────────────────┤
│  THIS WEEK                                                           │
│  [Linked view → Session Schedule, filter: This Week]               │
├─────────────────────────────────────────────────────────────────────┤
│  ONBOARDING PIPELINE                                                 │
│  [Linked view → Client Roster, Kanban by Onboarding Stage]         │
├─────────────────────────────────────────────────────────────────────┤
│  PACKAGES — LOW CREDITS OR EXPIRING                                  │
│  [Linked view → Revenue Tracker, filter: Sessions Remaining ≤ 3    │
│   or Expiring Soon = true]                                          │
├─────────────────────────────────────────────────────────────────────┤
│  FOLLOW-UPS NEEDED                                                   │
│  [Linked view → Session Schedule, filter: Follow-Up Needed = true] │
├─────────────────────────────────────────────────────────────────────┤
│  RECENT PROGRESS ENTRIES                                             │
│  [Linked view → Client Progress Dashboard, sort: Entry Date desc]  │
└─────────────────────────────────────────────────────────────────────┘
```

### Weekly Coach Snapshot

```
┌─────────────────────────────────────────────────────────────────────┐
│  WEEK OF [Date]                                                     │
├───────────────────┬─────────────────────────────────────────────────┤
│  Sessions Sched.  │  Sessions Comp.  │  No-Shows  │  Cancellations  │
│        32         │        29        │     1      │       2         │
├───────────────────┴──────────────────┴────────────┴─────────────────┤
│  MON  │  TUE  │  WED  │  THU  │  FRI  │  SAT  │  SUN              │
│  [S]  │  [S]  │  [S]  │  [S]  │  [S]  │  [S]  │  —               │
│  [S]  │  [S]  │  [S]  │  [S]  │  [S]  │       │                  │
│  [S]  │       │  [S]  │       │  [S]  │       │                  │
├───────┴───────┴───────┴───────┴───────┴───────┴───────────────────┤
│  RENEWALS TO PITCH THIS WEEK                                        │
│  • Client: Sarah M. — 10-pack expires in 8 days (2 sessions left)  │
│  • Client: James T. — Monthly membership renews Friday             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## KEY FORMULAS

### Client Retention Rate

Measures what percentage of your clients from 3 months ago are still active today. Track monthly.

```
Retention Rate (%) = (Active Clients at End of Period / Active Clients at Start of Period) × 100

Manual calculation using filtered views:

- Active Clients 3 months ago: [filter Start Date <= 3 months ago, Status = Active at that time]
- Currently Active from that cohort: [filter same clients, Status = Active today]
- Formula: (Currently Active / Cohort Size) × 100

Target benchmark: >75% is strong for 1:1 coaching
```

### Revenue Per Client (Monthly)

Measures how much revenue each active client generates on average.

```
Revenue Per Client = Total Monthly Revenue / Number of Active Clients

In Notion:

- Create a "Monthly Revenue" summary view in Revenue Tracker grouped by purchase month
- Divide by active client count from Client Roster

Example: $5,000 revenue / 24 active clients = $208/client/month
```

### Session Utilization Rate

Measures how many of your available coaching hours are being used. Helps identify capacity and pricing decisions.

```
Utilization Rate (%) = (Sessions Completed / Sessions Scheduled) × 100

In Notion:

- Sessions Scheduled: Count of Session Schedule entries with Status = Scheduled + Completed for the period
- Sessions Completed: Count of Session Schedule entries with Status = Completed for the period

Target: >85% utilization = healthy pipeline
Below 70% = marketing or retention issue
```

### Package Expiration Alert Formula (Notion)

Built into the Revenue & Package Tracker as a formula property:

```
Expiring Soon (formula):
if(prop("Days Until Expiry") <= 30 and prop("Days Until Expiry") > 0, true, false)

Use the "Expiring Soon" view to surface all packages requiring proactive renewal outreach.
```

### Sessions Remaining Formula (Notion)

Built into the Revenue & Package Tracker as a formula property:

```
Sessions Remaining:
prop("Sessions Included") - prop("Sessions Used")

Sessions Used is a Rollup from Session Schedule counting entries where:
  Client = this client AND Package = this package AND Status = Completed
```

### Progress Velocity (Strength)

Tracks rate of improvement in key lifts to assess programming effectiveness.

```
Progress Velocity = (Current 1RM - Baseline 1RM) / Weeks Since Baseline

Example: Squat 1RM went from 80kg to 100kg over 12 weeks
Progress Velocity = (100 - 80) / 12 = +1.67 kg/week

Log baseline and current values in Client Progress Dashboard.
Use Goal Progress Notes to record narrative assessment alongside the number.
```

---

## CHECKLISTS

### Client Onboarding Checklist

Use this for every new client from inquiry to first completed session.

```
INQUIRY STAGE

- [ ] Initial consultation call or meeting scheduled
- [ ] Coaching modality, availability, and goals discussed
- [ ] Pricing and packages explained
- [ ] Any obvious contraindications or medical flags noted

ADMIN STAGE

- [ ] Intake form sent and received
- [ ] PAR-Q completed and reviewed
- [ ] Liability waiver signed
- [ ] Package purchased and payment confirmed
- [ ] Client added to Client Roster with Status = Active
- [ ] Package added to Revenue & Package Tracker
- [ ] Package linked to client record

GOAL-SETTING STAGE

- [ ] Goals session scheduled and completed
- [ ] SMART goals documented in client record
- [ ] Baseline assessments scheduled (if applicable)
- [ ] Baseline measurements / strength benchmarks recorded in Progress Dashboard
- [ ] Baseline progress photos taken (if client consents)

PROGRAMMING STAGE

- [ ] Program selected or built from Workout Template Library
- [ ] Program assigned to client in Client Roster
- [ ] First 2-4 weeks of sessions previewed with client
- [ ] Any equipment limitations confirmed

FIRST SESSION

- [ ] Session added to Session Schedule with date, time, and location
- [ ] Client confirmed for attendance
- [ ] Session delivered and logged
- [ ] Session notes completed
- [ ] Onboarding Stage updated to "Onboarded"
```

### Pre-Session Checklist

Run through this before each client session.

```

- [ ] Review last session notes (Session Schedule → previous entry)
- [ ] Check client's energy and wellness notes from last check-in
- [ ] Confirm which workout block is next in their program
- [ ] Prep any equipment or warmup needs specific to today's plan
- [ ] Note any follow-up items from last session to address today
- [ ] Check if package has sessions remaining (Sessions Remaining field)
```

### Monthly Business Review Template

Run this at the end of each month.

```
## [Month Year] — Monthly Business Review

### Revenue
- Total revenue this month: $
- Revenue vs. last month: + / - $
- New packages sold: #
- Renewals closed: #
- Packages expiring next month (pipeline): #

### Client Health
- Active clients at month end: #
- New clients onboarded: #
- Clients churned: #
- Clients on hold: #
- Retention rate: %

### Session Operations
- Sessions scheduled: #
- Sessions completed: #
- No-shows: #
- Cancellations: #
- Utilization rate: %

### Business Actions for Next Month
- [ ] Reach out to renewal prospects:
- [ ] Adjust programming for:
- [ ] Onboard pending clients:
- [ ] Marketing / referral outreach:

### Wins This Month
-

### Challenges / What to Fix
-
```

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Package Types and Select Fields

Before entering clients, customize the select fields to match how you actually run your business:

- Open **Revenue & Package Tracker** and edit the "Package Type" select to reflect your real packages (e.g., "10-Session Pack — $750", "Monthly Membership — $350/mo")
- Open **Client Roster** and edit "Preferred Session Time," "Session Location," and "Primary Goal" to match your client base
- Open **Workout Template Library** and confirm the equipment and location options reflect what you work with

This takes 10-15 minutes and prevents junk data from the start.

### Step 2 — Build Your Core Programs

Before entering clients, add your 3-5 most-used programs to the **Workout Template Library**:

- One full beginner program (if you coach beginners)
- One intermediate strength program
- One hypertrophy program
- Any sport-specific or specialty programs you use repeatedly

Use the Exercise List format provided in the database. Don't worry about building your entire library yet — add programs as you assign them.

### Step 3 — Enter Your Active Clients

For each current client:
1. Create a record in **Client Roster & Programs** — fill in name, status (Active), modality, goal, experience level, contact info
2. Set Onboarding Stage to "Onboarded" for existing clients
3. Assign their current program from the Workout Template Library
4. Check all admin boxes (intake form, PAR-Q, waiver) as applicable

### Step 4 — Log Active Packages

For each active client:
1. Create a record in **Revenue & Package Tracker** — link to their client record, enter package type, sessions included, purchase date, expiry date, price paid
2. Set Package Status = Active
3. Link the package back to the client record in the "Sessions Package" field

After this step, Sessions Remaining will auto-calculate as you log sessions.

### Step 5 — Schedule This Week's Sessions

Open **Session Schedule** and add all upcoming sessions this week:

- One entry per session
- Link each to the correct client
- Set Status = Scheduled
- Set the session date and time using the Session Date property

Use the "This Week" or "Today" view as your daily operating view going forward.

### Step 6 — Log Sessions After They Happen

After each session:
1. Find the session in Session Schedule
2. Fill in Exercises Logged, Top Sets / PRs, Session Notes — Coach
3. Set Status = Completed and check the "Attended" and "Session Counted" boxes
4. Note any Follow-Up Needed items
5. Set "Next Session Focus" for your next visit

Sessions Remaining on the client's package will update automatically via the rollup.

### Step 7 — Track Progress at Check-Ins

Every 4-6 weeks per client (or at your standard check-in cadence):
1. Create a new entry in **Client Progress Dashboard**
2. Record strength benchmarks, body composition measurements, and wellness scores
3. Add Goal Progress Notes with your coaching narrative
4. Review trends against the client's baseline entry

Use this data in renewal conversations — tangible progress is your strongest retention tool.

### Step 8 — Run the Monthly Business Review

On the last day of each month:
1. Open **Revenue & Package Tracker** → Monthly Revenue view to pull income totals
2. Use **Client Roster** active client count and new/churned counts
3. Calculate utilization rate from Session Schedule completed vs. scheduled
4. Fill in the Monthly Business Review template
5. Use the Expiring Soon and Low Credits views to build your renewal outreach list for next month

### Pro Tips

- **Use the Dashboard as your home base.** Pin it in Notion's sidebar. Everything links from there.
- **Log sessions immediately after, not at the end of the day.** Details fade fast. Two minutes right after a session beats 15 minutes reconstructing five sessions at 9pm.
- **Proactive package renewal is the highest-leverage retention move.** Set up a weekly 2-minute review of the "Expiring Soon" view every Monday. Clients who are offered a renewal before they run out of sessions re-sign at much higher rates than clients who run out and have to be chased.
- **The Workout Template Library compounds over time.** Every time you build a new program, add it. After six months, you have a library that covers most new clients without building from scratch.
- **Use "Next Session Focus" religiously.** It takes 30 seconds to write and saves 5 minutes of recall at the start of the next session. Your clients will notice that you always know exactly where they left off.
- **Treat progress entries as a business asset, not just data.** Before any renewal conversation, pull up the client's Progress Dashboard entries and summarize their trajectory. Coaches who show data retain clients at significantly higher rates than those who rely on "you've been doing great."
