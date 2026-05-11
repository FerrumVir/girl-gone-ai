# CRM for Solopreneurs — Notion Template

> Duplicate this page into your Notion workspace to get started. All four databases are pre-linked with relations and rollups. Pipeline formulas and follow-up automation are pre-built. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Contacts

**Purpose:** Master record for every person in your network — leads, active clients, past clients, referral sources, and collaborators. One entry per person, linked to all their deals and interactions.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Name | Title | First and last name |
| Email | Email | Primary contact email |
| Phone | Phone | Mobile or direct line |
| Company | Text | Their business or organization |
| Role | Text | Job title or role |
| Website | URL | Personal or company site |
| LinkedIn | URL | Profile URL |
| Contact Type | Select | Lead / Prospect / Active Client / Past Client / Referral Source / Partner / Vendor |
| Lead Source | Select | Referral / Cold Outreach / Inbound / Social Media / Event / Website / DM / Content |
| Lead Score | Select | Hot / Warm / Cold / Unqualified |
| Status | Select | Active / Nurturing / Inactive / Do Not Contact |
| Tags | Multi-select | Decision Maker / Budget Holder / Technical / Creative / Enterprise / SMB / Solo / VIP |
| Time Zone | Select | ET / CT / MT / PT / GMT / CET / AEST / Other |
| Preferred Contact | Select | Email / Phone / DM / Video Call / Text |
| Notes | Text | Relationship context, personal details, preferences |
| First Contact Date | Date | When you first connected |
| Birthday | Date | Optional — for relationship maintenance |
| Referred By | Relation | -> Contacts (self-referential) |
| Linked Deals | Relation | -> Deals/Pipeline database |
| Linked Interactions | Relation | -> Interactions database |
| Open Deals | Rollup | Count of linked Deals where Stage is not Won or Lost |
| Total Revenue | Rollup | Sum of Amount from linked Deals where Stage = Won |
| Last Interaction | Rollup | Max of Date from linked Interactions |
| Days Since Contact | Formula | `if(empty(prop("Last Interaction")), "Never", format(dateBetween(now(), prop("Last Interaction"), "days")) + " days")` |
| Interaction Count | Rollup | Count of linked Interactions |
| Needs Follow-Up | Formula | `if(and(prop("Status") != "Do Not Contact", prop("Status") != "Inactive", or(empty(prop("Last Interaction")), dateBetween(now(), prop("Last Interaction"), "days") > 14)), true, false)` |

**Views:**

- **All Contacts** — Table, sorted by Name ascending
- **Active Clients** — Filter: Contact Type = Active Client, sorted by Last Interaction descending
- **Hot Leads** — Filter: Lead Score = Hot, sorted by Days Since Contact ascending
- **Needs Follow-Up** — Filter: Needs Follow-Up = true, sorted by Last Interaction ascending
- **By Lead Source** — Table, grouped by Lead Source
- **Contact Cards** — Gallery view, grouped by Contact Type
- **Referral Network** — Filter: Lead Source = Referral, showing Referred By
- **Nurturing** — Filter: Status = Nurturing, sorted by Last Interaction ascending

---

### 2. Deals / Pipeline

**Purpose:** Every revenue opportunity from first inquiry to close. Each deal moves through your pipeline stages and carries probability weighting for revenue forecasting.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Deal Name | Title | "[Contact/Company] — [Service]" format |
| Contact | Relation | -> Contacts database |
| Contact Name | Rollup | Name from linked Contact |
| Stage | Select | Inquiry / Discovery / Proposal Sent / Negotiation / Won / Lost / On Hold |
| Amount | Number (USD) | Expected deal value |
| Probability % | Formula | `if(prop("Stage") == "Inquiry", 10, if(prop("Stage") == "Discovery", 25, if(prop("Stage") == "Proposal Sent", 50, if(prop("Stage") == "Negotiation", 75, if(prop("Stage") == "Won", 100, 0)))))` |
| Weighted Value | Formula | `round(prop("Amount") * prop("Probability %") / 100)` |
| Service Type | Select | Strategy / Design / Development / Writing / Coaching / Consulting / Retainer / Course / Custom |
| Deal Source | Select | Referral / Inbound / Cold Outreach / Content / Social Media / Existing Client / Partner |
| Open Date | Date | When the inquiry came in |
| Expected Close | Date | Target close date |
| Actual Close | Date | When deal was actually won or lost |
| Days in Pipeline | Formula | `dateBetween(now(), prop("Open Date"), "days")` |
| Days Until Close | Formula | `if(empty(prop("Expected Close")), "No date", if(prop("Expected Close") < now(), "Overdue", format(dateBetween(prop("Expected Close"), now(), "days")) + " days"))` |
| Stale Deal | Formula | `if(and(prop("Stage") != "Won", prop("Stage") != "Lost", prop("Days in Pipeline") > 30), true, false)` |
| Next Step | Text | Specific next action to advance this deal |
| Next Step Date | Date | When that action needs to happen |
| Overdue | Formula | `if(and(not(empty(prop("Next Step Date"))), prop("Next Step Date") < now(), prop("Stage") != "Won", prop("Stage") != "Lost"), true, false)` |
| Proposal URL | URL | Link to proposal document |
| Contract Signed | Checkbox | Has the client signed? |
| Deposit Received | Checkbox | First payment received? |
| Why Won/Lost | Text | Post-close analysis |
| Competitor | Text | Who else they were considering |
| Linked Interactions | Relation | -> Interactions database |
| Last Activity | Rollup | Max of Date from linked Interactions |
| Tags | Multi-select | High Value / Quick Close / Recurring / Complex / Referral |
| Notes | Text | Deal context, objections, negotiation points |

**Views:**

- **Pipeline Board** — Kanban, grouped by Stage (main working view)
- **All Deals** — Table, sorted by Expected Close ascending
- **Overdue Actions** — Filter: Overdue = true, sorted by Next Step Date ascending
- **Stale Deals** — Filter: Stale Deal = true (no movement in 30+ days)
- **Revenue Forecast** — Table showing Deal Name, Stage, Amount, Weighted Value, Expected Close
- **Won Deals** — Filter: Stage = Won, sorted by Actual Close descending
- **Lost Deals** — Filter: Stage = Lost, sorted by Actual Close descending
- **By Service Type** — Table, grouped by Service Type
- **This Month's Closes** — Filter: Expected Close is this month, Stage not Won/Lost
- **High Value** — Filter: Amount > $5000, sorted by Amount descending

---

### 3. Interactions

**Purpose:** Complete log of every touchpoint — calls, emails, meetings, DMs, proposals sent, check-ins. Gives you full relationship history and feeds the follow-up reminder system.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Summary | Title | Brief description — e.g., "Discovery call — discussed timeline" |
| Date | Date | When it happened (include time for meetings) |
| Type | Select | Email / Call / Video Call / In-Person / DM / Proposal Sent / Invoice Sent / Check-In / Follow-Up / Note |
| Direction | Select | Outbound / Inbound |
| Contact | Relation | -> Contacts database |
| Contact Name | Rollup | From Contact relation |
| Deal | Relation | -> Deals/Pipeline database |
| Deal Name | Rollup | From Deal relation |
| Duration (min) | Number | Length of call/meeting |
| Outcome | Select | Positive / Neutral / Negative / No Response / Meeting Booked / Deal Advanced / Objection / Decision Pending |
| Details | Text | What was discussed, commitments made, key points |
| Follow-Up Needed | Checkbox | Does this require follow-up? |
| Follow-Up Date | Date | When to follow up |
| Follow-Up Done | Checkbox | Mark complete when done |
| Follow-Up Overdue | Formula | `if(and(prop("Follow-Up Needed"), not(prop("Follow-Up Done")), not(empty(prop("Follow-Up Date"))), prop("Follow-Up Date") < now()), true, false)` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Week | Formula | `formatDate(prop("Date"), "W")` |

**Views:**

- **Recent Activity** — Table, sorted by Date descending (full chronological log)
- **This Week** — Filter: Date is this week, sorted by Date descending
- **Follow-Ups Due** — Filter: Follow-Up Needed = true AND Follow-Up Done = false, sorted by Follow-Up Date ascending
- **Overdue Follow-Ups** — Filter: Follow-Up Overdue = true
- **By Contact** — Table, grouped by Contact Name
- **By Deal** — Table, grouped by Deal Name
- **Outbound Activity** — Filter: Direction = Outbound, sorted by Date descending
- **By Month** — Table, grouped by Month

---

### 4. Tasks

**Purpose:** Action items generated from deals and interactions. Quick-capture task list tied to your CRM so nothing falls through the cracks between meetings.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Task | Title | Clear action statement |
| Status | Select | To Do / In Progress / Waiting / Done |
| Priority | Select | Urgent / High / Medium / Low |
| Due Date | Date | When it needs to be done |
| Contact | Relation | -> Contacts database |
| Deal | Relation | -> Deals/Pipeline database |
| Category | Select | Follow-Up / Proposal / Admin / Onboarding / Delivery / Invoicing / Research |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Done"), true, false)` |
| Days Until Due | Formula | `if(prop("Status") == "Done", "Complete", if(empty(prop("Due Date")), "No date", format(dateBetween(prop("Due Date"), now(), "days")) + " days"))` |
| Created | Created time | Auto-populated |
| Completed Date | Date | When marked done |
| Notes | Text | Additional context |

**Views:**

- **To Do** — Filter: Status != Done, sorted by Due Date ascending
- **Today** — Filter: Due Date = today, Status != Done
- **Overdue** — Filter: Overdue = true
- **By Priority** — Table, grouped by Priority, filtered to Status != Done
- **By Deal** — Table, grouped by Deal
- **Done This Week** — Filter: Status = Done AND Completed Date is this week
- **Waiting** — Filter: Status = Waiting

---

## DASHBOARD

> Create this as the top-level page. Open it every morning as your CRM daily briefing. It tells you exactly who to contact, which deals need attention, and how your pipeline is performing.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  SOLOPRENEUR CRM                                 May 2026         |
+----------------+--------------+---------------+------------------+
|  Pipeline      |  Weighted    |  Open Deals   |  Overdue         |
|  $32,500       |  $18,750     |    7          |  2 follow-ups    |
+----------------+--------------+---------------+------------------+
|                                                                    |
|  PIPELINE BOARD                                                   |
|  [Linked view -> Deals, Kanban grouped by Stage]                  |
|                                                                    |
|  Inquiry    Discovery   Proposal   Negotiation   Won              |
|  --------   ---------   --------   -----------   ----             |
|  Card       Card        Card       Card          Card             |
|  Card       Card        Card                     Card             |
|                                                                    |
+----------------------------------+-------------------------------+
|  OVERDUE FOLLOW-UPS              |  TASKS DUE TODAY              |
|  [Linked view -> Interactions,   |  [Linked view -> Tasks,       |
|   Follow-Up Overdue = true]      |   Due Date = today]           |
+----------------------------------+-------------------------------+
|  CONTACTS NEEDING OUTREACH       |  REVENUE THIS MONTH           |
|  [Linked view -> Contacts,       |  [Linked view -> Deals,       |
|   Needs Follow-Up = true,        |   Stage = Won, Actual Close   |
|   sorted by Days Since Contact]  |   this month]                 |
+----------------------------------+-------------------------------+
|  STALE DEALS (30+ days, no movement)                              |
|  [Linked view -> Deals, Stale Deal = true]                        |
+------------------------------------------------------------------+
```

### Summary Stats (callout blocks, 4-column layout)

- **Total Pipeline** — Sum of Amount across all open deals (Inquiry through Negotiation)
- **Weighted Pipeline** — Sum of Weighted Value across all open deals
- **Deals to Close This Month** — Count where Expected Close is this month
- **Won This Month** — Sum of Amount where Stage = Won and Actual Close is current month

---

## REVENUE FORECASTING SYSTEM

### Stage-Based Probability Formula

```
if(
  prop("Stage") == "Inquiry", 10,
  if(
    prop("Stage") == "Discovery", 25,
    if(
      prop("Stage") == "Proposal Sent", 50,
      if(
        prop("Stage") == "Negotiation", 75,
        if(
          prop("Stage") == "Won", 100,
          0
        )
      )
    )
  )
)
```

Each stage carries a default close probability. These are conservative starting points — adjust based on your actual conversion rates after 3 months of data.

### Weighted Value Calculation

```
round(prop("Amount") * prop("Probability %") / 100)
```

A $5,000 deal at Discovery (25%) contributes $1,250 to your weighted pipeline. This gives you a realistic monthly revenue projection by summing all weighted values.

### Monthly Revenue Forecast

Sum the Weighted Value column in the "Revenue Forecast" view, filtered to Expected Close = this month. Compare to your monthly income target to know whether you need more pipeline or can focus on delivery.

### Pipeline Velocity

After 3+ months of data:
```
Average Deal Size x Win Rate x Number of Open Deals / Average Sales Cycle (days)
= Revenue per day capacity
```

Track this quarterly to understand whether your pipeline is healthy or you need to generate more leads.

---

## FOLLOW-UP AUTOMATION

### Contact Needs Follow-Up Formula

```
if(
  and(
    prop("Status") != "Do Not Contact",
    prop("Status") != "Inactive",
    or(
      empty(prop("Last Interaction")),
      dateBetween(now(), prop("Last Interaction"), "days") > 14
    )
  ),
  true,
  false
)
```

Surfaces any active contact you haven't touched in 14+ days. Adjust the threshold (14) based on your sales cycle — shorter for hot leads, longer for nurturing relationships.

### Interaction Follow-Up Overdue

```
if(
  and(
    prop("Follow-Up Needed"),
    not(prop("Follow-Up Done")),
    not(empty(prop("Follow-Up Date"))),
    prop("Follow-Up Date") < now()
  ),
  true,
  false
)
```

### Deal Stale Detection

```
if(
  and(
    prop("Stage") != "Won",
    prop("Stage") != "Lost",
    prop("Days in Pipeline") > 30
  ),
  true,
  false
)
```

Deals sitting in your pipeline for 30+ days without advancing to the next stage get flagged. Either advance them, put them on hold, or mark them lost.

### Deal Next Step Overdue

```
if(
  and(
    not(empty(prop("Next Step Date"))),
    prop("Next Step Date") < now(),
    prop("Stage") != "Won",
    prop("Stage") != "Lost"
  ),
  true,
  false
)
```

---

## KEY FORMULA REFERENCE

### Days Since Contact

```
if(
  empty(prop("Last Interaction")),
  "Never",
  format(dateBetween(now(), prop("Last Interaction"), "days")) + " days"
)
```

### Days Until Close

```
if(
  empty(prop("Expected Close")),
  "No date",
  if(
    prop("Expected Close") < now(),
    "Overdue",
    format(dateBetween(prop("Expected Close"), now(), "days")) + " days"
  )
)
```

### Task Overdue

```
if(
  and(
    not(empty(prop("Due Date"))),
    prop("Due Date") < now(),
    prop("Status") != "Done"
  ),
  true,
  false
)
```

### Win Rate (manual calculation)

Create two filtered views:

- Won deals (Stage = Won) — note the count
- All closed deals (Stage = Won OR Lost) — note the count
- Win Rate = Won / Total Closed x 100

Review monthly. Anything below 30% means you need better qualification. Above 70% means you might be leaving money on the table by not pursuing larger or riskier deals.

---

## QUICK-START GUIDE

### Step 1 — Add Your Contacts (15 minutes)

- Open the **Contacts** database
- Add everyone you're currently in conversation with — active clients first, then prospects
- Set Contact Type and Lead Score for each
- Don't add your entire LinkedIn network — just people with active or potential revenue relationships

### Step 2 — Build Your Pipeline (10 minutes)

- Open the **Deals/Pipeline** database
- Add one entry for every active opportunity you're pursuing
- Format: "[Name/Company] — [Service]" (e.g., "Sarah Chen — Brand Strategy")
- Set Stage, Amount, and Expected Close for each
- Write the Next Step and set a Next Step Date — this drives your follow-up system

### Step 3 — Log Recent Interactions (10 minutes)

- Open the **Interactions** database
- Add your last 2-3 interactions with each active deal
- For anything requiring follow-up: check Follow-Up Needed and set Follow-Up Date
- Going forward, log every meaningful touchpoint as it happens

### Step 4 — Set Up Your Dashboard

- Create a new page titled "CRM"
- Add linked database views as described in the Dashboard Layout
- Add four callout blocks at the top for summary stats
- Pin to your Notion sidebar

### Step 5 — Daily Rhythm (5 minutes every morning)

- Open Dashboard
- Check **Overdue Follow-Ups** — complete or reschedule each one
- Check **Tasks Due Today** — handle or delegate
- Glance at **Pipeline Board** — does anything need advancing?

### Step 6 — Weekly Pipeline Review (10 minutes, Friday)

- Walk through every open deal on the Pipeline Board
- Update Stage for any that advanced
- Update Next Step and Next Step Date for every deal
- Check **Stale Deals** — either advance, pause, or close them
- Check **Contacts Needing Outreach** — send a quick check-in to anyone flagged
- Log any interactions you missed during the week

### Pro Tips

- Log interactions immediately after they happen. If you wait until Friday, you'll forget half of them and your data becomes unreliable.
- The "Why Won/Lost" field is your most valuable long-term asset. After 20+ closed deals, patterns emerge that completely change how you qualify and pitch.
- Keep deal names consistent: "[Name] — [Service]" makes the Pipeline Board scannable at a glance.
- Probability % is auto-calculated from Stage, but you can override it with a manual property if a deal feels stronger or weaker than its stage suggests.
- Don't over-engineer. If you're a solopreneur doing $5-15K/month, you don't need 47 properties on each contact. The defaults here are plenty — resist the urge to add more until you've used this for 60 days.
- Review your Lost Deals quarterly. You'll notice that most losses share 2-3 common factors. Fix those factors and your win rate improves without needing more leads.
- Use the Tasks database for CRM-related actions only. Don't turn it into a general to-do list or it'll get noisy fast.
