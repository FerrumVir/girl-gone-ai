# Interview Prep System — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with STAR method frameworks, company research templates, question banks, and performance tracking already configured. Read the Quick-Start Guide at the bottom before your next interview.

---

## DATABASES

---

### 1. Job Applications

**Purpose:** Master tracker for every job you've applied to or are considering. Tracks the full pipeline from discovery through offer (or rejection), with interview stages, contacts, and notes at each step. Your job search command center.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Company — Role | Title | Format: "Company Name — Job Title" e.g. "Stripe — Senior PM" |
| Company | Text | Company name (for grouping) |
| Role Title | Text | Exact job title |
| Department | Text | Which team or department |
| Location | Text | City or "Remote" or "Hybrid — SF" |
| Salary Range | Text | Posted or researched range |
| Job Posting URL | URL | Link to the listing |
| Job Description | Files & Media | Save a PDF in case listing is removed |
| Source | Select | LinkedIn / Indeed / Company Site / Referral / Recruiter Outreach / AngelList / Glassdoor / Networking / Job Fair / Other |
| Referred By | Text | Name of person who referred you |
| Status | Select | Researching / Applied / Phone Screen / Technical Interview / Onsite / Final Round / Offer / Accepted / Rejected / Withdrew / Ghosted |
| Priority | Select | Dream Job / Strong Interest / Moderate Interest / Backup / Practice |
| Date Applied | Date | When you submitted your application |
| Days in Process | Formula | `if(empty(prop("Date Applied")), "—", format(dateBetween(now(), prop("Date Applied"), "days")) + " days")` |
| Application Method | Select | Online Portal / Email / Referral / Recruiter / Direct Message / Career Fair |
| Resume Version | Text | Which resume version you sent |
| Cover Letter | Checkbox | Did you submit a cover letter? |
| Cover Letter File | Files & Media | Copy of the cover letter sent |
| Recruiter Name | Text | HR/recruiter contact |
| Recruiter Email | Email | |
| Recruiter Phone | Phone | |
| Hiring Manager | Text | Direct supervisor for this role |
| Hiring Manager LinkedIn | URL | For research before interviews |
| Team Size | Text | How big is the team you'd join |
| Interview Round | Number | Current round (1, 2, 3, etc.) |
| Total Rounds Expected | Number | How many rounds they typically do |
| Next Interview Date | Date | Your next scheduled interview |
| Next Interview Type | Select | Phone Screen / Video / Technical / Behavioral / Case Study / Panel / Presentation / Onsite / Coffee Chat / Final |
| Next Interview With | Text | Who you're meeting next |
| Preparation Status | Select | Not Started / In Progress / Ready / Confident |
| Offer Amount | Number (USD) | Base salary offered |
| Offer Details | Text | Full comp details — equity, bonus, benefits, PTO |
| Offer Deadline | Date | When you need to respond |
| Decision Notes | Text | Pros and cons for decision-making |
| Why Interested | Text | What excites you about this role/company |
| Why Qualified | Text | Your unique fit — skills, experience, results |
| Potential Concerns | Text | Red flags or hesitations |
| Rejection Reason | Text | If rejected — why (if known) |
| Follow-Up Sent | Checkbox | Did you send a thank-you/follow-up? |
| Last Communication | Date | Most recent contact with this company |
| Company Research | Relation | → Company Research database |
| Linked Interviews | Relation | → Interviews database |
| Linked STAR Stories | Relation | → STAR Stories database |
| Tags | Multi-select | FAANG / Startup / Remote / Relocation / Negotiable / Equity Heavy / Urgent / Dream Role |
| Notes | Text | General application notes, timeline, gut feeling |

**Views:**

- **All Applications** — Table, sorted by Date Applied descending
- **Pipeline Board** — Kanban grouped by Status (main working view)
- **Active** — Filter: Status is Phone Screen through Final Round, sorted by Next Interview Date
- **Upcoming Interviews** — Filter: Next Interview Date is within 14 days, sorted ascending
- **Needs Prep** — Filter: Preparation Status = Not Started or In Progress AND Next Interview Date within 7 days
- **Offers** — Filter: Status = Offer
- **By Priority** — Table, grouped by Priority
- **By Source** — Table, grouped by Source (track what channels work)
- **Stale** — Filter: Last Communication > 14 days ago AND Status is active (follow up!)
- **Rejected/Ghosted** — Filter: Status = Rejected or Ghosted (for pattern analysis)
- **Dream Jobs** — Filter: Priority = Dream Job or Strong Interest
- **Calendar** — Calendar view by Next Interview Date

---

### 2. Company Research

**Purpose:** Deep research notes on each company you're interviewing with. Mission, culture, recent news, products, competitors, financials, and team structure. Being thoroughly researched is the single biggest differentiator in interviews.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Company Name | Title | Company name |
| Website | URL | Main website |
| Careers Page | URL | Their careers/jobs page |
| LinkedIn | URL | Company LinkedIn page |
| Glassdoor | URL | Glassdoor page (reviews, salary data) |
| Industry | Select | Tech / Finance / Healthcare / E-commerce / SaaS / Media / Education / Consulting / Retail / Manufacturing / Non-profit / Government / Startup / Other |
| Company Size | Select | 1–10 / 11–50 / 51–200 / 201–1000 / 1001–5000 / 5000+ / Public |
| Founded | Number | Year founded |
| Headquarters | Text | HQ location |
| Funding Stage | Select | Pre-Seed / Seed / Series A / Series B / Series C+ / Public / Bootstrapped / Private Equity |
| Last Funding | Text | Most recent round details |
| Revenue/ARR | Text | If known (public info) |
| Stock Ticker | Text | If public |
| Mission Statement | Text | Their stated mission/vision |
| Core Values | Text | Published company values |
| Culture Notes | Text | What's the vibe? Glassdoor themes, employee posts, interview experience |
| Products/Services | Text | What they sell/build |
| Key Customers | Text | Notable clients or use cases |
| Competitors | Text | Main competitors in their space |
| Competitive Advantage | Text | What makes them different/better |
| Recent News | Text | Last 3–6 months of relevant news, launches, acquisitions |
| Challenges/Risks | Text | Known challenges, market risks, concerns from research |
| Tech Stack | Text | If relevant — engineering tools and platforms |
| Team Structure | Text | How the team you'd join is organized |
| Leadership | Text | CEO, CTO, VP of your department — names and backgrounds |
| Interview Process | Text | What their typical interview process looks like (from Glassdoor, blog posts) |
| Glassdoor Rating | Number | Out of 5 |
| Interview Difficulty | Select | Easy / Average / Hard / Very Hard |
| Common Interview Topics | Text | Themes that come up in their interviews based on research |
| Questions to Ask Them | Text | Your prepared questions showing research depth |
| Why I Want to Work Here | Text | Your genuine, researched answer to "Why us?" |
| Concerns | Text | Red flags or areas to probe during interviews |
| Salary Research | Text | Levels.fyi, Glassdoor, Blind data points |
| Benefits Notes | Text | PTO, health, 401k, perks research |
| Remote Policy | Text | WFH, hybrid, in-office requirements |
| Linked Applications | Relation | → Job Applications database |
| Last Updated | Date | When you last refreshed this research |
| Research Depth | Select | Surface / Moderate / Deep / Expert |
| Notes | Text | Additional intelligence, insider info, network insights |

**Views:**

- **All Companies** — Table, sorted by Company Name
- **Active (Interviewing)** — Filter: linked Applications have active status
- **By Industry** — Table, grouped by Industry
- **Research Depth** — Table, sorted by Research Depth ascending (identify gaps)
- **Recently Updated** — Table, sorted by Last Updated descending
- **Needs Research** — Filter: Research Depth = Surface AND linked to active applications

---

### 3. STAR Stories

**Purpose:** Your library of pre-crafted behavioral interview answers using the STAR method (Situation, Task, Action, Result). Each story maps to common interview competencies so you can pull the right example for any behavioral question.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Story Title | Title | Short, memorable title — e.g. "Saved $2M by Restructuring Vendor Contracts" |
| Competency | Multi-select | Leadership / Teamwork / Problem Solving / Communication / Conflict Resolution / Initiative / Adaptability / Time Management / Decision Making / Customer Focus / Innovation / Failure/Learning / Influence / Data-Driven / Technical Challenge / Cross-Functional / Under Pressure / Ambiguity |
| Situation | Text | Context and background — what was happening? Where? When? |
| Task | Text | What was your specific responsibility or challenge? |
| Action | Text | What did YOU specifically do? (Be detailed — this is the meat) |
| Result | Text | Quantifiable outcome — numbers, percentages, revenue, time saved |
| Impact Statement | Text | One-sentence summary of the result for punchy delivery |
| Company Where It Happened | Text | Which employer or project |
| Role at the Time | Text | Your title when this happened |
| Timeframe | Text | When this occurred — e.g. "Q3 2024" |
| Strength of Story | Select | Killer (use for dream jobs) / Strong / Decent / Weak (need to improve) |
| Times Used | Number | How often you've told this in interviews |
| Audience Reaction | Select | Impressed / Engaged / Neutral / Confused / Not Relevant |
| Duration (mins) | Number | How long this story takes to tell (target: 2–3 minutes) |
| Follow-Up Questions Received | Text | What interviewers typically ask after this story |
| Prepared Follow-Up Answers | Text | Your answers to common follow-ups |
| Alternative Framing | Text | How to angle this story differently for different competencies |
| Lessons Learned | Text | What you'd do differently — shows self-awareness |
| Common Questions This Answers | Text | List interview questions this story works for |
| Linked Applications | Relation | → Job Applications database (which interviews you've used this in) |
| Practice Recording | Files & Media | Video/audio of yourself telling this story |
| Last Practiced | Date | When you last rehearsed |
| Tags | Multi-select | Technical / People / Process / Strategy / Crisis / Growth / Metrics Heavy / Short Version Available |
| Notes | Text | Delivery tips, transitions, what to emphasize for different companies |

**Views:**

- **All Stories** — Table, sorted by Story Title
- **By Competency** — Table, grouped by Competency (find the right story fast during prep)
- **Strongest Stories** — Filter: Strength = Killer or Strong
- **Needs Work** — Filter: Strength = Weak (improve before using)
- **Most Used** — Table, sorted by Times Used descending
- **Recently Practiced** — Table, sorted by Last Practiced descending
- **Short Stories (< 2 min)** — Filter: Duration <= 2
- **By Company/Role** — Table, grouped by Company Where It Happened
- **Unpracticed** — Filter: Last Practiced is empty or > 30 days ago

---

### 4. Interview Questions Bank

**Purpose:** Comprehensive library of interview questions organized by category, with your prepared answers and key talking points. Includes 200+ common questions across behavioral, technical, situational, and company-specific categories.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Question | Title | The full interview question |
| Category | Select | Behavioral / Technical / Situational / Brain Teaser / Case Study / Culture Fit / Motivation / Salary/Negotiation / Role-Specific / Weakness / Strength / Why This Company / Career Goals / Management / Leadership |
| Subcategory | Select | Tell Me About Yourself / Conflict / Failure / Leadership / Teamwork / Challenge / Achievement / Problem Solving / Communication / Decision Making / Prioritization / Growth / Values / Technical Deep Dive |
| Difficulty | Select | Easy / Medium / Hard / Curveball |
| Frequency | Select | Very Common / Common / Occasional / Rare |
| My Answer | Text | Your prepared response (key points, not a script) |
| STAR Story to Use | Relation | → STAR Stories database |
| Key Points | Text | Bullet points to hit in your answer |
| What They're Really Asking | Text | The underlying competency being evaluated |
| Common Mistakes | Text | What NOT to do when answering this |
| Good Answer Framework | Text | Structure for a strong answer |
| Practice Notes | Text | Notes from practicing this question |
| Confidence Level | Select | Nailed It / Good / Needs Work / Dreading This / Haven't Practiced |
| Times Encountered | Number | How many times you've been asked this in real interviews |
| Companies That Asked | Text | Which companies asked this (spot patterns) |
| Last Practiced | Date | When you last rehearsed this answer |
| Video Practice | Files & Media | Recording of your answer |
| Tags | Multi-select | Must Prepare / Tricky / Requires Examples / Technical / Numbers Heavy / Personal / Philosophical / Rapid Fire |
| Notes | Text | Additional tips, variations, follow-up questions they might ask |

**Views:**

- **All Questions** — Table, sorted by Category then Frequency
- **By Category** — Table, grouped by Category
- **Most Common** — Filter: Frequency = Very Common or Common (prep these first!)
- **Needs Practice** — Filter: Confidence Level = Needs Work or Dreading This or Haven't Practiced
- **Behavioral Questions** — Filter: Category = Behavioral, grouped by Subcategory
- **Technical Questions** — Filter: Category = Technical
- **The Essentials (Top 20)** — Filter: Frequency = Very Common AND Tags contains Must Prepare
- **Hard/Curveball** — Filter: Difficulty = Hard or Curveball
- **Confidence Board** — Kanban grouped by Confidence Level
- **Recently Practiced** — Filter: Last Practiced within 7 days
- **Unprepared** — Filter: My Answer is empty (still need to write your response)
- **Role-Specific** — Filter: Category = Role-Specific

---

### 5. Interviews (Session Log)

**Purpose:** Detailed record of every interview you complete. Pre-interview prep, real-time notes, post-interview reflection, and performance analysis. Builds your pattern recognition for what works and what doesn't across multiple interview processes.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Interview Title | Title | "Company — Round X — Type" e.g. "Stripe — R2 — Technical" |
| Application | Relation | → Job Applications database |
| Company | Rollup | From Application relation |
| Role | Rollup | From Application relation |
| Date & Time | Date | Interview date and time |
| Duration (mins) | Number | How long it lasted |
| Type | Select | Phone Screen / Video / Technical / Behavioral / Case Study / Panel / Presentation / Onsite / Coffee Chat / Final / Recruiter / Hiring Manager |
| Round | Number | Which round (1, 2, 3, etc.) |
| Interviewer Name | Text | Who interviewed you |
| Interviewer Title | Text | Their role at the company |
| Interviewer LinkedIn | URL | For post-interview follow-up |
| Platform | Select | Zoom / Google Meet / Teams / Phone / In-Person / CoderPad / HackerRank / Other |
| Prep Completed | Checkbox | Did you finish your prep checklist? |
| Prep Notes | Text | Key points to remember, talking points, questions to ask |
| Questions Asked by Them | Text | Actual questions they asked (log immediately after!) |
| My Answers Summary | Text | Brief notes on how you answered each question |
| STAR Stories Used | Relation | → STAR Stories database |
| Questions I Asked | Text | Questions you asked them and their responses |
| Their Concerns | Text | Any objections or concerns they raised |
| How I Addressed Concerns | Text | What you said to handle their hesitations |
| Technical Topics Covered | Text | Specific technical areas discussed |
| Code Challenge | Text | If applicable — what was the problem? |
| My Performance Rating | Select | Crushed It / Strong / Average / Weak / Bombed |
| What Went Well | Text | Specific moments that landed |
| What Went Poorly | Text | Specific mistakes or missed opportunities |
| What I'd Do Differently | Text | If you could redo it |
| Interviewer Vibe | Select | Enthusiastic / Friendly / Neutral / Tough / Cold / Hostile |
| Cultural Signals | Text | What you learned about the company culture from this person |
| Red Flags | Text | Any concerns raised by this interview |
| Green Flags | Text | Positive signals about the role/company |
| Thank-You Sent | Checkbox | Did you send a follow-up email? |
| Thank-You Date | Date | When you sent it |
| Outcome | Select | Advanced / Rejected / Pending / Offer / Ghosted |
| Outcome Date | Date | When you heard back |
| Feedback Received | Text | Any feedback from recruiter or interviewer |
| Next Steps | Text | What was communicated as next steps |
| Energy Level Before | Select | Energized / Calm / Nervous / Anxious / Exhausted |
| Energy Level After | Select | Energized / Relieved / Neutral / Drained / Defeated |
| Tags | Multi-select | Strong Performance / Learned a Lot / Tough Questions / Great Connection / Red Flags / Need Follow-Up |
| Notes | Text | Any additional reflections |

**Views:**

- **All Interviews** — Table, sorted by Date descending
- **Upcoming** — Filter: Date > today, sorted by Date ascending (prep view!)
- **This Week** — Filter: Date is this week
- **By Company** — Table, grouped by Company
- **Performance Review** — Table showing Company, Type, My Performance Rating, What Went Well, What I'd Do Differently
- **Strong Performances** — Filter: Performance Rating = Crushed It or Strong (confidence boost!)
- **Needs Thank-You** — Filter: Thank-You Sent = false AND Date < today (send within 24h!)
- **Pending Outcomes** — Filter: Outcome = Pending
- **Rejected** — Filter: Outcome = Rejected (analyze patterns)
- **By Type** — Table, grouped by Type (are you weak at a specific interview format?)
- **Recent** — Filter: Date within last 30 days

---

## COMMON INTERVIEW QUESTIONS (Pre-Loaded)

> These 200+ questions come pre-loaded in the Question Bank. Organize by category and start preparing your answers for the "Very Common" ones first.

### Behavioral — Tell Me About a Time When...

1. You had to deal with a difficult coworker or team member
2. You failed at something and how you handled it
3. You had to meet a tight deadline with competing priorities
4. You disagreed with your manager's decision
5. You took initiative beyond your job description
6. You had to persuade someone to see things your way
7. You received critical feedback and what you did with it
8. You made a mistake that impacted the team
9. You had to make a decision without complete information
10. You led a project from start to finish
11. You dealt with ambiguity or rapidly changing priorities
12. You had to manage conflicting stakeholder needs
13. You identified and solved a problem before anyone asked
14. You had to deliver bad news to a client or stakeholder
15. You worked with a team that was underperforming
16. You had to learn something new quickly under pressure
17. You improved a process or system
18. You went above and beyond for a customer or colleague
19. You had to say no to a request from leadership
20. You managed multiple projects simultaneously

### Motivation & Culture

21. Why do you want to work here?
22. What interests you about this role specifically?
23. Where do you see yourself in 5 years?
24. What's your ideal work environment?
25. What motivates you to do your best work?
26. Tell me about yourself (the #1 most important answer to nail)
27. Why are you leaving your current role?
28. What's your management style?
29. How do you handle stress and pressure?
30. What are you looking for in your next role?

### Strengths & Weaknesses

31. What's your greatest strength?
32. What's your biggest weakness?
33. What would your current manager say about you?
34. What's the most difficult piece of feedback you've received?
35. What's your superpower that sets you apart?

### Situational / Hypothetical

36. How would you handle [specific scenario relevant to role]?
37. If you joined and discovered the team was demoralized, what would you do?
38. How would you approach your first 90 days in this role?
39. If you had to choose between meeting a deadline with imperfect work or delaying for quality, what would you do?
40. How would you handle a disagreement with a senior colleague in a meeting?

---

## STAR METHOD FRAMEWORK

> Use this structure for every behavioral answer. Practice until it becomes second nature.

### The Framework

| Component | What to Include | Time Allocation |
|---|---|---|
| **S**ituation | Context, setting, who was involved, what was at stake | 15–20% (20–30 seconds) |
| **T**ask | Your specific responsibility, what you needed to accomplish | 10–15% (10–20 seconds) |
| **A**ction | What YOU specifically did — detailed, step-by-step | 50–60% (60–90 seconds) |
| **R**esult | Quantifiable outcome — numbers, impact, what you learned | 15–20% (20–30 seconds) |

### STAR Story Template

```
SITUATION: "When I was [role] at [company], [describe the context].
The situation was [what made it challenging/important]."

TASK: "My responsibility was to [specific deliverable or goal].
The deadline was [timeframe] and the stakes were [what was on the line]."

ACTION: "Here's what I did:
1. First, I [initial assessment or planning step]
2. Then, I [key action #1 with detail]
3. I also [key action #2 with detail]
4. When [obstacle] came up, I [how you adapted]"

RESULT: "As a result, [quantifiable outcome].
This represented [impact: % improvement, $ saved, time saved, people helped].
The key lesson I took from this was [learning/growth]."
```

### Tips for Strong STAR Answers

- Always quantify results (even estimates: "approximately 30% improvement")
- Use "I" not "we" — they want YOUR contribution
- Keep it to 2–3 minutes maximum
- Have a short version (90 seconds) and detailed version (3 minutes) of each story
- End with what you learned — shows self-awareness
- Practice out loud, not just in your head

---

## AUTOMATIONS / FORMULAS

### Days in Process

How long since you applied (tracks slow processes).

```
if(
  empty(prop("Date Applied")),
  "—",
  format(dateBetween(now(), prop("Date Applied"), "days")) + " days"
)
```

### Stale Application Detection

Flags applications with no communication in 2+ weeks.

```
if(
  and(
    not(empty(prop("Last Communication"))),
    dateBetween(now(), prop("Last Communication"), "days") > 14,
    prop("Status") != "Rejected",
    prop("Status") != "Withdrew",
    prop("Status") != "Accepted",
    prop("Status") != "Ghosted"
  ),
  true,
  false
)
```

### Interview Countdown

Days until next scheduled interview.

```
if(
  empty(prop("Next Interview Date")),
  "Not scheduled",
  if(
    dateBetween(prop("Next Interview Date"), now(), "days") == 0,
    "TODAY",
    format(dateBetween(prop("Next Interview Date"), now(), "days")) + " days"
  )
)
```

### Offer Deadline Countdown

Urgency indicator for pending offers.

```
if(
  empty(prop("Offer Deadline")),
  "No deadline",
  if(
    dateBetween(prop("Offer Deadline"), now(), "days") <= 0,
    "EXPIRED",
    format(dateBetween(prop("Offer Deadline"), now(), "days")) + " days to decide"
  )
)
```

### Application Success Rate

Track across all applications (use in a summary view):

- Total Applied
- Total Advanced Past Screen
- Total Offers
- Conversion Rate = Offers / Applied

---

## QUICK-START GUIDE

### Step 1 — Build Your STAR Story Library

- Open **STAR Stories** and write 8–12 stories from your career
- Cover these competencies at minimum: Leadership, Problem Solving, Teamwork, Failure/Learning, Conflict, Initiative, Communication, Adaptability
- For each, fill in all four STAR components with specific details and quantified results
- Rate each story's strength honestly — you'll improve the weak ones through practice

### Step 2 — Prepare Core Questions

- Open **Interview Questions Bank** (200+ questions are pre-loaded)
- Start with the "Most Common" view — prepare answers for the top 20 questions
- For each, write your Key Points and link the STAR Story you'd use
- Focus on: "Tell me about yourself," "Why this company," "Greatest weakness," and "Tell me about a time you failed"

### Step 3 — Add Your Active Applications

- Open **Job Applications** and add every active application
- Set Status, Priority, and Next Interview Date for each
- Link to Company Research (create entries for companies you're actively interviewing with)
- This gives you an immediate view of your pipeline

### Step 4 — Deep-Dive Company Research

- For every company where you have an interview scheduled, create a **Company Research** entry
- Spend 30–60 minutes per company: mission, products, recent news, Glassdoor, leadership, culture
- Write your "Why I Want to Work Here" answer based on genuine research
- Prepare 3–5 questions to ask them that demonstrate research depth

### Step 5 — Pre-Interview Prep Routine

**48 hours before each interview:**
1. Review Company Research — any new news in the last week?
2. Re-read the job description — highlight keywords to weave into answers
3. Select 4–5 STAR Stories most relevant to this role/company
4. Practice "Tell me about yourself" out loud (90-second version)
5. Review your Questions to Ask Them
6. Check interviewer's LinkedIn (if known)

**Day of interview:**
1. Review your prep notes (15 minutes, not more)
2. Have your STAR Stories page open during video interviews (reference, don't read)
3. Have your Questions to Ask Them ready
4. Test tech 30 minutes before (camera, mic, internet, lighting)

### Step 6 — Post-Interview Ritual

**Immediately after (within 30 minutes):**
1. Open **Interviews** and log the session while it's fresh
2. Write down every question they asked (you'll forget by tomorrow)
3. Note what went well and what went poorly
4. Record any concerns or red flags
5. Note questions they asked that you weren't prepared for — add these to your Question Bank

**Within 24 hours:**
1. Send a personalized thank-you email to each interviewer
2. Reference something specific from your conversation
3. Address any concerns they raised (if you think of a better answer)
4. Update your Application status and Next Steps

**Weekly job search review (30 minutes):**

- Check Pipeline Board — where does each application stand?
- Follow up on any "Stale" applications (no communication in 14+ days)
- Practice 3–5 questions you're weakest on
- Rehearse your top STAR Stories out loud (keep them sharp)
- Update any Company Research that's gotten stale

### Pro Tips

- "Tell me about yourself" is not your life story — it's a 90-second pitch connecting your past, present, and future to THIS role
- The STAR method's power is in the Action section — spend 60% of your time on specific actions YOU took, not the team
- Always have questions prepared for them — "no questions" signals disinterest. Ask about challenges, team dynamics, or what success looks like in 6 months
- Send thank-you emails within 24 hours — later than that and the impact drops significantly
- Track which STAR Stories get the best reactions and which fall flat — refine based on real data
- Record yourself answering questions on video — you'll spot filler words, rambling, and lack of structure immediately
- If you get rejected, always ask for feedback. Log it in the Feedback Received field. Patterns will emerge.
- Practice your weakest questions with a friend or in front of a mirror — discomfort in practice means comfort in the real thing
- The "Why are you leaving?" question has one rule: never speak negatively about your current employer. Frame it as running toward something, not away from something
- Negotiate every offer. The prepared data in your Company Research (salary ranges, levels.fyi data) gives you confidence to ask
