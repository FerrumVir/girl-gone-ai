# Student Study System — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Courses

**Purpose:** Master record for every course you're taking this term, with grade tracking and GPA calculation built in.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Course Name | Title | Full course title — e.g. "Intro to Psychology" |
| Course Code | Text | Department + number — e.g. "PSY 101" |
| Institution | Select | Your university or college name |
| Term | Select | Fall 2026 / Spring 2027 / Summer 2027 / etc. |
| Credits | Number | Credit hours for this course |
| Professor | Text | Instructor name |
| Professor Email | Email | For quick access |
| Office Hours | Text | Days, times, and location |
| Classroom | Text | Building + room number |
| Schedule | Text | Days/times — e.g. "MWF 10:00-10:50 AM" |
| Syllabus Link | URL | Link to online syllabus or LMS page |
| LMS Link | URL | Canvas, Blackboard, Moodle, etc. |
| Status | Select | Active / Completed / Dropped / Withdrawn |
| Current Grade | Select | A+ / A / A- / B+ / B / B- / C+ / C / C- / D+ / D / D- / F / IP (In Progress) |
| Grade Points | Formula | `if(prop("Current Grade") == "A+", 4.0, if(prop("Current Grade") == "A", 4.0, if(prop("Current Grade") == "A-", 3.7, if(prop("Current Grade") == "B+", 3.3, if(prop("Current Grade") == "B", 3.0, if(prop("Current Grade") == "B-", 2.7, if(prop("Current Grade") == "C+", 2.3, if(prop("Current Grade") == "C", 2.0, if(prop("Current Grade") == "C-", 1.7, if(prop("Current Grade") == "D+", 1.3, if(prop("Current Grade") == "D", 1.0, if(prop("Current Grade") == "D-", 0.7, 0))))))))))))` |
| Quality Points | Formula | `prop("Grade Points") * prop("Credits")` |
| Target Grade | Select | A / A- / B+ / B / B- / C+ / C |
| Grade Notes | Text | What you need on remaining assignments to hit your target |
| Total Study Hours | Rollup | Sum of Duration from linked Study Sessions |
| Assignments Count | Rollup | Count of linked Assignments |
| Completed Assignments | Rollup | Count of linked Assignments where Status = Completed |
| Completion Rate | Formula | `if(prop("Assignments Count") > 0, round((prop("Completed Assignments") / prop("Assignments Count")) * 100), 0)` |
| Notes | Text | Course-level notes, grading policy details, important policies |
| Tags | Multi-select | Core / Elective / Major / Minor / Gen-Ed / Lab / Seminar / Online |
| Linked Assignments | Relation | -> Assignments database |
| Linked Study Sessions | Relation | -> Study Sessions database |
| Linked Resources | Relation | -> Resources database |

**Views:**

- **All Courses** — Table, sorted by Course Code ascending
- **Active Courses** — Filter: Status = Active, sorted by Schedule
- **By Term** — Table, grouped by Term
- **Grade Overview** — Table showing Course Name, Credits, Current Grade, Grade Points, Target Grade — sorted by Current Grade
- **Course Cards** — Gallery view, grouped by Status

---

### 2. Assignments

**Purpose:** Every graded deliverable across all courses — homework, papers, projects, quizzes, exams, presentations, and labs.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Assignment Name | Title | Clear, specific name — e.g. "Chapter 5 Reading Response" |
| Course | Relation | -> Courses database |
| Course Name | Rollup | Course Name from linked Course |
| Course Code | Rollup | Course Code from linked Course |
| Type | Select | Homework / Essay / Research Paper / Lab Report / Problem Set / Quiz / Midterm / Final Exam / Presentation / Group Project / Discussion Post / Reading Response / Other |
| Status | Select | Not Started / In Progress / Completed / Submitted / Graded / Late / Dropped |
| Priority | Select | High / Medium / Low |
| Due Date | Date | Include time if applicable |
| Due Date Display | Formula | `if(empty(prop("Due Date")), "No date", formatDate(prop("Due Date"), "MMM D, YYYY"))` |
| Days Until Due | Formula | `if(empty(prop("Due Date")), 999, dateBetween(prop("Due Date"), now(), "days"))` |
| Urgency | Formula | `if(prop("Status") == "Completed" or prop("Status") == "Submitted" or prop("Status") == "Graded", "Done", if(prop("Days Until Due") < 0, "OVERDUE", if(prop("Days Until Due") <= 1, "DUE TODAY", if(prop("Days Until Due") <= 3, "DUE SOON", if(prop("Days Until Due") <= 7, "This Week", "Upcoming")))))` |
| Weight % | Number | How much this counts toward the course grade (e.g. 15 = 15%) |
| Score | Number | Points or percentage earned |
| Max Score | Number | Maximum possible points |
| Grade % | Formula | `if(and(prop("Score") > 0, prop("Max Score") > 0), round((prop("Score") / prop("Max Score")) * 100), 0)` |
| Letter Grade | Formula | `if(prop("Grade %") >= 93, "A", if(prop("Grade %") >= 90, "A-", if(prop("Grade %") >= 87, "B+", if(prop("Grade %") >= 83, "B", if(prop("Grade %") >= 80, "B-", if(prop("Grade %") >= 77, "C+", if(prop("Grade %") >= 73, "C", if(prop("Grade %") >= 70, "C-", if(prop("Grade %") >= 67, "D+", if(prop("Grade %") >= 63, "D", if(prop("Grade %") >= 60, "D-", if(prop("Grade %") > 0, "F", ""))))))))))))` |
| Group Project | Checkbox | Is this a group assignment? |
| Group Members | Text | Names of group members |
| Instructions | Text | Assignment prompt or link to instructions |
| Submission Link | URL | LMS submission page or upload link |
| Submitted Date | Date | When you actually submitted |
| Feedback | Text | Professor feedback, notes on what to improve |
| Study Sessions | Rollup | Count of linked Study Sessions |
| Hours Spent | Rollup | Sum of Duration from linked Study Sessions |
| Linked Study Sessions | Relation | -> Study Sessions database |

**Views:**

- **All Assignments** — Table, sorted by Due Date ascending
- **Due This Week** — Filter: Days Until Due >= 0 AND Days Until Due <= 7, Status is not Completed/Submitted/Graded
- **Overdue** — Filter: Urgency = "OVERDUE", highlight red
- **By Course** — Table, grouped by Course Name, sorted by Due Date
- **Assignment Board** — Kanban, grouped by Status
- **Upcoming Exams** — Filter: Type = Midterm OR Final Exam, sorted by Due Date
- **Graded** — Filter: Status = Graded, sorted by Grade % descending
- **Calendar** — Calendar view, by Due Date

---

### 3. Study Sessions

**Purpose:** Log every focused study block to track effort, identify patterns, and ensure balanced coverage across courses.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | Brief description — e.g. "PSY 101 — Chapter 5 review" |
| Date | Date | Date of study session |
| Course | Relation | -> Courses database |
| Course Name | Rollup | From Course relation |
| Assignment | Relation | -> Assignments database (optional — link if studying for a specific deliverable) |
| Duration (hours) | Number | Use decimals: 1.5 = 1 hour 30 minutes |
| Start Time | Text | e.g. "2:00 PM" — optional but useful for pattern tracking |
| Location | Select | Library / Dorm / Coffee Shop / Classroom / Home / Study Group / Online |
| Technique | Select | Active Recall / Spaced Repetition / Practice Problems / Reading / Note-Taking / Flashcards / Teaching/Explaining / Past Exams / Group Study / Lecture Review / Writing |
| Focus Level | Select | Deep Focus / Moderate / Distracted / Struggled |
| Productivity Rating | Select | 5 - Excellent / 4 - Good / 3 - Average / 2 - Below Average / 1 - Poor |
| Topics Covered | Text | Specific topics, chapters, or concepts |
| Notes | Text | Key takeaways, things you found confusing, questions to ask |
| Questions for Professor | Text | Capture questions while they're fresh |
| Pomodoros | Number | Number of 25-minute focused blocks completed (optional) |
| Week Number | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Day of Week | Formula | `formatDate(prop("Date"), "dddd")` |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week, sorted by Date descending
- **By Course** — Table, grouped by Course Name, with sum of Duration
- **By Technique** — Table, grouped by Technique
- **By Day of Week** — Table, grouped by Day of Week (reveals your study pattern)
- **By Week** — Table, grouped by Week Number, with sum of Duration
- **Deep Focus Only** — Filter: Focus Level = Deep Focus
- **Study Calendar** — Calendar view, by Date

---

### 4. Resources

**Purpose:** Every learning material you need for every course — textbooks, articles, lecture slides, videos, study guides, and notes — tagged and instantly searchable.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Resource Title | Title | Name of the book, article, video, etc. |
| Course | Relation | -> Courses database |
| Course Name | Rollup | From Course relation |
| Type | Select | Textbook / Article / Lecture Slides / Lecture Recording / YouTube Video / Podcast / Study Guide / Practice Exam / Cheat Sheet / Research Paper / Website / Notes |
| Format | Select | PDF / Link / Physical Book / Video / Audio / Google Doc / Notion Page |
| Link | URL | Direct link to the resource |
| File Location | Text | Where the file lives — Google Drive path, LMS module, etc. |
| Author | Text | Author or creator name |
| Required | Checkbox | Is this a required reading/resource? |
| Status | Select | Not Started / In Progress / Completed / Skimmed / Revisit |
| Priority | Select | Essential / Important / Supplementary / Optional |
| Chapters/Sections | Text | Specific assigned chapters or page ranges |
| Due Date | Date | When this needs to be read/reviewed by |
| Date Added | Date | When you added it to your library |
| Rating | Select | Extremely Useful / Useful / Somewhat Useful / Not Useful |
| Key Takeaways | Text | Summarize the most important points |
| Notes | Text | Your notes, annotations, or page references |
| Tags | Multi-select | Exam Prep / Paper Research / Lecture Supplement / Background Reading / Reference / Quick Review |

**Views:**

- **All Resources** — Table, sorted by Course Name then Resource Title
- **By Course** — Table, grouped by Course Name
- **Required Readings** — Filter: Required = true, sorted by Due Date
- **Unread Required** — Filter: Required = true AND Status = Not Started
- **Exam Prep Materials** — Filter: Tags contains "Exam Prep"
- **By Type** — Table, grouped by Type
- **Resource Cards** — Gallery view, grouped by Course Name

---

## DASHBOARD

> Create this as a Notion page that pulls from all four databases using linked views and summary blocks.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  STUDY COMMAND CENTER             Spring 2027                |
+--------------+--------------+--------------+-----------------+
|  Courses     |  Due This    |  Study Hours |  Semester GPA   |
|     5        |  Week: 7     |  This Week:  |    3.65         |
|              |              |    12.5 hrs  |                 |
+--------------+--------------+--------------+-----------------+
|  DUE THIS WEEK                                               |
|  [Linked view -> Assignments, filter: Due This Week]         |
+-------------------------------------------------------------+
|  OVERDUE / URGENT                                            |
|  [Linked view -> Assignments, filter: Urgency = OVERDUE      |
|   or DUE TODAY, highlight red]                               |
+-------------------------------------------------------------+
|  UPCOMING EXAMS                                              |
|  [Linked view -> Assignments, filter: Type = Midterm or      |
|   Final Exam, sorted by Due Date]                            |
+-------------------------------------------------------------+
|  RECENT STUDY SESSIONS                                       |
|  [Linked view -> Study Sessions, this week, sorted by        |
|   Date descending]                                           |
+------------------------------+------------------------------+
|  STUDY HOURS BY COURSE       |  GRADE OVERVIEW               |
|  [Linked view -> Study       |  [Linked view -> Courses,     |
|   Sessions, grouped by       |   showing Grade, Credits,     |
|   Course, sum Duration]      |   Target Grade, GPA]          |
+------------------------------+------------------------------+
|  UNREAD REQUIRED READINGS                                    |
|  [Linked view -> Resources, filter: Required + Not Started]  |
+-------------------------------------------------------------+
```

### GPA Calculator

**Semester GPA Calculation:**
Create a filtered view of Courses where Term = current term and Status = Active or Completed. The GPA is calculated as:

```
Semester GPA = Sum of Quality Points / Sum of Credits

Where:
- Quality Points = Grade Points x Credits (per course)
- Grade Points = numeric value of letter grade (A = 4.0, B+ = 3.3, etc.)
```

To calculate your semester GPA manually from the dashboard:
1. Open the "Grade Overview" view
2. Sum the Quality Points column
3. Sum the Credits column
4. Divide: Total Quality Points / Total Credits = Semester GPA

**Cumulative GPA:**
Add all completed terms to the same calculation. Filter Courses to Status = Completed across all terms.

### Key Formula Reference

**Urgency Detection (Assignments database):**
```
if(
  or(
    prop("Status") == "Completed",
    prop("Status") == "Submitted",
    prop("Status") == "Graded"
  ),
  "Done",
  if(
    prop("Days Until Due") < 0,
    "OVERDUE",
    if(
      prop("Days Until Due") <= 1,
      "DUE TODAY",
      if(
        prop("Days Until Due") <= 3,
        "DUE SOON",
        if(
          prop("Days Until Due") <= 7,
          "This Week",
          "Upcoming"
        )
      )
    )
  )
)
```

**Grade Percentage (Assignments database):**
```
if(
  and(prop("Score") > 0, prop("Max Score") > 0),
  round((prop("Score") / prop("Max Score")) * 100),
  0
)
```

**Completion Rate (Courses database):**
```
if(
  prop("Assignments Count") > 0,
  round((prop("Completed Assignments") / prop("Assignments Count")) * 100),
  0
)
```

**Weekly Study Hours:**
Create a filtered view of Study Sessions where Date is this week. Sum the Duration column. Compare against your weekly target (recommended: 2-3 hours per credit hour).

---

## EXAM PREP CHECKLIST SYSTEM

For each upcoming exam, create a sub-page inside the Assignment entry with this structure:

### Exam: [Course Code] — [Exam Name]

**Exam Details:**
- Date: [exam date and time]
- Location: [room]
- Format: [multiple choice / short answer / essay / problem sets / mixed]
- Materials allowed: [open book / calculator / note sheet / nothing]
- Covers: [chapters, lecture dates, or topic range]

**Topic Review Checklist:**

| Topic | Covered in Lecture | Notes Reviewed | Practice Done | Confident? |
|---|---|---|---|---|
| [Topic 1] | [ ] | [ ] | [ ] | [ ] |
| [Topic 2] | [ ] | [ ] | [ ] | [ ] |
| [Topic 3] | [ ] | [ ] | [ ] | [ ] |
| [Topic 4] | [ ] | [ ] | [ ] | [ ] |
| [Topic 5] | [ ] | [ ] | [ ] | [ ] |

**Study Plan:**
- [ ] Review all lecture notes for covered material
- [ ] Complete practice problems for each major topic
- [ ] Create flashcards for key terms and definitions
- [ ] Do one full practice exam under timed conditions
- [ ] Review mistakes from practice exam
- [ ] Identify 3 weakest topics and schedule extra study time
- [ ] Prepare allowed materials (note sheet, formula card, etc.)
- [ ] Confirm exam location and time — set an alarm

**Day-Before Checklist:**
- [ ] Light review only — no new material
- [ ] Review note sheet or key formulas
- [ ] Prepare what you need to bring (ID, pencils, calculator, water)
- [ ] Set alarm for exam day
- [ ] Get a full night of sleep

---

## QUICK-START GUIDE

### Step 1 — Enter Your Courses (5 minutes)
- Open the **Courses** database and add every course you're taking this term
- Fill in Course Code, Credits, Professor, and Schedule at minimum
- Set Status to "Active" for current courses
- Set your Target Grade for each course

### Step 2 — Load Your Assignments (10 minutes per course)
- Open each syllabus side by side with the **Assignments** database
- Enter every graded deliverable: homework, papers, projects, quizzes, exams
- Set the Due Date and Type for each one
- Enter the Weight % if your syllabus lists grade weights
- Link each assignment to its Course

### Step 3 — Add Your Key Resources (5 minutes)
- Open the **Resources** database
- Add your textbooks and any must-have resources for each course
- Mark required readings with the Required checkbox
- You can add more resources as the semester progresses — don't try to load everything at once

### Step 4 — Set Up Your Dashboard
- Pin the Dashboard page to your Notion sidebar
- This is your daily launch pad — open it every morning to see what's due

### Step 5 — Start Logging Study Sessions
- After every study block, spend 60 seconds adding an entry to **Study Sessions**
- Link it to the Course and (optionally) the Assignment you worked on
- Select your Technique and Focus Level
- This is how you build your study data over time

### Step 6 — Weekly Review (10 minutes every Sunday)
- Open the Dashboard
- Review upcoming assignments for the next 7 days
- Check your study hours by course — are you balanced?
- Enter any grades you've received
- Check your GPA — are you on track?
- Look at "Unread Required Readings" and plan your reading for the week

### Pro Tips

- Use the **Urgency** formula to sort your daily priorities — work on "DUE TODAY" and "DUE SOON" items first
- After receiving a grade, immediately enter it in the Assignments database — don't let grades pile up
- Set up Notion reminders on assignment Due Dates for a 24-hour advance alert
- Use the "By Day of Week" study session view to find your most productive study days
- For group projects, add all meeting times as study sessions with Location = "Study Group" to track that time
- Export the Calendar view to your phone's calendar app for at-a-glance deadline visibility
- At the end of each term, change course Status to "Completed" and enter your final grades — your cumulative GPA builds automatically over semesters
- If you struggle with a topic, add it to the "Questions for Professor" field in your study session — then actually bring it to office hours
