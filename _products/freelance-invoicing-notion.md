# Freelance Invoicing & Client Tracker — Notion Template

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Clients

**Purpose:** Master record for every client, past and present.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Client Name | Title | Full name or business name |
| Contact Name | Text | Primary point of contact (if company) |
| Email | Email | Primary billing email |
| Phone | Phone | Optional |
| Company | Text | Company or organization name |
| Billing Rate | Number (USD) | Default hourly or project rate |
| Rate Type | Select | Hourly / Project / Retainer / Day Rate |
| Status | Select | Active / Inactive / Prospect / Paused |
| Currency | Select | USD / EUR / GBP / CAD / AUD |
| Payment Terms | Select | Net 7 / Net 14 / Net 30 / Due on Receipt |
| Preferred Payment | Select | Bank Transfer / PayPal / Stripe / Check / Crypto |
| Notes | Text | Relationship notes, preferences, special terms |
| Tags | Multi-select | Long-term / Referral / Agency / Direct / High-value |
| Total Billed | Rollup | Sum of Amount from linked Invoices (Paid + Sent) |
| Total Paid | Rollup | Sum of Amount from linked Invoices where Status = Paid |
| Outstanding | Formula | `prop("Total Billed") - prop("Total Paid")` |
| Active Projects | Rollup | Count of linked Projects where Status = Active |
| First Project | Rollup | Min of Start Date from linked Projects |
| Client Since | Formula | Derived from First Project date |
| Linked Invoices | Relation | → Invoices database |
| Linked Projects | Relation | → Projects database |

**Views:**

- **All Clients** — Table, sorted by Status then Client Name
- **Active Clients** — Filter: Status = Active
- **High-Value Clients** — Filter: Total Billed > $5,000, sorted descending
- **Prospects** — Filter: Status = Prospect
- **Client Cards** — Gallery view, grouped by Status

---

### 2. Invoices

**Purpose:** Every invoice you issue, from draft through payment.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Invoice # | Title | Format: INV-2024-001 (year + sequence) |
| Client | Relation | → Clients database |
| Client Name | Rollup | Client Name from Client relation |
| Project | Relation | → Projects database |
| Issue Date | Date | When invoice was created/sent |
| Due Date | Date | Calculated or manual |
| Days Until Due | Formula | `dateBetween(prop("Due Date"), now(), "days")` |
| Line Item 1 Description | Text | e.g. "Web design — Homepage" |
| Line Item 1 Qty | Number | Hours or units |
| Line Item 1 Rate | Number | Rate for this item |
| Line Item 1 Amount | Formula | `prop("Line Item 1 Qty") * prop("Line Item 1 Rate")` |
| Line Item 2 Description | Text | |
| Line Item 2 Qty | Number | |
| Line Item 2 Rate | Number | |
| Line Item 2 Amount | Formula | `prop("Line Item 2 Qty") * prop("Line Item 2 Rate")` |
| Line Item 3 Description | Text | |
| Line Item 3 Qty | Number | |
| Line Item 3 Rate | Number | |
| Line Item 3 Amount | Formula | `prop("Line Item 3 Qty") * prop("Line Item 3 Rate")` |
| Subtotal | Formula | Sum of all Line Item Amounts |
| Discount % | Number | Optional percentage discount |
| Discount Amount | Formula | `prop("Subtotal") * (prop("Discount %") / 100)` |
| Tax Rate % | Number | Your applicable tax rate |
| Tax Amount | Formula | `(prop("Subtotal") - prop("Discount Amount")) * (prop("Tax Rate %") / 100)` |
| Total Amount | Formula | `prop("Subtotal") - prop("Discount Amount") + prop("Tax Amount")` |
| Amount Paid | Number | For partial payments |
| Balance Due | Formula | `prop("Total Amount") - prop("Amount Paid")` |
| Status | Select | Draft / Sent / Viewed / Partial / Paid / Overdue / Void / Disputed |
| Overdue Alert | Formula | `if(and(prop("Due Date") < now(), prop("Status") != "Paid", prop("Status") != "Void"), "OVERDUE", if(prop("Days Until Due") <= 3, "DUE SOON", ""))` |
| Payment Date | Date | When payment was received |
| Payment Method | Select | Bank Transfer / PayPal / Stripe / Check / Cash / Crypto |
| Invoice Notes | Text | Payment instructions, thank you message, etc. |
| Internal Notes | Text | Private notes, not shown to client |
| Send Reminder | Checkbox | Flag for follow-up needed |
| Reminder Sent | Date | Date of last reminder |

**Views:**

- **All Invoices** — Table, sorted by Issue Date descending
- **Outstanding** — Filter: Status = Sent OR Partial OR Overdue
- **Overdue** — Filter: Overdue Alert = "OVERDUE", highlight red
- **Paid This Month** — Filter: Status = Paid, Payment Date this month
- **Drafts** — Filter: Status = Draft
- **By Client** — Table, grouped by Client Name
- **Invoice Pipeline** — Board view, grouped by Status

---

### 3. Projects

**Purpose:** Track scope, timeline, budget, and hours for every engagement.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Project Name | Title | Clear, descriptive name |
| Client | Relation | → Clients database |
| Client Name | Rollup | From Client |
| Project Type | Select | Website / App / Branding / Writing / Consulting / Retainer / Other |
| Status | Select | Scoping / Active / On Hold / Waiting on Client / Complete / Cancelled |
| Start Date | Date | Kickoff date |
| End Date | Date | Deadline or delivery date |
| Days Remaining | Formula | `if(prop("Status") == "Active", dateBetween(prop("End Date"), now(), "days"), 0)` |
| Budget | Number | Total project budget (USD) |
| Budget Type | Select | Fixed / Hourly / Retainer |
| Hourly Rate | Number | If billing hourly |
| Hours Logged | Rollup | Sum of Hours from linked Time Log entries |
| Hours Budgeted | Number | Estimated hours for fixed-price work |
| Hours Remaining | Formula | `prop("Hours Budgeted") - prop("Hours Logged")` |
| Revenue Earned | Formula | `if(prop("Budget Type") == "Hourly", prop("Hours Logged") * prop("Hourly Rate"), prop("Budget"))` |
| Budget Used % | Formula | `if(prop("Budget") > 0, round((prop("Revenue Earned") / prop("Budget")) * 100), 0)` |
| Scope Notes | Text | What's included / excluded |
| Deliverables | Text | List of specific deliverables |
| Contract Signed | Checkbox | |
| Contract Date | Date | |
| Deposit Paid | Checkbox | |
| Deposit Amount | Number | |
| Linked Invoices | Relation | → Invoices database |
| Linked Time Logs | Relation | → Time Tracking Log database |
| Tags | Multi-select | Rush / Long-term / Recurring / Portfolio-worthy |

**Views:**

- **Active Projects** — Table, filter Status = Active, sorted by End Date
- **Project Timeline** — Timeline view, grouped by Client
- **Project Board** — Kanban, grouped by Status
- **Budget Health** — Table, sorted by Budget Used % descending
- **Completed Projects** — Filter: Status = Complete

---

### 4. Time Tracking Log

**Purpose:** Log every billable and non-billable hour against a project.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | Brief description of work done |
| Date | Date | Date work was performed |
| Project | Relation | → Projects database |
| Project Name | Rollup | From Project |
| Client | Rollup | Via Project → Client |
| Hours | Number | Time spent (use decimals: 1.5 = 1h 30m) |
| Billable | Checkbox | Is this time billable? |
| Hourly Rate | Rollup | From Project |
| Billable Amount | Formula | `if(prop("Billable"), prop("Hours") * prop("Hourly Rate"), 0)` |
| Description | Text | Detailed notes on work performed |
| Invoiced | Checkbox | Has this time been included on an invoice? |
| Week Number | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |

**Views:**

- **All Entries** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week
- **Uninvoiced Billable** — Filter: Billable = true AND Invoiced = false
- **By Project** — Table, grouped by Project Name
- **By Month** — Table, grouped by Month

---

## DASHBOARD

> Create this as a Notion page that pulls from all four databases using linked views and summary blocks.

### Dashboard Layout

```
┌─────────────────────────────────────────────────────────┐
│  FREELANCE HQ — [Your Name]              April 2024     │
├──────────────┬──────────────┬──────────────┬────────────┤
│  MTD Revenue │  Outstanding │ Active Proj. │ Overdue    │
│    $4,200    │   $1,800     │     3        │   1 ⚠️     │
├──────────────┴──────────────┴──────────────┴────────────┤
│  OUTSTANDING INVOICES                                    │
│  [Linked view → Invoices, filter: Status=Sent/Overdue]  │
├─────────────────────────────────────────────────────────┤
│  ACTIVE PROJECTS                                        │
│  [Linked view → Projects, filter: Status=Active]        │
├─────────────────────────────────────────────────────────┤
│  UNINVOICED TIME                                        │
│  [Linked view → Time Log, filter: Billable+Uninvoiced]  │
├─────────────────────────────────────────────────────────┤
│  REVENUE BY MONTH (Chart view — Invoices, group Month)  │
├─────────────────────────────────────────────────────────┤
│  CLIENT BREAKDOWN                                       │
│  [Linked view → Clients, sort: Total Billed desc]       │
└─────────────────────────────────────────────────────────┘
```

### Key Formula Reference

**Monthly Revenue (use in a Notion Chart or Gallery view):**
Create a filtered view of Invoices where Payment Date is current month and Status = Paid. Sum the Total Amount property.

**Overdue Detection:**
```
if(
  and(
    prop("Due Date") < now(),
    prop("Status") != "Paid",
    prop("Status") != "Void"
  ),
  "🔴 OVERDUE",
  if(
    dateBetween(prop("Due Date"), now(), "days") <= 3,
    "🟡 DUE SOON",
    "🟢 OK"
  )
)
```

**Effective Hourly Rate (per project):**
```
if(
  prop("Hours Logged") > 0,
  round(prop("Revenue Earned") / prop("Hours Logged")),
  0
)
```

**Year-to-Date Revenue:**
Create a linked Invoices view filtered to: Status = Paid, Payment Date is this year. Sum Total Amount.

---

## INVOICE TEMPLATE (Copy for each new invoice)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INVOICE

From:    [Your Name / Business Name]
         [Your Address]
         [Your Email] | [Your Phone]

To:      [Client Company]
         [Client Contact Name]
         [Client Email]

Invoice #:    INV-2024-___
Issue Date:   ____________
Due Date:     ____________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DESCRIPTION                        QTY    RATE    AMOUNT
─────────────────────────────────────────────────────────
[Service/Deliverable Description]  ___    $____   $______
[Service/Deliverable Description]  ___    $____   $______
[Service/Deliverable Description]  ___    $____   $______

                              Subtotal:   $______
                              Discount:   $______
                              Tax (__ %): $______
                         ─────────────────────────
                         TOTAL DUE:       $______

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Payment Instructions:
[Bank transfer details / PayPal email / Stripe link]

Late Payment: Invoices unpaid after [X] days are subject
to a [X]% monthly late fee.

Thank you for your business!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## EMAIL TEMPLATES

### Initial Invoice Send
> Subject: Invoice [INV-2024-XXX] — [Project Name] — Due [Date]

Hi [Client Name],

Please find attached Invoice [INV-2024-XXX] for [Project Name] in the amount of $[Amount], due [Date].

Payment can be made via [payment method]. Please reference invoice number [INV-2024-XXX] when sending payment.

Let me know if you have any questions or need anything adjusted.

Thanks,
[Your Name]

---

### Friendly Reminder (3 days before due)
> Subject: Friendly Reminder — Invoice [INV-2024-XXX] Due [Date]

Hi [Client Name],

Just a quick note that Invoice [INV-2024-XXX] for $[Amount] is due in [X] days on [Date].

[Payment link or instructions]

Thanks for your prompt attention!

[Your Name]

---

### Overdue Follow-Up
> Subject: Overdue Notice — Invoice [INV-2024-XXX] — [X] Days Past Due

Hi [Client Name],

I wanted to follow up on Invoice [INV-2024-XXX] for $[Amount], which was due on [Date] and is now [X] days past due.

Could you please let me know the status of this payment or if there's anything I can help clarify?

[Payment link or instructions]

Thanks,
[Your Name]

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Profile
- Open the **Clients** database and enter your first client
- Fill in rate, currency, payment terms, and preferred payment method
- Add any existing clients before creating invoices

### Step 2 — Create Your First Project
- Open **Projects** and click "+ New"
- Link it to the appropriate Client
- Set your budget type (Fixed or Hourly), enter the rate and budget
- Set start and end dates
- Mark "Contract Signed" once your agreement is in place

### Step 3 — Log Your Time
- Each day you work, add an entry to the **Time Tracking Log**
- Link it to the correct Project
- Check "Billable" for time you plan to invoice
- Use the "Uninvoiced Billable" view to see what's ready to bill

### Step 4 — Create an Invoice
- Open **Invoices** and click "+ New"
- Assign an invoice number (INV-YYYY-001, increment by 1 each time)
- Link to the Client and Project
- Fill in line items — descriptions, quantities, and rates
- Set Issue Date and Due Date
- Add your tax rate if applicable
- Set status to "Draft" while preparing, then "Sent" when delivered

### Step 5 — Use the Dashboard
- Pin the Dashboard page to your Notion sidebar
- Check it every Monday morning for your week's priorities
- Review "Outstanding" invoices and send reminders as needed
- Track "Uninvoiced Billable" time to ensure nothing slips through

### Step 6 — Mark Payments
- When a client pays, open the invoice and:
  - Change Status to "Paid"
  - Enter the Payment Date and Payment Method
  - Enter Amount Paid (if partial, use "Partial" status)

### Pro Tips
- Use the Invoice # format INV-YYYY-NNN so invoices sort chronologically
- Set up a recurring calendar reminder every 1st of the month to review outstanding invoices
- For retainer clients, duplicate last month's invoice and update the date and description
- Archive inactive clients by changing Status to "Inactive" — they won't clutter your active views
- Use the "Tags" property on clients to flag your best relationships for priority attention
- Export invoice pages to PDF using Notion's built-in export for sending to clients
