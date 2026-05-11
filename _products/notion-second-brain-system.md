# Second Brain System (PARA Method) — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases follow Tiago Forte's PARA methodology with progressive summarization built in. The capture inbox and review scheduling system are pre-configured. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Projects

**Purpose:** Active outcomes with a defined end date. A project has a clear finish line — when it's done, it moves to Archive. This is where your current commitments live, each linked to actionable notes and resources.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Project Name | Title | Clear outcome statement (e.g., "Launch podcast by March 15") |
| Status | Select | Active / Waiting / On Hold / Completed / Someday |
| Area | Relation | -> Areas database (which life area does this serve?) |
| Priority | Select | P1 (This Week) / P2 (This Month) / P3 (This Quarter) / P4 (Someday) |
| Start Date | Date | When work began |
| Due Date | Date | Target completion |
| Completed Date | Date | Actual completion |
| Days Remaining | Formula | `if(prop("Status") == "Completed", "Done", if(empty(prop("Due Date")), "No deadline", format(dateBetween(prop("Due Date"), now(), "days")) + " days"))` |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Completed"), true, false)` |
| Next Action | Text | The very next physical step |
| Next Action Date | Date | When it needs to happen |
| Progress | Select | Not Started / 25% / 50% / 75% / Nearly Done / Complete |
| Linked Resources | Relation | -> Resources database |
| Linked Notes | Relation | -> Inbox/Notes database |
| Resource Count | Rollup | Count of Linked Resources |
| Note Count | Rollup | Count of Linked Notes |
| Outcome | Text | What does "done" look like? |
| Stakeholders | Text | Who else is involved |
| Tags | Multi-select | Work / Personal / Creative / Learning / Health / Financial |
| Project Notes | Text | Running context, decisions made, blockers |

**Views:**

- **Active Projects** — Board, grouped by Status, filtered to exclude Completed
- **By Priority** — Table, sorted by Priority ascending, filtered to Status = Active
- **By Area** — Table, grouped by Area relation
- **This Week** — Filter: Priority = P1, Status = Active
- **Needs Action** — Filter: Overdue = true OR Next Action Date is past
- **Completed** — Filter: Status = Completed, sorted by Completed Date descending
- **Timeline** — Timeline view, Start Date to Due Date
- **Someday/Maybe** — Filter: Status = Someday OR Priority = P4

---

### 2. Areas

**Purpose:** Ongoing responsibilities with no end date. Areas represent the roles and standards you maintain indefinitely — your health, your finances, your career, your relationships. Areas don't get "completed" — they get maintained.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Area Name | Title | Role or responsibility (e.g., "Health & Fitness", "Career Development") |
| Description | Text | What does maintaining this area look like? What standard are you upholding? |
| Life Domain | Select | Professional / Personal / Health / Financial / Relationships / Creative / Spiritual / Home |
| Status | Select | Active / Maintenance / Needs Attention / On Hold |
| Icon | Text | Emoji or icon for visual identification |
| Current Projects | Rollup | Count of linked Projects where Status = Active |
| Total Resources | Rollup | Count of linked Resources |
| Key Metrics | Text | How you know this area is in good shape (list 2-3 indicators) |
| Review Frequency | Select | Weekly / Bi-weekly / Monthly / Quarterly |
| Last Reviewed | Date | When you last assessed this area |
| Next Review | Formula | `if(empty(prop("Last Reviewed")), "Never reviewed", if(prop("Review Frequency") == "Weekly", dateAdd(prop("Last Reviewed"), 7, "days"), if(prop("Review Frequency") == "Bi-weekly", dateAdd(prop("Last Reviewed"), 14, "days"), if(prop("Review Frequency") == "Monthly", dateAdd(prop("Last Reviewed"), 1, "months"), dateAdd(prop("Last Reviewed"), 3, "months")))))` |
| Review Overdue | Formula | `if(and(not(empty(prop("Next Review"))), prop("Next Review") < now()), true, false)` |
| Linked Projects | Relation | -> Projects database |
| Linked Resources | Relation | -> Resources database |
| Notes | Text | Standards, boundaries, commitments for this area |
| Tags | Multi-select | Core / Growth / Maintenance / Aspirational |

**Views:**

- **All Areas** — Gallery view with Icon, Area Name, Status, Current Projects
- **Active Areas** — Filter: Status = Active or Maintenance, sorted by Life Domain
- **Needs Attention** — Filter: Status = Needs Attention OR Review Overdue = true
- **By Domain** — Table, grouped by Life Domain
- **Review Schedule** — Table showing Next Review, sorted ascending

---

### 3. Resources

**Purpose:** Reference material organized by topic. Resources are things you want to keep for ongoing reference — articles, book notes, templates, guides, research, frameworks, and checklists. They're not tied to a deadline; they're available whenever you need them.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Title | Title | Descriptive name of the resource |
| Type | Select | Article / Book Notes / Course Notes / Video Notes / Podcast Notes / Framework / Template / Checklist / Research / Tutorial / Tool / Reference |
| Source URL | URL | Original source link |
| Author | Text | Creator of the original material |
| Topic | Multi-select | Productivity / Business / Marketing / Design / Writing / Technology / Psychology / Health / Finance / Leadership / Communication / Philosophy / Science / Creativity |
| Area | Relation | -> Areas database |
| Project | Relation | -> Projects database |
| Status | Select | To Process / Layer 1 Done / Layer 2 Done / Layer 3 Done / Evergreen / Outdated |
| Layer 1 — Captured | Text | Full text or raw highlights (bold the interesting parts) |
| Layer 2 — Highlighted | Text | Only the bolded passages from Layer 1 (the best 20%) |
| Layer 3 — Summarized | Text | Your own words: the core insight in 2-3 sentences |
| Layer 4 — Remixed | Text | How this connects to your work/life; original thoughts sparked |
| Key Insight | Text | Single sentence: what's the one takeaway? |
| Actionable | Checkbox | Does this contain something to act on? |
| Action Item | Text | Specific next step from this resource |
| Action Done | Checkbox | Completed the action |
| Quality Rating | Select | Essential / Valuable / Decent / Mediocre / Skip |
| Date Added | Date | When you captured this |
| Last Accessed | Date | When you last referenced this |
| Times Referenced | Number | How often you've come back to this |
| Review Date | Date | When to revisit |
| Tags | Multi-select | Evergreen / Timely / Foundational / Advanced / Quick Reference / Deep Dive |
| Related Resources | Relation | -> Resources (self-referential for linking related notes) |

**Views:**

- **All Resources** — Table, sorted by Date Added descending
- **To Process** — Filter: Status = To Process, sorted by Date Added ascending (oldest first)
- **By Topic** — Table, grouped by Topic
- **By Area** — Table, grouped by Area
- **Evergreen** — Filter: Status = Evergreen, sorted by Times Referenced descending
- **Actionable** — Filter: Actionable = true AND Action Done = false
- **Book Notes** — Filter: Type = Book Notes
- **Frameworks** — Filter: Type = Framework
- **Recently Added** — Sorted by Date Added descending, limit 20
- **Review Queue** — Filter: Review Date <= today, sorted by Review Date ascending
- **Best Of** — Filter: Quality Rating = Essential, sorted by Times Referenced descending

---

### 4. Archive

**Purpose:** Completed projects, outdated resources, and inactive areas stored for historical reference. Nothing is deleted — everything that leaves active circulation moves here. Searchable when you need it, invisible when you don't.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Item Name | Title | Original title from source database |
| Original Database | Select | Project / Area / Resource / Note |
| Archived Date | Date | When it was moved to archive |
| Original Status | Text | What was its status when archived |
| Archive Reason | Select | Completed / No Longer Relevant / Superseded / Outdated / Failed / Cancelled |
| Original Area | Text | Which life area it belonged to |
| Summary | Text | Brief description of what this was and why it mattered |
| Outcome Notes | Text | What happened? What did you learn? |
| Worth Revisiting | Checkbox | Flag for items that might be useful again |
| Revisit Trigger | Text | Under what circumstances would this become relevant again? |
| Tags | Multi-select | Success / Failure / Learning / Reference / Historical |
| Original URL | URL | If it was a resource, link to source |
| Date Created | Date | When the original item was first created |
| Lifespan | Formula | `if(and(not(empty(prop("Date Created"))), not(empty(prop("Archived Date")))), format(dateBetween(prop("Archived Date"), prop("Date Created"), "days")) + " days active", "Unknown")` |

**Views:**

- **All Archived** — Table, sorted by Archived Date descending
- **By Type** — Table, grouped by Original Database
- **Completed Projects** — Filter: Original Database = Project AND Archive Reason = Completed
- **Worth Revisiting** — Filter: Worth Revisiting = true
- **By Reason** — Table, grouped by Archive Reason
- **Search** — Table with all properties visible for finding old items
- **Recent** — Sorted by Archived Date descending, limit 30

---

### 5. Inbox (Capture System)

**Purpose:** Zero-friction capture point for everything — thoughts, ideas, links, tasks, references, and random inspiration. Nothing stays here permanently. During processing, every item gets moved to Projects, Resources, or Archive (or deleted).

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Capture | Title | Raw thought, link, or note — whatever came to mind |
| Captured Date | Created time | Auto-populated |
| Source | Select | Thought / Web Clip / Conversation / Book / Podcast / Meeting / Email / Social Media / Other |
| Source URL | URL | Link if captured from web |
| Type Guess | Select | Task / Project Idea / Resource / Reference / Thought / Quote / Action Item |
| Energy to Process | Select | Quick (2 min) / Medium (10 min) / Deep (30+ min) |
| Processed | Checkbox | Has this been sorted into PARA? |
| Destination | Select | Project / Resource / Archive / Delete / Waiting |
| Linked Project | Relation | -> Projects (assigned during processing) |
| Linked Resource | Relation | -> Resources (if it becomes a resource) |
| Priority | Select | Process Today / This Week / Whenever / Low |
| Context | Text | Additional notes captured in the moment |
| Days in Inbox | Formula | `dateBetween(now(), prop("Captured Date"), "days")` |
| Stale | Formula | `if(and(not(prop("Processed")), prop("Days in Inbox") > 7), true, false)` |

**Views:**

- **Unprocessed** — Filter: Processed = false, sorted by Captured Date descending (default working view)
- **Quick Wins** — Filter: Processed = false AND Energy to Process = Quick
- **Stale Items** — Filter: Stale = true (items sitting more than 7 days)
- **By Source** — Table, grouped by Source
- **Today's Captures** — Filter: Captured Date = today
- **Processed** — Filter: Processed = true, sorted by Captured Date descending

---

## DASHBOARD

> Create this as the top-level Notion page. It serves as your Second Brain command center — the single page you open every day to capture, process, and retrieve.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  SECOND BRAIN                                    May 2026          |
+----------------+--------------+----------------+-----------------+
|  Inbox Items   |  Active      |  Resources     |  Areas Needing  |
|  12 to process |  Projects: 5 |  342 total     |  Review: 2      |
+----------------+--------------+----------------+-----------------+
|                                                                    |
|  CAPTURE INBOX                                                    |
|  [Linked view -> Inbox, filter: Processed = false]                |
|  + New Capture button                                             |
|                                                                    |
+----------------------------------+-------------------------------+
|  ACTIVE PROJECTS                 |  PROCESS QUEUE                |
|  [Linked view -> Projects,       |  [Linked view -> Resources,   |
|   Status = Active, sorted by     |   Status = To Process,        |
|   Priority]                      |   sorted by Date Added]       |
+----------------------------------+-------------------------------+
|  AREAS OVERVIEW                                                   |
|  [Linked view -> Areas, Gallery, Status = Active]                 |
+----------------------------------+-------------------------------+
|  RECENTLY ADDED RESOURCES        |  REVIEW SCHEDULE              |
|  [Linked view -> Resources,      |  [Linked view -> Areas,       |
|   sorted by Date Added desc,     |   filter: Review Overdue]     |
|   limit 10]                      |  [Linked view -> Resources,   |
|                                  |   Review Date <= today]       |
+----------------------------------+-------------------------------+
|  STALE INBOX ITEMS (> 7 days)                                     |
|  [Linked view -> Inbox, Stale = true]                             |
+------------------------------------------------------------------+
```

---

## PROGRESSIVE SUMMARIZATION SYSTEM

Progressive summarization is the core technique for making notes findable and useful. Each layer distills the information further:

### Layer 0 — Original Source
The full article, book chapter, or transcript. Stored externally (or in Layer 1 of Resources).

### Layer 1 — Captured Highlights
Bold the passages that resonated. This is your first pass — highlight anything interesting without judgment. Aim for 10-20% of the original.

### Layer 2 — Progressive Highlights
From your Layer 1 bold text, highlight (or copy) only the truly essential passages. This should be 10-20% of Layer 1 — the core ideas.

### Layer 3 — Executive Summary
Write 2-5 sentences in your own words. What is the main argument? What's the single most important insight? This is what you'll read during reviews.

### Layer 4 — Remix
How does this connect to your existing knowledge? What does it change about how you think or act? This is where original thought happens.

### Processing Workflow

```
Inbox Item Captured
  -> Open item, read/review content
  -> Decide: Is this a Project task, a Resource, or trash?
  -> If Resource: Create entry in Resources database
    -> Add Layer 1 highlights
    -> Set Topic, Area, Tags
    -> Set Status = "Layer 1 Done"
    -> Set Review Date (1-2 weeks out for first review)
  -> If Project task: Link to relevant Project, add to project notes
  -> If neither: Archive or delete
  -> Mark Inbox item as Processed
```

---

## REVIEW SCHEDULING SYSTEM

### Area Review Formula

```
if(
  empty(prop("Last Reviewed")),
  "Never reviewed",
  if(
    prop("Review Frequency") == "Weekly",
    dateAdd(prop("Last Reviewed"), 7, "days"),
    if(
      prop("Review Frequency") == "Bi-weekly",
      dateAdd(prop("Last Reviewed"), 14, "days"),
      if(
        prop("Review Frequency") == "Monthly",
        dateAdd(prop("Last Reviewed"), 1, "months"),
        dateAdd(prop("Last Reviewed"), 3, "months")
      )
    )
  )
)
```

### Review Overdue Detection

```
if(
  and(
    not(empty(prop("Next Review"))),
    prop("Next Review") < now()
  ),
  true,
  false
)
```

### Spaced Repetition Schedule for Resources

After each review of a Resource, extend the Review Date interval:
- First review: 1 week after capture
- Second review: 2 weeks after first review
- Third review: 1 month after second review
- Fourth review: 3 months after third review
- Fifth+ review: 6 months (evergreen material)

Update the Review Date manually after each review and increment Times Referenced.

### Inbox Staleness Detection

```
if(
  and(
    not(prop("Processed")),
    prop("Days in Inbox") > 7
  ),
  true,
  false
)
```

Items sitting in Inbox for more than 7 days get flagged. During weekly review, either process them or delete them. A permanently growing inbox defeats the purpose.

---

## KEY FORMULA REFERENCE

### Project Days Remaining

```
if(
  prop("Status") == "Completed",
  "Done",
  if(
    empty(prop("Due Date")),
    "No deadline",
    format(dateBetween(prop("Due Date"), now(), "days")) + " days"
  )
)
```

### Project Overdue Detection

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Completed"
  ),
  true,
  false
)
```

### Archive Lifespan Calculation

```
if(
  and(
    not(empty(prop("Date Created"))),
    not(empty(prop("Archived Date")))
  ),
  format(dateBetween(prop("Archived Date"), prop("Date Created"), "days")) + " days active",
  "Unknown"
)
```

### Days in Inbox

```
dateBetween(now(), prop("Captured Date"), "days")
```

---

## WEEKLY REVIEW PROTOCOL

Every week (Sunday, 20-30 minutes):

### 1. Clear the Inbox (10 minutes)
- Open **Inbox > Unprocessed** view
- Process each item: assign to Project, create Resource, or delete
- Goal: zero unprocessed items (or flag anything needing deep processing for a dedicated session)

### 2. Review Active Projects (5 minutes)
- Open **Projects > Active** view
- Update Progress and Next Action for each
- Move completed projects to Archive
- Check: does any project need a new resource or note?

### 3. Check Areas (3 minutes)
- Open **Areas > Needs Attention** view
- Any areas with Review Overdue? Do a quick status check
- Update Last Reviewed date

### 4. Process Resources Queue (5 minutes)
- Open **Resources > To Process** view
- Pick 2-3 items and add Layer 2 or Layer 3 summaries
- Set next Review Date

### 5. Review Scheduled Reviews (2 minutes)
- Open **Resources > Review Queue**
- Quickly re-read Layer 3 summaries of items due
- Increment Times Referenced
- Extend Review Date based on spaced repetition schedule

---

## MONTHLY REVIEW ADDITIONS

Once per month (first Sunday, add 15 minutes to weekly review):

- Review all Areas: are any slipping? Do priorities need reshuffling?
- Check Archive: anything flagged "Worth Revisiting" that's now relevant?
- Resource audit: delete or archive anything rated Mediocre or Skip that you'll never reference
- Project pipeline: promote any Someday/Maybe items to Active if capacity allows
- Count stats: How many items captured this month? How many processed? What's your capture-to-evergreen conversion rate?

---

## QUICK-START GUIDE

### Step 1 — Define Your Areas (10 minutes)

- Open the **Areas** database
- Add 5-8 areas of responsibility (e.g., Career, Health, Finances, Relationships, Home, Creative Work, Learning)
- For each, write a one-sentence Description of what "maintained" looks like
- Set Review Frequency (monthly is fine for most areas to start)

### Step 2 — Add Active Projects (10 minutes)

- Open the **Projects** database
- Add everything you're currently committed to with a defined end date
- Link each project to its relevant Area
- Set Status, Priority, and Due Date
- Write the Next Action for each

### Step 3 — Seed Resources (15 minutes)

- Open the **Resources** database
- Add 10-15 of your best existing notes, bookmarks, or highlights
- For each, add at minimum: Title, Type, Topic, and Layer 1 content
- Don't try to migrate everything at once — add resources organically as you reference them

### Step 4 — Start Capturing (ongoing)

- Use the **Inbox** for everything: thoughts while walking, links from Twitter, ideas from conversations
- Keep capture friction as low as possible — Notion mobile, web clipper, or a daily batch from your notes app
- Don't organize during capture. Just dump and move on.

### Step 5 — Process Daily (5 minutes)

- Open the Inbox once per day
- Move Quick items immediately (2-minute tasks, simple resources)
- Flag anything that needs deep processing for your weekly review

### Step 6 — Weekly Review (start week 2)

- Follow the Weekly Review Protocol above
- This is non-negotiable. Without it, the system accumulates debt and becomes a graveyard.

### Pro Tips

- The Inbox is not a to-do list. If something is a task, it belongs in a Project. The Inbox is a temporary holding zone — nothing should live there permanently.
- Process Resources in layers over time, not all at once. Layer 1 on first capture, Layer 2 during weekly review, Layer 3 when you reference it for a project. Most resources never need Layer 4 — and that's fine.
- An Area is not a goal. "Get fit" is a project with a defined outcome. "Health & Fitness" is an area you maintain forever. If it has an end date, it's a project.
- Archive aggressively. Completed projects, outdated resources, and notes you haven't referenced in 6+ months belong in Archive. You can always search for them.
- The "Worth Revisiting" flag in Archive is powerful — it lets you archive without anxiety. If circumstances change, you'll find it.
- Quality Rating on Resources saves time during reviews. If you rated something "Mediocre" six months ago, you can safely skip or delete it without re-reading.
- Your Second Brain's value compounds over time. The first month feels like overhead. By month three, you'll start finding connections between resources that generate original ideas. By month six, you'll wonder how you ever worked without it.
