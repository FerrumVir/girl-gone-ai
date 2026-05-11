# Therapist Practice Manager — Digital Planner

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before entering real client data.
>
> **HIPAA Note:** This planner is a practice management organizer for administrative and scheduling information only. Do not store clinical notes, diagnoses, session content, or any protected health information (PHI) here. All clinical documentation belongs in your HIPAA-compliant EHR.

---

## DATABASES

---

### 1. Client Roster

**Purpose:** Master record for every current and former client — contact details, insurance information, billing rates, and session preferences. The source of truth for your entire caseload.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Client ID | Title | Format: CLT-001 (increment per client) |
| Preferred Name | Text | Name client uses in session |
| Last Name | Text | For sorting and formal reference |
| Phone | Phone | Primary contact number |
| Email | Email | Contact email (administrative use only) |
| Emergency Contact | Text | Name and phone number |
| Status | Select | Active / Inactive / Waitlist / Discharged / On Hold |
| Client Type | Select | Individual / Couples / Family / Adolescent / Child |
| Referral Source | Select | Self-referral / Physician / Insurance Panel / EAP / Former Client / Website / Psychology Today / Other |
| Start Date | Date | Date of first session |
| Discharge Date | Date | Date of last session (if discharged) |
| Sessions in Treatment | Rollup | Count of Session Log entries linked to this client |
| Sessions Attended | Rollup | Count of Session Log entries where Attendance = Attended |
| Sessions Cancelled | Rollup | Count of Session Log entries where Attendance = Cancelled or No-Show |
| Total Billed | Rollup | Sum of Fee Charged from linked Session Log entries |
| Total Collected | Rollup | Sum of Amount Paid from linked Billing records |
| Outstanding Balance | Formula | `prop("Total Billed") - prop("Total Collected")` |
| Session Fee | Number (USD) | Full fee per session |
| Sliding Scale Fee | Number (USD) | Adjusted fee if applicable (leave blank if full fee) |
| Effective Fee | Formula | `if(prop("Sliding Scale Fee") > 0, prop("Sliding Scale Fee"), prop("Session Fee"))` |
| Session Length | Select | 45 min / 50 min / 60 min / 75 min / 90 min |
| Frequency | Select | Weekly / Biweekly / Monthly / As Needed / Intensive |
| Day/Time Preference | Text | e.g., "Tuesdays 3–5pm" |
| Insurance | Checkbox | Does client use insurance? |
| Insurance Plan | Text | Plan name and payer |
| Insurance ID | Text | Member ID (administrative tracking only) |
| Group Number | Text | Group number |
| Copay / Coinsurance | Number (USD) | Client's portion per session |
| Deductible Met | Checkbox | Has annual deductible been met? |
| Authorization Number | Text | If prior auth required |
| Authorized Sessions | Number | Total sessions authorized |
| Sessions Used (Auth) | Rollup | Count of attended sessions since authorization start |
| Auth Expiration | Date | Date authorization expires |
| Superbill Required | Checkbox | Does client need superbill for out-of-network reimbursement? |
| Notes | Text | Administrative notes — scheduling preferences, billing quirks, etc. |
| Tags | Multi-select | Insurance / Sliding Scale / EAP / Telehealth / In-Person / Pro Bono |
| Linked Sessions | Relation | → Session Log database |
| Linked Billing | Relation | → Billing & Insurance Tracker database |
| Linked Treatment Plan | Relation | → Treatment Plans database |

**Views:**

- **Active Caseload** — Table, filter: Status = Active, sorted by Last Name
- **Full Client List** — Table, all clients, sorted by Start Date descending
- **Insurance Clients** — Filter: Insurance = true
- **Sliding Scale** — Filter: Sliding Scale Fee is not empty
- **Authorization Expiring** — Filter: Auth Expiration is within 30 days, sorted ascending
- **Outstanding Balances** — Table, filter: Outstanding Balance > 0, sorted descending
- **Waitlist** — Filter: Status = Waitlist
- **Discharged** — Filter: Status = Discharged

---

### 2. Session Log

**Purpose:** A chronological record of every scheduled appointment — date, type, attendance, duration, and fee. This is scheduling and attendance tracking, not clinical documentation.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session ID | Title | Format: SES-2024-0001 (year + sequence) |
| Client | Relation | → Client Roster database |
| Client Name | Rollup | Preferred Name from Client Roster |
| Session Date | Date | Date of appointment |
| Day of Week | Formula | `formatDate(prop("Session Date"), "dddd")` |
| Start Time | Text | e.g., "2:00 PM" |
| Session Type | Select | Individual / Couples / Family / Group / Consultation / Phone Check-in / Crisis |
| Modality | Select | In-Person / Telehealth / Hybrid |
| Duration | Select | 45 min / 50 min / 60 min / 75 min / 90 min |
| Attendance | Select | Attended / Cancelled — Client / Cancelled — Therapist / No-Show / Late Cancel / Rescheduled |
| Cancellation Reason | Text | Brief administrative note if applicable |
| Notice Given | Select | 24+ Hours / Less than 24 Hours / No Notice / N/A |
| Late Cancellation Fee | Checkbox | Was a late cancellation fee charged? |
| Fee Charged | Number (USD) | Amount billed for this session |
| Insurance Billing | Checkbox | Does this session go through insurance? |
| CPT Code | Text | Billing code (administrative reference only — e.g., 90837) |
| Claim Submitted | Checkbox | Has insurance claim been filed? |
| Session Number | Formula | Count of sessions for this client — see formula reference |
| Week | Formula | `formatDate(prop("Session Date"), "YYYY-[W]WW")` |
| Month | Formula | `formatDate(prop("Session Date"), "MMMM YYYY")` |
| Notes | Text | Brief admin notes only — e.g., "Rescheduled from 10/3", "Collected copay" |
| Linked Billing | Relation | → Billing & Insurance Tracker database |

**Views:**

- **This Week** — Filter: Session Date is this week, sorted by Session Date then Start Time
- **Today** — Filter: Session Date is today
- **All Sessions** — Table, sorted by Session Date descending
- **By Client** — Table, grouped by Client Name, sorted by Session Date descending
- **Attended Sessions** — Filter: Attendance = Attended
- **No-Shows & Late Cancels** — Filter: Attendance = No-Show OR Late Cancel
- **Unbilled Sessions** — Filter: Attendance = Attended AND Claim Submitted = false AND Insurance Billing = true
- **Telehealth Sessions** — Filter: Modality = Telehealth
- **Weekly Schedule** — Calendar view, Session Date, show Client Name and Start Time

---

### 3. Treatment Plans

**Purpose:** Administrative treatment plan tracking — goals, target session count, review schedules, and progress status. This is not a clinical document and does not contain session content, clinical formulations, or diagnostic information.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Plan ID | Title | Format: TP-CLT001-01 (client ID + version number) |
| Client | Relation | → Client Roster database |
| Client Name | Rollup | From Client Roster |
| Plan Version | Number | 1 for initial plan, increment for updates |
| Plan Start Date | Date | Date this treatment plan was initiated |
| Target Review Date | Date | Next scheduled treatment plan review |
| Plan End Date | Date | Anticipated discharge or plan end date |
| Days Until Review | Formula | `dateBetween(prop("Target Review Date"), now(), "days")` |
| Review Overdue | Formula | `if(prop("Days Until Review") < 0, "OVERDUE", if(prop("Days Until Review") <= 14, "DUE SOON", "On Track"))` |
| Presenting Focus | Text | General area of focus (non-clinical — e.g., "Work-related stress", "Relationship communication", "Anxiety management") |
| Goal 1 | Text | Stated treatment goal — administrative description |
| Goal 1 Status | Select | Not Started / In Progress / Achieved / Modified / Discontinued |
| Goal 2 | Text | |
| Goal 2 Status | Select | Not Started / In Progress / Achieved / Modified / Discontinued |
| Goal 3 | Text | |
| Goal 3 Status | Select | Not Started / In Progress / Achieved / Modified / Discontinued |
| Goal 4 | Text | |
| Goal 4 Status | Select | Not Started / In Progress / Achieved / Modified / Discontinued |
| Target Session Count | Number | Estimated total sessions for this treatment episode |
| Sessions Completed | Rollup | Count of attended sessions since Plan Start Date |
| Sessions Remaining | Formula | `prop("Target Session Count") - prop("Sessions Completed")` |
| Progress | Select | On Track / Progressing Slowly / Significant Progress / Goal Achieved / Stalled / Discharge Planning |
| Discharge Criteria | Text | What needs to be true for this client to complete treatment |
| Outcome at Discharge | Select | Goals Met / Partially Met / Not Met / Client Initiated / Transfer / N/A |
| Plan Status | Select | Active / Under Review / Completed / Archived |
| Notes | Text | Administrative notes on plan history, revisions, etc. |

**Views:**

- **Active Plans** — Filter: Plan Status = Active, sorted by Target Review Date ascending
- **Review Due** — Filter: Review Overdue = "OVERDUE" OR "DUE SOON", sorted ascending
- **All Plans** — Table, sorted by Plan Start Date descending
- **By Progress Status** — Table, grouped by Progress
- **Discharge Planning** — Filter: Progress = Discharge Planning

---

### 4. Billing & Insurance Tracker

**Purpose:** Track every billing transaction — client payments, insurance claims, and outstanding balances. This is administrative billing recordkeeping, not a formal accounting or claims submission system.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Transaction ID | Title | Format: BIL-2024-0001 |
| Client | Relation | → Client Roster database |
| Client Name | Rollup | From Client Roster |
| Linked Session | Relation | → Session Log database |
| Session Date | Rollup | Session Date from linked Session Log |
| Transaction Date | Date | Date payment was received or claim was submitted |
| Transaction Type | Select | Client Payment / Insurance Claim / Insurance Payment / Superbill Issued / Refund / Write-Off / Late Cancel Fee |
| CPT Code | Text | Billing code for this transaction (e.g., 90837, 90834) |
| Fee Charged | Number (USD) | Full fee for the session |
| Client Portion | Number (USD) | Copay, coinsurance, or full fee if self-pay |
| Insurance Portion | Number (USD) | Expected or received insurance payment |
| Amount Received | Number (USD) | Actual cash received for this transaction |
| Balance Remaining | Formula | `prop("Fee Charged") - prop("Amount Received")` |
| Payment Method | Select | Cash / Check / Credit Card / Venmo / Zelle / HSA / Insurance EFT / Other |
| Claim Status | Select | Not Submitted / Submitted / Under Review / Additional Info Requested / Approved / Partially Approved / Denied / Paid / Appealing |
| Claim Submitted Date | Date | |
| Claim Number | Text | Insurer's claim reference number |
| Expected Payment Date | Date | Estimated reimbursement date |
| Days Since Submission | Formula | `if(prop("Claim Submitted Date") != empty, dateBetween(now(), prop("Claim Submitted Date"), "days"), 0)` |
| Aging Alert | Formula | `if(and(prop("Claim Status") != "Paid", prop("Claim Status") != "Not Submitted", prop("Days Since Submission") > 45), "AGING CLAIM", if(prop("Days Since Submission") > 30, "FOLLOW UP", ""))` |
| Denial Reason | Text | If claim was denied — administrative note |
| Appeal Filed | Checkbox | |
| Appeal Date | Date | |
| Write-Off | Number (USD) | Amount written off (sliding scale discount, adjustment, etc.) |
| Notes | Text | Administrative notes on payment history or claim follow-up |

**Views:**

- **All Transactions** — Table, sorted by Transaction Date descending
- **Outstanding Balances** — Filter: Balance Remaining > 0, sorted by Transaction Date ascending
- **Insurance Claims — Open** — Filter: Transaction Type = Insurance Claim AND Claim Status is not Paid, sorted by Claim Submitted Date ascending
- **Aging Claims** — Filter: Aging Alert = "AGING CLAIM" OR "FOLLOW UP", sorted by Days Since Submission descending
- **Denied Claims** — Filter: Claim Status = Denied
- **Payments This Month** — Filter: Transaction Date is this month AND Transaction Type = Client Payment OR Insurance Payment
- **By Client** — Table, grouped by Client Name
- **Billing Pipeline** — Board view, grouped by Claim Status

---

### 5. Caseload Dashboard

**Purpose:** A live overview of your practice — active clients, session volume, revenue, and capacity. Reference this at the start of each week and at month-end.

> Build this as a Notion page that pulls linked views from all four databases, assembled into the layout below.

---

## DASHBOARD

### Dashboard Layout

```
┌──────────────────────────────────────────────────────────────┐
│  THERAPIST PRACTICE MANAGER          [Your Name]             │
│  Week of: ___________                [Current Month/Year]    │
├──────────────┬──────────────┬──────────────┬─────────────────┤
│ Active       │ Sessions     │ MTD Revenue  │ Outstanding     │
│ Clients      │ This Week    │              │ Balance         │
│    ___       │    ___       │   $______    │   $______       │
├──────────────┼──────────────┼──────────────┼─────────────────┤
│ Caseload     │ Cancellation │ Aging Claims │ Reviews Due     │
│ Capacity     │ Rate (90d)   │              │ (14 days)       │
│   ___%       │    ___%      │    ___       │    ___          │
├──────────────┴──────────────┴──────────────┴─────────────────┤
│  THIS WEEK'S SCHEDULE                                        │
│  [Linked view → Session Log, filter: This Week, calendar]    │
├──────────────────────────────────────────────────────────────┤
│  OUTSTANDING BALANCES                                        │
│  [Linked view → Billing Tracker, filter: Balance > 0]        │
├──────────────────────────────────────────────────────────────┤
│  AGING INSURANCE CLAIMS                                      │
│  [Linked view → Billing Tracker, filter: Aging Alert set]    │
├──────────────────────────────────────────────────────────────┤
│  TREATMENT PLAN REVIEWS DUE                                  │
│  [Linked view → Treatment Plans, filter: Review Due Soon]    │
├──────────────────────────────────────────────────────────────┤
│  ACTIVE CLIENT LIST                                          │
│  [Linked view → Client Roster, filter: Status = Active]      │
└──────────────────────────────────────────────────────────────┘
```

---

## KEY FORMULAS

### Session Utilization Rate

How many of your scheduled sessions actually resulted in attended appointments. Tracks the productive use of your calendar.

```
Session Utilization Rate =
  (Sessions Attended) / (Sessions Scheduled — Therapist Cancellations)
  × 100

Target: 80–90% or higher for a stable caseload
```

In your Session Log, create a filtered view for the trailing 90 days:
- **Attended sessions:** Filter Attendance = Attended, count rows
- **Scheduled sessions:** All rows in same period, exclude Attendance = Cancelled — Therapist

**Formula (Session Log rollup on Client Roster):**
```
if(
  prop("Sessions in Treatment") > 0,
  round((prop("Sessions Attended") / prop("Sessions in Treatment")) * 100),
  0
)
```

---

### Revenue Per Session

Your effective rate accounting for no-shows, sliding scale adjustments, and write-offs.

```
Revenue Per Session =
  Total Collected (period) / Sessions Attended (same period)
```

To calculate for a given month:
- Filter Billing Tracker: Transaction Date = this month, Transaction Type = Client Payment or Insurance Payment — sum Amount Received
- Filter Session Log: Session Date = this month, Attendance = Attended — count rows
- Divide

**Benchmark:** Compare this number to your stated session fee to understand the true impact of your no-show policy, sliding scale caseload, and insurance adjustments.

---

### Cancellation Rate

The percentage of scheduled appointments that were cancelled or no-showed within any given period.

```
Cancellation Rate =
  (Cancelled + No-Show sessions) / (All scheduled sessions)
  × 100

Target: below 15% for a stable practice
```

**Formula (add to Client Roster for per-client rate):**
```
if(
  prop("Sessions in Treatment") > 0,
  round(
    (prop("Sessions Cancelled") / prop("Sessions in Treatment")) * 100
  ),
  0
)
```

Use the **No-Shows & Late Cancels** view in Session Log to review patterns. High cancellation rates for specific clients may warrant a clinical conversation or policy discussion.

---

### Caseload Capacity

How full your practice is relative to your target weekly session count.

```
Caseload Capacity % =
  (Active Weekly Sessions) / (Target Weekly Sessions)
  × 100

- Under 75%: Room to take new referrals
- 75–90%: Healthy full practice
- Over 90%: At or near capacity — consider waitlist
- Over 100%: Overloaded — review scheduling
```

**To calculate Active Weekly Sessions:**
Filter Session Log to the current week. Count rows where Attendance = Attended or session is upcoming (today or future, this week).

**To set Target Weekly Sessions:**
Enter your target in a Practice Settings page (e.g., a single-row database or a Notion callout block): "Target: 25 sessions/week"

---

### Insurance Reimbursement Lag

The average number of days between claim submission and payment receipt.

```
Average Reimbursement Lag =
  Sum of (Payment Date — Claim Submitted Date) for all Paid claims
  / Count of Paid claims
```

Track this in the Billing Tracker. Create a filtered view: Transaction Type = Insurance Claim, Claim Status = Paid. The Days Since Submission property at time of payment gives you the lag per claim.

**Benchmark:** 14–30 days is typical for in-network claims. Consistently over 45 days warrants a call to the payer.

---

### Net Collection Rate

The percentage of what you billed that you actually collected — the gold standard for billing health.

```
Net Collection Rate =
  (Amount Received) / (Fee Charged — Contractual Write-Offs)
  × 100

Target: 95% or higher
```

In the Billing Tracker: sum Amount Received for a period, sum Fee Charged for the same period, subtract Write-Off amounts. Divide.

A net collection rate below 90% signals a billing process problem — either claims are going unpaid, client balances are not being collected, or write-offs are too high.

---

## QUICK-START GUIDE

### Step 1 — Configure Your Practice Settings

Before entering any client data, set up your baseline:

- Determine your full fee per session type (individual 50-min, couples 60-min, etc.)
- Note which insurance panels you are in-network with
- Set your target weekly session count (used for capacity calculations)
- Decide on your late cancellation policy (24-hour vs. 48-hour window)

Add these as a reference callout block at the top of your dashboard page.

### Step 2 — Add Your Existing Clients to the Client Roster

- Click "+ New" in the Client Roster database for each active client
- Assign a Client ID (CLT-001, CLT-002, etc.)
- Fill in their contact information, session fee, frequency, and insurance details
- Set Status to "Active"
- Tag appropriately (Insurance, Sliding Scale, Telehealth, etc.)
- Do not enter any clinical information — this is administrative only

For inactive or discharged clients you want to preserve for records, add them with Status = Inactive or Discharged.

### Step 3 — Log Your Past Sessions (Optional Backfill)

If you want historical data, backfill the last 30–90 days of sessions from your calendar:

- Open Session Log and click "+ New" for each past appointment
- Link to the correct Client, enter Session Date, Type, Duration, and Attendance
- Enter the Fee Charged for each attended session
- Check "Claim Submitted" for any sessions already billed to insurance

Going forward, log each session the same day or within 24 hours.

### Step 4 — Create Treatment Plan Records

For each active client:

- Open Treatment Plans and click "+ New"
- Assign a Plan ID (TP-CLT001-01)
- Link to the correct Client
- Enter the Plan Start Date and Target Review Date
- Add 2–4 administrative goal descriptions (non-clinical language)
- Set Target Session Count (your best estimate for this treatment episode)
- Set Plan Status to "Active"

Review and update these whenever you conduct a formal treatment plan review.

### Step 5 — Set Up Billing Records

For each session you log, create a corresponding Billing record:

- Open Billing & Insurance Tracker and click "+ New"
- Assign a Transaction ID (BIL-2024-0001)
- Link to the Client and the specific Session Log entry
- Set Transaction Type (Client Payment for self-pay; Insurance Claim for billed sessions)
- Enter Fee Charged, Client Portion, and Insurance Portion
- For insurance claims: enter Claim Submitted Date and set Claim Status to Submitted

When payment arrives:
- Update Amount Received
- Update Claim Status to Paid
- Enter Transaction Date for the payment

### Step 6 — Use the Dashboard Weekly

Pin the Caseload Dashboard to your Notion sidebar. Review it every Monday morning:

1. **This Week's Schedule** — Confirm appointments, note any open slots
2. **Outstanding Balances** — Identify clients with unpaid balances; send statements as needed
3. **Aging Claims** — Flag any insurance claims over 30 days for follow-up calls
4. **Treatment Plan Reviews Due** — Note which clients need a formal review this week or next
5. **Capacity** — Compare your active sessions to your target; decide whether to contact the waitlist

### Step 7 — Month-End Routine

At the end of each month, spend 20–30 minutes on practice administration:

- Review all Billing records for the month: are all attended sessions billed?
- Check for any submitted claims with no payment after 30+ days — call the payer
- Review your Cancellation Rate for the month: any clients with a concerning pattern?
- Update any Treatment Plans that have hit their target review date
- Note your MTD Revenue and compare to prior months
- Archive any clients who have been discharged this month (change Status to Discharged, add Discharge Date)

### Pro Tips

- Use the **Session ID format SES-YYYY-0001** so sessions sort chronologically across years
- For couples or family clients, create a single Client Roster entry for the case (e.g., "Smith Family") rather than separate entries — this keeps billing and session tracking unified
- The **Cancellation Rate formula per client** surfaces attendance patterns early — if a client is cancelling more than 25% of sessions, that's worth addressing proactively
- Use the **Tags property** on clients to quickly filter your caseload by characteristics: telehealth-only clients, EAP clients (who have limited sessions), or pro bono cases
- For EAP clients, use the **Authorized Sessions** and **Sessions Used (Auth)** properties to track when you're approaching the approved session limit — this gives you time to plan for the client's transition before the authorization runs out
- Set a recurring calendar reminder on the 1st of each month to run your month-end billing review
- If a client needs a superbill for out-of-network reimbursement, the **Superbill Required** checkbox in the Client Roster flags who needs one after each session — run that filter before closing out each week
