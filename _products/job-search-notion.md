# Job Search Command Center — Notion Template

> Duplicate this page into your Notion workspace. All databases are pre-linked. Read the Quick-Start Guide before entering real data to get the most out of the system.

---

## DATABASES

---

### 1. Applications Tracker

**Purpose:** The master log of every role you apply to, from first click to final decision.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Role Title | Title | Exact job title from the posting |
| Company | Relation | → Company Research database |
| Company Name | Rollup | From Company relation |
| Date Applied | Date | When you submitted the application |
| Source | Select | LinkedIn / Indeed / Company Site / Referral / Recruiter / Glassdoor / AngelList / Job Board / Cold Outreach |
| Status | Select | Researching / Applied / Application Viewed / Phone Screen / Interview Round 1 / Interview Round 2 / Interview Round 3 / Final Round / Offer / Negotiating / Accepted / Rejected / Withdrew / Ghosted |
| Salary Range (Min) | Number | Minimum of posted or estimated range |
| Salary Range (Max) | Number | Maximum of posted or estimated range |
| Midpoint | Formula | `round((prop("Salary Range (Min)") + prop("Salary Range (Max)")) / 2)` |
| My Target Salary | Number | What you want for this role |
| Above / Below Target | Formula | `if(prop("Midpoint") >= prop("My Target Salary"), "Above Target", if(prop("Midpoint") >= prop("My Target Salary") * 0.9, "Close", "Below Target"))` |
| Location | Text | City, Remote, Hybrid, or specific state/country |
| Work Mode | Select | Remote / Hybrid / On-site |
| Contact Name | Text | Recruiter or hiring manager name |
| Contact Email | Email | |
| Contact LinkedIn | URL | |
| Job Posting URL | URL | Link to original posting (save it — postings disappear) |
| Resume Version | Relation | → Resume Versions database |
| Cover Letter Used | Checkbox | Did you write a custom cover letter? |
| Referral | Text | Name of internal referral, if any |
| Notes | Text | Observations, red flags, interesting details from the posting |
| Next Action | Text | What's the next step you need to take? |
| Next Action Date | Date | When to follow up or prepare |
| Days in Status | Formula | `dateBetween(now(), prop("Date Applied"), "days")` |
| Last Updated | Last Edited Time | Auto-updated by Notion |
| Excitement Level | Select | High / Medium / Low / Applying Out of Obligation |
| Interview Count | Number | How many rounds completed |
| Rejection Reason | Text | If known — useful for patterns |
| Linked Interviews | Relation | → Interview Prep database |

**Views:**

- **All Applications** — Table, sorted by Date Applied descending
- **Active Pipeline** — Filter: Status not in (Rejected, Withdrew, Ghosted, Accepted), sorted by Next Action Date
- **This Week** — Filter: Date Applied is this week
- **By Status** — Kanban, grouped by Status
- **High Excitement** — Filter: Excitement Level = High
- **Need Follow-Up** — Filter: Next Action Date <= today, Status = Applied or Phone Screen
- **Ghosted Tracker** — Filter: Status = Ghosted (for pattern awareness)
- **Salary Range View** — Table, sorted by Midpoint descending

---

### 2. Company Research

**Purpose:** Deep-dive notes on every company worth researching, whether you've applied or not.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Company Name | Title | |
| Industry | Select | Tech / Finance / Healthcare / Media / Retail / Education / Nonprofit / Government / Startup / Agency / Other |
| Company Size | Select | 1-10 / 11-50 / 51-200 / 201-500 / 501-1000 / 1000-5000 / 5000+ |
| Stage | Select | Pre-seed / Seed / Series A / Series B / Series C+ / Public / Bootstrapped / Nonprofit |
| Company Website | URL | |
| Glassdoor URL | URL | |
| LinkedIn URL | URL | |
| Glassdoor Rating | Number | Out of 5 |
| CEO Approval % | Number | Glassdoor CEO approval rating |
| Review Summary | Text | 2-3 sentence summary of Glassdoor themes |
| Tech Stack | Text | Known technologies, tools, or platforms used |
| Products / Services | Text | What they make or do |
| Mission Statement | Text | Their stated mission |
| Culture Notes | Text | What the culture seems like based on research |
| Remote / Hybrid Policy | Text | Known policy or reported in reviews |
| Notable Benefits | Text | Equity, health, 401k match, PTO, etc. |
| Funding / Revenue | Text | Recent funding rounds or public revenue info |
| Recent News | Text | Recent press, product launches, layoffs, expansions |
| Pros | Text | Reasons this could be a great fit |
| Cons | Text | Red flags or concerns |
| Competitors | Text | Key competitors (useful for interview prep) |
| Interview Process Notes | Text | Glassdoor or community reports on their process |
| Overall Score | Select | Strong Interest / Interested / Neutral / Low Interest / Avoid |
| Linked Applications | Relation | → Applications Tracker |
| Linked Contacts | Relation | → Networking Tracker |

**Views:**

- **All Companies** — Table, sorted by Overall Score then Glassdoor Rating
- **Strong Interest** — Filter: Overall Score = Strong Interest
- **To Research** — Filter: Overall Score is empty, sorted by date added
- **By Industry** — Grouped by Industry

---

### 3. Interview Prep

**Purpose:** Prepare systematically for every interview stage.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Interview Name | Title | "[Company] — [Stage]" e.g. "Acme Corp — Round 2 Technical" |
| Application | Relation | → Applications Tracker |
| Company Name | Rollup | From Application |
| Interview Date | Date | Scheduled date and time |
| Interview Type | Select | Phone Screen / Video Call / Technical / Case Study / Behavioral / Panel / On-site / Presentation / Final |
| Interviewer Names | Text | Names and titles of interviewers |
| Interviewer LinkedIn | URL | Research each interviewer beforehand |
| Prep Status | Select | Not Started / In Progress / Ready |
| Questions to Prepare | Text | Specific questions you expect or were told to prepare |
| STAR Stories Planned | Text | Which stories from your experience to use (reference Stories database) |
| Company Research Done | Checkbox | |
| Role Research Done | Checkbox | Thoroughly reviewed job description? |
| Questions to Ask | Text | Your list of thoughtful questions for the interviewer |
| Notes (During/After) | Text | Real-time notes or immediate post-interview thoughts |
| Outcome | Select | Advancing / Rejected / Pending / Withdrew / Offer |
| Post-Interview Reflection | Text | What went well? What was hard? What to improve? |
| Thank You Sent | Checkbox | Sent thank-you email within 24 hours? |
| Thank You Date | Date | |

**Views:**

- **Upcoming Interviews** — Filter: Interview Date >= today, sorted by Interview Date
- **Prep Needed** — Filter: Prep Status = Not Started or In Progress AND Interview Date within 7 days
- **Past Interviews** — Filter: Interview Date < today, sorted descending
- **By Company** — Grouped by Company Name

---

### STAR Story Bank

**Purpose:** Build a reusable library of your best behavioral interview stories.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Story Title | Title | Short name for this story (e.g. "Led team through product launch under deadline") |
| Situation | Text | Context: where, when, what role, what was the challenge |
| Task | Text | What specifically were you responsible for? |
| Action | Text | What did YOU do? Be specific, use "I" not "we" |
| Result | Text | Quantified outcome: numbers, percentages, timeline improvements |
| Skills Demonstrated | Multi-select | Leadership / Communication / Problem-Solving / Conflict Resolution / Data Analysis / Project Management / Creativity / Adaptability / Technical / Collaboration |
| Common Questions This Answers | Text | "Tell me about a time you..." — which prompts fit this story? |
| Strength Level | Select | Core Story / Good Backup / Still Developing |
| Notes | Text | Tweaks to try, feedback received, variations |

**Common Behavioral Questions to Prep:**

- Tell me about a time you had to work with a difficult colleague.
- Describe a situation where you failed. What did you learn?
- Tell me about a time you had to make a decision with incomplete information.
- Describe your most challenging project and how you handled it.
- Tell me about a time you had to influence without authority.
- Give an example of when you went above and beyond your role.
- Tell me about a time you disagreed with your manager.
- Describe a time you had to learn something quickly.
- Tell me about a time you had competing priorities. How did you manage?
- What's your greatest professional accomplishment?

---

### 4. Networking Tracker

**Purpose:** Manage every professional relationship that supports your job search.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Contact Name | Title | Full name |
| Company | Text | Current company |
| Title / Role | Text | Their current role |
| LinkedIn URL | URL | |
| Email | Email | |
| Phone | Phone | |
| How You Know Them | Text | Conference, former colleague, alumni, warm intro, cold outreach |
| Relationship Strength | Select | Strong (close ally) / Warm (know each other) / Cold (loose connection) / New (just met) |
| Target Company Connection | Checkbox | Do they work at or know people at a company you're targeting? |
| Companies They're Connected To | Text | Relevant companies in their network |
| Last Contact Date | Date | When you last spoke or messaged |
| Next Follow-Up Date | Date | When to reach out again |
| Follow-Up Needed | Formula | `if(prop("Next Follow-Up Date") <= now(), "Follow Up Now", if(dateBetween(prop("Next Follow-Up Date"), now(), "days") <= 7, "This Week", "Later")` |
| Contact History | Text | Log of every interaction (date + brief summary) |
| Intro Requested | Checkbox | Have you asked them to make an introduction? |
| Intro To | Text | Who you asked to be introduced to |
| Referral Submitted | Checkbox | Have they submitted a referral for you? |
| Referral Company | Text | Which company |
| Thank-You Sent | Checkbox | Thanked them for their help? |
| Notes | Text | Personal details, interests, good conversation hooks |

**Views:**

- **All Contacts** — Table, sorted by Last Contact Date
- **Follow Up Now** — Filter: Follow-Up Needed = "Follow Up Now"
- **This Week** — Filter: Follow-Up Needed = "This Week"
- **Strong Connections** — Filter: Relationship Strength = Strong
- **Target Company Connections** — Filter: Target Company Connection = true
- **New Connections** — Filter: Relationship Strength = New, sorted by date added

---

### 5. Resume Versions

**Purpose:** Track every version of your resume so you know which one went where.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Version Name | Title | e.g. "Marketing Manager — Startup Focus v3" |
| File Link | URL | Google Drive, Dropbox, or Notion file link |
| Created Date | Date | |
| Target Role Type | Text | What type of role is this version optimized for? |
| Key Changes from Previous | Text | What did you adjust and why? |
| ATS Optimized | Checkbox | Did you optimize for ATS keyword matching? |
| Keywords Targeted | Text | Key skills and terms included |
| Used For | Relation | → Applications Tracker |
| Times Used | Rollup | Count of linked applications |
| Notes | Text | Feedback received, things to improve |

---

## OFFER EVALUATION MATRIX

Use this when comparing multiple offers or evaluating a single offer against your priorities.

```
OFFER EVALUATION WORKSHEET

Company A vs. Company B vs. My Current Situation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPENSATION
                        Company A    Company B    Current
Base Salary             $________    $________    $________
Signing Bonus           $________    $________    —
Annual Bonus (target)   $________    $________    $________
Equity (est. value)     $________    $________    $________
Total Comp (Year 1)     $________    $________    $________
Total Comp (Year 2+)    $________    $________    $________

BENEFITS
                        Company A    Company B    Current
Health Insurance        ________     ________     ________
Dental / Vision         ________     ________     ________
401k Match              ________     ________     ________
PTO Days                ________     ________     ________
Parental Leave          ________     ________     ________
Remote / Hybrid         ________     ________     ________
Learning Budget         ________     ________     ________

ROLE & GROWTH (Rate 1-10)
                        Company A    Company B    Current
Role Excitement         ___          ___          ___
Growth Potential        ___          ___          ___
Manager Quality         ___          ___          ___
Team Quality            ___          ___          ___
Company Stability       ___          ___          ___
Mission Alignment       ___          ___          ___
Work-Life Balance       ___          ___          ___

TOTAL SCORE             ___          ___          ___

DECISION NOTES:
_______________________________________________
_______________________________________________

NEGOTIATION PLAN (if applicable):
- Ask for: ____________________________________
- Walk away if: _______________________________
- Deadline for decision: ______________________
```

---

## SALARY COMPARISON TABLE

Track offers, market data, and targets in one view.

| Role | Company | Base | Bonus | Equity | Total | Location | Remote | Source | Notes |
|---|---|---|---|---|---|---|---|---|---|
| [Role] | [Co] | $_ | $_ | $_ | $_ | NYC | Hybrid | Offer | |
| [Role] | [Co] | $_ | $_ | $_ | $_ | Remote | Remote | Levels.fyi | |
| [Role] | [Co] | $_ | $_ | $_ | $_ | SF | On-site | Glassdoor | |
| My Target | — | $_ | $_ | — | $_ | — | Remote | Personal | |

**Compensation Research Resources:**

- Levels.fyi — tech roles
- Glassdoor Salary — broad industry data
- Payscale — by experience level
- LinkedIn Salary — role and location specific
- Blind (app) — tech industry peer data
- Salary.com — comprehensive database
- Your network — ask people you trust directly

---

## WEEKLY JOB SEARCH GOALS & REFLECTION

Copy and use each week:

```
## Job Search Week of [Date]

### GOALS THIS WEEK
- [ ] Applications to submit: ___ (target: ___)
- [ ] Networking outreach: ___ people
- [ ] Follow-ups to send: ___ (list below)
- [ ] Interview prep sessions: ___
- [ ] Company research: ___ companies
- [ ] Other: ___________________________

### APPLICATIONS THIS WEEK
| Company | Role | Status |
|---------|------|--------|
|         |      |        |
|         |      |        |
|         |      |        |

### FOLLOW-UPS TO SEND
- [ ] [Company] — [Contact] — [Last contact date]
- [ ] [Company] — [Contact] — [Last contact date]
- [ ] [Company] — [Contact] — [Last contact date]

### NETWORKING OUTREACH
- [ ] [Name] — [Message goal]
- [ ] [Name] — [Message goal]

### INTERVIEWS SCHEDULED
- [Company] — [Stage] — [Date/Time]

### END-OF-WEEK REFLECTION
- Applications sent: ___
- Response rate this week: ___
- What's working:
- What's not working:
- Mindset / energy level (honest check-in):
- Next week's priority:
```

---

## DASHBOARD

```
┌─────────────────────────────────────────────────────────┐
│  JOB SEARCH COMMAND CENTER                April 2024    │
├──────────────┬──────────────┬──────────────┬────────────┤
│  Applied     │  Active      │  Interviews  │  Offers    │
│  (Total)     │  Pipeline    │  Scheduled   │            │
│    47        │     8        │     2        │    1       │
├──────────────┴──────────────┴──────────────┴────────────┤
│  ACTIVE PIPELINE                                         │
│  [Linked view → Applications, filter: Active]           │
├─────────────────────────────────────────────────────────┤
│  UPCOMING INTERVIEWS                                     │
│  [Linked view → Interview Prep, filter: Future]         │
├─────────────────────────────────────────────────────────┤
│  FOLLOW-UP DUE                                          │
│  [Linked view → Applications, filter: Next Action ≤ Now]│
├─────────────────────────────────────────────────────────┤
│  NETWORKING: FOLLOW UP NOW                              │
│  [Linked view → Networking, filter: Follow Up Now]      │
├─────────────────────────────────────────────────────────┤
│  APPLICATIONS BY STATUS (Chart)                         │
│  [Chart view → Applications, group by Status]           │
├─────────────────────────────────────────────────────────┤
│  SALARY COMPARISON                                      │
│  [Linked view → Salary Table, sort: Midpoint desc]      │
└─────────────────────────────────────────────────────────┘
```

**Key Metrics to Watch:**

- **Application-to-Response Rate:** (Responses / Total Applied) × 100
- **Phone Screen-to-Interview Rate:** (Interviews / Phone Screens) × 100
- **Interview-to-Offer Rate:** (Offers / Final Round Interviews) × 100
- **Average Days from Apply to Response:** Track this — if it's >30 days, follow up or move on

---

## QUICK-START GUIDE

### Step 1 — Establish Your Target
Before entering any applications, use the template's blank area to write:

- The role type(s) you're targeting
- Your non-negotiable location and remote requirements
- Your minimum acceptable salary
- The 5 companies you most want to work for
- Your realistic timeline (by when do you need a job?)

Having clarity here makes every other decision in the search faster.

### Step 2 — Populate Company Research First
- Add your target companies to the **Company Research** database before applying
- Research Glassdoor, LinkedIn, recent news, and the tech stack
- Assign an Overall Score — this prevents you from wasting energy on low-interest applications

### Step 3 — Add Applications as You Submit
- Every time you click "Apply," immediately create a record in the **Applications Tracker**
- Paste the job posting URL while you have it — postings get taken down quickly
- Note the Resume Version used and whether a cover letter was submitted

### Step 4 — Build Your STAR Story Bank
- Before interviews start, spend one session populating your **STAR Story Bank**
- Aim for 8-10 strong stories that cover the most common behavioral categories
- Practice each story out loud until you can tell it naturally in 2 minutes

### Step 5 — Use the Pipeline View Daily
- Open the Kanban view each morning for a 5-minute review
- Move applications forward when status changes
- Check the "Follow-Up Due" view and send any pending follow-ups
- Check the Networking view for anyone due for outreach

### Step 6 — Prep for Every Interview
- Open **Interview Prep** and create a new entry the moment an interview is scheduled
- Complete: company research, role research, questions to ask, and STAR stories planned
- Never go into an interview without at least reviewing the interviewer's LinkedIn

### Step 7 — Reflect Weekly
- Fill in the **Weekly Goals & Reflection** template every Monday and Friday
- Job searching is a numbers game and a momentum game — weekly reflection keeps both on track

### Pro Tips
- Save job posting URLs immediately — postings disappear the moment a role closes
- Use the Excitement Level property to stay honest with yourself about what you actually want, not just what you'll settle for
- Log every networking interaction in Contact History — you'll be glad you did when you reconnect in 6 months
- The Offer Evaluation Matrix is most useful when you've already filled it in before an offer arrives — knowing your priorities ahead of time removes emotion from the decision
- Track rejection reasons if you receive them — patterns reveal what to fix in your materials or targeting
- Use the "Ghosted" status and don't take it personally — it's industry-wide behavior, not a reflection of your candidacy
