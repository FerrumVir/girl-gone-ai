# Photography Client Management — Notion Template

> Duplicate this page into your Notion workspace to get started. All six databases are pre-linked with booking workflows, payment tracking, gallery delivery automation, and mood board systems already configured. Read the Quick-Start Guide at the bottom before onboarding your first client.

---

## DATABASES

---

### 1. Clients

**Purpose:** Master record for every client — past, present, and prospective. Stores contact info, session history, preferences, and lifetime value. This is your client relationship hub that ensures personalized service and repeat bookings.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Client Name | Title | Full name or couple/family name — e.g. "Sarah & Mike Johnson" |
| Email | Email | Primary contact email |
| Phone | Phone | Mobile number |
| Instagram | URL | Their Instagram handle (for tagging and social proof) |
| Address | Text | Mailing address (for prints, albums, thank-you cards) |
| City | Text | Location for travel planning |
| State | Text | |
| Client Type | Select | Individual / Couple / Family / Maternity / Newborn / Senior / Corporate / Brand / Wedding / Elopement |
| Source | Select | Referral / Instagram / Google / Wedding Wire / The Knot / Pinterest / Word of Mouth / Repeat Client / Vendor Referral / Mini Session / Other |
| Referred By | Relation | → Clients database (self-referential) |
| Status | Select | Inquiry / Booked / Active / Completed / Past Client / VIP / Do Not Rebook |
| Preferred Contact Method | Select | Email / Text / Phone / Instagram DM |
| Communication Style | Select | Very Responsive / Normal / Slow to Reply / Needs Follow-Up |
| First Session Date | Date | When they first booked |
| Total Sessions | Rollup | Count of linked Sessions |
| Total Revenue | Rollup | Sum of Total Paid from linked Sessions |
| Lifetime Value | Formula | `if(prop("Total Revenue") == 0, "$0", "$" + format(prop("Total Revenue")))` |
| Average Session Value | Formula | `if(prop("Total Sessions") == 0, "—", "$" + format(round(prop("Total Revenue") / prop("Total Sessions"))))` |
| Last Session Date | Rollup | Max of Session Date from linked Sessions |
| Days Since Last Session | Formula | `if(empty(prop("Last Session Date")), "No sessions", format(dateBetween(now(), prop("Last Session Date"), "days")) + " days")` |
| Preferences | Text | Lighting preferences, best angles, comfort level, styling notes |
| Allergies/Sensitivities | Text | Important for outdoor shoots — allergies, mobility concerns |
| Important Dates | Text | Anniversaries, birthdays, milestones (for rebooking prompts) |
| Kids/Pets Names | Text | Personal details for connection |
| Notes | Text | Relationship context, session history notes, communication preferences |
| Model Release Signed | Checkbox | Can you use their images in your portfolio/marketing? |
| VIP | Checkbox | High-value repeat client — priority treatment |
| Tags | Multi-select | Portfolio Worthy / Testimonial Given / Repeat / High Budget / Low Maintenance / High Maintenance / Flexible Schedule / Weekend Only |
| Linked Sessions | Relation | → Sessions/Bookings database |
| Linked Mood Boards | Relation | → Mood Boards database |
| Linked Contracts | Relation | → Contracts & Payments database |

**Views:**

- **All Clients** — Table, sorted by Client Name ascending
- **Active Clients** — Filter: Status = Booked or Active
- **Inquiries** — Filter: Status = Inquiry, sorted by creation date descending (respond quickly!)
- **Past Clients** — Filter: Status = Completed or Past Client (rebooking opportunities)
- **VIP Clients** — Filter: VIP = true
- **By Client Type** — Table, grouped by Client Type
- **By Source** — Table, grouped by Source (track where clients come from)
- **Revenue Ranked** — Table, sorted by Total Revenue descending
- **Needs Re-engagement** — Filter: Days Since Last Session > 180 AND Status != Do Not Rebook
- **Referral Network** — Filter: Referred By is not empty
- **Client Cards** — Gallery view with photo, name, client type, total revenue

---

### 2. Sessions / Bookings

**Purpose:** Every photo session from initial inquiry through final gallery delivery. Tracks the full lifecycle: scheduling, prep, shoot day, editing, delivery, and final payment. This is your operational engine.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Name | Title | Client name + type — e.g. "Johnson Family — Fall Minis" |
| Client | Relation | → Clients database |
| Client Name | Rollup | From Client relation |
| Session Type | Select | Portrait / Wedding / Elopement / Engagement / Maternity / Newborn / Family / Senior / Headshot / Brand/Commercial / Event / Boudoir / Mini Session / Second Shooter |
| Package | Select | Mini ($250) / Standard ($500) / Premium ($1000) / Luxury ($2000) / Wedding ($3500) / Custom |
| Session Date | Date | Shoot date and start time |
| End Time | Date | Expected end time |
| Duration (hrs) | Number | Session length in hours |
| Location | Text | Shoot location — address or venue name |
| Backup Location | Text | Indoor/alternative if weather is bad |
| Status | Select | Inquiry / Proposal Sent / Booked / Prep / Shoot Day / Editing / Gallery Sent / Completed / Cancelled / Rescheduled / No Show |
| Workflow Stage | Formula | Maps Status to a progress percentage for visual tracking |
| Session Fee | Number (USD) | Base session fee |
| Products/Prints | Number (USD) | Additional product sales |
| Travel Fee | Number (USD) | If applicable |
| Total Invoice | Formula | `prop("Session Fee") + prop("Products/Prints") + prop("Travel Fee")` |
| Retainer/Deposit | Number (USD) | Amount of deposit collected |
| Deposit Paid | Checkbox | Has the deposit been received? |
| Deposit Date | Date | When deposit was paid |
| Balance Due | Formula | `prop("Total Invoice") - prop("Retainer/Deposit")` |
| Balance Paid | Checkbox | Is the remaining balance paid? |
| Balance Date | Date | When balance was paid |
| Total Paid | Formula | `if(and(prop("Deposit Paid"), prop("Balance Paid")), prop("Total Invoice"), if(prop("Deposit Paid"), prop("Retainer/Deposit"), 0))` |
| Payment Method | Select | Venmo / PayPal / Zelle / Cash / Check / Credit Card / HoneyBook / Square |
| Contract Signed | Checkbox | Has the contract been signed? |
| Contract Sent Date | Date | When contract was sent |
| Questionnaire Sent | Checkbox | Has the pre-session questionnaire been sent? |
| Questionnaire Returned | Checkbox | Did they fill it out? |
| Shot List Created | Checkbox | Do you have a shot list ready? |
| Images Delivered | Number | Final number of edited images delivered |
| Gallery Platform | Select | Pixieset / ShootProof / Pic-Time / CloudSpot / Google Drive / Dropbox |
| Gallery Link | URL | Link to the client gallery |
| Gallery Delivered Date | Date | When gallery was sent |
| Gallery Expiration | Date | When gallery link expires |
| Download Deadline | Date | Deadline for client to download |
| Editing Hours | Number | Time spent in post-processing |
| Turnaround Promise | Text | Promised delivery timeline — e.g. "2–3 weeks" |
| Turnaround Actual | Formula | `if(or(empty(prop("Session Date")), empty(prop("Gallery Delivered Date"))), "—", format(dateBetween(prop("Gallery Delivered Date"), prop("Session Date"), "days")) + " days")` |
| Sneak Peek Sent | Checkbox | Did you send a preview within 48h? |
| Sneak Peek Date | Date | When sneak peek was sent |
| Blog Post Created | Checkbox | Did you blog this session? |
| Social Media Posted | Checkbox | Posted to your feed? |
| Testimonial Requested | Checkbox | Did you ask for a review? |
| Testimonial Received | Checkbox | Did they leave one? |
| Mood Board | Relation | → Mood Boards database |
| Weather Conditions | Text | Weather on shoot day (for learning what works) |
| Gear Used | Text | Camera body, lenses, lighting used |
| Lessons Learned | Text | What went well, what to improve |
| Favorite Image | Files & Media | Your personal favorite from this session |
| Rating (Personal) | Select | Portfolio Worthy / Good / Average / Below Average / Bad Day |
| Linked Contract | Relation | → Contracts & Payments database |
| Tags | Multi-select | Golden Hour / Studio / Outdoor / Indoor / Rain Plan Used / Second Shooter Needed / Rush Edit / Print Order |
| Notes | Text | Session-specific notes, client requests, wardrobe details |

**Views:**

- **All Sessions** — Table, sorted by Session Date descending
- **Pipeline Board** — Kanban grouped by Status (main working view)
- **Calendar** — Calendar view by Session Date
- **This Month** — Filter: Session Date is this month
- **Needs Action** — Filter: Status = Inquiry or Proposal Sent (respond within 24h!)
- **Currently Editing** — Filter: Status = Editing, sorted by Session Date ascending (oldest first = deliver first)
- **Awaiting Payment** — Filter: Balance Paid = false AND Status != Cancelled, sorted by Session Date
- **Unpaid Deposits** — Filter: Deposit Paid = false AND Status = Booked
- **Revenue This Month** — Filter: Session Date is this month, showing Total Invoice and Total Paid
- **Revenue This Year** — Filter: Session Date is this year, sorted by month
- **By Session Type** — Table, grouped by Session Type
- **Gallery Expiring** — Filter: Gallery Expiration is within 14 days (notify clients!)
- **Portfolio Shots** — Filter: Rating = Portfolio Worthy
- **Completed** — Filter: Status = Completed, sorted by Session Date descending

---

### 3. Contracts & Payments

**Purpose:** Centralized tracking of all legal documents and financial transactions. Every contract, invoice, payment, and receipt in one place. Ensures nothing falls through the cracks on the business side.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Document Name | Title | e.g. "Johnson Wedding Contract" or "Invoice #2024-047" |
| Client | Relation | → Clients database |
| Client Name | Rollup | From Client relation |
| Session | Relation | → Sessions database |
| Type | Select | Contract / Invoice / Receipt / Model Release / Print Release / Second Shooter Agreement / Vendor Agreement |
| Status | Select | Draft / Sent / Signed / Paid / Overdue / Cancelled / Expired |
| Date Sent | Date | When document was sent to client |
| Date Signed | Date | When contract was signed |
| Date Due | Date | Payment due date |
| Overdue | Formula | `if(and(prop("Type") == "Invoice", prop("Status") != "Paid", not(empty(prop("Date Due"))), prop("Date Due") < now()), true, false)` |
| Days Overdue | Formula | `if(prop("Overdue"), format(dateBetween(now(), prop("Date Due"), "days")) + " days", "—")` |
| Amount | Number (USD) | Dollar amount |
| Payment Received | Number (USD) | Amount actually received |
| Payment Method | Select | Venmo / PayPal / Zelle / Cash / Check / Credit Card / HoneyBook / Square |
| Payment Date | Date | When payment was received |
| Platform | Select | HoneyBook / Dubsado / HelloSign / DocuSign / Manual / PDF |
| Document Link | URL | Link to the document in your CRM/signing platform |
| File | Files & Media | Upload PDF copy |
| Cancellation Policy | Text | Terms for cancellation (reference from contract) |
| Refund Issued | Checkbox | Was a refund given? |
| Refund Amount | Number (USD) | If applicable |
| Notes | Text | Payment notes, special terms, negotiations |
| Tags | Multi-select | Rush / Payment Plan / Discounted / Full Price / Add-On / Referral Discount |

**Views:**

- **All Documents** — Table, sorted by Date Sent descending
- **Outstanding Invoices** — Filter: Type = Invoice AND Status != Paid, sorted by Date Due ascending
- **Overdue** — Filter: Overdue = true (chase these immediately!)
- **Contracts Awaiting Signature** — Filter: Type = Contract AND Status = Sent
- **Paid This Month** — Filter: Payment Date is this month
- **Revenue Tracker** — Table showing all paid invoices with Payment Date, Amount, Client Name
- **By Client** — Table, grouped by Client Name
- **Model Releases** — Filter: Type = Model Release (check before posting)
- **Payment Plans** — Filter: Tags contains Payment Plan

---

### 4. Mood Boards

**Purpose:** Visual inspiration and planning boards for each session. Collaborate with clients on style, location, wardrobe, poses, and aesthetic direction. Ensures everyone is aligned before shoot day and results match expectations.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Board Name | Title | e.g. "Johnson Engagement — Moody Forest Vibes" |
| Client | Relation | → Clients database |
| Client Name | Rollup | From Client relation |
| Session | Relation | → Sessions database |
| Style Direction | Select | Light & Airy / Dark & Moody / Film / Editorial / Documentary / Romantic / Bold & Colorful / Minimalist / Vintage / Classic / Bohemian |
| Color Palette | Text | Dominant colors — e.g. "Rust, sage, cream, gold" |
| Season/Time | Select | Spring / Summer / Fall / Winter / Golden Hour / Blue Hour / Midday / Overcast |
| Location Ideas | Text | Potential locations that match the vibe |
| Wardrobe Notes | Text | Clothing suggestions, what to avoid, coordination tips |
| Wardrobe Colors | Text | Specific color recommendations for outfits |
| Props | Text | Any props to bring or source |
| Pose Inspiration | Files & Media | Reference pose images |
| Lighting References | Files & Media | Lighting examples to recreate |
| Location Scouting Photos | Files & Media | Photos from location scouts |
| Pinterest Board | URL | Link to collaborative Pinterest board |
| Client Input | Text | What the client wants — their words, their vision |
| Photographer Notes | Text | Your creative direction and technical plan |
| Approved by Client | Checkbox | Has the client signed off on this direction? |
| Approval Date | Date | When client approved |
| Status | Select | In Progress / Shared with Client / Approved / Archived |
| Inspiration Images | Files & Media | Collected reference images |
| Tags | Multi-select | Outdoor / Studio / Urban / Nature / Beach / Desert / Mountains / City / Home / Intimate |
| Notes | Text | Additional creative direction notes |

**Views:**

- **All Mood Boards** — Table, sorted by creation date descending
- **Active** — Filter: Status = In Progress or Shared with Client
- **Awaiting Approval** — Filter: Status = Shared with Client AND Approved by Client = false
- **By Style** — Table, grouped by Style Direction
- **Gallery** — Gallery view showing Inspiration Images
- **By Client** — Table, grouped by Client Name
- **Approved** — Filter: Approved by Client = true

---

### 5. Vendor Network

**Purpose:** Track all vendors you work with — florists, venues, planners, makeup artists, DJs, and other creatives. Essential for wedding photography and collaborative shoots. Builds your referral network and ensures smooth event-day coordination.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Vendor Name | Title | Business or person name |
| Contact Person | Text | Primary contact at the business |
| Email | Email | Business email |
| Phone | Phone | Business phone |
| Instagram | URL | Their Instagram (for tagging) |
| Website | URL | Portfolio or business site |
| Category | Select | Venue / Florist / Planner / MUA (Makeup) / Hair Stylist / DJ / Caterer / Baker / Officiant / Videographer / Second Shooter / Stationer / Rentals / Dress Shop / Suit Shop / Photo Booth / Other |
| Location | Text | City/area they serve |
| Price Range | Select | Budget / Mid-Range / Premium / Luxury |
| Quality Rating | Select | Exceptional / Good / Average / Below Average / Do Not Recommend |
| Easy to Work With | Select | Dream Team / Easy / Fine / Difficult / Never Again |
| Times Worked Together | Number | How many events/shoots |
| Last Worked Together | Date | Most recent collaboration |
| Refers Clients to Me | Checkbox | Do they send you business? |
| I Refer Clients to Them | Checkbox | Do you recommend them? |
| Portfolio Link | URL | Their work samples |
| Preferred Vendors List | Checkbox | On your official preferred vendors list? |
| Notes | Text | Working style, communication preferences, scheduling notes |
| Tags | Multi-select | Reliable / Creative / Responsive / Budget-Friendly / Premium / Local / Travel / New |

**Views:**

- **All Vendors** — Table, sorted by Category then Vendor Name
- **By Category** — Table, grouped by Category
- **Preferred Vendors** — Filter: Preferred Vendors List = true
- **Referral Partners** — Filter: Refers Clients to Me = true
- **By Location** — Table, grouped by Location
- **Dream Team** — Filter: Quality Rating = Exceptional AND Easy to Work With = Dream Team
- **Avoid** — Filter: Quality Rating = Below Average or Easy to Work With = Never Again

---

### 6. Gear & Equipment

**Purpose:** Inventory of all photography equipment with maintenance tracking, insurance values, and rental history. Know what you have, what needs service, and what to bring to each shoot.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Item Name | Title | e.g. "Canon R5 Body #1" or "70-200mm f/2.8 RF" |
| Category | Select | Camera Body / Lens / Flash / Trigger / Tripod / Light Stand / Modifier / Backdrop / Memory Card / Battery / Bag / Computer / Calibration / Misc |
| Brand | Text | Manufacturer |
| Model | Text | Specific model number |
| Serial Number | Text | For insurance and warranty |
| Purchase Date | Date | When acquired |
| Purchase Price | Number (USD) | Original cost |
| Current Value | Number (USD) | Estimated replacement value |
| Condition | Select | New / Excellent / Good / Fair / Needs Service / Retired |
| Last Serviced | Date | Last maintenance or calibration |
| Service Due | Date | Next scheduled maintenance |
| Shutter Count | Number | For camera bodies |
| Insurance Covered | Checkbox | Is this item on your insurance policy? |
| Rental Available | Checkbox | Do you rent this out? |
| Rental Rate | Number (USD) | If applicable |
| Primary Use | Select | Every Shoot / Portraits / Weddings / Studio / Backup / Specialty |
| Location | Select | Studio / Home / Car Kit / Second Shooter / Being Serviced |
| Notes | Text | Performance notes, quirks, accessories included |
| Tags | Multi-select | Essential / Backup / Heavy / Travel-Friendly / Rented / Insured |

**Views:**

- **All Gear** — Table, sorted by Category then Item Name
- **By Category** — Table, grouped by Category
- **Needs Service** — Filter: Condition = Needs Service OR Service Due is past
- **Insurance Inventory** — Table showing Item Name, Serial Number, Purchase Price, Current Value
- **Shoot Kit** — Filter: Primary Use = Every Shoot (packing checklist)
- **Total Value** — Table with sum of Current Value (for insurance purposes)

---

## CLIENT WORKFLOW AUTOMATION

> This is the step-by-step workflow for every client from first inquiry to final delivery. Use it as a checklist system — each stage triggers specific actions.

### Workflow Stages & Actions

| Stage | Status | Actions to Complete |
|---|---|---|
| 1. Inquiry Received | Inquiry | Respond within 24h, send pricing guide, ask qualifying questions |
| 2. Proposal Sent | Proposal Sent | Send custom proposal with package options and availability |
| 3. Booked | Booked | Contract signed, deposit received, add to calendar, send welcome guide |
| 4. Pre-Session Prep | Prep | Send questionnaire, create mood board, scout location, create shot list |
| 5. Shoot Day | Shoot Day | Execute session, backup cards immediately, send same-day thank you text |
| 6. Editing | Editing | Cull images, edit selects, maintain turnaround promise |
| 7. Sneak Peek | Editing | Send 3–5 edited previews within 48 hours |
| 8. Gallery Delivery | Gallery Sent | Upload gallery, send delivery email with download instructions |
| 9. Follow-Up | Completed | Request testimonial, share blog post, send print/album options |
| 10. Nurture | Past Client | Add to holiday card list, send anniversary reminder, seasonal mini promos |

### Client Communication Timeline

| When | Action | Template |
|---|---|---|
| Inquiry Day | Respond to inquiry | Inquiry Response template |
| +1 day (if no response) | Follow up on inquiry | Gentle Follow-Up template |
| Booking confirmed | Send welcome guide | Welcome Email template |
| 2 weeks before session | Send prep guide + questionnaire | Pre-Session Prep template |
| 1 week before session | Confirm details | Confirmation Email template |
| 1 day before | Weather/logistics check | Day-Before Reminder template |
| Same day (evening) | Thank you message | Post-Session Thank You template |
| +2 days | Sneak peek delivery | Sneak Peek Email template |
| +14–21 days | Full gallery delivery | Gallery Delivery Email template |
| +3 days after gallery | Check if they received/downloaded | Gallery Follow-Up template |
| +1 week after gallery | Request testimonial | Testimonial Request template |
| +3 months | Check-in / rebooking | Re-engagement Email template |

---

## AUTOMATIONS / FORMULAS

### Total Invoice Calculation

Sums all fees for a session.

```
prop("Session Fee") + prop("Products/Prints") + prop("Travel Fee")
```

### Balance Due

What the client still owes.

```
prop("Total Invoice") - prop("Retainer/Deposit")
```

### Turnaround Actual

Days between shoot and gallery delivery.

```
if(
  or(empty(prop("Session Date")), empty(prop("Gallery Delivered Date"))),
  "—",
  format(dateBetween(prop("Gallery Delivered Date"), prop("Session Date"), "days")) + " days"
)
```

### Client Lifetime Value

Total revenue from a single client across all sessions.

```
if(prop("Total Revenue") == 0, "$0", "$" + format(prop("Total Revenue")))
```

### Days Since Last Session

Time elapsed since most recent session with a client.

```
if(
  empty(prop("Last Session Date")),
  "No sessions yet",
  format(dateBetween(now(), prop("Last Session Date"), "days")) + " days"
)
```

### Invoice Overdue Detection

Flags unpaid invoices past their due date.

```
if(
  and(
    prop("Type") == "Invoice",
    prop("Status") != "Paid",
    not(empty(prop("Date Due"))),
    prop("Date Due") < now()
  ),
  true,
  false
)
```

### Average Session Value

Revenue per session across client's history.

```
if(
  prop("Total Sessions") == 0,
  "—",
  "$" + format(round(prop("Total Revenue") / prop("Total Sessions")))
)
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Existing Clients

- Open the **Clients** database and add all clients from the past 12 months
- At minimum: Name, Email, Client Type, Source, and Status
- For past clients, set Status = Past Client and note their Total Revenue
- For anyone currently booked, set Status = Booked or Active

### Step 2 — Set Up Active Sessions

- Open **Sessions/Bookings** and create entries for all currently booked shoots
- Link each to the Client, set Session Date, Package, Location, and current Status
- Fill in financial fields: Session Fee, Deposit amount, Deposit Paid checkbox
- This gives you an immediate view of your pipeline and cash flow

### Step 3 — Configure Your Packages

- Customize the Package select options to match your actual pricing
- Update the default values in the notes or create a separate pricing reference page
- Standard packages make quoting faster and ensure consistent pricing

### Step 4 — Build Your Vendor Network

- Add all vendors you regularly work with to the **Vendor Network** database
- Mark your preferred vendors and note who refers clients to you
- This becomes your go-to resource when clients ask for recommendations

### Step 5 — Create Your First Mood Board

- For your next booked session, create a **Mood Board** entry
- Share your Pinterest board link, add wardrobe suggestions, and note the style direction
- Send to your client for approval before shoot day

### Step 6 — Establish Your Workflow

**When an inquiry comes in:**
1. Add them to Clients (Status = Inquiry)
2. Respond within 24 hours with pricing guide
3. Create a Session entry (Status = Inquiry)
4. Follow up in 48 hours if no response

**When a session is booked:**
1. Update Session Status to Booked
2. Create Contract entry, send for signature
3. Collect deposit, mark Deposit Paid
4. Send welcome guide and questionnaire
5. Create Mood Board 2 weeks before shoot

**After the shoot:**
1. Update Session Status to Editing
2. Send sneak peek within 48 hours
3. Edit full gallery within promised turnaround
4. Update to Gallery Sent, send delivery email
5. Follow up for testimonial 1 week after delivery

**Monthly business review (30 minutes):**
- Check revenue: how much earned this month vs. target?
- Review pipeline: how many sessions booked for next 2 months?
- Check outstanding invoices: chase any overdue payments
- Review client sources: where are new clients coming from?
- Nurture past clients: anyone approaching an anniversary or milestone?

### Pro Tips

- The inquiry response time is everything — respond within 2 hours if possible. Clients often book the first photographer who replies
- Always get the deposit before adding to your calendar. No deposit = no hold
- Send sneak peeks within 48 hours of every session — clients share these on social media while they're still excited
- Track your Source religiously — after 6 months you'll know exactly where to spend your marketing dollars
- Use the "Currently Editing" view sorted by Session Date to enforce FIFO (first in, first out) delivery
- Blog your portfolio-worthy sessions — it's the best SEO investment for a photographer
- The Vendor Network pays dividends — vendors who love working with you will refer their clients
- Request testimonials within 1 week of gallery delivery while emotions are high
- Track Editing Hours to understand your true hourly rate (Total Paid / (Session Hours + Editing Hours + Admin Hours))
- Seasonal mini sessions are the best re-engagement tool for past clients — reach out 6 weeks before the season
