# Teacher Lesson Planner & Classroom Manager — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Lessons

**Purpose:** Plan and track individual daily lessons with standards alignment, materials, and post-lesson reflections.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Lesson Title | Title | Clear, descriptive name (e.g., "Intro to Fractions — Visual Models") |
| Date | Date | Scheduled teaching date |
| Unit | Relation | → Units database |
| Unit Name | Rollup | Unit Name from Unit relation |
| Subject | Select | Math / ELA / Science / Social Studies / Art / Music / PE / World Language / Other |
| Grade Level | Select | K / 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 |
| Period / Block | Select | 1st / 2nd / 3rd / 4th / 5th / 6th / 7th / 8th / Homeroom |
| Duration | Select | 30 min / 45 min / 50 min / 60 min / 90 min / Block |
| Standards | Multi-select | Tag with applicable standards codes (e.g., CCSS.MATH.3.NF.1) |
| Learning Objective | Text | "Students will be able to..." — measurable, observable |
| Essential Question | Text | The driving question for student inquiry |
| Status | Select | Draft / Planned / Taught / Skipped / Rescheduled |
| Warm-Up / Do Now | Text | 5-minute opening activity or bell ringer |
| Direct Instruction | Text | I Do — teacher modeling and explanation |
| Guided Practice | Text | We Do — collaborative practice with scaffolding |
| Independent Practice | Text | You Do — student application and practice |
| Closure | Text | Exit ticket, summary, or reflection activity |
| Differentiation — Below | Text | Modifications for struggling learners |
| Differentiation — Above | Text | Extensions for advanced learners |
| Accommodations | Text | IEP/504 accommodations to implement |
| Materials Needed | Text | List of physical and digital materials |
| Technology | Multi-select | Chromebook / Projector / Calculator / App / None |
| Assessment Type | Select | Formative / Summative / Observation / Exit Ticket / Quiz / None |
| Assessment Notes | Text | What you're assessing and how |
| Homework | Text | Assignment given, if any |
| Reflection | Text | Post-lesson: What worked? What to adjust? |
| Reflection Rating | Select | Great / Good / Needs Work / Reteach |
| Linked Resources | Relation | → Resources database |
| Tags | Multi-select | Hands-On / Group Work / Independent / Technology / Lab / Discussion / Project |

**Views:**
- **This Week** — Table, filter: Date is this week, sorted by Date then Period
- **All Lessons** — Table, sorted by Date descending
- **By Unit** — Table, grouped by Unit Name
- **Lesson Calendar** — Calendar view, by Date
- **Needs Planning** — Filter: Status = Draft
- **Needs Reflection** — Filter: Status = Taught AND Reflection is empty
- **By Subject** — Table, grouped by Subject
- **Board by Status** — Kanban, grouped by Status

---

### 2. Units

**Purpose:** Map out multi-week instructional units with pacing, essential questions, and summative assessments.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Unit Name | Title | Descriptive name (e.g., "Unit 3: Fractions & Decimals") |
| Subject | Select | Math / ELA / Science / Social Studies / Art / Music / PE / World Language / Other |
| Grade Level | Select | K–12 |
| Quarter / Semester | Select | Q1 / Q2 / Q3 / Q4 / S1 / S2 / Full Year |
| Start Date | Date | Unit kickoff date |
| End Date | Date | Unit conclusion date |
| Duration (Weeks) | Formula | `dateBetween(prop("End Date"), prop("Start Date"), "weeks")` |
| Status | Select | Planning / In Progress / Complete / Paused |
| Essential Questions | Text | 2-3 driving questions for the unit |
| Enduring Understandings | Text | What students should understand long-term |
| Standards Covered | Multi-select | Standards addressed across all lessons in this unit |
| Key Vocabulary | Text | Critical terms students must learn |
| Prior Knowledge | Text | What students should already know coming in |
| Summative Assessment | Text | Description of the unit's final assessment |
| Assessment Date | Date | When the summative assessment is scheduled |
| Performance Target | Text | What proficiency looks like for this unit |
| Unit Notes | Text | Pacing adjustments, curriculum notes, department alignment |
| Linked Lessons | Relation | → Lessons database |
| Lesson Count | Rollup | Count of linked Lessons |
| Lessons Taught | Rollup | Count of linked Lessons where Status = Taught |
| Completion % | Formula | `if(prop("Lesson Count") > 0, round(prop("Lessons Taught") / prop("Lesson Count") * 100), 0)` |
| Tags | Multi-select | Core / Enrichment / Remediation / Test Prep / Cross-Curricular |

**Views:**
- **All Units** — Table, sorted by Start Date
- **Active Units** — Filter: Status = In Progress
- **Unit Timeline** — Timeline view, Start Date to End Date
- **By Subject** — Table, grouped by Subject
- **By Quarter** — Table, grouped by Quarter/Semester
- **Unit Board** — Kanban, grouped by Status
- **Pacing Check** — Table, showing Completion % vs. Duration, sorted by Completion % ascending

---

### 3. Students

**Purpose:** Master roster with contact info, accommodations, grade tracking, and parent communication.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Student Name | Title | Last, First format |
| First Name | Text | For personalized communications |
| Student ID | Text | School-assigned ID number |
| Grade Level | Select | K–12 |
| Period / Block | Select | 1st / 2nd / 3rd / 4th / 5th / 6th / 7th / 8th |
| Status | Select | Active / Transferred / Withdrawn |
| Parent/Guardian Name | Text | Primary contact |
| Parent Email | Email | Primary contact email |
| Parent Phone | Phone | Primary contact phone |
| Preferred Contact | Select | Email / Phone / App (ClassDojo, Remind, etc.) |
| IEP | Checkbox | Student has an IEP |
| 504 Plan | Checkbox | Student has a 504 plan |
| ELL | Checkbox | English Language Learner |
| Accommodation Notes | Text | Specific accommodations to implement |
| Seating Notes | Text | Seating preferences or requirements |
| Assignment 1 | Number | Score (points or percentage) |
| Assignment 2 | Number | |
| Assignment 3 | Number | |
| Assignment 4 | Number | |
| Assignment 5 | Number | |
| Quiz 1 | Number | |
| Quiz 2 | Number | |
| Test 1 | Number | |
| Test 2 | Number | |
| Participation | Number | Ongoing participation score |
| Current Average | Formula | `round((prop("Assignment 1") + prop("Assignment 2") + prop("Assignment 3") + prop("Assignment 4") + prop("Assignment 5") + prop("Quiz 1") + prop("Quiz 2") + prop("Test 1") + prop("Test 2") + prop("Participation")) / 10)` |
| Letter Grade | Formula | `if(prop("Current Average") >= 90, "A", if(prop("Current Average") >= 80, "B", if(prop("Current Average") >= 70, "C", if(prop("Current Average") >= 60, "D", "F"))))` |
| Grade Status | Formula | `if(prop("Current Average") >= 70, "Passing", "At Risk")` |
| Behavior Notes | Text | Running log of behavioral observations |
| Strengths | Text | Academic and personal strengths |
| Growth Areas | Text | Areas for improvement |
| Last Parent Contact | Date | Date of most recent parent communication |
| Contact Log | Text | Running log: date, method, topic, outcome |
| Tags | Multi-select | Honor Roll / Tutoring / Gifted / At-Risk / New Student / Behavior Plan |

**Views:**
- **Full Roster** — Table, sorted by Student Name
- **By Period** — Table, grouped by Period/Block
- **At-Risk Students** — Filter: Grade Status = "At Risk"
- **IEP/504 Students** — Filter: IEP = true OR 504 Plan = true
- **Student Cards** — Gallery view, showing name, photo placeholder, grade, and status
- **Needs Parent Contact** — Filter: Last Parent Contact is more than 30 days ago OR is empty
- **Grade Overview** — Table, showing Student Name, Current Average, Letter Grade, Grade Status
- **Honor Roll** — Filter: Current Average >= 90

---

### 4. Resources

**Purpose:** A searchable library of every teaching resource — worksheets, videos, websites, books, manipulatives, and digital tools.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Resource Name | Title | Clear, findable name |
| Type | Select | Worksheet / Video / Website / Textbook / Book / Manipulative / App / Game / Slide Deck / Poster / Assessment / Other |
| Subject | Select | Math / ELA / Science / Social Studies / Art / Music / PE / World Language / Other |
| Grade Level | Multi-select | K / 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 / 11 / 12 |
| Standards | Multi-select | Aligned standards codes |
| Topic | Text | Specific topic or skill |
| URL | URL | Link to digital resource |
| File Location | Text | Physical location or drive path |
| Source | Text | Where you found it (TPT, colleague, curriculum, self-made) |
| Cost | Select | Free / Paid / Included with Curriculum |
| Quality Rating | Select | 5-Excellent / 4-Good / 3-Average / 2-Below Average / 1-Poor |
| Student Engagement | Select | High / Medium / Low |
| Differentiation Level | Select | Below Grade / On Grade / Above Grade / All Levels |
| Notes | Text | How to use, modifications, tips |
| Last Used | Date | When you last used this in class |
| Linked Lessons | Relation | → Lessons database |
| Times Used | Rollup | Count of linked Lessons |
| Tags | Multi-select | Printable / Digital / Hands-On / Centers / Homework / Assessment / Sub Plan / Anchor Chart |

**Views:**
- **All Resources** — Table, sorted by Resource Name
- **By Subject** — Table, grouped by Subject
- **By Type** — Table, grouped by Type
- **Top Rated** — Filter: Quality Rating = 5-Excellent or 4-Good, sorted by Times Used descending
- **Recently Used** — Table, sorted by Last Used descending
- **Never Used** — Filter: Times Used = 0 or Last Used is empty
- **Printables** — Filter: Tags contains Printable
- **Digital Resources** — Filter: Type = Website OR App OR Video
- **Search by Standard** — Table, grouped by Standards

---

## DASHBOARD

> Create this as a Notion page that pulls from all four databases using linked views and summary blocks.

### Dashboard Layout

```
┌──────────────────────────────────────────────────────────┐
│  CLASSROOM HQ — [Your Name]              Week of Apr 7   │
├──────────────┬──────────────┬───────────┬────────────────┤
│  Lessons     │  Units in    │ Students  │  At-Risk       │
│  This Week   │  Progress    │  Active   │  Students      │
│    5         │     2        │    28     │    3           │
├──────────────┴──────────────┴───────────┴────────────────┤
│  THIS WEEK'S LESSONS                                     │
│  [Linked view → Lessons, filter: Date = this week]       │
│  Mon: Intro to Fractions (Period 2, 3)                   │
│  Tue: Fraction Models — Guided Practice                  │
│  Wed: Comparing Fractions                                │
│  Thu: Fraction Word Problems                             │
│  Fri: Fractions Quiz + Reflection                        │
├──────────────────────────────────────────────────────────┤
│  NEEDS PLANNING                                          │
│  [Linked view → Lessons, filter: Status = Draft]         │
├──────────────────────────────────────────────────────────┤
│  NEEDS REFLECTION                                        │
│  [Linked view → Lessons, filter: Taught + no Reflection] │
├──────────────────────────────────────────────────────────┤
│  ACTIVE UNITS — PACING CHECK                             │
│  [Linked view → Units, filter: Status = In Progress]     │
│  Unit 3: Fractions — 60% complete (on pace)              │
│  Unit 4: Geometry — 25% complete (behind)                │
├──────────────────────────────────────────────────────────┤
│  AT-RISK STUDENTS                                        │
│  [Linked view → Students, filter: Grade Status=At Risk]  │
├──────────────────────────────────────────────────────────┤
│  PARENT CONTACT NEEDED                                   │
│  [Linked view → Students, filter: Last Contact > 30 days]│
├──────────────────────────────────────────────────────────┤
│  RECENTLY ADDED RESOURCES                                │
│  [Linked view → Resources, sorted: Last Used desc]       │
└──────────────────────────────────────────────────────────┘
```

---

## LESSON PLAN TEMPLATE (Copy for each new lesson)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LESSON PLAN

Subject:     [Subject]
Grade:       [Grade Level]
Date:        [Date]
Period:      [Period/Block]
Duration:    [Duration]
Unit:        [Unit Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STANDARDS:   [List applicable standards]
OBJECTIVE:   Students will be able to [measurable verb] [content] [condition].
ESSENTIAL Q: [Driving question for the lesson]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MATERIALS NEEDED:
- [Material 1]
- [Material 2]
- [Material 3]
- Technology: [devices/apps needed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WARM-UP / DO NOW (5 min)
─────────────────────────────────────────────────────────
[Quick review, bell ringer, or activation activity]

DIRECT INSTRUCTION — I DO (10-15 min)
─────────────────────────────────────────────────────────
[Teacher modeling, explicit instruction, think-aloud]

GUIDED PRACTICE — WE DO (10-15 min)
─────────────────────────────────────────────────────────
[Collaborative practice, partner work, scaffolded tasks]

INDEPENDENT PRACTICE — YOU DO (10-15 min)
─────────────────────────────────────────────────────────
[Student application, individual practice, centers]

CLOSURE (5 min)
─────────────────────────────────────────────────────────
[Exit ticket, summary, reflection prompt]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIFFERENTIATION:
  Below Grade Level: [Modifications, scaffolds, supports]
  Above Grade Level: [Extensions, enrichment, challenges]
  IEP/504:          [Specific accommodations per student]
  ELL:              [Language supports, visual aids, vocab]

ASSESSMENT:
  Type:    [Formative / Summative / Exit Ticket / Observation]
  Method:  [How you'll assess — what are you looking for?]

HOMEWORK:
  [Assignment description, due date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

POST-LESSON REFLECTION (fill in after teaching):
  What worked:        ________________________________
  What to adjust:     ________________________________
  Student engagement: [High / Medium / Low]
  Reteach needed:     [Yes — specify / No]
  Notes for next year: _______________________________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## KEY FORMULA REFERENCE

**Current Average (Student):**
```
round(
  (
    prop("Assignment 1") + prop("Assignment 2") + prop("Assignment 3") +
    prop("Assignment 4") + prop("Assignment 5") + prop("Quiz 1") +
    prop("Quiz 2") + prop("Test 1") + prop("Test 2") + prop("Participation")
  ) / 10
)
```
Customize: Adjust the divisor based on how many grade fields you actually use. For weighted grades, multiply each category by its weight before dividing.

**Letter Grade:**
```
if(prop("Current Average") >= 90, "A",
  if(prop("Current Average") >= 80, "B",
    if(prop("Current Average") >= 70, "C",
      if(prop("Current Average") >= 60, "D", "F")
    )
  )
)
```
Customize: Adjust thresholds to match your school's grading scale (e.g., 93+ for A at schools using a 7-point scale).

**Grade Status (At-Risk Flag):**
```
if(prop("Current Average") >= 70, "Passing", "At Risk")
```

**Unit Completion %:**
```
if(
  prop("Lesson Count") > 0,
  round(prop("Lessons Taught") / prop("Lesson Count") * 100),
  0
)
```

**Unit Duration (Weeks):**
```
dateBetween(prop("End Date"), prop("Start Date"), "weeks")
```

**Parent Contact Alert:**
Create a filtered view of Students where Last Parent Contact is more than 30 days ago or is empty. These students need outreach.

---

## PARENT COMMUNICATION TEMPLATES

### Progress Update (Positive)
> Subject: [Student Name] — Progress Update from [Your Name]

Hi [Parent Name],

I wanted to share a positive update on [Student's First Name]'s progress in [Subject]. [He/She/They] has been [specific positive observation — e.g., "actively participating in group discussions," "showing strong improvement on fraction concepts," "consistently turning in thoughtful work"].

[Student's First Name]'s current average is [grade], and [he/she/they] [specific recent achievement or growth].

Please let me know if you have any questions or would like to discuss [Student's First Name]'s progress further.

Best,
[Your Name]

---

### Concern / Check-In
> Subject: [Student Name] — [Subject] Class Check-In

Hi [Parent Name],

I'm reaching out about [Student's First Name]'s performance in [Subject]. I've noticed [specific, observable concern — e.g., "several missing assignments this quarter," "difficulty with the current unit on fractions," "a drop in participation over the past two weeks"].

[Student's First Name]'s current average is [grade]. I'd like to work together to support [him/her/them]. Some things that might help:

- [Specific suggestion 1]
- [Specific suggestion 2]
- [Specific suggestion 3]

Would you be available for a quick call or meeting this week? I'm available [days/times].

Thank you,
[Your Name]

---

### Conference Follow-Up
> Subject: Follow-Up — [Student Name] Conference on [Date]

Hi [Parent Name],

Thank you for meeting with me on [date] to discuss [Student's First Name]'s progress. Here's a summary of what we discussed and agreed on:

**Key Points:**
- [Point 1]
- [Point 2]
- [Point 3]

**Action Items:**
- [Your commitment — what you'll do]
- [Parent commitment — what they agreed to do]
- [Student commitment — what the student will do]

**Follow-up:** I'll check in again on [date] to see how things are going.

Please don't hesitate to reach out in the meantime.

Best,
[Your Name]

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Class Info
- Open the **Students** database and enter your class roster
- Fill in student names, grade level, period/block, and parent contact info
- Mark IEP, 504, and ELL checkboxes for applicable students
- Add accommodation notes for students who need them

### Step 2 — Build Your First Unit
- Open **Units** and click "+ New"
- Enter the unit name, subject, grade level, and quarter
- Set start and end dates based on your pacing guide
- Write your essential questions and enduring understandings
- List key vocabulary and the summative assessment plan

### Step 3 — Plan Your First Week of Lessons
- Open **Lessons** and click "+ New" for each day
- Link each lesson to the appropriate Unit
- Fill in the learning objective, standards, and essential question
- Use the lesson plan sections: Warm-Up, Direct Instruction, Guided Practice, Independent Practice, Closure
- Add differentiation notes for below-grade, above-grade, and accommodated students
- Set status to "Planned"

### Step 4 — Start Your Resource Library
- Open **Resources** and add 10-15 of your most-used resources
- Tag each with subject, grade level, type, and standards
- Include URLs for digital resources and file locations for physical ones
- Rate quality and student engagement based on past experience
- Link resources to the lessons that use them

### Step 5 — Use the Dashboard Daily
- Pin the Dashboard page to your Notion sidebar
- Check "This Week's Lessons" every morning for your daily plan
- After teaching, update lesson status to "Taught" and fill in the Reflection field
- Check "Needs Planning" on Sundays to prep the upcoming week
- Review "At-Risk Students" weekly and log parent communications

### Step 6 — Build the Weekly Habit
- **Sunday (30 min):** Plan next week's lessons — duplicate and modify previous lessons when topics repeat
- **Daily (5 min):** Review today's lesson plan, check materials list
- **After each lesson (2 min):** Mark status to Taught, add a one-line reflection
- **Friday (10 min):** Update grades, check pacing on active units, note any parent contacts needed
- **Monthly (20 min):** Review at-risk students, update unit pacing, clean up resource library

### Pro Tips
- Duplicate lessons that repeat across periods — change only the period and any differentiation notes
- Use the Reflection Rating to quickly identify lessons to rework vs. repeat as-is next year
- Tag resources as "Sub Plan" so you always have a curated list ready for substitute teachers
- Archive completed units by changing status to "Complete" — they won't clutter your active views but remain searchable
- Export student grade views to share with administrators or during parent conferences
- Use the "By Standard" resource view before planning to see what you already have for each standard
