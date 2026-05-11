# Esthetician Client Management System — Notion Template

> Duplicate this template into your Notion workspace. Full clinical-grade client management for solo estheticians and small spa teams. All databases are pre-linked with relations and rollups.

---

## DATABASES

---

### 1. Client Profiles

**Purpose:** Complete client records with skin history, treatment preferences, and relationship tracking.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Client Name | Title | First and last name |
| Phone | Phone | Primary contact |
| Email | Email | For confirmations and marketing |
| Date of Birth | Date | Age affects treatment protocols |
| Age | Formula | `dateBetween(now(), prop("Date of Birth"), "years")` |
| Client Since | Date | First appointment date |
| Fitzpatrick Type | Select | I / II / III / IV / V / VI |
| Skin Type | Select | Normal / Dry / Oily / Combination / Sensitive |
| Primary Concerns | Multi-select | Acne / Aging / Hyperpigmentation / Rosacea / Dehydration / Texture / Scarring / Sensitivity / Melasma / Large Pores / Dullness |
| Secondary Concerns | Multi-select | Same options as above |
| Allergies | Text | List all known allergies and sensitivities |
| Medications | Text | Current medications that affect skin (retinoids, hormones, antibiotics, etc.) |
| Contraindications | Multi-select | Accutane (current) / Accutane (past 6mo) / Pregnant / Nursing / Blood Thinners / Autoimmune / Diabetes / Active Herpes / Cancer Treatment / Seizure Disorder |
| Lifestyle Notes | Text | Sun exposure habits, smoking, diet, stress level, sleep quality |
| Preferences | Text | Pressure preference, temperature, music, conversation level, aromatherapy likes/dislikes |
| Home Care Routine | Text | Current AM and PM routine products |
| Home Care Compliance | Select | Excellent / Good / Fair / Poor / Unknown |
| Referral Source | Select | Instagram / Google / Referral / Walk-In / Yelp / TikTok / Website / Other |
| Referred By | Relation | -> Client Profiles (self-relation) |
| VIP | Checkbox | Loyalty program member or high-value client |
| Treatments | Relation | -> Treatment History |
| Total Visits | Rollup | Count of linked Treatments |
| Total Revenue | Rollup | Sum of Amount Paid from Treatments |
| Last Visit | Rollup | Latest date from linked Treatments |
| Days Since Visit | Formula | `dateBetween(now(), prop("Last Visit"), "days")` |
| Due for Appointment | Formula | `if(prop("Days Since Visit") > 35, true, false)` |
| Product Recommendations | Relation | -> Product Recs database |
| Photos | Relation | -> Photo Log |
| Notes | Text | General notes — personal details, conversation topics, family info |
| Status | Select | Active / Due for Rebook / At Risk / Lapsed / Inactive |

**Views:**
- **All Clients** — Table, sorted by name
- **Client Cards** — Gallery showing name, skin type, concerns, last visit
- **Active Clients** — Filter: Status = Active, sorted by Last Visit
- **Due for Rebook** — Filter: Due for Appointment = true, sorted by Days Since Visit descending
- **At Risk (60+ Days)** — Filter: Days Since Visit > 60 AND Total Visits > 2
- **Lapsed (90+ Days)** — Filter: Days Since Visit > 90
- **New Clients (Last 30 Days)** — Filter: Client Since within past 30 days
- **By Skin Type** — Grouped by Skin Type
- **By Primary Concern** — Grouped by Primary Concerns
- **VIP Clients** — Filter: VIP = true
- **Contraindication Alert** — Filter: Contraindications is not empty
- **Birthday This Month** — Filter: Date of Birth month = current month

---

### 2. Treatment History

**Purpose:** Clinical record of every treatment performed with protocols, products used, and outcomes.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Treatment Record | Title | Auto: "[Client] — [Service] — [Date]" |
| Client | Relation | -> Client Profiles |
| Date | Date | Treatment date |
| Service | Select | Custom Facial / Hydrafacial / Chemical Peel / Microneedling / Dermaplaning / LED Therapy / Microcurrent / Oxygen Facial / Enzyme Treatment / Acne Extraction / Back Facial / Body Treatment / Consultation / Other |
| Duration | Number | Minutes |
| Amount Paid | Number (USD) | Service price collected |
| Add-Ons | Multi-select | Extractions / LED Add-On / Dermaplaning Add-On / High-Frequency / Enzyme Boost / Eye Treatment / Lip Treatment / Neck & Decollete / Mask Upgrade / Peel Add-On |
| Protocol Used | Text | Step-by-step record of what was done |
| Products Applied | Text | Exact products used during treatment (brand, product name) |
| Peel Type & Strength | Text | If chemical peel: type, percentage, layers, time |
| Device Settings | Text | If machine-based: settings, intensity, passes |
| Skin Condition Today | Text | How skin presented at appointment |
| Areas Treated | Multi-select | Full Face / Forehead / T-Zone / Cheeks / Chin / Jawline / Neck / Decollete / Back / Hands |
| Extractions | Select | None / Minimal (under 5 min) / Moderate (5-10 min) / Extensive (10+ min) |
| Extraction Notes | Text | Location and type of congestion extracted |
| Client Tolerance | Select | Excellent / Good / Fair / Sensitive / Reactive |
| Reactions During Treatment | Text | Any redness, stinging, heat, sensitivity noted |
| Results Observed | Text | Immediate visible improvement, glow, texture change, etc. |
| Homecare Adjustments | Text | Any changes to home routine recommended today |
| Products Sold | Text | Retail products purchased at this visit |
| Product Revenue | Number (USD) | Retail sales amount |
| Before Photo | Files & media | Photo taken before treatment |
| After Photo | Files & media | Photo taken after treatment |
| Next Treatment Recommended | Text | What to do next time and when |
| Rebooking Date | Date | When they booked their next appointment |
| Provider Notes | Text | Internal notes not shared with client |
| Contraindication Check | Checkbox | Confirmed no contraindications before treatment |

**Views:**
- **By Client** — Grouped by Client, sorted by Date descending (see full history at a glance)
- **Today's Treatments** — Filter: Date = today
- **This Week** — Filter: Date within this week
- **This Month** — Filter: Date within this month
- **By Service Type** — Grouped by Service
- **Chemical Peels** — Filter: Service = Chemical Peel (track progression)
- **Revenue This Month** — Filter: Date within this month, showing sum of Amount Paid
- **Needs Follow-Up** — Filter: Date within past 3 days (for post-care check-in)

---

### 3. Product Recommendations

**Purpose:** Track what you've recommended to each client, what they've purchased, and what they're using.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Recommendation | Title | Product name + what it's for |
| Client | Relation | -> Client Profiles |
| Product Name | Text | Full product name |
| Brand | Text | Product brand |
| Category | Select | Cleanser / Toner / Serum / Moisturizer / SPF / Eye Cream / Exfoliant / Mask / Oil / Treatment / Retinoid / Vitamin C / Body |
| Purpose | Text | Why you recommended this specific product |
| Key Ingredients | Text | Active ingredients that make this right for them |
| Date Recommended | Date | When you first recommended it |
| Status | Select | Recommended / Purchased / Using / Repurchased / Discontinued / Reacted |
| Client Feedback | Text | How they feel about the product |
| Replaced By | Text | If discontinued, what replaced it |
| Retail Price | Number (USD) | Price point |
| Notes | Text | Usage instructions, frequency, where it fits in routine |

**Views:**
- **By Client** — Grouped by Client (see each person's full recommended routine)
- **Active Recommendations** — Filter: Status = Recommended or Using
- **Purchased** — Filter: Status = Purchased or Repurchased
- **Reactions** — Filter: Status = Reacted (know what to avoid)
- **By Category** — Grouped by Category

---

### 4. Photo Log

**Purpose:** Organized before/after photos linked to clients and treatments for progress tracking.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Photo Set | Title | "[Client] — [Date] — [Type]" |
| Client | Relation | -> Client Profiles |
| Treatment | Relation | -> Treatment History |
| Date Taken | Date | Photo date |
| Photo Type | Select | Before / After / Progress / Closeup / Full Face |
| Photos | Files & media | Upload photos here |
| Lighting | Select | Ring Light / Natural / Overhead |
| Angle | Select | Front / Left 45 / Right 45 / Left 90 / Right 90 |
| Notes | Text | What to observe in this photo |
| Shared with Client | Checkbox | Did you show/send this to the client? |
| Approved for Social | Checkbox | Client gave permission for social media use |

**Views:**
- **By Client (Gallery)** — Gallery view grouped by Client, showing photos
- **Before/After Pairs** — Filter for matching dates, side-by-side review
- **Social Media Approved** — Filter: Approved for Social = true
- **Recent (Last 30 Days)** — Filter: Date Taken within past 30 days

---

### 5. Rebooking & Follow-Up Tasks

**Purpose:** Never let a client fall through the cracks.

**Properties:**

| Property | Type | Notes |
|----------|------|-------|
| Task | Title | Description of the follow-up action |
| Client | Relation | -> Client Profiles |
| Type | Select | Post-Treatment Check-In / Rebooking Reminder / Product Follow-Up / Birthday / Re-Engagement / Series Reminder / Patch Test Follow-Up |
| Due Date | Date | When to complete this task |
| Status | Select | Pending / Completed / Skipped |
| Priority | Select | High / Medium / Low |
| Message Template | Text | Pre-written message to customize and send |
| Channel | Select | Text / Email / DM / Call |
| Completed Date | Date | When you actually did it |
| Result | Text | Did they respond? Did they book? |

**Views:**
- **Today's Tasks** — Filter: Due Date = today AND Status = Pending
- **This Week** — Filter: Due Date within this week AND Status = Pending
- **Overdue** — Filter: Due Date before today AND Status = Pending (RED FLAG)
- **Completed This Week** — Filter: Completed Date within this week

---

## TREATMENT PROTOCOL LIBRARY

### Protocol: Custom Facial (60 min)

```
STEP-BY-STEP PROTOCOL

1. CONSULTATION (5 min)
   - Review client card/history
   - Assess skin under magnification
   - Discuss concerns and goals for today
   - Confirm no contraindication changes

2. CLEANSE (5 min)
   - First cleanse: [PRODUCT] — remove makeup/SPF
   - Second cleanse: [PRODUCT] — deep clean
   - Technique: circular motions, include hairline and jawline

3. SKIN ANALYSIS (3 min)
   - Wood's lamp or magnifying lamp
   - Note: dehydration, congestion, sensitivity, changes
   - Update client card

4. EXFOLIATION (5-8 min)
   - Choose based on skin type:
     - Sensitive: enzyme exfoliant
     - Oily/congested: BHA or physical
     - Aging/dull: AHA (glycolic, lactic)
     - Combo: targeted application
   - Product: [PRODUCT]
   - Time on skin: [X] minutes

5. EXTRACTIONS (5-10 min, if needed)
   - Steam or desincrustation prep
   - Gentle pressure, proper technique
   - Focus areas: [note congested zones]
   - Stop if skin becomes too reactive
   - Apply antiseptic after

6. TREATMENT MASK / MODALITY (15 min)
   - Choose based on goals:
     - Hydration: hyaluronic/alginate mask
     - Calming: centella/aloe/chamomile
     - Brightening: vitamin C/arbutin
     - Anti-aging: peptides/collagen
   - Add device if applicable:
     - LED (red/blue/combo)
     - High frequency
     - Microcurrent
   - Scalp, hand, or arm massage during mask time

7. MASK REMOVAL + TONER (3 min)
   - Remove with warm towels
   - Apply balancing toner

8. SERUMS + MOISTURIZER + SPF (5 min)
   - Targeted serum: [PRODUCT]
   - Eye cream: [PRODUCT]
   - Moisturizer: [PRODUCT]
   - SPF (if daytime): [PRODUCT]

9. CONSULTATION CLOSE (5 min)
   - Show results (mirror + photos)
   - Explain what was done and why
   - Home care instructions
   - Product recommendations
   - Book next appointment
```

### Protocol: Chemical Peel (45 min)

```
PRE-PEEL CHECKLIST:
[ ] Contraindication review complete
[ ] No retinoids for [X] days confirmed
[ ] No recent sun exposure confirmed
[ ] Consent form signed
[ ] Patch test completed (if first peel)
[ ] Peel strength selected: __________

STEPS:
1. Double cleanse + degreasing prep
2. Protect sensitive areas (eyes, lips, nostrils)
3. Apply peel: [TYPE] at [STRENGTH]
   - Layer 1 — time: ____ Observation: ____
   - Layer 2 — time: ____ Observation: ____
   - Layer 3 — time: ____ Observation: ____
4. Neutralize (if required by peel type)
5. Remove completely
6. Apply post-peel calming products
7. SPF application
8. Aftercare instructions (verbal + printed)
9. Photo documentation
10. Schedule follow-up check-in (48 hours)
```

---

## CLIENT CONSULTATION TEMPLATES

### Initial Consultation Questions (Ask at First Visit)

```
1. What brings you in today?
2. What's your #1 skin concern right now?
3. How long have you been dealing with this?
4. What have you tried already? (Products, treatments)
5. What does your current morning routine look like?
6. What does your current evening routine look like?
7. Any allergies or sensitivities I should know about?
8. Current medications or supplements?
9. Are you pregnant, nursing, or trying to conceive?
10. How much sun exposure do you get weekly?
11. Stress level on a scale of 1-10?
12. How much water do you drink daily?
13. Any hormonal changes recently?
14. What's your budget for services? For products?
15. What does your ideal result look like?
```

### Progress Check-In Questions (Ask at Follow-Ups)

```
1. How has your skin been since our last session?
2. Any breakouts, dryness, sensitivity, or changes?
3. Have you been using the products we discussed?
4. How's your skin in the morning when you wake up?
5. Anything new — medication changes, stress, diet?
6. Are you happy with the progress so far?
7. Anything you'd like to adjust about our approach?
```

---

## FOLLOW-UP MESSAGE TEMPLATES

### 24-Hour Post-Treatment

**After Facial:**
"Hey [Name]! Just checking in after your facial yesterday. How's your skin feeling today? A little redness or sensitivity is normal for the first 24 hours. Remember: no actives tonight, SPF tomorrow, and keep it hydrated. Let me know if anything feels off!"

**After Peel:**
"Hi [Name]! Checking in on day 1 post-peel. Your skin may feel a bit tight or warm today — totally normal. Stick to your gentle cleanser + recovery moisturizer only. Absolutely no retinol, AHAs, or scrubbing for [X] days. Text me if you have any concerns at all."

**After Extractions (Heavy Session):**
"Hey [Name]! Your skin worked hard today with those extractions. You might see some redness or small bumps for 24-48 hours — that's normal healing. Ice if needed, no touching, and let it breathe tonight (minimal products). It's going to look amazing in 2-3 days."

### Rebooking Reminders

**Standard (at recommended interval):**
"Hi [Name]! It's been about [X] weeks since your last [service] — you're probably due for your next session. I have openings [DAY/TIME] and [DAY/TIME] this week. Want me to hold one for you?"

**Series Treatment Reminder:**
"Hey [Name]! You're [X/6] sessions into your [treatment series]. Session [X+1] should be in [X] days for optimal results. I have [DATE] or [DATE] available — which works better for you?"

### Product Check-In

"Hi [Name]! Just wanted to check — how's the [PRODUCT] working for you? It's been about [X] weeks since you started it. Are you noticing [expected benefit]? Let me know and I can adjust if needed."

---

## QUICK-START GUIDE

### Step 1: Import Your Clients
Add your current active clients to the Client Profiles database. Start with your top 20 regulars. Fill in: name, contact info, skin type, concerns, allergies, and any notes you remember. You'll fill in more detail at their next visit.

### Step 2: Start Logging Treatments
From today forward, create a Treatment History entry for every appointment. It takes 3-5 minutes after each client. Over time, this becomes an invaluable record of what works for each person.

### Step 3: Set Up Rebooking Tasks
After each completed treatment, create a follow-up task for 24 hours later (check-in) and a rebooking task at the recommended interval. Check these daily.

### Step 4: Document Products
When you recommend products, log them in the Product Recommendations database. Track what they buy and how they respond. This builds a complete picture of their home care compliance.

### Step 5: Take Photos Consistently
Before/after photos at every treatment (same lighting, same angle, same distance). Upload to the Photo Log linked to the client and treatment. This shows progress and builds your portfolio.

### Step 6: Review Weekly
Every Monday: check the "Due for Rebook" view, process overdue follow-ups, review this week's schedule for any clients with notes to remember (allergies, preferences, personal details).
