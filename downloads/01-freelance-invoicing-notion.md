# Freelance Invoicing & Client Tracker
### A Notion Template for Freelancers Who Want to Get Paid

---

> **QUICK START -- Read This First (Takes 3 Minutes)**
>
> 1. Duplicate this template to your Notion workspace using the link provided
> 2. Open the **Clients Database** and add your first client
> 3. Create your first invoice in the **Invoices Database** -- link it to the client
> 4. Fill in the line items, rate, and hours
> 5. Set the status to "Sent" and note the due date
>
> That's it for day one. The rest of the system builds on these basics.

---

## Template Overview

This Notion workspace gives you a complete freelance business backend: client management, project tracking, time logging, and invoicing -- all connected through Notion's relational databases so data flows automatically between them.

No spreadsheets. No hunting through email. No guessing which invoices are outstanding.

---

## What's Included

### 1. Clients Database

Your single source of truth for every client relationship.

**Properties:**
- Client Name, Company, Contact Email, Phone
- Billing Rate (hourly or project-based)
- Payment Terms (Net 15, Net 30, Net 60)
- Currency
- Status (Active, Paused, Completed, Prospect)
- Total Billed (rollup from Invoices)
- Total Paid (rollup from Invoices)
- Outstanding Balance (formula)
- Notes

**Views:**
- All Clients (table)
- Active Clients Only
- By Outstanding Balance (sorted highest first)
- Client Lifetime Value (sorted by total paid)

### 2. Invoices Database

Create, track, and manage every invoice from draft to paid.

**Properties:**
- Invoice Number (auto-generated format: INV-001)
- Client (relation to Clients Database)
- Project (relation to Projects Database)
- Issue Date, Due Date
- Line Items (text block for itemized billing)
- Subtotal, Discount %, Tax Rate, Total
- Amount Paid, Balance Due (formula)
- Status (Draft, Sent, Viewed, Paid, Overdue, Disputed)
- Payment Method, Payment Date
- Overdue Alert (formula -- flags anything past due date with unpaid balance)

**Views:**
- All Invoices
- Outstanding (unpaid, sorted by due date)
- Overdue Only
- Paid This Month
- By Client

### 3. Projects Database

Track scope, timeline, budget, and hours for every engagement.

**Properties:**
- Project Name, Client (relation), Description
- Start Date, End Date, Deadline
- Budget (fixed or hourly cap)
- Hours Logged (rollup from Time Tracking)
- Budget Utilization % (formula)
- Effective Hourly Rate (formula: total billed / hours logged)
- Status (Scoping, Active, On Hold, Complete, Cancelled)

### 4. Time Tracking Log

Log billable hours daily and never leave money on the table.

**Properties:**
- Date, Client (relation), Project (relation)
- Task Description
- Hours Worked, Billable (checkbox)
- Invoiced (checkbox)
- Rate (pulled from client)

**Key View: Uninvoiced Billable** -- Filters to show only billable hours that haven't been invoiced yet. This is where your lost revenue hides.

---

## Dashboard

Your main dashboard shows at a glance:
- Month-to-date revenue
- Outstanding invoices (count and total)
- Overdue invoices (flagged in red)
- Active projects with budget utilization
- Top clients by lifetime value
- Uninvoiced billable hours

---

## Email Templates Included

1. **Invoice Send Email** -- Professional, friendly, includes payment details
2. **Friendly Reminder** -- For invoices approaching or just past due date
3. **Overdue Follow-Up** -- Firmer tone for significantly overdue invoices

Copy, customize with your details, and send. No awkward wording required.

---

## Tips for Getting the Most Out of This Template

- **Log time daily.** Even 30 seconds at end of day. The Uninvoiced Billable view only works if your hours are logged.
- **Invoice promptly.** The moment a project milestone is done or the month ends, create the invoice. Delayed invoicing = delayed payment.
- **Review the dashboard weekly.** Sunday or Monday morning, 5 minutes. Know your numbers.
- **Use the Overdue Alert.** If something is flagged, follow up that day. The longer you wait, the harder it gets.
- **Customize your tax rate and payment terms.** The formulas are explained in plain English in the Formula Reference section of the template.

---

## Formula Reference

All formulas are documented inside the template with plain-English explanations. Key formulas:
- **Balance Due** = Total - Amount Paid
- **Overdue Alert** = If (Due Date < Today AND Balance Due > 0) then "OVERDUE"
- **Budget Utilization** = (Hours Logged * Rate) / Budget * 100
- **Effective Hourly Rate** = Total Billed / Hours Logged
- **Client Outstanding** = Sum of all unpaid invoice balances (rollup)

---

## Requirements

- Notion account (free plan works)
- Desktop or mobile -- template works on both
- No third-party integrations required

---

> Built by a freelancer, for freelancers. Stop losing money to lost invoices and unbilled hours.
