# Wedding Planning Dashboard — Complete Wedding Organizer — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Budget

**Purpose:** Track every wedding expense from estimated through final payment, with category-level and overall budget monitoring.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Expense Item | Title | Clear description (e.g., "Venue Rental — Ceremony + Reception") |
| Category | Select | Venue / Catering / Photography / Videography / Flowers & Decor / Music & Entertainment / Attire & Beauty / Stationery / Favors & Gifts / Transportation / Officiant / Wedding Planner / Rentals / Cake & Dessert / Rehearsal Dinner / Honeymoon / Miscellaneous |
| Vendor | Relation | → Vendors database |
| Vendor Name | Rollup | Vendor Name from Vendor relation |
| Estimated Cost | Number (USD) | Initial budget estimate |
| Actual Cost | Number (USD) | Final confirmed or paid amount |
| Variance | Formula | `prop("Actual Cost") - prop("Estimated Cost")` |
| Over/Under | Formula | `if(prop("Variance") > 0, "Over Budget", if(prop("Variance") < 0, "Under Budget", "On Budget"))` |
| Deposit Amount | Number (USD) | Deposit paid or due |
| Deposit Paid | Checkbox | Has the deposit been paid? |
| Deposit Date | Date | When deposit was/is due |
| Second Payment | Number (USD) | Interim payment if applicable |
| Second Payment Paid | Checkbox | |
| Final Payment Due | Number (USD) | Remaining balance |
| Final Payment Date | Date | When final payment is due |
| Final Payment Paid | Checkbox | |
| Total Paid | Formula | `(if(prop("Deposit Paid"), prop("Deposit Amount"), 0)) + (if(prop("Second Payment Paid"), prop("Second Payment"), 0)) + (if(prop("Final Payment Paid"), prop("Final Payment Due"), 0))` |
| Amount Remaining | Formula | `prop("Actual Cost") - prop("Total Paid")` |
| Payment Status | Formula | `if(prop("Amount Remaining") <= 0, "Paid in Full", if(prop("Total Paid") > 0, "Partially Paid", "Unpaid"))` |
| Priority | Select | Must-Have / Nice-to-Have / Splurge / Can Cut |
| Notes | Text | Contract details, negotiation notes, alternatives considered |
| Tags | Multi-select | Booked / Negotiating / Researching / Paid / Canceled |

**Views:**
- **All Expenses** — Table, sorted by Category then Expense Item
- **By Category** — Table, grouped by Category, showing subtotals
- **Payment Schedule** — Table, sorted by next upcoming payment date
- **Unpaid Items** — Filter: Payment Status != "Paid in Full"
- **Over Budget Items** — Filter: Over/Under = "Over Budget"
- **Budget Board** — Kanban, grouped by Priority
- **Summary** — Table showing Category, sum of Estimated, sum of Actual, sum of Total Paid, sum of Amount Remaining

---

### Budget Summary Section

**Overall Budget Tracking:**

| Metric | Formula |
|---|---|
| Total Budget | Enter your total wedding budget here (manual entry) |
| Total Estimated | `Sum of all Estimated Cost` |
| Total Actual | `Sum of all Actual Cost` |
| Total Paid | `Sum of all Total Paid` |
| Total Remaining | `Total Actual - Total Paid` |
| Budget vs Estimated | `Total Budget - Total Estimated` |
| Budget vs Actual | `Total Budget - Total Actual` |
| % of Budget Used | `round(Total Actual / Total Budget * 100)` |

**Recommended Budget Allocation (% of total):**

| Category | Suggested % | For $30,000 Budget |
|---|---|---|
| Venue | 30-35% | $9,000-$10,500 |
| Catering | 25-30% | $7,500-$9,000 |
| Photography | 10-12% | $3,000-$3,600 |
| Flowers & Decor | 8-10% | $2,400-$3,000 |
| Music & Entertainment | 5-8% | $1,500-$2,400 |
| Attire & Beauty | 5-8% | $1,500-$2,400 |
| Stationery | 2-3% | $600-$900 |
| All Other | 5-10% | $1,500-$3,000 |

---

### 2. Vendors

**Purpose:** Research, compare, book, and manage every vendor relationship from first contact through final payment.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Vendor Name | Title | Business or individual name |
| Category | Select | Venue / Caterer / Photographer / Videographer / Florist / DJ / Band / Officiant / Baker / Hair & Makeup / Planner / Coordinator / Rental Company / Transportation / Stationer / Tailor / Other |
| Contact Name | Text | Primary point of contact |
| Email | Email | Primary email |
| Phone | Phone | Primary phone |
| Website | URL | Vendor website |
| Instagram | URL | Social media for portfolio review |
| Status | Select | Researching / Contacted / Meeting Scheduled / Quote Received / Negotiating / Booked / Declined / Backup |
| Quote Amount | Number (USD) | Most recent quoted price |
| Contract Signed | Checkbox | Has the contract been signed? |
| Contract Date | Date | Date contract was signed |
| Contract Notes | Text | Key contract terms, cancellation policy, inclusions |
| Deposit Required | Number (USD) | |
| Deposit Due Date | Date | |
| Final Payment Due Date | Date | |
| Rating | Select | 5-Love / 4-Great / 3-Good / 2-Okay / 1-Pass |
| Review Notes | Text | Your impressions after meeting/tasting/consultation |
| Referral Source | Text | How you found them (friend, WeddingWire, venue recommendation) |
| Linked Budget Items | Relation | → Budget database |
| Tags | Multi-select | Top Choice / Backup / Friend Recommended / Award-Winning / Budget-Friendly |

**Views:**
- **All Vendors** — Table, sorted by Category then Vendor Name
- **By Category** — Table, grouped by Category
- **Booked Vendors** — Filter: Status = Booked
- **Vendor Board** — Kanban, grouped by Status
- **Need Follow-Up** — Filter: Status = Contacted OR Meeting Scheduled, sorted by oldest first
- **Vendor Cards** — Gallery view, showing name, category, rating, status
- **Contract Tracker** — Filter: Status = Booked, showing Contract Signed, Deposit info, Payment dates

---

### 3. Guests

**Purpose:** Complete guest list with RSVP tracking, meal preferences, seating assignments, and gift/thank-you tracking.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Guest Name | Title | Full name |
| Side | Select | Bride / Groom / Partner A / Partner B / Both / Mutual |
| Relationship | Select | Family / Friend / College / Work / Childhood / Neighbor / Other |
| Invited To | Multi-select | Ceremony / Reception / Rehearsal Dinner / Brunch / All Events |
| Address | Text | Mailing address for invitations |
| Email | Email | For digital communication |
| Phone | Phone | |
| Invitation Sent | Checkbox | Has the invitation been mailed/sent? |
| Invitation Sent Date | Date | |
| RSVP Status | Select | Awaiting / Attending / Declined / No Response |
| RSVP Date | Date | When they responded |
| Plus One | Checkbox | Are they bringing a plus-one? |
| Plus One Name | Text | Name of plus-one |
| Plus One Meal | Select | Chicken / Beef / Fish / Vegetarian / Vegan / Kids Meal / Other |
| Meal Choice | Select | Chicken / Beef / Fish / Vegetarian / Vegan / Kids Meal / Other |
| Dietary Restrictions | Text | Allergies, intolerances, special requirements |
| Table Number | Number | Assigned table |
| Table Name | Text | If using named tables instead of numbers |
| Age Group | Select | Adult / Teen / Child / Infant |
| Hotel Block | Checkbox | Using the hotel room block |
| Transportation Need | Checkbox | Needs shuttle or transportation |
| Gift Received | Text | Description of gift |
| Gift Date | Date | When gift was received |
| Thank You Sent | Checkbox | Has thank-you note been sent? |
| Thank You Date | Date | When thank-you was sent |
| Notes | Text | Dietary details, conflicts with other guests, special needs |
| Tags | Multi-select | VIP / Wedding Party / Speech / Out-of-Town / Needs Accessibility |

**Views:**
- **Full Guest List** — Table, sorted alphabetically
- **By Side** — Table, grouped by Side
- **RSVP Tracker** — Table, grouped by RSVP Status, showing counts
- **Attending** — Filter: RSVP Status = Attending
- **No Response** — Filter: RSVP Status = Awaiting OR No Response, sorted by Invitation Sent Date
- **Meal Count** — Table, grouped by Meal Choice (for caterer headcount)
- **Seating Chart** — Table, grouped by Table Number, sorted by Guest Name
- **Unassigned Seating** — Filter: RSVP Status = Attending AND Table Number is empty
- **Gift Tracker** — Table, showing Gift Received, Thank You Sent, sorted by Gift Date
- **Thank-Yous Needed** — Filter: Gift Received is not empty AND Thank You Sent = false
- **Wedding Party** — Filter: Tags contains Wedding Party

---

### Guest Summary Section

| Metric | Formula |
|---|---|
| Total Invited | Count of all guests |
| Invitations Sent | Count where Invitation Sent = true |
| Invitations Pending | Count where Invitation Sent = false |
| Attending | Count where RSVP Status = Attending |
| Declined | Count where RSVP Status = Declined |
| Awaiting Response | Count where RSVP Status = Awaiting or No Response |
| Response Rate | `round(Attending + Declined) / Total Invited * 100)` |
| Total Headcount | Attending + count of Plus Ones where RSVP = Attending |
| Chicken | Count where Meal Choice = Chicken |
| Beef | Count where Meal Choice = Beef |
| Fish | Count where Meal Choice = Fish |
| Vegetarian / Vegan | Count where Meal Choice = Vegetarian or Vegan |
| Kids Meals | Count where Meal Choice = Kids Meal |
| Tables Needed | `ceil(Total Headcount / 8)` (adjust 8 to your table capacity) |

---

### 4. Tasks

**Purpose:** Comprehensive wedding timeline with every planning task organized by phase, with assignees, due dates, and dependencies.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Task | Title | Clear, actionable description |
| Phase | Select | 12+ Months / 9-12 Months / 6-9 Months / 3-6 Months / 1-3 Months / 1 Month / 1 Week / Day-Of / Post-Wedding |
| Category | Select | Venue / Catering / Photography / Attire / Flowers / Music / Stationery / Guest List / Legal / Travel / Decor / Beauty / Other |
| Status | Select | Not Started / In Progress / Waiting / Complete / Skipped |
| Priority | Select | Critical / Important / Nice-to-Have |
| Assignee | Select | Partner A / Partner B / Both / MOH / Best Man / Planner / Vendor / Family |
| Due Date | Date | When this should be completed |
| Days Until Due | Formula | `dateBetween(prop("Due Date"), now(), "days")` |
| Urgency | Formula | `if(prop("Status") == "Complete", "Done", if(prop("Days Until Due") < 0, "OVERDUE", if(prop("Days Until Due") <= 7, "This Week", if(prop("Days Until Due") <= 30, "This Month", "Upcoming"))))` |
| Completed Date | Date | When actually completed |
| Notes | Text | Details, links, reminders |
| Linked Vendor | Relation | → Vendors database |
| Linked Budget | Relation | → Budget database |
| Dependencies | Text | What needs to happen first |
| Tags | Multi-select | Requires Appointment / Requires Payment / Requires Decision / Can Delegate |

**Pre-Loaded Tasks (80+):**

**12+ Months Out:**
- Set overall wedding budget
- Draft initial guest list
- Research and tour venues (5-8 visits)
- Book venue and sign contract
- Choose wedding date
- Start engagement photos
- Research wedding insurance
- Set up shared planning workspace (this template)
- Discuss wedding style and vision with partner
- Begin looking at wedding attire

**9-12 Months Out:**
- Book photographer
- Book videographer (if applicable)
- Book caterer / tasting appointments
- Book officiant
- Choose wedding party and ask them
- Research and book florist
- Research and book DJ or band
- Start dress/suit shopping
- Create wedding website
- Book hotel room block for guests

**6-9 Months Out:**
- Order invitations and stationery
- Book hair and makeup artist
- Book rehearsal dinner venue
- Plan honeymoon and book travel
- Register for gifts
- Book transportation (limo, shuttle, etc.)
- Schedule cake/dessert tasting
- Order wedding cake
- Plan ceremony details with officiant
- Begin writing vows (if personal vows)

**3-6 Months Out:**
- Send save-the-dates (if not already sent)
- Finalize guest list
- Order wedding attire (alterations timeline)
- Book rentals (tables, chairs, linens, tent)
- Plan rehearsal dinner menu and details
- Choose ceremony readings
- Apply for marriage license (check local timeline)
- Schedule dress fittings
- Plan welcome bags for out-of-town guests
- Confirm all vendor contracts and payments

**1-3 Months Out:**
- Send invitations (8 weeks before wedding)
- Finalize seating chart
- Write and submit song requests / do-not-play list
- Confirm final headcount with caterer
- Finalize timeline with photographer
- Schedule final dress fitting
- Plan bachelor/bachelorette parties
- Order favors
- Prepare toasts/speeches with wedding party
- Create day-of timeline
- Buy gifts for wedding party
- Arrange marriage license appointment

**1 Month Out:**
- Confirm all vendor arrival times and details
- Final dress fitting
- Break in wedding shoes
- Prepare emergency kit
- Finalize vows
- RSVP follow-up with non-respondents
- Submit final guest count to caterer
- Confirm rehearsal dinner details
- Prepare final vendor payments (checks, envelopes)
- Create seating chart cards / place cards

**1 Week Out:**
- Confirm timeline with all vendors (one final check)
- Pack for honeymoon
- Prepare day-of emergency bag
- Delegate day-of tasks to wedding party
- Rehearsal and rehearsal dinner
- Get a good night's sleep

**Day-Of:**
- Morning: Hair, makeup, getting ready
- Distribute vendor final payments and tips
- Ceremony
- Reception
- Enjoy your wedding

**Post-Wedding:**
- Send thank-you notes (within 3 months)
- Submit marriage license
- Name change paperwork (if applicable)
- Preserve wedding dress
- Review and tip vendors
- Order wedding album
- Submit vendor reviews online

**Views:**
- **Full Timeline** — Table, sorted by Phase then Due Date
- **By Phase** — Table, grouped by Phase
- **Task Board** — Kanban, grouped by Status
- **This Month** — Filter: Urgency = "This Month" or "This Week" or "OVERDUE"
- **Overdue** — Filter: Urgency = "OVERDUE"
- **By Assignee** — Table, grouped by Assignee
- **By Category** — Table, grouped by Category
- **Critical Path** — Filter: Priority = Critical, sorted by Due Date
- **Completed** — Filter: Status = Complete, sorted by Completed Date descending

---

### 5. Inspiration Board

**Purpose:** Save, organize, and reference every idea, photo, and aesthetic inspiration for your wedding vision.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Idea Name | Title | Descriptive name |
| Category | Select | Flowers / Decor / Dress / Suit / Cake / Table Setting / Venue Styling / Invitations / Color Palette / Hair / Makeup / Photography Style / Ceremony / Reception / Favors / Other |
| Image URL | URL | Link to Pinterest, Instagram, or uploaded image |
| Source | Text | Where you found it (Pinterest, magazine, wedding blog, Instagram) |
| Status | Select | Love It / Maybe / Passed / Using This |
| Color Palette | Multi-select | Sage / Blush / Ivory / Gold / Navy / Burgundy / Dusty Blue / Terracotta / Lavender / Black / White / Custom |
| Season | Select | Spring / Summer / Fall / Winter / Any |
| Vibe | Multi-select | Romantic / Rustic / Modern / Boho / Classic / Glamorous / Minimalist / Whimsical / Garden / Industrial |
| Estimated Cost | Number (USD) | What this might cost to execute |
| Notes | Text | Why you like it, how to adapt it, vendor who could do this |
| Linked Vendor | Relation | → Vendors database |
| Linked Budget | Relation | → Budget database |
| Partner A Opinion | Select | Love / Like / Neutral / Dislike |
| Partner B Opinion | Select | Love / Like / Neutral / Dislike |

**Views:**
- **All Inspiration** — Gallery view, sorted by Category
- **By Category** — Gallery, grouped by Category
- **Love It** — Filter: Status = "Love It" or "Using This"
- **Both Love** — Filter: Partner A Opinion = Love AND Partner B Opinion = Love
- **By Color** — Gallery, grouped by Color Palette
- **By Vibe** — Gallery, grouped by Vibe
- **Need to Discuss** — Filter: Partner A and Partner B opinions differ

---

## DASHBOARD

> Create this as a Notion page that serves as your wedding command center.

### Dashboard Layout

```
┌─────────────────────────────────────────────────────────────┐
│  WEDDING HQ — [Your Names]           [Wedding Date]         │
│                                      [X] Days to Go!        │
├───────────────┬───────────────┬──────────────┬──────────────┤
│  Budget       │  Budget       │  Guests      │  Tasks       │
│  Total        │  Remaining    │  Attending   │  Overdue     │
│  $28,500      │  $4,200       │  127         │  2           │
├───────────────┴───────────────┴──────────────┴──────────────┤
│  BUDGET SNAPSHOT                                            │
│  Total Budget: $32,000                                      │
│  Estimated:    $30,800  |  Actual: $28,500  |  Paid: $24,300│
│  Remaining to Pay: $4,200                                   │
│  [Progress bar: 89% of budget allocated]                    │
├─────────────────────────────────────────────────────────────┤
│  UPCOMING TASKS                                             │
│  [Linked view → Tasks, filter: This Month, sorted by Due]   │
├─────────────────────────────────────────────────────────────┤
│  RSVP PROGRESS                                              │
│  Attending: 127  |  Declined: 18  |  Awaiting: 23          │
│  Response Rate: 86%                                         │
│  [Linked view → Guests, filter: No Response]                │
├─────────────────────────────────────────────────────────────┤
│  VENDOR STATUS                                              │
│  [Linked view → Vendors, filter: Status = Booked]           │
│  Next payment due: [Florist — $800 — May 15]                │
├─────────────────────────────────────────────────────────────┤
│  UPCOMING PAYMENTS                                          │
│  [Linked view → Budget, filter: unpaid items, sorted by     │
│   next payment date]                                        │
├─────────────────────────────────────────────────────────────┤
│  SEATING CHART PROGRESS                                     │
│  Assigned: 104  |  Unassigned: 23  |  Tables Filled: 13/17  │
│  [Linked view → Guests, filter: Attending + no table]       │
├─────────────────────────────────────────────────────────────┤
│  INSPIRATION FAVORITES                                      │
│  [Linked view → Inspiration, filter: Status = Love It]      │
└─────────────────────────────────────────────────────────────┘
```

---

## SEATING CHART PLANNING TOOL

### How to Use the Seating Chart

1. Filter the Guests database to show only "Attending" guests
2. Create tables by assigning Table Numbers (1, 2, 3...) or Table Names ("Rose Table," "Oak Table")
3. Use the "Seating Chart" view (grouped by Table Number) to see who is at each table
4. Use the "Unassigned Seating" view to see who still needs a table
5. Check the Dietary Restrictions and Notes fields when grouping tables to avoid seating conflicts

### Seating Strategy Tips

- **Start with must-seats:** Immediate family, wedding party, and VIPs go first
- **Group by relationship:** College friends together, work friends together, family branches together
- **Check dietary restrictions per table** to ensure the caterer can serve efficiently
- **Flag conflicts** in the Notes field: "Do not seat near [person]"
- **Keep out-of-town guests with other out-of-town guests** so they have conversation partners
- **Head table or sweetheart table:** Decide early — this affects how many tables you need
- **Kids table:** Consider whether children sit with parents or separately

### Table Capacity Calculator

```
Total Attending Guests:  ___
Table Capacity:          ___ (typically 8 or 10)
Tables Needed:           = ceil(Total Guests / Table Capacity)
Add 1-2 buffer tables for last-minute changes
```

---

## KEY FORMULA REFERENCE

**Budget Variance:**
```
prop("Actual Cost") - prop("Estimated Cost")
```
Positive = over budget. Negative = under budget.

**Total Paid per Item:**
```
(if(prop("Deposit Paid"), prop("Deposit Amount"), 0)) +
(if(prop("Second Payment Paid"), prop("Second Payment"), 0)) +
(if(prop("Final Payment Paid"), prop("Final Payment Due"), 0))
```

**Payment Status:**
```
if(
  prop("Amount Remaining") <= 0,
  "Paid in Full",
  if(prop("Total Paid") > 0, "Partially Paid", "Unpaid")
)
```

**Task Urgency:**
```
if(prop("Status") == "Complete", "Done",
  if(prop("Days Until Due") < 0, "OVERDUE",
    if(prop("Days Until Due") <= 7, "This Week",
      if(prop("Days Until Due") <= 30, "This Month", "Upcoming")
    )
  )
)
```

**Countdown to Wedding:**
```
dateBetween(prop("Wedding Date"), now(), "days") & " days to go"
```

---

## QUICK-START GUIDE

### Step 1 — Set Your Foundation
- Enter your **wedding date** in the Dashboard countdown
- Enter your **total budget** in the Budget Summary section
- Decide on budget category allocations using the recommended percentages as a starting point

### Step 2 — Build Your Guest List
- Open the **Guests** database and start entering names
- Don't worry about addresses yet — just get names, sides, and relationship categories in
- Mark the "Invited To" field for each guest (Ceremony, Reception, both, etc.)
- This gives you an initial headcount estimate for venue and catering conversations

### Step 3 — Start Vendor Research
- Open **Vendors** and add any vendors you're already considering
- Set status to "Researching" or "Contacted" as appropriate
- After meetings, update with quotes, ratings, and review notes
- When you book, change status to "Booked" and link to the Budget database

### Step 4 — Set Up Your Budget
- Open the **Budget** database and add your major expense categories
- Enter estimated costs based on vendor quotes and research
- Link budget items to their respective vendors
- Set up payment schedule dates as vendors are booked

### Step 5 — Load Your Timeline
- The **Tasks** database comes pre-loaded with 80+ common wedding tasks
- Review the full list and delete any that don't apply to your wedding
- Add any custom tasks specific to your plans
- Set due dates based on your wedding date (work backwards)
- Assign tasks to yourself, your partner, or other helpers

### Step 6 — Use the Dashboard Weekly
- Check the Dashboard every week for upcoming tasks and payment deadlines
- Update RSVP statuses as responses come in
- Review budget regularly — especially after booking new vendors
- Use the Inspiration Board to save and discuss ideas with your partner

### Pro Tips
- Schedule a weekly "wedding planning meeting" with your partner — even 20 minutes keeps things on track
- Update the RSVP tracker immediately when responses come in — don't let a stack build up
- Use the "Notes" field on vendors to record everything discussed in meetings — memory is unreliable over 12+ months of planning
- Duplicate your Task view and filter to just your assigned items vs. your partner's for clarity
- Start the seating chart 6 weeks before the wedding, once most RSVPs are in
- Keep the Inspiration Board active throughout — it helps when making vendor decisions
- Export the guest meal count view to send directly to your caterer
- Use the Thank-You tracker after the wedding to ensure every gift gets acknowledged
