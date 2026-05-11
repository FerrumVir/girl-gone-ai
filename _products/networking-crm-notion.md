# Networking CRM — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with relationship scoring, follow-up automation, and event tracking already configured. Read the Quick-Start Guide at the bottom before importing your contacts.

---

## DATABASES

---

### 1. Contacts

**Purpose:** Master record for every person in your professional network. Not just people you need something from — everyone who matters to your career growth, industry knowledge, and mutual support system. Tracks relationship strength, communication history, and optimal follow-up timing.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Name | Title | Full name |
| Company | Text | Current employer or "Self-employed" / "Freelance" |
| Job Title | Text | Current role |
| Industry | Select | Tech / Finance / Marketing / Healthcare / Legal / Education / Media / Design / Consulting / Real Estate / Non-Profit / Government / Startup / VC/PE / Other |
| Email | Email | Primary email |
| Phone | Phone | Mobile or direct |
| LinkedIn | URL | Profile URL |
| Twitter/X | URL | Handle or profile URL |
| Website | URL | Personal site or portfolio |
| Location | Text | City, State/Country |
| Time Zone | Select | ET / CT / MT / PT / GMT / CET / JST / AEST / Other |
| How We Met | Text | Context of first interaction — e.g. "SaaStr 2025, sat next to each other at lunch" |
| Date Met | Date | When you first connected |
| Introduced By | Relation | → Contacts database (self-referential) |
| Relationship Type | Multi-select | Mentor / Mentee / Peer / Colleague / Former Colleague / Client / Prospect / Investor / Advisor / Industry Friend / Conference Contact / Online Connection / Vendor / Recruiter |
| Relationship Strength | Select | Strong (5) / Good (4) / Moderate (3) / Weak (2) / New (1) / Dormant (0) |
| Strength Score | Number | 0–5 numeric version for sorting and formulas |
| Status | Select | Active / Nurturing / Dormant / Lost Touch / Do Not Contact |
| Tags | Multi-select | Decision Maker / Connector / Expert / Hiring Manager / Speaker / Author / Investor / Potential Client / Potential Partner / Can Intro To |
| Interests | Text | Professional interests, hobbies, passions — conversation starters |
| Personal Notes | Text | Family details, preferences, achievements to congratulate — builds genuine rapport |
| Birthday | Date | Optional but powerful for relationship building |
| Value I Provide | Text | What can you specifically offer this person? |
| Value They Provide | Text | What have they offered or could they offer? |
| Preferred Contact Method | Select | Email / LinkedIn / Text / Phone / Twitter DM / In Person |
| Contact Frequency Goal | Select | Weekly / Bi-weekly / Monthly / Quarterly / Semi-annually / Annually / As Needed |
| Last Contacted | Date | When you last reached out or spoke |
| Days Since Contact | Formula | `if(empty(prop("Last Contacted")), "Never", format(dateBetween(now(), prop("Last Contacted"), "days")))` |
| Follow-Up Due | Formula | Based on Contact Frequency Goal, calculates if a follow-up is overdue |
| Needs Outreach | Formula | `if(and(prop("Status") != "Do Not Contact", prop("Status") != "Lost Touch", or(empty(prop("Last Contacted")), dateBetween(now(), prop("Last Contacted"), "days") > prop("Frequency Days"))), true, false)` |
| Frequency Days | Formula | Maps Contact Frequency Goal to days: Weekly=7, Bi-weekly=14, Monthly=30, Quarterly=90, Semi-annually=180, Annually=365 |
| Total Interactions | Rollup | Count of linked Interactions |
| Interactions This Year | Rollup | Count of linked Interactions where Date is this year |
| Mutual Connections | Relation | → Contacts database (self-referential for shared network) |
| Linked Interactions | Relation | → Interactions database |
| Linked Events | Relation | → Events database |
| Linked Opportunities | Relation | → Opportunities database |
| Photo | Files & Media | Profile photo for visual recognition |
| Notes | Text | General notes, context, relationship history |

**Views:**

- **All Contacts** — Table, sorted by Name ascending
- **Needs Outreach** — Filter: Needs Outreach = true, sorted by Days Since Contact descending (longest neglected first)
- **Strong Relationships** — Filter: Relationship Strength = Strong or Good
- **By Industry** — Table, grouped by Industry
- **By Relationship Type** — Table, grouped by Relationship Type
- **Contact Cards** — Gallery view showing Name, Company, Job Title, Relationship Strength, Last Contacted
- **New Connections** — Filter: Date Met is within 30 days (nurture these!)
- **Dormant** — Filter: Status = Dormant or Lost Touch (re-engage opportunities)
- **Mentors & Advisors** — Filter: Relationship Type contains Mentor or Advisor
- **Connectors** — Filter: Tags contains Connector (people who can intro you to others)
- **Birthday Calendar** — Calendar view by Birthday
- **Local Network** — Filter by Location for in-person meetup planning

---

### 2. Interactions

**Purpose:** Complete log of every meaningful interaction with every contact. Not just scheduled meetings — also includes random run-ins, helpful emails, content sharing, introductions made, and favors exchanged. This is the memory that makes you a great networker.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Interaction Title | Title | Brief summary — e.g. "Coffee chat re: career transition" |
| Contact | Relation | → Contacts database |
| Contact Name | Rollup | From Contact relation |
| Date | Date | When this interaction happened |
| Type | Select | Coffee/Lunch / Video Call / Phone Call / Email Thread / LinkedIn Message / DM / In-Person Event / Introduction Made / Favor Given / Favor Received / Content Shared / Comment/Engagement / Gift Sent / Referral Given / Referral Received |
| Direction | Select | I Initiated / They Initiated / Mutual / Passive (event attendance) |
| Duration (mins) | Number | For meetings/calls — how long |
| Location | Text | Where it happened (coffee shop, Zoom, conference, etc.) |
| Event | Relation | → Events database (if interaction occurred at an event) |
| Summary | Text | What was discussed, key points, context |
| Action Items | Text | What you committed to doing after this interaction |
| They Committed To | Text | What they said they would do |
| Value Exchanged | Select | I Helped Them / They Helped Me / Mutual Exchange / Relationship Building / Information Sharing |
| Follow-Up Required | Checkbox | Does this need a follow-up action? |
| Follow-Up Date | Date | When to follow up |
| Follow-Up Done | Checkbox | Completed? |
| Follow-Up Overdue | Formula | `if(and(prop("Follow-Up Required"), not(prop("Follow-Up Done")), not(empty(prop("Follow-Up Date"))), prop("Follow-Up Date") < now()), true, false)` |
| Mood/Energy | Select | Great Connection / Positive / Neutral / Awkward / Negative |
| Relationship Impact | Select | Strengthened / Maintained / Neutral / Weakened |
| Notes | Text | Additional context, personal details mentioned, topics to revisit |
| Tags | Multi-select | Strategic / Casual / Business Dev / Career / Learning / Mentorship / Social / Follow-Up Needed |

**Views:**

- **All Interactions** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week
- **Follow-Ups Due** — Filter: Follow-Up Required = true AND Follow-Up Done = false, sorted by Follow-Up Date ascending
- **Overdue Follow-Ups** — Filter: Follow-Up Overdue = true (urgent!)
- **By Contact** — Table, grouped by Contact Name
- **Introductions Made** — Filter: Type = Introduction Made
- **Favors Given** — Filter: Type = Favor Given or Referral Given (track your generosity)
- **Favors Received** — Filter: Type = Favor Received or Referral Received
- **By Month** — Table, grouped by month formula
- **Recent Inbound** — Filter: Direction = They Initiated, sorted by Date descending

---

### 3. Events

**Purpose:** Conferences, meetups, networking events, dinners, webinars, and any gathering where you meet or deepen relationships with contacts. Tracks who you met, follow-ups needed, and ROI of event attendance.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Event Name | Title | Full event name — e.g. "SaaStr Annual 2026" |
| Date | Date | Event date (use date range for multi-day events) |
| End Date | Date | For multi-day events |
| Type | Select | Conference / Meetup / Networking Event / Dinner / Webinar / Workshop / Happy Hour / Industry Event / Company Event / Private Gathering / Online Community Event |
| Location | Text | Venue, city, or "Virtual" |
| URL | URL | Event page or registration link |
| Status | Select | Interested / Registered / Attended / Cancelled / Skipped |
| Cost | Number (USD) | Registration, travel, and related costs |
| Organizer | Text | Who organized or hosted |
| My Role | Select | Attendee / Speaker / Panelist / Sponsor / Organizer / Volunteer |
| Goals | Text | What do you want to accomplish at this event? |
| People to Meet | Relation | → Contacts database (target connections) |
| People Met | Relation | → Contacts database (who you actually connected with) |
| New Contacts Made | Number | Count of brand-new connections |
| Interactions at Event | Rollup | Count of linked Interactions |
| Key Takeaways | Text | Main learnings, insights, trends observed |
| Follow-Up Actions | Text | What to do after the event (send emails, connect on LinkedIn, etc.) |
| Follow-Ups Completed | Checkbox | All post-event outreach done? |
| Business Cards Collected | Number | Physical or digital cards collected |
| ROI Notes | Text | Was this event worth it? Would you attend again? |
| Rating | Select | Excellent / Good / Average / Poor / Skip Next Time |
| Photos | Files & Media | Event photos, badge, booth pics |
| Linked Interactions | Relation | → Interactions database |
| Tags | Multi-select | Industry / Local / Paid / Free / Annual / First Time / VIP / Must Attend |
| Notes | Text | General event notes, logistics, tips for next time |

**Views:**

- **All Events** — Table, sorted by Date descending
- **Upcoming** — Filter: Date >= today AND Status = Interested or Registered, sorted by Date ascending
- **Past Events** — Filter: Date < today AND Status = Attended
- **Event Calendar** — Calendar view by Date
- **By Type** — Table, grouped by Type
- **Needs Follow-Up** — Filter: Status = Attended AND Follow-Ups Completed = false
- **High ROI** — Filter: Rating = Excellent or Good (prioritize these for next year)
- **Cost Tracker** — Table showing Event Name, Date, Cost, Rating, New Contacts Made (calculate cost per connection)
- **Speaking Opportunities** — Filter: My Role = Speaker or Panelist

---

### 4. Opportunities

**Purpose:** Track professional opportunities that arise from your network — job leads, collaborations, partnerships, speaking invitations, introductions requested, and business development leads. Connects the dots between relationships and tangible career/business outcomes.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Opportunity Name | Title | Clear description — e.g. "VP Marketing role at Stripe (via Sarah Chen)" |
| Type | Select | Job Lead / Collaboration / Partnership / Speaking Gig / Advisory Role / Freelance Project / Business Deal / Introduction Request / Mentorship / Investment / Board Seat / Media Feature |
| Source Contact | Relation | → Contacts database (who brought this to you) |
| Source Name | Rollup | From Source Contact |
| Related Contacts | Relation | → Contacts database (other people involved) |
| Status | Select | Identified / Exploring / Active / Negotiating / Won / Lost / Passed / On Hold |
| Priority | Select | High / Medium / Low |
| Potential Value | Text | Estimated financial or career value |
| Date Identified | Date | When this opportunity surfaced |
| Deadline | Date | If time-sensitive |
| Days Until Deadline | Formula | `if(empty(prop("Deadline")), "No deadline", format(dateBetween(prop("Deadline"), now(), "days")) + " days")` |
| Next Step | Text | What specifically needs to happen next |
| Next Step Date | Date | When to take that step |
| Overdue | Formula | `if(and(not(empty(prop("Next Step Date"))), prop("Next Step Date") < now(), prop("Status") != "Won", prop("Status") != "Lost", prop("Status") != "Passed"), true, false)` |
| Notes | Text | Full context, requirements, pros/cons |
| Outcome | Text | What happened — result and learnings |
| Linked Interactions | Relation | → Interactions database |
| Tags | Multi-select | Urgent / Warm Intro / Cold / Recurring / High Value / Quick Win / Long Shot |

**Views:**

- **All Opportunities** — Table, sorted by Date Identified descending
- **Active** — Filter: Status = Exploring or Active or Negotiating, sorted by Priority then Next Step Date
- **Pipeline Board** — Kanban grouped by Status
- **Needs Action** — Filter: Overdue = true
- **Won** — Filter: Status = Won (celebrate and analyze)
- **By Type** — Table, grouped by Type
- **By Source** — Table, grouped by Source Name (who generates the most opportunities for you?)
- **High Priority** — Filter: Priority = High

---

### 5. Outreach Templates

**Purpose:** Pre-written message templates for common networking scenarios. Saves time and ensures consistent, thoughtful communication. Customize per contact but use these as starting frameworks.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Template Name | Title | Scenario name — e.g. "Post-Conference Follow-Up" |
| Category | Select | Initial Outreach / Follow-Up / Thank You / Introduction Request / Congratulations / Reconnection / Event Invite / Value Offer / Ask / Holiday/Birthday |
| Channel | Select | Email / LinkedIn / Text / DM / Handwritten Note |
| Subject Line | Text | For emails — suggested subject |
| Message Body | Text | Full template with [BRACKETS] for personalization |
| When to Use | Text | Specific scenario this template fits |
| Personalization Tips | Text | How to customize this for different contacts |
| Tone | Select | Professional / Casual / Warm / Brief / Detailed |
| Response Rate | Select | High / Medium / Low / Untested |
| Times Used | Number | Track how often you use this |
| Last Used | Date | When you last sent this template |
| Example | Text | A real example of this template filled in |
| Notes | Text | Tips, variations, what to avoid |
| Tags | Multi-select | Quick / Requires Research / High Touch / Scalable / Seasonal |

**Views:**

- **All Templates** — Table, sorted by Category then Template Name
- **By Category** — Table, grouped by Category
- **By Channel** — Table, grouped by Channel
- **High Response Rate** — Filter: Response Rate = High
- **Most Used** — Table, sorted by Times Used descending
- **Quick Templates** — Filter: Tags contains Quick (for rapid outreach)

---

## RELATIONSHIP STRENGTH SCORING

> This system provides an objective measure of how strong each relationship is, helping you identify which connections need nurturing and which are thriving.

### Scoring Criteria (0–5 Scale)

| Score | Label | Criteria |
|---|---|---|
| 5 | Strong | Regular contact (monthly+), mutual value exchange, would respond to a favor request within 24h, met in person multiple times |
| 4 | Good | Contact every 1–3 months, have exchanged favors, strong mutual awareness of each other's work |
| 3 | Moderate | Contact every 3–6 months, positive interactions when in touch, would respond to a message within a week |
| 2 | Weak | Contact once or twice a year, cordial but not deep, might need context reminder |
| 1 | New | Just met, had one interaction, no established rapport yet |
| 0 | Dormant | Haven't spoken in 6+ months, relationship has cooled, needs intentional re-engagement |

### Strength Decay Rules

Relationship strength naturally decays without maintenance:

- If Days Since Contact > Frequency Days * 2 → reduce Strength Score by 1
- If Days Since Contact > Frequency Days * 4 → set Status to Dormant
- Exception: Mentor/Advisor relationships decay slower (multiply thresholds by 1.5)

### Re-engagement Thresholds

| Current Strength | Days Without Contact | Action Needed |
|---|---|---|
| Strong (5) | 45+ days | Quick check-in |
| Good (4) | 60+ days | Share relevant content or news |
| Moderate (3) | 90+ days | Personal outreach with specific value |
| Weak (2) | 120+ days | Meaningful re-connection attempt |
| Dormant (0) | 180+ days | Full re-introduction with context |

---

## NETWORKING DASHBOARD

```
┌────────────────────────────────────────────────────────────────┐
│  NETWORKING COMMAND CENTER                                       │
├────────────────┬───────────────┬──────────────┬────────────────┤
│  Total Network │  Strong/Good  │  Need Outreach│  This Month   │
│     247        │     43        │     18        │  12 interactions│
├────────────────┴───────────────┴──────────────┴────────────────┤
│  NEEDS OUTREACH (sorted by days since contact)                  │
│  [Linked view → Contacts, filter: Needs Outreach = true]        │
├────────────────────────────────────────────────────────────────┤
│  OVERDUE FOLLOW-UPS                                             │
│  [Linked view → Interactions, filter: Follow-Up Overdue = true] │
├─────────────────────────────────┬──────────────────────────────┤
│  UPCOMING EVENTS                │  ACTIVE OPPORTUNITIES         │
│  [Linked view → Events,        │  [Linked view → Opportunities,│
│   filter: upcoming]             │   filter: Status = Active]    │
├─────────────────────────────────┴──────────────────────────────┤
│  RECENT INTERACTIONS                                            │
│  [Linked view → Interactions, sorted by Date desc, limit 15]    │
├────────────────────────────────────────────────────────────────┤
│  NEW CONNECTIONS (last 30 days)                                  │
│  [Linked view → Contacts, filter: Date Met within 30 days]      │
└────────────────────────────────────────────────────────────────┘
```

---

## AUTOMATIONS / FORMULAS

### Needs Outreach Detection

Identifies contacts who are overdue for communication based on their frequency goal.

```
if(
  and(
    prop("Status") != "Do Not Contact",
    prop("Status") != "Lost Touch",
    or(
      empty(prop("Last Contacted")),
      dateBetween(now(), prop("Last Contacted"), "days") > prop("Frequency Days")
    )
  ),
  true,
  false
)
```

### Frequency Days Mapping

Converts the Contact Frequency Goal select into a numeric day value for calculations.

```
if(prop("Contact Frequency Goal") == "Weekly", 7,
if(prop("Contact Frequency Goal") == "Bi-weekly", 14,
if(prop("Contact Frequency Goal") == "Monthly", 30,
if(prop("Contact Frequency Goal") == "Quarterly", 90,
if(prop("Contact Frequency Goal") == "Semi-annually", 180,
if(prop("Contact Frequency Goal") == "Annually", 365, 999))))))
```

### Follow-Up Overdue

Flags interactions with overdue follow-up actions.

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

### Days Since Contact

Human-readable time since last interaction.

```
if(
  empty(prop("Last Contacted")),
  "Never contacted",
  format(dateBetween(now(), prop("Last Contacted"), "days")) + " days"
)
```

### Opportunity Overdue

Flags opportunities where the next step date has passed.

```
if(
  and(
    not(empty(prop("Next Step Date"))),
    prop("Next Step Date") < now(),
    prop("Status") != "Won",
    prop("Status") != "Lost",
    prop("Status") != "Passed"
  ),
  true,
  false
)
```

### Event ROI Calculation

Cost per new contact made at each event (use in views).

```
if(
  prop("New Contacts Made") == 0,
  "No contacts made",
  "$" + format(round(prop("Cost") / prop("New Contacts Made")))
)
```

---

## QUICK-START GUIDE

### Step 1 — Import Your Existing Network

- Open the **Contacts** database and add your 20–30 most important professional connections first
- For each person: Name, Company, Job Title, How We Met, and Relationship Strength
- Don't try to add everyone at once — start with active relationships and expand over time
- Set Contact Frequency Goal based on how often you want to stay in touch

### Step 2 — Set Up Your Templates

- Open the **Outreach Templates** database and customize the pre-loaded templates
- At minimum, create templates for: Post-Event Follow-Up, Congratulations, Reconnection, and Introduction Request
- These save massive time when you need to reach out to 10 people after a conference

### Step 3 — Log Recent Interactions

- Open **Interactions** and add your last 2–3 interactions with each contact you added
- This populates the "Last Contacted" field and establishes baseline relationship data
- For each: Date, Type, Summary, and whether Follow-Up is required

### Step 4 — Add Upcoming Events

- Open **Events** and add any conferences, meetups, or networking events in your calendar
- Set Goals for each event (who do you want to meet? what do you want to learn?)
- Use People to Meet to identify target connections before attending

### Step 5 — Build Your Dashboard

- Create a new page called "Networking Hub"
- Add linked database views following the dashboard layout above
- The "Needs Outreach" view is your daily action driver
- Pin to your sidebar and check every Monday morning

### Step 6 — Establish Your Networking Rhythm

**Every Monday (10 minutes):**

- Review "Needs Outreach" — pick 3–5 people to contact this week
- Check "Follow-Ups Due" — complete any overdue actions
- Choose an outreach template, personalize it, and send

**After every interaction:**

- Log it in the Interactions database (takes 60 seconds)
- Update the contact's Last Contacted date
- Set Follow-Up Required and date if needed
- Adjust Relationship Strength if the interaction was particularly strengthening or if decay has happened

**Before every event:**

- Review the event page — who do you want to meet?
- Prep talking points using the Interests and Personal Notes fields on target contacts
- Set Goals for what you want to accomplish

**After every event:**

- Add all new contacts to the database within 24 hours (while you remember context)
- Log interactions with everyone you spoke to meaningfully
- Send follow-up messages within 48 hours (use your Post-Event Follow-Up template)
- Rate the event and write ROI Notes

**Monthly (15 minutes):**

- Review Relationship Strength scores — has anyone decayed?
- Check the "Dormant" view — is anyone worth re-engaging?
- Review Opportunities by Source — who consistently brings value to your network?
- Add any new contacts from the past month that you missed

### Pro Tips

- The #1 networking rule: give before you ask. Use the "Value I Provide" field to remind yourself what you can offer each contact
- Log even small interactions (liking a post, sharing an article) — they count toward maintaining the relationship
- Use the Introduced By field religiously — it helps you thank connectors and understand your network's structure
- Batch your outreach — set aside 30 minutes on Monday for all your weekly networking touches
- Personal Notes is your secret weapon — remembering someone's kid's name or their hobby creates genuine connection
- Quality over quantity: 50 strong relationships beat 500 LinkedIn connections. Focus on deepening, not just expanding
- After every conference, the follow-up is more valuable than the event itself. Block time the day after for outreach
- Set Contact Frequency Goal realistically — it's better to maintain 20 monthly contacts than to guilt yourself over 100
- Use the Opportunities database to track the tangible ROI of networking — it justifies the time investment and shows which relationships generate the most value
- Review the "Connectors" view when you need an introduction — these are the people whose networks you can tap into
