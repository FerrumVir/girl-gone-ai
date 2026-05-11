# Notion Vacation Rental Manager — Notion Template

> Duplicate this page into your Notion workspace to get started. All six databases are pre-linked with booking calendars, guest communication workflows, cleaning checklists, revenue tracking, and maintenance scheduling already configured. Read the Quick-Start Guide at the bottom before your next guest check-in.

---

## DATABASES

---

### 1. Properties

**Purpose:** Master record for each rental property you manage. Stores listing details, amenities, house rules, access codes, and operational information. If you manage one property or twenty, this is your central reference.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Property Name | Title | Display name — e.g. "Lakeside Cabin" or "Downtown Loft #3" |
| Address | Text | Full street address |
| City | Text | City name |
| State/Region | Text | State or region |
| Property Type | Select | House / Apartment / Condo / Cabin / Studio / Townhouse / Villa / Cottage / Tiny Home / Room |
| Bedrooms | Number | Number of bedrooms |
| Bathrooms | Number | Number of bathrooms |
| Max Guests | Number | Maximum occupancy |
| Square Footage | Number | Size of property |
| Status | Select | Active / Inactive / Under Renovation / Seasonal / Listed / Unlisted |
| Listing Platforms | Multi-select | Airbnb / VRBO / Booking.com / Direct / Furnished Finder / Houfy / Hipcamp / Other |
| Airbnb Link | URL | Listing URL |
| VRBO Link | URL | Listing URL |
| Direct Booking Link | URL | Your own booking site |
| Nightly Rate (Base) | Number (USD) | Standard nightly rate |
| Weekend Rate | Number (USD) | Friday/Saturday rate |
| Weekly Discount % | Number | Percentage off for 7+ night stays |
| Monthly Rate | Number (USD) | For 28+ night stays |
| Cleaning Fee | Number (USD) | Per-stay cleaning fee charged to guests |
| Pet Fee | Number (USD) | If pets allowed |
| Security Deposit | Number (USD) | Refundable deposit amount |
| Minimum Stay | Number | Minimum nights required |
| Check-In Time | Text | Standard check-in — e.g. "3:00 PM" |
| Check-Out Time | Text | Standard check-out — e.g. "11:00 AM" |
| Wifi Network | Text | Network name |
| Wifi Password | Text | Password |
| Door Code | Text | Keypad or lockbox code |
| Parking | Text | Parking instructions |
| House Rules | Text | Key rules for guests |
| Amenities | Multi-select | Pool / Hot Tub / Fireplace / Grill / Washer-Dryer / Dishwasher / AC / Heating / Wifi / TV / Game Room / Gym / Lake Access / Beach Access / Pet Friendly / EV Charger / Workspace |
| Emergency Contacts | Text | Local emergency numbers, property manager, neighbor |
| Cleaning Team | Text | Name/company and contact info |
| Maintenance Contact | Text | Handyman/repair contact |
| Property Manager | Text | If not self-managed |
| Annual Revenue | Rollup | Sum of Total Revenue from linked Bookings (this year) |
| Occupancy Rate | Formula | Calculated from booked nights vs. available nights |
| Average Nightly Rate | Rollup | Average of Nightly Rate from linked Bookings |
| Total Bookings | Rollup | Count of linked Bookings |
| Average Rating | Rollup | Average of Guest Rating from linked Bookings |
| Photos | Files & Media | Professional listing photos |
| Floor Plan | Files & Media | Layout diagram |
| Linked Bookings | Relation | → Bookings database |
| Linked Maintenance | Relation | → Maintenance database |
| Linked Expenses | Relation | → Expenses database |
| Notes | Text | General property notes, upcoming plans, seasonal considerations |

**Views:**

- **All Properties** — Table, sorted by Property Name
- **Active Listings** — Filter: Status = Active or Listed
- **Property Cards** — Gallery view with Photos, Property Name, Bedrooms, Nightly Rate, Average Rating
- **Revenue Overview** — Table showing Property Name, Annual Revenue, Occupancy Rate, Average Nightly Rate
- **By City** — Table, grouped by City

---

### 2. Bookings

**Purpose:** Every reservation across all properties and platforms. Tracks guest info, dates, revenue, communication status, and operational tasks (cleaning, key exchange, etc.). The operational heart of your rental business.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Booking Name | Title | Guest name + dates — e.g. "Smith Family (May 12–15)" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Guest Name | Text | Primary guest's full name |
| Guest Email | Email | Contact email |
| Guest Phone | Phone | Contact phone |
| Number of Guests | Number | How many people staying |
| Platform | Select | Airbnb / VRBO / Booking.com / Direct / Repeat Guest / Friend/Family |
| Confirmation Code | Text | Platform confirmation number |
| Check-In Date | Date | Arrival date |
| Check-Out Date | Date | Departure date |
| Nights | Formula | `dateBetween(prop("Check-Out Date"), prop("Check-In Date"), "days")` |
| Status | Select | Inquiry / Pending / Confirmed / Checked In / Checked Out / Cancelled / No Show / Blocked |
| Nightly Rate | Number (USD) | Rate for this booking |
| Cleaning Fee | Number (USD) | Cleaning fee charged |
| Pet Fee | Number (USD) | If applicable |
| Extra Guest Fee | Number (USD) | If over base occupancy |
| Total Revenue | Formula | `(prop("Nightly Rate") * prop("Nights")) + prop("Cleaning Fee") + prop("Pet Fee") + prop("Extra Guest Fee")` |
| Platform Fee | Number (USD) | Commission taken by Airbnb/VRBO |
| Net Revenue | Formula | `prop("Total Revenue") - prop("Platform Fee")` |
| Revenue Per Night | Formula | `if(prop("Nights") == 0, 0, round(prop("Net Revenue") / prop("Nights")))` |
| Payment Status | Select | Pending / Partial / Paid / Refunded / Disputed |
| Payout Date | Date | When you received/will receive payment |
| Special Requests | Text | Anything the guest asked for (early check-in, crib, etc.) |
| Purpose of Stay | Select | Vacation / Business / Event / Relocation / Family Visit / Remote Work / Anniversary / Other |
| Pets | Checkbox | Bringing pets? |
| Pet Details | Text | Type, size, number of pets |
| Check-In Instructions Sent | Checkbox | Have you sent the arrival guide? |
| Welcome Message Sent | Checkbox | Sent day-of welcome? |
| Mid-Stay Check-In | Checkbox | Sent mid-stay message (for 3+ night stays)? |
| Check-Out Reminder Sent | Checkbox | Sent checkout instructions? |
| Review Left by Guest | Checkbox | Did they leave a review? |
| Guest Rating | Number | 1–5 stars they gave (if visible) |
| Review Left by Host | Checkbox | Did you review them? |
| My Rating of Guest | Select | Excellent / Good / Average / Problematic / Would Not Host Again |
| Cleaning Scheduled | Checkbox | Is turnover cleaning booked? |
| Cleaning Completed | Checkbox | Was cleaning done before check-in? |
| Cleaning Team | Text | Who is cleaning for this turnover |
| Inspection Done | Checkbox | Post-checkout property inspection completed? |
| Damage Reported | Checkbox | Any damage found? |
| Damage Notes | Text | Description of damage |
| Damage Claim Filed | Checkbox | Insurance or platform claim submitted? |
| Guest Communication Log | Text | Key messages exchanged |
| Linked Cleaning | Relation | → Cleaning Checklists database |
| Tags | Multi-select | Long Stay / Short Stay / Holiday / Peak Season / Off-Season / Last Minute / Repeat Guest / High Maintenance / VIP |
| Notes | Text | Booking-specific notes and observations |

**Views:**

- **All Bookings** — Table, sorted by Check-In Date descending
- **Calendar** — Calendar view by Check-In Date (essential view)
- **Current & Upcoming** — Filter: Status = Confirmed or Checked In, sorted by Check-In Date ascending
- **Pipeline** — Kanban grouped by Status
- **This Month** — Filter: Check-In Date is this month
- **Needs Communication** — Filter: various communication checkboxes unchecked based on timing
- **Revenue This Month** — Filter: Check-Out Date is this month, showing Net Revenue
- **Revenue This Year** — Filter: Check-In Date is this year, sorted by month
- **By Property** — Table, grouped by Property Name
- **Cancelled** — Filter: Status = Cancelled (track lost revenue)
- **Problem Guests** — Filter: My Rating = Problematic or Would Not Host Again
- **Repeat Guests** — Filter: Tags contains Repeat Guest
- **Unpaid** — Filter: Payment Status = Pending or Partial
- **Pending Reviews** — Filter: Review Left by Host = false AND Status = Checked Out

---

### 3. Guest Communication Templates

**Purpose:** Pre-written message templates for every stage of the guest journey. Ensures consistent, professional communication and saves hours of repetitive typing. Customize variables per booking but use these as your framework.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Template Name | Title | When to use — e.g. "Check-In Instructions (Day Before)" |
| Trigger Timing | Select | Inquiry Response / Booking Confirmed / 1 Week Before / 3 Days Before / Day Before / Check-In Day / Day After Arrival / Mid-Stay (3+ nights) / Check-Out Day / Day After Check-Out / Review Request / Re-booking Offer |
| Channel | Select | Platform Message / Email / Text / Automated |
| Subject Line | Text | For emails |
| Message Body | Text | Full template with [BRACKETS] for personalization variables |
| Variables Used | Text | List of fields to personalize — e.g. "[GUEST_NAME], [CHECK_IN_TIME], [DOOR_CODE]" |
| Platform | Select | Airbnb / VRBO / Direct / Universal |
| Property Specific | Checkbox | Does this template need per-property customization? |
| Tone | Select | Professional / Friendly / Concise / Detailed |
| Include Attachments | Text | What to attach — house manual, map, etc. |
| Response Rate | Select | High / Medium / Low / N/A |
| Last Updated | Date | When this template was last revised |
| Notes | Text | Tips, variations, things to personalize |
| Tags | Multi-select | Essential / Optional / Problem Resolution / Upsell / Automated |

**Views:**

- **All Templates** — Table, sorted by Trigger Timing order
- **Communication Timeline** — Table, sorted by Trigger Timing (the full guest journey)
- **By Channel** — Table, grouped by Channel
- **By Property** — Filter: Property Specific = true
- **Essential Only** — Filter: Tags contains Essential

---

### 4. Cleaning & Turnover Checklists

**Purpose:** Standardized cleaning checklists for each property ensuring consistent quality between every guest. Tracks turnover tasks, deep cleaning schedules, and supply inventory. Your cleaning team references this; you verify against it.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Checklist Name | Title | e.g. "Lakeside Cabin — Standard Turnover" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Booking | Relation | → Bookings database (specific turnover) |
| Type | Select | Standard Turnover / Deep Clean / Pre-Season / Post-Season / Inspection Only / Restocking |
| Date Assigned | Date | When cleaning is scheduled |
| Date Completed | Date | When cleaning was finished |
| Assigned To | Text | Cleaning team member or company |
| Status | Select | Scheduled / In Progress / Completed / Issue Found / Re-Clean Needed |
| Duration (mins) | Number | How long the turnover took |
| Cost | Number (USD) | What you paid for this cleaning |
| Guest Check-In Time | Date | When next guest arrives (urgency indicator) |
| Hours Until Check-In | Formula | `if(empty(prop("Guest Check-In Time")), "No guest scheduled", format(dateBetween(prop("Guest Check-In Time"), now(), "hours")) + " hours")` |
| Quality Rating | Select | Perfect / Good / Acceptable / Issues / Failed |
| Issues Found | Text | Anything wrong — damage, low supplies, maintenance needed |
| Photos | Files & Media | Post-cleaning verification photos |
| Supplies Restocked | Checkbox | Were all consumables replenished? |
| Linens Changed | Checkbox | Fresh bedding and towels? |
| Kitchen Deep Cleaned | Checkbox | Appliances, fridge, counters |
| Bathrooms Sanitized | Checkbox | Toilets, showers, sinks |
| Floors Cleaned | Checkbox | Vacuumed and mopped |
| Outdoor Areas | Checkbox | Patio, grill, yard tidied |
| Trash Removed | Checkbox | All bins emptied and relined |
| Welcome Items Set | Checkbox | Any welcome basket, guide placement, etc. |
| Thermostat Set | Checkbox | Set to pre-arrival temperature |
| Lights/Ambiance | Checkbox | Lights on, candles placed, music ready |
| Lost & Found | Text | Items left by previous guest |
| Lost & Found Contacted | Checkbox | Did you reach out to the previous guest? |
| Maintenance Flagged | Text | Anything that needs repair (links to Maintenance database) |
| Supply Reorder Needed | Text | What supplies are running low |
| Notes | Text | Cleaning notes, tips for this property |
| Tags | Multi-select | Rush / Same-Day Turn / Deep Clean Required / Extra Dirty / Pet Stay / Large Group |

**Views:**

- **All Checklists** — Table, sorted by Date Assigned descending
- **Today's Turnovers** — Filter: Date Assigned = today (morning briefing!)
- **Upcoming** — Filter: Status = Scheduled, sorted by Date Assigned ascending
- **Needs Attention** — Filter: Status = Issue Found or Re-Clean Needed
- **By Property** — Table, grouped by Property Name
- **Cost Tracker** — Table showing Date, Property, Cost (monthly cleaning expenses)
- **Quality Log** — Filter: Quality Rating = Issues or Failed (identify problem cleaners)
- **Rush Turnovers** — Filter: Tags contains Rush or Same-Day Turn

---

### 5. Maintenance & Repairs

**Purpose:** Track all property maintenance — scheduled upkeep, emergency repairs, and capital improvements. Ensures properties stay in top condition and nothing slips through the cracks. Critical for guest satisfaction and property value preservation.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Issue Name | Title | Clear description — e.g. "Kitchen faucet leak" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Category | Select | Plumbing / Electrical / HVAC / Appliance / Structural / Cosmetic / Outdoor / Furniture / Technology / Safety / Pest Control / Seasonal |
| Priority | Select | Emergency / Urgent / Normal / Low / Scheduled |
| Status | Select | Reported / Scheduled / In Progress / Waiting for Parts / Completed / Deferred / Recurring |
| Reported Date | Date | When issue was first noticed |
| Reported By | Select | Guest / Cleaning Team / Inspection / Owner / Neighbor |
| Scheduled Date | Date | When repair is planned |
| Completed Date | Date | When repair was finished |
| Days Open | Formula | `if(prop("Status") == "Completed", format(dateBetween(prop("Completed Date"), prop("Reported Date"), "days")) + " days", format(dateBetween(now(), prop("Reported Date"), "days")) + " days (open)")` |
| Vendor/Contractor | Text | Who is doing the repair |
| Vendor Phone | Phone | Contact number |
| Estimated Cost | Number (USD) | Expected expense |
| Actual Cost | Number (USD) | Final cost |
| Warranty Claim | Checkbox | Covered under warranty? |
| Insurance Claim | Checkbox | Filed with property insurance? |
| Affects Bookings | Checkbox | Does this impact guest experience or bookability? |
| Bookings Affected | Relation | → Bookings database |
| Guest Notified | Checkbox | If current guest is impacted, were they notified? |
| Guest Compensation | Text | Any discount or refund offered |
| Before Photo | Files & Media | Photo of the issue |
| After Photo | Files & Media | Photo after repair |
| Description | Text | Full description of the issue |
| Resolution | Text | What was done to fix it |
| Recurring | Checkbox | Does this need regular attention? |
| Recurrence Schedule | Text | e.g. "Every 6 months" or "Annually in spring" |
| Next Service Due | Date | For recurring maintenance |
| Notes | Text | Additional context, part numbers, access instructions |
| Tags | Multi-select | Guest-Reported / Preventive / Capital Improvement / Insurance / Tax Deductible / DIY / Professional Required |

**Views:**

- **All Maintenance** — Table, sorted by Reported Date descending
- **Open Issues** — Filter: Status != Completed AND Status != Deferred, sorted by Priority then Reported Date
- **Emergency/Urgent** — Filter: Priority = Emergency or Urgent (act immediately!)
- **By Property** — Table, grouped by Property Name
- **By Category** — Table, grouped by Category
- **Scheduled** — Filter: Status = Scheduled, sorted by Scheduled Date ascending
- **Completed** — Filter: Status = Completed, sorted by Completed Date descending
- **Cost Tracker** — Table showing Issue Name, Property, Actual Cost (running maintenance expense)
- **Recurring Maintenance** — Filter: Recurring = true, sorted by Next Service Due
- **Affects Bookings** — Filter: Affects Bookings = true AND Status != Completed
- **Warranty Items** — Filter: Warranty Claim = true

---

### 6. Financial Tracking / Expenses

**Purpose:** Track all income and expenses per property for accounting, tax preparation, and profitability analysis. Every dollar in and every dollar out, categorized and allocated to the correct property.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Description | Title | What this expense/income is for |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Type | Select | Income / Expense |
| Category | Select | Booking Revenue / Cleaning / Maintenance / Supplies / Utilities / Insurance / Mortgage / Property Tax / HOA / Software/Tools / Marketing / Furnishing / Capital Improvement / Professional Services / Travel / Platform Fees / Miscellaneous |
| Amount | Number (USD) | Dollar amount (positive for income, positive for expense) |
| Date | Date | Transaction date |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3))` |
| Year | Formula | `formatDate(prop("Date"), "YYYY")` |
| Recurring | Checkbox | Is this a monthly/regular expense? |
| Tax Deductible | Checkbox | Deductible business expense? |
| Tax Category | Select | Depreciation / Repairs / Cleaning / Utilities / Insurance / Mortgage Interest / Property Tax / Management / Advertising / Travel / Supplies / Professional Services / Other |
| Receipt | Files & Media | Upload receipt or invoice |
| Vendor | Text | Who was paid or who paid you |
| Payment Method | Select | Bank Transfer / Credit Card / Cash / Check / PayPal / Venmo / Platform Payout |
| Booking | Relation | → Bookings database (if related to a specific booking) |
| Maintenance | Relation | → Maintenance database (if related to a repair) |
| Notes | Text | Additional context |
| Tags | Multi-select | Fixed Cost / Variable / One-Time / Annual / Seasonal / Capital |

**Views:**

- **All Transactions** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month
- **Income** — Filter: Type = Income, sorted by Date descending
- **Expenses** — Filter: Type = Expense, sorted by Date descending
- **By Property** — Table, grouped by Property Name (see profitability per property)
- **By Category** — Table, grouped by Category
- **Monthly Summary** — Table grouped by Month with sum of Amount
- **Quarterly Summary** — Table grouped by Quarter
- **Tax Deductible** — Filter: Tax Deductible = true, grouped by Tax Category (hand this to your accountant)
- **Recurring Expenses** — Filter: Recurring = true (your fixed monthly overhead)
- **Capital Improvements** — Filter: Category = Capital Improvement (depreciation tracking)
- **P&L by Property** — Table showing Property Name with income sum vs expense sum

---

## REVENUE DASHBOARD

```
┌────────────────────────────────────────────────────────────────┐
│  RENTAL MANAGER COMMAND CENTER                                   │
├────────────────┬───────────────┬──────────────┬────────────────┤
│  Revenue MTD   │  Occupancy    │  Avg Nightly │  Upcoming      │
│  $4,850        │  72%          │  $185        │  3 bookings    │
├────────────────┴───────────────┴──────────────┴────────────────┤
│  BOOKING CALENDAR                                                │
│  [Linked view → Bookings, Calendar by Check-In Date]             │
├────────────────────────────────────────────────────────────────┤
│  TODAY'S ACTIONS                                                  │
│  - Turnovers due today                                           │
│  - Check-ins today                                               │
│  - Check-outs today                                              │
│  - Messages to send                                              │
├─────────────────────────────────┬──────────────────────────────┤
│  UPCOMING CHECK-INS (7 days)   │  OPEN MAINTENANCE              │
│  [Linked view → Bookings]      │  [Linked view → Maintenance]   │
├─────────────────────────────────┴──────────────────────────────┤
│  REVENUE BY PROPERTY (this month)                                │
│  [Linked view → Expenses, filter: Income, grouped by Property]   │
├────────────────────────────────────────────────────────────────┤
│  CLEANING SCHEDULE (next 7 days)                                 │
│  [Linked view → Cleaning Checklists, upcoming]                   │
└────────────────────────────────────────────────────────────────┘
```

---

## AUTOMATIONS / FORMULAS

### Booking Revenue Calculation

Total guest payment for a booking.

```
(prop("Nightly Rate") * prop("Nights")) + prop("Cleaning Fee") + prop("Pet Fee") + prop("Extra Guest Fee")
```

### Net Revenue

After platform commission.

```
prop("Total Revenue") - prop("Platform Fee")
```

### Revenue Per Night

Normalized metric for comparing bookings.

```
if(prop("Nights") == 0, 0, round(prop("Net Revenue") / prop("Nights")))
```

### Number of Nights

Calculated from check-in and check-out dates.

```
dateBetween(prop("Check-Out Date"), prop("Check-In Date"), "days")
```

### Hours Until Check-In

Urgency indicator for cleaning team.

```
if(
  empty(prop("Guest Check-In Time")),
  "No guest scheduled",
  format(dateBetween(prop("Guest Check-In Time"), now(), "hours")) + " hours"
)
```

### Maintenance Days Open

Tracks how long an issue has been unresolved.

```
if(
  prop("Status") == "Completed",
  format(dateBetween(prop("Completed Date"), prop("Reported Date"), "days")) + " days",
  format(dateBetween(now(), prop("Reported Date"), "days")) + " days (open)"
)
```

### Occupancy Rate (Monthly)

Calculate by counting booked nights in a month divided by available nights.

```
(Booked Nights in Month / Total Days in Month) * 100
```

Use a filtered view of Bookings where Check-In or Check-Out falls within the target month, sum the Nights property, divide by days in month.

---

## QUICK-START GUIDE

### Step 1 — Add Your Properties

- Open the **Properties** database and create an entry for each rental
- Fill in essential operational fields: Address, Check-In/Out Times, Wifi, Door Code, Max Guests
- Add your nightly rates and fee structure
- Upload professional photos and floor plan if available
- List Amenities and House Rules

### Step 2 — Import Existing Bookings

- Open **Bookings** and add all confirmed reservations
- At minimum: Guest Name, Check-In/Out Dates, Platform, Nightly Rate, Status
- For current month bookings, ensure all communication checkboxes reflect what you've already sent
- Link each booking to the correct Property

### Step 3 — Set Up Communication Templates

- Open **Guest Communication Templates** and customize the pre-loaded messages
- Replace [BRACKETS] with your specific property details
- At minimum, create: Booking Confirmation, Check-In Instructions (day before), Welcome Message (check-in day), Check-Out Reminder, and Review Request
- Test each template by reading it as if you were the guest

### Step 4 — Create Your Cleaning Checklists

- Open **Cleaning & Turnover Checklists** and create a master checklist for each property
- Duplicate the master for each upcoming turnover (link to specific Booking)
- Share with your cleaning team so they know exactly what's expected
- Include property-specific details (which sheets fit which bed, where supplies are stored)

### Step 5 — Establish Your Financial Baseline

- Open **Financial Tracking** and add:
  - All recurring monthly expenses (mortgage, insurance, utilities, subscriptions)
  - Revenue from the past 3 months (to establish baseline)
  - Any upcoming scheduled expenses
- Set Tax Deductible = true for all business expenses

### Step 6 — Operational Rhythms

**Every morning (5 minutes):**
- Check "Today's Actions" — any check-ins, check-outs, or turnovers today?
- Send any scheduled communication (day-before instructions, welcome messages)
- Verify cleaning is confirmed for any turnovers

**After every check-out:**
1. Update booking Status to Checked Out
2. Confirm cleaning team has started turnover
3. Review cleaning photos/report when done
4. Note any maintenance issues flagged
5. Send review request to guest within 24 hours
6. Leave your review of the guest

**Weekly (15 minutes):**
- Review upcoming bookings for next 7 days — all communications scheduled?
- Check maintenance items — anything open that needs attention before next guest?
- Review revenue vs. this time last year
- Update pricing for any remaining open dates (dynamic pricing)

**Monthly (30 minutes):**
- Run revenue report: total income, expenses, net profit per property
- Review occupancy rate — any patterns in low-occupancy periods?
- Check average rating — declining reviews need immediate attention
- Update cleaning supply inventory
- Review and pay any outstanding vendor invoices
- Check seasonal maintenance schedule

### Pro Tips

- The #1 driver of 5-star reviews is communication. Use your templates consistently and respond to all messages within 1 hour during business hours
- Always confirm cleaning completion before the guest arrives — "cleaning is booked" is not the same as "cleaning is done"
- Track Revenue Per Night, not just total revenue — a 2-night stay at $250/night is better than a 7-night stay at $100/night after cleaning costs
- Take post-cleaning photos of every turnover — they protect you in damage disputes
- The mid-stay check-in message (for 3+ night stays) prevents small issues from becoming bad reviews
- Dynamic pricing is essential: raise rates for weekends, holidays, and local events; lower for slow weekdays to maintain occupancy
- Log every expense immediately — chasing receipts at tax time is painful and you'll miss deductions
- Review your guest communication after every piece of feedback — if a guest asks a question your check-in instructions should have covered, update the template
- Keep a "Lost & Found" protocol — contacting previous guests about forgotten items earns you loyalty and positive reviews
- Maintenance prevention is cheaper than emergency repairs — use the Recurring Maintenance view to stay ahead of issues
