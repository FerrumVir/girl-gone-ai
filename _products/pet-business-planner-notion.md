# Pet Business Planner — Notion Template

> Duplicate this page into your Notion workspace to get started. All six databases are pre-linked and all formulas are pre-built. Read the Quick-Start Guide at the bottom before entering real data — it will save you time.

---

## DATABASES

---

### 1. Clients

**Purpose:** Master record for every pet parent you work with — active clients, past clients, prospects, and referral sources.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Client Name | Title | Full name of the pet parent |
| Email | Email | Primary contact email |
| Phone | Phone | Mobile — this is how most pet clients communicate |
| Address | Text | Service address (where the pet is) |
| Address Notes | Text | Gate codes, key locations, parking instructions, alarm codes |
| Preferred Contact | Select | Text / Call / Email / App Message |
| How They Found You | Select | Referral / Google / Instagram / Nextdoor / Rover / Yelp / Facebook / Walk-By / Repeat Client / Other |
| Referred By | Relation | → Clients database (self-referential) |
| Client Status | Select | Active / Paused / Inactive / Prospect / Do Not Service |
| Client Since | Date | When they became a client |
| Billing Preference | Select | Per Visit / Weekly / Bi-Weekly / Monthly / Package |
| Payment Method | Select | Venmo / Zelle / Cash / Check / Credit Card / PayPal / Other |
| Outstanding Balance | Rollup | Sum of Amount from linked Revenue entries where Status = Pending or Overdue |
| Total Revenue | Rollup | Sum of Amount from linked Revenue entries where Status = Paid |
| Last Appointment | Rollup | Max of Date from linked Appointments |
| Days Since Last Visit | Formula | `if(empty(prop("Last Appointment")), "No visits", format(dateBetween(now(), prop("Last Appointment"), "days")) + " days ago")` |
| Number of Pets | Rollup | Count of linked Pet Profiles |
| Appointment Count | Rollup | Count of linked Appointments |
| Emergency Contact Name | Text | Someone other than the client to call in an emergency |
| Emergency Contact Phone | Phone | |
| Notes | Text | Preferences, quirks, scheduling patterns, communication style |
| Linked Pets | Relation | → Pet Profiles database |
| Linked Appointments | Relation | → Appointments database |
| Linked Revenue | Relation | → Revenue Tracker database |
| Tags | Multi-select | VIP / Regular / Occasional / Holiday Only / New / Difficult / Great Tipper / Flexible Schedule / Strict Schedule |

**Views:**

- **All Clients** — Table, sorted by Client Name ascending
- **Active Clients** — Filter: Client Status = Active, sorted by Client Name
- **Needs Follow-Up** — Filter: Days Since Last Visit > 30, Client Status = Active or Paused
- **Outstanding Balances** — Filter: Outstanding Balance > 0, sorted by Outstanding Balance descending
- **By Revenue** — Table, sorted by Total Revenue descending (your best clients)
- **By Referral Source** — Table, grouped by How They Found You
- **Prospects** — Filter: Client Status = Prospect
- **Client Cards** — Gallery view, grouped by Client Status

---

### 2. Pet Profiles

**Purpose:** Detailed record for every animal in your care. This is your operational reference — review it before every visit.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Pet Name | Title | The animal's name |
| Owner | Relation | → Clients database |
| Owner Name | Rollup | Client Name from linked Client |
| Owner Phone | Rollup | Phone from linked Client |
| Species | Select | Dog / Cat / Bird / Rabbit / Reptile / Fish / Hamster / Guinea Pig / Ferret / Other |
| Breed | Text | Specific breed or mix |
| Color/Markings | Text | Physical description for identification |
| Age | Text | Age or estimated age (e.g., "4 years" or "~2 years, adopted 2024") |
| Date of Birth | Date | If known |
| Weight (lbs) | Number | Current weight — important for medication dosing and handling |
| Sex | Select | Male / Female / Male (Neutered) / Female (Spayed) |
| Microchip Number | Text | For identification if lost |
| Temperament | Select | Calm / Friendly / Anxious / Reactive / Aggressive / Shy / High Energy / Stubborn / Playful |
| Temperament Notes | Text | Detailed behavioral notes — triggers, fears, preferences |
| Leash Behavior | Select | Great / Good / Pulls / Reactive on Leash / Not Leash Trained |
| Good with Dogs | Select | Yes / Yes with Introduction / Selective / No / Unknown |
| Good with Cats | Select | Yes / No / Unknown |
| Good with Children | Select | Yes / Supervised Only / No / Unknown |
| Feeding Instructions | Text | What, how much, when, where the food is stored, any dietary restrictions |
| Feeding Schedule | Text | Specific times — e.g., "7 AM and 5 PM, 1 cup kibble + 1 tbsp wet food" |
| Medications | Text | Name, dosage, frequency, administration method, where stored |
| Medication Schedule | Text | Specific times and instructions |
| Allergies | Text | Food allergies, environmental allergies, medication allergies |
| Special Needs | Text | Mobility issues, blindness, deafness, anxiety protocols, crate requirements |
| Vet Name | Text | Primary veterinarian |
| Vet Phone | Phone | |
| Vet Address | Text | |
| Emergency Vet | Text | Nearest 24-hour emergency vet clinic name and address |
| Last Vet Visit | Date | |
| Grooming Notes | Text | Coat type, preferred cut, matting concerns, sensitive areas, grooming frequency |
| Favorite Toys/Treats | Text | What motivates them — useful for walks and sitting |
| Where to Walk | Text | Preferred routes, areas to avoid, off-leash parks they're trained for |
| House Rules | Text | Allowed on furniture? Crate at night? Specific rooms off-limits? |
| Photo | Files | Upload a photo for quick identification |
| Status | Select | Active / Deceased / Rehomed / No Longer a Client |
| Linked Appointments | Relation | → Appointments database |
| Linked Vaccinations | Relation | → Vaccination & Medical Records database |
| Tags | Multi-select | Senior / Puppy / Special Needs / Flight Risk / Resource Guarder / Separation Anxiety / Diabetic / Heart Condition |

**Views:**

- **All Pets** — Table, sorted by Pet Name ascending
- **Active Pets** — Filter: Status = Active, sorted by Pet Name
- **By Owner** — Table, grouped by Owner Name
- **Dogs** — Filter: Species = Dog
- **Cats** — Filter: Species = Cat
- **Special Needs** — Filter: Tags contains Special Needs or Senior or Diabetic or Heart Condition
- **Pet Cards** — Gallery view with photo, grouped by Species
- **Needs Vet Visit** — Filter: Last Vet Visit is more than 365 days ago, Status = Active

---

### 3. Appointments

**Purpose:** Every scheduled service — past, present, and future. Your operational calendar and the source of truth for what happened and when.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Appointment Title | Title | Auto-format: "[Pet Name] — [Service] — [Date]" |
| Client | Relation | → Clients database |
| Client Name | Rollup | From Client relation |
| Pet(s) | Relation | → Pet Profiles database (can link multiple pets for multi-pet households) |
| Pet Names | Rollup | From Pet relation |
| Service | Relation | → Services & Pricing database |
| Service Name | Rollup | From Service relation |
| Service Price | Rollup | Price from linked Service |
| Date | Date | Appointment date and start time |
| End Time | Date | Expected end time |
| Duration (min) | Number | Planned duration |
| Status | Select | Scheduled / Confirmed / In Progress / Completed / Cancelled / No Show / Rescheduled |
| Confirmation Sent | Checkbox | Did you send a 24-hour confirmation? |
| Needs Confirmation | Formula | `if(and(not(prop("Confirmation Sent")), prop("Status") == "Scheduled", dateBetween(prop("Date"), now(), "hours") <= 48, dateBetween(prop("Date"), now(), "hours") > 0), true, false)` |
| Payment Status | Select | Paid / Pending / Overdue / Waived / Included in Package |
| Amount Charged | Number (USD) | Actual amount charged (may differ from service price for add-ons or discounts) |
| Tip | Number (USD) | |
| Payment Method | Select | Venmo / Zelle / Cash / Check / Credit Card / PayPal / Other |
| Notes | Text | Visit notes — how the pet was, anything the owner should know |
| Report to Owner | Text | Summary to send to the client after the visit (photos, behavior, potty, etc.) |
| Recurring | Checkbox | Is this a standing appointment? |
| Recurrence | Select | Daily / Mon-Fri / MWF / Tu-Th / Weekly / Bi-Weekly / Monthly |
| Weather Conditions | Select | Clear / Hot / Cold / Rain / Snow / Extreme Heat / Extreme Cold |
| Linked Revenue | Relation | → Revenue Tracker database |
| Created | Date | When the appointment was booked |
| Tags | Multi-select | First Visit / Meet & Greet / Holiday Rate / Last Minute / Group Walk / Solo Walk / Extended Visit |

**Views:**

- **All Appointments** — Table, sorted by Date descending
- **Today's Schedule** — Filter: Date is today, sorted by Date ascending (your daily view)
- **This Week** — Filter: Date is this week, sorted by Date ascending
- **Upcoming** — Filter: Status = Scheduled or Confirmed, Date is in the future, sorted by Date ascending
- **Needs Confirmation** — Filter: Needs Confirmation = true (send these clients a message)
- **Unpaid** — Filter: Payment Status = Pending or Overdue, Status = Completed
- **Daily Board** — Kanban, grouped by Status
- **Calendar** — Calendar view, by Date
- **By Client** — Table, grouped by Client Name
- **Cancelled / No Shows** — Filter: Status = Cancelled or No Show
- **Recurring Schedule** — Filter: Recurring = true, sorted by Recurrence

---

### 4. Services & Pricing

**Purpose:** Your complete service menu. Every service you offer, with pricing, duration, and description. Linked to appointments so revenue calculations are automatic.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Service Name | Title | Clear name — e.g., "30-Minute Dog Walk" |
| Category | Select | Dog Walking / Pet Sitting / Overnight Sitting / Grooming / Bath / Nail Trim / Training / Puppy Visit / Meet & Greet / Transportation / Medication Administration / Other |
| Description | Text | What's included in this service |
| Duration (min) | Number | Standard duration |
| Price | Number (USD) | Standard price |
| Holiday Price | Number (USD) | Holiday/weekend premium rate |
| Additional Pet Price | Number (USD) | Add-on price per additional pet from same household |
| Active | Checkbox | Is this service currently offered? |
| Total Bookings | Rollup | Count of linked Appointments |
| Total Revenue | Rollup | Sum of Amount Charged from linked Appointments where Payment Status = Paid |
| Revenue per Booking | Formula | `if(prop("Total Bookings") > 0, round(prop("Total Revenue") / prop("Total Bookings") * 100) / 100, 0)` |
| Notes | Text | Special requirements, equipment needed, seasonal availability |
| Linked Appointments | Relation | → Appointments database |

**Pre-loaded Services:**

| Service | Category | Duration | Price |
|---|---|---|---|
| 30-Minute Dog Walk | Dog Walking | 30 | $20 |
| 60-Minute Dog Walk | Dog Walking | 60 | $35 |
| Group Dog Walk (30 min) | Dog Walking | 30 | $15 |
| Drop-In Pet Visit (30 min) | Pet Sitting | 30 | $22 |
| Drop-In Pet Visit (60 min) | Pet Sitting | 60 | $38 |
| Overnight Pet Sitting | Overnight Sitting | 720 | $75 |
| Puppy Visit (30 min) | Puppy Visit | 30 | $25 |
| Full Groom — Small Dog | Grooming | 90 | $55 |
| Full Groom — Medium Dog | Grooming | 120 | $70 |
| Full Groom — Large Dog | Grooming | 150 | $90 |
| Bath & Brush — Small Dog | Bath | 45 | $30 |
| Bath & Brush — Medium Dog | Bath | 60 | $40 |
| Bath & Brush — Large Dog | Bath | 75 | $50 |
| Nail Trim | Nail Trim | 15 | $15 |
| Medication Administration | Medication Administration | 15 | $5 (add-on) |
| Pet Transportation | Transportation | 30 | $25 |
| Meet & Greet | Meet & Greet | 30 | Free |
| Dog Training Session (60 min) | Training | 60 | $65 |

**Views:**

- **Full Menu** — Table, sorted by Category then Service Name
- **Active Services** — Filter: Active = true
- **By Category** — Table, grouped by Category
- **By Revenue** — Table, sorted by Total Revenue descending
- **Price List** — Table, showing only Service Name, Duration, Price, Holiday Price (share with clients)

---

### 5. Revenue Tracker

**Purpose:** Every dollar that comes in or is owed. Your financial record of truth.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | Auto-format: "[Client] — [Service] — [Date]" |
| Date | Date | Payment date or service date |
| Client | Relation | → Clients database |
| Client Name | Rollup | From Client relation |
| Appointment | Relation | → Appointments database |
| Service | Rollup | Service Name from linked Appointment |
| Amount | Number (USD) | Amount charged |
| Tip | Number (USD) | Tip received |
| Total Received | Formula | `prop("Amount") + prop("Tip")` |
| Payment Method | Select | Venmo / Zelle / Cash / Check / Credit Card / PayPal / Other |
| Status | Select | Paid / Pending / Overdue / Waived / Refunded |
| Days Outstanding | Formula | `if(and(or(prop("Status") == "Pending", prop("Status") == "Overdue"), not(empty(prop("Date")))), dateBetween(now(), prop("Date"), "days"), 0)` |
| Invoice Sent | Checkbox | |
| Invoice Number | Text | If you use invoicing |
| Notes | Text | Discounts, package credits, special arrangements |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Tags | Multi-select | Holiday Rate / Discount / Package / First Visit / Referral Bonus |

**Views:**

- **All Revenue** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month, sorted by Date descending
- **This Week** — Filter: Date is this week
- **Pending Payments** — Filter: Status = Pending, sorted by Date ascending (oldest first)
- **Overdue** — Filter: Status = Overdue or (Status = Pending AND Days Outstanding > 7)
- **By Client** — Table, grouped by Client Name, sorted by Total Received descending
- **By Month** — Table, grouped by Month
- **By Payment Method** — Table, grouped by Payment Method
- **Cash Received** — Filter: Payment Method = Cash (important for tax tracking)

---

### 6. Vaccination & Medical Records

**Purpose:** Complete health records for every pet in your care. Protects the animals, protects your business, and gives clients confidence.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Record Title | Title | "[Pet Name] — [Vaccine/Record Type]" |
| Pet | Relation | → Pet Profiles database |
| Pet Name | Rollup | From Pet relation |
| Owner | Rollup | Owner Name via Pet → Client |
| Record Type | Select | Vaccination / Medication / Allergy / Surgery / Condition / Vet Visit / Lab Work / Dental / Other |
| Vaccine Name | Select | Rabies / DHPP (Distemper) / Bordetella / Canine Influenza / Leptospirosis / Lyme / FVRCP (Cat) / FeLV (Cat) / Other |
| Date Administered | Date | When the vaccine was given or record was created |
| Expiration Date | Date | When this vaccine expires |
| Days Until Expiration | Formula | `if(empty(prop("Expiration Date")), 999, dateBetween(prop("Expiration Date"), now(), "days"))` |
| Expired | Formula | `if(and(not(empty(prop("Expiration Date"))), prop("Expiration Date") < now()), true, false)` |
| Expiring Soon | Formula | `if(and(not(prop("Expired")), prop("Days Until Expiration") <= 30, prop("Days Until Expiration") >= 0), true, false)` |
| Administered By | Text | Vet name or clinic |
| Lot Number | Text | Vaccine lot number if provided |
| Dosage | Text | For medications |
| Frequency | Text | For ongoing medications |
| Side Effects | Text | Any reactions observed |
| Document | Files | Upload vaccination certificate or vet records |
| Notes | Text | Additional context |
| Status | Select | Current / Expired / Discontinued |
| Verified | Checkbox | Have you seen the original documentation? |

**Views:**

- **All Records** — Table, sorted by Date Administered descending
- **By Pet** — Table, grouped by Pet Name
- **Current Vaccinations** — Filter: Record Type = Vaccination, Status = Current
- **Expiring Soon** — Filter: Expiring Soon = true, sorted by Expiration Date ascending
- **Expired** — Filter: Expired = true, Status = Current (needs attention)
- **Unverified** — Filter: Verified = false (request documentation from client)
- **Medications** — Filter: Record Type = Medication
- **Allergies** — Filter: Record Type = Allergy

---

## DASHBOARD

> Create this as the top-level Notion page. Pin it to your sidebar. Check it every morning as your daily business briefing.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  PET BUSINESS COMMAND CENTER             April 2026           |
+--------------+--------------+--------------+-----------------+
|  Today's     |  This Week   |  Pending     |  Vaccines       |
|  Appointments|  Revenue     |  Payments    |  Expiring       |
|     5        |  $485        |  $120        |     2           |
+--------------+--------------+--------------+-----------------+
|  TODAY'S SCHEDULE                                             |
|  [Linked view → Appointments, filter: Date = today,          |
|   sorted by Date ascending]                                  |
+-------------------------------------------------------------+
|  NEEDS CONFIRMATION                                           |
|  [Linked view → Appointments, filter: Needs Confirmation      |
|   = true]                                                    |
+-----------------------------+-------------------------------+
|  PENDING PAYMENTS           |  UPCOMING THIS WEEK            |
|  [Linked view → Revenue,    |  [Linked view → Appointments,  |
|   filter: Status = Pending  |   filter: Date is this week,   |
|   or Overdue]               |   Status = Scheduled/Confirmed]|
+-----------------------------+-------------------------------+
|  VACCINES EXPIRING SOON                                       |
|  [Linked view → Vaccination Records, filter: Expiring Soon    |
|   = true or Expired = true]                                  |
+-------------------------------------------------------------+
|  TOP CLIENTS (by revenue)                                     |
|  [Linked view → Clients, sorted by Total Revenue desc,        |
|   limit 10]                                                  |
+-------------------------------------------------------------+
```

### Dashboard Summary Stats

Create four callout blocks side by side:

- **Today's Appointments** — Count from Appointments filtered to today
- **This Week's Revenue** — Sum from Revenue Tracker filtered to this week, Status = Paid
- **Pending Payments** — Sum from Revenue Tracker where Status = Pending or Overdue
- **Vaccines Expiring** — Count from Vaccination Records where Expiring Soon = true or Expired = true

---

## KEY FORMULA REFERENCE

### Days Since Last Visit (Clients database)
Shows how long since you last serviced this client. Used to surface clients going cold in the "Needs Follow-Up" view.

```
if(
  empty(prop("Last Appointment")),
  "No visits",
  format(dateBetween(now(), prop("Last Appointment"), "days")) + " days ago"
)
```

### Needs Confirmation (Appointments database)
Flags appointments within the next 48 hours that haven't been confirmed yet. Check this view every evening.

```
if(
  and(
    not(prop("Confirmation Sent")),
    prop("Status") == "Scheduled",
    dateBetween(prop("Date"), now(), "hours") <= 48,
    dateBetween(prop("Date"), now(), "hours") > 0
  ),
  true,
  false
)
```

### Vaccine Expiring Soon (Vaccination Records database)
Surfaces any vaccination that expires within 30 days. Gives you time to notify the client before it becomes a problem.

```
if(
  and(
    not(prop("Expired")),
    prop("Days Until Expiration") <= 30,
    prop("Days Until Expiration") >= 0
  ),
  true,
  false
)
```

### Days Outstanding (Revenue Tracker database)
Calculates how many days a payment has been pending. Used to auto-flag overdue payments.

```
if(
  and(
    or(prop("Status") == "Pending", prop("Status") == "Overdue"),
    not(empty(prop("Date")))
  ),
  dateBetween(now(), prop("Date"), "days"),
  0
)
```

### Revenue per Booking (Services database)
Shows actual average revenue per booking for each service type, accounting for add-ons and discounts.

```
if(
  prop("Total Bookings") > 0,
  round(prop("Total Revenue") / prop("Total Bookings") * 100) / 100,
  0
)
```

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Services (10 minutes)
- Open the **Services & Pricing** database
- Review the pre-loaded services and adjust prices to match your rates
- Add any services you offer that aren't listed
- Remove or uncheck "Active" for services you don't offer
- This is the foundation — appointments and revenue link back to these

### Step 2 — Add Your Clients (15 minutes)
- Open the **Clients** database and add your current active clients
- At minimum, fill in: Client Name, Phone, Address, Client Status, Payment Method
- Add Address Notes (gate codes, key locations) — you'll thank yourself on the next visit
- Start with your most active clients; add the rest as they book

### Step 3 — Add Their Pets (15 minutes)
- Open the **Pet Profiles** database and add each client's pet(s)
- Link each pet to their Owner using the Owner relation
- At minimum: Pet Name, Species, Breed, Temperament, Feeding Instructions
- Add medications, allergies, and behavioral notes — this is your safety reference
- Upload a photo if you have one

### Step 4 — Enter Vaccination Records (10 minutes per pet)
- Open the **Vaccination & Medical Records** database
- For each pet, add their current vaccinations with expiration dates
- Request documentation from clients if you don't have it — use the "Unverified" view
- The "Expiring Soon" view will start working immediately

### Step 5 — Schedule Your Appointments
- Open the **Appointments** database
- Add your upcoming appointments for this week
- Link each to the Client, Pet(s), and Service
- Set Status to "Scheduled"
- For recurring clients, check "Recurring" and set the Recurrence pattern

### Step 6 — Start Tracking Revenue
- As appointments are completed, create entries in the **Revenue Tracker**
- Link each entry to the Appointment, Client, and set Status (Paid/Pending)
- The "Pending Payments" view will immediately show you who owes what

### Step 7 — Set Up Your Dashboard
- Create a new Notion page titled "Pet Business Command Center"
- Add linked database views for each section described in the Dashboard Layout above
- Pin this page to your sidebar — check it every morning

### Daily Rhythm (10 minutes)

**Every morning:**
- Open the Dashboard
- Review Today's Schedule — confirm you have all the info you need for each visit
- Check "Needs Confirmation" — send a confirmation text to unconfirmed appointments
- Check "Pending Payments" — send a reminder to anyone overdue

**After every visit:**
- Update the Appointment status to "Completed"
- Add visit notes and a Report to Owner
- Log payment in Revenue Tracker (or mark as Pending if not yet paid)

**Every evening:**
- Check tomorrow's schedule
- Review pet profiles for tomorrow's visits — refresh your memory on medications, feeding, and behavioral notes
- Send tomorrow's confirmation texts

### Weekly Rhythm (15 minutes, Sunday evening)

- Review the "Needs Follow-Up" view in Clients — re-engage anyone you haven't seen in 30+ days
- Check "Expiring Soon" in Vaccination Records — notify clients whose pets need updated records
- Review weekly revenue in the Revenue Tracker
- Plan next week's schedule

### Monthly Rhythm (30 minutes)

- Review revenue by service type — which services are most profitable?
- Review revenue by client — who are your best clients?
- Check for any overdue payments older than 30 days
- Update service pricing if needed

### Pro Tips

- Take 30 seconds after each visit to write notes in the Appointment record. "Bailey pulled toward the small brown dog at Oak Park again" is the kind of note that prevents incidents.
- Use the "Report to Owner" field to send clients a quick summary after each visit. Even a two-sentence text about how their pet did builds trust and justifies your rates.
- The "Outstanding Balance" rollup on the Client record shows total unpaid amounts. Check this before accepting a new booking from a client with a balance.
- Set Holiday Prices in the Services database and reference them for holiday bookings. Don't forget to charge your holiday rate — you're working when others aren't.
- When a new client does a Meet & Greet, fill out the Pet Profile completely during the visit. Doing it in person is 10x faster than trying to get the info over text later.
- Flag pets with "Flight Risk" tag if they're door dashers or have a history of slipping collars. This note could prevent a disaster.
- Back up vaccination records by uploading the actual documents to the Files property. If a client claims their pet is up to date but can't produce records, you have a copy.
- Track Cash payments diligently using the "Cash Received" view. This is essential for accurate tax reporting.
