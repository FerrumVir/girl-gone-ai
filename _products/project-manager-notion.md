# Project Manager Pro — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Read the Quick-Start Guide at the bottom before entering your real data — the setup order matters.

---

## DATABASES

---

### 1. Projects

**Purpose:** The master record for every project — client, internal, or personal. All task, milestone, and team data connects back here. This is the single source of truth for project status, health, timeline, and financials.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Project Name | Title | Clear, descriptive name — include client or department if managing many projects |
| Client / Stakeholder | Text | Client name or internal department owning this project |
| Project Type | Select | Client Work / Internal / Retainer / Discovery / Maintenance / Campaign |
| Status | Select | Not Started / Active / On Hold / Waiting on Client / In Review / Complete / Cancelled |
| Priority | Select | Critical / High / Medium / Low |
| Owner | Relation | → Team & Resources database — primary accountable person |
| Start Date | Date | Kickoff or contract start date |
| Target End Date | Date | Hard deadline or committed delivery date |
| Actual End Date | Date | Set when project reaches Complete status |
| Days Remaining | Formula | `if(prop("Status") == "Active", dateBetween(prop("Target End Date"), now(), "days"), 0)` |
| Timeline Progress % | Formula | `if(dateBetween(prop("Target End Date"), prop("Start Date"), "days") > 0, round((dateBetween(now(), prop("Start Date"), "days") / dateBetween(prop("Target End Date"), prop("Start Date"), "days")) * 100), 0)` |
| Total Tasks | Rollup | Count all from linked Tasks |
| Completed Tasks | Rollup | Count of linked Tasks where Status = Done |
| Task Completion % | Formula | `if(prop("Total Tasks") > 0, round((prop("Completed Tasks") / prop("Total Tasks")) * 100), 0)` |
| Total Milestones | Rollup | Count all from linked Milestones |
| Completed Milestones | Rollup | Count of linked Milestones where Status = Complete |
| Overdue Tasks | Rollup | Count of linked Tasks where Overdue Alert = "OVERDUE" |
| Health Score | Formula | See formula section below |
| Health Status | Formula | `if(prop("Health Score") >= 75, "On Track", if(prop("Health Score") >= 45, "At Risk", "Off Track"))` |
| Budget | Number (USD) | Total project budget |
| Budget Type | Select | Fixed / Hourly / Retainer / Internal (no budget) |
| Hours Estimated | Number | Total estimated hours for this project |
| Hours Logged | Rollup | Sum of Hours from linked Tasks |
| Budget Utilized % | Formula | `if(prop("Hours Estimated") > 0, round((prop("Hours Logged") / prop("Hours Estimated")) * 100), 0)` |
| Budget vs. Timeline Gap | Formula | `prop("Budget Utilized %") - prop("Timeline Progress %")` — positive means running hot |
| Scope Notes | Text | What's in scope, what's explicitly excluded |
| Key Deliverables | Text | Numbered list of top-level outputs |
| Contract Signed | Checkbox | |
| Kickoff Done | Checkbox | |
| Invoice Trigger | Text | Notes on billing milestones or payment schedule |
| Linked Tasks | Relation | → Tasks database |
| Linked Milestones | Relation | → Milestones database |
| Linked Team | Relation | → Team & Resources database |
| Tags | Multi-select | Rush / Long-term / High-visibility / Recurring / Portfolio |
| Notes | Text | Internal project notes, decisions, context |

**Views:**

- **Active Projects** — Table, filter: Status = Active, sorted by Target End Date ascending
- **Project Board** — Kanban, grouped by Status
- **Project Timeline** — Timeline view, date range: Start Date → Target End Date, grouped by Client/Stakeholder
- **Health Dashboard** — Table, sorted by Health Score ascending (worst health first), show: Project Name, Status, Health Status, Task Completion %, Days Remaining, Overdue Tasks
- **Budget Watch** — Table, filter: Budget Type != Internal (no budget), sorted by Budget vs. Timeline Gap descending
- **All Projects** — Table, sorted by Start Date descending
- **Completed** — Table, filter: Status = Complete, sorted by Actual End Date descending

---

### 2. Tasks

**Purpose:** Every unit of work across all projects. The core execution layer. Tasks link upward to projects and milestones, outward to team members, and to each other via dependency relationships.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Task Name | Title | Specific, action-oriented — starts with a verb when possible |
| Project | Relation | → Projects database — required |
| Project Name | Rollup | From Project relation |
| Milestone | Relation | → Milestones database — optional, link if this task is part of a milestone |
| Assignee | Relation | → Team & Resources database |
| Assignee Name | Rollup | From Assignee relation |
| Status | Select | To Do / In Progress / In Review / Blocked / Done / Cancelled |
| Priority | Select | Critical / High / Medium / Low |
| Task Type | Select | Design / Development / Content / Research / Review / Admin / Communication / Other |
| Start Date | Date | When work should begin |
| Due Date | Date | Hard deadline for this task |
| Days Until Due | Formula | `dateBetween(prop("Due Date"), now(), "days")` |
| Overdue Alert | Formula | `if(and(prop("Due Date") < now(), not(prop("Status") == "Done"), not(prop("Status") == "Cancelled")), "OVERDUE", if(and(prop("Days Until Due") <= 2, not(prop("Status") == "Done")), "DUE SOON", ""))` |
| Hours Estimated | Number | Estimated effort in hours |
| Hours Logged | Number | Actual time spent — update as you work |
| Effort Variance | Formula | `if(prop("Hours Estimated") > 0, prop("Hours Logged") - prop("Hours Estimated"), 0)` — positive means over estimate |
| Is Subtask | Checkbox | Check if this is a child task under a parent task |
| Parent Task | Relation | → Tasks database (self-relation) — link the parent task if Is Subtask is checked |
| Subtasks | Relation | → Tasks database (self-relation) — populated automatically via Parent Task inverse |
| Blocked By | Relation | → Tasks database (self-relation) — list all tasks that must be Done before this one can start |
| Blocks | Relation | → Tasks database (self-relation) — populated automatically via Blocked By inverse |
| Blocking Status | Formula | `if(prop("Blocked By Count") > 0, if(prop("Open Predecessors") > 0, "Blocked", "Ready"), "Ready")` |
| Blocked By Count | Rollup | Count all from Blocked By relation |
| Open Predecessors | Rollup | Count of linked Blocked By tasks where Status != Done |
| Description | Text | Task details, acceptance criteria, or relevant context |
| Attachments | Files & Media | Supporting files, references, or assets |
| Comments | Text | Internal notes, questions, update log |
| Created | Created time | Auto-populated |
| Last Updated | Last edited time | Auto-populated |
| Tags | Multi-select | Client-facing / Internal / Recurring / Quick Win / Deep Work |

**Views:**

- **My Tasks** — Table, filter: Assignee = [your name], Status != Done / Cancelled, sorted by Priority then Due Date
- **All Active Tasks** — Table, filter: Status = In Progress OR To Do, sorted by Due Date ascending
- **Kanban Board** — Kanban, grouped by Status, filtered to active project(s)
- **Blocked Tasks** — Table, filter: Blocking Status = Blocked — shows tasks waiting on predecessors
- **Overdue** — Table, filter: Overdue Alert = OVERDUE, sorted by Due Date ascending
- **By Project** — Table, grouped by Project Name, sorted by Priority within groups
- **By Assignee** — Table, grouped by Assignee Name, sorted by Due Date within groups
- **This Week** — Calendar view, filter: Due Date is this week
- **Done** — Table, filter: Status = Done, sorted by Last Updated descending
- **Effort Tracker** — Table, show: Task Name, Assignee Name, Hours Estimated, Hours Logged, Effort Variance — for retrospective review

---

### 3. Milestones

**Purpose:** The delivery gates that matter to clients and stakeholders. Milestones represent meaningful checkpoints — phase completions, client approvals, launch events, or billing triggers. They aggregate task completion data to show real progress against what was promised.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Milestone Name | Title | Descriptive name that means something to the client — e.g., "Design Approval", "Beta Launch", "Phase 2 Kickoff" |
| Project | Relation | → Projects database — required |
| Project Name | Rollup | From Project relation |
| Milestone Type | Select | Phase Gate / Client Approval / Deliverable / Launch / Invoice Trigger / Internal Review / Retrospective |
| Status | Select | Not Started / In Progress / At Risk / Complete / Delayed / Cancelled |
| Target Date | Date | Committed delivery date for this milestone |
| Actual Date | Date | Date milestone was actually achieved |
| Days Until Target | Formula | `if(prop("Status") != "Complete", dateBetween(prop("Target Date"), now(), "days"), 0)` |
| Milestone Overdue | Formula | `if(and(prop("Target Date") < now(), prop("Status") != "Complete", prop("Status") != "Cancelled"), "OVERDUE", if(prop("Days Until Target") <= 5, "DUE SOON", ""))` |
| Linked Tasks | Relation | → Tasks database |
| Total Tasks | Rollup | Count all from linked Tasks |
| Completed Tasks | Rollup | Count of linked Tasks where Status = Done |
| Completion % | Formula | `if(prop("Total Tasks") > 0, round((prop("Completed Tasks") / prop("Total Tasks")) * 100), 0)` |
| Open Blockers | Rollup | Count of linked Tasks where Blocking Status = Blocked |
| Milestone Owner | Relation | → Team & Resources database |
| Description | Text | What this milestone represents, what must be true for it to be complete |
| Client-Facing | Checkbox | Check if this milestone is visible in client status reports |
| Invoice Trigger Amount | Number (USD) | If billing on milestone achievement, enter the invoice amount |
| Notes | Text | Context, decisions, dependencies on other milestones |
| Predecessor Milestones | Relation | → Milestones database (self-relation) — milestones that must be Complete before this one is reachable |

**Views:**

- **Milestone Roadmap** — Timeline view, date: Target Date, grouped by Project Name
- **Upcoming Milestones** — Table, filter: Status != Complete / Cancelled, sorted by Target Date ascending, showing next 30 days
- **At Risk** — Table, filter: Status = At Risk OR Milestone Overdue = OVERDUE, sorted by Target Date ascending
- **Client-Facing** — Table, filter: Client-Facing = checked — use this to build client status reports
- **By Project** — Table, grouped by Project Name, sorted by Target Date within groups
- **Invoice Triggers** — Table, filter: Invoice Trigger Amount > 0, Status != Complete — surfaces upcoming billable milestones
- **Completed Milestones** — Table, filter: Status = Complete, sorted by Actual Date descending
- **Calendar** — Calendar view, date: Target Date

---

### 4. Team & Resources

**Purpose:** One record per team member or contractor. Provides a live view of who is working on what, how loaded they are, and where capacity exists. Works equally well for a solo operator (track yourself) or a distributed team.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Name | Title | Full name or handle |
| Role | Select | Project Manager / Designer / Developer / Copywriter / Strategist / Account Manager / Contractor / Intern |
| Email | Email | Primary contact |
| Availability | Select | Full-time / Part-time / Contractor / On Leave |
| Weekly Capacity (hrs) | Number | Available working hours per week — e.g., 40 for full-time, 20 for part-time |
| Active Tasks | Rollup | Count of linked Tasks where Status = In Progress OR To Do |
| Total Tasks Assigned | Rollup | Count of all linked Tasks where Status != Cancelled |
| Hours Committed This Week | Rollup | Sum of Hours Estimated from linked Tasks where Due Date = this week and Status != Done / Cancelled |
| Capacity Used % | Formula | `if(prop("Weekly Capacity (hrs)") > 0, round((prop("Hours Committed This Week") / prop("Weekly Capacity (hrs)")) * 100), 0)` |
| Workload Status | Formula | `if(prop("Capacity Used %") > 100, "Overloaded", if(prop("Capacity Used %") >= 80, "Near Capacity", if(prop("Capacity Used %") >= 40, "Healthy", "Light Load")))` |
| Overdue Tasks | Rollup | Count of linked Tasks where Overdue Alert = OVERDUE |
| Linked Projects | Relation | → Projects database — projects this person is actively involved in |
| Linked Tasks | Relation | → Tasks database — all tasks assigned to this person |
| Linked Milestones | Relation | → Milestones database — milestones this person owns |
| Skills | Multi-select | UX Design / UI Design / Frontend / Backend / Copywriting / SEO / Paid Media / Strategy / PM / Video / Illustration |
| Timezone | Select | ET / CT / MT / PT / GMT / CET / IST / AEST / Other |
| Start Date | Date | When this person joined the team or engagement |
| Notes | Text | Working preferences, communication style, tools used |
| Tags | Multi-select | Core Team / Contractor / Client-Facing / Technical Lead |

**Views:**

- **Workload Board** — Gallery view, sorted by Capacity Used % descending — shows each person as a card with load indicator
- **Capacity Table** — Table, sorted by Capacity Used % descending, showing: Name, Role, Active Tasks, Hours Committed This Week, Weekly Capacity (hrs), Capacity Used %, Workload Status
- **Overloaded** — Table, filter: Workload Status = Overloaded — use before assigning new tasks
- **Light Load** — Table, filter: Workload Status = Light Load OR Healthy — use to find available people
- **By Project** — Table, grouped by Linked Projects — see who is on each project
- **Skills Directory** — Table, sorted by Role, filtered to Availability = Full-time / Part-time / Contractor

---

## DASHBOARD

> Build this as a Notion page that pulls in linked database views. Pin this page to your Notion sidebar and open it every morning.

### Dashboard Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  PROJECT MANAGER PRO                           Week of [Date]     │
├───────────────┬───────────────┬───────────────┬──────────────────┤
│ Active        │ Milestones    │ Overdue       │ Team Members     │
│ Projects      │ Due This Week │ Tasks         │ Overloaded       │
│    [N]        │    [N]        │    [N]        │    [N]           │
├───────────────┴───────────────┴───────────────┴──────────────────┤
│  PROJECT HEALTH                                                   │
│  [Linked view → Projects, "Health Dashboard" view]               │
│  Columns: Project Name | Health Status | Task % | Days Left      │
│           Overdue Tasks | Budget Utilized %                      │
├──────────────────────────────────────────────────────────────────┤
│  UPCOMING MILESTONES (Next 14 Days)                              │
│  [Linked view → Milestones, "Upcoming Milestones" view]          │
│  Columns: Milestone Name | Project | Target Date | Completion %  │
│           Milestone Owner | Status                               │
├──────────────────────────────────────────────────────────────────┤
│  OVERDUE & BLOCKED TASKS                                         │
│  [Linked view → Tasks, "Overdue" view]                           │
│  [Linked view → Tasks, "Blocked Tasks" view]                     │
├──────────────────────────────────────────────────────────────────┤
│  TEAM WORKLOAD                                                    │
│  [Linked view → Team & Resources, "Capacity Table" view]         │
│  Columns: Name | Role | Active Tasks | Hours This Week           │
│           Capacity Used % | Workload Status                      │
├──────────────────────────────────────────────────────────────────┤
│  THIS WEEK'S TASKS (Calendar)                                    │
│  [Linked view → Tasks, "This Week" calendar view]                │
└──────────────────────────────────────────────────────────────────┘
```

### How to Build the Summary Callouts

Add four **Callout blocks** at the top of the dashboard for the four summary numbers. Update these manually at the start of each week during your review, or use linked database view counts:

- **Active Projects** — Count from Projects where Status = Active
- **Milestones Due This Week** — Count from Milestones where Target Date is this week and Status != Complete
- **Overdue Tasks** — Count from Tasks where Overdue Alert = OVERDUE
- **Team Members Overloaded** — Count from Team & Resources where Workload Status = Overloaded

---

## KEY FORMULAS

### Project Health Score

The health score combines three signals: task completion progress vs. timeline elapsed, overdue task count, and milestone status. Copy this formula into the **Health Score** Number formula property on the Projects database.

```
if(
  prop("Status") == "Complete" or prop("Status") == "Cancelled",
  100,
  max(
    0,
    min(
      100,
      (
        (
          if(
            prop("Timeline Progress %") > 0,
            prop("Task Completion %") - prop("Timeline Progress %"),
            0
          ) + 50
        )
        - (prop("Overdue Tasks") * 15)
        - (
          if(
            prop("Total Milestones") > 0,
            round(
              ((prop("Total Milestones") - prop("Completed Milestones")) / prop("Total Milestones")) * 10
            ),
            0
          )
        )
      )
    )
  )
)
```

**How to read the score:**
- **75–100** — On Track: task completion is keeping pace with (or ahead of) the timeline
- **45–74** — At Risk: task completion is falling behind the timeline or overdue tasks are accumulating
- **0–44** — Off Track: significant gap between timeline progress and task completion, or multiple overdue items

---

### Task Overdue Detection

Copy into the **Overdue Alert** Formula property on the Tasks database.

```
if(
  or(prop("Status") == "Done", prop("Status") == "Cancelled"),
  "",
  if(
    prop("Due Date") < now(),
    "OVERDUE",
    if(
      dateBetween(prop("Due Date"), now(), "days") <= 2,
      "DUE SOON",
      ""
    )
  )
)
```

---

### Blocking Status (Dependency Check)

Copy into the **Blocking Status** Formula property on the Tasks database. This requires the **Open Predecessors** rollup to be configured first (count of linked Blocked By tasks where Status != Done).

```
if(
  or(prop("Status") == "Done", prop("Status") == "Cancelled"),
  "Complete",
  if(
    prop("Open Predecessors") > 0,
    "Blocked",
    "Ready"
  )
)
```

---

### Team Workload Status

Copy into the **Workload Status** Formula property on the Team & Resources database.

```
if(
  prop("Weekly Capacity (hrs)") == 0,
  "No Capacity Set",
  if(
    prop("Capacity Used %") > 100,
    "Overloaded",
    if(
      prop("Capacity Used %") >= 80,
      "Near Capacity",
      if(
        prop("Capacity Used %") >= 40,
        "Healthy",
        "Light Load"
      )
    )
  )
)
```

---

### Milestone Completion Percentage

Copy into the **Completion %** Formula property on the Milestones database.

```
if(
  prop("Total Tasks") == 0,
  if(prop("Status") == "Complete", 100, 0),
  round((prop("Completed Tasks") / prop("Total Tasks")) * 100)
)
```

---

### Days Until Due (Signed — Negative = Overdue)

Optional secondary formula for any database with a due date. Useful for sorting "most overdue first."

```
dateBetween(prop("Due Date"), now(), "days")
```

A negative result means the item is that many days overdue. Sort ascending to put the most overdue items first.

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Team

Before adding any projects, open the **Team & Resources** database and create a record for each person who will appear on tasks or milestones (including yourself).

- Set the **Role** and **Availability** for each person
- Enter **Weekly Capacity (hrs)** — this is critical for workload formulas to work correctly (use 40 for full-time, 20 for half-time, your typical weekly hours for solo use)
- Add **Skills** and **Timezone** if you're managing a distributed team
- For solo use: create a single record for yourself and use it for all assignments

### Step 2 — Create Your First Project

Open **Projects** and click "+ New."

- Give it a clear **Project Name** — include the client name if you're managing multiple clients (e.g., "Acme Corp — Website Redesign")
- Set **Status** to Active, **Priority**, and **Project Type**
- Enter **Start Date** and **Target End Date**
- Fill in **Budget** and **Hours Estimated** if you're tracking financials
- Link the **Owner** to the relevant Team & Resources record
- Add **Scope Notes** and **Key Deliverables** to capture what was agreed
- Check **Contract Signed** and **Kickoff Done** when those happen

### Step 3 — Add Milestones

Before creating individual tasks, define the milestones — the delivery gates the project must pass through.

- Open **Milestones** and create 3–6 milestones per project (less for small projects)
- Set **Milestone Type** and a clear **Target Date** for each
- Link each milestone to the project via the **Project** relation
- Check **Client-Facing** on any milestone that belongs in a status report
- Set **Invoice Trigger Amount** on billing milestones if you invoice by phase

Good milestone examples: "Discovery Complete," "Wireframes Approved," "Development Complete," "QA Signed Off," "Launch," "Post-Launch Review."

### Step 4 — Build Your Task List

With milestones defined, break each one into concrete tasks.

- Open **Tasks** and create tasks for the first milestone or first two weeks of work
- Link each task to its **Project** (required) and to a **Milestone** if applicable
- Assign to a team member via the **Assignee** relation
- Set **Status** (start at "To Do"), **Priority**, **Due Date**, and **Hours Estimated**
- For tasks with dependencies, use **Blocked By** to link to the task(s) that must finish first — the Blocking Status formula will update automatically
- For large tasks with multiple steps, create subtasks and check **Is Subtask** on the children, then link them to the parent via **Parent Task**

**Tip:** Don't try to plan every task for a long project upfront. Create tasks for the current milestone or sprint window, then plan forward as you approach each new milestone.

### Step 5 — Configure Your Dashboard

Once you have at least one project, two or three milestones, and a handful of tasks, set up the dashboard.

- Create a new Notion page called "Project Manager Pro — Dashboard"
- Add the four callout summary blocks at the top (update manually each Monday)
- Use **"Create linked database"** in Notion to add a view of each database to the dashboard
- Select the pre-built views for each linked database (e.g., "Health Dashboard" view for Projects, "Upcoming Milestones" for Milestones, "Overdue" and "Blocked Tasks" for Tasks, "Capacity Table" for Team)
- Rearrange sections to match the ASCII layout above, or arrange them to match your review workflow
- Add the page to your Notion sidebar favorites

### Step 6 — Run Your Weekly Review

Set a recurring 15–20 minute block each Monday morning to run through the dashboard.

1. **Project Health** — Any project that dropped to At Risk or Off Track since last week? Investigate root cause and either address the blockers or update the timeline expectation.
2. **Upcoming Milestones** — Any milestone due in the next 14 days with less than 80% task completion? Treat this as an alert. Reassign tasks, clear blockers, or have a scope conversation now rather than at deadline.
3. **Overdue Tasks** — Clear the overdue list. Reassign, reschedule, or cancel — but do not leave overdue tasks sitting unchecked. Every overdue item is a signal.
4. **Blocked Tasks** — Check if any blocked tasks can be unblocked. Look at what's in the Blocked By chain and see if those predecessor tasks need to be prioritized or reassigned.
5. **Team Workload** — Anyone overloaded? Anyone with a light load who could absorb work from an overloaded team member? Balance before assigning any new work arriving this week.
6. **Forward Planning** — Review tasks due this week. Are they realistically scoped? Are the right people assigned? Adjust before the week starts, not after.

---

## PRO TIPS

- **Status workflow matters:** Enforce a strict transition: To Do → In Progress → In Review → Done. Do not skip In Review for client-facing work — it prevents unreviewed deliverables reaching clients.

- **Naming convention for projects:** Use a consistent format like `[Client] — [Project Name] — [Year]` (e.g., "Acme — Brand Refresh — 2026"). This makes filters, rollups, and search much more useful as your project count grows.

- **Use Milestone Type = Invoice Trigger** to replace a separate billing tracker. When the milestone hits Complete, that's your trigger to send an invoice. The Invoice Trigger Amount property gives you the number without digging through a contract.

- **Don't over-link tasks to milestones.** Only link tasks to a milestone if that task's completion is genuinely part of what makes that milestone achievable. Keep milestones meaningful, not a bucket for every task on the project.

- **For retrospectives,** use the Effort Tracker view on Tasks (Hours Estimated vs. Hours Logged) filtered to completed projects. This is the fastest way to see where your estimates were off and calibrate future proposals.

- **Archive completed projects** by changing Status to Complete and adding an Actual End Date. Keep the record — the rollup data and task history is valuable for future estimates, proposals, and portfolio references.

- **The Timeline view on Milestones** is your de facto Gantt chart. Group by Project, zoom to the appropriate time range, and you have a clean delivery calendar you can screenshot and share with stakeholders.
