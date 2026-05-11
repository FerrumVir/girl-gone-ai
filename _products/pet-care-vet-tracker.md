# Pet Care & Vet Visit Tracker — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with medication reminders, feeding schedules, vet visit histories, and expense tracking already configured. Read the Quick-Start Guide at the bottom before adding your first pet's profile.

---

## DATABASES

---

### 1. Pet Profiles

**Purpose:** Complete profile for each pet in your household. Medical history, dietary needs, emergency info, behavioral notes, and care instructions all in one place. Essential for pet sitters, emergencies, and multi-pet households.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Pet Name | Title | Your pet's name |
| Species | Select | Dog / Cat / Bird / Fish / Rabbit / Hamster / Guinea Pig / Reptile / Horse / Ferret / Other |
| Breed | Text | Breed or mix description |
| Color/Markings | Text | Physical description for identification |
| Date of Birth | Date | Birthday or estimated birth date |
| Age | Formula | `if(empty(prop("Date of Birth")), "Unknown", format(dateBetween(now(), prop("Date of Birth"), "years")) + " years")` |
| Adoption Date | Date | When they joined your family |
| Sex | Select | Male / Female / Male (Neutered) / Female (Spayed) |
| Weight (lbs) | Number | Current weight |
| Weight Goal | Number | Target weight if on a plan |
| Microchip Number | Text | ID number for microchip |
| Microchip Registry | Text | Which registry (HomeAgain, AKC, etc.) |
| License Number | Text | City/county pet license |
| Insurance Provider | Text | Pet insurance company |
| Policy Number | Text | Insurance policy number |
| Primary Vet | Text | Veterinarian name and clinic |
| Vet Phone | Phone | Clinic phone number |
| Vet Address | Text | Clinic address |
| Emergency Vet | Text | After-hours emergency vet clinic |
| Emergency Vet Phone | Phone | Emergency clinic number |
| Allergies | Text | Known food or environmental allergies |
| Medical Conditions | Text | Chronic conditions, ongoing concerns |
| Current Medications | Rollup | Names of active medications from linked Medications |
| Dietary Needs | Text | Food type, amount, restrictions |
| Food Brand | Text | Current food brand and formula |
| Feeding Schedule | Text | Times and amounts — e.g. "1 cup AM, 1 cup PM" |
| Treats Allowed | Text | Approved treats and daily limits |
| Behavioral Notes | Text | Temperament, triggers, training level |
| Fears/Anxieties | Text | Thunder, fireworks, other dogs, vet visits, etc. |
| Favorite Activities | Text | What they love — walks, fetch, cuddles, etc. |
| Training Commands | Text | Commands they know |
| Grooming Schedule | Text | How often, what type — e.g. "Bath monthly, nails every 2 weeks" |
| Last Grooming | Date | Most recent grooming session |
| Next Grooming Due | Date | When next grooming is needed |
| Spayed/Neutered | Checkbox | Has been fixed? |
| Spay/Neuter Date | Date | When procedure was done |
| Rabies Vaccination | Date | Current rabies vaccine date |
| Rabies Expiration | Date | When rabies vaccine expires |
| DHPP/FVRCP Date | Date | Core vaccine date |
| Core Vaccine Expiration | Date | When next core vaccine is due |
| Photo | Files & Media | Current photo (update annually) |
| Pet Sitter Notes | Text | Instructions for when someone else cares for them |
| Emergency Plan | Text | What to do in an emergency — authorized spending, DNR preferences, etc. |
| Status | Select | Active / Deceased / Rehomed / Foster |
| Total Vet Visits | Rollup | Count of linked Vet Visits |
| Total Expenses | Rollup | Sum of Amount from linked Expenses |
| Annual Cost | Formula | Estimated yearly cost based on recurring expenses |
| Linked Vet Visits | Relation | → Vet Visits database |
| Linked Medications | Relation | → Medications database |
| Linked Feeding Log | Relation | → Daily Care Log database |
| Linked Expenses | Relation | → Expenses database |
| Notes | Text | General notes, history, personality observations |

**Views:**

- **All Pets** — Table, sorted by Pet Name
- **Active Pets** — Filter: Status = Active
- **Pet Cards** — Gallery view with Photo, Pet Name, Species, Breed, Age
- **Medical Summary** — Table showing Pet Name, Allergies, Medical Conditions, Current Medications, Rabies Expiration
- **Vaccination Due** — Filter: Rabies Expiration or Core Vaccine Expiration within 30 days
- **Pet Sitter Reference** — Table showing Pet Name, Feeding Schedule, Medications, Behavioral Notes, Emergency contacts

---

### 2. Vet Visits

**Purpose:** Complete record of every veterinary visit — wellness checks, sick visits, emergencies, and procedures. Stores diagnoses, treatments, prescriptions, and costs. Critical for tracking health trends, sharing history with new vets, and insurance claims.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Visit Title | Title | Brief description — e.g. "Annual wellness exam" or "Limping — left rear leg" |
| Pet | Relation | → Pet Profiles database |
| Pet Name | Rollup | From Pet relation |
| Date | Date | Visit date and time |
| Clinic | Text | Which vet clinic |
| Veterinarian | Text | Specific vet seen |
| Visit Type | Select | Wellness/Annual / Sick Visit / Emergency / Surgery / Dental / Vaccination / Follow-Up / Lab Work / Imaging / Behavioral / Euthanasia / Other |
| Reason | Text | Why this visit was scheduled — symptoms, concerns |
| Symptoms | Text | What you observed before the visit |
| Diagnosis | Text | What the vet diagnosed |
| Treatment | Text | What was done during the visit |
| Procedures Performed | Multi-select | Physical Exam / Blood Work / Urinalysis / X-Ray / Ultrasound / Dental Cleaning / Dental Extraction / Surgery / Vaccination / Microchip / Nail Trim / Ear Clean / Expression / Biopsy / Cytology |
| Vaccinations Given | Multi-select | Rabies / DHPP / Bordetella / Leptospirosis / Canine Influenza / FVRCP / FeLV / Lyme |
| Weight at Visit | Number | Weight recorded at vet |
| Weight Change | Formula | Compare to previous visit weight |
| Medications Prescribed | Text | New medications prescribed at this visit |
| Dosage Instructions | Text | How to administer medications |
| Lab Results | Text | Key lab values or "all normal" |
| Lab Report | Files & Media | Upload lab result PDF |
| Follow-Up Needed | Checkbox | Does this require a return visit? |
| Follow-Up Date | Date | When to come back |
| Follow-Up Notes | Text | What to watch for, when to be concerned |
| Restrictions | Text | Activity restrictions — e.g. "No jumping for 2 weeks" |
| Recovery Notes | Text | How recovery went (fill in after) |
| Vet Recommendations | Text | Preventive care or lifestyle recommendations |
| Cost | Number (USD) | Total visit cost |
| Insurance Claimed | Checkbox | Did you submit to insurance? |
| Insurance Reimbursed | Number (USD) | Amount insurance paid back |
| Out of Pocket | Formula | `prop("Cost") - prop("Insurance Reimbursed")` |
| Documents | Files & Media | Discharge papers, prescriptions, imaging |
| Visit Rating | Select | Excellent Care / Good / Average / Concerned / Switching Vets |
| Questions for Next Visit | Text | Things to ask at the next appointment |
| Tags | Multi-select | Routine / Unexpected / Expensive / Surgery / Dental / Preventive / Senior Care / Chronic |
| Notes | Text | Additional observations, vet's demeanor, wait time |

**Views:**

- **All Visits** — Table, sorted by Date descending
- **By Pet** — Table, grouped by Pet Name
- **Upcoming** — Filter: Follow-Up Date is in the future, sorted by Follow-Up Date ascending
- **This Year** — Filter: Date is this year
- **By Visit Type** — Table, grouped by Visit Type
- **Vaccinations** — Filter: Visit Type = Vaccination, sorted by Date descending
- **Sick Visits** — Filter: Visit Type = Sick Visit or Emergency
- **Cost History** — Table showing Date, Pet Name, Visit Type, Cost, Insurance Reimbursed, Out of Pocket
- **Follow-Ups Due** — Filter: Follow-Up Needed = true AND Follow-Up Date <= today + 7 days
- **Lab History** — Filter: Procedures contains Blood Work or Urinalysis (track trends)
- **Weight History** — Table showing Date, Pet Name, Weight at Visit (plot trends)

---

### 3. Medications & Supplements

**Purpose:** Track all current and past medications, supplements, flea/tick preventives, and vitamins for each pet. Includes dosage schedules, refill dates, and administration tracking to ensure nothing is missed.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Medication Name | Title | Drug name — e.g. "Apoquel 16mg" or "NexGard Plus" |
| Pet | Relation | → Pet Profiles database |
| Pet Name | Rollup | From Pet relation |
| Type | Select | Prescription / Preventive / Supplement / OTC / Topical / Injectable |
| Category | Select | Flea/Tick / Heartworm / Pain / Anti-Inflammatory / Antibiotic / Allergy / Anxiety / Joint / Digestive / Eye/Ear / Thyroid / Heart / Seizure / Dental / Vitamin / Probiotic |
| Status | Select | Active / Discontinued / As Needed / Seasonal / Completed |
| Dosage | Text | Amount per dose — e.g. "16mg (1 tablet)" |
| Frequency | Select | Once Daily / Twice Daily / Every 8 Hours / Weekly / Bi-weekly / Monthly / Every 3 Months / As Needed |
| Administration Time | Text | When to give — e.g. "Morning with food" |
| Administration Method | Select | Oral (Tablet) / Oral (Liquid) / Topical / Injection / Chewable / Transdermal / Eye Drops / Ear Drops / Inhaler |
| With Food | Checkbox | Must be given with food? |
| Start Date | Date | When this medication was started |
| End Date | Date | When to stop (if applicable) |
| Days on Medication | Formula | `if(empty(prop("End Date")), format(dateBetween(now(), prop("Start Date"), "days")) + " days (ongoing)", format(dateBetween(prop("End Date"), prop("Start Date"), "days")) + " days (completed)")` |
| Prescribed By | Text | Which vet prescribed this |
| Reason | Text | Why this was prescribed — condition being treated |
| Side Effects to Watch | Text | What to look out for |
| Observed Side Effects | Text | What you've actually noticed |
| Refill Date | Date | When you need to refill/reorder |
| Refills Remaining | Number | How many refills left on prescription |
| Days Until Refill | Formula | `if(empty(prop("Refill Date")), "No refill date", if(dateBetween(prop("Refill Date"), now(), "days") <= 0, "REFILL NOW", format(dateBetween(prop("Refill Date"), now(), "days")) + " days"))` |
| Pharmacy | Text | Where to get refills |
| Monthly Cost | Number (USD) | Cost per month |
| Last Administered | Date | When you last gave this medication |
| Next Due | Date | When next dose is due |
| Overdue | Formula | `if(and(not(empty(prop("Next Due"))), prop("Next Due") < now(), prop("Status") == "Active"), true, false)` |
| Effectiveness | Select | Very Effective / Somewhat Effective / Uncertain / Ineffective / Made Worse |
| Notes | Text | Administration tips, storage requirements, interactions |
| Tags | Multi-select | Critical / Seasonal / Long-Term / Short-Term / Expensive / Refrigerate / Compounded |

**Views:**

- **All Medications** — Table, sorted by Status then Medication Name
- **Active Medications** — Filter: Status = Active, grouped by Pet Name
- **Daily Schedule** — Filter: Status = Active, sorted by Administration Time (daily checklist!)
- **Refills Due** — Filter: Days Until Refill = "REFILL NOW" or Refill Date within 7 days
- **By Pet** — Table, grouped by Pet Name
- **Preventives** — Filter: Type = Preventive (flea/tick, heartworm schedule)
- **Discontinued** — Filter: Status = Discontinued (history reference)
- **Monthly Cost** — Table showing active medications with Monthly Cost (total recurring med expense)
- **Overdue** — Filter: Overdue = true (missed doses!)
- **By Category** — Table, grouped by Category

---

### 4. Daily Care Log

**Purpose:** Daily log of feeding, exercise, bathroom habits, grooming, and notable behaviors. Especially valuable for pets with health issues, new pets establishing routines, multi-pet households, and when sharing care responsibilities.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Entry Title | Title | Auto-generated or brief note — e.g. "Luna — Mon 5/6" |
| Pet | Relation | → Pet Profiles database |
| Pet Name | Rollup | From Pet relation |
| Date | Date | Log date |
| Logged By | Text | Who logged this entry (for shared households) |
| Meals Fed | Multi-select | Breakfast / Lunch / Dinner / Snack |
| Food Amount | Text | How much was fed — e.g. "1 cup kibble + 2 tbsp pumpkin" |
| Food Brand | Text | If different from usual |
| Appetite | Select | Excellent / Normal / Reduced / Refused Food / Picky |
| Water Intake | Select | Normal / More Than Usual / Less Than Usual / Refused Water |
| Treats Given | Text | What and how many treats |
| Exercise Type | Multi-select | Walk / Run / Hike / Fetch / Swimming / Play Date / Dog Park / Indoor Play / Training Session |
| Exercise Duration (mins) | Number | Total active time |
| Exercise Intensity | Select | High / Moderate / Light / Rest Day |
| Bathroom - Pee | Select | Normal / Frequent / Straining / Accident / Blood |
| Bathroom - Poop | Select | Normal / Soft / Diarrhea / Constipated / Blood / Mucus / None |
| Poop Frequency | Number | Number of times |
| Vomiting | Checkbox | Did they vomit? |
| Vomit Details | Text | When, what it looked like, food or bile |
| Medications Given | Multi-select | List each med administered today |
| Medications Missed | Text | Any missed doses and why |
| Grooming Done | Multi-select | Bath / Brush / Nails / Teeth / Ears / Eyes / Paw Cleaning |
| Energy Level | Select | Very High / Normal / Low / Lethargic / Hyperactive |
| Mood | Select | Happy / Content / Anxious / Clingy / Aggressive / Withdrawn / Playful / Restless |
| Sleep Quality | Select | Normal / Restless / Excessive / Disrupted Night |
| Symptoms Observed | Text | Anything unusual — limping, scratching, coughing, etc. |
| Behavior Notes | Text | Anything notable about behavior today |
| Weight | Number | If weighed today |
| Temperature | Number | If taken (for sick pets) |
| Photos/Videos | Files & Media | Daily photos, funny moments, symptoms documentation |
| Concerns | Text | Anything you want to mention to the vet or monitor |
| Overall Day Rating | Select | Great Day / Good / Normal / Off Day / Concerning / Vet Needed |
| Tags | Multi-select | Normal / Sick Day / Recovery / New Food / Behavioral Change / Travel / Pet Sitter / Holiday |
| Notes | Text | Additional daily observations |

**Views:**

- **All Entries** — Table, sorted by Date descending
- **Today** — Filter: Date = today, grouped by Pet Name
- **By Pet** — Table, grouped by Pet Name, sorted by Date descending
- **This Week** — Filter: Date is this week
- **Calendar** — Calendar view by Date
- **Concerns** — Filter: Overall Day Rating = Concerning or Vet Needed
- **Symptom Log** — Filter: Symptoms Observed is not empty (show to vet)
- **Bathroom Issues** — Filter: Bathroom Poop != Normal OR Bathroom Pee != Normal
- **Exercise Log** — Table showing Date, Pet Name, Exercise Type, Duration (track activity levels)
- **Vomiting Log** — Filter: Vomiting = true (track patterns)
- **Weight Tracker** — Filter: Weight is not empty, sorted by Date (plot trends)
- **Medication Compliance** — Filter: Medications Missed is not empty

---

### 5. Expenses

**Purpose:** Track all pet-related spending — food, vet bills, medications, grooming, toys, boarding, insurance, and more. Provides a clear picture of the true cost of pet ownership and helps with budgeting and insurance claims.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Expense Name | Title | What you spent on — e.g. "Monthly heartworm prevention" |
| Pet | Relation | → Pet Profiles database |
| Pet Name | Rollup | From Pet relation |
| Date | Date | Purchase date |
| Category | Select | Vet Visit / Medication / Food / Treats / Grooming / Boarding/Daycare / Pet Sitting / Training / Toys / Beds/Furniture / Clothing/Accessories / Insurance Premium / Supplies / Emergency / Travel / License/Registration / Adoption/Purchase / Other |
| Amount | Number (USD) | Cost |
| Recurring | Checkbox | Is this a regular expense? |
| Frequency | Select | Weekly / Bi-weekly / Monthly / Quarterly / Annually / One-time |
| Vendor/Store | Text | Where purchased |
| Payment Method | Select | Credit Card / Debit / Cash / Insurance / Check |
| Insurance Covered | Checkbox | Will insurance reimburse? |
| Reimbursed | Number (USD) | Amount reimbursed by insurance |
| Net Cost | Formula | `prop("Amount") - prop("Reimbursed")` |
| Tax Deductible | Checkbox | If pet is a service/working animal |
| Receipt | Files & Media | Upload receipt |
| Vet Visit | Relation | → Vet Visits database (if related) |
| Notes | Text | Additional context |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Year | Formula | `formatDate(prop("Date"), "YYYY")` |
| Tags | Multi-select | Necessary / Optional / Splurge / Emergency / Budgeted / Unexpected |

**Views:**

- **All Expenses** — Table, sorted by Date descending
- **This Month** — Filter: Date is this month
- **By Pet** — Table, grouped by Pet Name (cost per pet)
- **By Category** — Table, grouped by Category (where money goes)
- **Monthly Summary** — Table grouped by Month with sum of Amount
- **Annual Summary** — Table grouped by Year
- **Recurring** — Filter: Recurring = true (your fixed pet costs)
- **Insurance Claims** — Filter: Insurance Covered = true, showing Amount, Reimbursed, Net Cost
- **Biggest Expenses** — Table sorted by Amount descending
- **Budget View** — Monthly grouped showing Category totals (for budgeting)
- **Vet Costs** — Filter: Category = Vet Visit or Medication (medical spending)

---

## MEDICATION SCHEDULE DASHBOARD

> Create this as a daily reference for administering medications across all pets.

```
┌────────────────────────────────────────────────────────────────┐
│  PET CARE COMMAND CENTER                                         │
├────────────────┬───────────────┬──────────────┬────────────────┤
│  Active Pets   │  Meds Today   │  Vet Visits  │  Monthly Cost  │
│     3          │     7 doses   │  1 upcoming  │    $342        │
├────────────────┴───────────────┴──────────────┴────────────────┤
│  TODAY'S MEDICATION SCHEDULE                                     │
│  [Linked view → Medications, Active, sorted by Admin Time]       │
│                                                                  │
│  Morning:                                                        │
│  - Luna: Apoquel 16mg (with breakfast)                          │
│  - Luna: NexGard Plus (1st of month only)                       │
│  - Max: Joint supplement                                         │
│                                                                  │
│  Evening:                                                        │
│  - Luna: Apoquel 16mg (with dinner)                             │
│  - Max: Gabapentin 100mg                                        │
├────────────────────────────────────────────────────────────────┤
│  REFILLS DUE SOON                                                │
│  [Linked view → Medications, filter: Refill within 14 days]      │
├─────────────────────────────────┬──────────────────────────────┤
│  UPCOMING VET VISITS            │  VACCINATION SCHEDULE          │
│  [Linked view → Vet Visits,    │  [Linked view → Pet Profiles,  │
│   upcoming follow-ups]          │   vaccine expirations]         │
├─────────────────────────────────┴──────────────────────────────┤
│  DAILY CARE LOG (today)                                          │
│  [Linked view → Daily Care Log, filter: Date = today]            │
├────────────────────────────────────────────────────────────────┤
│  RECENT CONCERNS                                                 │
│  [Linked view → Daily Care Log, filter: Concerns not empty,     │
│   last 7 days]                                                   │
└────────────────────────────────────────────────────────────────┘
```

---

## AUTOMATIONS / FORMULAS

### Pet Age Calculation

Human-readable age from date of birth.

```
if(
  empty(prop("Date of Birth")),
  "Unknown",
  format(dateBetween(now(), prop("Date of Birth"), "years")) + " years"
)
```

### Medication Refill Alert

Countdown to refill date or urgent alert if overdue.

```
if(
  empty(prop("Refill Date")),
  "No refill date set",
  if(
    dateBetween(prop("Refill Date"), now(), "days") <= 0,
    "REFILL NOW",
    format(dateBetween(prop("Refill Date"), now(), "days")) + " days"
  )
)
```

### Medication Overdue

Flags active medications past their next administration date.

```
if(
  and(
    not(empty(prop("Next Due"))),
    prop("Next Due") < now(),
    prop("Status") == "Active"
  ),
  true,
  false
)
```

### Vet Visit Cost After Insurance

Net out-of-pocket after insurance reimbursement.

```
prop("Cost") - prop("Insurance Reimbursed")
```

### Days on Medication

Duration tracking for medication history.

```
if(
  empty(prop("End Date")),
  format(dateBetween(now(), prop("Start Date"), "days")) + " days (ongoing)",
  format(dateBetween(prop("End Date"), prop("Start Date"), "days")) + " days (completed)"
)
```

### Expense Net Cost

After insurance reimbursement.

```
prop("Amount") - prop("Reimbursed")
```

### Vaccination Expiration Alert

Use in Pet Profiles views to surface upcoming vaccine due dates.

```
if(
  empty(prop("Rabies Expiration")),
  "No date",
  if(
    dateBetween(prop("Rabies Expiration"), now(), "days") <= 0,
    "EXPIRED",
    if(
      dateBetween(prop("Rabies Expiration"), now(), "days") <= 30,
      "Due in " + format(dateBetween(prop("Rabies Expiration"), now(), "days")) + " days",
      "Current"
    )
  )
)
```

---

## QUICK-START GUIDE

### Step 1 — Create Pet Profiles

- Open the **Pet Profiles** database and create a profile for each pet
- Essential fields first: Name, Species, Breed, Date of Birth, Weight, Sex
- Add vet information: Primary Vet, Vet Phone, Emergency Vet
- Enter current vaccination dates and expiration dates
- Add their Photo (you'll reference this card often)
- Fill in Feeding Schedule, Food Brand, and Dietary Needs
- Write Pet Sitter Notes as if a stranger needed to care for them tomorrow

### Step 2 — Enter Current Medications

- Open **Medications & Supplements** and add every active medication, preventive, and supplement
- For each: Dosage, Frequency, Administration Time, and Refill Date
- Set Status = Active for everything your pets are currently taking
- Calculate the next Refill Date and set it
- Include preventives: flea/tick, heartworm, and any seasonal medications

### Step 3 — Log Vet History

- Open **Vet Visits** and add visits from the past 12 months (at minimum)
- Focus on: wellness exams, vaccinations, and any significant sick visits
- Include upcoming follow-ups with their scheduled dates
- Upload any lab reports or discharge papers you have on hand

### Step 4 — Start Daily Logging

- Open **Daily Care Log** and create today's entry for each pet
- Log meals, exercise, bathroom habits, and medications given
- This takes 2–3 minutes per pet once you're in the habit
- The value compounds over time — patterns emerge that help your vet

### Step 5 — Set Up Expense Tracking

- Open **Expenses** and add recurring monthly costs: food, insurance premiums, preventive medications
- Add any vet bills from the past few months
- Mark recurring expenses so you can calculate your monthly pet budget
- Going forward, log every purchase as it happens

### Step 6 — Establish Your Routines

**Every morning (2 minutes per pet):**
- Check the medication schedule — administer morning meds
- Log breakfast in Daily Care Log
- Note any overnight issues (bathroom accidents, vomiting, restlessness)

**Every evening (2 minutes per pet):**
- Administer evening medications
- Log dinner, exercise, bathroom habits, energy level, and mood
- Note any symptoms or concerns

**Weekly (5 minutes):**
- Review the week's Daily Care Log — any patterns?
- Check Refills Due — order anything within 7 days of running out
- Weigh pets if tracking weight (monthly at minimum)
- Quick scan of upcoming vet appointments

**Monthly (10 minutes):**
- Review expense summary — on budget?
- Check vaccination expiration dates
- Schedule any upcoming vet visits
- Update weight in Pet Profiles
- Review grooming schedule — anything overdue?
- Refill medications before they run out (order 1 week before empty)

### Pro Tips

- The Daily Care Log is your #1 vet resource — when your vet asks "how long has this been happening?" you'll have exact dates and patterns
- Log bathroom habits consistently — changes in stool or urination frequency are often the first sign of health issues
- Upload vet documents immediately after every visit — you won't do it later
- For multi-pet households, the "By Pet" views are essential for keeping track of who needs what when
- Set Refill Date 7 days before you'll actually run out — shipping delays happen
- Track weight monthly for senior pets and pets with weight management goals — a slow 0.5 lb gain per month adds up to 6 lbs in a year
- The Emergency Plan field in Pet Profiles is critical — if something happens to you, can someone find this information?
- Use the Symptom Log view when calling your vet — specific dates and descriptions lead to faster diagnoses
- Pet insurance claims require documentation — the Vet Visits database with uploaded documents makes claims painless
- Photograph your pet quarterly in the same spot/pose — weight changes are visible over time even when daily changes are imperceptible
