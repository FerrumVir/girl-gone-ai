# Remote Team Meeting System — Notion Template

> Duplicate this page into your Notion workspace and share it with your team. All databases are pre-linked and templates are pre-built. Follow the Quick-Start Guide at the bottom to get your team running structured meetings within a day.

---

## DATABASES

---

### 1. Meetings

**Purpose:** The master record for every meeting your team runs — with pre-built agenda templates, notes, and links to action items and decisions generated.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Meeting Title | Title | Clear name — e.g. "Standup — April 9" or "1:1 — Sarah & Mike — April 9" |
| Meeting Type | Select | Standup / 1:1 / Retrospective / All-Hands / Sprint Planning / Design Review / Team Sync / Leadership / Ad Hoc / Custom |
| Date | Date | Meeting date and time |
| Duration (min) | Number | Planned meeting length in minutes |
| Actual Duration (min) | Number | How long the meeting actually ran (fill in after) |
| Efficiency | Formula | `if(and(prop("Actual Duration (min)") > 0, prop("Duration (min)") > 0), if(prop("Actual Duration (min)") <= prop("Duration (min)"), "On Time", "Ran Over"), "")` |
| Status | Select | Scheduled / In Progress / Completed / Cancelled / Rescheduled |
| Facilitator | Person | Who is running this meeting |
| Attendees | Person | All participants (use Notion's People property for tagging) |
| Attendee List | Text | Fallback: list attendees as text if not using People property |
| Team | Select | Engineering / Product / Design / Marketing / Sales / Operations / Leadership / All Company / Cross-functional / Custom |
| Recurring | Checkbox | Is this a recurring meeting? |
| Recurrence | Select | Daily / Weekly / Bi-weekly / Monthly / Quarterly |
| Location | Select | Zoom / Google Meet / Microsoft Teams / Slack Huddle / In-Person / Hybrid / Async |
| Meeting Link | URL | Video call link |
| Agenda | Text | Pre-meeting agenda items (filled in before the meeting) |
| Notes | Text | Meeting notes (filled in during or immediately after) |
| Key Takeaways | Text | 2-3 sentence summary of what matters from this meeting |
| Action Item Count | Rollup | Count of linked Action Items |
| Open Action Items | Rollup | Count of linked Action Items where Status is not Complete |
| Decision Count | Rollup | Count of linked Decisions |
| Previous Meeting | Relation | -> Meetings database (self-referential — link to last meeting of this type) |
| Follow-Up Meeting | Relation | -> Meetings database (link to next meeting of this type) |
| Linked Action Items | Relation | -> Action Items database |
| Linked Decisions | Relation | -> Decisions database |
| Rating | Select | 5 - Very Productive / 4 - Productive / 3 - Average / 2 - Could Skip / 1 - Waste of Time |
| Tags | Multi-select | Important / Follow-Up Needed / Urgent / Routine / Strategic |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Week | Formula | `formatDate(prop("Date"), "W")` |

**Views:**

- **All Meetings** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week, sorted by Date ascending
- **Upcoming** — Filter: Status = Scheduled, sorted by Date ascending
- **By Type** — Table, grouped by Meeting Type
- **By Team** — Table, grouped by Team
- **Meeting Board** — Kanban, grouped by Status
- **Standup Archive** — Filter: Meeting Type = Standup, sorted by Date descending
- **1:1 Archive** — Filter: Meeting Type = 1:1, sorted by Date descending
- **Retro Archive** — Filter: Meeting Type = Retrospective, sorted by Date descending
- **Calendar** — Calendar view, by Date
- **Meetings with Open Items** — Filter: Open Action Items > 0

---

### 2. Action Items

**Purpose:** Every task that comes out of a meeting — with a clear owner, deadline, and status. The accountability layer that turns meeting talk into actual work.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Action Item | Title | Specific, actionable description — e.g. "Draft Q2 OKRs and share with team by Friday" |
| Meeting | Relation | -> Meetings database (where this action item was created) |
| Meeting Title | Rollup | Meeting Title from linked Meeting |
| Meeting Date | Rollup | Date from linked Meeting |
| Meeting Type | Rollup | Meeting Type from linked Meeting |
| Owner | Person | Who is responsible for completing this |
| Owner Name | Text | Fallback: owner name as text |
| Status | Select | To Do / In Progress / Blocked / Complete / Cancelled |
| Priority | Select | Urgent / High / Medium / Low |
| Due Date | Date | When this needs to be done |
| Days Until Due | Formula | `if(empty(prop("Due Date")), 999, dateBetween(prop("Due Date"), now(), "days"))` |
| Overdue | Formula | `if(and(prop("Days Until Due") < 0, prop("Status") != "Complete", prop("Status") != "Cancelled"), true, false)` |
| Urgency | Formula | `if(or(prop("Status") == "Complete", prop("Status") == "Cancelled"), "Done", if(prop("Overdue"), "OVERDUE", if(prop("Days Until Due") <= 1, "DUE TODAY", if(prop("Days Until Due") <= 3, "DUE SOON", "On Track"))))` |
| Completed Date | Date | When the action item was actually completed |
| Days to Complete | Formula | `if(and(not(empty(prop("Completed Date"))), not(empty(prop("Meeting Date")))), dateBetween(prop("Completed Date"), prop("Meeting Date"), "days"), 0)` |
| Blocked By | Text | What's preventing progress (fill in when Status = Blocked) |
| Related Decision | Relation | -> Decisions database (if this action item implements a decision) |
| Notes | Text | Additional context, links, or deliverable details |
| Reviewed In | Relation | -> Meetings database (which meeting reviewed this item's progress) |
| Created | Date | Auto-set when the action item is created |
| Tags | Multi-select | Quick Win / Requires Approval / Cross-Team / Technical / Process / Communication |

**Views:**

- **All Action Items** — Table, sorted by Due Date ascending
- **Open Items** — Filter: Status = To Do or In Progress or Blocked, sorted by Due Date
- **Overdue** — Filter: Overdue = true, sorted by Due Date ascending (most overdue first)
- **By Owner** — Table, grouped by Owner Name, sorted by Due Date (shows each person's workload)
- **By Meeting** — Table, grouped by Meeting Title, sorted by Due Date
- **Blocked** — Filter: Status = Blocked
- **Due This Week** — Filter: Days Until Due >= 0 AND Days Until Due <= 7, Status not Complete
- **Completed** — Filter: Status = Complete, sorted by Completed Date descending
- **Action Item Board** — Kanban, grouped by Status
- **By Priority** — Table, grouped by Priority, sorted by Due Date

---

### 3. Decisions

**Purpose:** Every significant decision your team makes — with context, rationale, and a link to the meeting where it was made. Your team's institutional memory.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Decision | Title | Clear statement of what was decided — e.g. "Migrate from Heroku to AWS by end of Q2" |
| Meeting | Relation | -> Meetings database (where this decision was made) |
| Meeting Title | Rollup | From linked Meeting |
| Meeting Date | Rollup | Date from linked Meeting |
| Date | Date | Decision date (may differ from meeting date if ratified later) |
| Category | Select | Technical / Product / Process / People / Budget / Strategy / Policy / Vendor / Other |
| Impact | Select | High / Medium / Low |
| Status | Select | Active / Superseded / Reversed / Under Review / Proposed |
| Decision Makers | Text | Who was in the room and agreed to this decision |
| Context | Text | What situation or problem led to this decision? What were the constraints? |
| Options Considered | Text | What alternatives were discussed before reaching this decision? |
| Rationale | Text | Why was this option chosen over the alternatives? What was the reasoning? |
| Risks | Text | What risks does this decision introduce? What could go wrong? |
| Reversible | Select | Easily Reversible / Reversible with Effort / Difficult to Reverse / Irreversible |
| Review Date | Date | When should this decision be revisited? (especially for "let's try this for 3 months" decisions) |
| Outcome | Text | Fill in later: what actually happened as a result of this decision? |
| Superseded By | Relation | -> Decisions database (self-referential — link to the decision that replaced this one) |
| Related Action Items | Relation | -> Action Items database |
| Tags | Multi-select | Architecture / Hiring / Process Change / Tool Selection / Budget / Scope / Timeline / Team Structure |

**Views:**

- **All Decisions** — Table, sorted by Date descending
- **Active Decisions** — Filter: Status = Active, sorted by Date descending
- **By Category** — Table, grouped by Category
- **High Impact** — Filter: Impact = High, sorted by Date descending
- **Needs Review** — Filter: Review Date is within 14 days, Status = Active
- **Recent** — Filter: Date is within last 30 days
- **Decision Archive** — Full table with all fields, for searching
- **Superseded** — Filter: Status = Superseded (useful for understanding decision evolution)
- **By Meeting** — Table, grouped by Meeting Title

---

## MEETING AGENDA TEMPLATES

---

### Template 1: Daily Standup (15 minutes)

> **Purpose:** Quick team sync to surface blockers and coordinate the day's work. Not a status report — a coordination mechanism.
>
> **Format:** Synchronous (video call) or async (fill in before a set time).
>
> **Cadence:** Daily, same time, same link.

```
STANDUP — [Date]

TEAM: [Team Name]
TIME: [Time + Time Zone]
FACILITATOR: [Name — rotate weekly]

PREVIOUS ACTION ITEMS (2 min)
Review any overdue or due-today items from the Action Items database.
[Linked view -> Action Items, filter: Owner is attendee, Due = today or overdue]

ROUND ROBIN (10 min — 2 min per person max)
Each person answers:

[Name 1]
- Yesterday:
- Today:
- Blockers:

[Name 2]
- Yesterday:
- Today:
- Blockers:

[Name 3]
- Yesterday:
- Today:
- Blockers:

[Name 4]
- Yesterday:
- Today:
- Blockers:

[Name 5]
- Yesterday:
- Today:
- Blockers:

PARKING LOT (3 min)
Items that need discussion but shouldn't happen in standup.
Schedule follow-up conversations for anything that takes >2 min.

-
-

NEW ACTION ITEMS
[Capture any action items generated — add to Action Items database]
```

**Standup rules:**
- Hard stop at 15 minutes. If you're running over, the topics are too detailed for standup.
- Blockers are the most important part. If someone is blocked, resolve it immediately or assign someone to unblock them today.
- "Yesterday/Today" is about coordination, not accountability. The goal is for teammates to know if they need to sync with anyone.
- If a topic requires discussion, say "parking lot" and move on. Schedule a separate 15-minute call.

**Async standup option:**
- Each team member fills in their section in the Notion page by 9:00 AM local time
- Facilitator reviews all updates and flags any blockers or conflicts
- Sync standup is skipped unless blockers require real-time discussion
- This saves 75 minutes per week per team (15 min x 5 days) when no blockers exist

---

### Template 2: 1:1 Meeting (30 minutes)

> **Purpose:** Manager-report relationship maintenance, priority alignment, blocker removal, and career development.
>
> **Format:** Video call (cameras on preferred — this is a relationship meeting).
>
> **Cadence:** Weekly or bi-weekly.

```
1:1 — [Manager Name] & [Report Name] — [Date]

PREVIOUS ACTION ITEMS (3 min)
[Linked view -> Action Items from last 1:1, filter: Owner = either person]
- [ ] [Item 1] — Status:
- [ ] [Item 2] — Status:

CHECK-IN (3 min)
How are you doing? (Not a formality — listen to the answer.)
Energy level this week (1-5):
Anything on your mind outside of work that's affecting your work?


REPORT'S AGENDA (10 min — report drives this section)
Topics the report wants to discuss. Report should add these before the meeting.
1.
2.
3.

MANAGER'S AGENDA (5 min — manager drives this section)
Topics the manager wants to discuss or share.
1.
2.

PRIORITIES & ALIGNMENT (5 min)
Top 3 priorities for the next 1-2 weeks:
1.
2.
3.

Any misalignment between what you're working on and what you think
you should be working on?


BLOCKERS & SUPPORT (3 min)
What's slowing you down? What can I unblock for you?


GROWTH & DEVELOPMENT (ongoing — cover at least monthly)
- Current development goal:
- Progress since last check-in:
- What support do you need?

FEEDBACK (give or request — cover at least bi-weekly)
- Feedback for report:
- Feedback for manager:

NEW ACTION ITEMS
- [ ] [Owner] — [Action] — Due: [Date]
- [ ] [Owner] — [Action] — Due: [Date]
```

**1:1 best practices:**
- This is the report's meeting, not the manager's. The report should bring 60% of the agenda.
- Never cancel a 1:1. If you must reschedule, reschedule to the same week.
- Link to the previous 1:1 using the "Previous Meeting" relation. This creates a running thread.
- Cover growth/development at least once a month. Don't let the urgent crowd out the important.
- End every 1:1 with at least one action item for each person.
- Avoid turning 1:1s into status updates — that's what standups are for. 1:1s are for alignment, support, and feedback.

---

### Template 3: Retrospective (60 minutes)

> **Purpose:** Reflect on the last sprint/cycle, identify what worked and what didn't, and commit to specific improvements.
>
> **Format:** Video call with screen share (facilitator drives the Notion page).
>
> **Cadence:** End of every sprint/cycle (typically bi-weekly or monthly).

```
RETROSPECTIVE — [Sprint/Cycle Name] — [Date]

TEAM: [Team Name]
FACILITATOR: [Name — should rotate each retro]
ATTENDEES: [List]

REVIEW LAST RETRO'S ACTION ITEMS (5 min)
Did we follow through on what we committed to last time?
[Linked view -> Action Items from last Retro]

| Action Item | Owner | Status | Notes |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

Completion rate: ___/___
If items are incomplete — why? Carry forward or drop?

WHAT WENT WELL (10 min)
What should we keep doing? What are we proud of?
(Each person contributes at least one item. Facilitator captures all.)

1.
2.
3.
4.
5.
6.

WHAT DIDN'T GO WELL (10 min)
What was frustrating? What slowed us down? What would we change?
(Psychological safety note: this is about systems and processes,
not blame. Facilitator should model this.)

1.
2.
3.
4.
5.
6.

WHAT SHOULD WE CHANGE? (15 min)
Based on the above, what specific changes do we want to make?
(Discussion should be focused on actionable improvements, not venting.)

1.
2.
3.

VOTE ON TOP IMPROVEMENTS (5 min)
Each person gets 3 votes. Place them on the changes above.
Top 2-3 by vote count become action items.

| Improvement | Votes | Action? |
|---|---|---|
| | | |
| | | |
| | | |

SHOUTOUTS (5 min)
Who went above and beyond? Who helped you? Who deserves recognition?
(This is important. Remote teams under-recognize each other.)

-
-
-

ACTION ITEMS (5 min)
Commit to 2-3 specific, owned, time-bound improvements.
More than 3 means you'll complete none of them.

- [ ] [Owner] — [Specific action] — Due: [Date]
- [ ] [Owner] — [Specific action] — Due: [Date]
- [ ] [Owner] — [Specific action] — Due: [Date]

RETRO HEALTH CHECK
How was this retro? (1-5):
What should we change about the retro format itself?

```

**Retro best practices:**
- Limit to 3 action items. Retros that generate 10 action items complete zero of them.
- Always review last retro's action items first. If the team consistently doesn't follow through, that's the retro topic.
- Rotate the facilitator. Different facilitators surface different conversations.
- Use silent writing time (2-3 minutes) before each section to get honest, uninfluenced input. Then discuss.
- The "What should we change?" section must produce actions, not observations. "Communication was bad" is an observation. "Create a #blockers channel in Slack and post there before standup" is an action.

---

### Template 4: All-Hands Meeting (45 minutes)

> **Purpose:** Company or team-wide alignment. Share results, celebrate wins, surface strategy, and answer questions.
>
> **Format:** Video call with presentation/screen share. One or two speakers, rest of team on mute with Q&A.
>
> **Cadence:** Monthly or bi-weekly.

```
ALL-HANDS — [Date]

HOST: [Name/Role]
ATTENDEES: All [Team/Company]
RECORDING: [Link — post after meeting for those who can't attend live]

OPENING (2 min)
Welcome. Brief framing of what's on the agenda.

METRICS & RESULTS (10 min)
Key numbers since last all-hands. Show the data.

| Metric | Last Period | This Period | Change | Target |
|---|---|---|---|---|
| [Revenue/Users/etc.] | | | | |
| [Key metric 2] | | | | |
| [Key metric 3] | | | | |
| [Key metric 4] | | | | |

Commentary:


WINS & HIGHLIGHTS (5 min)
What went well? What should the whole team celebrate?

1.
2.
3.

TEAM/INDIVIDUAL SPOTLIGHT (5 min)
Feature a team or individual who did exceptional work.

Spotlight: [Name/Team]
What they did:
Why it matters:

STRATEGIC UPDATES (10 min)
What's changing? What's the direction for the next period?
(Keep it to 2-3 topics max. Depth over breadth.)

1. [Topic]:
2. [Topic]:
3. [Topic]:

ANNOUNCEMENTS (5 min)
Operational announcements the whole team needs to know.

-
-
-

Q&A (8 min)
Open floor. Encourage questions in chat/thread for those uncomfortable
asking live. Read and answer submitted questions.

Q:
A:

Q:
A:

Q:
A:

UNANSWERED QUESTIONS
(Capture questions that couldn't be answered live — assign an owner
to follow up with answers within 48 hours.)

| Question | Assigned To | Answer | |
|---|---|---|---|
| | | | |
| | | | |

CLOSING (2 min)
Summary of the 1-2 most important things discussed.
Next all-hands date.

DECISIONS MADE
[Add to Decisions database]

ACTION ITEMS
[Add to Action Items database]
- [ ] [Owner] — [Action] — Due: [Date]
- [ ] [Owner] — Follow up on unanswered questions — Due: [2 days]
```

**All-hands best practices:**
- Record every all-hands. Team members in different time zones or who are out should be able to watch the recording.
- Post the recording and notes within 24 hours.
- The Q&A section is non-negotiable. If leadership doesn't take questions, trust erodes.
- Answer every submitted question — even the uncomfortable ones. If a question can't be answered publicly, say so and explain why.
- Spotlight a different team or individual every all-hands. Recognition at the company level matters more than most leaders realize.
- Keep strategic updates to 2-3 topics. Trying to cover everything means communicating nothing.

---

## DASHBOARD

> Create this as the top-level Notion page. Pin it to your team's sidebar. Every team member sees this as their meeting operations home base.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  MEETING COMMAND CENTER               April 2026              |
+--------------+--------------+--------------+-----------------+
|  Meetings    |  Open Action |  Overdue     |  Decisions      |
|  This Week   |  Items       |  Items       |  This Month     |
|     7        |    12        |     3        |     5           |
+--------------+--------------+--------------+-----------------+
|  UPCOMING MEETINGS                                           |
|  [Linked view -> Meetings, filter: Status = Scheduled,       |
|   sorted by Date ascending, limit next 7 days]               |
+-------------------------------------------------------------+
|  OVERDUE ACTION ITEMS                                        |
|  [Linked view -> Action Items, filter: Overdue = true,       |
|   sorted by Due Date ascending]                              |
+-----------------------------+-------------------------------+
|  ACTION ITEMS BY OWNER      |  DUE THIS WEEK                 |
|  [Linked view -> Action     |  [Linked view -> Action Items, |
|   Items, grouped by Owner,  |   filter: Due This Week,       |
|   filter: Status != Done]   |   Status != Complete]          |
+-----------------------------+-------------------------------+
|  RECENT DECISIONS                                            |
|  [Linked view -> Decisions, sorted by Date descending,       |
|   limit 10]                                                  |
+-------------------------------------------------------------+
|  MEETING CALENDAR                                            |
|  [Linked view -> Meetings, Calendar by Date]                 |
+-------------------------------------------------------------+
```

### Dashboard Summary Stats

Create four callout blocks side by side at the top:

- **Meetings This Week** — Count from Meetings view filtered to this week
- **Open Action Items** — Count from Action Items where Status is not Complete or Cancelled
- **Overdue Items** — Count from Action Items where Overdue = true
- **Decisions This Month** — Count from Decisions where Date is this month

---

## KEY FORMULA REFERENCE

### Overdue Detection (Action Items database)
Flags any action item where the due date has passed and the item is not complete or cancelled.

```
if(
  and(
    prop("Days Until Due") < 0,
    prop("Status") != "Complete",
    prop("Status") != "Cancelled"
  ),
  true,
  false
)
```

### Urgency Level (Action Items database)
Classifies action items by how close they are to their deadline.

```
if(
  or(prop("Status") == "Complete", prop("Status") == "Cancelled"),
  "Done",
  if(
    prop("Overdue"),
    "OVERDUE",
    if(
      prop("Days Until Due") <= 1,
      "DUE TODAY",
      if(
        prop("Days Until Due") <= 3,
        "DUE SOON",
        "On Track"
      )
    )
  )
)
```

### Meeting Efficiency (Meetings database)
Compares planned duration to actual duration so you can spot meetings that consistently run over.

```
if(
  and(
    prop("Actual Duration (min)") > 0,
    prop("Duration (min)") > 0
  ),
  if(
    prop("Actual Duration (min)") <= prop("Duration (min)"),
    "On Time",
    "Ran Over"
  ),
  ""
)
```

### Days to Complete (Action Items database)
Measures how long action items take from creation to completion. Useful for understanding team velocity on meeting-generated tasks.

```
if(
  and(
    not(empty(prop("Completed Date"))),
    not(empty(prop("Meeting Date")))
  ),
  dateBetween(prop("Completed Date"), prop("Meeting Date"), "days"),
  0
)
```

---

## QUICK-START GUIDE

### Step 1 — Set Up Your First Meeting (5 minutes)
- Open the **Meetings** database
- Create a new entry for your next upcoming meeting
- Set Meeting Type, Date, Duration, and Attendees
- Copy the appropriate agenda template (from the templates above) into the Agenda field
- Share the Notion page link in your meeting invite so attendees can see the agenda before the meeting

### Step 2 — Run Your First Structured Meeting (during the meeting)
- Open the Notion page at the start of the meeting
- Screen-share the agenda (the facilitator drives the page)
- Fill in Notes as the meeting progresses
- When an action item is agreed upon: immediately create it in the **Action Items** database with an Owner and Due Date
- When a decision is made: immediately create it in the **Decisions** database with Context and Rationale
- At the end of the meeting: review all action items captured to confirm accuracy

### Step 3 — Set Up the Action Items Tracker (5 minutes)
- Open the **Action Items** database
- Check the "By Owner" view — each team member should see their items
- Share the "Overdue" view with your team — this is the accountability view
- Make reviewing overdue items the first agenda item in every standup

### Step 4 — Initialize the Decisions Database (5 minutes)
- Open the **Decisions** database
- Add 3-5 recent significant decisions your team has made (even if they happened before you had this template)
- For each: fill in Decision, Date, Category, Context, and Rationale
- This seeds your institutional memory so the database has value immediately

### Step 5 — Set Up Your Dashboard
- Pin the Dashboard page to your team's Notion sidebar
- Every team member should see the dashboard when they open Notion
- The Overdue Action Items section is the most important view — check it daily

### Step 6 — Establish Team Rhythms

**Daily:**
- Facilitator creates tomorrow's Standup entry using the template
- Team fills in standup updates (async) or delivers them live
- Action items from standup are added to the database immediately

**Weekly:**
- Run 1:1s using the template — link to previous 1:1 for continuity
- Review the "Open Items" view: is anything stuck or blocked?
- Check "Needs Review" in Decisions: any decisions due for reconsideration?

**Bi-weekly or per-sprint:**
- Run Retrospective using the template
- Always start with last retro's action items
- Commit to max 3 new action items

**Monthly:**
- Run All-Hands using the template
- Post recording and notes within 24 hours
- Review meeting efficiency: are meetings running over? Which types?

### Team Rollout Plan

**Week 1 — Pilot with standups:**
- Create standup entries for every day this week
- Have the team fill in their updates using the template
- Add action items from standups to the database
- This is the lowest-friction way to build the habit

**Week 2 — Add 1:1s and action item tracking:**
- Run 1:1s using the template
- Begin actively using the "Overdue" view in standups: "Let's check if any action items are overdue"
- Team starts to feel the benefit of tracked accountability

**Week 3 — Add retrospective and decisions:**
- Run your first retro using the template
- Begin logging decisions in the Decisions database
- The "Decisions" view becomes your team's reference when questions arise

**Week 4 — Full system operational:**
- All meeting types are running from templates
- Action items are tracked and reviewed daily
- Decisions are logged and searchable
- The dashboard is your team's operational home base

### Pro Tips

- The fastest way to build adoption is the "Overdue" view. When people see their overdue items displayed in standup, they start completing action items before the meeting. That's the system working.
- Always create the meeting entry and share the agenda link before the meeting. Preparation time is when meetings become productive.
- For 1:1s: link every 1:1 to the previous one using the "Previous Meeting" relation. This creates a running thread that makes career development conversations build on each other over time.
- Rotate the standup and retro facilitator. It builds shared ownership and prevents one person from becoming the "meeting person."
- Use the Meeting Rating property honestly. If a meeting is consistently rated 2 or below, cancel it or fundamentally change the format. Not every recurring meeting deserves to exist.
- The Decisions database is the sleeper hit of this template. You won't appreciate it for the first month. Six months in, when someone asks "why did we choose that vendor?" and you can pull up the decision with context and alternatives in 10 seconds — that's when it pays for itself.
- Keep action items specific and time-bound. "Improve documentation" is not an action item. "Write onboarding guide for the API integration and share in #engineering by Friday" is an action item.
- If your team resists, start small. Even just using the standup template + action item tracker will change your meeting culture within 2 weeks.
