# Client CRM & Pipeline Tracker — Notion Template

> Duplicate this page into your Notion workspace to get started. All four databases are pre-linked and all formulas are pre-built. Read the Quick-Start Guide at the bottom before entering real data — it will save you time.

---

## DATABASES

---

### 1. Contacts

**Purpose:** Master record for every person in your professional network — prospects, active clients, past clients, partners, and referral sources.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Full Name | Title | First and last name |
| Company | Relation | → Companies database |
| Company Name | Rollup | Name from linked Company record |
| Job Title | Text | Role at their organization |
| Email | Email | Primary contact email |
| Phone | Phone | Mobile or direct line |
| LinkedIn | URL | Profile URL for quick access |
| Website | URL | Personal or company site |
| Contact Type | Select | Prospect / Active Client / Past Client / Partner / Referral Source / Vendor |
| Lead Source | Select | Referral / Cold Outreach / Inbound / Social Media / Event / Conference / Website |
| Lead Score | Select | Hot / Warm / Cold / Unqualified |
| Relationship Strength | Select | Strong / Good / Weak / New |
| Status | Select | Active / Nurturing / Inactive / Do Not Contact |
| Tags | Multi-select | Agency / Enterprise / SMB / Decision Maker / Champion / Budget Holder / Technical / Executive |
| Budget Range | Select | Under $1K / $1K–$5K / $5K–$20K / $20K–$50K / $50K+ / Unknown |
| Time Zone | Select | ET / CT / MT / PT / GMT / CET / AEST / Other |
| Preferred Contact Method | Select | Email / Phone / LinkedIn / Video Call / Text |
| Notes | Text | Relationship context, personal details worth remembering, preferences |
| Last Contacted | Rollup | Max of Date from linked Activities |
| Days Since Contact | Formula | `if(empty(prop("Last Contacted")), "Never", format(dateBetween(now(), prop("Last Contacted"), "days")) + " days ago")` |
| Open Deals | Rollup | Count of linked Deals where Stage is not Closed Won or Closed Lost |
| Total Deal Value | Rollup | Sum of Deal Value from linked Deals |
| Won Deals | Rollup | Count of linked Deals where Stage = Closed Won |
| Total Activities | Rollup | Count of linked Activities |
| Contact Since | Date | When you first made contact |
| Birthday | Date | Optional — useful for relationship maintenance |
| Referred By | Relation | → Contacts database (self-referential) |
| Linked Deals | Relation | → Deals database |
| Linked Activities | Relation | → Activities database |
| Do Not Email | Checkbox | Flag to exclude from bulk outreach |

**Views:**

- **All Contacts** — Table, sorted by Full Name ascending
- **Active Clients** — Filter: Contact Type = Active Client, sorted by Last Contacted ascending (oldest first)
- **Hot Prospects** — Filter: Lead Score = Hot, sorted by Total Deal Value descending
- **Needs Outreach** — Filter: Days Since Contact > 30, Status = Active or Nurturing (use a formula filter)
- **By Company** — Table, grouped by Company Name
- **Contact Cards** — Gallery view, grouped by Contact Type
- **Referral Network** — Filter: Lead Source = Referral, sorted by Won Deals descending

---

### 2. Companies

**Purpose:** Organization-level records linking all contacts and deals at a single account. Essential when selling to businesses with multiple stakeholders.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Company Name | Title | Legal or trading name |
| Industry | Select | Technology / Marketing / Finance / Healthcare / Legal / Real Estate / Education / E-commerce / Non-profit / Media / Manufacturing / Consulting / Other |
| Company Size | Select | 1 (Solo) / 2–10 / 11–50 / 51–200 / 201–500 / 500+ |
| Annual Revenue | Select | Under $100K / $100K–$1M / $1M–$10M / $10M–$50M / $50M+ / Unknown |
| Website | URL | Company website |
| LinkedIn | URL | Company LinkedIn page |
| HQ Location | Text | City, State/Country |
| Time Zone | Select | ET / CT / MT / PT / GMT / CET / AEST / Other |
| Account Status | Select | Prospect / Active Client / Past Client / Partner / At Risk / Churned |
| Account Tier | Select | Strategic / Key / Standard / Small |
| Primary Contact | Relation | → Contacts database (the main decision-maker) |
| All Contacts | Rollup | Count of linked Contacts |
| Open Deals | Rollup | Count of linked Deals where Stage is not Closed Won or Closed Lost |
| Total Pipeline Value | Rollup | Sum of Deal Value from all linked Deals that are not Closed Lost |
| Total Won Revenue | Rollup | Sum of Deal Value from linked Deals where Stage = Closed Won |
| Last Activity | Rollup | Max of Date from linked Activities (via Contacts) |
| Contract Start | Date | When your engagement began |
| Contract Renewal | Date | Next renewal or review date |
| Account Notes | Text | Key account context, history, and strategic notes |
| Tags | Multi-select | Enterprise / Agency / Startup / Nonprofit / Retainer / Seasonal |
| Linked Contacts | Relation | → Contacts database |
| Linked Deals | Relation | → Deals database |

**Views:**

- **All Companies** — Table, sorted by Account Status then Company Name
- **Active Clients** — Filter: Account Status = Active Client, sorted by Total Won Revenue descending
- **Prospects** — Filter: Account Status = Prospect, sorted by Total Pipeline Value descending
- **Renewals Coming Up** — Filter: Contract Renewal is within 60 days, sorted by Contract Renewal ascending
- **By Industry** — Table, grouped by Industry
- **At Risk** — Filter: Account Status = At Risk
- **Company Cards** — Gallery view, grouped by Account Tier

---

### 3. Deals / Pipeline

**Purpose:** Every potential or active revenue opportunity, moving through your pipeline from first qualification to close. This is the operational center of your CRM.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Deal Name | Title | Clear, specific name — e.g. "Acme Corp — Brand Redesign" |
| Contact | Relation | → Contacts database (primary decision-maker) |
| Contact Name | Rollup | From Contact relation |
| Company | Relation | → Companies database |
| Company Name | Rollup | From Company relation |
| Stage | Select | Lead / Qualified / Proposal Sent / Negotiation / Closed Won / Closed Lost / On Hold |
| Deal Value | Number (USD) | Expected total contract value |
| Probability % | Number | Likelihood of closing (0–100) |
| Weighted Value | Formula | `round(prop("Deal Value") * (prop("Probability %") / 100))` |
| Deal Type | Select | New Business / Expansion / Renewal / Retainer / Project / Referral |
| Service Type | Select | Strategy / Design / Development / Writing / Marketing / Consulting / Retainer / Other |
| Open Date | Date | When this deal entered the pipeline |
| Expected Close | Date | Target close or start date |
| Actual Close | Date | When the deal was actually won or lost |
| Days in Stage | Formula | `dateBetween(now(), prop("Open Date"), "days")` |
| Days Until Close | Formula | `if(empty(prop("Expected Close")), "No date set", format(dateBetween(prop("Expected Close"), now(), "days")) + " days")` |
| Next Action | Text | What specifically needs to happen next |
| Next Action Date | Date | When that action needs to happen |
| Overdue | Formula | `if(and(not(empty(prop("Next Action Date"))), prop("Next Action Date") < now(), prop("Stage") != "Closed Won", prop("Stage") != "Closed Lost"), true, false)` |
| Deal Source | Select | Referral / Inbound / Cold Outreach / Event / Social Media / Partner / Existing Client |
| Competitor | Text | Known competitors being evaluated |
| Why Won / Lost | Text | Post-close notes on what determined the outcome |
| Proposal Sent Date | Date | |
| Contract Sent Date | Date | |
| Contract Signed | Checkbox | |
| Deposit Received | Checkbox | |
| Total Activities | Rollup | Count of linked Activities |
| Last Activity Date | Rollup | Max of Date from linked Activities |
| Deal Notes | Text | Full context, objections, key discussion points |
| Tags | Multi-select | Urgent / High Value / Complex / Fast Close / Strategic |
| Linked Activities | Relation | → Activities database |

**Views:**

- **Pipeline Board** — Kanban, grouped by Stage (default view — the main working view)
- **All Deals** — Table, sorted by Expected Close ascending
- **Needs Follow-Up** — Filter: Overdue = true, sorted by Next Action Date ascending
- **Hot Deals** — Filter: Stage is Qualified or Proposal Sent or Negotiation, sorted by Deal Value descending
- **Closed Won** — Filter: Stage = Closed Won, sorted by Actual Close descending
- **Closed Lost** — Filter: Stage = Closed Lost (for win/loss analysis)
- **Pipeline Forecast** — Table, showing Deal Name, Stage, Deal Value, Weighted Value, Expected Close — sorted by Expected Close
- **On Hold** — Filter: Stage = On Hold
- **By Company** — Table, grouped by Company Name

---

### 4. Activities / Touchpoints

**Purpose:** A complete log of every interaction with every contact. Calls, emails, meetings, LinkedIn messages, proposal deliveries, check-ins — every touchpoint recorded so you have full relationship history and never lose track of what was said or promised.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Activity Title | Title | Brief summary — e.g. "Discovery call — Acme Corp" |
| Date | Date | Date the activity occurred (include time for meetings) |
| Activity Type | Select | Email / Call / Video Meeting / In-Person Meeting / LinkedIn Message / Proposal Sent / Contract Sent / Demo / Check-In / Follow-Up / Note / Task |
| Direction | Select | Outbound (you initiated) / Inbound (they initiated) |
| Contact | Relation | → Contacts database |
| Contact Name | Rollup | From Contact relation |
| Company | Rollup | Via Contact → Company |
| Deal | Relation | → Deals database |
| Deal Name | Rollup | From Deal relation |
| Duration (mins) | Number | Length of call or meeting in minutes |
| Outcome | Select | Positive / Neutral / Negative / No Response / Meeting Booked / Proposal Requested / Deal Advanced / Objection Raised / Decision Pending |
| Summary | Text | What was discussed, what was decided, any commitments made |
| Follow-Up Required | Checkbox | Does this activity require a follow-up action? |
| Follow-Up Date | Date | When to follow up |
| Follow-Up Done | Checkbox | Mark complete when follow-up is completed |
| Follow-Up Overdue | Formula | `if(and(prop("Follow-Up Required"), not(prop("Follow-Up Done")), not(empty(prop("Follow-Up Date"))), prop("Follow-Up Date") < now()), true, false)` |
| Created By | Person | Useful for small teams — who logged this entry |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Internal Notes | Text | Private notes not shared with clients |

**Views:**

- **All Activities** — Table, sorted by Date descending (full chronological log)
- **This Week** — Filter: Date is this week, sorted by Date descending
- **Follow-Ups Due** — Filter: Follow-Up Required = true AND Follow-Up Done = false, sorted by Follow-Up Date ascending
- **Overdue Follow-Ups** — Filter: Follow-Up Overdue = true (urgent attention view)
- **By Contact** — Table, grouped by Contact Name, sorted by Date descending within groups
- **By Deal** — Table, grouped by Deal Name
- **Calls & Meetings** — Filter: Activity Type = Call or Video Meeting or In-Person Meeting
- **By Month** — Table, grouped by Month (for reviewing activity volume over time)
- **Recent Inbound** — Filter: Direction = Inbound, sorted by Date descending

---

## DASHBOARD

> Create this as the top-level Notion page. Pin it to your sidebar. It pulls from all four databases using linked database views. Check it every morning as your daily CRM briefing.

### Dashboard Layout

```
┌────────────────────────────────────────────────────────────────┐
│  CRM COMMAND CENTER                          April 2026        │
├────────────────┬───────────────┬──────────────┬───────────────┤
│  Pipeline      │  Weighted     │  Open Deals  │  Follow-Ups   │
│  $48,500       │  $27,200      │     9        │  3 overdue    │
├────────────────┴───────────────┴──────────────┴───────────────┤
│  PIPELINE BOARD                                                │
│  [Linked view → Deals, Board grouped by Stage]                 │
│                                                                │
│  Lead        Qualified    Proposal    Negotiation   Closed Won │
│  ─────────   ─────────    ────────    ───────────   ──────────│
│  Deal card   Deal card    Deal card   Deal card     Deal card  │
│  Deal card   Deal card    Deal card                Deal card  │
│  Deal card                                                     │
├────────────────────────────────────────────────────────────────┤
│  NEEDS FOLLOW-UP (Overdue actions)                             │
│  [Linked view → Deals, filter: Overdue = true]                 │
├─────────────────────────────┬──────────────────────────────────┤
│  RECENT ACTIVITY            │  FOLLOW-UPS DUE                  │
│  [Linked view → Activities, │  [Linked view → Activities,      │
│   sorted by Date desc,      │   filter: Follow-Up Required,    │
│   limit 10]                 │   not done, sorted by date]      │
├─────────────────────────────┴──────────────────────────────────┤
│  HOT PROSPECTS                                                 │
│  [Linked view → Contacts, filter: Lead Score = Hot]            │
├────────────────────────────────────────────────────────────────┤
│  ACTIVE CLIENTS                                                │
│  [Linked view → Companies, filter: Status = Active Client]     │
└────────────────────────────────────────────────────────────────┘
```

### Dashboard Summary Stats (Add as Notion callout blocks at the top)

Create four callout blocks side by side using a 4-column layout:

- **Total Pipeline** — Link to a filtered Deals view (exclude Closed Lost), note the sum of Deal Value
- **Weighted Pipeline** — Sum of Weighted Value across all open deals
- **Deals This Month** — Count of Deals where Actual Close is this month and Stage = Closed Won
- **Overdue Follow-Ups** — Count from Activities view where Follow-Up Overdue = true

---

## KEY FORMULA REFERENCE

### Weighted Deal Value
Multiplies the deal's dollar value by its close probability to give a realistic forecast figure. A $10,000 deal at 50% probability contributes $5,000 to your weighted pipeline.

```
round(prop("Deal Value") * (prop("Probability %") / 100))
```

### Overdue Deal Detection (Deals database)
Flags any deal where the Next Action Date has passed but the deal is still open. Drives the "Needs Follow-Up" view that should be your first check every morning.

```
if(
  and(
    not(empty(prop("Next Action Date"))),
    prop("Next Action Date") < now(),
    prop("Stage") != "Closed Won",
    prop("Stage") != "Closed Lost"
  ),
  true,
  false
)
```

### Days Since Contact (Contacts database)
Calculates how long it has been since you logged any activity with a contact. Used to surface relationships going cold.

```
if(
  empty(prop("Last Contacted")),
  "Never contacted",
  format(dateBetween(now(), prop("Last Contacted"), "days")) + " days ago"
)
```

### Follow-Up Overdue (Activities database)
Identifies activity log entries where a follow-up was required, hasn't been marked done, and the due date has passed. Drives the "Overdue Follow-Ups" view.

```
if(
  and(
    prop("Follow-Up Required"),
    not(prop("Follow-Up Done")),
    not(empty(prop("Follow-Up Date"))),
    prop("Follow-Up Date") < now()
  ),
  true,
  false
)
```

### Days Until Close (Deals database)
Shows how many days remain until the expected close date, or flags if no date is set. Sort the Pipeline Forecast view by this property to prioritize near-term closes.

```
if(
  empty(prop("Expected Close")),
  "No date set",
  format(dateBetween(prop("Expected Close"), now(), "days")) + " days"
)
```

### Win Rate (manual calculation using views)
Create a Deals view filtered to Stage = Closed Won and note the count. Create a second view filtered to Stage = Closed Won OR Closed Lost. Divide Won by Total Closed to get your win rate. Review monthly.

### Pipeline Velocity (use in weekly reviews)
Total Pipeline Value / Average Days to Close = estimated revenue per day. As you accumulate closed deals, note your average sales cycle length and use it to set more accurate Expected Close dates.

---

## QUICK-START GUIDE

### Step 1 — Add Your Companies
- Open the **Companies** database and add the organizations you currently work with or are actively pursuing
- Fill in Industry, Company Size, and Account Status for each
- You don't need every field — Company Name and Account Status are enough to get started

### Step 2 — Add Your Contacts
- Open the **Contacts** database and add the people you're actively in conversation with
- Link each contact to their Company record using the Company relation property
- Set Contact Type (Prospect, Active Client, etc.) and Lead Score for anyone in your pipeline
- Add existing clients first, then active prospects

### Step 3 — Build Your Pipeline
- Open the **Deals** database and add one entry for every active opportunity
- Name each deal clearly: "[Company] — [Service]" (e.g., "Greenfield Agency — Website Redesign")
- Link each deal to its Contact and Company
- Set the Stage, Deal Value, Probability %, and Expected Close date
- Write the Next Action and set a Next Action Date — this is critical for the follow-up system to work

### Step 4 — Log Past and Current Activities
- Open the **Activities** database and start logging recent touchpoints
- Work backwards — add your last interaction with each active deal first
- Set Follow-Up Required and Follow-Up Date for anything that needs action
- Going forward, log every call, email, and meeting as it happens

### Step 5 — Set Up Your Dashboard
- Create a new Notion page titled "CRM Command Center"
- Add linked database views for each of the four databases using the views listed in the dashboard section above
- Add four callout blocks at the top as your quick-stats summary
- Pin this page to your Notion sidebar so it's one click away every morning

### Step 6 — Establish Your Daily and Weekly Rhythms

**Every morning (5 minutes):**
- Open the Dashboard
- Check "Needs Follow-Up" in the Deals database — complete any overdue next actions
- Check "Follow-Ups Due" in the Activities database — respond to anything flagged

**Every Friday (15 minutes):**
- Review the Pipeline Board — move any deals that advanced during the week
- Update Next Action and Next Action Date for every open deal
- Log any activities you didn't capture during the week
- Check the "Needs Outreach" view in Contacts — re-engage anyone you haven't contacted in 30+ days

**Monthly:**
- Review Closed Won and Closed Lost deals and fill in the "Why Won / Lost" field
- Calculate your win rate and average deal size
- Check "Contract Renewal" dates in Companies — any clients coming up for renewal in 60 days?

### Pro Tips

- Keep deal names consistent: "[Company] — [Service Type]" so the Pipeline Board is scannable at a glance
- Log activities immediately or they won't happen — keep the Activities database open in a browser tab
- The Probability % field is most valuable when you're honest: a deal where the client hasn't responded in two weeks is not 80%
- Use the "Why Won / Lost" field on every closed deal — after 20+ entries you'll see patterns that sharpen your qualification
- For retainer clients, create a recurring deal entry and duplicate it each renewal period to maintain historical pipeline data
- When a deal is lost, change Stage to Closed Lost but do not delete the record — lost deals are your best data source for improving your pitch
- Add a "Check-In" activity entry for every active client once a month even if nothing specific happened — it keeps the relationship timeline accurate and prompts proactive outreach
