# Travel Planning Dashboard — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with budget formulas, day-by-day itinerary views, and multi-trip management built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Trips

**Purpose:** Master record for every trip — past, current, and planned. Each trip links to its itinerary days, bookings, packing lists, and budget entries. This is your trip portfolio and the top-level navigation layer.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Trip Name | Title | Descriptive name (e.g., "Japan 2026" or "Portland Long Weekend") |
| Destination | Text | Primary destination(s) |
| Country | Select | (Add countries as needed) |
| Trip Type | Select | Vacation / Business / Family / Adventure / Weekend Getaway / Road Trip / Honeymoon / Solo / Group / Digital Nomad |
| Status | Select | Dreaming / Planning / Booked / In Progress / Completed / Cancelled |
| Start Date | Date | Departure date |
| End Date | Date | Return date |
| Duration | Formula | `if(and(not(empty(prop("Start Date"))), not(empty(prop("End Date")))), format(dateBetween(prop("End Date"), prop("Start Date"), "days")) + " days", "TBD")` |
| Days Until Trip | Formula | `if(empty(prop("Start Date")), "No date", if(prop("Start Date") > now(), format(dateBetween(prop("Start Date"), now(), "days")) + " days away", if(and(prop("Start Date") <= now(), prop("End Date") >= now()), "Currently traveling!", "Completed")))` |
| Travelers | Number | How many people |
| Traveler Names | Text | Who's going |
| Total Budget | Number (USD) | Planned total spend |
| Actual Spend | Number (USD) | Running total (rollup from Budget entries) |
| Budget Remaining | Formula | `prop("Total Budget") - prop("Actual Spend")` |
| Budget Status | Formula | `if(prop("Total Budget") == 0, "No budget set", if(prop("Actual Spend") > prop("Total Budget"), "Over Budget!", if(prop("Actual Spend") / prop("Total Budget") > 0.85, "Almost at limit", "On Track")))` |
| Per Day Budget | Formula | `if(or(prop("Total Budget") == 0, prop("Duration") == "TBD"), 0, round(prop("Total Budget") / toNumber(replace(prop("Duration"), " days", ""))))` |
| Currency | Select | USD / EUR / GBP / JPY / AUD / CAD / CHF / Other |
| Exchange Rate | Number | Local currency per 1 USD (for conversion) |
| Time Zone | Text | Destination time zone |
| Linked Itinerary | Relation | -> Itinerary Days database |
| Linked Bookings | Relation | -> Bookings database |
| Linked Packing | Relation | -> Packing Lists database |
| Linked Budget | Relation | -> Budget/Expenses database |
| Booking Count | Rollup | Count of Linked Bookings |
| Itinerary Days | Rollup | Count of Linked Itinerary |
| Trip Notes | Text | General planning notes, visa requirements, emergency contacts |
| Trip Rating | Select | 5 Stars / 4 Stars / 3 Stars / 2 Stars / 1 Star (post-trip) |
| Highlights | Text | Best moments (fill in after trip) |
| Would Return | Checkbox | Would you go back? |
| Cover Photo | Files & media | Trip cover image for gallery view |
| Tags | Multi-select | Beach / City / Mountains / Culture / Food / Adventure / Relaxation / Photography / Budget / Luxury |

**Views:**

- **All Trips** — Gallery with Cover Photo, sorted by Start Date descending
- **Upcoming** — Filter: Status = Planning or Booked, sorted by Start Date ascending
- **Currently Traveling** — Filter: Status = In Progress
- **Past Trips** — Filter: Status = Completed, sorted by Start Date descending
- **Dream List** — Filter: Status = Dreaming
- **By Destination** — Table, grouped by Country
- **Timeline** — Timeline view, Start Date to End Date
- **Budget Overview** — Table showing Trip Name, Total Budget, Actual Spend, Budget Status

---

### 2. Itinerary Days

**Purpose:** Day-by-day breakdown of each trip. Each entry represents one day with time-blocked activities, locations, reservations, and logistics. This is what you reference during the trip — your on-the-ground guide.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Day Title | Title | "Day [N] — [Theme/Location]" (e.g., "Day 3 — Kyoto Temples") |
| Trip | Relation | -> Trips database |
| Date | Date | Calendar date for this day |
| Day Number | Number | Day 1, Day 2, etc. |
| Location | Text | Where you'll be this day |
| Morning | Text | Activities/plans for morning (with times) |
| Afternoon | Text | Activities/plans for afternoon (with times) |
| Evening | Text | Activities/plans for evening (with times) |
| Meals | Text | Breakfast, lunch, dinner plans/reservations |
| Transportation | Text | How you're getting between places |
| Reservations | Text | Any timed reservations (restaurants, tours, tickets) |
| Reservation Confirmation | Text | Confirmation numbers for the day |
| Accommodation | Text | Where you're sleeping tonight |
| Check-in/Check-out | Text | Any accommodation transitions |
| Estimated Cost | Number (USD) | Projected spend for this day |
| Actual Cost | Number (USD) | What you actually spent (fill during/after trip) |
| Walking Distance | Text | Estimated walking/activity level |
| Weather Note | Text | Expected weather (fill closer to date) |
| Must-Do | Text | The one thing that absolutely cannot be missed today |
| Backup Plan | Text | What to do if weather/logistics derail the plan |
| Notes | Text | Tips, addresses, phone numbers, transit directions |
| Map Link | URL | Google Maps link with pinned locations for the day |
| Day Rating | Select | Amazing / Great / Good / OK / Rough (post-trip) |
| Highlight | Text | Best moment of this day (post-trip journal) |

**Views:**

- **Full Itinerary** — Table, sorted by Day Number ascending (trip planning view)
- **By Trip** — Table, grouped by Trip
- **Calendar** — Calendar view by Date
- **Today** — Filter: Date = today (use during travel)
- **This Trip** — Filter by specific trip relation (filtered per active trip)
- **Day Cards** — Gallery showing Day Title, Morning/Afternoon/Evening, Must-Do

---

### 3. Bookings

**Purpose:** Every reservation, ticket, and booking across all trips. Flights, hotels, tours, restaurants, rental cars, trains — anything with a confirmation number lives here.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Booking Name | Title | Clear description (e.g., "LAX -> NRT Flight, United 837") |
| Trip | Relation | -> Trips database |
| Category | Select | Flight / Hotel / Airbnb / Hostel / Car Rental / Train / Bus / Ferry / Tour / Activity / Restaurant / Insurance / Visa / Other |
| Status | Select | Researching / Booked / Confirmed / Checked-In / Completed / Cancelled / Refunded |
| Provider | Text | Airline, hotel chain, booking platform |
| Confirmation # | Text | Booking reference number |
| Date | Date | Date of service |
| End Date | Date | Check-out or return date (for multi-day bookings) |
| Time | Text | Departure/arrival time, check-in time |
| Location | Text | Address or terminal |
| Cost | Number (USD) | Total cost |
| Cost Per Person | Formula | `if(prop("Travelers Splitting") == 0, prop("Cost"), round(prop("Cost") / prop("Travelers Splitting") * 100) / 100)` |
| Travelers Splitting | Number | How many people splitting this cost |
| Payment Status | Select | Unpaid / Deposit Paid / Fully Paid / Refund Pending / Refunded |
| Cancellation Policy | Select | Free Cancellation / Cancel by [date] / Non-refundable / Partial Refund |
| Cancel By Date | Date | Last date for free cancellation |
| Booking URL | URL | Link to manage booking |
| Contact | Text | Phone/email for the provider |
| Notes | Text | Seat preferences, room requests, pickup details |
| Documents | Files & media | Tickets, vouchers, confirmation PDFs |
| Linked Itinerary Day | Relation | -> Itinerary Days (which day this booking is for) |
| Days Until | Formula | `if(empty(prop("Date")), "No date", if(prop("Date") < now(), "Past", format(dateBetween(prop("Date"), now(), "days")) + " days"))` |
| Tags | Multi-select | Flexible / Non-refundable / Loyalty Points / Early Bird / Splurge / Budget |

**Views:**

- **All Bookings** — Table, sorted by Date ascending
- **By Trip** — Table, grouped by Trip
- **By Category** — Table, grouped by Category
- **Upcoming** — Filter: Status = Booked or Confirmed, sorted by Date ascending
- **Flights** — Filter: Category = Flight
- **Accommodation** — Filter: Category = Hotel or Airbnb or Hostel
- **Cancellation Deadlines** — Sorted by Cancel By Date ascending, filtered to future dates
- **Unpaid** — Filter: Payment Status = Unpaid or Deposit Paid
- **This Trip** — Filter by specific trip (for active trip reference)
- **Calendar** — Calendar view by Date

---

### 4. Packing Lists

**Purpose:** Packing checklists organized by category and trip type. Reusable templates you can duplicate for each trip. Check items off as you pack — never forget essentials again.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Item | Title | Specific item name |
| Trip | Relation | -> Trips database |
| Category | Select | Clothing / Toiletries / Electronics / Documents / Medicine / Accessories / Gear / Snacks / Comfort / Work / Kids / Misc |
| Packed | Checkbox | Is it in the bag? |
| Quantity | Number | How many to bring |
| Bag | Select | Carry-on / Checked / Personal Item / Day Pack / Not Assigned |
| Essential | Checkbox | Cannot be forgotten (passport, meds, charger) |
| Weather-Dependent | Checkbox | Only needed based on weather conditions |
| Trip Type Relevant | Multi-select | Beach / City / Mountains / Business / Cold Weather / Tropical / Adventure / Any |
| Weight (oz) | Number | For weight-conscious packers |
| Notes | Text | Brand, size notes, alternatives |
| Template Item | Checkbox | Part of a reusable template (not trip-specific) |

**Views:**

- **Packing Checklist** — Filter by Trip, grouped by Category, showing Packed checkbox (main packing view)
- **Not Packed Yet** — Filter: Packed = false, current trip
- **Essentials** — Filter: Essential = true (double-check these last)
- **By Bag** — Table, grouped by Bag
- **Templates** — Filter: Template Item = true, grouped by Trip Type Relevant (for copying to new trips)
- **All Items** — Table, sorted by Category

### Pre-Built Packing Templates

Duplicate these for each trip type:

**Beach/Tropical:** Swimsuits x2, sunscreen, hat, sunglasses, sandals, cover-up, aloe vera, beach towel, waterproof phone case, reef-safe sunscreen

**City Break:** Walking shoes, smart casual outfit x2, jacket, umbrella, crossbody bag, portable charger, guidebook/app

**Business:** Suits/professional attire, dress shoes, laptop + charger, business cards, notebook, iron/steamer, extension cord

**Adventure/Hiking:** Hiking boots, moisture-wicking layers, rain jacket, headlamp, first aid kit, water bottle, trail snacks, sunscreen, hat, trekking poles

**Cold Weather:** Thermal base layers, heavy coat, gloves, scarf, beanie, wool socks, boots, hand warmers, lip balm

---

### 5. Budget / Expenses

**Purpose:** Tracks every expense for every trip — planned and actual. Organized by category with per-person splitting for group travel. Feeds rollups to the Trips database for real-time budget monitoring.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Expense | Title | What you spent money on |
| Trip | Relation | -> Trips database |
| Date | Date | When the expense occurred |
| Category | Select | Flights / Accommodation / Food & Drink / Transport / Activities / Shopping / Tips / Insurance / Visa / Communication / Laundry / Emergency / Misc |
| Amount (Local) | Number | Amount in local currency |
| Amount (USD) | Number | Converted to USD |
| Conversion Formula | Formula | `if(prop("Amount (Local)") == 0, 0, round(prop("Amount (Local)") / max(prop("Exchange Rate"), 1) * 100) / 100)` |
| Exchange Rate | Number | Local currency per 1 USD for this transaction |
| Payment Method | Select | Credit Card / Debit Card / Cash / Points / Prepaid / Venmo / Split |
| Paid By | Text | Who paid (for group splitting) |
| Split Between | Number | How many people splitting |
| Per Person | Formula | `if(prop("Split Between") == 0, prop("Amount (USD)"), round(prop("Amount (USD)") / prop("Split Between") * 100) / 100)` |
| Planned | Checkbox | Was this a planned/budgeted expense? |
| Necessary | Select | Essential / Nice-to-have / Splurge / Unexpected |
| Receipt | Files & media | Photo of receipt |
| Notes | Text | Context, worth it? |
| Day Number | Number | Which day of the trip |
| Linked Day | Relation | -> Itinerary Days |

**Views:**

- **All Expenses** — Table, sorted by Date descending
- **By Trip** — Table, grouped by Trip
- **By Category** — Table, grouped by Category (with sum of Amount USD)
- **By Day** — Table, grouped by Day Number
- **Daily Spending** — Table showing Date, total Amount USD per day
- **Splitting Summary** — Table showing Paid By, total amounts, Per Person calculations
- **Unplanned** — Filter: Planned = false (for budget analysis)
- **Splurges** — Filter: Necessary = Splurge
- **This Trip** — Filter by current trip, sorted by Date

---

## DASHBOARD

> Create this as the top-level page. It shows upcoming trips, current trip details, and past trip memories. Switch between planning mode and travel mode as needed.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  TRAVEL HQ                                                        |
+------------------------------------------------------------------+
|  UPCOMING TRIPS                                                   |
|  [Linked view -> Trips, Gallery, Status = Planning or Booked,     |
|   sorted by Start Date]                                           |
|                                                                    |
|  Japan 2026         Portland Weekend      Italy Sept              |
|  Jun 12 - Jun 26    May 22 - May 25       Sep 3 - Sep 17         |
|  32 days away        16 days away          120 days away          |
|  Budget: $8,000      Budget: $1,200        Budget: $6,500         |
|                                                                    |
+----------------------------------+-------------------------------+
|  NEXT TRIP: JAPAN 2026           |  BOOKING STATUS               |
|  Countdown: 32 days             |  [Linked view -> Bookings,    |
|  Budget: $3,200 / $8,000        |   this trip, sorted by Date]  |
|  Bookings: 8 confirmed          |                               |
|  Itinerary: 12/14 days planned  |  Flights: Confirmed           |
|                                  |  Hotels: 3/4 Booked           |
|                                  |  Activities: 5 Researching    |
+----------------------------------+-------------------------------+
|  PACKING LIST                    |  BUDGET TRACKER               |
|  [Linked view -> Packing,       |  [Linked view -> Budget,      |
|   next trip, Not Packed view]    |   this trip, by Category]     |
|  14/47 items packed             |                               |
+----------------------------------+-------------------------------+
|  CANCELLATION DEADLINES                                           |
|  [Linked view -> Bookings, Cancel By Date in next 14 days]       |
+------------------------------------------------------------------+
|  PAST TRIPS (Gallery)                                             |
|  [Linked view -> Trips, Status = Completed, with Cover Photos]   |
+------------------------------------------------------------------+
```

---

## EXPENSE SPLITTING SYSTEM

For group travel, track who paid what and calculate who owes whom:

### Per-Person Cost Formula

```
if(
  prop("Split Between") == 0,
  prop("Amount (USD)"),
  round(prop("Amount (USD)") / prop("Split Between") * 100) / 100
)
```

### How to Track Group Expenses

1. Every expense: record who "Paid By" and "Split Between" how many people
2. At end of trip, filter "By Trip" and group by "Paid By"
3. Sum each person's total payments
4. Calculate: Each person's fair share = Total Trip Cost / Number of Travelers
5. Difference between what each person paid and their fair share = settlement amount

### Currency Conversion Formula

```
if(
  prop("Amount (Local)") == 0,
  0,
  round(prop("Amount (Local)") / max(prop("Exchange Rate"), 1) * 100) / 100
)
```

Set Exchange Rate on each transaction (or use a consistent daily rate for the trip).

---

## KEY FORMULA REFERENCE

### Trip Duration

```
if(
  and(not(empty(prop("Start Date"))), not(empty(prop("End Date")))),
  format(dateBetween(prop("End Date"), prop("Start Date"), "days")) + " days",
  "TBD"
)
```

### Days Until Trip

```
if(
  empty(prop("Start Date")),
  "No date",
  if(
    prop("Start Date") > now(),
    format(dateBetween(prop("Start Date"), now(), "days")) + " days away",
    if(
      and(prop("Start Date") <= now(), prop("End Date") >= now()),
      "Currently traveling!",
      "Completed"
    )
  )
)
```

### Budget Status

```
if(
  prop("Total Budget") == 0,
  "No budget set",
  if(
    prop("Actual Spend") > prop("Total Budget"),
    "Over Budget!",
    if(
      prop("Actual Spend") / prop("Total Budget") > 0.85,
      "Almost at limit",
      "On Track"
    )
  )
)
```

### Per Day Budget

```
if(
  or(prop("Total Budget") == 0, prop("Duration") == "TBD"),
  0,
  round(prop("Total Budget") / toNumber(replace(prop("Duration"), " days", "")))
)
```

### Booking Cost Per Person

```
if(
  prop("Travelers Splitting") == 0,
  prop("Cost"),
  round(prop("Cost") / prop("Travelers Splitting") * 100) / 100
)
```

### Days Until Booking

```
if(
  empty(prop("Date")),
  "No date",
  if(
    prop("Date") < now(),
    "Past",
    format(dateBetween(prop("Date"), now(), "days")) + " days"
  )
)
```

---

## QUICK-START GUIDE

### Step 1 — Create Your Trip (5 minutes)

- Open the **Trips** database
- Add a new trip with Name, Destination, Start/End Dates, Travelers
- Set Total Budget and Status (Planning or Booked)
- Add any known Trip Notes (visa info, emergency contacts)

### Step 2 — Build Your Itinerary (20 minutes per trip)

- Open **Itinerary Days** and create one entry per day of your trip
- Name each day: "Day 1 — Arrival", "Day 2 — [Theme]", etc.
- Fill in Morning, Afternoon, Evening blocks with activities and times
- Add transportation between locations
- Note any timed reservations
- Set the Must-Do for each day (the one unmissable thing)

### Step 3 — Add Bookings (15 minutes)

- Open **Bookings** and add every reservation you've made
- Include: Confirmation #, Cost, Date, Time, and Cancellation Policy
- Upload confirmation PDFs to the Documents field
- Link each booking to its relevant Itinerary Day
- Check Cancellation Deadlines view for anything with a "Cancel By" date

### Step 4 — Set Your Budget (10 minutes)

- Open **Budget/Expenses** and add any pre-trip expenses already paid (flights, hotels, deposits)
- Set category for each
- During the trip: add expenses daily (takes 2 minutes with mobile Notion)
- The Trip record will automatically show running totals vs. budget

### Step 5 — Pack with the Checklist (before departure)

- Open **Packing Lists** and duplicate a template for your trip type
- Customize: remove irrelevant items, add trip-specific ones
- Check items off as you pack
- Use "Essentials" view as your final check before leaving

### Step 6 — During the Trip

- Check **Today's Itinerary** each morning
- Reference **This Trip Bookings** for confirmation numbers
- Log expenses in **Budget** at end of each day (or use receipts to batch-enter)
- Fill in Day Rating and Highlight each evening (optional but creates great memories)

### Step 7 — After the Trip

- Set Trip Status = Completed
- Add Trip Rating and Highlights
- Upload a Cover Photo
- Review budget: was your estimate accurate? Use this for future trip budgeting
- Optional: fill in Highlight field on each Itinerary Day for a trip journal

### Pro Tips

- Keep your Itinerary flexible — plan 60% of each day, leave 40% for wandering and discovery. Over-planned trips feel like work.
- Always record Cancellation Policy and Cancel By dates. Free cancellation bookings can be made speculatively and cancelled if plans change — but only if you track the deadline.
- For group trips, designate one "Paid By" person per day to simplify splitting. Rotate who pays. Settle up after the trip using the Splitting Summary view.
- Use the Map Link field on Itinerary Days to save a Google Maps route with all the day's pins. Pull it up on your phone each morning.
- The Backup Plan field on Itinerary Days is a lifesaver for weather-dependent activities. Always have a rainy-day alternative.
- Add a "Dream List" trip for every destination that interests you. When it's time to plan, you already have a curated list instead of decision paralysis.
- Packing Templates are reusable — create once per trip type, duplicate forever. After 5+ trips, your templates become perfectly calibrated to your actual packing needs.
