# Study Planner Pro — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with formulas, rollups, and automations already configured. Read the Quick-Start Guide at the bottom before entering your courses — it will save you hours of setup.

---

## DATABASES

---

### 1. Courses / Classes

**Purpose:** Master record for every course you are enrolled in this semester. Links to all assignments, study sessions, and exams. Provides the high-level view of your academic workload and progress.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Course Name | Title | Full course name — e.g. "CHEM 201 — Organic Chemistry" |
| Course Code | Text | Short code — e.g. "CHEM201" |
| Professor | Text | Instructor name |
| Professor Email | Email | For quick reference |
| Semester | Select | Fall 2025 / Spring 2026 / Summer 2026 / Fall 2026 / Spring 2027 |
| Day & Time | Text | Meeting schedule — e.g. "MWF 9:00–9:50 AM" |
| Location | Text | Building and room number |
| Credits | Number | Credit hours |
| Grade Weight | Text | Summary of syllabus weighting — e.g. "Exams 40%, HW 30%, Participation 20%, Final 10%" |
| Current Grade | Formula | `if(prop("Total Points Earned") == 0, "N/A", format(round(prop("Total Points Earned") / prop("Total Points Possible") * 100)) + "%")` |
| Total Points Earned | Rollup | Sum of Points Earned from linked Assignments (where Status = Graded) |
| Total Points Possible | Rollup | Sum of Points Possible from linked Assignments (where Status = Graded) |
| Letter Grade | Formula | `if(prop("Current Grade") == "N/A", "—", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.93, "A", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.90, "A-", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.87, "B+", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.83, "B", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.80, "B-", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.77, "C+", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.73, "C", if(prop("Total Points Earned") / prop("Total Points Possible") >= 0.70, "C-", "D/F")))))))))` |
| GPA Points | Formula | Maps Letter Grade to 4.0 scale value |
| Status | Select | Active / Completed / Dropped / Withdrawn |
| Color Tag | Select | Red / Blue / Green / Purple / Orange / Yellow / Pink / Teal (for visual calendar coding) |
| Syllabus | Files & Media | Upload PDF syllabus |
| Office Hours | Text | Days, times, and location |
| TA Name | Text | Teaching assistant name |
| TA Email | Email | TA contact |
| Total Assignments | Rollup | Count of linked Assignments |
| Completed Assignments | Rollup | Count of linked Assignments where Status = Submitted or Graded |
| Completion Rate | Formula | `if(prop("Total Assignments") == 0, "N/A", format(round(prop("Completed Assignments") / prop("Total Assignments") * 100)) + "%")` |
| Total Study Hours | Rollup | Sum of Duration from linked Study Sessions |
| Linked Assignments | Relation | → Assignments database |
| Linked Study Sessions | Relation | → Study Sessions database |
| Linked Exams | Relation | → Exams database |
| Notes | Text | General course notes, tips from past students, resource links |

**Views:**

- **All Courses** — Table, sorted by Course Name ascending
- **This Semester** — Filter: Semester = current semester, grouped by Status
- **By Day** — Table, grouped by Day & Time for weekly schedule overview
- **Grade Overview** — Table showing Course Name, Current Grade, Letter Grade, GPA Points, Credits
- **Active Only** — Filter: Status = Active, sorted by Course Name
- **Course Cards** — Gallery view, card shows Course Code, Professor, Day & Time, Current Grade

---

### 2. Assignments

**Purpose:** Every homework, paper, project, quiz, lab report, and deliverable across all courses. The operational center that ensures nothing is missed and everything is submitted on time.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Assignment Name | Title | Clear name — e.g. "Chapter 5 Problem Set" |
| Course | Relation | → Courses database |
| Course Name | Rollup | Name from linked Course |
| Type | Select | Homework / Essay / Lab Report / Project / Presentation / Quiz / Discussion Post / Reading / Worksheet / Group Project / Extra Credit |
| Status | Select | Not Started / In Progress / Submitted / Graded / Late / Dropped |
| Priority | Select | High / Medium / Low |
| Due Date | Date | Include time if applicable |
| Days Until Due | Formula | `if(empty(prop("Due Date")), "No date", if(dateBetween(prop("Due Date"), now(), "days") < 0, "OVERDUE by " + format(abs(dateBetween(prop("Due Date"), now(), "days"))) + " days", if(dateBetween(prop("Due Date"), now(), "days") == 0, "DUE TODAY", format(dateBetween(prop("Due Date"), now(), "days")) + " days left")))` |
| Urgency Flag | Formula | `if(and(prop("Status") != "Submitted", prop("Status") != "Graded", not(empty(prop("Due Date"))), dateBetween(prop("Due Date"), now(), "days") <= 2), true, false)` |
| Estimated Time (hrs) | Number | How long you think it will take |
| Actual Time (hrs) | Number | How long it actually took (fill in after) |
| Points Possible | Number | Max points for grading |
| Points Earned | Number | Your score (fill in after grading) |
| Percentage | Formula | `if(or(empty(prop("Points Earned")), empty(prop("Points Possible"))), "—", format(round(prop("Points Earned") / prop("Points Possible") * 100)) + "%")` |
| Weight % | Number | What percentage of final grade this is worth |
| Submission Link | URL | Where to submit (Canvas, Blackboard, etc.) |
| Instructions | Text | Assignment instructions or notes |
| Attachments | Files & Media | Upload rubric, reference materials, drafts |
| Completed Date | Date | When you actually submitted |
| Group Members | Text | For group projects — who is in your team |
| Tags | Multi-select | Writing / Math / Research / Lab / Coding / Reading / Creative / Collaborative |
| Linked Study Sessions | Relation | → Study Sessions database |

**Views:**

- **All Assignments** — Table, sorted by Due Date ascending
- **Due This Week** — Filter: Due Date is within 7 days AND Status is Not Started or In Progress, sorted by Due Date ascending
- **Due Today** — Filter: Due Date = today
- **Overdue** — Filter: Due Date < today AND Status is Not Started or In Progress (urgent!)
- **By Course** — Table, grouped by Course Name, sorted by Due Date within groups
- **Kanban Board** — Kanban grouped by Status
- **Priority Board** — Kanban grouped by Priority
- **Graded** — Filter: Status = Graded, sorted by Percentage descending (performance review)
- **Upcoming (Calendar)** — Calendar view by Due Date
- **Not Started** — Filter: Status = Not Started, sorted by Due Date ascending
- **Heavy Weeks** — Calendar view to visualize workload distribution

---

### 3. Study Sessions

**Purpose:** Plan and track focused study time. Every study block is logged with duration, topic, and effectiveness rating so you can optimize how you spend your time and identify which subjects need more attention.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | What you studied — e.g. "Organic Chemistry — Reaction Mechanisms Ch.5" |
| Course | Relation | → Courses database |
| Course Name | Rollup | Name from linked Course |
| Assignment | Relation | → Assignments database (optional — link if studying for a specific deliverable) |
| Date | Date | When the session occurred (include start time) |
| Duration (mins) | Number | Actual time spent studying in minutes |
| Duration (hrs) | Formula | `format(round(prop("Duration (mins)") / 60 * 100) / 100)` |
| Planned Duration (mins) | Number | How long you intended to study |
| Method | Select | Active Recall / Spaced Repetition / Practice Problems / Reading / Note-Taking / Flashcards / Video Lecture / Group Study / Tutoring / Teaching Others / Past Exams |
| Location | Select | Library / Home / Coffee Shop / Campus Study Room / Online / Other |
| Focus Level | Select | Deep Focus / Moderate / Distracted / Very Distracted |
| Effectiveness | Select | Highly Effective / Effective / Neutral / Ineffective / Waste of Time |
| Topics Covered | Text | Specific topics, chapters, or concepts studied |
| Key Takeaways | Text | Main things you learned or realized |
| Struggled With | Text | Concepts that need more review |
| Pomodoros Completed | Number | If using Pomodoro technique (25-min blocks) |
| Break Time (mins) | Number | Total break time taken |
| Distractions | Text | What pulled you off-task (phone, social media, etc.) |
| Energy Level | Select | High / Medium / Low / Exhausted |
| Time of Day | Formula | Extracts morning/afternoon/evening from Date property |
| Week Number | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Streak Day | Number | Consecutive study days (manually updated or use automation) |
| Tags | Multi-select | Exam Prep / Catch-Up / Review / Deep Dive / Quick Review / Group |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week, sorted by Date descending
- **By Course** — Table, grouped by Course Name, showing total Duration per group
- **Study Calendar** — Calendar view by Date
- **Effectiveness Review** — Table, sorted by Effectiveness then Focus Level (identify patterns)
- **By Method** — Table, grouped by Method (find what works best)
- **Daily Log** — Filter: Date = today
- **Low Focus Sessions** — Filter: Focus Level = Distracted or Very Distracted (identify problem patterns)
- **Weekly Hours** — Table grouped by Week Number with Duration sum
- **Time of Day Analysis** — Grouped by Time of Day formula to find optimal study hours

---

### 4. Exams & Tests

**Purpose:** Dedicated tracker for all exams, midterms, finals, and major tests. Includes countdown timers, study progress tracking, and post-exam reflection to continuously improve test performance.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Exam Name | Title | Clear name — e.g. "CHEM201 Midterm 2" |
| Course | Relation | → Courses database |
| Course Name | Rollup | Name from linked Course |
| Exam Type | Select | Quiz / Midterm / Final / Practical / Oral / Take-Home / Standardized |
| Date & Time | Date | Exam date and start time |
| Location | Text | Room/building or "Online" |
| Days Until Exam | Formula | `if(empty(prop("Date & Time")), "No date set", if(dateBetween(prop("Date & Time"), now(), "days") < 0, "COMPLETED", if(dateBetween(prop("Date & Time"), now(), "days") == 0, "TODAY", format(dateBetween(prop("Date & Time"), now(), "days")) + " days")))` |
| Duration (mins) | Number | Length of exam |
| Format | Multi-select | Multiple Choice / Short Answer / Essay / Problem Solving / Lab Practical / Open Book / Open Note / Cumulative |
| Topics Covered | Text | List of chapters, units, or topics on the exam |
| Study Plan Status | Select | Not Started / Planning / In Progress / Final Review / Ready / Completed |
| Study Hours Target | Number | Hours you plan to dedicate to prep |
| Study Hours Logged | Rollup | Sum of Duration from linked Study Sessions tagged with this exam |
| Study Progress % | Formula | `if(prop("Study Hours Target") == 0, "No target set", format(round(prop("Study Hours Logged") / 60 / prop("Study Hours Target") * 100)) + "%")` |
| Weight % | Number | What % of final grade this exam is worth |
| Points Possible | Number | Total possible points |
| Points Earned | Number | Your score (fill in after) |
| Score % | Formula | `if(or(empty(prop("Points Earned")), empty(prop("Points Possible"))), "—", format(round(prop("Points Earned") / prop("Points Possible") * 100)) + "%")` |
| Grade | Text | Letter grade received |
| Materials Allowed | Text | What you can bring — calculator, note sheet, textbook, etc. |
| Professor Review Session | Date | If offered — date/time of review session |
| Study Group Planned | Checkbox | Are you studying with others? |
| Confidence Level | Select | Very Confident / Somewhat Confident / Neutral / Anxious / Unprepared |
| Post-Exam Reflection | Text | What went well, what surprised you, what to do differently |
| Mistakes Made | Text | Specific errors to learn from |
| Would Change | Text | What you would do differently in preparation |
| Linked Study Sessions | Relation | → Study Sessions database |
| Linked Resources | Relation | → Resources database |
| Tags | Multi-select | High Stakes / Cumulative / Group Study / Extra Credit Available |

**Views:**

- **All Exams** — Table, sorted by Date & Time ascending
- **Upcoming** — Filter: Days Until Exam is not "COMPLETED", sorted by Date ascending
- **Countdown Board** — Kanban grouped by Study Plan Status
- **This Month** — Filter: Date is this month
- **By Course** — Table, grouped by Course Name
- **Past Exams** — Filter: Days Until Exam = "COMPLETED", sorted by Score % descending
- **Finals Week** — Filter: Exam Type = Final, sorted by Date ascending
- **Needs Prep** — Filter: Study Plan Status = Not Started or Planning, sorted by Date ascending (urgent!)
- **Performance History** — Table showing all graded exams with Score %, Grade, and Post-Exam Reflection

---

### 5. Resources & Materials

**Purpose:** Central library for all study materials — textbook chapters, lecture slides, YouTube videos, practice exams, flashcard sets, and useful links organized by course and topic.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Resource Name | Title | Descriptive name — e.g. "Khan Academy — Titration Tutorial" |
| Course | Relation | → Courses database |
| Course Name | Rollup | Name from linked Course |
| Type | Select | Textbook Chapter / Lecture Slides / Video / Practice Exam / Flashcards / Article / Website / PDF / Study Guide / Cheat Sheet / Tutor Notes |
| URL | URL | Link to online resource |
| File | Files & Media | Upload PDFs, slides, notes |
| Topic | Text | Specific topic or chapter this covers |
| Usefulness | Select | Essential / Very Useful / Somewhat Useful / Reference Only / Skip |
| Reviewed | Checkbox | Have you gone through this material? |
| Review Date | Date | When you last reviewed it |
| Notes | Text | Key points, page numbers, timestamps for videos |
| Recommended By | Text | Professor, TA, classmate, Reddit, etc. |
| Linked Exams | Relation | → Exams database |
| Tags | Multi-select | Free / Paid / Official / Community / Practice / Theory / Application |

**Views:**

- **All Resources** — Table, sorted by Course Name then Resource Name
- **By Course** — Table, grouped by Course Name
- **Essential** — Filter: Usefulness = Essential
- **Unreviewed** — Filter: Reviewed = false, sorted by Course Name
- **Videos** — Filter: Type = Video
- **Practice Exams** — Filter: Type = Practice Exam
- **By Topic** — Table, sorted by Topic

---

## GPA CALCULATOR

> Create a dedicated section or page that pulls from the Courses database to calculate your cumulative GPA.

### How It Works

The GPA is calculated using the standard formula:

```
GPA = Sum(GPA Points * Credits) / Sum(Credits)
```

Each course's Letter Grade maps to GPA Points:
- A = 4.0, A- = 3.7
- B+ = 3.3, B = 3.0, B- = 2.7
- C+ = 2.3, C = 2.0, C- = 1.7
- D+ = 1.3, D = 1.0, D- = 0.7
- F = 0.0

### GPA Formula (in Courses database)

```
if(prop("Letter Grade") == "A", 4.0,
if(prop("Letter Grade") == "A-", 3.7,
if(prop("Letter Grade") == "B+", 3.3,
if(prop("Letter Grade") == "B", 3.0,
if(prop("Letter Grade") == "B-", 2.7,
if(prop("Letter Grade") == "C+", 2.3,
if(prop("Letter Grade") == "C", 2.0,
if(prop("Letter Grade") == "C-", 1.7,
if(prop("Letter Grade") == "D", 1.0, 0)))))))))
```

### Semester GPA View

Create a table view of Courses filtered by the current semester. Add a summary row showing:
- Total Credits (sum)
- Average GPA Points (weighted by credits — use a formula property: `prop("GPA Points") * prop("Credits")`)

### Cumulative GPA

Filter to Status = Completed or Active (all semesters). The weighted calculation gives your running cumulative GPA across your entire academic career.

---

## WEEKLY SCHEDULE TEMPLATE

> Add this as a toggle block or sub-page for a quick reference of your weekly routine.

```
┌──────────┬───────────────┬───────────────┬───────────────┬───────────────┬───────────────┐
│  Time    │   Monday      │   Tuesday     │  Wednesday    │   Thursday    │    Friday     │
├──────────┼───────────────┼───────────────┼───────────────┼───────────────┼───────────────┤
│  8:00 AM │               │               │               │               │               │
│  9:00 AM │  CHEM 201     │  MATH 301     │  CHEM 201     │  MATH 301     │  CHEM 201     │
│ 10:00 AM │  Study Block  │  ENG 102      │  Study Block  │  ENG 102      │  Study Block  │
│ 11:00 AM │  MATH 301     │  Study Block  │  MATH 301     │  Study Block  │  MATH 301     │
│ 12:00 PM │  Lunch        │  Lunch        │  Lunch        │  Lunch        │  Lunch        │
│  1:00 PM │  ENG 102      │  Lab          │  ENG 102      │  Lab          │  Office Hrs   │
│  2:00 PM │  Study Block  │  Lab          │  Study Block  │  Lab          │  Free         │
│  3:00 PM │  Study Block  │  Study Block  │  Study Block  │  Study Block  │  Free         │
│  4:00 PM │  Free         │  Free         │  Free         │  Free         │  Free         │
└──────────┴───────────────┴───────────────┴───────────────┴───────────────┴───────────────┘
```

---

## AUTOMATIONS / FORMULAS

### Assignment Urgency Detection

Flags assignments due within 48 hours that haven't been submitted. Drives the "Urgent" indicator in the Kanban view.

```
if(
  and(
    prop("Status") != "Submitted",
    prop("Status") != "Graded",
    not(empty(prop("Due Date"))),
    dateBetween(prop("Due Date"), now(), "days") <= 2
  ),
  true,
  false
)
```

### Exam Countdown

Shows a human-readable countdown to each exam, changing to "COMPLETED" after the exam date passes.

```
if(
  empty(prop("Date & Time")),
  "No date set",
  if(
    dateBetween(prop("Date & Time"), now(), "days") < 0,
    "COMPLETED",
    if(
      dateBetween(prop("Date & Time"), now(), "days") == 0,
      "TODAY",
      format(dateBetween(prop("Date & Time"), now(), "days")) + " days"
    )
  )
)
```

### Study Session Duration Conversion

Converts minutes to decimal hours for easier weekly/monthly totals.

```
format(round(prop("Duration (mins)") / 60 * 100) / 100)
```

### Current Grade Calculator

Computes running grade percentage based on all graded assignments in a course.

```
if(
  prop("Total Points Earned") == 0,
  "N/A",
  format(round(prop("Total Points Earned") / prop("Total Points Possible") * 100)) + "%"
)
```

### Study Progress for Exams

Shows what percentage of your target study hours you've completed for each exam.

```
if(
  prop("Study Hours Target") == 0,
  "No target set",
  format(round(prop("Study Hours Logged") / 60 / prop("Study Hours Target") * 100)) + "%"
)
```

### Overdue Assignment Detection

Flags any assignment past its due date that hasn't been turned in.

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Submitted",
    prop("Status") != "Graded",
    prop("Status") != "Dropped"
  ),
  true,
  false
)
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Courses

- Open the **Courses** database and add every class you are taking this semester
- Fill in Course Name, Course Code, Professor, Day & Time, and Credits
- Upload your syllabus to each course record for quick reference
- Set all courses to Status = Active

### Step 2 — Enter All Assignments from Your Syllabi

- Go through each syllabus and add every known assignment to the **Assignments** database
- Link each assignment to its Course using the relation property
- Set the Due Date, Type, and Points Possible for each
- This is the most time-consuming step but you only do it once — after this, your semester is mapped out

### Step 3 — Add Your Exams

- Open the **Exams** database and add every quiz, midterm, and final
- Link each exam to its Course
- Set the Date & Time, Weight %, Topics Covered, and Format
- Set a Study Hours Target for each major exam (a good rule: 2 hours of study per 1% of grade weight)

### Step 4 — Start Logging Study Sessions

- Every time you sit down to study, create a new entry in **Study Sessions**
- Link it to the Course (and optionally the Assignment or Exam you are preparing for)
- After finishing, fill in Duration, Focus Level, Effectiveness, and Key Takeaways
- Be honest about Focus Level and Distractions — this data helps you optimize

### Step 5 — Build Your Dashboard

- Create a new page called "Study Command Center"
- Add linked database views:
  - Assignments Due This Week (sorted by Due Date)
  - Exam Countdown (upcoming exams with days remaining)
  - Today's Study Sessions
  - Grade Overview (all courses with current grade)
  - Weekly Study Hours (study sessions grouped by week)
- Pin this page to your sidebar

### Step 6 — Establish Your Rhythms

**Every morning (2 minutes):**
- Check "Due This Week" — what needs attention today?
- Check the Exam Countdown — anything within 7 days triggers study mode

**Every evening (3 minutes):**
- Log your study sessions from the day
- Update assignment statuses (mark anything submitted)
- Plan tomorrow's study blocks

**Every Sunday (15 minutes):**
- Review the upcoming week's assignments and exams
- Plan study sessions for the week ahead
- Check your current grades across all courses
- Identify any weak areas that need extra study time

**After each exam:**
- Fill in Points Earned and Score %
- Write your Post-Exam Reflection while it's fresh
- Note Mistakes Made and Would Change for next time

### Pro Tips

- Use the Calendar view of Assignments to visualize heavy weeks and plan ahead
- Track your Focus Level and Time of Day in Study Sessions — after 2 weeks you'll know exactly when you study best
- Set Estimated Time on assignments before starting, then log Actual Time after — you'll learn to plan more accurately
- For group projects, add all group members in the Group Members field and use the Notes section to track who is doing what
- Color-code your courses and use those colors in your physical planner too for visual consistency
- Review your "Low Focus Sessions" view weekly — if a pattern emerges (always distracted at home, always focused in the library), restructure your schedule accordingly
- Use the Resources database to build a library of helpful materials — when finals approach, you'll have everything organized by course and topic
- Aim for a study streak — even 20 minutes counts as a session. Consistency beats intensity for retention
