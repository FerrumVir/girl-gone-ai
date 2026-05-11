# Certification Exam Tracker — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with study plans, practice test analytics, weak area identification, and exam countdown systems already configured. Read the Quick-Start Guide at the bottom before beginning your certification journey.

---

## DATABASES

---

### 1. Certifications

**Purpose:** Master record for each certification you're pursuing or have earned. Tracks the exam details, study timeline, requirements, costs, and maintenance/renewal obligations. Your certification portfolio and planning hub.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Certification Name | Title | Full name — e.g. "AWS Solutions Architect — Associate (SAA-C03)" |
| Issuing Body | Select | AWS / Microsoft / Google Cloud / CompTIA / PMI / ISC2 / Cisco / Salesforce / CPA Board / Oracle / Scrum Alliance / ISACA / HRCI / HubSpot / Other |
| Category | Select | Cloud / Security / Networking / Project Management / Data / Development / Business / Finance / Marketing / HR / Agile / DevOps / AI/ML / Other |
| Exam Code | Text | Official exam code — e.g. "SAA-C03" or "PMP" |
| Status | Select | Researching / Planned / Studying / Scheduled / Passed / Failed / Expired / Renewed |
| Priority | Select | Must Have (Career Requirement) / High (Career Advancement) / Medium (Skill Validation) / Low (Nice to Have) |
| Target Exam Date | Date | When you plan to take the exam |
| Actual Exam Date | Date | When you actually took it |
| Days Until Exam | Formula | `if(empty(prop("Target Exam Date")), "No date set", if(dateBetween(prop("Target Exam Date"), now(), "days") < 0, "PAST", format(dateBetween(prop("Target Exam Date"), now(), "days")) + " days"))` |
| Study Start Date | Date | When you began preparation |
| Total Study Days | Formula | `if(or(empty(prop("Study Start Date")), empty(prop("Target Exam Date"))), "—", format(dateBetween(prop("Target Exam Date"), prop("Study Start Date"), "days")) + " days")` |
| Study Hours Target | Number | Total hours you plan to study |
| Study Hours Logged | Rollup | Sum of Duration from linked Study Sessions |
| Study Progress % | Formula | `if(prop("Study Hours Target") == 0, "0%", format(round(prop("Study Hours Logged") / prop("Study Hours Target") * 100)) + "%")` |
| Passing Score | Number | Minimum score to pass (e.g., 720 for AWS, 61% for PMP) |
| My Score | Number | Your actual exam score (fill in after) |
| Pass/Fail | Formula | `if(empty(prop("My Score")), "—", if(prop("My Score") >= prop("Passing Score"), "PASSED", "FAILED"))` |
| Exam Duration (mins) | Number | How long the exam is |
| Number of Questions | Number | Total questions on the exam |
| Question Format | Multi-select | Multiple Choice / Multiple Response / Drag & Drop / Scenario-Based / Performance-Based / Essay / Simulation / Case Study |
| Exam Cost | Number (USD) | Registration fee |
| Retake Cost | Number (USD) | Fee for retaking if failed |
| Total Investment | Rollup | Sum of all costs (courses, materials, exam fee) |
| Prerequisites | Text | Required certifications or experience |
| Experience Required | Text | Work experience needed (e.g., "3 years project management") |
| Validity Period | Text | How long the cert is valid — e.g. "3 years" |
| Expiration Date | Date | When your certification expires (if earned) |
| Renewal Requirements | Text | What's needed to renew — CEUs, re-exam, etc. |
| Renewal Cost | Number (USD) | Cost to renew |
| CEUs Required | Number | Continuing education units needed for renewal |
| CEUs Earned | Number | CEUs completed so far |
| Certification Number | Text | Your credential number (after passing) |
| Digital Badge URL | URL | Link to your Credly/Acclaim badge |
| Certificate File | Files & Media | PDF of your certificate |
| Study Resources | Text | Primary materials — courses, books, practice exams |
| Official Study Guide | URL | Link to official prep materials |
| Exam Registration URL | URL | Where to schedule the exam |
| Testing Center | Text | Where you'll take it (or "Online/Remote") |
| Difficulty Rating | Select | Easy / Moderate / Hard / Very Hard / Brutal |
| Community Rating | Text | What others say about difficulty (Reddit, forums) |
| Average Practice Score | Rollup | Average of Score % from linked Practice Tests |
| Best Practice Score | Rollup | Max of Score % from linked Practice Tests |
| Weak Areas | Rollup | From linked Study Topics where Mastery = Weak |
| Career Impact | Text | How this cert will benefit your career specifically |
| Salary Impact | Text | Expected salary bump based on research |
| Linked Study Sessions | Relation | → Study Sessions database |
| Linked Practice Tests | Relation | → Practice Tests database |
| Linked Study Topics | Relation | → Study Topics database |
| Linked Expenses | Relation | → Expenses database |
| Notes | Text | General notes, strategy, exam tips from others |

**Views:**

- **All Certifications** — Table, sorted by Status then Priority
- **Active Study** — Filter: Status = Studying or Scheduled
- **Dashboard Cards** — Gallery showing Cert Name, Days Until Exam, Study Progress %, Average Practice Score
- **Exam Countdown** — Filter: Status = Studying or Scheduled, sorted by Target Exam Date ascending
- **Earned** — Filter: Status = Passed or Renewed (your credential portfolio!)
- **By Category** — Table, grouped by Category
- **By Issuing Body** — Table, grouped by Issuing Body
- **Expiring Soon** — Filter: Expiration Date within 90 days (renew before it lapses!)
- **Failed (Retake Needed)** — Filter: Status = Failed
- **Planned** — Filter: Status = Planned or Researching (future study queue)
- **Investment Tracker** — Table showing Cert Name, Exam Cost, Total Investment, Career Impact

---

### 2. Study Topics / Domains

**Purpose:** Break each certification exam into its component domains, topics, and objectives. Track mastery level for each area so you know exactly where to focus your study time. Maps directly to the exam blueprint/content outline.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Topic Name | Title | Domain or objective — e.g. "Design Resilient Architectures" |
| Certification | Relation | → Certifications database |
| Cert Name | Rollup | From Certification relation |
| Domain Number | Number | Domain/section order (1, 2, 3...) |
| Exam Weight % | Number | What percentage of the exam covers this topic |
| Weighted Importance | Formula | `if(prop("Exam Weight %") >= 25, "Heavy", if(prop("Exam Weight %") >= 15, "Moderate", "Light"))` |
| Subtopics | Text | Detailed list of sub-objectives within this domain |
| Key Concepts | Text | Core concepts you must understand |
| Mastery Level | Select | Not Started / Weak / Developing / Proficient / Mastered |
| Confidence | Select | Very Confident / Somewhat Confident / Neutral / Shaky / No Clue |
| Study Priority | Formula | Calculated from Exam Weight % and Mastery Level — high weight + low mastery = highest priority |
| Hours Studied | Number | Time spent on this specific topic |
| Last Studied | Date | When you last focused on this topic |
| Days Since Study | Formula | `if(empty(prop("Last Studied")), "Never", format(dateBetween(now(), prop("Last Studied"), "days")) + " days")` |
| Practice Test Performance | Text | How you score on questions in this domain |
| Common Question Types | Text | What kinds of questions appear for this topic |
| Tricky Areas | Text | Specific concepts or question patterns that trip you up |
| Study Resources | Text | Best resources specifically for this topic |
| Resource URLs | URL | Links to videos, articles, documentation |
| Flashcards Created | Checkbox | Have you made flashcards for this topic? |
| Hands-On Lab | Checkbox | Have you done practical exercises? |
| Lab Notes | Text | Notes from hands-on practice |
| Real-World Experience | Select | Extensive / Some / Minimal / None |
| Notes | Text | Study notes, mnemonics, key facts to memorize |
| Tags | Multi-select | Core / Advanced / Memorization Required / Lab Required / Hands-On / Theory / Calculation / Scenario-Based |

**Views:**

- **All Topics** — Table, sorted by Certification then Domain Number
- **By Certification** — Table, grouped by Cert Name
- **Weak Areas** — Filter: Mastery Level = Weak or Not Started, sorted by Exam Weight % descending (study these first!)
- **High Weight** — Filter: Exam Weight % >= 20, sorted descending (bang for your buck)
- **Study Priority** — Table sorted by custom priority formula (high weight + low mastery = top)
- **Mastery Board** — Kanban grouped by Mastery Level
- **Needs Review** — Filter: Days Since Study > 14 AND Mastery Level != Mastered
- **Mastered** — Filter: Mastery Level = Mastered (confidence booster)
- **By Confidence** — Table, grouped by Confidence
- **Exam Blueprint** — Table showing Domain Number, Topic Name, Exam Weight %, Mastery Level (mirrors official exam guide)

---

### 3. Practice Tests

**Purpose:** Track every practice exam, quiz, and mock test you take. Analyzes scores over time, identifies weak domains, and determines exam readiness. The most predictive factor of exam success is consistent practice test scores above the passing threshold.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Test Name | Title | Which test — e.g. "Tutorials Dojo Practice Exam 2" |
| Certification | Relation | → Certifications database |
| Cert Name | Rollup | From Certification relation |
| Date Taken | Date | When you took this practice test |
| Source | Select | Official Practice / Tutorials Dojo / Whizlabs / MeasureUp / Kaplan / Boson / ExamTopics / Pocket Prep / Course Quiz / Custom / Other |
| Test Type | Select | Full Mock Exam / Domain-Specific / Quick Quiz / Timed / Untimed / Review Mode |
| Total Questions | Number | Number of questions on this test |
| Correct Answers | Number | Questions answered correctly |
| Score % | Formula | `if(prop("Total Questions") == 0, 0, round(prop("Correct Answers") / prop("Total Questions") * 100))` |
| Passing Score | Number | Target score (from certification) |
| Pass/Fail | Formula | `if(prop("Score %") >= prop("Passing Score"), "PASS", "FAIL")` |
| Points Above/Below | Formula | `prop("Score %") - prop("Passing Score")` |
| Time Taken (mins) | Number | How long you spent |
| Time Per Question | Formula | `if(prop("Total Questions") == 0, "—", format(round(prop("Time Taken (mins)") / prop("Total Questions") * 10) / 10) + " min/question")` |
| Timed | Checkbox | Were you under time pressure? |
| Ran Out of Time | Checkbox | Did time expire before finishing? |
| Domain Breakdown | Text | Score per domain — e.g. "Domain 1: 80%, Domain 2: 60%, Domain 3: 90%" |
| Weakest Domain | Text | Which domain had the lowest score |
| Strongest Domain | Text | Which domain had the highest score |
| Questions Flagged | Number | Questions you were unsure about |
| Guessed Correctly | Number | Flagged questions that happened to be right (don't count on these) |
| Adjusted Score | Formula | Score minus lucky guesses — more realistic readiness indicator |
| Incorrect Topics | Text | Specific topics/concepts you got wrong |
| Key Mistakes | Text | Pattern of errors — misread question? Wrong concept? Rushed? |
| Lessons Learned | Text | What this test taught you about your preparation |
| Review Completed | Checkbox | Did you review all incorrect answers? |
| Review Notes | Text | Notes from reviewing wrong answers |
| Confidence After | Select | Ready for Exam / Almost Ready / Need More Study / Not Ready / Panicking |
| Attempt Number | Number | 1st, 2nd, 3rd attempt at this specific test (track improvement) |
| Improvement from Last | Formula | Compare to previous attempt score |
| Tags | Multi-select | Baseline / Final Prep / Domain Focus / Retake / Timed / Untimed / Confidence Builder |
| Notes | Text | Test-specific observations |

**Views:**

- **All Practice Tests** — Table, sorted by Date Taken descending
- **By Certification** — Table, grouped by Cert Name
- **Score Progression** — Table sorted by Date Taken ascending (watch scores improve!)
- **Passing** — Filter: Pass/Fail = PASS (confidence view)
- **Failing** — Filter: Pass/Fail = FAIL (reality check — more study needed)
- **By Source** — Table, grouped by Source (which test banks are best?)
- **Recent (Last 7 Days)** — Filter: Date Taken within 7 days
- **Needs Review** — Filter: Review Completed = false (don't skip the review!)
- **Full Mock Exams** — Filter: Test Type = Full Mock Exam (most predictive of real score)
- **Domain-Specific** — Filter: Test Type = Domain-Specific
- **Weak Domain Analysis** — Table showing Date, Weakest Domain, Score % (identify persistent weak areas)

---

### 4. Study Sessions

**Purpose:** Log every study activity — video lessons, reading, practice labs, flashcards, and practice tests. Builds accountability, tracks time investment, and helps optimize your study schedule based on what's working.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | What you studied — e.g. "VPC and Networking — Stephane Maarek Ch. 7" |
| Certification | Relation | → Certifications database |
| Cert Name | Rollup | From Certification relation |
| Topic | Relation | → Study Topics database |
| Topic Name | Rollup | From Topic relation |
| Date | Date | Study date |
| Duration (mins) | Number | Time spent |
| Duration (hrs) | Formula | `format(round(prop("Duration (mins)") / 60 * 100) / 100) + "h"` |
| Activity Type | Select | Video Course / Reading / Practice Exam / Hands-On Lab / Flashcards / Note-Taking / Review / Study Group / Tutoring / Documentation / White Paper / Podcast |
| Resource | Text | Specific resource used — course name, book chapter, etc. |
| Topics Covered | Text | Specific concepts or objectives covered |
| Key Learnings | Text | Main things you learned or clarified |
| Confused About | Text | What's still unclear after this session |
| Focus Level | Select | Deep Focus / Moderate / Distracted / Very Distracted |
| Effectiveness | Select | Highly Effective / Effective / Neutral / Ineffective |
| Energy Level | Select | High / Medium / Low / Exhausted |
| Time of Day | Select | Early Morning / Morning / Afternoon / Evening / Late Night |
| Study Method | Select | Active Recall / Spaced Repetition / Practice Questions / Video + Notes / Reading + Highlighting / Hands-On / Teaching/Explaining / Mind Map / Flashcards |
| Pomodoros | Number | If using Pomodoro technique — how many 25-min blocks |
| Confidence Change | Select | More Confident / Same / Less Confident |
| Week Number | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Tags | Multi-select | Morning Study / Evening Study / Weekend / Weekday / Quick Session / Deep Session / Pre-Exam / Review |
| Notes | Text | Session observations and reflections |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **By Certification** — Table, grouped by Cert Name
- **This Week** — Filter: Date is this week
- **By Topic** — Table, grouped by Topic Name (time per domain)
- **By Activity Type** — Table, grouped by Activity Type
- **Calendar** — Calendar view by Date
- **Effectiveness Analysis** — Table grouped by Activity Type, showing average Effectiveness
- **Weekly Hours** — Table grouped by Week Number with sum of Duration
- **Study Streak** — Table sorted by Date (track consecutive days)
- **High Effectiveness** — Filter: Effectiveness = Highly Effective (do more of this!)
- **Low Focus** — Filter: Focus Level = Distracted or Very Distracted (identify patterns)
- **Time of Day Analysis** — Table grouped by Time of Day (when do you study best?)

---

### 5. Expenses

**Purpose:** Track all certification-related spending — courses, books, practice exams, exam fees, and renewal costs. Provides a clear picture of your total investment and helps justify the expense through salary impact data.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Expense Name | Title | What you purchased |
| Certification | Relation | → Certifications database |
| Cert Name | Rollup | From Certification relation |
| Date | Date | Purchase date |
| Category | Select | Exam Fee / Retake Fee / Video Course / Practice Exams / Book / Study Guide / Lab Subscription / Bootcamp / Flashcards / Renewal Fee / CEU Course / Membership / Travel / Other |
| Amount | Number (USD) | Cost |
| Vendor | Text | Where purchased |
| Platform | Select | AWS / Udemy / A Cloud Guru / Pluralsight / Whizlabs / Tutorials Dojo / Amazon / Official / Other |
| Payment Method | Select | Personal / Company Reimbursement / Training Budget / Scholarship |
| Reimbursed | Checkbox | Was this reimbursed by employer? |
| Reimbursement Amount | Number (USD) | How much was reimbursed |
| Net Cost | Formula | `prop("Amount") - prop("Reimbursement Amount")` |
| Tax Deductible | Checkbox | Can deduct as professional development |
| Receipt | Files & Media | Upload receipt |
| Subscription | Checkbox | Is this a recurring subscription? |
| Subscription Period | Select | Monthly / Annual / One-Time |
| Access Expiration | Date | When your access to this resource expires |
| Value Rating | Select | Essential / Helpful / Okay / Waste / Didn't Use |
| Notes | Text | Resource quality notes, login info |

**Views:**

- **All Expenses** — Table, sorted by Date descending
- **By Certification** — Table, grouped by Cert Name (cost per cert)
- **By Category** — Table, grouped by Category
- **Unreimbursed** — Filter: Reimbursed = false AND Payment Method = Personal
- **Subscriptions** — Filter: Subscription = true (track recurring costs)
- **Expiring Access** — Filter: Access Expiration within 30 days
- **Total Investment** — Table with sum of Net Cost
- **This Year** — Filter: Date is this year
- **Tax Deductible** — Filter: Tax Deductible = true (for tax prep)

---

## EXAM READINESS ASSESSMENT

> Use this framework to determine if you're truly ready to schedule your exam or need more preparation time.

### Readiness Indicators

| Indicator | Not Ready | Almost Ready | Ready | Confident |
|---|---|---|---|---|
| Practice Test Average | Below passing | At passing | 10% above passing | 15%+ above passing |
| Consecutive passes | 0 | 1–2 | 3+ | 5+ |
| Weak domains | 3+ weak areas | 1–2 weak areas | No weak areas | All proficient+ |
| Study hours | < 50% of target | 50–75% | 75–100% | 100%+ |
| Hands-on labs | Not done | Partially done | All completed | Created own scenarios |
| Time management | Running out of time | Tight but finishing | Comfortable | Time to spare |
| Confidence | Panicking | Nervous | Cautiously optimistic | Ready to crush it |

### When to Schedule the Exam

Schedule your exam when:

1. You've passed 3+ full-length practice exams in a row
2. Your average practice score is 10%+ above the passing threshold
3. No domain scores below passing on the last 2 practice exams
4. You've completed all hands-on labs for applicable topics
5. You can explain every wrong answer from your last practice test
6. Your "lucky guess" adjusted score still passes

### Exam Day Checklist

- [ ] Photo ID ready
- [ ] Testing center address confirmed (or online proctoring environment prepped)
- [ ] Calculator, scratch paper, or allowed materials ready
- [ ] Water and snack for break (if applicable)
- [ ] Arrive 30 minutes early (or log in 30 min before for online)
- [ ] Quick review of weak areas (15 min, no more)
- [ ] Deep breaths — you've prepared for this
- [ ] Read every question twice before answering
- [ ] Flag uncertain questions and return to them
- [ ] Manage time: check progress at 25%, 50%, 75% marks

---

## STUDY PLAN TEMPLATES

### AWS Certification — 8 Week Plan

| Week | Focus | Hours | Activities |
|---|---|---|---|
| 1 | Foundation + Domain 1 overview | 10 | Video course, initial notes |
| 2 | Domain 1 deep dive + Domain 2 start | 12 | Videos, hands-on labs |
| 3 | Domain 2 deep dive + Domain 3 start | 12 | Videos, labs, first practice quiz |
| 4 | Domain 3 + Domain 4 | 12 | Videos, labs, domain quizzes |
| 5 | Full review + First mock exam | 10 | Review notes, full practice test |
| 6 | Weak area focus + Second mock | 12 | Targeted study on weak domains |
| 7 | Third mock + Deep review | 10 | Practice exams, review all wrongs |
| 8 | Final prep + Exam day | 8 | Light review, confidence building |

### PMP Certification — 12 Week Plan

| Week | Focus | Hours | Activities |
|---|---|---|---|
| 1–2 | PMBOK overview + Predictive fundamentals | 12 | Reading, video course |
| 3–4 | Agile/Hybrid approaches | 12 | Videos, practice scenarios |
| 5–6 | People domain deep dive | 10 | Study, situational questions |
| 7–8 | Process + Business Environment domains | 12 | Study, mini-quizzes |
| 9 | Full mock exam #1 + review | 8 | Identify weak areas |
| 10 | Targeted weak area study | 10 | Focused domain review |
| 11 | Mock exams #2 and #3 | 10 | Build stamina for 180 questions |
| 12 | Final review + Exam | 6 | Light review, exam day |

### CPA Exam — Per Section Plan (6 Weeks)

| Week | Focus | Hours | Activities |
|---|---|---|---|
| 1 | Units 1–3, initial study | 15 | Reading, video lectures |
| 2 | Units 4–6, continue | 15 | Lectures, practice MCQs |
| 3 | Units 7–9, continue | 15 | Lectures, MCQs, simulations |
| 4 | Full section review + weak areas | 12 | Review, targeted practice |
| 5 | Practice exams + simulations | 12 | Mock exams, task-based simulations |
| 6 | Final review + Exam | 8 | Focused weak area, exam day |

---

## AUTOMATIONS / FORMULAS

### Days Until Exam

Countdown to your target exam date.

```
if(
  empty(prop("Target Exam Date")),
  "No date set",
  if(
    dateBetween(prop("Target Exam Date"), now(), "days") < 0,
    "PAST",
    format(dateBetween(prop("Target Exam Date"), now(), "days")) + " days"
  )
)
```

### Study Progress

Percentage of target study hours completed.

```
if(
  prop("Study Hours Target") == 0,
  "0%",
  format(round(prop("Study Hours Logged") / prop("Study Hours Target") * 100)) + "%"
)
```

### Practice Test Score

Percentage correct on a practice exam.

```
if(
  prop("Total Questions") == 0,
  0,
  round(prop("Correct Answers") / prop("Total Questions") * 100)
)
```

### Practice Test Pass/Fail

Binary indicator against the passing threshold.

```
if(prop("Score %") >= prop("Passing Score"), "PASS", "FAIL")
```

### Points Above/Below Passing

How far above or below the passing score.

```
prop("Score %") - prop("Passing Score")
```

### Time Per Question

Pacing metric for exam time management.

```
if(
  prop("Total Questions") == 0,
  "—",
  format(round(prop("Time Taken (mins)") / prop("Total Questions") * 10) / 10) + " min/question"
)
```

### Topic Study Priority

High exam weight + low mastery = highest study priority.

```
if(
  and(prop("Exam Weight %") >= 20, prop("Mastery Level") == "Weak"),
  "CRITICAL",
  if(
    or(
      and(prop("Exam Weight %") >= 20, prop("Mastery Level") == "Developing"),
      and(prop("Exam Weight %") >= 15, prop("Mastery Level") == "Weak")
    ),
    "High",
    if(
      prop("Mastery Level") == "Mastered",
      "Maintain",
      "Normal"
    )
  )
)
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Certification

- Open the **Certifications** database and create an entry
- Fill in: Cert Name, Exam Code, Issuing Body, Passing Score, Number of Questions, Exam Duration
- Set your Target Exam Date (even if approximate — it creates urgency)
- Calculate Study Hours Target (common benchmarks: AWS Associate = 80–120 hrs, PMP = 100–150 hrs, CPA per section = 80–120 hrs)
- Research and fill in Difficulty Rating and Study Resources

### Step 2 — Break Down the Exam Blueprint

- Open **Study Topics** and create entries for each domain on the official exam content outline
- Every certification body publishes an exam guide — use it as your map
- Fill in Exam Weight % for each domain (these are usually in the exam guide)
- Set initial Mastery Level honestly based on your current knowledge
- Note: domains with high weight AND low mastery are your #1 study priority

### Step 3 — Acquire Study Materials

- Based on your research, purchase your primary study resources
- Log each in the **Expenses** database
- Common stack: Video course + official study guide + practice exam bank + hands-on labs
- Open study material access links in the Notes or Resource fields

### Step 4 — Create Your Study Plan

- Based on your Target Exam Date and Study Hours Target, calculate hours per week needed
- Map domains to weeks using the study plan templates above as a starting point
- Front-load heavy-weight domains (more exam impact per study hour)
- Save 20–25% of total time for practice tests and review

### Step 5 — Start Studying and Logging

- Every study session, create an entry in **Study Sessions**
- Link to the Certification and Topic you're covering
- Log Duration, Activity Type, Focus Level, and Effectiveness
- After each session, note Key Learnings and update the Topic's Mastery Level if appropriate
- Aim for consistency over intensity — 1 hour daily beats 7 hours on Saturday

### Step 6 — Practice Testing Cycle

**After covering all domains (approximately 60% through your timeline):**
1. Take your first full-length practice exam
2. Log it in **Practice Tests** with full details
3. Review EVERY wrong answer (this is where the real learning happens)
4. Note your Weakest Domain and create a targeted study plan
5. Study weak areas for 3–5 days, then take another practice test
6. Repeat until you pass 3+ consecutive practice exams with 10%+ margin

### Study Rhythm

**Daily (while actively studying):**
- Study session: 60–90 minutes on target domain
- Log session in database
- 10–20 practice questions on today's topic
- Review flashcards for completed topics (spaced repetition)

**Weekly:**
- Take a domain-specific quiz to measure progress
- Update Topic Mastery Levels based on quiz performance
- Review Study Progress % — on track for your target date?
- Plan next week's focus areas
- Log any expenses (new resources purchased)

**Bi-weekly (or every 10 study sessions):**
- Take a full-length practice exam under timed conditions
- Detailed review of all incorrect answers
- Update weak area identification
- Adjust study plan based on results
- Assess: is your target date realistic?

**Pre-Exam Week:**
- Light review only — no new material
- Take 1–2 final practice exams for confidence
- Review your compiled "Key Mistakes" notes
- Focus on weak areas but don't cram
- Get good sleep, exercise, and eat well

### Pro Tips

- The official exam content outline is your bible — every question maps to a published objective. Study the outline, not random topics
- Practice tests are the #1 predictor of success. Your average score on quality practice exams (not brain dumps) closely predicts your real score
- Review wrong answers immediately — understanding WHY you got it wrong is more valuable than getting it right by guessing
- Track your "Guessed Correctly" count — these don't represent true knowledge. Your adjusted score is more realistic
- Study the highest-weighted domains first and most deeply — a 30% domain is 3x more important than a 10% domain
- Hands-on experience (labs, projects) cements concepts that reading alone cannot. Budget lab time even if it feels slow
- The "explain it to someone" test: if you can't explain a concept simply, you don't understand it deeply enough for scenario questions
- For timed exams, practice under time pressure. Many failures come from time management, not knowledge gaps
- Don't memorize brain dumps — they're often outdated and you learn nothing. Understand concepts and you'll handle any question variation
- If you fail, analyze WHERE you failed (domain breakdown), adjust your study plan, and rebook. Most people pass on the second attempt with targeted preparation
- Track your expenses and career impact — if a $300 cert leads to a $15K raise, that's a 50x ROI. This data helps justify future investments to yourself and your employer
