# Beauty Business Booking & CRM — Notion Template

> Duplicate this template into your Notion workspace. All databases are pre-linked with relations and rollups. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Clients

**Purpose:** Complete client database with contact info, preferences, visit history, and lifetime value tracking.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Client Name | Title | First and last name |
| Phone | Phone | Primary contact number |
| Email | Email | For confirmations and marketing |
| Instagram | URL | Their IG handle for tagging/reposting |
| Birthday | Date | Send birthday offers |
| Referral Source | Select | Instagram / TikTok / Google / Referral / Walk-In / Yelp / Other |
| Referred By | Relation | -> Clients database (self-referral tracking) |
| Client Since | Date | Date of first appointment |
| VIP Status | Formula | `if(prop("Total Spent") >= 2000, "VIP Gold", if(prop("Total Spent") >= 1000, "VIP Silver", if(prop("Total Spent") >= 500, "Regular+", "New")))` |
| Skin Type | Select | Normal / Dry / Oily / Combination / Sensitive |
| Skin Concerns | Multi-select | Acne / Aging / Hyperpigmentation / Rosacea / Dehydration / Texture / Scarring / None |
| Allergies | Text | Latex, specific ingredients, adhesives, etc. |
| Preferences | Text | Preferred pressure, temperature, music, conversation level |
| Products Used | Text | At-home products they currently use |
| Notes | Text | General notes, personal details to remember |
| Appointments | Relation | -> Appointments database |
| Total Appointments | Rollup | Count of linked Appointments |
| Total Spent | Rollup | Sum of Total Paid from linked Appointments |
| Last Visit | Rollup | Latest Date from linked Appointments |
| Days Since Last Visit | Formula | `dateBetween(now(), prop("Last Visit"), "days")` |
| Needs Follow-Up | Formula | `if(prop("Days Since Last Visit") > 42, true, false)` |
| Avg Ticket | Formula | `if(prop("Total Appointments") > 0, prop("Total Spent") / prop("Total Appointments"), 0)` |
| Tags | Multi-select | Consistent / At-Risk / Lapsed / High-Spender / Referral-Machine / New-Client |

**Views:**

- **All Clients** — Table, sorted by Client Name
- **Client Cards** — Gallery view showing name, VIP status, last visit, total spent
- **VIP Clients** — Filter: VIP Status = "VIP Gold" or "VIP Silver"
- **Needs Follow-Up** — Filter: Needs Follow-Up = true, sorted by Days Since Last Visit descending
- **New Clients (Last 30 Days)** — Filter: Client Since is within past 30 days
- **By Referral Source** — Table grouped by Referral Source
- **At-Risk** — Filter: Days Since Last Visit > 60 AND Total Appointments > 2
- **Birthdays This Month** — Filter: Birthday month = current month
- **Top Spenders** — Table sorted by Total Spent descending, top 20

---

### 2. Services

**Purpose:** Service menu with pricing, duration, cost analysis, and booking settings.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Service Name | Title | Full service name as listed on menu |
| Category | Select | Facial / Lash / Brow / Wax / Peel / Body / Add-On / Package |
| Duration | Number | Minutes (include buffer time) |
| Buffer Time | Number | Minutes between appointments for cleanup/prep |
| Total Block | Formula | `prop("Duration") + prop("Buffer Time")` |
| Price | Number (USD) | Retail price charged to client |
| Product Cost | Number (USD) | Cost of products/supplies used per service |
| Profit Margin | Formula | `if(prop("Price") > 0, round((prop("Price") - prop("Product Cost")) / prop("Price") * 100), 0)` |
| Hourly Rate | Formula | `if(prop("Duration") > 0, prop("Price") / (prop("Duration") / 60), 0)` |
| Description | Text | What's included (for booking page) |
| Aftercare | Text | Post-service instructions to send to client |
| Frequency | Select | Weekly / Bi-Weekly / Monthly / 6 Weeks / 8 Weeks / Quarterly / One-Time |
| Active | Checkbox | Currently offering this service |
| Appointments | Relation | -> Appointments database |
| Times Booked | Rollup | Count of linked Appointments |
| Total Revenue | Rollup | Sum of Service Price from linked Appointments |
| Popularity Rank | Formula | `prop("Times Booked")` (sort descending to see most popular) |

**Views:**

- **Full Menu** — Table filtered: Active = true, grouped by Category
- **Pricing Sheet** — Table showing: Service Name, Duration, Price, grouped by Category
- **Profitability** — Table sorted by Hourly Rate descending
- **Add-Ons** — Filter: Category = Add-On
- **Packages** — Filter: Category = Package
- **Inactive** — Filter: Active = false

---

### 3. Appointments

**Purpose:** Every appointment tracked with status, payment, and service details.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Appointment | Title | Auto-format: "[Client] — [Service] — [Date]" |
| Client | Relation | -> Clients database |
| Service | Relation | -> Services database |
| Date | Date | Appointment date and start time |
| End Time | Formula | `dateAdd(prop("Date"), prop("Service Duration"), "minutes")` |
| Service Duration | Rollup | Duration from linked Service |
| Status | Select | Booked / Confirmed / Completed / No-Show / Cancelled / Rescheduled |
| Service Price | Rollup | Price from linked Service |
| Add-Ons | Multi-select | List any add-on services included |
| Add-On Revenue | Number (USD) | Total of add-on services |
| Discount | Number (USD) | Any discount applied |
| Total Paid | Formula | `prop("Service Price") + prop("Add-On Revenue") - prop("Discount")` |
| Payment Method | Select | Cash / Card / Venmo / Zelle / CashApp / Gift Card / Comp |
| Tip | Number (USD) | Tip amount received |
| Products Sold | Text | Retail products sold during this appointment |
| Product Revenue | Number (USD) | Retail product sales |
| Notes | Text | Service notes, what was done, client feedback |
| Before Photo | Files & media | Upload before photos |
| After Photo | Files & media | Upload after photos |
| Follow-Up Sent | Checkbox | Did you send a follow-up message? |
| Rebook Date | Date | When they rebooked for |
| Rebooked | Checkbox | Did client rebook before leaving? |

**Views:**

- **Today** — Filter: Date = today, sorted by time
- **This Week** — Filter: Date is within this week, sorted by Date
- **Calendar** — Calendar view by Date
- **Upcoming** — Filter: Date is after today AND Status = Booked or Confirmed
- **Completed** — Filter: Status = Completed, sorted by Date descending
- **No-Shows** — Filter: Status = No-Show
- **Revenue This Month** — Filter: Date is within this month AND Status = Completed, showing sum of Total Paid
- **Needs Follow-Up** — Filter: Follow-Up Sent = false AND Status = Completed AND Date is within past 3 days
- **Not Rebooked** — Filter: Rebooked = false AND Status = Completed AND Date is within past 7 days

---

### 4. Follow-Ups

**Purpose:** Automated follow-up task list to maintain client relationships and drive rebookings.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Task | Title | Description of follow-up action |
| Client | Relation | -> Clients database |
| Type | Select | Post-Appointment / Rebooking Reminder / Birthday / Re-Engagement / Review Request / Thank You |
| Due Date | Date | When to send/complete |
| Status | Select | Pending / Sent / Completed / Skipped |
| Priority | Select | High / Medium / Low |
| Message Template | Text | Pre-written message to send |
| Channel | Select | Text / Email / DM / Call |
| Notes | Text | Additional context |
| Linked Appointment | Relation | -> Appointments database |

**Views:**

- **Today's Follow-Ups** — Filter: Due Date = today AND Status = Pending
- **This Week** — Filter: Due Date is within this week AND Status = Pending
- **Overdue** — Filter: Due Date is before today AND Status = Pending
- **By Type** — Table grouped by Type
- **Completed** — Filter: Status = Sent or Completed

---

### 5. Revenue Tracker

**Purpose:** Monthly revenue overview pulling data from appointments.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Month | Title | Format: "2026-01 January" |
| Service Revenue | Number (USD) | Total from services completed |
| Add-On Revenue | Number (USD) | Total from add-on services |
| Product Revenue | Number (USD) | Total retail product sales |
| Tips | Number (USD) | Total tips received |
| Gross Revenue | Formula | `prop("Service Revenue") + prop("Add-On Revenue") + prop("Product Revenue") + prop("Tips")` |
| Total Appointments | Number | Number of completed appointments |
| No-Shows | Number | Number of no-shows |
| Cancellations | Number | Number of cancellations |
| No-Show Rate | Formula | `if(prop("Total Appointments") + prop("No-Shows") > 0, round(prop("No-Shows") / (prop("Total Appointments") + prop("No-Shows")) * 100), 0)` |
| New Clients | Number | First-time clients this month |
| Rebook Rate | Number | Percentage of clients who rebooked |
| Avg Ticket | Formula | `if(prop("Total Appointments") > 0, prop("Service Revenue") / prop("Total Appointments"), 0)` |
| Goal | Number (USD) | Monthly revenue goal |
| vs Goal | Formula | `if(prop("Goal") > 0, round(prop("Gross Revenue") / prop("Goal") * 100), 0)` |
| Working Days | Number | Days you worked this month |
| Revenue Per Day | Formula | `if(prop("Working Days") > 0, prop("Gross Revenue") / prop("Working Days"), 0)` |

**Views:**

- **Monthly Overview** — Table sorted by Month descending
- **Year at a Glance** — Table filtered to current year
- **Goal Tracking** — Table showing Month, Gross Revenue, Goal, vs Goal

---

## DASHBOARD

### Layout

```
+----------------------------------------------------------+
|  BEAUTY BIZ HQ — [Month Year]                             |
+-------------+-------------+-------------+-----------------+
|  Revenue    |  Clients    | Appointments|  Rebook Rate    |
|  This Month |  Total      | This Week   |                 |
|  $4,280     |  127        |  18         |  72%            |
+-------------+-------------+-------------+-----------------+
|  TODAY'S SCHEDULE                                          |
|  [Linked view -> Appointments, filter: today]             |
|  9:00  Sarah M. — Classic Facial (60 min)                 |
|  10:30 Jennifer L. — Chemical Peel (45 min)               |
|  12:00 [LUNCH]                                            |
|  1:00  Ashley R. — Hydrafacial (75 min)                   |
|  3:00  Maria T. — Brow Lamination (45 min)                |
|  4:15  New Client — Consultation (30 min)                 |
+----------------------------------------------------------+
|  FOLLOW-UPS DUE TODAY                                     |
|  [Linked view -> Follow-Ups, filter: today + pending]     |
+----------------------------------------------------------+
|  CLIENTS NEEDING REBOOK                                   |
|  [Linked view -> Appointments, Not Rebooked view]         |
+----------------------------------------------------------+
|  THIS MONTH'S NUMBERS                                     |
|  Revenue: $4,280 / $6,000 goal (71%)                      |
|  Appointments: 42 completed                               |
|  New Clients: 7                                           |
|  No-Show Rate: 4%                                         |
+----------------------------------------------------------+
|  CLIENT BIRTHDAYS THIS WEEK                               |
|  [Linked view -> Clients, birthday filter]                |
+----------------------------------------------------------+
```

---

## FOLLOW-UP MESSAGE TEMPLATES

### Post-Appointment (Send within 24 hours)

**Standard:**
"Hey [Name]! It was so great seeing you today. Your [service] turned out amazing. Remember to [key aftercare tip]. If you have any questions, don't hesitate to reach out! See you in [frequency]."

**New Client:**
"Hi [Name]! Thank you so much for trusting me with your first [service]! I loved working with you. Here are your aftercare instructions: [tips]. I'd love to see you again in [timeframe] for your next appointment. Would you like me to get you on the books?"

**VIP Client:**
"[Name]!! Always love our appointments. You look incredible. I saved your [date + time] for next time like we discussed. See you then!"

### Rebooking Reminder (Send at recommended interval)

"Hey [Name]! It's been [weeks] since your last [service] and you're probably due for a refresh. I have a few openings next week — want me to save one for you? [Link]"

### Re-Engagement (60+ days, no appointment)

"Hi [Name]! I've missed seeing you. It's been a while since your last visit and I wanted to check in. If you'd like to get back on track with your [service], I'd love to get you scheduled. I have availability [days]. Let me know!"

### Birthday

"Happy Birthday [Name]!! Hope you have the most amazing day. As a little gift from me, enjoy [offer — $10 off, free add-on, etc.] on your next appointment. Valid this month. Cheers to you!"

### Review Request (Send 2-3 days post-appointment)

"Hey [Name]! So glad you loved your [service]! If you have 30 seconds, it would mean the world if you left a quick Google review. It helps other people find me and I really appreciate it. Here's the link: [link]. Thank you!!"

---

## QUICK-START GUIDE

### Step 1: Set Up Services
- Open the **Services** database
- Add every service you currently offer with accurate pricing and duration
- Include buffer time (cleanup, prep between clients)
- Fill in product cost per service to see your true margins
- Mark Add-Ons and Packages separately

### Step 2: Import Existing Clients
- Open the **Clients** database
- Add your current client list (start with your most active 20-30 clients)
- Fill in contact info, skin type, preferences, and any allergies
- Set the "Client Since" date as accurately as possible
- Note their preferred services and any personal details you remember

### Step 3: Start Logging Appointments
- Going forward, create an entry for every appointment (booked, completed, or no-show)
- Link to the correct Client and Service
- After each appointment: update status, add notes, upload before/after photos
- Check the "Rebooked" box if they scheduled their next visit

### Step 4: Set Up Follow-Up Workflows
- After each completed appointment, create a Follow-Up entry for 24 hours later (thank you + aftercare)
- Create rebooking reminders based on service frequency (e.g., 5 weeks after a 6-week service)
- Add birthday follow-ups for the beginning of each client's birthday month
- Check Follow-Ups daily and mark as Sent when completed

### Step 5: Track Revenue Monthly
- At the end of each month, create a new Revenue Tracker entry
- Pull totals from your Appointments database (filter by month + completed)
- Set goals and track your progress month over month
- Review no-show rate and rebook rate to identify areas for improvement

### Step 6: Use the Dashboard Daily
- Check Today's Schedule each morning
- Process Follow-Ups during downtime between clients
- Review "Needs Rebook" and "At-Risk" clients weekly
- Send birthday messages at the start of each week
