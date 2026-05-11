# ADHD Productivity System — Notion Template

> Duplicate this page into your Notion workspace to get started. Every database, formula, and view is designed around ADHD neuroscience — not neurotypical assumptions. The system compensates for executive function challenges at a structural level. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Brain Dump Inbox

**Purpose:** Zero-friction capture for every thought, task, worry, idea, and random impulse that fires through your ADHD brain. Nothing gets judged or organized here — just captured. Processing happens later in a separate, structured workflow.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Capture | Title | Whatever's in your head — raw, unfiltered, no formatting required |
| Captured | Created time | Auto-populated timestamp |
| Source | Select | Random Thought / Anxiety / Task / Idea / Reminder / Impulse Buy / Someday / Conversation / Other |
| Energy to Sort | Select | Low (2 min) / Medium (10 min) / High (needs focus session) |
| Processed | Checkbox | Has this been sorted? |
| Destination | Select | Task Board / Someday / Delete / Reference / Waiting / Calendar |
| Urgency Guess | Select | Today / This Week / Eventually / Never |
| Days in Inbox | Formula | `dateBetween(now(), prop("Captured"), "days")` |
| Stale | Formula | `if(and(not(prop("Processed")), prop("Days in Inbox") > 3), true, false)` |
| Context | Text | Any additional notes you captured in the moment |

**Views:**

- **Dump Zone** — Filter: Processed = false, sorted by Captured descending (default — what you see when you open this)
- **Quick Sort** — Filter: Processed = false AND Energy to Sort = Low (2-minute items)
- **Stale** — Filter: Stale = true (sitting more than 3 days — decide or delete)
- **By Source** — Table, grouped by Source
- **Processed** — Filter: Processed = true (archive of what you've handled)

---

### 2. Task Board (Energy-Based)

**Purpose:** Your active task list organized by energy level required — not arbitrary priority levels that mean nothing when your executive function is offline. You pick tasks based on your current energy state, not guilt.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Task | Title | Clear, specific action (verb + object) — "Email Sarah about timeline" not "project stuff" |
| Energy Required | Select | Zombie (near-zero effort) / Low (light cognitive load) / Medium (sustained attention) / High (deep focus required) / Hyperfocus-worthy (complex, engaging, time-intensive) |
| Status | Select | To Do / In Progress / Blocked / Done / Won't Do |
| Time Estimate | Select | 2 min / 5 min / 15 min / 30 min / 1 hr / 2 hr / Deep Session |
| Actual Time | Number | How long it actually took (minutes) — for calibrating future estimates |
| Context | Select | Computer / Phone / Errands / Home / Anywhere / With Others |
| Project | Text | Which project this belongs to (optional) |
| Due Date | Date | Hard deadline (only if it truly exists — don't fake urgency) |
| Soft Deadline | Date | When you'd like it done (no guilt if missed) |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Done", prop("Status") != "Won't Do"), true, false)` |
| Dopamine Rating | Select | Boring / Neutral / Mildly Interesting / Fun / Exciting |
| Reward After | Text | What you get after completing this (immediate reward) |
| Body Double | Checkbox | Easier with someone else present? |
| First Step | Text | The absolute smallest first action (2-minute start) |
| Blocked By | Text | What's preventing this from starting? |
| Created | Created time | Auto-populated |
| Completed Date | Date | When finished |
| Days Open | Formula | `if(prop("Status") == "Done", dateBetween(prop("Completed Date"), prop("Created"), "days"), dateBetween(now(), prop("Created"), "days"))` |
| Paralysis Risk | Formula | `if(and(prop("Energy Required") == "High", prop("Dopamine Rating") == "Boring", prop("Time Estimate") == "2 hr"), "High - break this down!", if(and(prop("Energy Required") == "Medium", prop("Dopamine Rating") == "Boring"), "Medium - use body doubling", "Low"))` |
| Tags | Multi-select | Quick Win / Procrastinated / Admin / Creative / Repeat / One-time / Batch-able |

**Views:**

- **Right Now (by energy)** — Board, grouped by Energy Required, filtered to Status = To Do (MAIN VIEW — pick based on current energy)
- **Zombie Mode** — Filter: Energy Required = Zombie, Status = To Do (for crash days)
- **Quick Wins (under 15 min)** — Filter: Time Estimate = 2 min OR 5 min OR 15 min, Status = To Do
- **Dopamine Menu** — Filter: Dopamine Rating = Fun or Exciting, Status = To Do
- **Overdue** — Filter: Overdue = true
- **Blocked** — Filter: Status = Blocked (what needs unblocking?)
- **Body Double Tasks** — Filter: Body Double = true, Status = To Do
- **High Paralysis Risk** — Filter: Paralysis Risk contains "High" (needs breakdown)
- **Done This Week** — Filter: Status = Done, Completed Date is this week (celebration view)
- **Won't Do** — Filter: Status = Won't Do (permission to drop things)

---

### 3. Dopamine Menu

**Purpose:** A pre-built list of healthy, accessible dopamine sources organized by time and energy cost. When you finish a task, get bored, or feel the urge to doom-scroll, open this instead. It replaces destructive dopamine habits with intentional ones.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Activity | Title | The dopamine-generating activity |
| Time Required | Select | 2 min / 5 min / 15 min / 30 min / 1 hr / Open-ended |
| Energy Cost | Select | Zero / Low / Medium / High |
| Category | Select | Physical / Creative / Social / Sensory / Learning / Gaming / Nature / Music / Food / Other |
| Indoor/Outdoor | Select | Indoor / Outdoor / Either |
| Solo/Social | Select | Solo / Social / Either |
| Dopamine Level | Select | Mild Boost / Good Hit / Strong Rush / Hyperfocus Fuel |
| Availability | Select | Always / Most Days / Requires Planning / Weather Dependent |
| Post-Activity Feeling | Select | Energized / Calm / Satisfied / Neutral / Sometimes Drained |
| Last Done | Date | When you last did this |
| Frequency | Text | How often you typically do this |
| Notes | Text | Conditions, tips, variations |
| Favorites | Checkbox | One of your go-to activities |

**Views:**

- **Quick Hits (under 15 min)** — Filter: Time Required = 2 min, 5 min, or 15 min (for between-task breaks)
- **By Category** — Board, grouped by Category
- **Favorites** — Filter: Favorites = true
- **Solo Activities** — Filter: Solo/Social = Solo or Either
- **By Time** — Table, grouped by Time Required
- **Haven't Done Recently** — Sorted by Last Done ascending (rediscover forgotten pleasures)
- **Zero Energy** — Filter: Energy Cost = Zero (for crash moments)
- **Physical Options** — Filter: Category = Physical or Nature

---

### 4. Hyperfocus Sessions

**Purpose:** Tracks when hyperfocus states occur, what triggered them, how long they lasted, and what the aftermath looked like. Over time, this data reveals your flow patterns so you can schedule important work during natural hyperfocus windows and plan recovery for afterward.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Name | Title | What you hyperfocused on |
| Date | Date | When it happened |
| Start Time | Text | Approximate start (e.g., "2pm") |
| End Time | Text | When you surfaced |
| Duration (hrs) | Number | Total hours in hyperfocus |
| Trigger | Select | Deadline Pressure / Novel Topic / Creative Flow / Problem-Solving / Personal Interest / Anger/Frustration / Competition / Unknown |
| Activity Type | Select | Work / Creative / Research / Learning / Gaming / Hobby / Admin / Code / Writing |
| Planned | Checkbox | Did you intentionally enter this state? |
| Productive | Checkbox | Was the output valuable? |
| Quality of Output | Select | Exceptional / Good / Mixed / Wasted |
| Physical Neglect | Multi-select | Skipped Meal / No Water / Missed Sleep / No Breaks / Ignored People / Missed Appointment |
| Recovery Needed | Select | None / Light (30 min) / Moderate (few hours) / Heavy (next day crash) |
| Aftermath Mood | Select | Satisfied / Energized / Crashed / Anxious / Irritable / Proud / Guilty |
| What Broke the State | Select | Exhaustion / Interruption / Hunger / Boredom Shift / Completed / External Obligation |
| Lessons | Text | What did you learn about your hyperfocus patterns? |
| Day of Week | Formula | `formatDate(prop("Date"), "dddd")` |
| Time of Day | Formula | `if(contains(prop("Start Time"), "am"), "Morning", if(or(contains(prop("Start Time"), "12"), contains(prop("Start Time"), "1p"), contains(prop("Start Time"), "2p")), "Early Afternoon", "Late Afternoon/Evening"))` |
| Week | Formula | `formatDate(prop("Date"), "W")` |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **Productive Sessions** — Filter: Productive = true AND Quality of Output = Exceptional or Good
- **By Trigger** — Table, grouped by Trigger (find what reliably induces flow)
- **By Day of Week** — Table, grouped by Day of Week (find your best days)
- **By Time** — Table, grouped by Time of Day formula
- **Heavy Recovery** — Filter: Recovery Needed = Heavy (avoid replicating these conditions)
- **Unplanned** — Filter: Planned = false (understand accidental hyperfocus)
- **Pattern Analysis** — Table showing Trigger, Day of Week, Time of Day, Duration, Quality

---

### 5. Body Doubling Log

**Purpose:** Tracks your body doubling sessions — working alongside someone (in-person or virtually) to overcome task initiation paralysis. Records who, when, what you accomplished, and how it compared to working alone.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session | Title | Brief description of what you worked on |
| Date | Date | When the session happened |
| Partner | Text | Who you body doubled with (person, group, or service) |
| Type | Select | In-Person / Video Call / Discord / Focusmate / Cafe Proximity / Twitch Stream / Library |
| Duration (min) | Number | Session length in minutes |
| Tasks Completed | Number | How many tasks you finished |
| Task List | Text | What specifically got done |
| Effectiveness | Select | Breakthrough / Very Helpful / Somewhat Helpful / Didn't Help / Made It Worse |
| Would Have Done Alone | Select | Definitely Not / Probably Not / Maybe / Probably Yes |
| Task Type | Select | Admin / Creative / Difficult / Boring / Phone Calls / Cleaning / Other |
| Notes | Text | What worked, what didn't, observations |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **By Effectiveness** — Table, grouped by Effectiveness
- **By Type** — Table, grouped by Type
- **Best Partners** — Table, grouped by Partner, sorted by average Effectiveness
- **By Task Type** — Table, grouped by Task Type (find what benefits most from body doubling)

---

## DASHBOARD

> This is your daily landing page. Open it every time you sit down to work. It immediately tells you what your options are based on your current state — no decision fatigue, no guilt-based priority lists.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  ADHD COMMAND CENTER                                              |
+------------------------------------------------------------------+
|  HOW ARE YOU RIGHT NOW?                                           |
|                                                                    |
|  [Energy selector - pick your current state:]                     |
|  Zombie | Low | Medium | High | Hyperfocus                       |
|                                                                    |
|  (Based on selection, view the matching energy level in Task      |
|   Board below)                                                    |
+----------------------------------+-------------------------------+
|  BRAIN DUMP                      |  QUICK WINS (< 15 min)       |
|  [Linked view -> Brain Dump,     |  [Linked view -> Task Board,  |
|   Processed = false]             |   Time Estimate <= 15 min,    |
|                                  |   Status = To Do]             |
|  + Quick Capture button          |                               |
+----------------------------------+-------------------------------+
|  TODAY'S TASK BOARD (by energy level)                              |
|  [Linked view -> Task Board, Board grouped by Energy Required]    |
|                                                                    |
|  Zombie    |  Low      |  Medium   |  High     | Hyperfocus     |
|  --------  |  -------  |  -------  |  -------  | ----------     |
|  Sort mail |  Emails   |  Write    |  Strategy | Redesign       |
|  Dishes    |  Schedule |  Research |  Coding   | Build app      |
+----------------------------------+-------------------------------+
|  DOPAMINE MENU                   |  OVERDUE (actual deadlines)   |
|  [Linked view -> Dopamine Menu,  |  [Linked view -> Task Board,  |
|   Quick Hits + Favorites]        |   Overdue = true]             |
+----------------------------------+-------------------------------+
|  DONE THIS WEEK (celebrate!)     |  BODY DOUBLE OPPORTUNITIES    |
|  [Linked view -> Task Board,     |  [Linked view -> Task Board,  |
|   Done this week - count them!]  |   Body Double = true]         |
+----------------------------------+-------------------------------+
|  HYPERFOCUS INSIGHTS                                              |
|  [Linked view -> Hyperfocus Sessions, last 5, showing Trigger     |
|   and Quality]                                                    |
+------------------------------------------------------------------+
```

---

## ENERGY-BASED TASK SORTING

The core principle: ADHD brains cannot reliably choose tasks from a traditional priority list because executive function governs task initiation — the very thing ADHD impairs. Energy-based sorting works because it removes the choice paralysis and matches tasks to your actual capacity in the moment.

### Energy Levels Explained

**Zombie (near-zero effort):**

- Executive function is offline
- Tasks: sort laundry, wash one dish, delete emails, file papers, water plants
- No decisions required, no focus needed, purely mechanical

**Low (light cognitive load):**

- Can follow simple instructions but not generate plans
- Tasks: respond to easy emails, make a phone call from a script, simple data entry, scheduling
- Low-stakes, low-complexity, clear next step

**Medium (sustained attention):**

- Can focus for 20-30 minute blocks with breaks
- Tasks: write a draft, research a topic, plan an event, moderate-complexity work
- Requires some cognitive effort but isn't deeply challenging

**High (deep focus required):**

- Full executive function available (rare and precious)
- Tasks: strategic planning, complex problem-solving, difficult conversations, creative work
- Protect these windows ruthlessly

**Hyperfocus-worthy:**

- Tasks complex and engaging enough to trigger flow state
- Tasks: major project work, coding, writing, creative projects, learning new skills
- Schedule these when you've identified your natural hyperfocus windows from session data

---

## PARALYSIS RISK FORMULA

```
if(
  and(
    prop("Energy Required") == "High",
    prop("Dopamine Rating") == "Boring",
    prop("Time Estimate") == "2 hr"
  ),
  "High - break this down!",
  if(
    and(
      prop("Energy Required") == "Medium",
      prop("Dopamine Rating") == "Boring"
    ),
    "Medium - use body doubling",
    "Low"
  )
)
```

Tasks that are high-energy, boring, AND long are ADHD kryptonite. The formula flags these so you can:
1. Break them into 15-minute micro-tasks
2. Pair them with body doubling
3. Add an immediate reward after each segment
4. Schedule them during your highest-energy windows only

---

## KEY FORMULA REFERENCE

### Task Overdue Detection

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Done",
    prop("Status") != "Won't Do"
  ),
  true,
  false
)
```

### Brain Dump Staleness

```
if(
  and(
    not(prop("Processed")),
    prop("Days in Inbox") > 3
  ),
  true,
  false
)
```

Note: 3 days, not 7. ADHD inboxes decay faster — if you haven't processed something in 3 days, it needs forced attention or deletion.

### Days Open (Tasks)

```
if(
  prop("Status") == "Done",
  dateBetween(prop("Completed Date"), prop("Created"), "days"),
  dateBetween(now(), prop("Created"), "days")
)
```

Tracks how long tasks have been sitting. Tasks open 14+ days are likely stuck — either break them down, delegate them, or move to "Won't Do."

---

## PROCESSING THE BRAIN DUMP

Do this daily (under 10 minutes) or every other day:

### Step 1: Open "Dump Zone" view

### Step 2: For each unprocessed item, decide:
- **Task?** Create an entry in Task Board with Energy Required, Time Estimate, and First Step. Mark inbox item Processed.
- **Someday?** Set Destination = Someday, mark Processed. (You'll review these monthly.)
- **Reference?** Save it wherever you keep references. Mark Processed.
- **Nothing?** Delete it or mark Processed. Most brain dump items are just noise — and that's fine. Capturing them cleared mental RAM.

### Step 3: Check "Stale" view
- Anything 3+ days old: decide NOW. 2-second rule — if you can't decide in 2 seconds, delete it. It wasn't important enough to remember, which means it's not important enough to do.

---

## DOPAMINE MENU USAGE

### When to Use It:
- Between tasks (transition breaks)
- When you feel the urge to doom-scroll
- After completing something difficult (intentional reward)
- During low-energy periods when you can't work but need stimulation
- When waiting for something and boredom hits

### Pre-Built Categories to Start:

**Physical (2-15 min):** Stretch, walk around block, dance to one song, jumping jacks, cold water on face
**Creative (5-30 min):** Doodle, play instrument, rearrange desk, take photos, write haiku
**Sensory (2-10 min):** Essential oils, textured object, cold drink, sun on face, loud music with headphones
**Learning (5-15 min):** Watch one YouTube video on a topic, read one article, practice flashcards, listen to podcast clip
**Social (5-30 min):** Text a friend, voice memo someone, call family, browse community Discord
**Nature (5-30 min):** Step outside, watch birds, tend plants, sit in sun, walk barefoot on grass

---

## QUICK-START GUIDE

### Step 1 — Brain Dump Everything (15 minutes)

- Open the **Brain Dump Inbox**
- Set a 15-minute timer
- Write EVERYTHING in your head — tasks, worries, ideas, things you keep forgetting, random thoughts
- Don't organize. Don't judge. Just dump.
- This is the single most important step. It clears mental RAM immediately.

### Step 2 — Process the Dump (10 minutes)

- Go through each item using the Processing workflow above
- Move real tasks to the Task Board
- Delete noise (most of it will be noise — that's normal and fine)
- Mark everything Processed

### Step 3 — Set Up Your Task Board (10 minutes)

- Open the **Task Board** and review the tasks you moved from Brain Dump
- For each task, set:
  - Energy Required (be honest — not aspirational)
  - Time Estimate (double your first guess — ADHD underestimates time)
  - First Step (the absolute smallest possible starting action)
  - Dopamine Rating (how boring/interesting is this?)
- Don't worry about due dates unless there's a REAL external deadline

### Step 4 — Build Your Dopamine Menu (10 minutes)

- Open the **Dopamine Menu** database
- Add 10-15 activities you genuinely enjoy that take 2-30 minutes
- Categorize them by Time Required and Energy Cost
- Mark 3-5 as Favorites for quick access
- This becomes your go-to alternative to phone scrolling

### Step 5 — Start Using the System (daily)

**Every morning (3 minutes):**

- Open the Dashboard
- Check your energy level honestly
- Look at the matching energy column on the Task Board
- Pick ONE task. Just one. Start with the First Step.

**Throughout the day:**

- Brain dump whenever a thought intrudes (keep Inbox open in a tab)
- After completing a task, check one item from your Dopamine Menu
- If you notice hyperfocus happening, let it run but log the session after

**Every evening (2 minutes):**

- Process any brain dump items from today
- Note: what energy level were you today? Were your estimates accurate?

### Step 6 — Track Hyperfocus (ongoing)

- After every hyperfocus episode (planned or accidental), log it
- After 10+ entries, review patterns: What triggers flow? What time of day? What activities?
- Use this data to schedule your most important work during natural flow windows

### Pro Tips

- "Won't Do" is a valid status and you should use it without guilt. Dropping tasks that don't matter protects your limited executive function for tasks that do.
- Double every time estimate. ADHD brains have time blindness — if you think it'll take 30 minutes, budget 60. This prevents the spiral of "I'm always behind."
- The First Step field is your most powerful tool. Task initiation is the hardest part of ADHD. Making the first step so small it's almost embarrassing ("open the document") removes the activation energy barrier.
- Never put more than 3 tasks on your "today" list. Ambitious lists create shame spirals. Three completions is a great day.
- Body doubling works even if the other person is doing something completely different. The presence of another human doing focused work activates mirror neurons and reduces initiation friction.
- Your Dopamine Menu prevents destructive dopamine habits (doom-scrolling, impulse buying, binge-eating) by giving you pre-approved alternatives that satisfy the craving without the crash.
- Review your Done list every Friday. ADHD brains forget accomplishments instantly. Seeing everything you completed this week counteracts the "I never get anything done" narrative.
- Track Actual Time vs. Time Estimate on completed tasks. After 20+ entries, you'll develop a calibration multiplier that makes future planning realistic instead of fictional.
