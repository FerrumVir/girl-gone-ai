# Home Renovation Budget Tracker — Google Sheets Template

---

## Setup Guide

### How to Import

1. Open Google Sheets (sheets.google.com)
2. Create a new blank spreadsheet
3. For each sheet below, create a new tab (click the "+" at the bottom)
4. Name each tab as indicated
5. Copy the column headers and sample data into each tab
6. The formulas use cell references — adjust if you insert or move columns

### Tips

- **Lock formula cells** — Protect cells containing formulas so you don't accidentally overwrite them
- **Use data validation** — For Status columns, create dropdown menus (Data > Data Validation)
- **Conditional formatting** — Set up color coding: green for under budget, yellow for 80-99%, red for over 100%
- **Currency formatting** — Select cost columns and format as Currency (Format > Number > Currency)
- **Mobile access** — Google Sheets works on mobile — check budgets from the hardware store

---

## SHEET 1: Budget Overview

> This is your command center. Check it before every spending decision.

### Column Layout

| Column | Header | Type | Notes |
|---|---|---|---|
| A | Room / Area | Text | Name of each room or project area |
| B | Total Budget | Currency | Allocated budget for this room |
| C | Total Spent | Currency | Formula: SUM of actual costs from Room Detail sheet |
| D | Remaining | Currency | Formula: `=B2-C2` |
| E | % Spent | Percentage | Formula: `=IF(B2>0, C2/B2, 0)` |
| F | Status | Text | Formula: `=IF(E2>1, "OVER BUDGET", IF(E2>0.8, "APPROACHING", "ON TRACK"))` |
| G | Notes | Text | Key decisions, change orders, budget adjustments |

### Pre-loaded Rooms

| Room / Area | Total Budget | Total Spent | Remaining | % Spent | Status |
|---|---|---|---|---|---|
| Kitchen | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Primary Bathroom | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Secondary Bathroom | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Primary Bedroom | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Living Room | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Dining Room | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Basement | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Exterior | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Landscaping | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| General / Whole House | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| Contingency (10-15%) | $0.00 | $0.00 | $0.00 | 0% | ON TRACK |
| **TOTAL** | **$0.00** | **$0.00** | **$0.00** | **0%** | |

### Summary Section (place above or below the table)

```
PROJECT SUMMARY
─────────────────────────────────
Total Project Budget:     $[SUM of Column B]
Total Spent to Date:      $[SUM of Column C]
Total Remaining:          $[SUM of Column D]
Overall % Complete:       [SUM(C)/SUM(B)]
Contingency Budget:       $[Contingency row, Column B]
Contingency Used:         $[Contingency row, Column C]
─────────────────────────────────
Rooms Over Budget:        [COUNTIF of Status = "OVER BUDGET"]
Rooms Approaching:        [COUNTIF of Status = "APPROACHING"]
Rooms On Track:           [COUNTIF of Status = "ON TRACK"]
```

### Conditional Formatting Rules

- Column F "Status":
  - "ON TRACK" → Green background (#d4edda)
  - "APPROACHING" → Yellow background (#fff3cd)
  - "OVER BUDGET" → Red background (#f8d7da)
- Column E "% Spent":
  - 0-79% → Green text
  - 80-99% → Orange text
  - 100%+ → Red text, bold

---

## SHEET 2: Room-by-Room Detail

> Create a section for each room. Use the same format for every room so the Budget Overview can pull totals.

### Column Layout (repeat per room)

| Column | Header | Type | Notes |
|---|---|---|---|
| A | Category | Text | Type of expense |
| B | Description | Text | Specific item or service |
| C | Budgeted | Currency | Planned cost |
| D | Actual | Currency | What you actually spent |
| E | Variance | Currency | Formula: `=C2-D2` (positive = under, negative = over) |
| F | % of Budget | Percentage | Formula: `=IF(C2>0, D2/C2, 0)` |
| G | Vendor / Contractor | Text | Who you paid |
| H | Date | Date | When purchased or invoiced |
| I | Notes | Text | Changes, substitutions, decisions |

### Kitchen Section (example — repeat format for each room)

```
═══════════════════════════════════════════════════════════════
KITCHEN                                    Budget: $______
═══════════════════════════════════════════════════════════════
```

| Category | Description | Budgeted | Actual | Variance | % | Vendor | Date | Notes |
|---|---|---|---|---|---|---|---|---|
| **Demolition** | | | | | | | | |
| Labor | Demolition and removal | | | | | | | |
| Disposal | Dumpster / haul-away | | | | | | | |
| **Cabinets** | | | | | | | | |
| Cabinets | Cabinet purchase | | | | | | | |
| Installation | Cabinet installation labor | | | | | | | |
| Hardware | Handles, pulls, hinges | | | | | | | |
| **Countertops** | | | | | | | | |
| Material | Countertop material (granite/quartz/etc.) | | | | | | | |
| Fabrication & Install | Template, cut, and install | | | | | | | |
| Backsplash | Material and installation | | | | | | | |
| **Appliances** | | | | | | | | |
| Refrigerator | | | | | | | | |
| Stove / Range | | | | | | | | |
| Dishwasher | | | | | | | | |
| Microwave / Range Hood | | | | | | | | |
| **Plumbing** | | | | | | | | |
| Sink | Sink fixture | | | | | | | |
| Faucet | Faucet fixture | | | | | | | |
| Plumbing labor | Rough-in and finish | | | | | | | |
| **Electrical** | | | | | | | | |
| Lighting fixtures | Under-cabinet, pendant, recessed | | | | | | | |
| Electrical labor | Wiring, outlets, switches | | | | | | | |
| **Flooring** | | | | | | | | |
| Flooring material | | | | | | | | |
| Flooring installation | | | | | | | | |
| **Paint** | | | | | | | | |
| Paint & supplies | | | | | | | | |
| Painting labor | | | | | | | | |
| **Permits** | | | | | | | | |
| Building permit | | | | | | | | |
| Electrical permit | | | | | | | | |
| Plumbing permit | | | | | | | | |
| **Miscellaneous** | | | | | | | | |
| Trim / molding | | | | | | | | |
| Window treatments | | | | | | | | |
| Unexpected costs | | | | | | | | |
| | **KITCHEN TOTAL** | **$0.00** | **$0.00** | **$0.00** | | | | |

### Bathroom Section

```
═══════════════════════════════════════════════════════════════
BATHROOM (Primary / Secondary)             Budget: $______
═══════════════════════════════════════════════════════════════
```

| Category | Description | Budgeted | Actual | Variance |
|---|---|---|---|---|
| **Demolition** | | | | |
| Labor | Demolition and removal | | | |
| **Tile** | | | | |
| Floor tile | Material | | | |
| Wall tile / shower tile | Material | | | |
| Tile installation | Labor | | | |
| Grout and supplies | | | | |
| **Fixtures** | | | | |
| Toilet | | | | |
| Vanity | | | | |
| Vanity top / sink | | | | |
| Faucet | | | | |
| Shower head / fixtures | | | | |
| Tub (if replacing) | | | | |
| Mirror | | | | |
| Towel bars / accessories | | | | |
| **Plumbing** | | | | |
| Plumbing labor | Rough-in and finish | | | |
| **Electrical** | | | | |
| Lighting fixtures | Vanity light, exhaust fan | | | |
| Electrical labor | | | | |
| **Flooring** | | | | |
| (if not tile) | Material and install | | | |
| **Paint** | | | | |
| Paint & supplies | | | | |
| **Glass** | | | | |
| Shower door / enclosure | | | | |
| **Permits** | | | | |
| Building permit | | | | |
| Plumbing permit | | | | |
| **Miscellaneous** | | | | |
| Unexpected costs | | | | |
| | **BATHROOM TOTAL** | **$0.00** | **$0.00** | **$0.00** |

### General / Whole House Section

```
═══════════════════════════════════════════════════════════════
GENERAL / WHOLE HOUSE                      Budget: $______
═══════════════════════════════════════════════════════════════
```

| Category | Description | Budgeted | Actual | Variance |
|---|---|---|---|---|
| HVAC | System replacement or repair | | | |
| Roof | Repair or replacement | | | |
| Windows | Replacement (specify count) | | | |
| Doors | Interior/exterior replacement | | | |
| Insulation | | | | |
| Drywall | Whole-house patching or replacement | | | |
| Interior paint | Whole-house painting | | | |
| Exterior paint | | | | |
| Flooring | Whole-house flooring | | | |
| Electrical panel | Upgrade | | | |
| Plumbing | Whole-house re-pipe | | | |
| Architectural / Design | Plans and consulting | | | |
| General contractor | GC management fee (if applicable) | | | |
| Insurance | Builder's risk or additional coverage | | | |
| Storage | Pod or unit during renovation | | | |
| Temporary housing | If living elsewhere during renovation | | | |
| | **GENERAL TOTAL** | **$0.00** | **$0.00** | **$0.00** |

---

## SHEET 3: Contractor Comparison

> Use this sheet when evaluating bids. Don't just go with the cheapest number.

### Comparison Layout (per project/room)

```
PROJECT: [Kitchen Remodel / Bathroom / etc.]
DATE BIDS COLLECTED: ___________
```

| Criteria | Contractor A | Contractor B | Contractor C | Contractor D |
|---|---|---|---|---|
| **Company Name** | | | | |
| **Contact Name** | | | | |
| **Phone** | | | | |
| **Email** | | | | |
| **License #** | | | | |
| **License Verified** | Yes / No | Yes / No | Yes / No | Yes / No |
| **Insurance Verified** | Yes / No | Yes / No | Yes / No | Yes / No |
| **Years in Business** | | | | |
| **References Checked** | Yes / No | Yes / No | Yes / No | Yes / No |
| | | | | |
| **BID DETAILS** | | | | |
| Total Bid Amount | $ | $ | $ | $ |
| Estimated Timeline | weeks | weeks | weeks | weeks |
| Payment Terms | | | | |
| Warranty Offered | | | | |
| | | | | |
| **INCLUSIONS** | | | | |
| Demolition included | Yes / No | Yes / No | Yes / No | Yes / No |
| Materials included | Yes / No | Yes / No | Yes / No | Yes / No |
| Permits included | Yes / No | Yes / No | Yes / No | Yes / No |
| Cleanup / disposal | Yes / No | Yes / No | Yes / No | Yes / No |
| Final inspection | Yes / No | Yes / No | Yes / No | Yes / No |
| | | | | |
| **SCORING (1-5 each)** | | | | |
| Price competitiveness | /5 | /5 | /5 | /5 |
| Timeline | /5 | /5 | /5 | /5 |
| Scope completeness | /5 | /5 | /5 | /5 |
| Credentials / experience | /5 | /5 | /5 | /5 |
| Communication quality | /5 | /5 | /5 | /5 |
| References / reviews | /5 | /5 | /5 | /5 |
| Warranty / guarantee | /5 | /5 | /5 | /5 |
| **TOTAL SCORE** | **/35** | **/35** | **/35** | **/35** |
| | | | | |
| **SELECTED** | Yes / No | Yes / No | Yes / No | Yes / No |
| **Reason for Selection** | | | | |

### Scoring Guide

- **5** — Excellent. Best among all bids.
- **4** — Good. Above average.
- **3** — Acceptable. Meets expectations.
- **2** — Below average. Concerns noted.
- **1** — Poor. Significant concerns.

### Red Flags to Watch For

- Bid is significantly lower than all others (may indicate missing scope or cut corners)
- No written contract or detailed scope of work
- Requests full payment up front (standard: 10-30% deposit, progress payments, final on completion)
- Cannot provide license number or proof of insurance
- No references or refuses to provide them
- Vague timeline with no milestones
- No warranty on workmanship

---

## SHEET 4: Material Cost Tracker

> Log every material purchase here. Sort by room to see where your materials budget is going.

### Column Layout

| Column | Header | Type | Notes |
|---|---|---|---|
| A | Date | Date | Purchase date |
| B | Vendor / Store | Text | Where you bought it |
| C | Item Description | Text | What you bought |
| D | Room / Area | Text | Which room this is for (use dropdown matching Budget Overview) |
| E | Category | Text | Material type: Lumber / Tile / Paint / Fixtures / Hardware / Appliances / Electrical / Plumbing / Flooring / Other |
| F | Quantity | Number | |
| G | Unit Price | Currency | Price per unit |
| H | Total Cost | Currency | Formula: `=F2*G2` |
| I | Payment Method | Text | Card / Cash / Check / Account |
| J | Receipt # / Ref | Text | Receipt number or reference for returns |
| K | Returned | Checkbox | Was this item returned? |
| L | Return Amount | Currency | Refund amount if returned |
| M | Net Cost | Currency | Formula: `=H2-L2` |
| N | Notes | Text | Color, size, model number — details for reordering |

### Summary Section (at bottom or separate area)

| Room | Total Materials Budget | Total Materials Spent | Remaining | Returns |
|---|---|---|---|---|
| Kitchen | | =SUMIF(Room="Kitchen", Net Cost) | | =SUMIF(Room="Kitchen", Return Amount) |
| Primary Bathroom | | | | |
| Secondary Bathroom | | | | |
| Bedroom | | | | |
| Living Room | | | | |
| Exterior | | | | |
| General | | | | |
| **TOTAL** | | | | |

---

## SHEET 5: Timeline / Gantt View

> Track your renovation phases against the plan. Catch delays before they cascade.

### Column Layout

| Column | Header | Type | Notes |
|---|---|---|---|
| A | Phase / Task | Text | Room name or specific work phase |
| B | Description | Text | What work is being done |
| C | Contractor | Text | Who is responsible |
| D | Planned Start | Date | |
| E | Planned End | Date | |
| F | Planned Duration | Number | Formula: `=E2-D2` (days) |
| G | Actual Start | Date | |
| H | Actual End | Date | |
| I | Actual Duration | Number | Formula: `=H2-G2` |
| J | Delay (Days) | Number | Formula: `=IF(H2>E2, H2-E2, IF(AND(G2>D2, ISBLANK(H2)), TODAY()-E2, 0))` |
| K | Status | Text | Not Started / In Progress / Completed / Delayed / On Hold |
| L | Dependencies | Text | What must be done before this can start |
| M | Notes | Text | Delay reasons, schedule changes |

### Pre-loaded Phases (customize to your project)

| Phase | Description | Planned Start | Planned End | Status |
|---|---|---|---|---|
| Planning & Design | Architectural plans, design decisions | | | Not Started |
| Permits | Submit and receive all required permits | | | Not Started |
| Demolition | Remove existing structures as needed | | | Not Started |
| Structural | Framing, load-bearing changes | | | Not Started |
| Rough Plumbing | Pipe relocation, rough-in | | | Not Started |
| Rough Electrical | Wiring, panel upgrades, rough-in | | | Not Started |
| HVAC | Ductwork, system installation | | | Not Started |
| Insulation | Wall and ceiling insulation | | | Not Started |
| Drywall | Hang, tape, mud, sand | | | Not Started |
| Tile Work | Bathroom/kitchen tile installation | | | Not Started |
| Cabinetry | Cabinet installation | | | Not Started |
| Countertops | Template, fabrication, install | | | Not Started |
| Flooring | Installation throughout | | | Not Started |
| Painting | Priming and painting | | | Not Started |
| Fixture Installation | Lighting, plumbing fixtures, hardware | | | Not Started |
| Appliance Installation | Kitchen appliances, washer/dryer | | | Not Started |
| Punch List | Final touch-ups and fixes | | | Not Started |
| Final Inspections | All required inspections | | | Not Started |
| Cleanup | Final cleaning and debris removal | | | Not Started |

### Visual Gantt (create using Google Sheets)

To create a visual Gantt chart:
1. In columns N onward, create date headers (one column per week)
2. Use conditional formatting: if the cell's column date falls between Planned Start and Planned End, fill with blue
3. If the cell's column date falls between Actual Start and Actual End, fill with green (or red if past Planned End)
4. This creates a visual bar chart of your timeline

---

## SHEET 6: Permit & Inspection Checklist

> Unpermitted work can derail a home sale. Track every permit from application to final inspection.

### Column Layout

| Column | Header | Type | Notes |
|---|---|---|---|
| A | Permit Type | Text | |
| B | Required | Yes/No | Is this permit required for your project? |
| C | Issuing Authority | Text | City/county building department |
| D | Application Date | Date | When you applied |
| E | Permit Fee | Currency | |
| F | Approval Date | Date | When approved |
| G | Permit Number | Text | |
| H | Inspection Required | Yes/No | |
| I | Inspection Date | Date | Scheduled or completed inspection |
| J | Inspector Name | Text | |
| K | Result | Text | Pass / Fail / Pending / Corrections Required |
| L | Re-inspection Date | Date | If corrections were required |
| M | Re-inspection Result | Text | Pass / Fail |
| N | Status | Text | Not Needed / Applied / Approved / Inspection Scheduled / Passed / Failed |
| O | Notes | Text | |

### Pre-loaded Permit Types

| Permit Type | Typical Requirement |
|---|---|
| Building Permit (General) | Required for most structural work, additions, and major remodels |
| Electrical Permit | Required for new circuits, panel upgrades, rewiring |
| Plumbing Permit | Required for new plumbing lines, fixture relocation, water heater |
| Mechanical/HVAC Permit | Required for new HVAC systems, ductwork changes |
| Demolition Permit | Required for removal of structures or walls |
| Roofing Permit | Required in many jurisdictions for re-roofing |
| Fence Permit | Required in many areas for new fences |
| Deck/Patio Permit | Required for new deck construction |
| Pool Permit | Required for pool installation or major modification |
| Grading Permit | Required for significant land grading or drainage changes |
| Tree Removal Permit | Required in some municipalities for removing mature trees |
| Historic District Permit | Required in historic districts for exterior changes |
| HOA Approval | Not a government permit but often required before work begins |

### Permit Cost Summary

```
Total Permit Fees:          $[SUM of Column E]
Permits Required:           [COUNT where Required = Yes]
Permits Approved:           [COUNT where Status = Approved or Passed]
Inspections Passed:         [COUNT where Result = Pass]
Inspections Pending:        [COUNT where Result = Pending]
```

---

## SHEET 7: ROI Calculator

> Use this before and after your renovation to estimate the impact on your home's resale value.

### ROI Estimation Table

Based on national averages from remodeling cost-vs-value reports. Your actual ROI will vary by market, quality, and current real estate conditions.

| Renovation Type | Avg. Cost | Avg. Value Added | Avg. ROI % | Your Cost | Est. Value Added | Your ROI % |
|---|---|---|---|---|---|---|
| Minor Kitchen Remodel | $28,000 | $22,100 | 78.9% | $ | =Your Cost * 0.789 | |
| Major Kitchen Remodel | $80,000 | $48,000 | 60.0% | $ | | |
| Bathroom Remodel (Midrange) | $25,000 | $17,300 | 69.1% | $ | | |
| Bathroom Remodel (Upscale) | $78,000 | $40,600 | 52.0% | $ | | |
| Bathroom Addition | $55,000 | $30,800 | 56.0% | $ | | |
| Wood Deck Addition | $18,000 | $12,100 | 67.2% | $ | | |
| Composite Deck Addition | $24,000 | $14,900 | 62.1% | $ | | |
| Siding Replacement (Vinyl) | $18,000 | $14,000 | 77.6% | $ | | |
| Siding Replacement (Fiber Cement) | $21,000 | $17,000 | 81.0% | $ | | |
| Window Replacement (Vinyl) | $22,000 | $14,700 | 66.8% | $ | | |
| Window Replacement (Wood) | $25,000 | $16,400 | 65.6% | $ | | |
| Roofing Replacement | $30,000 | $20,100 | 67.0% | $ | | |
| Garage Door Replacement | $4,500 | $4,200 | 93.3% | $ | | |
| Entry Door Replacement (Steel) | $2,200 | $2,000 | 90.9% | $ | | |
| Manufactured Stone Veneer | $11,000 | $10,900 | 99.1% | $ | | |
| Attic Insulation | $2,500 | $2,400 | 96.0% | $ | | |

### Your Project ROI Summary

```
RENOVATION ROI SUMMARY
─────────────────────────────────
Total Renovation Cost:        $[SUM of Your Cost column]
Estimated Total Value Added:  $[SUM of Est. Value Added column]
Net ROI:                      [((Value Added - Cost) / Cost) * 100]%
Estimated Net Gain / (Loss):  $[Value Added - Cost]

Current Home Value (est.):    $[YOUR ESTIMATE]
Post-Renovation Value (est.): $[Current + Value Added]

─────────────────────────────────
Note: These are estimates based on national averages.
Actual ROI depends on your local market, quality of
work, and current real estate conditions. Consult a
local real estate agent for market-specific estimates.
```

### Before & After Notes

Use this section to document each room's condition before and after renovation. Useful for insurance, resale, and personal records.

| Room | Before Notes | Before Photos | After Notes | After Photos | Key Improvements |
|---|---|---|---|---|---|
| Kitchen | | (link to photos) | | (link to photos) | |
| Primary Bathroom | | | | | |
| Secondary Bathroom | | | | | |
| Living Room | | | | | |
| Exterior | | | | | |
| Landscaping | | | | | |

---

## QUICK-START GUIDE

### Step 1 — Set Your Total Budget (5 minutes)
- Decide your total renovation budget including a 10-15% contingency
- Enter the total in the Budget Overview sheet
- Allocate budgets to each room/area you're renovating
- Fill in $0 for rooms you're not touching (or hide those rows)

### Step 2 — Build Room-by-Room Budgets (30 minutes)
- For each room you're renovating, go to the Room-by-Room Detail sheet
- Fill in budgeted amounts for each line item
- Use contractor estimates for labor, store prices for materials
- Don't skip the "miscellaneous" and "unexpected costs" lines — budget $500-$1,000 per room

### Step 3 — Collect and Compare Bids (as bids come in)
- For each major project, get at least 3 bids
- Enter each bid in the Contractor Comparison sheet
- Score each contractor on all 7 criteria
- Make your selection based on total score, not just price

### Step 4 — Set Your Timeline (15 minutes)
- Fill in the Timeline sheet with your planned phases and dates
- Note dependencies (can't tile until plumbing rough-in is done)
- Share the timeline with your contractor(s)

### Step 5 — Check Permits (15 minutes)
- Review the Permit Checklist and mark which permits are required
- Apply for permits before work begins
- Schedule inspections at appropriate milestones

### Step 6 — Track Everything As You Go
- Log every material purchase in the Material Cost Tracker as it happens
- Update the Room-by-Room Detail sheet when invoices come in
- Check the Budget Overview weekly to see your overall position
- Update the Timeline when phases start, end, or get delayed

### Weekly Review (10 minutes)
- Open the Budget Overview — are any rooms trending over?
- Check the Timeline — is anything delayed?
- Review the Material Cost Tracker — any large purchases coming up?
- Update any contractor payments in the Room-by-Room Detail

### Pro Tips

- **Budget 10-15% contingency.** Not 5%. Not "we'll figure it out." A real contingency line item that you don't touch unless needed. You will need it.
- **Track change orders religiously.** Every "while we're at it, can you also..." conversation is a change order. Get a price before saying yes. Log it immediately.
- **Pay contractors on a schedule, not up front.** Standard payment structure: 10-30% deposit, progress payments at milestones, 10% held until punch list is complete. Any contractor demanding full payment up front is a red flag.
- **Take photos constantly.** Before demo, during rough-in (while walls are open — document wiring and plumbing locations), after each phase. These are invaluable for insurance claims, warranty disputes, and future projects.
- **The cheapest bid is rarely the best bid.** Use the Contractor Comparison scoring system. A contractor who costs 15% more but includes permits, cleanup, and a 2-year warranty is often the better deal.
- **Materials always cost more than your first estimate.** Waste, breakage, miscounts, and "while I'm here" additions are real. Budget materials at 10-15% above the raw calculation.
- **Keep every receipt.** Especially for capital improvements — they may be tax-deductible or increase your cost basis when you sell the home. The Material Cost Tracker's receipt reference column exists for this reason.
- **Use the ROI Calculator before you commit to expensive finishes.** A $5,000 countertop in a $200,000 house has a different ROI than in a $600,000 house. Spend proportionally to your home's value and your neighborhood's expectations.
- **Share the Budget Overview with your partner.** Both people should be able to see the current financial state of the project at any time. Financial surprises during a renovation cause more stress than the renovation itself.
- **Update the spreadsheet the same day money changes hands.** The moment you pay an invoice or buy materials, log it. Batching updates leads to forgotten expenses and inaccurate budgets.
