# Mental Health Check-In Journal — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with mood tracking, CBT thought records, gratitude prompts, therapist session management, and crisis planning already configured. Read the Quick-Start Guide at the bottom. This is a personal wellness tool, not a replacement for professional mental health care.

---

## DATABASES

---

### 1. Daily Check-Ins

**Purpose:** Your daily mental health pulse check. A structured space to record mood, energy, triggers, and reflections every day. Over time, this builds a powerful dataset that reveals patterns in your mental health — what helps, what hurts, and what you can control. Share trends with your therapist for deeper insight.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Date | Title | Today's date — e.g. "Tuesday, May 6, 2026" |
| Day of Week | Formula | Extracted from date for pattern analysis |
| Mood (Morning) | Select | Great / Good / Okay / Low / Bad / Very Bad |
| Mood (Afternoon) | Select | Great / Good / Low / Bad / Very Bad |
| Mood (Evening) | Select | Great / Good / Okay / Low / Bad / Very Bad |
| Overall Mood | Select | Excellent / Good / Neutral / Low / Bad / Crisis |
| Mood Score | Number | 1–10 numeric rating (1 = worst, 10 = best) |
| Energy Level | Select | High / Moderate / Low / Exhausted / Wired |
| Anxiety Level | Select | None / Mild / Moderate / Severe / Panic |
| Stress Level | Select | Minimal / Manageable / High / Overwhelming / Burnout |
| Sleep Hours | Number | Hours slept last night |
| Sleep Quality | Select | Restful / Adequate / Poor / Insomnia / Nightmares |
| Woke Up Feeling | Select | Refreshed / Groggy / Anxious / Dread / Neutral |
| Exercise | Checkbox | Did you move your body today? |
| Exercise Type | Text | What you did — walk, yoga, gym, etc. |
| Exercise Duration (mins) | Number | How long |
| Time Outdoors (mins) | Number | Time spent outside |
| Meals Eaten | Select | 3 Meals / 2 Meals / 1 Meal / Snacking Only / Skipped / Overate |
| Water Intake | Select | Plenty / Adequate / Not Enough / Barely Any |
| Medication Taken | Checkbox | Did you take prescribed medication? |
| Medication Notes | Text | Any changes, missed doses, side effects |
| Substances | Multi-select | None / Caffeine (excess) / Alcohol / Cannabis / Nicotine / Sugar Binge / Other |
| Social Interaction | Select | Fulfilling / Adequate / Isolated / Overwhelming / Conflict |
| Social Context | Text | Who you spent time with or why you were alone |
| Highlights | Text | Best moment(s) of the day — even small wins |
| Challenges | Text | What was hard today — be specific |
| Triggers | Text | What set off negative emotions — situations, people, thoughts |
| Coping Strategies Used | Multi-select | Deep Breathing / Meditation / Exercise / Journaling / Therapy Homework / Grounding / Distraction / Social Support / Nature / Music / Art / Rest / Boundary Setting / Positive Self-Talk / None |
| Coping Effectiveness | Select | Very Helpful / Somewhat Helpful / Neutral / Didn't Help / Made Worse |
| Intrusive Thoughts | Checkbox | Were intrusive or obsessive thoughts present? |
| Self-Harm Urges | Checkbox | Were self-harm urges present? (triggers crisis check) |
| Suicidal Thoughts | Checkbox | Were suicidal thoughts present? (triggers crisis check) |
| Gratitude 1 | Text | Something you're grateful for today |
| Gratitude 2 | Text | A second thing |
| Gratitude 3 | Text | A third thing |
| Tomorrow's Intention | Text | One thing you intend to do for your wellbeing tomorrow |
| Win Today | Text | One thing you did well today — celebrate it |
| Therapist Would Say | Text | What would your therapist say about today? (builds internal voice) |
| Journal Entry | Text | Free-form journaling — say whatever needs to be said |
| Weather | Select | Sunny / Cloudy / Rainy / Cold / Hot / Stormy (correlate with mood) |
| Menstrual Cycle Day | Number | For tracking hormonal mood patterns (if applicable) |
| Tags | Multi-select | Good Day / Hard Day / Breakthrough / Setback / Normal / Therapy Day / Trigger Day / Self-Care Day / Social Day / Alone Day |
| Linked Thought Records | Relation | → CBT Thought Records database |
| Linked Therapist Notes | Relation | → Therapist Sessions database |

**Views:**

- **All Check-Ins** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week
- **This Month** — Filter: Date is this month
- **Calendar** — Calendar view (visual overview of mood)
- **Low Days** — Filter: Overall Mood = Low or Bad or Crisis (identify patterns)
- **Good Days** — Filter: Overall Mood = Excellent or Good (what made them good?)
- **Mood Trend** — Table showing Date, Mood Score, Sleep Hours, Exercise, Anxiety Level (for charting)
- **Trigger Analysis** — Filter: Triggers is not empty, sorted by Date (show to therapist)
- **Gratitude Scroll** — Table showing only Gratitude 1, 2, 3 (read when you need a boost)
- **Crisis Days** — Filter: Suicidal Thoughts = true OR Self-Harm Urges = true (share with therapist)
- **Exercise Impact** — Table showing Date, Exercise (bool), Mood Score (correlate movement with mood)
- **Sleep Impact** — Table showing Date, Sleep Hours, Sleep Quality, Mood Score
- **Weekly Summary** — Grouped by week with average Mood Score

---

### 2. CBT Thought Records

**Purpose:** Structured Cognitive Behavioral Therapy thought records for challenging and reframing negative automatic thoughts. This is one of the most evidence-based tools for managing anxiety, depression, and distorted thinking. Your therapist may assign these between sessions.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Situation | Title | Brief description of what happened — e.g. "Boss didn't reply to my email for 3 hours" |
| Date & Time | Date | When this occurred |
| Linked Check-In | Relation | → Daily Check-Ins database |
| Trigger Type | Select | Work / Relationship / Social / Health / Financial / Self-Image / Family / Future / Past / Existential / Other |
| Emotions Felt | Multi-select | Anxious / Sad / Angry / Guilty / Ashamed / Hopeless / Worthless / Fearful / Frustrated / Jealous / Lonely / Overwhelmed / Numb / Panicked |
| Emotion Intensity (Before) | Number | 1–10 scale (10 = most intense) |
| Physical Sensations | Text | What you felt in your body — tight chest, racing heart, nausea, etc. |
| Automatic Thought | Text | The exact thought that popped into your head — e.g. "She's going to fire me" |
| Thought Believability (Before) | Number | 0–100% how much you believed the thought initially |
| Cognitive Distortion | Multi-select | All-or-Nothing / Catastrophizing / Mind Reading / Fortune Telling / Emotional Reasoning / Should Statements / Labeling / Personalization / Overgeneralization / Mental Filter / Discounting Positives / Magnification / Jumping to Conclusions |
| Evidence FOR the Thought | Text | What evidence supports this thought being true? |
| Evidence AGAINST the Thought | Text | What evidence contradicts this thought? |
| Alternative Thought | Text | A more balanced, realistic way to think about this situation |
| Thought Believability (After) | Number | 0–100% how much you believe the original thought now |
| Emotion Intensity (After) | Number | 1–10 scale after completing the record |
| Reduction | Formula | `format(prop("Emotion Intensity (Before)") - prop("Emotion Intensity (After)"))` |
| Behavioral Experiment | Text | Optional: what could you do to test if the thought is true? |
| Experiment Result | Text | What happened when you tested it? |
| What I Learned | Text | Insight gained from this exercise |
| Compassionate Response | Text | What would you say to a friend in this situation? |
| Therapist Notes | Text | Notes from discussing this record in therapy |
| Pattern | Text | Is this a recurring thought pattern? When does it usually appear? |
| Core Belief Touched | Text | What deeper belief does this thought stem from? |
| Effectiveness | Select | Very Helpful / Helpful / Neutral / Didn't Help |
| Tags | Multi-select | Recurring / New Pattern / Breakthrough / Therapy Homework / Crisis / Work / Relationship / Self-Worth / Anxiety / Depression |
| Notes | Text | Additional reflections |

**Views:**

- **All Thought Records** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week
- **By Distortion Type** — Table, grouped by Cognitive Distortion (identify your most common patterns)
- **By Trigger Type** — Table, grouped by Trigger Type
- **High Intensity** — Filter: Emotion Intensity (Before) >= 7
- **Most Effective** — Filter: Effectiveness = Very Helpful (review these when struggling)
- **Recurring Patterns** — Filter: Tags contains Recurring (bring these to therapy)
- **Breakthroughs** — Filter: Tags contains Breakthrough
- **Reduction Analysis** — Table showing Date, Situation, Intensity Before, Intensity After, Reduction (is this technique working?)
- **By Core Belief** — Table, grouped by Core Belief Touched (deep pattern work)
- **Therapy Homework** — Filter: Tags contains Therapy Homework

---

### 3. Therapist Sessions

**Purpose:** Track every therapy session with pre-session prep, session notes, homework assigned, and progress tracking. Ensures continuity between sessions, helps you arrive prepared, and maintains a record of your therapeutic journey over time.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | e.g. "Session #14 — Boundary setting with family" |
| Session Number | Number | Running count of sessions |
| Date | Date | Session date and time |
| Therapist | Text | Therapist name |
| Type | Select | Individual / Couples / Family / Group / EMDR / CBT / DBT / Intake / Crisis / Medication Check / Psychiatric |
| Format | Select | In-Person / Video / Phone |
| Duration (mins) | Number | Session length |
| Status | Select | Scheduled / Completed / Cancelled / No Show / Rescheduled |
| Cost | Number (USD) | Session cost |
| Insurance Covered | Number (USD) | Amount covered by insurance |
| Out of Pocket | Formula | `prop("Cost") - prop("Insurance Covered")` |
| Pre-Session Prep | Text | What you want to discuss — write BEFORE the session |
| Topics Discussed | Text | What you actually talked about |
| Key Insights | Text | The most important things that emerged |
| Aha Moments | Text | Breakthrough realizations or new perspectives |
| Emotions During Session | Multi-select | Relieved / Sad / Anxious / Angry / Hopeful / Vulnerable / Defensive / Confused / Empowered / Numb / Tearful |
| Homework Assigned | Text | Specific tasks or exercises to do before next session |
| Homework Completed | Checkbox | Did you complete the homework? |
| Progress Noted | Text | What progress your therapist or you noticed |
| Stuck Points | Text | Where you feel stuck or resistant |
| Coping Skills Discussed | Text | New or reviewed coping strategies |
| Next Session Focus | Text | What to tackle next time |
| Next Session Date | Date | When your next appointment is |
| Session Rating | Select | Very Productive / Productive / Okay / Unproductive / Difficult but Important / Avoided the Hard Stuff |
| Energy After | Select | Lighter / Neutral / Heavy / Drained / Energized |
| Medication Changes | Text | Any prescription changes discussed or made |
| Linked Thought Records | Relation | → CBT Thought Records database |
| Linked Check-Ins | Relation | → Daily Check-Ins database |
| Diagnoses | Multi-select | GAD / MDD / PTSD / ADHD / OCD / Bipolar / BPD / Social Anxiety / Panic Disorder / Adjustment / Grief / Other |
| Treatment Goals | Text | Current goals you're working toward in therapy |
| Goal Progress | Select | Significant Progress / Some Progress / Maintaining / Stalled / Regressing |
| Tags | Multi-select | Breakthrough / Hard Session / Homework Given / Medication / Crisis / Maintenance / Check-In / Deep Work |
| Notes | Text | Private session notes — only for you |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **Upcoming** — Filter: Status = Scheduled, sorted by Date ascending
- **Completed** — Filter: Status = Completed
- **Session History** — Table showing Session Number, Date, Topics Discussed, Key Insights
- **Homework Tracker** — Filter: Homework Assigned is not empty, showing Homework Assigned, Homework Completed
- **Incomplete Homework** — Filter: Homework Completed = false AND Status = Completed (do before next session!)
- **Breakthroughs** — Filter: Tags contains Breakthrough
- **Progress Timeline** — Table showing Date, Progress Noted, Goal Progress
- **Cost Tracker** — Table showing Date, Cost, Insurance Covered, Out of Pocket
- **By Topic** — Search through Topics Discussed (what have you worked on?)
- **Prep for Next Session** — Filter: Status = Scheduled (open before your appointment)

---

### 4. Coping Strategies & Self-Care

**Purpose:** Personal library of coping strategies, self-care activities, and wellness practices that work for YOU. Rate effectiveness, track when you use them, and build a personalized toolkit for different emotional states. When you're in crisis or struggling, this database tells you exactly what to do.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Strategy Name | Title | The coping skill or self-care practice |
| Category | Select | Grounding / Breathing / Physical / Social / Creative / Cognitive / Sensory / Spiritual / Rest / Distraction / Processing / Professional Help |
| Best For | Multi-select | Anxiety / Depression / Anger / Panic / Insomnia / Overwhelm / Loneliness / Grief / Intrusive Thoughts / Low Energy / Self-Harm Urges / Dissociation / Rumination |
| Time Required | Select | 1 Minute / 5 Minutes / 15 Minutes / 30 Minutes / 1 Hour / Half Day / Ongoing |
| Energy Required | Select | No Energy (can do from bed) / Low / Moderate / High |
| Location | Select | Anywhere / Home Only / Outside / With Others / Alone |
| Instructions | Text | Step-by-step how to do this practice |
| Why It Works | Text | The science or logic behind this strategy |
| My Experience | Text | Personal notes on how this works for you specifically |
| Effectiveness Rating | Select | Life Saver / Very Effective / Effective / Sometimes Helps / Rarely Helps / Doesn't Work |
| Times Used | Number | How often you've used this |
| Last Used | Date | Most recent use |
| Learned From | Text | Where you learned this — therapist, book, app, etc. |
| Tools Needed | Text | Any materials required — journal, ice, essential oils, etc. |
| Contraindications | Text | When NOT to use this strategy |
| Pairs Well With | Relation | → Coping Strategies (self-referential for combinations) |
| Status | Select | Active / Tried and Failed / Want to Try / Retired |
| Tags | Multi-select | Quick / Deep / Physical / Mental / Emotional / Nighttime / Morning / Emergency / Preventive / Maintenance |
| Notes | Text | Additional observations and tips |

**Views:**

- **All Strategies** — Table, sorted by Category then Strategy Name
- **By Category** — Table, grouped by Category
- **For Anxiety** — Filter: Best For contains Anxiety, sorted by Effectiveness Rating
- **For Depression** — Filter: Best For contains Depression, sorted by Effectiveness Rating
- **For Panic** — Filter: Best For contains Panic (quick access during panic attacks)
- **No Energy Required** — Filter: Energy Required = No Energy (for worst days)
- **Quick (< 5 min)** — Filter: Time Required = 1 Minute or 5 Minutes
- **Most Effective** — Filter: Effectiveness Rating = Life Saver or Very Effective
- **Emergency Kit** — Filter: Tags contains Emergency (crisis go-to list)
- **Want to Try** — Filter: Status = Want to Try
- **By Effectiveness** — Table, grouped by Effectiveness Rating

---

### 5. Crisis Plan

**Purpose:** Your personalized safety plan for mental health crises. Pre-written when you're stable so it's accessible when you're not. Contains warning signs, escalation steps, emergency contacts, and specific actions for different crisis levels. Share this with trusted people.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Plan Element | Title | Component name — e.g. "Warning Signs" or "Level 3 Actions" |
| Section | Select | Warning Signs / Triggers / Internal Coping / People to Contact / Professional Help / Environment Safety / Reasons to Live / Crisis Level 1 / Crisis Level 2 / Crisis Level 3 / Post-Crisis |
| Order | Number | Display order within the plan |
| Content | Text | The actual plan content — detailed and specific |
| Contact Name | Text | For people sections — who to call |
| Contact Phone | Phone | Their phone number |
| Contact Relationship | Text | How they relate to you |
| Contact Availability | Text | When they're typically available |
| Location/Resource | Text | Address or link to crisis resource |
| Last Reviewed | Date | When you last reviewed and updated this section |
| Needs Update | Checkbox | Flag sections that need refreshing |
| Shared With | Text | Who has a copy of this plan |
| Notes | Text | Additional context |

**Views:**

- **Full Plan (Ordered)** — Table, sorted by Section then Order (the complete crisis plan)
- **Warning Signs** — Filter: Section = Warning Signs
- **People to Contact** — Filter: Section = People to Contact (quick phone list)
- **By Crisis Level** — Table, grouped by Section (escalating response)
- **Needs Update** — Filter: Needs Update = true or Last Reviewed > 90 days
- **Reasons to Live** — Filter: Section = Reasons to Live (read this when you need it most)

---

## CRISIS PLAN TEMPLATE

> Fill this in while you're in a stable state. Review every 90 days. Share with therapist, trusted friend, or family member.

### Warning Signs (How I Know I'm Declining)

Early signs that things are getting worse:

- Changes in sleep (more or less than usual)
- Withdrawing from friends and activities
- Increased irritability or emotional numbness
- Neglecting hygiene or responsibilities
- Increased substance use
- Recurring negative thought patterns
- [Add your personal warning signs]

### My Personal Triggers

Situations or events that typically worsen my mental health:

- [Specific trigger 1]
- [Specific trigger 2]
- [Specific trigger 3]
- [Specific trigger 4]

### Crisis Levels & Response Plan

**Level 1 — Feeling Low / Struggling (can manage independently)**

- Use coping strategies from my toolkit
- Complete a CBT Thought Record
- Reach out to a friend for connection
- Exercise, get outside, maintain routine
- Journal about what's happening

**Level 2 — Escalating / Distressing (need support)**

- Contact my therapist (between-session message)
- Call a trusted friend or family member: [Name] — [Phone]
- Use grounding techniques (5-4-3-2-1, ice, cold water)
- Remove myself from triggering environment
- Do NOT make major decisions

**Level 3 — Crisis / Unsafe (immediate help needed)**

- 988 Suicide & Crisis Lifeline: call or text 988
- Crisis Text Line: Text HOME to 741741
- Emergency contact: [Name] — [Phone]
- Go to nearest emergency room: [Hospital name and address]
- Remove access to means of self-harm
- Do NOT be alone

### Reasons to Live (Write These When You're Well)

1. [Person who needs you]
2. [Experience you want to have]
3. [Goal you're working toward]
4. [Memory that brings peace]
5. [Thing that makes life worth living]
6. [What you'd miss]
7. [Who would miss you]
8. [Something you're looking forward to]

### Post-Crisis Protocol

After a crisis episode:

- Contact therapist to debrief
- Log the experience in Daily Check-In
- Complete a Thought Record about what happened
- Review what coping strategies worked and which didn't
- Update this crisis plan if needed
- Be gentle with yourself — recovery is not linear

---

## GRATITUDE PROMPTS

> Use these when you're stuck on what to write in the Gratitude fields. Rotate through them to avoid repetitive entries.

### Prompt Categories

**Simple Present Moment:**

- What's something comfortable in your environment right now?
- What's one thing your body did well today?
- What technology made your life easier today?

**People:**

- Who made you feel seen or heard recently?
- Who do you take for granted that you shouldn't?
- Whose absence would you feel deeply?

**Growth:**

- What can you do today that you couldn't a year ago?
- What mistake taught you something valuable?
- What boundary are you grateful you set?

**Basics:**

- What basic need was easily met today (food, shelter, safety)?
- What about your health are you grateful for?
- What freedom do you have that others don't?

**Unexpected:**

- What inconvenience turned out well?
- What "no" led to a better "yes"?
- What challenge are you stronger for having faced?

---

## AUTOMATIONS / FORMULAS

### Mood Score Trend

Track daily mood scores over time (use in chart/graph views).

```
Average of prop("Mood Score") across the last 7 daily check-ins
```

### Thought Record Reduction

Shows how much emotional intensity decreased after the exercise.

```
format(prop("Emotion Intensity (Before)") - prop("Emotion Intensity (After)"))
```

### Session Cost After Insurance

Net therapy cost per session.

```
prop("Cost") - prop("Insurance Covered")
```

### Homework Overdue

Flags incomplete therapy homework before next session.

```
if(
  and(
    not(prop("Homework Completed")),
    not(empty(prop("Homework Assigned"))),
    prop("Status") == "Completed"
  ),
  true,
  false
)
```

### Sleep/Mood Correlation

Track in views by showing Sleep Hours and Mood Score side by side — patterns typically emerge within 2–3 weeks.

### Exercise/Mood Correlation

Compare days with Exercise = true vs. false against average Mood Score. Research shows 20+ minutes of movement correlates with mood improvement for most people.

### Crisis Indicator

Flags daily check-ins where crisis-level fields are checked.

```
if(
  or(prop("Suicidal Thoughts"), prop("Self-Harm Urges")),
  "CRISIS — USE SAFETY PLAN",
  if(
    prop("Overall Mood") == "Crisis",
    "Reach out for support",
    "—"
  )
)
```

---

## QUICK-START GUIDE

### Step 1 — Set Up Your Crisis Plan First

- Open the **Crisis Plan** database and fill in every section while you're in a stable state
- Add emergency contacts with real phone numbers
- Write your personal Warning Signs and Triggers
- Write your Reasons to Live (this is powerful)
- Share this plan with your therapist and one trusted person
- Review every 90 days and update as needed

### Step 2 — Build Your Coping Strategy Toolkit

- Open **Coping Strategies & Self-Care** and add strategies you already know work
- Add at least 3 strategies for each category: Quick (< 5 min), Moderate (15–30 min), and Deep (1 hr+)
- Include at least 2–3 "No Energy Required" options for your hardest days
- Rate each one's effectiveness honestly — this is your personalized mental health toolkit
- Ask your therapist to suggest strategies to add

### Step 3 — Start Daily Check-Ins

- Open **Daily Check-Ins** and create today's entry
- You don't have to fill every field — Mood Score, Energy Level, Highlights, and Gratitude are enough to start
- The goal is consistency, not perfection. A 2-minute check-in every day beats a 20-minute one you do once a week
- Set a daily reminder — same time each day builds the habit

### Step 4 — Learn CBT Thought Records

- Open **CBT Thought Records** when you notice a strong negative emotion
- Start with the Automatic Thought — what exact words popped into your head?
- Identify the Cognitive Distortion (the list is pre-loaded for reference)
- Challenge the thought with Evidence For and Evidence Against
- Write an Alternative Thought that's more balanced and realistic
- Rate your emotion intensity before and after — watch it decrease

### Step 5 — Log Your Therapy Sessions

- After each therapy session, create an entry in **Therapist Sessions**
- Fill in Topics Discussed, Key Insights, and Homework Assigned
- BEFORE your next session, open the upcoming session entry and write Pre-Session Prep
- Arriving with a written agenda makes therapy significantly more productive

### Step 6 — Establish Your Wellness Rhythms

**Every morning (2 minutes):**

- Open today's Daily Check-In
- Rate your morning mood and note how you woke up feeling
- Set one intention for the day

**Every evening (5 minutes):**

- Complete the rest of today's check-in: Overall Mood, Energy, Challenges, Gratitude
- If you noticed a strong negative thought today, decide if it warrants a Thought Record
- Note what coping strategies you used and how effective they were
- Write tomorrow's intention

**When triggered or distressed:**

- Open your Coping Strategies database — filter by what you're feeling
- If the emotion is strong, do a CBT Thought Record
- If you're in crisis, open your Crisis Plan immediately
- Log what happened in your daily check-in later (when you're stable)

**Before each therapy session (10 minutes):**

- Review the past week's Daily Check-Ins — what themes emerged?
- Review any Thought Records from the week
- Write your Pre-Session Prep: what do you most need to discuss?
- Check if you completed last session's homework

**Monthly (15 minutes):**

- Review your Mood Score trend — improving, stable, or declining?
- Identify your top 3 triggers from the month
- Note which coping strategies you used most and their effectiveness
- Celebrate progress — what's better now than 30 days ago?
- Update your Crisis Plan if anything has changed
- Review your Reasons to Live — add new ones, affirm existing ones

### Pro Tips

- Consistency matters more than detail. A daily "Mood: 6, Sleep: 7hrs, Grateful for coffee" is more valuable than an occasional 20-minute essay
- The Gratitude fields are not about toxic positivity — on your worst days, "I'm grateful I survived today" is a valid and powerful entry
- CBT Thought Records are most effective when done in the moment (or as close to it as possible). The emotion needs to still be present for the exercise to work
- Share your mood trend data with your therapist — they see you for 1 hour/week, but your daily data shows the full picture
- The "Therapist Would Say" field builds your internal therapeutic voice. Over time, you'll internalize your therapist's perspective
- Track Sleep Hours and Exercise against Mood Score for 30 days — most people discover strong correlations they can act on
- If you notice the same Cognitive Distortion appearing repeatedly in Thought Records, bring that to your therapist — it likely connects to a core belief
- The Crisis Plan is not morbid — it's responsible preparation. Having it means you've thought clearly about what to do when you can't think clearly
- Don't judge your entries. There's no "right" way to feel. The check-in is observation, not evaluation
- If Daily Check-Ins feel overwhelming, start with just Mood Score and one Gratitude item. You can expand later when the habit is established
- Bad days are data, not failure. A string of low mood scores is valuable information, not evidence that you're broken. It means something needs attention — bring it to your therapist
