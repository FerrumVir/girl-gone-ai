# Airbnb Host Management Dashboard — Notion Template

> Duplicate this page into your Notion workspace to get started. All eight databases are pre-linked and all formulas are pre-built. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Properties

**Purpose:** Master record for every listing you manage. The foundation that all other databases link back to.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Property Name | Title | Friendly name — e.g., "Downtown Loft" or "Lake House" |
| Address | Text | Full street address |
| City | Text | |
| State/Region | Text | |
| Property Type | Select | Apartment / House / Condo / Cabin / Townhouse / Studio / Room / Guest Suite / Tiny House / Other |
| Bedrooms | Number | |
| Bathrooms | Number | |
| Max Occupancy | Number | Maximum number of guests |
| Square Footage | Number | |
| Airbnb Listing URL | URL | |
| VRBO Listing URL | URL | |
| Other Platform URL | URL | |
| Wifi Network | Text | Network name |
| Wifi Password | Text | |
| Access Instructions | Text | Lockbox code, smart lock details, key location, parking |
| House Rules | Text | Quiet hours, pet policy, smoking, parties, max occupancy rules |
| Check-In Time | Text | e.g., "3:00 PM" |
| Check-Out Time | Text | e.g., "11:00 AM" |
| Amenities | Multi-select | Pool / Hot Tub / Gym / Washer / Dryer / Dishwasher / AC / Heat / Fireplace / Grill / Garage / EV Charger / Pet Friendly / Workspace / Smart TV |
| Cleaning Team | Text | Name and contact for assigned cleaner(s) |
| Cleaning Fee | Number (USD) | Per-turnover cleaning fee |
| Base Nightly Rate | Number (USD) | Standard nightly rate |
| Weekend Rate | Number (USD) | Friday-Saturday rate |
| Peak Season Rate | Number (USD) | High-demand period rate |
| Minimum Stay | Number | Minimum nights |
| Owner | Text | Property owner (for co-hosts managing others' properties) |
| Owner Contact | Text | |
| Management Fee % | Number | Your co-hosting commission percentage (if applicable) |
| Status | Select | Active / Paused / Seasonal / Renovating / Inactive |
| Date Listed | Date | When the property first went live |
| Total Revenue | Rollup | Sum of Total Payout from linked Bookings |
| Total Expenses | Rollup | Sum of Amount from linked Expenses |
| Net Revenue | Formula | `prop("Total Revenue") - prop("Total Expenses")` |
| Total Bookings | Rollup | Count of linked Bookings where Status = Completed |
| Average Rating | Rollup | Average of Rating from linked Reviews |
| Linked Bookings | Relation | → Bookings database |
| Linked Expenses | Relation | → Expense Tracker database |
| Linked Reviews | Relation | → Review Management database |
| Linked Maintenance | Relation | → Maintenance Log database |
| Notes | Text | Property-specific context, quirks, seasonal considerations |
| Photos | Files | Property photos for reference |
| Tags | Multi-select | Superhost / High Performer / Needs Work / New Listing / Seasonal |

**Views:**

- **All Properties** — Table, sorted by Property Name
- **Active Listings** — Filter: Status = Active
- **Property Cards** — Gallery view with photos
- **By Performance** — Table, sorted by Net Revenue descending
- **Needs Attention** — Filter: Status = Renovating or Tags contains "Needs Work"

---

### 2. Bookings

**Purpose:** Every reservation — past, present, and future. Your operational calendar and revenue source of truth.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Booking Title | Title | "[Guest Name] — [Property] — [Check-in Date]" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Guest Name | Text | |
| Guest Email | Email | |
| Guest Phone | Phone | |
| Number of Guests | Number | |
| Platform | Select | Airbnb / VRBO / Booking.com / Direct / Other |
| Confirmation Code | Text | Platform booking reference |
| Check-In | Date | Check-in date and time |
| Check-Out | Date | Check-out date and time |
| Nights | Formula | `dateBetween(prop("Check-Out"), prop("Check-In"), "days")` |
| Nightly Rate | Number (USD) | Average nightly rate for this booking |
| Gross Booking Value | Formula | `prop("Nights") * prop("Nightly Rate")` |
| Cleaning Fee Charged | Number (USD) | Cleaning fee charged to guest |
| Platform Fees | Number (USD) | Fees deducted by the platform |
| Total Payout | Number (USD) | Actual amount received after platform fees |
| Profit Margin | Formula | `if(prop("Gross Booking Value") > 0, round((prop("Total Payout") / prop("Gross Booking Value")) * 100), 0)` |
| Status | Select | Confirmed / Checked In / Completed / Cancelled / No Show / Pending |
| Special Requests | Text | Guest's special requests or notes |
| Communication Status | Select | Confirmation Sent / Pre-Arrival Sent / Check-In Day Sent / Mid-Stay Sent / Checkout Sent / Post-Stay Sent / Complete |
| Turnover | Relation | → Cleaning & Turnover database |
| Turnover Status | Rollup | Status from linked Turnover |
| Review Left By Guest | Checkbox | Did the guest leave a review? |
| Review Requested | Checkbox | Did you request a review? |
| Guest Rating Given | Number | Rating you received (1-5 stars) |
| Notes | Text | Booking-specific notes, issues, damage reports |
| Linked Review | Relation | → Review Management database |
| Tags | Multi-select | Repeat Guest / Long Stay / Last Minute / Holiday / High Value / Problem Guest / VIP |

**Views:**

- **All Bookings** — Table, sorted by Check-In descending
- **Upcoming** — Filter: Check-In is in the future, Status = Confirmed, sorted by Check-In ascending
- **Current Guests** — Filter: Status = Checked In
- **Calendar** — Calendar view by Check-In date
- **By Property** — Table, grouped by Property Name
- **This Month** — Filter: Check-In is this month
- **Revenue Board** — Table showing Guest Name, Property, Nights, Total Payout, sorted by Total Payout descending
- **Booking Gaps** — Filter: Status = Confirmed or Completed, sorted by Check-Out ascending (manually identify gaps between bookings)
- **Cancelled / No Shows** — Filter: Status = Cancelled or No Show
- **Needs Review Request** — Filter: Status = Completed, Review Left By Guest = false, Review Requested = false
- **By Platform** — Table, grouped by Platform

---

### 3. Guest Communication Templates

**Purpose:** Pre-written message templates for every guest touchpoint. Customize per property, then copy-paste when needed.

**Entries (one set per property):**

#### Template 1: Booking Confirmation

```
Subject: Booking Confirmed — [PROPERTY NAME]

Hi [GUEST NAME],

Thank you for booking [PROPERTY NAME]! I'm excited to host you.

Here are your reservation details:
- Check-in: [DATE] at [CHECK-IN TIME]
- Check-out: [DATE] at [CHECK-OUT TIME]
- Guests: [NUMBER]
- Confirmation: [CODE]

I'll send detailed check-in instructions a few days before your arrival. In the meantime, feel free to reach out with any questions.

Looking forward to your stay!

[YOUR NAME]
```

#### Template 2: Pre-Arrival Instructions (Send 2 days before)

```
Hi [GUEST NAME],

Your stay at [PROPERTY NAME] is almost here! Here's everything you need for a smooth arrival.

ADDRESS: [FULL ADDRESS]

CHECK-IN INSTRUCTIONS:
[ACCESS INSTRUCTIONS — lockbox code, smart lock, key location]

PARKING:
[PARKING DETAILS]

WIFI:
Network: [WIFI NETWORK]
Password: [WIFI PASSWORD]

HOUSE ESSENTIALS:
- [Thermostat location/instructions]
- [TV/streaming instructions]
- [Washer/dryer location]
- [Trash/recycling schedule]
- [Any property-specific instructions]

HOUSE RULES:
- Quiet hours: [TIMES]
- [Smoking/pet/party policy]
- Check-out time: [TIME]

LOCAL RECOMMENDATIONS:
- Coffee: [RECOMMENDATION]
- Restaurants: [2-3 RECOMMENDATIONS]
- Groceries: [NEAREST STORE]

If you need anything during your stay, don't hesitate to message me. I typically respond within 30 minutes during daytime hours.

Enjoy your trip!

[YOUR NAME]
```

#### Template 3: Check-In Day (Send morning of check-in)

```
Hi [GUEST NAME],

Happy check-in day! Just a reminder that [PROPERTY NAME] is ready for you starting at [CHECK-IN TIME].

Quick reminders:
- [ACCESS INSTRUCTIONS — brief version]
- Wifi: [NETWORK] / [PASSWORD]

Let me know once you're settled in or if you need anything at all.

[YOUR NAME]
```

#### Template 4: Mid-Stay Check-In (Send morning after first night)

```
Hi [GUEST NAME],

Hope you had a great first night at [PROPERTY NAME]! Just checking in to make sure everything is to your liking.

Is there anything you need or any questions about the space?

Enjoy the rest of your stay!

[YOUR NAME]
```

#### Template 5: Checkout Reminder (Send evening before checkout)

```
Hi [GUEST NAME],

Hope you've enjoyed your stay at [PROPERTY NAME]! Just a friendly reminder that check-out is tomorrow at [CHECK-OUT TIME].

Before you head out:
- [ ] Please start a load of towels in the washer (optional but appreciated)
- [ ] Take out any trash to the [BIN LOCATION]
- [ ] Load any dirty dishes into the dishwasher
- [ ] Turn off all lights and [AC/HEAT]
- [ ] Lock the door — [LOCK INSTRUCTIONS]
- [ ] [Any property-specific checkout tasks]

No need to strip the beds — our cleaning team will take care of that.

Thank you for staying with us! If you enjoyed your experience, I'd truly appreciate a review. It helps future guests find the listing and means a lot to me as a host.

Safe travels!

[YOUR NAME]
```

#### Template 6: Post-Checkout Thank You (Send day after checkout)

```
Hi [GUEST NAME],

Thank you for staying at [PROPERTY NAME]! I hope you had a wonderful time in [CITY].

I've just left you a 5-star review. If you have a moment, I'd really appreciate a review from your side — it makes a huge difference for our listing.

You're always welcome back! I offer a [X]% discount for return guests. Just message me directly next time you're planning a trip to [CITY].

Best,

[YOUR NAME]
```

#### Template 7: Review Request Follow-Up (Send 5 days after checkout if no review)

```
Hi [GUEST NAME],

Hope you've been well since your trip! I just wanted to follow up — if you have 2 minutes, a review of your stay at [PROPERTY NAME] would mean the world to me.

Here's the direct link: [REVIEW LINK if available]

No pressure at all, but it really helps future guests and supports our small hosting business.

Thanks again for choosing to stay with us!

[YOUR NAME]
```

---

### 4. Cleaning & Turnover Schedule

**Purpose:** Every turnover between guests, with cleaning assignment, checklist, and status. Your operations backbone.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Turnover Title | Title | "[Property] — [Date]" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Booking (Checkout) | Relation | → Bookings database (the departing guest) |
| Booking (Check-In) | Relation | → Bookings database (the arriving guest) |
| Checkout Time | Date | When the departing guest leaves |
| Check-In Time | Date | When the next guest arrives |
| Time Window | Formula | `if(and(not(empty(prop("Check-In Time"))), not(empty(prop("Checkout Time")))), format(dateBetween(prop("Check-In Time"), prop("Checkout Time"), "hours")) + " hours", "No next guest")` |
| Cleaner Assigned | Text | Name of assigned cleaner or team |
| Cleaner Notified | Checkbox | Have you confirmed with the cleaner? |
| Status | Select | Scheduled / In Progress / Completed / Issue Found / Cancelled |
| Cleaning Type | Select | Standard Turnover / Deep Clean / Touch-Up / Pre-Season / Post-Season |
| Checklist Complete | Checkbox | All items on the checklist done? |
| Cost | Number (USD) | Cleaning cost |
| Issues Found | Text | Damage, missing items, maintenance needs discovered during cleaning |
| Photos | Files | Post-cleaning verification photos |
| Notes | Text | Special instructions for this turnover |
| Linked Expense | Relation | → Expense Tracker database |

**Standard Turnover Checklist (copy into each entry):**

```
KITCHEN
- [ ] Wash all dishes / run dishwasher / empty dishwasher
- [ ] Wipe countertops, stovetop, and backsplash
- [ ] Clean inside microwave
- [ ] Clean inside refrigerator — remove all guest food
- [ ] Empty all trash cans and replace liners
- [ ] Restock: dish soap, sponge, paper towels, trash bags
- [ ] Run garbage disposal with ice and lemon

BATHROOMS
- [ ] Scrub toilet (inside and outside)
- [ ] Clean shower/tub — check for hair and soap buildup
- [ ] Wipe mirror and all surfaces
- [ ] Clean sink and faucet
- [ ] Empty trash and replace liner
- [ ] Restock: toilet paper (2 extra rolls), hand soap, shampoo, conditioner, body wash
- [ ] Fold or hang fresh towels (bath towel, hand towel, washcloth per guest)

BEDROOMS
- [ ] Strip and remake all beds with fresh linens
- [ ] Check under beds and in drawers for left-behind items
- [ ] Dust nightstands and dressers
- [ ] Empty trash
- [ ] Check hangers in closet (minimum 10 per closet)

LIVING AREAS
- [ ] Vacuum all carpets and rugs
- [ ] Mop all hard floors
- [ ] Dust all surfaces
- [ ] Wipe remote controls, light switches, and door handles
- [ ] Fluff and arrange pillows and throws
- [ ] Check for and remove any guest items left behind

GENERAL
- [ ] Wipe all light switches, door handles, and high-touch surfaces
- [ ] Clean all windows (interior) — remove fingerprints
- [ ] Sweep and mop entryway
- [ ] Set thermostat to [TEMP]
- [ ] Turn on porch light / entry light
- [ ] Check all light bulbs — replace any that are out
- [ ] Check wifi is working
- [ ] Check TV and streaming services work
- [ ] Set out welcome amenities: [LIST]
- [ ] Lock all windows
- [ ] Take post-cleaning photos
- [ ] Report any issues or maintenance needs
```

**Views:**

- **All Turnovers** — Table, sorted by Checkout Time descending
- **Today's Turnovers** — Filter: Checkout Time is today
- **This Week** — Filter: Checkout Time is this week, sorted by Checkout Time ascending
- **Upcoming** — Filter: Status = Scheduled, sorted by Checkout Time ascending
- **By Property** — Table, grouped by Property Name
- **Issues Found** — Filter: Status = Issue Found
- **Needs Cleaner Notification** — Filter: Cleaner Notified = false, Status = Scheduled, Checkout Time is within 3 days

---

### 5. Expense Tracker

**Purpose:** Every dollar spent on your rental business, organized for operations and tax preparation.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Expense Title | Title | Clear description — e.g., "Lake House — HVAC Repair" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Date | Date | When the expense occurred |
| Amount | Number (USD) | |
| Category | Select | Cleaning / Supplies / Repairs / Maintenance / Utilities / Insurance / Mortgage/Rent / Property Tax / HOA / Furniture / Linens & Towels / Appliances / Platform Fees / Software / Professional Services / Marketing / Permits & Licenses / Travel / Other |
| Tax Deductible | Checkbox | Is this expense deductible? |
| Payment Method | Select | Credit Card / Debit / Check / Cash / Transfer / Other |
| Vendor | Text | Who you paid |
| Receipt | Files | Upload receipt photo or document |
| Recurring | Checkbox | Is this a recurring monthly expense? |
| Linked Booking | Relation | → Bookings database (if expense is tied to a specific booking) |
| Linked Maintenance | Relation | → Maintenance Log database |
| Notes | Text | |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Quarter | Formula | `"Q" + format(ceil(toNumber(formatDate(prop("Date"), "M")) / 3)) + " " + formatDate(prop("Date"), "YYYY")` |
| Tags | Multi-select | Capital Improvement / Operating / Emergency / Preventive / Guest-Caused |

**Views:**

- **All Expenses** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month
- **By Property** — Table, grouped by Property Name
- **By Category** — Table, grouped by Category
- **By Month** — Table, grouped by Month
- **By Quarter** — Table, grouped by Quarter (for quarterly tax estimates)
- **Tax Deductible** — Filter: Tax Deductible = true
- **Recurring** — Filter: Recurring = true (your monthly fixed costs)
- **Large Expenses** — Table, sorted by Amount descending

---

### 6. Revenue & Financial Dashboard

> This section is built using views from the Bookings and Expense Tracker databases. Create this as a Notion page with linked database views.

### Financial Dashboard Layout

```
+-------------------------------------------------------------+
|  FINANCIAL OVERVIEW                      April 2026           |
+--------------+--------------+--------------+-----------------+
|  Gross Rev.  |  Expenses    |  Net Revenue |  Occupancy      |
|  This Month  |  This Month  |  This Month  |  Rate           |
|  $4,200      |  $1,340      |  $2,860      |  78%            |
+--------------+--------------+--------------+-----------------+
|  REVENUE BY PROPERTY (This Month)                             |
|  [Linked view → Bookings, grouped by Property, showing Total  |
|   Payout sum, filter: Check-In is this month]                |
+-------------------------------------------------------------+
|  REVENUE BY PLATFORM (This Month)                             |
|  [Linked view → Bookings, grouped by Platform]               |
+-----------------------------+-------------------------------+
|  EXPENSES BY CATEGORY       |  EXPENSES BY PROPERTY          |
|  [Linked view → Expenses,   |  [Linked view → Expenses,      |
|   grouped by Category,      |   grouped by Property Name,    |
|   filter: this month]       |   filter: this month]          |
+-----------------------------+-------------------------------+
|  MONTHLY TRENDS                                               |
|  [Linked view → Bookings, grouped by Month, showing count     |
|   and sum of Total Payout — last 12 months]                  |
+-------------------------------------------------------------+
```

### Occupancy Rate Calculation

For each property, calculate occupancy manually at month-end:

```
Occupancy Rate = (Booked Nights / Available Nights) x 100

Example:
- April has 30 days
- Property was booked for 23 nights
- Occupancy = (23/30) x 100 = 76.7%
```

Track in a simple table per property per month:

| Property | Month | Available Nights | Booked Nights | Occupancy % | Revenue | Avg Nightly Rate |
|---|---|---|---|---|---|---|
| Downtown Loft | April 2026 | 30 | 23 | 76.7% | $3,220 | $140 |
| Lake House | April 2026 | 30 | 18 | 60.0% | $2,700 | $150 |

---

### 7. Review Management

**Purpose:** Track every review received and given. Protect and grow your ratings.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Review Title | Title | "[Guest Name] — [Property] — [Rating]" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Booking | Relation | → Bookings database |
| Guest Name | Text | |
| Date | Date | When the review was posted |
| Platform | Select | Airbnb / VRBO / Booking.com / Google / Other |
| Rating (Received) | Number | Star rating from guest (1-5) |
| Review Text | Text | Full text of the guest's review |
| Response Written | Checkbox | Did you respond to the review? |
| Your Response | Text | Your public response to the review |
| Response Date | Date | |
| Rating (Given) | Number | Star rating you gave the guest |
| Your Review of Guest | Text | Review you wrote for the guest |
| Sentiment | Select | Positive / Neutral / Negative / Mixed |
| Issues Mentioned | Multi-select | Cleanliness / Communication / Check-In / Accuracy / Location / Value / Noise / Temperature / Wifi / Amenities / Other |
| Action Taken | Text | What you did or changed in response to the feedback |
| Tags | Multi-select | Superhost Relevant / Needs Improvement / Repeat Guest / Unfair Review |

**Views:**

- **All Reviews** — Table, sorted by Date descending
- **Needs Response** — Filter: Response Written = false, sorted by Date ascending
- **By Property** — Table, grouped by Property Name
- **Negative Reviews** — Filter: Rating (Received) <= 3
- **By Rating** — Table, grouped by Rating (Received)
- **Average Rating Tracker** — Table, grouped by Property Name, showing average of Rating (Received)
- **Issues Tracker** — Table, grouped by Issues Mentioned (identify recurring complaints)

---

### 8. Maintenance Log

**Purpose:** Every repair, replacement, and improvement. Proactive maintenance protects your ratings and your investment.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Maintenance Title | Title | Clear description — e.g., "Lake House — Kitchen Faucet Replacement" |
| Property | Relation | → Properties database |
| Property Name | Rollup | From Property relation |
| Date Reported | Date | When the issue was discovered or reported |
| Date Completed | Date | When the work was finished |
| Urgency | Select | Emergency / Urgent / Normal / Low / Preventive |
| Status | Select | Reported / Scheduled / In Progress / Completed / Deferred / Recurring |
| Category | Select | Plumbing / Electrical / HVAC / Appliance / Structural / Cosmetic / Landscaping / Pest Control / Safety / Technology / Furniture / Cleaning Equipment / Other |
| Description | Text | Detailed description of the issue |
| Resolution | Text | What was done to fix it |
| Vendor | Text | Contractor or service provider name |
| Vendor Contact | Text | Phone/email |
| Cost | Number (USD) | |
| Covered by Insurance | Checkbox | |
| Covered by Warranty | Checkbox | |
| Guest Reported | Checkbox | Was this reported by a guest during their stay? |
| Linked Booking | Relation | → Bookings database (if discovered during a stay) |
| Linked Expense | Relation | → Expense Tracker database |
| Before Photos | Files | Photos before repair |
| After Photos | Files | Photos after repair |
| Next Scheduled | Date | For recurring/preventive maintenance — when is the next service? |
| Notes | Text | |
| Tags | Multi-select | Capital Improvement / Warranty / Insurance Claim / Guest Damage / Wear and Tear / Upgrade |

**Pre-loaded Preventive Maintenance Schedule:**

| Task | Frequency | Category | Notes |
|---|---|---|---|
| HVAC filter replacement | Every 3 months | HVAC | Schedule for March, June, Sept, Dec |
| Smoke/CO detector battery test | Every 6 months | Safety | Test and replace batteries |
| Deep clean carpets | Every 6 months | Cleaning Equipment | Professional steam clean |
| Dryer vent cleaning | Annually | Appliance | Fire prevention |
| Water heater flush | Annually | Plumbing | Extend water heater life |
| Gutter cleaning | Twice yearly | Structural | Spring and fall |
| Pest control treatment | Quarterly | Pest Control | Exterior perimeter spray |
| Fire extinguisher check | Annually | Safety | Check pressure gauge, replace if expired |
| Exterior paint touch-up | Annually | Cosmetic | Check for peeling, touch up |
| Mattress rotation | Every 6 months | Furniture | Extend mattress life |
| Lock/keypad battery replacement | Every 6 months | Technology | Prevent guest lockouts |

**Views:**

- **All Maintenance** — Table, sorted by Date Reported descending
- **Open Items** — Filter: Status is not Completed or Deferred, sorted by Urgency then Date Reported
- **By Property** — Table, grouped by Property Name
- **Emergency / Urgent** — Filter: Urgency = Emergency or Urgent, Status is not Completed
- **Scheduled Maintenance** — Filter: Next Scheduled is within 30 days
- **Completed** — Filter: Status = Completed, sorted by Date Completed descending
- **By Category** — Table, grouped by Category
- **Guest-Reported Issues** — Filter: Guest Reported = true

---

## DASHBOARD

> Create this as the top-level Notion page. Pin it to your sidebar. Check it every morning before your first guest interaction.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  HOSTING COMMAND CENTER                  April 2026           |
+--------------+--------------+--------------+-----------------+
|  Active      |  Check-Ins   |  Turnovers   |  Open           |
|  Guests      |  Today       |  Today       |  Maintenance    |
|     3        |     1        |     2        |     4           |
+--------------+--------------+--------------+-----------------+
|  TODAY'S OPERATIONS                                           |
|  [Linked view → Turnovers, filter: today]                    |
|  [Linked view → Bookings, filter: Check-In = today]          |
+-------------------------------------------------------------+
|  UPCOMING BOOKINGS (Next 14 Days)                             |
|  [Linked view → Bookings, Calendar by Check-In]              |
+-----------------------------+-------------------------------+
|  PENDING REVIEWS            |  URGENT MAINTENANCE            |
|  [Linked view → Reviews,    |  [Linked view → Maintenance,   |
|   filter: Needs Response]   |   filter: Emergency/Urgent,    |
|                             |   Status != Completed]         |
+-----------------------------+-------------------------------+
|  FINANCIAL SUMMARY (This Month)                               |
|  [Linked view → Bookings, sum of Total Payout this month]    |
|  [Linked view → Expenses, sum of Amount this month]          |
+-------------------------------------------------------------+
|  REVIEW REQUEST QUEUE                                         |
|  [Linked view → Bookings, filter: Completed, no review,      |
|   review not requested]                                      |
+-------------------------------------------------------------+
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Properties (10 minutes per property)
- Open the **Properties** database and add each listing
- At minimum: Property Name, Address, Property Type, Bedrooms, Bathrooms, Check-In/Out Times
- Add Wifi details, access instructions, and house rules — these feed your guest communication templates
- Set the Base Nightly Rate and Cleaning Fee

### Step 2 — Customize Guest Communication Templates (15 minutes per property)
- Open the **Guest Communication Templates** and customize each template for each property
- Replace all [PLACEHOLDER] text with your specific property details
- Save these as Notion pages linked to each property for quick copy-paste access

### Step 3 — Add Your Bookings (5 minutes)
- Open the **Bookings** database
- Add all upcoming confirmed bookings
- Link each to the correct Property
- Add at least the last month of completed bookings for revenue baseline data

### Step 4 — Set Up Turnovers (5 minutes)
- For every booking where a guest is departing and another is arriving the same day, create a Turnover entry
- Link to both the departing and arriving bookings
- Assign your cleaner and set Status to Scheduled
- Copy the Standard Turnover Checklist into the entry

### Step 5 — Enter Historical Expenses (20 minutes)
- Add the last 3 months of expenses to the **Expense Tracker**
- Be thorough: cleaning fees, supplies, repairs, utilities, insurance, mortgage, platform fees
- Categorize each expense — this matters for tax deductions and profit analysis

### Step 6 — Seed Your Reviews (10 minutes)
- Add your last 10–20 reviews to the **Review Management** database
- Note any reviews you haven't responded to — respond to them now
- This seeds your average rating tracking

### Step 7 — Initialize Maintenance Log
- Add any open maintenance issues
- Add the Preventive Maintenance Schedule items with their next scheduled dates
- Set reminders for yourself to check the "Scheduled Maintenance" view monthly

### Step 8 — Build Your Dashboard
- Create the Dashboard page using the layout above
- Pin it to your Notion sidebar
- This is your daily operations home base

### Daily Rhythm (10 minutes)

**Every morning:**

- Open the Dashboard
- Check "Today's Turnovers" — confirm cleaners are notified and assigned
- Check "Check-Ins Today" — send check-in day messages from templates
- Check "Current Guests" — send mid-stay check-in if it's their first morning
- Check "Pending Reviews" — respond to any new reviews

**After every checkout:**

- Update booking Status to Completed
- Create a Turnover entry if not already created
- Verify cleaner has completed and confirmed

**Every evening:**

- Check tomorrow's turnovers and check-ins
- Pre-send any guest messages for tomorrow
- Update Communication Status on active bookings

### Weekly Rhythm (20 minutes)

- Review this week's revenue in the Bookings database
- Check "Review Request Queue" — follow up with guests who haven't reviewed
- Review "Open Maintenance" — any items slipping?
- Check booking calendar for the next 30 days — any gaps to address with pricing?

### Monthly Rhythm (45 minutes)

- Calculate occupancy rate per property
- Review monthly revenue vs. expenses — update the Financial Dashboard
- Review reviews for the month — any recurring complaints?
- Check Scheduled Maintenance — anything due this month?
- Review expenses by category — any cost categories growing unexpectedly?
- Export expense data if needed for tax estimates

### Pro Tips

- Send the pre-arrival instructions exactly 2 days before check-in. Earlier and guests forget the details. Later and they're already anxious about logistics.
- The mid-stay check-in message (morning after first night) is the highest-ROI message you can send. It catches problems before they become complaints. Most issues a guest experiences — a weird thermostat, a tricky shower, a noisy neighbor — happen the first night. A proactive message gives them a way to tell you before it becomes a bad review.
- Take post-cleaning photos for every turnover. If a guest claims damage, your timestamped photos are your evidence.
- Track your actual cleaning costs in the Expense Tracker, not just what you charge guests. If you're paying your cleaner $120 but charging a $100 cleaning fee, you're subsidizing every turnover.
- Use the "Issues Found" field on turnovers religiously. Your cleaner is your eyes on the property. Every issue they report is a maintenance problem caught early.
- Review your pricing monthly by checking the "Booking Gaps" view. Frequent gaps between bookings often mean your price is too high for the shoulder days, or your minimum stay is too restrictive.
- Respond to every review — positive and negative. Public responses to negative reviews matter more than the review itself. Future guests read your response to decide if the issue was a fluke or a pattern.
- The Preventive Maintenance Schedule is what separates amateur hosts from professionals. A $15 HVAC filter replaced quarterly prevents a $2,000 compressor failure at the worst possible time.
