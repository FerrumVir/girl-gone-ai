# Digital Marketing Agency Client Tracker
### A Notion Template for Agency Operations

---

> **QUICK-START GUIDE — Get Running in One Day**
>
> 1. Duplicate this template to your Notion workspace
> 2. Open the **Clients Database** and add your current clients (start with your top 5)
> 3. For each client, fill in: contact info, retainer value, account manager, service tier
> 4. Open the **Deliverables Tracker** and add this week's pending deliverables
> 5. Open the **Campaigns Database** and add each client's active campaigns
> 6. Share the workspace with your team
> 7. Check the Dashboard every morning — it shows you what needs attention
>
> Don't try to backfill everything on Day 1. Start with what's active and build forward.

---

## How This System Works

Every database in this template is linked. When you create a deliverable, it connects to a client and a campaign. When you log meeting notes, they connect to a client. When you track retainer hours, they roll up to the client record. The result: open any client's page and see everything — campaigns, deliverables, meetings, retainer usage, SOWs — in one place.

**The five daily habits that make this system work:**
1. Check the Dashboard for overdue deliverables and upcoming deadlines
2. Update deliverable statuses as work progresses
3. Log meeting notes after every client call
4. Update retainer hours weekly (or after each work session)
5. Update campaign metrics weekly (or when reports are pulled)

---

---

# DATABASE 1: CLIENTS

> This is the hub. Every other database connects back here.

---

## Client Record Template

### Client Information

| Field | Value |
|-------|-------|
| **Client Name** | [Company Name] |
| **Primary Contact** | [Name] |
| **Email** | [email@company.com] |
| **Phone** | [Number] |
| **Website** | [URL] |
| **Industry** | [e.g., SaaS, E-commerce, Professional Services, Healthcare] |
| **Status** | [ ] Active [ ] Onboarding [ ] Paused [ ] Churned |
| **Account Manager** | [Team Member Name] |
| **Service Tier** | [ ] Starter [ ] Growth [ ] Premium [ ] Enterprise |

### Contract Details

| Field | Value |
|-------|-------|
| **Contract Start Date** | [Date] |
| **Contract End Date / Renewal Date** | [Date] |
| **Monthly Retainer Value** | $[Amount] |
| **Retainer Hours Included** | [X] hours/month |
| **Payment Terms** | [Net-15 / Net-30] |
| **Services Included** | [e.g., SEO, PPC, Social Media, Email, Content] |
| **SOW Reference** | [Link to SOW] |

### Quick View (Auto-populated from linked databases)

| Metric | Value |
|--------|-------|
| **Active Campaigns** | [Auto-count from Campaigns DB] |
| **Pending Deliverables** | [Auto-count from Deliverables DB] |
| **Overdue Deliverables** | [Auto-count, filtered by past due date] |
| **Hours Used This Month** | [Auto-sum from Retainer DB] |
| **Hours Remaining** | [Allocated minus Used] |
| **Last Meeting** | [Auto-populated from Meeting Notes DB] |
| **Client Health** | [ ] Green [ ] Yellow [ ] Red |

### Client Notes

[Open space for general notes, preferences, communication style, key stakeholders, internal context]

---

### Views to Build

1. **All Clients — Table View** (default: sorted by status, then name)
2. **Active Clients — Gallery View** (card shows: name, retainer value, account manager, health status)
3. **By Account Manager — Board View** (grouped by account manager)
4. **Renewals Coming Up — Table View** (filtered: renewal date within 60 days)
5. **Churned Clients — Table View** (filtered: status = churned, sorted by churn date)

---

---

# DATABASE 2: ONBOARDING PIPELINE

> Track every new client through a standardized onboarding process.

---

## Onboarding Pipeline — Kanban Stages

### Stage 1: Signed
**Checklist:**

- [ ] Contract signed and filed
- [ ] Invoice sent for first month / deposit
- [ ] Payment received
- [ ] Client added to Clients Database
- [ ] Internal kickoff scheduled with team

### Stage 2: Kickoff Scheduled
**Checklist:**

- [ ] Kickoff call scheduled with client
- [ ] Pre-kickoff questionnaire sent to client
- [ ] Internal brief prepared
- [ ] Team members assigned and notified

### Stage 3: Access Granted
**Checklist:**

- [ ] Google Analytics access received
- [ ] Google Ads access received (if applicable)
- [ ] Meta Business Manager access received (if applicable)
- [ ] Google Search Console access received (if applicable)
- [ ] Website CMS access received (if applicable)
- [ ] Brand assets received (logos, fonts, style guide)
- [ ] Social media account access received (if applicable)
- [ ] Email marketing platform access received (if applicable)
- [ ] All access credentials stored securely in [password manager]

### Stage 4: Strategy Call Complete
**Checklist:**

- [ ] Kickoff / strategy call completed
- [ ] Meeting notes documented
- [ ] Client goals and KPIs confirmed
- [ ] Target audience and personas reviewed
- [ ] Competitor landscape discussed
- [ ] Content calendar framework agreed upon
- [ ] Reporting cadence confirmed (weekly / bi-weekly / monthly)
- [ ] Communication preferences confirmed (email / Slack / calls)

### Stage 5: First Deliverable Sent
**Checklist:**

- [ ] Initial audit or assessment completed (if applicable)
- [ ] First month's strategy document delivered
- [ ] First deliverable sent (ad creative / content / campaign setup)
- [ ] Client feedback received on first deliverable

### Stage 6: Onboarding Complete
**Checklist:**

- [ ] All access confirmed working
- [ ] All campaigns live or scheduled
- [ ] Reporting template set up for this client
- [ ] Retainer tracking started
- [ ] Client moved to "Active" status in Clients Database
- [ ] 30-day check-in scheduled

---

## Onboarding Record Template

| Field | Value |
|-------|-------|
| **Client** | [Link to Clients DB] |
| **Onboarding Start Date** | [Date] |
| **Target Completion Date** | [Date — typically 14-30 days after signing] |
| **Current Stage** | [Stage 1-6] |
| **Account Manager** | [Name] |
| **Blockers** | [Any items waiting on the client or third party] |
| **Notes** | [Open field] |

---

---

# DATABASE 3: CAMPAIGNS

> Every campaign across every channel, linked to the client it serves.

---

## Campaign Record Template

### Campaign Details

| Field | Value |
|-------|-------|
| **Campaign Name** | [e.g., "Q2 Brand Awareness — Meta"] |
| **Client** | [Link to Clients DB] |
| **Platform** | [ ] Google Ads [ ] Meta (FB/IG) [ ] LinkedIn [ ] TikTok [ ] YouTube [ ] Email [ ] SEO [ ] Content [ ] Other: ___ |
| **Campaign Type** | [ ] Awareness [ ] Traffic [ ] Lead Gen [ ] Conversion [ ] Retargeting [ ] Branding [ ] Content [ ] Email Sequence |
| **Status** | [ ] Planning [ ] Setup [ ] Live [ ] Paused [ ] Completed [ ] Cancelled |
| **Start Date** | [Date] |
| **End Date** | [Date or Ongoing] |
| **Monthly Budget** | $[Amount] |
| **Total Budget** | $[Amount] |
| **Assigned To** | [Team Member(s)] |

### Performance Metrics (Update Weekly)

| Metric | Week 1 | Week 2 | Week 3 | Week 4 | Monthly Total |
|--------|--------|--------|--------|--------|---------------|
| **Spend** | $ | $ | $ | $ | $ |
| **Impressions** | | | | | |
| **Clicks** | | | | | |
| **CTR** | % | % | % | % | % |
| **Conversions** | | | | | |
| **CPA** | $ | $ | $ | $ | $ |
| **ROAS** | x | x | x | x | x |
| **Revenue** | $ | $ | $ | $ | $ |

### Campaign Notes

**Strategy:**
[What is this campaign trying to achieve? Target audience, messaging angle, creative approach]

**Key Learnings:**
[What's working? What's not? Optimizations made.]

**Action Items:**

- [ ] [Action item 1]
- [ ] [Action item 2]

---

### Views to Build

1. **All Campaigns — Table View** (grouped by client)
2. **Active Campaigns — Board View** (grouped by status)
3. **By Platform — Table View** (grouped by platform)
4. **By Team Member — Table View** (grouped by assigned to)
5. **Campaign Calendar — Calendar View** (by start date)

---

---

# DATABASE 4: DELIVERABLES TRACKER

> Every deliverable promised to every client. The accountability backbone of your agency.

---

## Deliverable Record Template

| Field | Value |
|-------|-------|
| **Deliverable Name** | [e.g., "April Blog Post — 10 SEO Tips"] |
| **Client** | [Link to Clients DB] |
| **Campaign** | [Link to Campaigns DB, if applicable] |
| **Type** | [ ] Blog Post [ ] Ad Creative [ ] Landing Page [ ] Email [ ] Social Post [ ] Report [ ] Audit [ ] Video [ ] Design Asset [ ] Strategy Doc [ ] Other: ___ |
| **Assigned To** | [Team Member] |
| **Due Date** | [Date] |
| **Status** | [ ] Not Started [ ] In Progress [ ] In Review [ ] Revision [ ] Approved [ ] Delivered |
| **Priority** | [ ] Low [ ] Medium [ ] High [ ] Urgent |
| **Notes** | [Brief description, specs, or client instructions] |
| **Link to Asset** | [Google Drive / Figma / Canva / etc.] |

---

### Views to Build

1. **All Deliverables — Table View** (sorted by due date)
2. **Overdue — Table View** (filtered: due date is before today AND status is not Delivered/Approved)
3. **By Client — Board View** (grouped by client)
4. **By Team Member — Table View** (grouped by assigned to)
5. **This Week — Table View** (filtered: due date is this week)
6. **Kanban — Board View** (grouped by status)

---

---

# DATABASE 5: RETAINER MANAGEMENT

> Track hours and budget allocation per client per month.

---

## Monthly Retainer Record Template

| Field | Value |
|-------|-------|
| **Client** | [Link to Clients DB] |
| **Month** | [e.g., April 2026] |
| **Hours Allocated** | [X] hours |
| **Hours Used** | [X] hours |
| **Hours Remaining** | [Allocated - Used] |
| **Utilization %** | [Used / Allocated * 100]% |
| **Budget Allocated** | $[Amount] |
| **Budget Spent** | $[Amount] |
| **Budget Remaining** | $[Allocated - Spent] |
| **Overage Hours** | [If Used > Allocated] |
| **Overage Billed** | $[Overage Hours * Overage Rate] |

### Time Log

| Date | Team Member | Task Description | Hours |
|------|-------------|-----------------|-------|
| [Date] | [Name] | [What was done] | [X.X] |
| [Date] | [Name] | [What was done] | [X.X] |
| [Date] | [Name] | [What was done] | [X.X] |
| [Date] | [Name] | [What was done] | [X.X] |
| [Date] | [Name] | [What was done] | [X.X] |
| | | **Total** | **[Sum]** |

### Notes

[Any context: scope discussions, overage conversations, efficiency observations]

---

### Views to Build

1. **Current Month — Table View** (filtered: month = current month, sorted by client)
2. **Over Budget — Table View** (filtered: utilization > 100%)
3. **By Client — Timeline View** (grouped by client, showing month-over-month)
4. **Historical — Table View** (all months, sorted by date descending)

---

---

# DATABASE 6: MEETING NOTES

> Document every client meeting in a searchable, linked archive.

---

## Meeting Notes Template

| Field | Value |
|-------|-------|
| **Meeting Title** | [e.g., "Acme Corp — Monthly Strategy Review"] |
| **Client** | [Link to Clients DB] |
| **Date** | [Date] |
| **Type** | [ ] Kickoff [ ] Weekly Check-in [ ] Monthly Review [ ] Strategy Session [ ] QBR [ ] Ad Hoc |
| **Attendees** | [Names — internal and client-side] |
| **Meeting Owner** | [Who ran the meeting] |

### Agenda

1. [Agenda item 1]
2. [Agenda item 2]
3. [Agenda item 3]

### Notes

[Meeting notes — key discussion points, client feedback, concerns raised, decisions made]

### Decisions

| Decision | Made By | Date |
|----------|---------|------|
| [Decision 1] | [Name] | [Date] |
| [Decision 2] | [Name] | [Date] |

### Action Items

| Action Item | Owner | Due Date | Status |
|-------------|-------|----------|--------|
| [Action 1] | [Name] | [Date] | [ ] Open [ ] Done |
| [Action 2] | [Name] | [Date] | [ ] Open [ ] Done |
| [Action 3] | [Name] | [Date] | [ ] Open [ ] Done |

---

---

# SOW TRACKER

> Keep tabs on every Statement of Work across your client base.

---

| Client | SOW Title | Value | Start Date | End Date | Status | Renewal Date |
|--------|-----------|-------|------------|----------|--------|--------------|
| [Client] | [SOW Title] | $[Amount] | [Date] | [Date] | [ ] Active [ ] Expired [ ] Renewed | [Date] |
| [Client] | [SOW Title] | $[Amount] | [Date] | [Date] | [ ] Active [ ] Expired [ ] Renewed | [Date] |

---

---

# TEAM ALLOCATION VIEW

> See who's working on what across all clients.

---

| Team Member | Client | Role | Hours/Week | Deliverables This Week |
|-------------|--------|------|------------|----------------------|
| [Name] | [Client 1] | [e.g., Account Manager] | [X] | [List] |
| [Name] | [Client 2] | [e.g., Designer] | [X] | [List] |
| [Name] | [Client 3] | [e.g., Media Buyer] | [X] | [List] |

**Total Capacity Check:**

| Team Member | Total Hours Assigned | Capacity (hrs/week) | Utilization |
|-------------|---------------------|---------------------|-------------|
| [Name] | [X] | [40] | [X]% |
| [Name] | [X] | [40] | [X]% |
| [Name] | [X] | [40] | [X]% |

---

---

# REPORTING TEMPLATES

---

## Monthly Client Report Template

### [CLIENT NAME] — Monthly Performance Report
**Reporting Period:** [Month Year]
**Prepared by:** [Your Agency Name]
**Date:** [Date]

---

**Executive Summary**
[2-3 sentence overview of the month: what was accomplished, key results, what's next]

---

**Campaign Performance**

| Campaign | Platform | Spend | Impressions | Clicks | CTR | Conversions | CPA | ROAS |
|----------|----------|-------|-------------|--------|-----|-------------|-----|------|
| [Campaign 1] | [Platform] | $X | X | X | X% | X | $X | Xx |
| [Campaign 2] | [Platform] | $X | X | X | X% | X | $X | Xx |
| **Totals** | | **$X** | **X** | **X** | **X%** | **X** | **$X** | **Xx** |

---

**Deliverables Completed**

| Deliverable | Status | Notes |
|-------------|--------|-------|
| [Deliverable 1] | Delivered | [Brief note] |
| [Deliverable 2] | Delivered | [Brief note] |
| [Deliverable 3] | In Progress | [Expected delivery date] |

---

**Key Wins**
1. [Win 1 — specific result with numbers]
2. [Win 2]
3. [Win 3]

**Challenges & Learnings**
1. [Challenge and how it was addressed]
2. [Learning that will inform future strategy]

**Next Month's Plan**
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

---

**Retainer Usage**

| Allocated | Used | Remaining | Utilization |
|-----------|------|-----------|-------------|
| [X] hrs | [X] hrs | [X] hrs | [X]% |

---

## Weekly Status Update Template

### [CLIENT NAME] — Weekly Update
**Week of:** [Date Range]
**Account Manager:** [Name]

**Completed This Week:**

- [Item 1]
- [Item 2]
- [Item 3]

**In Progress:**

- [Item 1 — expected completion: Date]
- [Item 2 — expected completion: Date]

**Blocked / Needs Client Input:**

- [Item — what's needed from the client]

**Key Metrics This Week:**
| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| [Metric 1] | [Value] | [Value] | [+/- %] |
| [Metric 2] | [Value] | [Value] | [+/- %] |

**Next Week's Focus:**

- [Priority 1]
- [Priority 2]

---

---

# AGENCY DASHBOARD

> Your daily command center. Build this as a Notion page with linked database views.

---

## Dashboard Layout

### Row 1: Key Numbers
| Active Clients | Monthly Retainer Revenue | Overdue Deliverables | Team Utilization |
|---------------|------------------------|---------------------|-----------------|
| [Auto-count] | $[Auto-sum] | [Auto-count, red if > 0] | [Average %] |

### Row 2: Urgent Attention
**Overdue Deliverables** (linked view from Deliverables DB, filtered: overdue, sorted by due date)

**Upcoming Deadlines — Next 7 Days** (linked view from Deliverables DB, filtered: due within 7 days)

### Row 3: Client Health
**Clients by Health Status** (linked view from Clients DB, board view grouped by health: Green / Yellow / Red)

### Row 4: Team Load
**Team Allocation This Week** (linked view from Team Allocation, sorted by utilization descending)

### Row 5: Recent Activity
**Recent Meeting Notes** (linked view from Meeting Notes DB, sorted by date, limit 10)

**Recent Deliverables Completed** (linked view from Deliverables DB, filtered: status = Delivered, sorted by date, limit 10)

---

---

# SETUP CHECKLIST

Use this to get the full system running:

- [ ] Duplicate template to your Notion workspace
- [ ] Add all current clients to the Clients Database
- [ ] Set up retainer records for the current month
- [ ] Add all active campaigns
- [ ] Add all pending deliverables for this week and next week
- [ ] Set up the onboarding pipeline for any clients currently onboarding
- [ ] Create the Dashboard page with linked database views
- [ ] Share the workspace with your team
- [ ] Walk the team through the daily workflow (5-minute explanation)
- [ ] Set a daily reminder to check the Dashboard
- [ ] Schedule a weekly 15-minute team sync to review overdue items and upcoming deadlines
- [ ] After 2 weeks: review and customize database properties, views, and templates to match your workflow
