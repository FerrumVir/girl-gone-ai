# Interior Design Client Manager — Notion Template

> Duplicate this page into your Notion workspace to get started. All six databases are pre-linked with budget formulas, timeline tracking, and client management workflows built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Clients

**Purpose:** Master record for every client — contact details, project history, preferences, and communication log. One entry per client (household or business), linked to all their projects and invoices.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Client Name | Title | Full name or household name (e.g., "Sarah & James Miller") |
| Email | Email | Primary contact email |
| Phone | Phone | Best contact number |
| Address | Text | Property/project address |
| City | Text | City for project location |
| Status | Select | Inquiry / Active / On Hold / Completed / Past Client / Referral Pending |
| Client Type | Select | Residential / Commercial / Staging / Vacation Rental / Model Home |
| Source | Select | Referral / Instagram / Website / Houzz / Word of Mouth / Magazine / Event / Other |
| Referred By | Text | Who sent them your way |
| Budget Range | Select | Under $5K / $5K-$15K / $15K-$50K / $50K-$100K / $100K-$250K / $250K+ |
| Design Style | Multi-select | Modern / Traditional / Transitional / Mid-Century / Scandinavian / Bohemian / Industrial / Coastal / Farmhouse / Minimalist / Maximalist / Art Deco / Eclectic |
| Color Preferences | Text | Colors they love and hate |
| Lifestyle Notes | Text | Pets, kids, entertaining frequency, WFH needs, mobility considerations |
| Communication Preference | Select | Email / Text / Phone / Marco Polo / WhatsApp |
| Response Speed | Select | Same Day / 24 Hours / 2-3 Days / Slow |
| Decision Style | Select | Decisive / Collaborative / Needs Hand-Holding / Indecisive / Committee |
| Contract Signed | Checkbox | Has the contract been signed? |
| Contract Date | Date | When contract was signed |
| Total Project Value | Rollup | Sum of Total Budget from linked Projects |
| Total Spent | Rollup | Sum of Actual Spend from linked Projects |
| Active Projects | Rollup | Count of linked Projects where Status = Active |
| Completed Projects | Rollup | Count of linked Projects where Status = Completed |
| Linked Projects | Relation | -> Projects/Rooms database |
| Notes | Text | Personal details, gift preferences, relationship notes |
| Anniversary | Date | Move-in date or project completion (for follow-up) |
| Last Contact | Date | Most recent communication |
| Follow-Up Date | Date | When to reach out next |
| Tags | Multi-select | VIP / High Maintenance / Dream Client / Referral Machine / Photographer-Ready / Social Media OK |

**Views:**

- **All Clients** — Table, sorted by Client Name
- **Active Clients** — Filter: Status = Active, sorted by Last Contact ascending
- **Pipeline** — Filter: Status = Inquiry (potential new projects)
- **By Budget** — Table, grouped by Budget Range
- **By Style** — Table, grouped by Design Style
- **Follow-Up Due** — Filter: Follow-Up Date <= today
- **Referral Sources** — Table showing Source and Referred By
- **Past Clients** — Filter: Status = Past Client (for referral outreach)
- **Client Cards** — Gallery view with Client Name, Status, Active Projects

---

### 2. Projects / Rooms

**Purpose:** Each room or space being designed. A single client may have multiple projects (living room, master bedroom, kitchen). Tracks scope, budget, timeline, and links to mood boards and product sourcing.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Project Name | Title | "[Client] — [Room/Space]" (e.g., "Miller — Primary Bedroom") |
| Client | Relation | -> Clients database |
| Client Name | Rollup | From Client relation |
| Room/Space | Select | Living Room / Dining Room / Kitchen / Primary Bedroom / Guest Bedroom / Kids Room / Bathroom / Home Office / Nursery / Outdoor / Entryway / Hallway / Basement / Whole Home / Commercial Space |
| Status | Select | Concept / Design Development / Sourcing / Ordering / Installation / Punch List / Completed / On Hold |
| Phase | Select | Phase 1 / Phase 2 / Phase 3 (for phased projects) |
| Start Date | Date | Project kick-off date |
| Target Completion | Date | Expected finish |
| Actual Completion | Date | When it was done |
| Days Remaining | Formula | `if(prop("Status") == "Completed", "Done", if(empty(prop("Target Completion")), "No date", format(dateBetween(prop("Target Completion"), now(), "days")) + " days"))` |
| Total Budget | Number (USD) | Approved budget for this room |
| Actual Spend | Number (USD) | Running total spent |
| Budget Remaining | Formula | `prop("Total Budget") - prop("Actual Spend")` |
| Budget Status | Formula | `if(prop("Total Budget") == 0, "No budget set", if(prop("Actual Spend") / prop("Total Budget") > 0.9, "Over/Near Limit!", if(prop("Actual Spend") / prop("Total Budget") > 0.75, "Watch Closely", "On Track")))` |
| Budget Used % | Formula | `if(prop("Total Budget") == 0, 0, round(prop("Actual Spend") / prop("Total Budget") * 100))` |
| Design Fee | Number (USD) | Your fee for this project |
| Fee Type | Select | Flat Fee / Hourly / Cost-Plus % / Hybrid |
| Markup % | Number | Standard markup on furnishings |
| Estimated Markup Revenue | Formula | `round(prop("Actual Spend") * prop("Markup %") / 100)` |
| Mood Board | Relation | -> Mood Boards database |
| Linked Products | Relation | -> Product Sourcing database |
| Product Count | Rollup | Count of Linked Products |
| Ordered Count | Rollup | Count of Linked Products where Status = Ordered |
| Received Count | Rollup | Count of Linked Products where Status = Received |
| Sourcing Progress | Formula | `if(prop("Product Count") == 0, "No products", format(prop("Received Count")) + "/" + format(prop("Product Count")) + " received")` |
| Linked Timeline | Relation | -> Timeline database |
| Priority | Select | High / Medium / Low |
| Style Direction | Text | Design concept summary for this room |
| Key Measurements | Text | Room dimensions, window sizes, ceiling height |
| Special Considerations | Text | Structural limitations, existing pieces to keep, etc. |
| Tags | Multi-select | Photography Scheduled / Client Favorite / Award Submission / Portfolio Piece |

**Views:**

- **All Projects** — Table, sorted by Status then Client Name
- **By Status** — Board, grouped by Status (main working view)
- **Active by Client** — Table, grouped by Client Name, filtered to Status != Completed
- **Budget Alerts** — Filter: Budget Status = "Over/Near Limit!" or "Watch Closely"
- **Timeline** — Timeline view, Start Date to Target Completion
- **Sourcing Status** — Table showing Sourcing Progress for each project
- **Completed** — Filter: Status = Completed, sorted by Actual Completion descending
- **By Room Type** — Table, grouped by Room/Space
- **Revenue** — Table showing Design Fee + Estimated Markup Revenue per project

---

### 3. Mood Boards

**Purpose:** Visual inspiration and design direction for each project. Stores images, color palettes, texture references, and concept notes. Shareable with clients for approval.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Board Name | Title | "[Client] — [Room] Mood Board" |
| Project | Relation | -> Projects/Rooms database |
| Client | Rollup | Via Project -> Client |
| Status | Select | Draft / Presented / Approved / Revised / Rejected |
| Version | Number | Board iteration number |
| Style | Multi-select | Modern / Traditional / Transitional / Mid-Century / Scandinavian / Bohemian / Industrial / Coastal / Minimalist |
| Color Palette | Text | Primary, secondary, and accent colors with hex codes |
| Materials | Multi-select | Wood / Marble / Brass / Chrome / Velvet / Linen / Leather / Concrete / Terrazzo / Rattan / Glass / Ceramic |
| Mood/Feeling | Text | 3-5 adjectives describing the desired atmosphere |
| Inspiration Images | Files & media | Upload mood board images, textures, reference photos |
| Reference Links | URL | Pinterest boards, designer portfolios, product links |
| Client Feedback | Text | Notes from presentation — what they loved, what to change |
| Presented Date | Date | When shown to client |
| Approved Date | Date | When client signed off |
| Notes | Text | Design rationale, alternatives considered |

**Views:**

- **All Boards** — Gallery view with Inspiration Images
- **By Project** — Table, grouped by Project
- **Pending Approval** — Filter: Status = Presented
- **Approved** — Filter: Status = Approved
- **Drafts** — Filter: Status = Draft

---

### 4. Product Sourcing

**Purpose:** Every item being sourced for every project — furniture, lighting, textiles, accessories, hardware. Tracks vendor, pricing, lead times, order status, and delivery. This is the operational heart of your purchasing workflow.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Product Name | Title | Specific product name and finish/color |
| Project | Relation | -> Projects/Rooms database |
| Client | Rollup | Via Project -> Client |
| Category | Select | Furniture / Lighting / Rug / Textile / Art / Accessories / Hardware / Plumbing / Tile / Wallpaper / Window Treatment / Outdoor |
| Vendor | Text | Supplier or showroom name |
| Vendor Contact | Text | Sales rep name and email |
| SKU/Item # | Text | Vendor's product identifier |
| Product URL | URL | Link to product page |
| Product Image | Files & media | Photo or rendering |
| Retail Price | Number (USD) | MSRP |
| Trade/Net Price | Number (USD) | Your cost (if trade pricing) |
| Client Price | Formula | `if(prop("Trade/Net Price") == 0, prop("Retail Price"), round(prop("Trade/Net Price") * (1 + prop("Markup Applied") / 100)))` |
| Markup Applied | Number | Markup percentage for this item |
| Margin | Formula | `if(prop("Client Price") == 0, 0, round((prop("Client Price") - prop("Trade/Net Price")) / prop("Client Price") * 100))` |
| Quantity | Number | How many needed |
| Total Cost | Formula | `prop("Client Price") * prop("Quantity")` |
| Status | Select | Considering / Approved / Ordered / Shipped / Received / Installed / Returned / Discontinued |
| Order Date | Date | When ordered |
| Lead Time | Text | Expected lead time (e.g., "6-8 weeks") |
| Expected Delivery | Date | Anticipated arrival date |
| Actual Delivery | Date | When it actually arrived |
| Delivery Delayed | Formula | `if(and(not(empty(prop("Expected Delivery"))), prop("Expected Delivery") < now(), prop("Status") != "Received", prop("Status") != "Installed"), true, false)` |
| Tracking # | Text | Shipping tracking number |
| Condition on Arrival | Select | Perfect / Minor Issue / Damaged / Wrong Item |
| Installed | Checkbox | Has been placed/installed in the space |
| Notes | Text | Dimensions, COM details, custom specifications |
| Alternative | Text | Backup option if primary is unavailable |
| Sample Status | Select | Not Requested / Requested / Received / Approved / Returned |
| Tags | Multi-select | Custom Order / Quick Ship / Final Sale / Fragile / White Glove / COM / Oversized |

**Views:**

- **All Products** — Table, sorted by Project then Category
- **By Project** — Table, grouped by Project
- **Order Tracker** — Filter: Status = Ordered or Shipped, sorted by Expected Delivery
- **Delivery Delays** — Filter: Delivery Delayed = true
- **Needs Ordering** — Filter: Status = Approved (approved but not yet ordered)
- **By Category** — Table, grouped by Category
- **By Vendor** — Table, grouped by Vendor
- **Pending Samples** — Filter: Sample Status = Requested
- **Budget Summary** — Table showing Total Cost per project (sum by project)
- **Considering** — Filter: Status = Considering (options being evaluated)
- **Installed** — Filter: Installed = true

---

### 5. Budget Tracker

**Purpose:** Detailed budget breakdown by category for each project. Tracks estimates, actuals, and variances. Prevents cost overruns by surfacing variances before they become problems.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Line Item | Title | Budget category or specific item |
| Project | Relation | -> Projects/Rooms database |
| Client | Rollup | Via Project -> Client |
| Category | Select | Furniture / Lighting / Rugs / Window Treatments / Art & Accessories / Hardware / Labor / Contractor / Paint / Wallpaper / Tile / Plumbing / Electrical / Custom Millwork / Shipping / Tax / Contingency |
| Estimated | Number (USD) | Budgeted amount |
| Actual | Number (USD) | Amount spent |
| Variance | Formula | `prop("Estimated") - prop("Actual")` |
| Variance % | Formula | `if(prop("Estimated") == 0, 0, round((prop("Actual") - prop("Estimated")) / prop("Estimated") * 100))` |
| Status | Formula | `if(prop("Variance") < 0, "Over Budget", if(prop("Variance") == 0, "On Budget", "Under Budget"))` |
| Alert | Formula | `if(prop("Variance %") > 15, "OVER 15%+ — needs discussion", if(prop("Variance %") > 5, "Slightly over — monitor", "OK"))` |
| Paid | Checkbox | Has this been invoiced/paid? |
| Payment Date | Date | When payment was made |
| Invoice # | Text | Reference number |
| Notes | Text | Context, approval notes, change orders |

**Views:**

- **By Project** — Table, grouped by Project, showing Estimated, Actual, Variance
- **Over Budget** — Filter: Status = "Over Budget"
- **Alerts** — Filter: Alert contains "OVER" or "Slightly over"
- **By Category** — Table, grouped by Category (across all projects)
- **Unpaid** — Filter: Paid = false AND Actual > 0
- **Summary** — Table showing totals by Project

---

### 6. Timeline / Milestones

**Purpose:** Project timeline with milestones, deadlines, and dependencies. Gives you and the client visibility into what's happening when, and surfaces delays before they cascade.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Milestone | Title | Clear deliverable or event name |
| Project | Relation | -> Projects/Rooms database |
| Client | Rollup | Via Project -> Client |
| Phase | Select | Design / Sourcing / Ordering / Fabrication / Delivery / Installation / Styling / Photography |
| Status | Select | Upcoming / In Progress / Completed / Delayed / Blocked |
| Start Date | Date | When this phase begins |
| Due Date | Date | Target completion |
| Completed Date | Date | Actual completion |
| Overdue | Formula | `if(and(not(empty(prop("Due Date"))), prop("Due Date") < now(), prop("Status") != "Completed"), true, false)` |
| Days Until Due | Formula | `if(prop("Status") == "Completed", "Done", if(empty(prop("Due Date")), "No date", format(dateBetween(prop("Due Date"), now(), "days")) + " days"))` |
| Depends On | Relation | -> Timeline (self-referential for dependencies) |
| Dependency Met | Rollup | All linked Depends On where Status = Completed |
| Blocked | Formula | `if(and(not(empty(prop("Depends On"))), prop("Dependency Met") == false), true, false)` |
| Owner | Select | Designer / Client / Contractor / Vendor / Installer |
| Notes | Text | Details, next steps, blockers |
| Client Visible | Checkbox | Show this to the client? |

**Views:**

- **Timeline** — Timeline view by Start Date to Due Date (main project view)
- **By Project** — Table, grouped by Project
- **Overdue** — Filter: Overdue = true
- **This Week** — Filter: Due Date is this week
- **By Phase** — Table, grouped by Phase
- **Blocked** — Filter: Blocked = true or Status = Blocked
- **Client View** — Filter: Client Visible = true (share this with clients)
- **By Owner** — Table, grouped by Owner

---

## DASHBOARD

> Create this as the top-level page. Open it every morning to see all active projects, upcoming deadlines, pending orders, and client communication needs at a glance.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  DESIGN STUDIO HQ                                May 2026         |
+----------------+--------------+----------------+-----------------+
|  Active        |  Products    |  Deliveries    |  Budget          |
|  Projects: 4  |  On Order: 12|  This Week: 3  |  Alerts: 1      |
+----------------+--------------+----------------+-----------------+
|                                                                    |
|  ACTIVE PROJECTS BY STATUS                                        |
|  [Linked view -> Projects, Board grouped by Status]               |
|                                                                    |
+----------------------------------+-------------------------------+
|  THIS WEEK'S MILESTONES          |  DELIVERY TRACKING            |
|  [Linked view -> Timeline,       |  [Linked view -> Products,    |
|   Due Date this week]            |   Status = Ordered/Shipped,   |
|                                  |   sorted by Expected Delivery]|
+----------------------------------+-------------------------------+
|  BUDGET ALERTS                   |  CLIENT FOLLOW-UPS            |
|  [Linked view -> Budget Tracker, |  [Linked view -> Clients,     |
|   Alert != "OK"]                 |   Follow-Up Date <= today]    |
+----------------------------------+-------------------------------+
|  PENDING APPROVALS                                                |
|  [Linked view -> Mood Boards, Status = Presented]                 |
|  [Linked view -> Products, Status = Considering]                  |
+------------------------------------------------------------------+
```

---

## KEY FORMULA REFERENCE

### Budget Status (Projects)

```
if(
  prop("Total Budget") == 0,
  "No budget set",
  if(
    prop("Actual Spend") / prop("Total Budget") > 0.9,
    "Over/Near Limit!",
    if(
      prop("Actual Spend") / prop("Total Budget") > 0.75,
      "Watch Closely",
      "On Track"
    )
  )
)
```

### Client Price with Markup (Products)

```
if(
  prop("Trade/Net Price") == 0,
  prop("Retail Price"),
  round(prop("Trade/Net Price") * (1 + prop("Markup Applied") / 100))
)
```

### Margin Calculation (Products)

```
if(
  prop("Client Price") == 0,
  0,
  round((prop("Client Price") - prop("Trade/Net Price")) / prop("Client Price") * 100)
)
```

### Budget Variance Alert

```
if(
  prop("Variance %") > 15,
  "OVER 15%+ — needs discussion",
  if(
    prop("Variance %") > 5,
    "Slightly over — monitor",
    "OK"
  )
)
```

### Delivery Delay Detection

```
if(
  and(
    not(empty(prop("Expected Delivery"))),
    prop("Expected Delivery") < now(),
    prop("Status") != "Received",
    prop("Status") != "Installed"
  ),
  true,
  false
)
```

### Sourcing Progress (Projects)

```
format(prop("Received Count")) + "/" + format(prop("Product Count")) + " received"
```

### Estimated Markup Revenue

```
round(prop("Actual Spend") * prop("Markup %") / 100)
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Clients (10 minutes)

- Open the **Clients** database
- Add all active clients and any hot inquiries
- Set Status, Client Type, Budget Range, and Design Style for each
- Add contact details and Communication Preference
- Write Lifestyle Notes (pets, kids, entertaining — this informs design decisions)

### Step 2 — Create Projects for Each Room (10 minutes)

- Open the **Projects/Rooms** database
- Add one entry per room/space being designed for each client
- Link to the Client record
- Set Status, Total Budget, Start Date, and Target Completion
- Add Key Measurements and Style Direction

### Step 3 — Build Mood Boards (ongoing)

- For each active project, create a **Mood Board** entry
- Upload inspiration images, set Color Palette and Materials
- Present to client and update Status to Presented
- Record Client Feedback after presentation
- Iterate until Approved

### Step 4 — Start Product Sourcing (ongoing)

- As you source items, add them to **Product Sourcing**
- Link each product to its Project
- Set Trade/Net Price, Markup, and Quantity
- Move through statuses: Considering -> Approved -> Ordered -> Shipped -> Received -> Installed
- Update Expected Delivery dates from vendors

### Step 5 — Set Up Budgets (per project)

- Open **Budget Tracker** and add line items for each project
- Standard categories: Furniture, Lighting, Rugs, Art, Hardware, Labor, Shipping, Contingency
- Set Estimated amounts based on client's approved budget allocation
- Update Actual as purchases are made
- Watch the Alerts view for variances

### Step 6 — Create Your Timeline (per project)

- Open **Timeline** and add milestones for each project
- Standard phases: Concept Approval, Sourcing Complete, Orders Placed, Delivery Window, Installation Week, Styling, Photography
- Set dependencies where relevant (Installation depends on all Deliveries)
- Share the "Client View" filtered timeline with your client

### Step 7 — Build Your Dashboard

- Create the top-level page following the Dashboard Layout
- Pin to sidebar for daily use

### Pro Tips

- Always set Budget Contingency at 10-15% of total project budget. Overages happen — shipping surprises, discontinued items requiring upgrades, client add-ons. Having a contingency prevents awkward conversations.
- Update product Status immediately when you get shipping notifications. The Delivery Tracking view only works if data is current.
- Use the Follow-Up Date on Clients to schedule quarterly check-ins with past clients. Past clients are your best source of referrals and repeat business.
- The "Decision Style" property on Clients saves sanity. If a client is Indecisive, present only 2 options (not 5). If they're Decisive, send one strong recommendation with a backup.
- Take 5 minutes every Friday to update timeline milestones. Delays cascade — catching a 1-week slip early prevents a 4-week delay at installation.
- The Markup % and Margin formulas let you see your actual revenue per product. Use this data to evaluate which vendors and categories are most profitable.
- Use Tags on Products ("Final Sale", "Custom Order") to prevent returns on non-returnable items. Flag these during client presentations.
