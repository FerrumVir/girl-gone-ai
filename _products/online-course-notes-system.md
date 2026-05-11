# Online Course Notes System — Notion Template

> Duplicate this page into your Notion workspace to get started. All four databases are pre-linked with progress tracking, key takeaway extraction, and action item management already configured. Read the Quick-Start Guide at the bottom before starting your next online course.

---

## DATABASES

---

### 1. Courses

**Purpose:** Master record for every online course, bootcamp, workshop, or learning program you're taking or have completed. Tracks platform, progress, completion status, and overall value assessment. Your lifelong learning portfolio.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Course Name | Title | Full course title — e.g. "The Complete Web Developer Bootcamp 2026" |
| Instructor | Text | Course creator or lead instructor |
| Platform | Select | Udemy / Coursera / Skillshare / LinkedIn Learning / YouTube / MasterClass / Pluralsight / edX / Khan Academy / Domestika / Maven / Cohort-Based / Book / Podcast Series / Company Training / Other |
| URL | URL | Link to the course |
| Category | Select | Programming / Design / Marketing / Business / Data Science / Writing / Finance / Photography / Music / Language / Health / Leadership / Product Management / AI/ML / Freelancing / Other |
| Subcategory | Text | More specific — e.g. "React" or "SEO" or "Watercolor" |
| Status | Select | Wishlist / Not Started / In Progress / Paused / Completed / Abandoned |
| Priority | Select | High (Career Critical) / Medium (Skill Building) / Low (Interest/Fun) |
| Start Date | Date | When you started |
| Completion Date | Date | When you finished |
| Total Modules | Number | Number of modules/sections in the course |
| Completed Modules | Rollup | Count of linked Modules where Status = Completed |
| Progress % | Formula | `if(prop("Total Modules") == 0, "0%", format(round(prop("Completed Modules") / prop("Total Modules") * 100)) + "%")` |
| Course Duration | Text | Total estimated time — e.g. "42 hours" or "8 weeks" |
| Time Invested (hrs) | Rollup | Sum of Time Spent from linked Modules |
| Certificate | Checkbox | Does this course offer a certificate? |
| Certificate Earned | Checkbox | Did you earn it? |
| Certificate Link | URL | Link to your certificate |
| Certificate File | Files & Media | Download of certificate PDF |
| Cost | Number (USD) | What you paid (0 for free courses) |
| ROI Assessment | Select | Life Changing / Highly Valuable / Worth It / Neutral / Waste of Time / Waste of Money |
| Difficulty | Select | Beginner / Intermediate / Advanced / Mixed |
| My Rating | Select | 5 Stars / 4 Stars / 3 Stars / 2 Stars / 1 Star |
| Would Recommend | Checkbox | Would you recommend this to others? |
| Recommendation Notes | Text | Who specifically would benefit from this course |
| Course Goals | Text | What you want to achieve by completing this course |
| Key Outcomes | Text | What you actually achieved (fill in after completion) |
| Prerequisites | Text | What you needed to know before starting |
| Tools Required | Text | Software, subscriptions, or equipment needed |
| Instructor Quality | Select | Exceptional / Good / Average / Poor |
| Production Quality | Select | Professional / Good / Adequate / Low / Outdated |
| Content Freshness | Select | Current / Mostly Current / Somewhat Dated / Outdated |
| Best Feature | Text | What makes this course stand out |
| Biggest Gap | Text | What the course is missing or does poorly |
| Related Courses | Relation | → Courses database (self-referential for learning paths) |
| Linked Modules | Relation | → Modules & Lessons database |
| Linked Action Items | Relation | → Action Items database |
| Tags | Multi-select | Career / Side Project / Certification / Fun / Required / Free / Paid / Self-Paced / Cohort / Video / Reading / Hands-On |
| Notes | Text | General course notes, login info, community links |

**Views:**

- **All Courses** — Table, sorted by Status then Course Name
- **In Progress** — Filter: Status = In Progress, sorted by Priority
- **Progress Board** — Kanban grouped by Status
- **By Platform** — Table, grouped by Platform
- **By Category** — Table, grouped by Category
- **Completed** — Filter: Status = Completed, sorted by Completion Date descending
- **Wishlist** — Filter: Status = Wishlist, sorted by Priority
- **Course Cards** — Gallery view showing Course Name, Progress %, Platform, Category, My Rating
- **High ROI** — Filter: ROI Assessment = Life Changing or Highly Valuable (replicate these!)
- **Abandoned** — Filter: Status = Abandoned (analyze why — pattern?)
- **Certificates Earned** — Filter: Certificate Earned = true
- **Investment Tracker** — Table showing Course Name, Cost, ROI Assessment, My Rating (worth the money?)

---

### 2. Modules & Lessons

**Purpose:** Individual sections, modules, or lessons within each course. This is where your actual notes live — detailed summaries, key concepts, timestamps, and your own synthesis of the material. The operational note-taking layer.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Module Title | Title | Section or lesson name — e.g. "Module 3: CSS Flexbox Deep Dive" |
| Course | Relation | → Courses database |
| Course Name | Rollup | From Course relation |
| Module Number | Number | Order within the course (1, 2, 3...) |
| Lesson Count | Number | Number of individual lessons in this module (if applicable) |
| Status | Select | Not Started / In Progress / Completed / Skipped / Review Needed |
| Date Started | Date | When you started this module |
| Date Completed | Date | When you finished it |
| Time Spent (hrs) | Number | Actual time spent on this module |
| Estimated Duration | Text | How long the platform says this module takes |
| Difficulty | Select | Easy / Moderate / Hard / Very Hard |
| Understanding Level | Select | Full Mastery / Good Understanding / Partial / Confused / Need to Rewatch |
| Notes | Text | Your full notes from this module (the main content field) |
| Key Concepts | Text | The 3–5 most important ideas or concepts |
| Key Takeaways | Text | What you'll actually remember and use from this module |
| Quotes & Highlights | Text | Exact quotes, formulas, or statements worth saving |
| Timestamps | Text | Important video timestamps — e.g. "12:34 — explains the closure concept" |
| Code Snippets | Text | Any code examples worth saving (use code blocks) |
| Screenshots | Files & Media | Captured slides or diagrams |
| Exercises Completed | Checkbox | Did you do the practice exercises? |
| Exercise Notes | Text | Notes from hands-on practice |
| Quiz Score | Text | If there was a quiz — your score |
| Questions I Have | Text | Things you didn't understand or want to explore further |
| Connections | Text | How this connects to what you already know or other courses |
| Summary (My Words) | Text | Explain this module as if teaching someone else |
| Would Rewatch | Checkbox | Worth revisiting in the future? |
| Rewatched | Checkbox | Have you already rewatched? |
| Linked Action Items | Relation | → Action Items database |
| Linked Takeaways | Relation | → Key Takeaways database |
| Tags | Multi-select | Core Concept / Practice Required / Reference / Skippable / Advanced / Foundational / Project-Based / Theory / Application |

**Views:**

- **All Modules** — Table, sorted by Course Name then Module Number
- **By Course** — Table, grouped by Course Name, sorted by Module Number
- **In Progress** — Filter: Status = In Progress
- **Completed** — Filter: Status = Completed
- **Need Review** — Filter: Status = Review Needed OR Understanding Level = Confused or Partial
- **Key Concepts** — Table showing Module Title, Key Concepts, Key Takeaways (reference view)
- **Questions Outstanding** — Filter: Questions I Have is not empty AND Status = Completed (things to research)
- **Would Rewatch** — Filter: Would Rewatch = true AND Rewatched = false
- **Exercises Incomplete** — Filter: Exercises Completed = false AND Status != Not Started
- **Course Outline** — Table grouped by Course Name, showing only Module Title, Status, Understanding Level (progress map)

---

### 3. Key Takeaways

**Purpose:** Distilled wisdom extracted from your course notes. Each entry is a single actionable insight, principle, or technique that you want to remember and apply long-term. This is your personal knowledge base — the gold you mined from hours of learning.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Takeaway | Title | The insight in one clear sentence |
| Course | Relation | → Courses database |
| Course Name | Rollup | From Course relation |
| Module | Relation | → Modules database |
| Category | Select | Principle / Technique / Framework / Mindset / Tool / Process / Fact / Quote / Resource / Tip |
| Domain | Select | Technical / Business / Creative / Personal / Strategy / Communication / Leadership / Productivity / Health / Finance |
| Importance | Select | Critical (use daily) / Important (use often) / Good to Know / Reference Only |
| Applied | Checkbox | Have you actually used this in real life? |
| Application Notes | Text | How and when you applied this takeaway |
| Date Captured | Date | When you noted this |
| Full Context | Text | The surrounding context that makes this takeaway meaningful |
| My Interpretation | Text | What this means to you specifically, in your own words |
| Related To | Text | How this connects to your work, projects, or goals |
| Source Quote | Text | If this is from a specific quote or reference |
| Reminder Frequency | Select | Daily / Weekly / Monthly / Quarterly / One-Time / As Needed |
| Last Reviewed | Date | When you last revisited this takeaway |
| Still Relevant | Checkbox | Is this still applicable to your current situation? |
| Tags | Multi-select | Career / Side Project / Habit / Mindset Shift / Process / Technical / Creative / Revenue / Personal Growth |
| Notes | Text | Additional context or related resources |

**Views:**

- **All Takeaways** — Table, sorted by Date Captured descending
- **By Course** — Table, grouped by Course Name
- **By Domain** — Table, grouped by Domain
- **Critical** — Filter: Importance = Critical (review these regularly!)
- **Not Yet Applied** — Filter: Applied = false AND Importance = Critical or Important (knowledge without action)
- **Applied Successfully** — Filter: Applied = true (proof of learning)
- **By Category** — Table, grouped by Category
- **Weekly Review** — Filter: Reminder Frequency = Weekly or Daily
- **Search by Tag** — Table with all tags visible for filtering
- **Recently Captured** — Filter: Date Captured within 30 days
- **Outdated** — Filter: Still Relevant = false (archive these)

---

### 4. Action Items

**Purpose:** Every actionable task that emerges from a course — projects to build, techniques to practice, habits to form, tools to explore, and skills to apply. Bridges the gap between learning and doing. Knowledge without application is just entertainment.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Action Item | Title | Specific, actionable task — e.g. "Build a portfolio site using Flexbox" |
| Course | Relation | → Courses database |
| Course Name | Rollup | From Course relation |
| Module | Relation | → Modules database |
| Type | Select | Project / Practice Exercise / Habit to Form / Tool to Try / Skill to Develop / Person to Contact / Resource to Read / Process to Implement / Experiment |
| Status | Select | To Do / In Progress / Completed / Deferred / Cancelled |
| Priority | Select | Must Do / Should Do / Could Do / Someday |
| Due Date | Date | If time-sensitive |
| Completed Date | Date | When you finished |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Completed", prop("Status") != "Cancelled"), true, false)` |
| Estimated Time (hrs) | Number | How long this will take |
| Actual Time (hrs) | Number | How long it actually took |
| Difficulty | Select | Quick Win (< 30 min) / Small (1–2 hrs) / Medium (half day) / Large (multi-day) / Ongoing |
| Context | Text | Why this action item matters — what completing it gives you |
| Steps | Text | Sub-tasks or steps to complete this item |
| Outcome | Text | What happened when you did this (fill in after) |
| Blocked By | Text | If something is preventing progress |
| Dependencies | Text | What needs to happen first |
| Related Project | Text | If this feeds into a larger project |
| Tags | Multi-select | Career / Portfolio / Skill Building / Networking / Tool Setup / Habit / Quick Win / Deep Work |
| Notes | Text | Additional context or ideas |

**Views:**

- **All Action Items** — Table, sorted by Status then Priority
- **To Do** — Filter: Status = To Do, sorted by Priority then Due Date
- **In Progress** — Filter: Status = In Progress
- **Overdue** — Filter: Overdue = true (these need attention!)
- **By Course** — Table, grouped by Course Name
- **Quick Wins** — Filter: Difficulty = Quick Win AND Status = To Do (grab one when you have 30 minutes)
- **Kanban** — Kanban grouped by Status
- **Completed** — Filter: Status = Completed, sorted by Completed Date descending (your accomplishments!)
- **By Type** — Table, grouped by Type
- **Deferred** — Filter: Status = Deferred (review monthly — still relevant?)
- **Priority Board** — Kanban grouped by Priority
- **Projects** — Filter: Type = Project (larger undertakings)
- **This Week** — Filter: Due Date is this week

---

## NOTE-TAKING FRAMEWORKS

> Choose the framework that best matches each course type. You can mix frameworks within a single course.

### Framework 1: Cornell Method (Adapted for Video)

Best for: Lecture-heavy courses with clear concepts

```
┌─────────────────────┬────────────────────────────────────────────┐
│  CUE COLUMN         │  NOTES (during the lesson)                  │
│  (Key terms,        │                                             │
│   questions,        │  - Main point 1                             │
│   triggers)         │    - Supporting detail                      │
│                     │    - Example given                          │
│  • What is X?       │  - Main point 2                             │
│  • How does Y       │    - How it works                           │
│    relate to Z?     │    - When to use it                         │
│  • KEY: Formula     │  - Main point 3                             │
│                     │    - Common mistakes                        │
│                     │    - Best practices                         │
├─────────────────────┴────────────────────────────────────────────┤
│  SUMMARY (after the lesson — in your own words)                   │
│  This module taught that [main concept]. The key insight is       │
│  [your synthesis]. I can apply this by [specific application].    │
└──────────────────────────────────────────────────────────────────┘
```

### Framework 2: Progressive Summarization

Best for: Dense courses where you'll reference notes later

1. **Layer 1:** Full notes during the lesson (everything useful)
2. **Layer 2:** Bold the most important sentences
3. **Layer 3:** Highlight the key phrases within bolded text
4. **Layer 4:** Write a "Summary (My Words)" in your own language
5. **Layer 5:** Extract Key Takeaways to the Takeaways database

### Framework 3: Question-Based Notes

Best for: Courses preparing you for real-world application

Structure every module's notes around questions:
- **What did I learn?** (facts and concepts)
- **Why does it matter?** (relevance to my goals)
- **How do I use this?** (specific applications)
- **What should I do next?** (action items)
- **What am I still confused about?** (questions for further research)

### Framework 4: Mind Map Style

Best for: Creative courses, big-picture thinking, interconnected topics

- Central concept in the middle
- Branch out to sub-topics
- Connect related ideas across branches
- Use Notion's toggle lists for expandable branches
- Add timestamps and screenshots at each node

---

## REVIEW SYSTEM

> Completing a course is only the beginning. This review system ensures knowledge retention over time.

### Spaced Review Schedule

| Timing | Action |
|---|---|
| End of each module | Write Summary (My Words) and extract Key Takeaways |
| End of each week | Review that week's Key Takeaways, complete Action Items |
| End of course | Write Key Outcomes, Overall Rating, ROI Assessment |
| 1 week after completion | Review all Key Takeaways — are they sticking? |
| 1 month after completion | Check Action Items — how many completed? What's blocked? |
| 3 months after completion | Review Key Takeaways — still relevant? Applied in practice? |

### Monthly Learning Review Questions

1. What courses did I work on this month?
2. What is the single most valuable thing I learned?
3. What did I apply from my learning to real work/life?
4. What am I stuck on or confused about?
5. Is my current course selection aligned with my goals?
6. What should I start, stop, or continue?

---

## AUTOMATIONS / FORMULAS

### Course Progress

Percentage of modules completed.

```
if(
  prop("Total Modules") == 0,
  "0%",
  format(round(prop("Completed Modules") / prop("Total Modules") * 100)) + "%"
)
```

### Action Item Overdue

Flags action items past their due date.

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

### Time Invested per Course

Rollup summing hours from all linked modules.

```
Sum of Time Spent (hrs) from linked Modules
```

### Cost Per Hour of Learning

Value assessment formula (use in views).

```
if(
  prop("Time Invested (hrs)") == 0,
  "—",
  "$" + format(round(prop("Cost") / prop("Time Invested (hrs)") * 100) / 100) + "/hr"
)
```

### Completion Velocity

Average modules per week (for estimating finish date).

```
if(
  or(empty(prop("Start Date")), prop("Completed Modules") == 0),
  "—",
  format(round(prop("Completed Modules") / (dateBetween(now(), prop("Start Date"), "days") / 7) * 100) / 100) + " modules/week"
)
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Current Courses

- Open the **Courses** database and add everything you're currently learning
- Include any courses in progress, recently completed, or on your wishlist
- For in-progress courses: set Total Modules, Start Date, and current Status
- Set Priority based on career/life impact

### Step 2 — Create Module Entries

- For your primary active course, create a Module entry for each section
- You can do this all at once (using the course table of contents) or as you progress
- Set Module Number to maintain order
- Don't fill in notes yet — that happens as you study

### Step 3 — Take Notes as You Learn

- When you sit down to study, open the relevant Module entry
- Take notes in the Notes field using one of the frameworks above
- After completing a module:
  - Fill in Key Concepts, Key Takeaways, and Summary (My Words)
  - Update Status to Completed and Understanding Level
  - Extract any action items to the Action Items database
  - Create Key Takeaway entries for critical insights

### Step 4 — Extract Action Items

- Every time you learn something actionable, create an **Action Item**
- Link it to the Course and Module it came from
- Set Priority and an estimated time to complete
- Be specific — "Try Flexbox on my portfolio site" is better than "Practice CSS"

### Step 5 — Build Your Takeaway Library

- As you complete modules and courses, extract the gold into **Key Takeaways**
- Each entry should be one clear, memorable insight
- Rate by Importance — Critical insights get reviewed regularly
- Over time, this becomes your personal knowledge reference

### Step 6 — Establish Your Learning Rhythm

**During each study session:**
1. Open the current Module entry
2. Set Status to In Progress
3. Take notes while watching/reading
4. When done: write Summary, extract Takeaways, create Action Items
5. Set Status to Completed and rate Understanding Level
6. Log Time Spent

**Weekly (10 minutes):**
- Review this week's Key Takeaways — are they sinking in?
- Check Action Items — complete at least one Quick Win
- Update Course Progress — celebrate the percentage gains
- Plan next week's study sessions

**Monthly (20 minutes):**
- Review all courses — are priorities still right?
- Check abandoned/paused courses — resume or officially drop them?
- Review Key Takeaways from the past month — how many did you apply?
- Assess: Is your learning aligned with your goals?
- Look at your Wishlist — is it time to start something new?

**After completing a course:**
1. Fill in Completion Date, Key Outcomes, and ROI Assessment
2. Rate the course (My Rating) and note Would Recommend
3. Review all Key Takeaways — mark Critical ones for ongoing review
4. Check Action Items — prioritize any "Must Do" items
5. Write a brief review in Notes (helps when friends ask for recommendations)

### Pro Tips

- The Summary (My Words) field is the highest-value note you take — if you can explain a concept in your own words, you understand it. If you can't, you need to rewatch
- Don't take notes on everything — capture what's new to YOU, not what you already know
- Extract Action Items immediately — "I'll come back to this" means "I'll never do this"
- Use the Key Takeaways database as your study-for-life system — review Critical takeaways monthly even after finishing the course
- Timestamps are gold — when you need to reference a specific explanation, you want "32:15 — closure example" not "somewhere in module 4"
- Take screenshots of important diagrams and frameworks — they're faster to review than rewatching the video
- If Understanding Level = Confused, don't move forward. Rewatch, find supplementary resources, or ask in the course community
- Rate ROI honestly — this data helps you choose better courses in the future
- The "Not Yet Applied" view is your learning accountability partner — knowledge you don't use is knowledge you'll lose
- Course notes without Action Items are just passive consumption. Every module should produce at least one "thing I will do" or "thing I now understand differently"
