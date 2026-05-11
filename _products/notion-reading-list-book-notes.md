# Reading List & Book Notes System — Notion Template

> Duplicate this page into your Notion workspace to get started. All three databases are pre-linked with reading pace formulas, review scheduling, and status workflows built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Books

**Purpose:** Master library of every book — to-read, currently reading, and completed. Tracks status, ratings, dates, genres, and connects to your reading sessions and notes for each title.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Title | Title | Full book title |
| Author | Text | Author name(s) |
| Cover | Files & media | Upload cover image for gallery view |
| Status | Select | Want to Read / Up Next / Currently Reading / Completed / Abandoned / Re-reading |
| Rating | Select | 5 Stars / 4 Stars / 3 Stars / 2 Stars / 1 Star / Unrated |
| Genre | Multi-select | Fiction / Non-fiction / Business / Self-help / Science / Philosophy / Psychology / Biography / History / Fantasy / Sci-fi / Memoir / Health / Finance / Creativity / Technology / Spirituality |
| Format | Select | Physical / Kindle / Audiobook / PDF / Library |
| Pages | Number | Total page count |
| Current Page | Number | Where you are now (for Currently Reading) |
| Reading Progress | Formula | `if(prop("Pages") == 0, 0, round(prop("Current Page") / prop("Pages") * 100))` |
| Progress Display | Formula | `format(prop("Reading Progress")) + "% (" + format(prop("Current Page")) + "/" + format(prop("Pages")) + ")"` |
| Start Date | Date | When you started reading |
| Finish Date | Date | When you completed it |
| Days to Read | Formula | `if(and(not(empty(prop("Start Date"))), not(empty(prop("Finish Date")))), dateBetween(prop("Finish Date"), prop("Start Date"), "days"), if(and(not(empty(prop("Start Date"))), prop("Status") == "Currently Reading"), dateBetween(now(), prop("Start Date"), "days"), 0))` |
| Pages Per Day | Formula | `if(prop("Days to Read") == 0, 0, round(prop("Pages") / max(prop("Days to Read"), 1)))` |
| Estimated Days Left | Formula | `if(or(prop("Pages Per Day") == 0, prop("Status") != "Currently Reading"), 0, round((prop("Pages") - prop("Current Page")) / prop("Pages Per Day")))` |
| Estimated Finish | Formula | `if(prop("Estimated Days Left") == 0, "N/A", format(prop("Estimated Days Left")) + " days at current pace")` |
| Year Read | Formula | `if(empty(prop("Finish Date")), "", formatDate(prop("Finish Date"), "YYYY"))` |
| Month Read | Formula | `if(empty(prop("Finish Date")), "", formatDate(prop("Finish Date"), "MMMM YYYY"))` |
| Source | Select | Recommendation / Goodreads / Podcast / Newsletter / Bookstore / Library / Gift / Course / Social Media |
| Recommended By | Text | Who recommended this (for future reference) |
| Priority | Select | Must Read / High / Medium / Low / Someday |
| One-Line Summary | Text | Your one-sentence summary of what this book is about |
| Key Takeaway | Text | The single most important thing you got from this book |
| Would Recommend | Checkbox | Would you recommend this to someone else? |
| Recommend To | Text | Who specifically would benefit from this book? |
| Tags | Multi-select | Favorite / Re-read / Book Club / Quick Read / Dense / Practical / Inspiring / Mind-Changing / Reference / Career / Gifted |
| Linked Sessions | Relation | -> Reading Sessions database |
| Linked Notes | Relation | -> Key Takeaways & Quotes database |
| Session Count | Rollup | Count of Linked Sessions |
| Total Reading Time | Rollup | Sum of Duration from Linked Sessions |
| Quote Count | Rollup | Count of Linked Notes where Type = Quote |
| Review Date | Date | When to revisit notes from this book |
| Review Done | Checkbox | Reviewed on schedule |
| Notes | Text | General thoughts, why you chose this book, context |

**Views:**

- **Currently Reading** — Filter: Status = Currently Reading, showing Progress Display
- **Library** — Gallery view with Cover, sorted by Author (all completed books)
- **To Read** — Filter: Status = Want to Read OR Up Next, sorted by Priority
- **Completed** — Filter: Status = Completed, sorted by Finish Date descending
- **By Genre** — Table, grouped by Genre
- **This Year** — Filter: Year Read = current year, sorted by Finish Date
- **5-Star Books** — Filter: Rating = 5 Stars
- **Favorites** — Filter: Tags contains Favorite
- **By Author** — Table, grouped by Author, sorted by Rating descending
- **Abandoned** — Filter: Status = Abandoned (for reflection)
- **Review Queue** — Filter: Review Date <= today AND Review Done = false
- **Reading Challenge** — Filter: Year Read = current year, count visible

---

### 2. Reading Sessions

**Purpose:** Logs individual reading sessions with page progress and time spent. Feeds reading pace calculations and helps you understand your reading patterns — when you read best, how long your sessions are, and your actual throughput.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Title | Title | Auto: "[Book Title] — [Date]" |
| Book | Relation | -> Books database |
| Book Title | Rollup | Title from Book relation |
| Date | Date | When this session happened |
| Start Page | Number | Page where you began this session |
| End Page | Number | Page where you stopped |
| Pages Read | Formula | `prop("End Page") - prop("Start Page")` |
| Duration (min) | Number | How long you read in minutes |
| Pages Per Hour | Formula | `if(prop("Duration (min)") == 0, 0, round(prop("Pages Read") / (prop("Duration (min)") / 60)))` |
| Time of Day | Select | Early Morning / Morning / Afternoon / Evening / Night |
| Location | Select | Home / Cafe / Commute / Bed / Park / Library / Travel / Other |
| Focus Quality | Select | Deep / Good / Distracted / Skimming |
| Format Used | Select | Physical / Kindle / Audiobook / PDF |
| Notes | Text | Quick reactions, thoughts during reading |
| Highlights Captured | Checkbox | Did you capture highlights/quotes from this session? |
| Week | Formula | `formatDate(prop("Date"), "W")` |
| Month | Formula | `formatDate(prop("Date"), "MMMM YYYY")` |

**Views:**

- **Recent Sessions** — Table, sorted by Date descending
- **This Week** — Filter: Date is this week
- **By Book** — Table, grouped by Book Title
- **Calendar** — Calendar view by Date
- **Best Sessions** — Filter: Focus Quality = Deep, sorted by Pages Read descending
- **By Time of Day** — Table, grouped by Time of Day (find your optimal reading time)
- **Monthly Log** — Table, grouped by Month, showing total Pages Read per month

---

### 3. Key Takeaways & Quotes

**Purpose:** Captures the most valuable content from your reading — key insights, memorable quotes, action items, and chapter summaries. This is what you actually review later. Connected to books so you can pull up all notes for any title instantly.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Content | Title | The quote, insight, or takeaway text |
| Book | Relation | -> Books database |
| Book Title | Rollup | Title from Book relation |
| Type | Select | Quote / Key Insight / Action Item / Chapter Summary / Concept / Framework / Question / Disagreement |
| Chapter | Text | Chapter name or number for reference |
| Page | Number | Page number for finding it again |
| Category | Multi-select | Life Advice / Business Strategy / Psychology / Writing / Productivity / Relationships / Leadership / Creativity / Health / Philosophy / Science / Money |
| Importance | Select | Core (use often) / Notable (reference occasionally) / Interesting (archive) |
| My Reflection | Text | Your own interpretation or how this applies to your life |
| Action Required | Checkbox | Does this insight require you to do something? |
| Action Item | Text | Specific action step derived from this insight |
| Action Done | Checkbox | Completed the action |
| Connected To | Relation | -> Key Takeaways & Quotes (self-referential for linking ideas across books) |
| Tags | Multi-select | Mindset / Strategy / Tactical / Counterintuitive / Quotable / Share-worthy / Personal |
| Date Captured | Date | When you recorded this |
| Times Reviewed | Number | How often you've revisited this note |
| Last Reviewed | Date | Most recent review |
| Still Relevant | Checkbox | Is this still meaningful to you? (checked during reviews) |

**Views:**

- **All Notes** — Table, sorted by Date Captured descending
- **By Book** — Table, grouped by Book Title
- **Quotes** — Filter: Type = Quote, sorted by Importance
- **Key Insights** — Filter: Type = Key Insight
- **Action Items** — Filter: Action Required = true AND Action Done = false
- **Frameworks** — Filter: Type = Framework or Concept
- **Core Ideas** — Filter: Importance = Core (your most referenced insights)
- **By Category** — Table, grouped by Category
- **Needs Review** — Filter: Last Reviewed is empty OR more than 30 days ago
- **Share-worthy** — Filter: Tags contains Share-worthy or Quotable
- **Connected Ideas** — Table showing Connected To relation (cross-book links)

---

## DASHBOARD

> Create this as the top-level page for your reading system. It shows what you're currently reading, your pace, and surfaces notes for review.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  READING HUB                                     2026             |
+----------------+--------------+----------------+-----------------+
|  Books Read    |  Currently   |  Pages This    |  Reading Pace   |
|  This Year: 12|  Reading: 2  |  Month: 847    |  22 pg/day avg  |
+----------------+--------------+----------------+-----------------+
|                                                                    |
|  CURRENTLY READING                                                |
|  [Linked view -> Books, Status = Currently Reading]               |
|  Atomic Habits: 72% (186/259 pages) - ~3 days left               |
|  Thinking Fast & Slow: 34% (155/449 pages) - ~13 days left       |
|                                                                    |
+----------------------------------+-------------------------------+
|  RECENT SESSIONS                 |  UP NEXT                      |
|  [Linked view -> Sessions,       |  [Linked view -> Books,       |
|   last 7 days]                   |   Status = Up Next,           |
|                                  |   sorted by Priority]         |
+----------------------------------+-------------------------------+
|  READING CHALLENGE 2026                                           |
|  Goal: 36 books | Completed: 12 | Pace: on track for 35         |
|  [Linked view -> Books, Year Read = 2026]                         |
+----------------------------------+-------------------------------+
|  NOTES TO REVIEW                 |  RECENT CAPTURES              |
|  [Linked view -> Key Takeaways,  |  [Linked view -> Key          |
|   Needs Review]                  |   Takeaways, recent 10]       |
+----------------------------------+-------------------------------+
|  5-STAR SHELF                                                     |
|  [Linked view -> Books, Gallery, Rating = 5 Stars]                |
+------------------------------------------------------------------+
```

---

## STATUS WORKFLOW

Books move through these stages:

```
Want to Read -> Up Next -> Currently Reading -> Completed
                                             -> Abandoned (if quitting)
                                             -> Re-reading (for favorites)
```

### Rules

- **Want to Read:** Anything that interests you. No limit. This is your infinite backlog.
- **Up Next:** Your curated short list (max 5-7). These are the next books you'll actually read.
- **Currently Reading:** What you're actively reading (max 2-3 at a time to avoid context-switching).
- **Completed:** Finished. Set the Finish Date, Rating, One-Line Summary, and Key Takeaway.
- **Abandoned:** Quit reading. Add a note about why. No shame — life is too short for bad books.
- **Re-reading:** Coming back to a book. Great for favorites or reference material.

---

## READING PACE FORMULAS

### Reading Progress (Books database)

```
if(
  prop("Pages") == 0,
  0,
  round(prop("Current Page") / prop("Pages") * 100)
)
```

### Days to Read (Books database)

```
if(
  and(not(empty(prop("Start Date"))), not(empty(prop("Finish Date")))),
  dateBetween(prop("Finish Date"), prop("Start Date"), "days"),
  if(
    and(not(empty(prop("Start Date"))), prop("Status") == "Currently Reading"),
    dateBetween(now(), prop("Start Date"), "days"),
    0
  )
)
```

### Pages Per Day (Books database)

```
if(
  prop("Days to Read") == 0,
  0,
  round(prop("Pages") / max(prop("Days to Read"), 1))
)
```

### Estimated Days to Finish (Books database)

```
if(
  or(prop("Pages Per Day") == 0, prop("Status") != "Currently Reading"),
  0,
  round((prop("Pages") - prop("Current Page")) / prop("Pages Per Day"))
)
```

### Pages Per Hour (Reading Sessions)

```
if(
  prop("Duration (min)") == 0,
  0,
  round(prop("Pages Read") / (prop("Duration (min)") / 60))
)
```

### Reading Challenge Pace

Calculate manually from "This Year" view:
```
Books completed this year / months elapsed * 12 = projected year-end total
```

If projected total < goal, you need to increase reading frequency or choose shorter books.

---

## REVIEW SYSTEM

### Spaced Review Schedule

After completing a book, set Review Date intervals:
- First review: 7 days after finishing
- Second review: 30 days after first review
- Third review: 90 days after second review
- Annual review: once per year for core favorites

### What to Do During a Review

1. Open the book's linked Key Takeaways & Quotes
2. Re-read your Key Insights and Quotes
3. Ask: "Is this still relevant? Has anything changed?"
4. Check "Still Relevant" on notes that still matter
5. Mark any Action Items that are now done
6. Update "Times Reviewed" and "Last Reviewed"
7. Set next Review Date
8. If a book no longer resonates, move it out of the review cycle

---

## BOOK NOTES TEMPLATE

When you finish a book (or after major reading sessions), create entries in Key Takeaways & Quotes using this structure:

### For each book, capture at minimum:

1. **3-5 Key Insights** (Type = Key Insight) — The most important ideas in your own words
2. **5-10 Best Quotes** (Type = Quote) — Passages you highlighted
3. **1-3 Action Items** (Type = Action Item) — Things to do based on what you read
4. **1 Chapter Summary per chapter** (Type = Chapter Summary) — Optional for non-fiction

### Template for Key Insight entries:
- Content: The insight stated clearly in one sentence
- My Reflection: How this applies to your life/work specifically
- Category: Which area of life it relates to
- Importance: Core / Notable / Interesting
- Connected To: Link to related insights from other books

---

## KEY FORMULA REFERENCE

### Progress Display

```
format(prop("Reading Progress")) + "% (" + format(prop("Current Page")) + "/" + format(prop("Pages")) + ")"
```

### Estimated Finish Display

```
if(
  prop("Estimated Days Left") == 0,
  "N/A",
  format(prop("Estimated Days Left")) + " days at current pace"
)
```

### Session Pages Read

```
prop("End Page") - prop("Start Page")
```

### Year Read

```
if(empty(prop("Finish Date")), "", formatDate(prop("Finish Date"), "YYYY"))
```

---

## QUICK-START GUIDE

### Step 1 — Add Your Current Books (10 minutes)

- Open the **Books** database
- Add what you're currently reading. Set Status = Currently Reading, add Pages and Current Page.
- Add 5-10 books you want to read next. Set Status = Want to Read or Up Next.
- Add 5-10 books you've read recently. Set Status = Completed, add Rating and Finish Date.

### Step 2 — Start Logging Sessions (ongoing)

- Every time you read, create a quick entry in **Reading Sessions**
- Required: Book, Date, Start Page, End Page, Duration
- Optional but valuable: Time of Day, Focus Quality, Location
- This takes 30 seconds and gives you incredible reading analytics over time

### Step 3 — Capture Notes as You Read

- When you highlight something important, add it to **Key Takeaways & Quotes**
- You don't need to capture everything — aim for 3-5 insights and 5-10 quotes per book
- Batch-capture at the end of a reading session or when you finish the book

### Step 4 — Complete the Finish Workflow

When you finish a book:
1. Set Status = Completed and add Finish Date
2. Set Rating
3. Write One-Line Summary and Key Takeaway
4. Add your Key Insights and Quotes to the notes database
5. Set first Review Date (7 days out)
6. Mark "Would Recommend" and write "Recommend To" if applicable

### Step 5 — Build Your Dashboard

- Create a new page titled "Reading Hub"
- Add linked views as shown in the Dashboard Layout
- Pin to your sidebar

### Step 6 — Set Your Reading Challenge

- Decide on your annual goal (number of books)
- Use the "This Year" view to track progress
- Check monthly: are you on pace? Adjust by reading shorter books or increasing session frequency.

### Pro Tips

- Update Current Page every time you read. It takes 2 seconds and keeps your progress display accurate — which is motivating.
- Don't rate books immediately after finishing. Wait 3-7 days. Your rating will be more honest once the recency effect fades.
- The "Abandoned" status is a feature, not a failure. Forcing yourself through a bad book wastes time you could spend on a great one. Quit without guilt.
- Use "Connected To" in Key Takeaways to link ideas across books. After 20+ books, these connections become your most valuable intellectual asset.
- Track Time of Day in Reading Sessions for a month. You'll discover when you read best (most people have a clear winner) and can protect that time.
- Keep "Up Next" to 5-7 books maximum. An infinite to-read list is aspirational fantasy. A short curated queue is an actual reading plan.
- Review your notes. Capturing insights is pointless if you never revisit them. The spaced review system prevents the common failure where you read 30 books and can't recall what any of them said.
