# Language Learning Tracker — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with spaced repetition scheduling, streak tracking, and fluency milestone systems already built. Read the Quick-Start Guide at the bottom before adding your first vocabulary words.

---

## DATABASES

---

### 1. Languages

**Purpose:** Master record for each language you are studying. Tracks overall progress, goals, study streaks, and proficiency level. Serves as the hub connecting vocabulary, grammar, sessions, and milestones.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Language | Title | Language name — e.g. "Spanish" or "Japanese (JLPT N3)" |
| Native Name | Text | Name in the target language — e.g. "Espanol" |
| Flag Emoji | Text | Country flag for visual identification |
| Current Level | Select | A1 / A2 / B1 / B2 / C1 / C2 (CEFR scale) |
| Target Level | Select | A1 / A2 / B1 / B2 / C1 / C2 |
| Started Date | Date | When you began studying this language |
| Days Studying | Formula | `dateBetween(now(), prop("Started Date"), "days")` |
| Current Streak | Number | Consecutive days studied (update daily or via automation) |
| Longest Streak | Number | Personal best streak |
| Total Study Hours | Rollup | Sum of Duration from linked Study Sessions |
| Total Vocabulary | Rollup | Count of linked Vocabulary entries |
| Mastered Vocabulary | Rollup | Count of linked Vocabulary where Mastery = Mastered |
| Vocab Mastery % | Formula | `if(prop("Total Vocabulary") == 0, "0%", format(round(prop("Mastered Vocabulary") / prop("Total Vocabulary") * 100)) + "%")` |
| Grammar Units Completed | Rollup | Count of linked Grammar entries where Status = Mastered |
| Total Grammar Units | Rollup | Count of linked Grammar entries |
| Grammar Progress % | Formula | `if(prop("Total Grammar Units") == 0, "0%", format(round(prop("Grammar Units Completed") / prop("Total Grammar Units") * 100)) + "%")` |
| Weekly Goal (mins) | Number | Target study minutes per week |
| This Week Mins | Rollup | Sum of Duration from Study Sessions this week |
| Weekly Goal Progress | Formula | `if(prop("Weekly Goal (mins)") == 0, "No goal set", format(round(prop("This Week Mins") / prop("Weekly Goal (mins)") * 100)) + "%")` |
| Primary Resource | Text | Main learning tool — e.g. "Anki + Pimsleur + italki" |
| Motivation | Text | Why are you learning this language? Travel, career, heritage, etc. |
| Status | Select | Active / Paused / Completed / Abandoned |
| Linked Vocabulary | Relation | → Vocabulary database |
| Linked Grammar | Relation | → Grammar database |
| Linked Sessions | Relation | → Study Sessions database |
| Linked Milestones | Relation | → Milestones database |
| Notes | Text | General observations, strategies, resources |

**Views:**

- **All Languages** — Table, sorted by Status then Language
- **Active Languages** — Filter: Status = Active
- **Dashboard Cards** — Gallery view showing Language, Current Level, Streak, Vocab Mastery %, Weekly Goal Progress
- **Progress Overview** — Table with Language, Current Level, Total Study Hours, Total Vocabulary, Grammar Progress %

---

### 2. Vocabulary

**Purpose:** Every word and phrase you are learning, organized with spaced repetition scheduling. Each entry tracks meaning, example sentences, pronunciation, and mastery level with an automated review schedule.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Word / Phrase | Title | The target language word or phrase |
| Language | Relation | → Languages database |
| Language Name | Rollup | Name from linked Language |
| Translation | Text | English (or native language) meaning |
| Part of Speech | Select | Noun / Verb / Adjective / Adverb / Preposition / Conjunction / Pronoun / Phrase / Idiom / Expression |
| Pronunciation | Text | IPA, romanization, or phonetic guide |
| Audio | Files & Media | Upload or link pronunciation audio |
| Example Sentence | Text | Full sentence using the word in context (target language) |
| Example Translation | Text | Translation of the example sentence |
| Category | Select | Greetings / Food / Travel / Business / Family / Numbers / Colors / Weather / Emotions / Body / Home / Shopping / Time / Nature / Technology / Medical / Legal |
| Difficulty | Select | Beginner / Intermediate / Advanced |
| Source | Text | Where you encountered this word — textbook, conversation, show, etc. |
| Image | Files & Media | Visual association (great for concrete nouns) |
| Mnemonic | Text | Memory trick or association |
| Mastery | Select | New / Learning / Reviewing / Mastered / Leech |
| Times Reviewed | Number | How many times you've studied this word |
| Times Correct | Number | How many times you recalled it correctly |
| Accuracy % | Formula | `if(prop("Times Reviewed") == 0, "—", format(round(prop("Times Correct") / prop("Times Reviewed") * 100)) + "%")` |
| Last Reviewed | Date | When you last practiced this word |
| Next Review | Date | Scheduled next review (spaced repetition) |
| Review Interval (days) | Number | Current interval — increases as mastery grows |
| Days Until Review | Formula | `if(empty(prop("Next Review")), "Schedule now", if(dateBetween(prop("Next Review"), now(), "days") <= 0, "REVIEW TODAY", format(dateBetween(prop("Next Review"), now(), "days")) + " days"))` |
| Date Added | Date | When you added this word |
| Conjugation Notes | Text | For verbs — key conjugations or irregular forms |
| Related Words | Relation | → Vocabulary database (self-referential for word families) |
| Tags | Multi-select | High Frequency / Irregular / False Friend / Cognate / Slang / Formal / Written / Spoken |

**Views:**

- **All Vocabulary** — Table, sorted by Date Added descending
- **Review Today** — Filter: Next Review <= today AND Mastery != Mastered, sorted by Next Review ascending
- **New Words** — Filter: Mastery = New, sorted by Date Added descending
- **Learning** — Filter: Mastery = Learning, sorted by Accuracy % ascending (weakest first)
- **Mastered** — Filter: Mastery = Mastered
- **Leeches** — Filter: Mastery = Leech (words you keep getting wrong — need special attention)
- **By Category** — Table, grouped by Category
- **By Part of Speech** — Table, grouped by Part of Speech
- **Flashcard View** — Gallery view showing only Word/Phrase on card front (use toggle to reveal translation)
- **Low Accuracy** — Filter: Accuracy % < 60% AND Times Reviewed > 3
- **Recently Added** — Filter: Date Added is within 7 days

---

### 3. Grammar

**Purpose:** Track grammar concepts, rules, and structures from beginner to advanced. Each entry includes explanations, examples, conjugation tables, and practice exercises with a mastery progression system.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Grammar Point | Title | Name of the concept — e.g. "Past Tense (Preterite)" or "Te-form" |
| Language | Relation | → Languages database |
| Language Name | Rollup | Name from linked Language |
| Level | Select | A1 / A2 / B1 / B2 / C1 / C2 |
| Category | Select | Tenses / Conjugation / Particles / Word Order / Cases / Articles / Pronouns / Conditionals / Subjunctive / Passive / Reported Speech / Comparatives / Prepositions |
| Status | Select | Not Started / Learning / Practicing / Mastered |
| Rule Summary | Text | Brief explanation of the grammar rule |
| Detailed Explanation | Text | Full explanation with nuances and exceptions |
| Formula / Pattern | Text | The structural pattern — e.g. "Subject + haber + past participle" |
| Example 1 | Text | Example sentence with the grammar point highlighted |
| Example 1 Translation | Text | English translation |
| Example 2 | Text | Second example sentence |
| Example 2 Translation | Text | English translation |
| Example 3 | Text | Third example sentence |
| Example 3 Translation | Text | English translation |
| Common Mistakes | Text | Typical errors learners make with this point |
| Exceptions | Text | Irregular cases or exceptions to the rule |
| Practice Exercises | Text | Self-created or sourced exercises to drill this point |
| Related Grammar | Relation | → Grammar database (self-referential for connected concepts) |
| Prerequisites | Relation | → Grammar database (what you need to know first) |
| Resource Links | URL | External explanations, videos, or exercises |
| Confidence | Select | Shaky / Getting There / Solid / Automatic |
| Last Practiced | Date | When you last actively used this grammar point |
| Times Practiced | Number | How many sessions focused on this point |
| Notes | Text | Personal observations, tricks, connections to native language |
| Order | Number | Suggested learning sequence within level |
| Tags | Multi-select | Core / Advanced / Conversational / Written / Formal / Colloquial / Tricky |

**Views:**

- **All Grammar** — Table, sorted by Level then Order
- **By Level** — Table, grouped by Level
- **Learning Path** — Filter: Status = Not Started or Learning, sorted by Level then Order (what to study next)
- **Mastered** — Filter: Status = Mastered
- **Needs Practice** — Filter: Status = Practicing AND Last Practiced > 14 days ago
- **By Category** — Table, grouped by Category
- **Kanban** — Kanban grouped by Status
- **Current Level Focus** — Filter by your current CEFR level

---

### 4. Study Sessions

**Purpose:** Log every study activity — whether it's Duolingo, a textbook chapter, a conversation with a tutor, watching a show in the target language, or flashcard review. Builds your streak and tracks what methods are most effective.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | What you did — e.g. "italki lesson — conversational practice" |
| Language | Relation | → Languages database |
| Language Name | Rollup | Name from linked Language |
| Date | Date | Session date and time |
| Duration (mins) | Number | Time spent in minutes |
| Duration (hrs) | Formula | `format(round(prop("Duration (mins)") / 60 * 100) / 100) + "h"` |
| Activity Type | Select | Vocabulary Review / Grammar Study / Listening / Speaking / Reading / Writing / Conversation / Tutor Session / App (Duolingo, etc.) / Immersion (TV/Music) / Flashcards / Textbook / Podcast |
| Skill Focus | Multi-select | Listening / Speaking / Reading / Writing / Vocabulary / Grammar / Pronunciation |
| Resource Used | Text | Specific app, book, video, or tutor |
| Method | Select | Active Recall / Spaced Repetition / Shadowing / Comprehensible Input / Grammar Drill / Free Writing / Dictation / Translation / Immersion |
| New Words Learned | Number | Vocabulary items added this session |
| Words Reviewed | Number | Vocabulary items reviewed this session |
| Effectiveness | Select | Highly Effective / Effective / Neutral / Ineffective |
| Difficulty | Select | Too Easy / Just Right / Challenging / Too Hard |
| Enjoyment | Select | Loved It / Enjoyed / Neutral / Boring / Frustrating |
| Focus Level | Select | Deep Focus / Moderate / Distracted |
| Topics Covered | Text | Specific topics, chapters, or themes |
| Key Learnings | Text | Main takeaways from this session |
| Mistakes Made | Text | Errors to review later |
| Confidence After | Select | Higher / Same / Lower |
| Streak Day | Number | Which day of the current streak this was |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |
| Tags | Multi-select | Morning / Evening / Quick Session / Deep Session / With Tutor / Solo / Fun / Intensive |

**Views:**

- **All Sessions** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week
- **Today** — Filter: Date = today
- **By Activity Type** — Table, grouped by Activity Type (see where time goes)
- **By Skill Focus** — Table, grouped by Skill Focus
- **Effectiveness Review** — Filter: sorted by Effectiveness, grouped by Activity Type (find what works)
- **Calendar** — Calendar view by Date
- **Monthly Summary** — Table grouped by Month with sum of Duration
- **Streak Tracker** — Table sorted by Date descending, showing Streak Day
- **Tutor Sessions** — Filter: Activity Type = Tutor Session or Conversation

---

### 5. Milestones & Goals

**Purpose:** Track major accomplishments and set specific, measurable goals for your language learning journey. From "ordered coffee in Spanish" to "passed JLPT N3" — every win is recorded to maintain motivation and track real-world progress.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Milestone | Title | What you achieved or aim to achieve |
| Language | Relation | → Languages database |
| Language Name | Rollup | Name from linked Language |
| Type | Select | Goal / Achievement / Certification / Real-World Use / Streak / Vocabulary Count / Level Up |
| Category | Select | Speaking / Listening / Reading / Writing / Vocabulary / Grammar / Cultural / Exam / Travel / Professional |
| Status | Select | Not Started / In Progress / Achieved / Abandoned |
| Target Date | Date | When you aim to achieve this |
| Achieved Date | Date | When you actually achieved it |
| Days to Achieve | Formula | `if(empty(prop("Achieved Date")), "—", format(dateBetween(prop("Achieved Date"), prop("Started Date"), "days")) + " days")` |
| Started Date | Date | When you began working toward this |
| Progress % | Number | 0–100 manual progress tracking |
| Metric | Text | How you measure success — e.g. "500 words mastered" or "20-min conversation without English" |
| Current Value | Number | Current progress toward metric |
| Target Value | Number | Goal number for the metric |
| Auto Progress | Formula | `if(prop("Target Value") == 0, "—", format(round(prop("Current Value") / prop("Target Value") * 100)) + "%")` |
| Evidence | Text | Proof or notes about the achievement |
| Celebration | Text | How you rewarded yourself (important for motivation!) |
| Difficulty | Select | Easy / Moderate / Hard / Stretch |
| Priority | Select | Must Do / Should Do / Nice to Have |
| Related Milestone | Relation | → Milestones database (self-referential for milestone chains) |
| Notes | Text | Strategy, blockers, reflections |
| Tags | Multi-select | Monthly Goal / Quarterly Goal / Yearly Goal / Bucket List / Certification / Travel Prep |

**Views:**

- **All Milestones** — Table, sorted by Status then Target Date
- **Active Goals** — Filter: Status = In Progress, sorted by Target Date ascending
- **Achievements** — Filter: Status = Achieved, sorted by Achieved Date descending (motivation wall!)
- **By Category** — Table, grouped by Category
- **Upcoming Deadlines** — Filter: Status = In Progress AND Target Date within 30 days
- **Goal Board** — Kanban grouped by Status
- **By Language** — Table, grouped by Language Name
- **Celebration Log** — Filter: Status = Achieved AND Celebration is not empty (review your wins)

---

## SPACED REPETITION SYSTEM

> This is the core review scheduling engine. It determines when each vocabulary word should be reviewed next based on how well you recall it.

### How It Works

When you review a vocabulary word, update these fields based on recall quality:

**If you recalled correctly:**

1. Increment Times Reviewed by 1
2. Increment Times Correct by 1
3. Set Last Reviewed to today
4. Multiply Review Interval by the interval multiplier:
   - First correct: interval = 1 day
   - Second correct: interval = 3 days
   - Third correct: interval = 7 days
   - Fourth correct: interval = 14 days
   - Fifth correct: interval = 30 days
   - Sixth+ correct: interval = previous interval * 2
5. Set Next Review to today + Review Interval
6. Update Mastery:
   - 1–2 correct in a row → Learning
   - 3–4 correct → Reviewing
   - 5+ correct with interval > 21 days → Mastered

**If you recalled incorrectly:**

1. Increment Times Reviewed by 1 (do NOT increment Times Correct)
2. Set Last Reviewed to today
3. Reset Review Interval to 1 day
4. Set Next Review to tomorrow
5. If Accuracy % drops below 40% after 8+ reviews → set Mastery to Leech

### Interval Schedule Reference

| Correct Streak | Interval | Mastery Level |
|---|---|---|
| 0 (just added) | Review same day | New |
| 1 | 1 day | Learning |
| 2 | 3 days | Learning |
| 3 | 7 days | Reviewing |
| 4 | 14 days | Reviewing |
| 5 | 30 days | Mastered |
| 6 | 60 days | Mastered |
| 7+ | 120+ days | Mastered |

### Next Review Formula

```
if(
  empty(prop("Last Reviewed")),
  "Schedule now",
  if(
    dateBetween(prop("Next Review"), now(), "days") <= 0,
    "REVIEW TODAY",
    format(dateBetween(prop("Next Review"), now(), "days")) + " days"
  )
)
```

---

## STREAK TRACKING SYSTEM

### Daily Streak Rules

- Any study session of 5+ minutes counts toward the streak
- The streak resets to 0 if no session is logged for a full calendar day
- Update the Current Streak field in the Languages database daily
- If Current Streak exceeds Longest Streak, update Longest Streak

### Streak Milestones

| Days | Badge | Reward Suggestion |
|---|---|---|
| 7 | Week Warrior | New song in target language |
| 14 | Two-Week Titan | Movie night in target language |
| 30 | Monthly Master | New resource purchase |
| 60 | Sixty Slayer | Treat yourself |
| 90 | Quarter Champion | Book a tutor session |
| 180 | Half-Year Hero | Plan a trip |
| 365 | Year Legend | Major celebration |

---

## AUTOMATIONS / FORMULAS

### Vocabulary Accuracy

Tracks long-term recall accuracy per word.

```
if(
  prop("Times Reviewed") == 0,
  "—",
  format(round(prop("Times Correct") / prop("Times Reviewed") * 100)) + "%"
)
```

### Weekly Goal Progress

Shows percentage of weekly study goal completed.

```
if(
  prop("Weekly Goal (mins)") == 0,
  "No goal set",
  format(round(prop("This Week Mins") / prop("Weekly Goal (mins)") * 100)) + "%"
)
```

### Vocabulary Mastery Percentage

Overall mastery rate across all vocabulary for a language.

```
if(
  prop("Total Vocabulary") == 0,
  "0%",
  format(round(prop("Mastered Vocabulary") / prop("Total Vocabulary") * 100)) + "%"
)
```

### Grammar Progress

Percentage of grammar points mastered.

```
if(
  prop("Total Grammar Units") == 0,
  "0%",
  format(round(prop("Grammar Units Completed") / prop("Total Grammar Units") * 100)) + "%"
)
```

### Milestone Auto-Progress

Calculates progress toward a numeric goal automatically.

```
if(
  prop("Target Value") == 0,
  "—",
  format(round(prop("Current Value") / prop("Target Value") * 100)) + "%"
)
```

### Days Studying

Total days since you started learning a language.

```
dateBetween(now(), prop("Started Date"), "days")
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Language(s)

- Open the **Languages** database and create an entry for each language you are studying
- Set your Current Level honestly (use online CEFR tests if unsure)
- Set a Target Level and Weekly Goal (start modest — 60–90 mins/week is sustainable)
- Write your Motivation — reviewing this on low-energy days helps

### Step 2 — Seed Your Vocabulary

- Open the **Vocabulary** database and add 20–50 words you already know
- Set these to Mastery = Reviewing or Mastered (they form your foundation)
- Add 10–20 new words you want to learn and set Mastery = New
- For each word, include at least a Translation and Example Sentence
- Set the Next Review date for new words to today

### Step 3 — Map Your Grammar

- Open the **Grammar** database and add the grammar points for your current level
- Use your textbook's table of contents or a CEFR grammar checklist as a guide
- Mark concepts you already know as Mastered
- Set the rest as Not Started and arrange by Order (learning sequence)

### Step 4 — Start Logging Sessions

- Every time you study (even 5 minutes), log it in **Study Sessions**
- Link to the Language, set Activity Type, Duration, and Skill Focus
- After the session, rate Effectiveness and note Key Learnings
- This builds your streak and shows which activities produce the best results

### Step 5 — Set Your First Milestones

- Open **Milestones** and create 3–5 goals:
  - One short-term (achievable within 2 weeks)
  - One medium-term (1–3 months)
  - One ambitious stretch goal (6–12 months)
- Make each goal specific and measurable — "Learn 500 words" not "Get better at vocabulary"

### Step 6 — Daily Review Routine

**Every day (10–20 minutes minimum):**

1. Open the "Review Today" view in Vocabulary
2. Go through each word — test yourself before revealing the translation
3. Update Times Reviewed, Times Correct, Last Reviewed, and Next Review based on the spaced repetition rules
4. Update Mastery level if thresholds are crossed
5. Log the session in Study Sessions
6. Update your streak

**Every week (15 minutes):**

- Review your Weekly Goal Progress
- Check Grammar points that "Need Practice"
- Add new vocabulary from the week's exposure (reading, conversations, media)
- Update Milestone progress

**Every month:**

- Review your Milestones — celebrate achievements, adjust deadlines if needed
- Check Vocabulary Accuracy across all words — target >80%
- Review "Leeches" and decide whether to reform the mnemonic or drop the word
- Consider leveling up (update Current Level) if Grammar and Vocabulary mastery justify it

### Pro Tips

- Add words you encounter in real life (signs, menus, conversations) — they stick better than textbook words
- Use the Mnemonic field generously — bizarre visual associations dramatically improve recall
- Track which Activity Types have the highest Effectiveness rating and do more of those
- The Leech system is your friend — words stuck at low accuracy need a different approach (new mnemonic, more context, audio practice)
- Set your review interval conservatively at first; it's better to over-review than to forget
- Use the "By Category" vocabulary view before specific situations (e.g., review "Food" words before dining abroad)
- Log immersion activities (watching TV, listening to podcasts) as study sessions — they count and they build passive skills
- When your streak breaks, don't spiral — just start a new one. The Longest Streak field preserves your record
- Grammar is best learned through examples, not rules — fill in all three example fields for each grammar point
