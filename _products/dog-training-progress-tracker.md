# Dog Training Progress Tracker — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Track commands, log training sessions, monitor behavior patterns, manage socialization milestones, and keep vet records organized — all in one place.

---

> **SETUP GUIDE — Get Running in 15 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 7 tabs/sheets and name them: Command Tracker, Session Log, Progress Ratings, Socialization Checklist, Vet Records, Exercise Log, Behavior Incidents
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Start by filling in your dog's info and the Command Tracker with your training priorities
> 6. Log sessions daily — even 5-minute sessions count
>
> **Tip:** Consistency beats duration. Three 5-minute training sessions per day produce better results than one 30-minute session. Log every session to see your streak build.

---

## Dog Information

| Field | Value |
|-------|-------|
| Dog's Name | |
| Breed | |
| Age / Date of Birth | |
| Weight | lbs |
| Trainer/Owner Name | |
| Training Start Date | |
| Veterinarian | |
| Vet Phone | |
| Microchip # | |
| Special Needs / Notes | |

---

---

# SHEET 1: COMMAND TRACKER

> Track every command/behavior from introduction to full mastery across all environments.

---

## Proficiency Scale

| Level | Code | Description |
|:-----:|:----:|-------------|
| 0 | Not Started | Haven't introduced yet |
| 1 | Introduced | Dog has heard the cue, beginning to associate |
| 2 | Learning | Responds correctly ~50% of the time with lure/prompt |
| 3 | Practicing | Responds ~75% without lure, low distraction only |
| 4 | Reliable | Responds ~90% in familiar environments |
| 5 | Proofed | Responds reliably in any environment with distractions |

---

## Command/Behavior Master List

| Command | Category | Priority | Current Level | Date Introduced | Date Level 3 | Date Level 5 | Notes |
|---------|----------|:--------:|:-------------:|:---------------:|:-------------:|:-------------:|-------|
| Sit | Basic Obedience | High | /5 | | | | |
| Down | Basic Obedience | High | /5 | | | | |
| Stay | Basic Obedience | High | /5 | | | | |
| Come (Recall) | Basic Obedience | Critical | /5 | | | | |
| Leave It | Safety | Critical | /5 | | | | |
| Drop It | Safety | Critical | /5 | | | | |
| Wait | Impulse Control | High | /5 | | | | |
| Place (Go to Mat) | Impulse Control | High | /5 | | | | |
| Heel | Leash Skills | Medium | /5 | | | | |
| Loose Leash Walk | Leash Skills | High | /5 | | | | |
| Look at Me (Focus) | Foundation | High | /5 | | | | |
| Touch (Hand Target) | Foundation | Medium | /5 | | | | |
| Off | Manners | Medium | /5 | | | | |
| Quiet | Manners | Medium | /5 | | | | |
| Settle | Calm Behaviors | High | /5 | | | | |
| Crate (Kennel) | Management | High | /5 | | | | |
| Shake / Paw | Tricks | Low | /5 | | | | |
| Roll Over | Tricks | Low | /5 | | | | |
| Spin | Tricks | Low | /5 | | | | |
| Speak | Tricks | Low | /5 | | | | |
| Play Dead | Tricks | Low | /5 | | | | |
| Fetch / Bring | Play | Medium | /5 | | | | |
| Go Potty (on cue) | Practical | Medium | /5 | | | | |
| Car (Load Up) | Practical | Medium | /5 | | | | |
| Gentle (take treats softly) | Manners | High | /5 | | | | |
| Back Up | Advanced | Low | /5 | | | | |
| Through (weave legs) | Tricks | Low | /5 | | | | |
| Over (jump) | Agility | Low | /5 | | | | |
| Under (crawl under) | Tricks | Low | /5 | | | | |
| Find It (scent work) | Enrichment | Medium | /5 | | | | |
| [Custom 1] | | | /5 | | | | |
| [Custom 2] | | | /5 | | | | |
| [Custom 3] | | | /5 | | | | |
| [Custom 4] | | | /5 | | | | |
| [Custom 5] | | | /5 | | | | |

---

## Progress Summary

| Metric | Value |
|--------|------:|
| Total Commands Tracked | |
| Level 5 (Proofed) | |
| Level 4 (Reliable) | |
| Level 3 (Practicing) | |
| Level 2 (Learning) | |
| Level 1 (Introduced) | |
| Not Started | |
| **Overall Mastery %** | **%** |

`FORMULA (Overall Mastery): =COUNTIF(LevelColumn, 5) / COUNTA(CommandColumn) * 100`
`FORMULA (Level counts): =COUNTIF(LevelColumn, 5), =COUNTIF(LevelColumn, 4), etc.`

---

---

# SHEET 2: SESSION LOG

> Log every training session. Include what you practiced, duration, and how it went.

---

## Session Log Columns

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **Date** | **Time of Day** | **Duration (min)** | **Commands Practiced** | **Environment** | **Distraction Level** | **Success Rate** | **Treats/Rewards Used** | **Notes / What to Work On** |

---

## Time of Day (Dropdown)
- Morning (6am-10am)
- Midday (10am-2pm)
- Afternoon (2pm-6pm)
- Evening (6pm-10pm)

## Environment (Dropdown)
- Home - Inside
- Home - Backyard
- Neighborhood Walk
- Park (quiet)
- Park (busy)
- Pet Store
- Vet Office
- Friend's House
- Downtown / High Distraction
- Car
- Other

## Distraction Level (Dropdown)
- Low (quiet, familiar, no distractions)
- Medium (some distractions, manageable)
- High (many distractions, challenging)
- Extreme (other dogs, squirrels, crowds)

---

## Sample Session Entries

| Date | Time | Min | Commands | Environment | Distraction | Success | Rewards | Notes |
|------|------|:---:|----------|-------------|:-----------:|:-------:|---------|-------|
| 2026-01-15 | Morning | 10 | Sit, Down, Stay | Home - Inside | Low | 90% | Chicken | Stay duration up to 15 sec |
| 2026-01-15 | Afternoon | 5 | Recall | Home - Backyard | Medium | 70% | Hot dogs | Squirrel interrupted once |
| 2026-01-16 | Morning | 8 | Heel, Focus | Neighborhood | Medium | 60% | Cheese | Needs work near other dogs |
| 2026-01-16 | Evening | 5 | Place, Settle | Home - Inside | Low | 95% | Kibble | Great calm behavior |
| 2026-01-17 | Midday | 15 | Recall, Leave It | Park (busy) | High | 50% | Steak pieces | Too challenging, back up |

---

## Weekly Session Summary

| Week Of | Sessions Logged | Total Minutes | Avg Success Rate | Commands Worked | Best Session | Needs Work |
|---------|:--------------:|:-------------:|:----------------:|:--------------:|:-------------|:-----------|
| [date] | | min | % | | | |
| [date] | | min | % | | | |
| [date] | | min | % | | | |
| [date] | | min | % | | | |

`FORMULA (Sessions Logged): =COUNTIFS(Date, ">="&WeekStart, Date, "<="&WeekEnd)`
`FORMULA (Avg Success): =AVERAGEIFS(SuccessRate, Date, ">="&WeekStart, Date, "<="&WeekEnd)`

---

## Training Streak Tracker

| Metric | Value |
|--------|------:|
| Current Streak (consecutive days) | days |
| Longest Streak | days |
| Total Sessions This Month | |
| Total Training Minutes This Month | min |
| Average Session Length | min |

`FORMULA (Current Streak): Count consecutive dates with at least 1 entry`
`FORMULA (Avg Session Length): =SUM(Duration) / COUNT(Sessions)`

---

---

# SHEET 3: PROGRESS RATINGS

> Rate your dog's progress on key behaviors weekly. Watch the trend over time.

---

## Weekly Progress Score (Rate 1-10)

| Behavior | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 | Week 7 | Week 8 | Trend |
|----------|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:-----:|
| Recall reliability | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Leash manners | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Impulse control | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Calm in public | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Focus around distractions | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| House manners | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Greeting people calmly | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Dog-to-dog behavior | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Crate/confinement comfort | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| Overall obedience | /10 | /10 | /10 | /10 | /10 | /10 | /10 | /10 | |
| **AVERAGE** | **/10** | **/10** | **/10** | **/10** | **/10** | **/10** | **/10** | **/10** | |

`FORMULA (Average): =AVERAGE(B2:B11)`
`FORMULA (Trend): =IF(CurrentWeek > PreviousWeek, "Improving", IF(CurrentWeek < PreviousWeek, "Declining", "Stable"))`

---

## Monthly Milestone Check-In

| Month | Biggest Win | Biggest Challenge | Goal for Next Month | Trainer Notes |
|-------|-------------|-------------------|--------------------:|---------------|
| Month 1 | | | | |
| Month 2 | | | | |
| Month 3 | | | | |
| Month 4 | | | | |
| Month 5 | | | | |
| Month 6 | | | | |

---

---

# SHEET 4: SOCIALIZATION CHECKLIST

> Expose your dog to a variety of people, animals, environments, sounds, and surfaces. Check off each exposure. Goal: positive associations with all items.

---

## People (Goal: 50+ different people in first 3 months)

| Exposure Type | First Exposure Date | Reaction (1-5) | Positive? | Repeat Needed? | Notes |
|---------------|:-------------------:|:--------------:|:---------:|:--------------:|-------|
| Men with beards | | /5 | Y/N | Y/N | |
| Women with hats | | /5 | Y/N | Y/N | |
| Children (toddlers) | | /5 | Y/N | Y/N | |
| Children (school age) | | /5 | Y/N | Y/N | |
| Teenagers | | /5 | Y/N | Y/N | |
| Elderly people | | /5 | Y/N | Y/N | |
| People with wheelchairs | | /5 | Y/N | Y/N | |
| People with canes/walkers | | /5 | Y/N | Y/N | |
| Delivery person/uniform | | /5 | Y/N | Y/N | |
| Person running/jogging | | /5 | Y/N | Y/N | |
| Person on bicycle | | /5 | Y/N | Y/N | |
| Person with stroller | | /5 | Y/N | Y/N | |
| Large groups of people | | /5 | Y/N | Y/N | |
| People with umbrellas | | /5 | Y/N | Y/N | |

---

## Animals

| Exposure Type | First Exposure | Reaction | Positive? | Repeat? | Notes |
|---------------|:--------------:|:--------:|:---------:|:-------:|-------|
| Small dogs | | /5 | Y/N | Y/N | |
| Large dogs | | /5 | Y/N | Y/N | |
| Puppies | | /5 | Y/N | Y/N | |
| Cats | | /5 | Y/N | Y/N | |
| Birds | | /5 | Y/N | Y/N | |
| Squirrels/rabbits | | /5 | Y/N | Y/N | |
| Horses/livestock | | /5 | Y/N | Y/N | |

---

## Environments

| Environment | First Exposure | Reaction | Positive? | Repeat? | Notes |
|-------------|:--------------:|:--------:|:---------:|:-------:|-------|
| Busy street | | /5 | Y/N | Y/N | |
| Pet store | | /5 | Y/N | Y/N | |
| Vet office (happy visit) | | /5 | Y/N | Y/N | |
| Car ride | | /5 | Y/N | Y/N | |
| Elevator | | /5 | Y/N | Y/N | |
| Stairs (open/closed) | | /5 | Y/N | Y/N | |
| Park with other dogs | | /5 | Y/N | Y/N | |
| Restaurant patio | | /5 | Y/N | Y/N | |
| Friend's house | | /5 | Y/N | Y/N | |
| Parking garage | | /5 | Y/N | Y/N | |
| Body of water | | /5 | Y/N | Y/N | |

---

## Sounds

| Sound | First Exposure | Reaction | Positive? | Repeat? | Notes |
|-------|:--------------:|:--------:|:---------:|:-------:|-------|
| Vacuum cleaner | | /5 | Y/N | Y/N | |
| Doorbell | | /5 | Y/N | Y/N | |
| Thunder/fireworks | | /5 | Y/N | Y/N | |
| Sirens | | /5 | Y/N | Y/N | |
| Construction noise | | /5 | Y/N | Y/N | |
| Loud music | | /5 | Y/N | Y/N | |
| Baby crying | | /5 | Y/N | Y/N | |
| Garage door | | /5 | Y/N | Y/N | |
| Skateboard/scooter | | /5 | Y/N | Y/N | |

---

## Surfaces

| Surface | First Exposure | Reaction | Positive? | Repeat? | Notes |
|---------|:--------------:|:--------:|:---------:|:-------:|-------|
| Metal grate | | /5 | Y/N | Y/N | |
| Slippery floor | | /5 | Y/N | Y/N | |
| Gravel | | /5 | Y/N | Y/N | |
| Sand | | /5 | Y/N | Y/N | |
| Wet grass | | /5 | Y/N | Y/N | |
| Wobble board | | /5 | Y/N | Y/N | |
| Carpet vs. hard floor | | /5 | Y/N | Y/N | |

---

## Reaction Scale

| Score | Meaning |
|:-----:|---------|
| 5 | Confident, happy, engaged |
| 4 | Calm, neutral, no stress |
| 3 | Slightly uncertain but recovers quickly |
| 2 | Nervous, avoidant, whale eye, lip licking |
| 1 | Fearful, reactive, barking, cowering, snapping |

---

---

# SHEET 5: VET RECORDS

> Keep all health information in one place for quick reference.

---

## Vaccination Record

| Vaccine | Date Given | Next Due | Vet/Clinic | Lot # | Notes |
|---------|:----------:|:--------:|------------|-------|-------|
| Rabies | | | | | |
| DHPP (Distemper combo) | | | | | |
| Bordetella | | | | | |
| Leptospirosis | | | | | |
| Canine Influenza | | | | | |
| Lyme Disease | | | | | |

---

## Medications

| Medication | Dosage | Frequency | Start Date | End Date | Prescribing Vet | Purpose |
|-----------|--------|-----------|:----------:|:--------:|-----------------|---------|
| Heartworm Prevention | | Monthly | | Ongoing | | |
| Flea/Tick Prevention | | Monthly | | Ongoing | | |
| | | | | | | |

---

## Vet Visit Log

| Date | Reason | Vet/Clinic | Diagnosis | Treatment | Cost | Follow-Up Date | Notes |
|------|--------|------------|-----------|-----------|-----:|:--------------:|-------|
| | | | | | $ | | |
| | | | | | $ | | |
| | | | | | $ | | |

---

## Weight Tracker

| Date | Weight (lbs) | Change | Ideal Range | Notes |
|------|:------------:|:------:|:-----------:|-------|
| | | +/- | - lbs | |
| | | +/- | - lbs | |
| | | +/- | - lbs | |

---

---

# SHEET 6: EXERCISE LOG

> Track daily physical exercise and mental enrichment.

---

## Daily Exercise Log

| Date | Activity | Duration (min) | Intensity | Distance | Notes |
|------|----------|:--------------:|:---------:|:--------:|-------|
| | Walk | | Easy/Moderate/Vigorous | mi | |
| | Run/Jog | | Easy/Moderate/Vigorous | mi | |
| | Fetch | | Moderate/Vigorous | -- | |
| | Dog Park | | Varies | -- | |
| | Swimming | | Moderate | -- | |
| | Hike | | Moderate/Vigorous | mi | |
| | Puzzle Toy | | Mental | -- | |
| | Sniff Walk | | Easy (mental) | mi | |
| | Tug/Play | | Moderate | -- | |

---

## Weekly Exercise Summary

| Week Of | Total Walk Min | Total Play Min | Total Mental Min | Rest Days | Total Active Days | Meets Needs? |
|---------|:--------------:|:--------------:|:----------------:|:---------:|:-----------------:|:------------:|
| [date] | min | min | min | | /7 | Y/N |
| [date] | min | min | min | | /7 | Y/N |

---

## Exercise Needs Guide (by breed type)

| Energy Level | Daily Exercise Target | Mental Enrichment | Examples |
|:------------:|:---------------------:|:-----------------:|---------|
| Very High | 90-120+ min | 30+ min | Border Collie, Aussie, Vizsla |
| High | 60-90 min | 20-30 min | Lab, Golden, Husky |
| Medium | 30-60 min | 15-20 min | Beagle, Cocker Spaniel |
| Low | 20-30 min | 10-15 min | Bulldog, Basset, Shih Tzu |

---

---

# SHEET 7: BEHAVIOR INCIDENTS

> Log problem behaviors with context. Patterns reveal triggers and help your trainer (or you) solve issues.

---

## Incident Log

| Date | Time | Behavior | Trigger (what happened before) | Environment | Duration | Intensity (1-5) | Your Response | Outcome | Prevention Plan |
|------|------|----------|-------------------------------|-------------|:--------:|:---------------:|:-------------|---------|:----------------|
| | | | | | | /5 | | | |
| | | | | | | /5 | | | |
| | | | | | | /5 | | | |

---

## Behavior Types (Dropdown)
- Barking (excessive)
- Lunging/Reactivity (dogs)
- Lunging/Reactivity (people)
- Resource Guarding
- Jumping on People
- Counter Surfing
- Chewing (inappropriate)
- Separation Anxiety Signs
- Pulling on Leash
- Nipping/Mouthing
- Potty Accident
- Fear Response
- Aggression Warning
- Escape Attempts
- Other

---

## Behavior Pattern Analysis

| Behavior | Total Incidents (30 days) | Most Common Trigger | Most Common Time | Most Common Place | Trend | Priority |
|----------|:-------------------------:|--------------------:|:----------------:|:-----------------:|:-----:|:--------:|
| | | | | | Up/Down/Flat | High/Med/Low |
| | | | | | Up/Down/Flat | High/Med/Low |
| | | | | | Up/Down/Flat | High/Med/Low |

`FORMULA (Total Incidents): =COUNTIFS(Behavior, "Barking", Date, ">="&TODAY()-30)`
`FORMULA (Trend): Compare last 2 weeks vs. previous 2 weeks`

---

## Trigger Tracking Summary

| Trigger | Frequency | Behaviors It Causes | Management Strategy |
|---------|:---------:|:-------------------:|:-------------------:|
| Other dogs on leash | | Lunging, barking | Increase distance, U-turn |
| Doorbell | | Barking, jumping | Place command, management |
| Being left alone | | Whining, destructive | Gradual desensitization |
| Food/toys near other pets | | Guarding | Feed separately, trade games |

---

---

# FORMULA REFERENCE GUIDE

---

## Progress Tracking

**Overall mastery percentage:**
```
=COUNTIF(LevelColumn, 5) / COUNTA(CommandColumn) * 100
```

**Average weekly progress score:**
```
=AVERAGE(WeeklyScores)
```

**Training streak (consecutive days):**
```
=Manual count or: check if each date has at least 1 session entry
```

## Session Analysis

**Average session success rate:**
```
=AVERAGE(SuccessRateColumn)
```

**Total training minutes this month:**
```
=SUMIFS(Duration, Date, ">="&MonthStart, Date, "<="&MonthEnd)
```

**Sessions per week:**
```
=COUNTIFS(Date, ">="&WeekStart, Date, "<="&WeekEnd)
```

## Conditional Formatting

**Command at Level 5 (green):**
```
=D2 = 5
```

**Command at Level 1-2 (yellow, needs work):**
```
=D2 <= 2
```

**Behavior incident, high intensity (red):**
```
=G2 >= 4
```

**Socialization reaction below 3 (orange, needs counter-conditioning):**
```
=D2 < 3
```

**Vet appointment overdue (red):**
```
=AND(NextDueDate <> "", NextDueDate < TODAY())
```

---

> **NOTE:** This tracker uses positive reinforcement methodology. Never log punishment — it is not an effective training tool and damages the human-dog relationship. If you are struggling with serious behavioral issues (aggression, severe anxiety, resource guarding), work with a certified professional dog trainer (CPDT-KA) or veterinary behaviorist. This tracker helps you and your trainer monitor progress and identify patterns, but it is not a substitute for professional guidance when needed.
