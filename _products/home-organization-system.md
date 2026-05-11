# Home Organization System — Notion Template

> Duplicate this page into your Notion workspace to get started. All four databases are pre-linked with maintenance schedules, decluttering workflows, and seasonal checklists already configured. Read the Quick-Start Guide at the bottom before your first room audit.

---

## DATABASES

---

### 1. Rooms & Zones

**Purpose:** Master record for every room and zone in your home. Each room tracks its current organization status, storage solutions in use, and links to all decluttering sessions and maintenance tasks. Think of this as your home's "floor plan database."

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Room Name | Title | Specific name — e.g. "Primary Bedroom Closet" or "Kitchen Pantry" |
| Zone | Select | Kitchen / Living Room / Primary Bedroom / Bedroom 2 / Bedroom 3 / Bathroom (Primary) / Bathroom 2 / Home Office / Garage / Laundry Room / Entryway / Dining Room / Basement / Attic / Hallway / Outdoor / Storage Unit |
| Floor | Select | Main Floor / Upper Floor / Basement / Garage / Outdoor |
| Organization Status | Select | Pristine / Well-Organized / Needs Attention / Cluttered / Disaster Zone / Not Started |
| Last Organized | Date | When this room was last fully organized |
| Days Since Organized | Formula | `if(empty(prop("Last Organized")), "Never", format(dateBetween(now(), prop("Last Organized"), "days")) + " days")` |
| Maintenance Frequency | Select | Daily / Weekly / Bi-weekly / Monthly / Quarterly / Seasonally |
| Next Maintenance Due | Date | When this room needs its next maintenance pass |
| Maintenance Overdue | Formula | `if(and(not(empty(prop("Next Maintenance Due"))), prop("Next Maintenance Due") < now()), true, false)` |
| Square Footage | Number | Approximate room size (helpful for storage planning) |
| Storage Solutions | Multi-select | Shelving / Bins / Drawer Dividers / Labels / Hooks / Over-Door Organizers / Under-Bed Storage / Closet System / Pegboard / Cabinet Organizers / Lazy Susan / File System / Baskets / Vacuum Bags |
| Problem Areas | Text | What tends to get messy? What are the pain points? |
| Vision | Text | What does this room look like when perfectly organized? Your ideal state. |
| Before Photo | Files & Media | Photo before organizing (motivation and progress tracking) |
| After Photo | Files & Media | Photo after organizing |
| Current Photo | Files & Media | What it looks like right now |
| Priority | Select | High / Medium / Low |
| Estimated Time to Organize | Text | How long a full organization session would take |
| Budget Allocated | Number (USD) | Money available for storage solutions |
| Budget Spent | Rollup | Sum of Cost from linked Storage Purchases |
| Total Items Decluttered | Rollup | Sum of items removed from linked Declutter Sessions |
| Linked Declutter Sessions | Relation | → Declutter Sessions database |
| Linked Maintenance Tasks | Relation | → Maintenance Schedule database |
| Linked Storage Purchases | Relation | → Storage Solutions database |
| Notes | Text | General notes, layout ideas, measurements |

**Views:**

- **All Rooms** — Table, sorted by Zone then Room Name
- **Status Overview** — Table showing Room Name, Organization Status, Days Since Organized, Next Maintenance Due
- **Needs Attention** — Filter: Organization Status = Needs Attention or Cluttered or Disaster Zone, sorted by Priority
- **Maintenance Overdue** — Filter: Maintenance Overdue = true
- **By Zone** — Table, grouped by Zone
- **By Floor** — Table, grouped by Floor
- **Room Cards** — Gallery view with Before/After Photos, Organization Status
- **Priority Board** — Kanban grouped by Priority
- **Clean & Organized** — Filter: Organization Status = Pristine or Well-Organized (your wins!)

---

### 2. Declutter Sessions

**Purpose:** Track every decluttering session room by room. Records what was removed, where it went (trash, donate, sell, relocate), time spent, and progress made. Over time, this builds a powerful record of your decluttering journey and helps maintain momentum.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Name | Title | What you tackled — e.g. "Kitchen junk drawer purge" |
| Room | Relation | → Rooms & Zones database |
| Room Name | Rollup | From linked Room |
| Date | Date | When this session happened |
| Duration (mins) | Number | How long you spent |
| Category Tackled | Select | Clothing / Books / Papers / Kitchen / Electronics / Toys / Decor / Tools / Bathroom Products / Linens / Seasonal / Sentimental / Miscellaneous |
| Method Used | Select | KonMari / One-In-One-Out / 20-Minute Sweep / Box Method / Category Purge / Full Room Reset / Quick Tidy / Seasonal Rotation |
| Items Reviewed | Number | Total items you looked at/evaluated |
| Items Kept | Number | Items that stayed |
| Items Trashed | Number | Items thrown away |
| Items Donated | Number | Items going to donation |
| Items Sold | Number | Items listed for sale |
| Items Relocated | Number | Items moved to a better location |
| Items Removed Total | Formula | `prop("Items Trashed") + prop("Items Donated") + prop("Items Sold") + prop("Items Relocated")` |
| Declutter Rate % | Formula | `if(prop("Items Reviewed") == 0, "—", format(round(prop("Items Removed Total") / prop("Items Reviewed") * 100)) + "%")` |
| Donation Destination | Text | Where donated items are going — e.g. "Goodwill on Main St" |
| Donation Drop-Off | Checkbox | Have you actually dropped off the donation? |
| Sale Platform | Text | Where items are listed — eBay, Facebook Marketplace, Poshmark, etc. |
| Sale Revenue | Number (USD) | Money earned from sold items |
| Difficulty | Select | Easy / Moderate / Hard / Emotionally Difficult |
| Energy Before | Select | High / Medium / Low / Dreading It |
| Energy After | Select | Energized / Satisfied / Neutral / Drained / Overwhelmed |
| What Worked | Text | Techniques or approaches that made this session effective |
| What Was Hard | Text | Blockers, emotional attachments, decisions deferred |
| Before Photo | Files & Media | Photo before this session |
| After Photo | Files & Media | Photo after (the reward!) |
| Bags/Boxes Removed | Number | Physical volume removed (motivating metric) |
| Follow-Up Needed | Text | Anything that requires a return visit or purchase |
| Status | Select | Completed / In Progress / Paused / Planned |
| Tags | Multi-select | Quick Win / Deep Clean / Seasonal / Maintenance / First Pass / Second Pass / Final Edit |
| Notes | Text | Observations, discoveries, lessons learned |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month
- **By Room** — Table, grouped by Room Name
- **Calendar** — Calendar view by Date
- **Donations Pending** — Filter: Items Donated > 0 AND Donation Drop-Off = false (remind yourself to actually deliver!)
- **Planned** — Filter: Status = Planned (upcoming sessions to schedule)
- **Progress Photos** — Gallery view showing Before/After Photos
- **By Category** — Table, grouped by Category Tackled
- **Revenue Tracker** — Filter: Items Sold > 0, showing Sale Revenue (motivation from money earned)
- **Impact Summary** — Table showing Date, Room Name, Items Removed Total, Duration, Declutter Rate %

---

### 3. Maintenance Schedule

**Purpose:** Recurring maintenance tasks that keep your organized spaces from sliding back into chaos. Covers daily tidying, weekly resets, monthly deep maintenance, and seasonal overhauls. The key to organization is maintenance, not one-time cleanouts.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Task Name | Title | Specific task — e.g. "Wipe down kitchen counters" |
| Room | Relation | → Rooms & Zones database |
| Room Name | Rollup | From linked Room |
| Category | Select | Tidying / Cleaning / Deep Cleaning / Organizing / Purging / Restocking / Seasonal Swap / Inspection / Repair |
| Frequency | Select | Daily / Every Other Day / Weekly / Bi-weekly / Monthly / Quarterly / Semi-annually / Annually / Seasonally |
| Day of Week | Multi-select | Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday (for daily/weekly tasks) |
| Season | Multi-select | Spring / Summer / Fall / Winter (for seasonal tasks) |
| Time Required (mins) | Number | How long this task takes |
| Best Time of Day | Select | Morning / Midday / Afternoon / Evening / Anytime |
| Priority | Select | Essential / Important / Nice to Have |
| Assigned To | Text | Who is responsible (if household has multiple people) |
| Last Completed | Date | When this was last done |
| Next Due | Date | When this needs to happen next |
| Overdue | Formula | `if(and(not(empty(prop("Next Due"))), prop("Next Due") < now()), true, false)` |
| Days Overdue | Formula | `if(prop("Overdue"), format(dateBetween(now(), prop("Next Due"), "days")) + " days overdue", "On track")` |
| Streak | Number | Consecutive completions without missing |
| Total Completions | Number | All-time completions |
| Completion Rate | Text | Rough percentage — "on track" or "frequently missed" |
| Instructions | Text | Step-by-step for the task (useful if delegating or for consistency) |
| Supplies Needed | Text | What products/tools are required |
| Checklist | Text | Sub-steps within this task (use as a reference) |
| Difficulty | Select | Effortless / Easy / Moderate / Hard / Hate It |
| Skippable | Checkbox | Can this be skipped without consequence for one cycle? |
| Status | Select | Active / Paused / Seasonal Only / Retired |
| Tags | Multi-select | Quick / Deep / Requires Products / Two-Person Job / Music Recommended / Podcast Task |
| Notes | Text | Tips, shortcuts, or motivational notes |

**Views:**

- **All Tasks** — Table, sorted by Frequency then Task Name
- **Today's Tasks** — Filter: Day of Week includes today AND Frequency = Daily, plus any Overdue tasks
- **This Week** — Filter: Frequency = Weekly AND Next Due is this week
- **Overdue** — Filter: Overdue = true, sorted by Days Overdue descending (most overdue first)
- **By Room** — Table, grouped by Room Name
- **By Frequency** — Table, grouped by Frequency
- **Daily Routine** — Filter: Frequency = Daily, sorted by Best Time of Day
- **Weekly Reset** — Filter: Frequency = Weekly, sorted by Day of Week
- **Monthly Tasks** — Filter: Frequency = Monthly
- **Seasonal Tasks** — Filter: Frequency = Seasonally or Season is not empty, grouped by Season
- **Quick Tasks** — Filter: Time Required <= 10 (grab one when you have a few minutes)
- **By Person** — Table, grouped by Assigned To (for household task division)

---

### 4. Storage Solutions & Purchases

**Purpose:** Track every organizational product, storage solution, and system you purchase or implement. Includes where it's used, cost, effectiveness rating, and links to purchase again. Prevents re-buying things that didn't work and helps replicate what did.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Product Name | Title | What you bought — e.g. "Clear stackable bins (set of 6)" |
| Room | Relation | → Rooms & Zones database |
| Room Name | Rollup | From linked Room |
| Category | Select | Bins & Containers / Shelving / Drawer Organizers / Closet Systems / Labels / Hooks & Hangers / Over-Door Solutions / Under-Bed / Vacuum Storage / File/Paper / Cabinet Inserts / Lazy Susan / Baskets / Furniture / Wall-Mounted / Miscellaneous |
| Brand | Text | Brand name |
| Where Purchased | Select | Amazon / Target / IKEA / Container Store / Walmart / Home Depot / Dollar Store / Thrift Store / DIY / Other |
| Purchase URL | URL | Link to rebuy |
| Cost | Number (USD) | Price paid |
| Quantity | Number | How many you bought |
| Date Purchased | Date | When you got it |
| Date Installed | Date | When you put it to use |
| Status | Select | In Use / Returned / Sold / Gave Away / Broken / Planned / In Cart |
| Effectiveness | Select | Game Changer / Very Helpful / Helpful / Neutral / Waste of Money / Returned |
| Still Organized | Checkbox | Is the space this product is in still well-organized? |
| Dimensions | Text | Size info for reference — e.g. "12x8x6 inches" |
| Color | Text | For aesthetic consistency |
| Specific Location | Text | Exactly where in the room — e.g. "Upper left cabinet, second shelf" |
| Problem It Solves | Text | What issue this product addresses |
| Would Rebuy | Checkbox | Would you buy this again? |
| Would Recommend | Checkbox | Would you recommend to a friend? |
| Rating | Select | 5 Stars / 4 Stars / 3 Stars / 2 Stars / 1 Star |
| Photo | Files & Media | Photo of product in use |
| Notes | Text | Tips for use, alternatives considered, assembly notes |
| Tags | Multi-select | Budget / Premium / Aesthetic / Functional / Temporary / Permanent / Modular / Stackable |

**Views:**

- **All Products** — Table, sorted by Date Purchased descending
- **In Use** — Filter: Status = In Use, grouped by Room Name
- **By Category** — Table, grouped by Category
- **Game Changers** — Filter: Effectiveness = Game Changer or Very Helpful (replicate these!)
- **Waste of Money** — Filter: Effectiveness = Waste of Money or Returned (learn from mistakes)
- **Budget Tracker** — Table showing Product Name, Cost, Room Name, Effectiveness (total cost at bottom)
- **Shopping List** — Filter: Status = Planned or In Cart
- **By Store** — Table, grouped by Where Purchased
- **Would Rebuy** — Filter: Would Rebuy = true (your go-to products list)
- **Recently Purchased** — Filter: Date Purchased within 30 days

---

## SEASONAL DEEP-CLEAN CHECKLISTS

> These are pre-built checklists for each season. Copy them into the Maintenance Schedule database as seasonal tasks or use them as reference guides during your quarterly deep cleans.

### Spring Deep Clean

| Task | Room/Zone | Time (mins) | Notes |
|---|---|---|---|
| Wash all windows inside and out | Whole House | 120 | Use vinegar solution |
| Flip and rotate mattresses | Bedrooms | 30 | |
| Deep clean oven and stovetop | Kitchen | 45 | Use baking soda paste overnight |
| Clean behind and under refrigerator | Kitchen | 30 | Pull out, vacuum coils |
| Wash all curtains and blinds | Whole House | 90 | Check care labels |
| Clean ceiling fans and light fixtures | Whole House | 60 | Pillowcase trick for fan blades |
| Power wash exterior (deck, patio, siding) | Outdoor | 120 | Rent washer if needed |
| Clean and organize garage | Garage | 180 | Full purge + reorganize |
| Swap winter → summer wardrobes | Bedrooms | 60 | Declutter while swapping |
| Deep clean all bathrooms (grout, caulk) | Bathrooms | 90 | Re-caulk if needed |
| Wash all bedding including pillows and duvets | Bedrooms | 60 | Check pillow replacement (every 2 years) |
| Clean out and organize pantry | Kitchen | 45 | Check expiration dates |
| HVAC filter replacement | Utility | 15 | Note size for reorder |
| Clean dryer vent | Laundry | 30 | Fire prevention |
| Organize medicine cabinet, check expirations | Bathroom | 20 | Dispose properly |
| Garden prep — clean planters, prep soil | Outdoor | 60 | |

### Summer Deep Clean

| Task | Room/Zone | Time (mins) | Notes |
|---|---|---|---|
| Deep clean grill and outdoor furniture | Outdoor | 60 | |
| Clean and organize kids' rooms pre-school | Bedrooms | 90 | Purge outgrown items |
| Wash exterior windows | Whole House | 60 | |
| Clean ceiling fans (running constantly) | Whole House | 30 | |
| Organize summer gear (pool, sports, camping) | Garage/Storage | 60 | |
| Deep clean refrigerator and freezer | Kitchen | 45 | Defrost if needed |
| Clean and treat deck/patio furniture | Outdoor | 45 | Seal wood if needed |
| Organize entryway for summer gear | Entryway | 30 | Swap shoe storage |
| Check and clean gutters | Outdoor | 45 | After spring pollen |
| Wash all throw blankets and pillow covers | Living Room | 30 | |
| Clean and organize craft/hobby supplies | Home Office | 45 | |
| Purge expired sunscreen and pool chemicals | Garage | 15 | |

### Fall Deep Clean

| Task | Room/Zone | Time (mins) | Notes |
|---|---|---|---|
| Swap summer → winter wardrobes | Bedrooms | 60 | Declutter as you go |
| Deep clean and organize coat closet | Entryway | 45 | Make room for winter coats |
| Clean and store outdoor furniture | Outdoor | 60 | Cover or bring inside |
| Clean gutters before winter | Outdoor | 45 | |
| HVAC inspection and filter change | Utility | 30 | Schedule professional service |
| Wash all blankets and winter bedding | Bedrooms | 45 | Before they're needed |
| Deep clean and organize holiday decor storage | Attic/Storage | 60 | Toss broken items |
| Clean fireplace and chimney | Living Room | 30 | Professional if needed |
| Organize pantry for holiday baking | Kitchen | 30 | Stock up and arrange |
| Deep clean oven before holiday cooking | Kitchen | 45 | |
| Weatherstripping check on doors/windows | Whole House | 30 | Replace if worn |
| Organize kids' toys before gift influx | Bedrooms | 60 | Donate outgrown items |
| Test smoke and CO detectors, replace batteries | Whole House | 15 | |

### Winter Deep Clean

| Task | Room/Zone | Time (mins) | Notes |
|---|---|---|---|
| Post-holiday decor takedown and organization | Whole House | 90 | Label everything clearly |
| Purge new-year — closet cleanout | Bedrooms | 60 | New year, fresh start |
| Deep clean kitchen after holiday season | Kitchen | 60 | Behind appliances |
| Organize paperwork, file taxes prep | Home Office | 90 | Shred old documents |
| Clean and organize storage areas | Basement/Attic | 120 | Annual purge of stored items |
| Wash all walls and baseboards | Whole House | 120 | Magic eraser for scuffs |
| Deep clean carpets (shampoo or steam) | Whole House | 90 | Rent machine or hire out |
| Organize digital files and photos | Home Office | 60 | Back up and delete |
| Clean under all furniture | Whole House | 60 | Move and vacuum |
| Inventory cleaning supplies, restock | Utility | 20 | |
| Assess storage solutions — what's working? | Whole House | 30 | Note what to replace/add |
| Update home inventory for insurance | Home Office | 60 | Photograph valuable items |

---

## AUTOMATIONS / FORMULAS

### Maintenance Overdue Detection

Flags rooms where scheduled maintenance is past due.

```
if(
  and(
    not(empty(prop("Next Maintenance Due"))),
    prop("Next Maintenance Due") < now()
  ),
  true,
  false
)
```

### Days Since Organized

Shows how long since a room was last fully organized.

```
if(
  empty(prop("Last Organized")),
  "Never organized",
  format(dateBetween(now(), prop("Last Organized"), "days")) + " days"
)
```

### Declutter Rate

Percentage of reviewed items that were removed from the space.

```
if(
  prop("Items Reviewed") == 0,
  "—",
  format(round(prop("Items Removed Total") / prop("Items Reviewed") * 100)) + "%"
)
```

### Items Removed Total

Sum of all items removed through any method.

```
prop("Items Trashed") + prop("Items Donated") + prop("Items Sold") + prop("Items Relocated")
```

### Task Overdue Days

Shows how many days a maintenance task is overdue.

```
if(
  and(not(empty(prop("Next Due"))), prop("Next Due") < now()),
  format(dateBetween(now(), prop("Next Due"), "days")) + " days overdue",
  "On track"
)
```

### Budget Remaining Per Room

Calculate available budget for storage purchases.

```
if(
  prop("Budget Allocated") == 0,
  "No budget set",
  "$" + format(prop("Budget Allocated") - prop("Budget Spent")) + " remaining"
)
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Rooms

- Open the **Rooms & Zones** database and add every space in your home
- Be specific — "Kitchen Pantry" and "Kitchen Cabinets" are separate entries from "Kitchen Counters"
- For each room, set the current Organization Status honestly
- Set Priority based on which rooms bother you most or impact your daily life most
- Add your Vision for each room — what does it look like perfectly organized?

### Step 2 — Assess and Photograph

- Walk through your home with your phone
- Take a "Before Photo" of every room/zone (you will thank yourself later)
- In each room, note the Problem Areas
- Estimate the time to organize each space
- This initial audit takes 30–60 minutes but creates your roadmap

### Step 3 — Build Your Maintenance Schedule

- Open **Maintenance Schedule** and add recurring tasks for each room
- Start with the essentials: daily countertop wipe, weekly vacuum, monthly fridge clean, etc.
- Set realistic frequencies — it's better to maintain a modest schedule than to create an ambitious one you'll ignore
- Assign tasks to household members if applicable

### Step 4 — Plan Your First Declutter Sessions

- Open **Declutter Sessions** and create 3–5 planned sessions
- Start with a Quick Win — the messiest room that would give you the most relief
- Schedule sessions for specific days (put them on your calendar)
- A good first session: 30–60 minutes, one small zone, low emotional difficulty

### Step 5 — Execute Your First Session

- When it's time, set a timer and start
- Use the session record to track items as you sort: Keep / Trash / Donate / Sell / Relocate
- Don't try to organize and declutter in the same session — declutter first, organize second
- Take Before and After photos
- Log everything in the Declutter Sessions database when done

### Step 6 — Establish Your Rhythms

**Daily (5–10 minutes):**

- Check "Today's Tasks" in Maintenance Schedule
- Do your daily tidying tasks (counters, dishes, quick pickup)
- Reset each room to baseline before bed

**Weekly (30 minutes):**

- Complete all weekly maintenance tasks
- Do one 20-minute declutter session (even a single drawer counts)
- Mark completed tasks and update streaks

**Monthly (1–2 hours):**

- Complete monthly maintenance tasks
- Do one deeper declutter session (closet, pantry, garage section)
- Review Room Status — update any that have improved or slipped
- Order any storage solutions identified as needed

**Quarterly/Seasonal (half day):**

- Work through the seasonal deep-clean checklist
- Seasonal wardrobe/gear swaps
- Major declutter sessions for storage areas
- Assess which storage solutions are working and which need replacement

### Pro Tips

- The #1 rule of organization: every item needs a home. If something doesn't have a designated spot, it will end up on a surface
- Declutter BEFORE buying storage solutions — you might not need that Container Store haul once you remove 40% of the stuff
- The "one in, one out" rule prevents future accumulation — every new item means something leaves
- Photograph storage setups that work well (use the Storage Solutions database) — when things inevitably get messed up, you have a reference photo to reset to
- Label everything. Even if you "know where things go," labels help everyone in the household maintain the system
- Set a donation bag in each closet — add items as you notice them, drop off when full (no hoarding of "to donate" piles)
- Schedule seasonal deep cleans as non-negotiable calendar events — treat them like appointments
- Track Sale Revenue from sold items in Declutter Sessions — the money earned is excellent motivation
- If a room keeps reverting to chaos, the organizational system isn't working for that space. Re-evaluate the storage solutions rather than blaming yourself
- Take progress photos quarterly and compare to your "Before" photos — visible progress maintains motivation through the long haul
