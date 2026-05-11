# Homeschool Curriculum Planner — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with progress tracking formulas, attendance calculations, and grade rollups built in. Supports 1-4 students across multiple grade levels. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Students

**Purpose:** Profile for each student in your homeschool. Stores grade level, learning style, accommodations, and links to all their subjects, lessons, and progress records. The hub that connects everything else.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Student Name | Title | First name (or nickname used at home) |
| Grade Level | Select | Pre-K / K / 1st / 2nd / 3rd / 4th / 5th / 6th / 7th / 8th / 9th / 10th / 11th / 12th |
| Age | Number | Current age |
| Birth Date | Date | For records |
| Learning Style | Multi-select | Visual / Auditory / Kinesthetic / Reading/Writing / Social / Solitary |
| Strengths | Text | What they excel at — both academic and personal |
| Challenges | Text | Areas needing extra support or accommodation |
| Accommodations | Text | IEP/504 notes, sensory needs, attention supports |
| Curriculum Approach | Multi-select | Charlotte Mason / Classical / Montessori / Unschooling / Textbook / Eclectic / Unit Study / Waldorf |
| School Year | Select | 2025-2026 / 2026-2027 / 2027-2028 |
| Start Date | Date | When the school year began |
| Target End Date | Date | Planned last day |
| Total School Days Required | Number | Your state's minimum (typically 172-180) |
| Days Completed | Number | Running count of school days logged |
| Attendance Rate | Formula | `if(prop("Total School Days Required") == 0, 0, round(prop("Days Completed") / prop("Total School Days Required") * 100))` |
| Attendance Display | Formula | `format(prop("Days Completed")) + "/" + format(prop("Total School Days Required")) + " days (" + format(prop("Attendance Rate")) + "%)"` |
| Days Remaining | Formula | `prop("Total School Days Required") - prop("Days Completed")` |
| On Track | Formula | `if(prop("Days Remaining") <= 0, "Complete!", if(dateBetween(prop("Target End Date"), now(), "days") >= prop("Days Remaining"), "On Track", "Behind — add days"))` |
| Linked Subjects | Relation | -> Subjects database |
| Linked Lessons | Relation | -> Lessons/Units database |
| Subject Count | Rollup | Count of Linked Subjects |
| Overall GPA | Text | Calculated manually from subject grades (or use weighted formula) |
| Notes | Text | General observations, goals for the year |
| Photo | Files & media | Student photo for dashboard |
| Tags | Multi-select | Gifted / 2E / Special Needs / Early Reader / Reluctant Learner / Self-Directed |

**Views:**

- **All Students** — Gallery with Photo, Name, Grade Level, Attendance Display
- **Progress Dashboard** — Table showing Attendance Rate, Days Remaining, On Track
- **By Grade** — Table, grouped by Grade Level

---

### 2. Subjects

**Purpose:** Each subject a student is studying this year. Defines the curriculum used, schedule, credits, and overall grade. Links to all lessons/units within that subject.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Subject Name | Title | (e.g., "Math — 5th Grade" or "US History") |
| Student | Relation | -> Students database |
| Student Name | Rollup | From Student relation |
| Category | Select | Math / Language Arts / Science / History / Social Studies / Foreign Language / Art / Music / PE / Health / Computer Science / Life Skills / Religion / Elective |
| Curriculum/Program | Text | Name of textbook, program, or resource used |
| Publisher | Text | Publisher or creator |
| Status | Select | Not Started / In Progress / Completed / Paused / Dropped |
| Schedule | Multi-select | Monday / Tuesday / Wednesday / Thursday / Friday |
| Days Per Week | Number | How many days this subject is taught |
| Duration Per Session | Select | 15 min / 20 min / 30 min / 45 min / 60 min / 90 min / Variable |
| Credit Hours | Number | For high school transcripts (typically 0.5 or 1.0) |
| Grade Weight | Select | Standard / Honors / AP (for weighted GPA) |
| Total Units/Lessons | Number | How many lessons/chapters in the full curriculum |
| Completed Units | Number | How many finished so far |
| Progress % | Formula | `if(prop("Total Units/Lessons") == 0, 0, round(prop("Completed Units") / prop("Total Units/Lessons") * 100))` |
| Progress Display | Formula | `format(prop("Completed Units")) + "/" + format(prop("Total Units/Lessons")) + " (" + format(prop("Progress %")) + "%)"` |
| Pace Status | Formula | `if(prop("Total Units/Lessons") == 0, "No units set", if(prop("Progress %") >= 90, "Nearly done!", if(prop("Progress %") >= 66, "On pace", if(prop("Progress %") >= 33, "Check pace", "Behind"))))` |
| Current Grade | Select | A+ / A / A- / B+ / B / B- / C+ / C / C- / D / F / Pass / Incomplete |
| Grade % | Number | Numeric grade (0-100) |
| Assessment Method | Select | Tests / Portfolio / Mastery / Standards-Based / Narrative / Mixed |
| Linked Lessons | Relation | -> Lessons/Units database |
| Linked Resources | Relation | -> Resources database |
| Lesson Count | Rollup | Count of Linked Lessons |
| Start Date | Date | When subject instruction began |
| Target End Date | Date | Planned completion |
| Notes | Text | Curriculum notes, modifications, pacing adjustments |
| Tags | Multi-select | Core / Elective / Co-op / Online / Self-Paced / Parent-Led / Outsourced |

**Views:**

- **All Subjects** — Table, sorted by Student then Category
- **By Student** — Table, grouped by Student Name
- **By Category** — Table, grouped by Category
- **Progress Board** — Board, grouped by Pace Status
- **In Progress** — Filter: Status = In Progress
- **Schedule** — Table showing Subject Name, Schedule (days), Duration
- **High School Credits** — Filter: Credit Hours > 0 (transcript view)
- **Behind Pace** — Filter: Pace Status = "Behind" or "Check pace"

---

### 3. Lessons / Units

**Purpose:** Individual lessons, chapters, or units within each subject. Tracks completion, dates, grades on assignments/tests, and time spent. This is where daily teaching gets logged.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Lesson Title | Title | Chapter/lesson name or topic |
| Subject | Relation | -> Subjects database |
| Subject Name | Rollup | From Subject relation |
| Student | Relation | -> Students database |
| Student Name | Rollup | From Student relation |
| Unit Number | Number | Sequential order (1, 2, 3...) |
| Status | Select | Not Started / In Progress / Completed / Skipped / Review Needed |
| Date Assigned | Date | When lesson was introduced |
| Date Completed | Date | When student finished |
| Days to Complete | Formula | `if(and(not(empty(prop("Date Assigned"))), not(empty(prop("Date Completed")))), dateBetween(prop("Date Completed"), prop("Date Assigned"), "days"), 0)` |
| Time Spent (min) | Number | Minutes spent on this lesson |
| Grade/Score | Number | Score if assessed (0-100) |
| Assessment Type | Select | Test / Quiz / Essay / Project / Presentation / Worksheet / Oral / Observation / N/A |
| Mastery Level | Select | Exceeds / Meets / Approaching / Below / Not Assessed |
| Difficulty for Student | Select | Too Easy / Just Right / Challenging / Too Hard |
| Engagement | Select | Highly Engaged / Engaged / Neutral / Resistant / Refused |
| Teaching Method | Select | Lecture / Hands-on / Video / Reading / Discussion / Game / Field Trip / Lab / Workbook |
| Materials Used | Text | Specific pages, videos, manipulatives, or resources |
| Homework Assigned | Text | If applicable |
| Homework Completed | Checkbox | Done? |
| Parent Notes | Text | How the lesson went, what to revisit, observations |
| Student Work | Files & media | Photos of work, uploaded assignments |
| Tags | Multi-select | Review Later / Portfolio Piece / Struggled / Mastered / Fun / Field Trip |

**Views:**

- **All Lessons** — Table, sorted by Subject then Unit Number
- **By Subject** — Table, grouped by Subject Name
- **By Student** — Table, grouped by Student Name
- **This Week** — Filter: Date Assigned or Date Completed is this week
- **Needs Completion** — Filter: Status = In Progress or Not Started, sorted by Date Assigned
- **Completed** — Filter: Status = Completed, sorted by Date Completed descending
- **Review Needed** — Filter: Status = Review Needed
- **Grades** — Table showing Lesson Title, Grade/Score, Mastery Level, grouped by Subject
- **Calendar** — Calendar view by Date Assigned
- **By Engagement** — Table, grouped by Engagement (spot patterns)
- **Portfolio Pieces** — Filter: Tags contains Portfolio Piece

---

### 4. Resources

**Purpose:** Books, websites, videos, apps, and materials used across your curriculum. Organized by subject and type so you can quickly find and reuse resources, track what's checked out from the library, and plan purchases.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Resource Name | Title | Book title, website name, app name, etc. |
| Type | Select | Textbook / Workbook / Book (reading) / Video / Website / App / Game / Manipulative / Printable / Subscription / Kit |
| Subject | Relation | -> Subjects database |
| Student | Relation | -> Students database |
| Category | Select | Math / Language Arts / Science / History / Art / Music / PE / Foreign Language / Life Skills / Multi-subject |
| Status | Select | In Use / On Shelf / Library (checked out) / Wishlist / Returned / Digital |
| Library Due Date | Date | If checked out from library |
| Library Overdue | Formula | `if(and(prop("Status") == "Library (checked out)", not(empty(prop("Library Due Date"))), prop("Library Due Date") < now()), true, false)` |
| Cost | Number (USD) | What you paid (or will pay) |
| Source | Select | Owned / Library / Borrowed / Subscription / Free Online / Purchased |
| URL | URL | Link to resource (for digital) |
| ISBN | Text | For books |
| Grade Level | Text | Appropriate grade range |
| Quality Rating | Select | Excellent / Good / OK / Poor / Haven't Used Yet |
| Reusable | Checkbox | Can be used for younger siblings later? |
| Notes | Text | How you're using it, what works, modifications |
| Tags | Multi-select | Favorite / Secular / Faith-Based / Hands-On / Screen-Free / Self-Paced / Parent-Intensive |

**Views:**

- **All Resources** — Table, sorted by Subject then Type
- **By Subject** — Table, grouped by Subject
- **Library Items** — Filter: Status = Library (checked out), showing Library Due Date
- **Library Overdue** — Filter: Library Overdue = true
- **Wishlist** — Filter: Status = Wishlist (for purchasing decisions)
- **By Type** — Table, grouped by Type
- **Favorites** — Filter: Quality Rating = Excellent
- **In Use** — Filter: Status = In Use

---

### 5. State Requirements / Compliance

**Purpose:** Tracks your state's homeschool requirements — attendance minimums, required subjects, testing schedules, portfolio deadlines, and notification due dates. Prevents compliance surprises.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Requirement | Title | What's required |
| Category | Select | Attendance / Subjects / Testing / Notification / Portfolio / Evaluation / Immunization / Other |
| State | Text | Your state |
| Due Date | Date | When this is due |
| Frequency | Select | Annual / Semi-Annual / Quarterly / One-Time / Ongoing |
| Status | Select | Not Started / In Progress / Completed / Submitted / Overdue |
| Completed Date | Date | When you finished this requirement |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Completed", prop("Status") != "Submitted"), true, false)` |
| Description | Text | Full details of what's required |
| How to Submit | Text | Where/how to file (address, website, process) |
| Evidence Needed | Text | What documentation to include |
| Documents | Files & media | Uploaded completed forms, evaluations |
| Reference Link | URL | Link to state law or school district page |
| Notes | Text | Tips, experiences from past years |
| Linked Students | Relation | -> Students database |
| School Year | Select | 2025-2026 / 2026-2027 |
| Reminder Date | Date | When to start working on this |

**Views:**

- **All Requirements** — Table, sorted by Due Date ascending
- **Upcoming** — Filter: Status != Completed, sorted by Due Date ascending
- **Overdue** — Filter: Overdue = true
- **By Category** — Table, grouped by Category
- **This School Year** — Filter: School Year = current year
- **Completed** — Filter: Status = Completed or Submitted
- **Calendar** — Calendar view by Due Date

---

## DASHBOARD

> Create this as the top-level page. It's your homeschool command center — shows attendance progress, this week's lessons, and any compliance deadlines at a glance.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  HOMESCHOOL HQ                                   2025-2026        |
+------------------------------------------------------------------+
|  STUDENT PROGRESS                                                 |
|  [Linked view -> Students, Gallery with Photo]                    |
|                                                                    |
|  Emma (5th)              Jack (3rd)             Lily (K)          |
|  142/175 days (81%)      142/175 days (81%)     130/160 days (81%)|
|  On Track                On Track               On Track          |
|  Subjects: 8/8 active    Subjects: 7/7 active   Subjects: 5/5    |
|                                                                    |
+----------------------------------+-------------------------------+
|  THIS WEEK'S LESSONS             |  COMPLIANCE DEADLINES         |
|  [Linked view -> Lessons,        |  [Linked view -> State Reqs,  |
|   Date Assigned this week,       |   upcoming, sorted by         |
|   grouped by Student]            |   Due Date]                   |
+----------------------------------+-------------------------------+
|  SUBJECT PROGRESS                                                 |
|  [Linked view -> Subjects, showing Progress Display and           |
|   Pace Status for all students]                                   |
|                                                                    |
|  Emma - Math: 67/96 (70%) On pace                                |
|  Emma - LA: 45/72 (63%) On pace                                  |
|  Emma - Science: 18/36 (50%) Check pace                          |
|  Jack - Math: 52/85 (61%) On pace                                |
+----------------------------------+-------------------------------+
|  NEEDS ATTENTION                 |  LIBRARY DUE DATES            |
|  [Linked view -> Subjects,       |  [Linked view -> Resources,   |
|   Pace Status = Behind]          |   Library items, sorted by    |
|  [Linked view -> Lessons,        |   Due Date]                   |
|   Status = Review Needed]        |                               |
+----------------------------------+-------------------------------+
|  RECENTLY COMPLETED                                               |
|  [Linked view -> Lessons, Status = Completed, last 7 days]       |
+------------------------------------------------------------------+
```

---

## KEY FORMULA REFERENCE

### Attendance Rate (Students)

```
if(
  prop("Total School Days Required") == 0,
  0,
  round(prop("Days Completed") / prop("Total School Days Required") * 100)
)
```

### Attendance On-Track Check

```
if(
  prop("Days Remaining") <= 0,
  "Complete!",
  if(
    dateBetween(prop("Target End Date"), now(), "days") >= prop("Days Remaining"),
    "On Track",
    "Behind — add days"
  )
)
```

Compares remaining calendar days to remaining required school days. If you have fewer calendar days left than school days needed, you're behind.

### Subject Progress

```
if(
  prop("Total Units/Lessons") == 0,
  0,
  round(prop("Completed Units") / prop("Total Units/Lessons") * 100)
)
```

### Subject Pace Status

```
if(
  prop("Total Units/Lessons") == 0,
  "No units set",
  if(
    prop("Progress %") >= 90,
    "Nearly done!",
    if(
      prop("Progress %") >= 66,
      "On pace",
      if(
        prop("Progress %") >= 33,
        "Check pace",
        "Behind"
      )
    )
  )
)
```

Note: These thresholds assume linear pacing through the year. Adjust if your school year is front-loaded or back-loaded.

### Library Overdue

```
if(
  and(
    prop("Status") == "Library (checked out)",
    not(empty(prop("Library Due Date"))),
    prop("Library Due Date") < now()
  ),
  true,
  false
)
```

### Compliance Overdue

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Completed",
    prop("Status") != "Submitted"
  ),
  true,
  false
)
```

### Days to Complete a Lesson

```
if(
  and(not(empty(prop("Date Assigned"))), not(empty(prop("Date Completed")))),
  dateBetween(prop("Date Completed"), prop("Date Assigned"), "days"),
  0
)
```

---

## WEEKLY PLANNING WORKFLOW

Every Sunday (20-30 minutes):

### 1. Review Last Week (5 minutes)
- Open **Lessons > This Week** view
- Mark completed lessons as Completed
- Note any that need review (change Status to "Review Needed")
- Update "Completed Units" count on relevant Subjects

### 2. Plan Next Week (15 minutes)
- For each student, for each subject:
  - Create lesson entries for the upcoming week
  - Set Date Assigned for each day's work
  - Note Materials Used (check library due dates)
  - If a subject is "Behind" pace, add extra sessions this week

### 3. Check Compliance (2 minutes)
- Open **State Requirements > Upcoming** view
- Anything due in the next 30 days? Start preparing.
- Update attendance count (add last week's school days to "Days Completed")

### 4. Resource Check (3 minutes)
- **Library Overdue** view — renew or return anything due
- **Wishlist** — any resources needed for next week's lessons?

---

## GRADING GUIDE

### For Elementary (K-5):
Use **Mastery Level** instead of letter grades:

- Exceeds: Working above grade level
- Meets: Demonstrates understanding at grade level
- Approaching: Making progress, not yet consistent
- Below: Needs significant support

### For Middle/High School (6-12):
Use **Grade %** and **Letter Grade**:

- A: 90-100% (Excellent mastery)
- B: 80-89% (Good understanding)
- C: 70-79% (Adequate)
- D: 60-69% (Below standard)
- F: Below 60% (Not passing)

### GPA Calculation (High School):
- A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0.0
- Honors: add 0.5, AP: add 1.0
- GPA = Sum of (Grade Points x Credit Hours) / Total Credit Hours
- Record in Student's "Overall GPA" field each semester

---

## QUICK-START GUIDE

### Step 1 — Add Your Students (5 minutes)

- Open the **Students** database
- Add each student with Grade Level, Learning Style, and School Year
- Set Total School Days Required (check your state's minimum)
- Set Start Date and Target End Date for the year
- Note any Accommodations or special needs

### Step 2 — Add Subjects (10 minutes per student)

- Open the **Subjects** database
- Add every subject each student will study this year
- Link each to the correct Student
- Set the Curriculum/Program, Schedule (which days), and Duration
- Enter Total Units/Lessons from the curriculum's scope and sequence
- For high schoolers: set Credit Hours

### Step 3 — Set Up State Requirements (10 minutes)

- Open **State Requirements** database
- Research your state's homeschool laws (HSLDA website is a good reference)
- Add each requirement with Category, Due Date, and Description
- Set Reminder Dates 30 days before each due date
- Link to relevant students

### Step 4 — Add Resources (15 minutes)

- Open **Resources** and add your curriculum materials
- Mark Status (In Use, On Shelf, Library)
- Set Library Due Dates for anything checked out
- Add links for digital resources

### Step 5 — Start Logging Lessons (daily, 5 minutes)

- Each school day, create lesson entries for what was taught
- Required: Lesson Title, Subject, Student, Status, Date Assigned
- Helpful: Teaching Method, Engagement, Time Spent
- Mark as Completed when finished
- This takes 5 minutes at the end of each school day

### Step 6 — Build Your Dashboard

- Create the top-level page following the Dashboard Layout
- Pin to sidebar for daily reference

### Step 7 — Establish Rhythms

**Daily (5 minutes, end of school day):**

- Log today's lessons (mark completed)
- Note engagement and difficulty observations

**Weekly (20 minutes, Sunday):**

- Follow the Weekly Planning Workflow above

**Monthly (15 minutes, first of month):**

- Update Subject progress (Completed Units)
- Review "Behind Pace" subjects and adjust plans
- Check 30-day compliance deadlines
- Update "Days Completed" on Student records

**Semester (30 minutes):**

- Calculate grades for each subject
- Generate progress reports (use Subject data + Lesson grades)
- Update GPA for high school students
- Archive completed lessons and resources no longer in use

### Pro Tips

- Don't log every single thing as a "lesson." Short activities, read-alouds, and informal learning can be grouped: "Science — Week 12 Observations" is fine as a single entry covering multiple days of nature study.
- Use the Engagement field honestly. Patterns of resistance in a subject tell you the curriculum isn't working — not that the child is failing. Switch approaches before frustration builds.
- The Pace Status formula assumes linear progress (33% by 1/3 of the year, 66% by 2/3). If you intentionally front-load or back-load certain subjects, ignore the "Behind" flag for those.
- Keep a "Review Needed" running list. Children forget material over breaks. Use these flags to spiral back to concepts before testing or portfolio reviews.
- For multi-student households: batch similar subjects. If all kids are doing science on Tuesday, one entry per student with shared Materials Used saves planning time.
- State Requirements is your legal protection. Overcomplicate your daily logging? Maybe. But never underestimate compliance documentation. Keep it current.
- Library Due Dates alone will save you $20+/year in late fees. Worth the 30 seconds per book to enter.
