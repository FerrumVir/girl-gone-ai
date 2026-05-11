# Setup Guide: Habit Streak Tracker — Google Sheets

## Step 1: Import the CSV Into Google Sheets

1. Go to [sheets.google.com](https://sheets.google.com) and open a new blank spreadsheet.
2. Go to **File > Import**.
3. Click **Upload** and select `template.csv` from your downloads folder.
4. In the import settings:

   - Import location: **Replace spreadsheet**
   - Separator type: **Comma**
   - Convert text to numbers and dates: **Yes**
5. Click **Import data**.

All content will load into a single sheet with section markers. You'll see `--- SHEET: ---` headers separating each section.

---

## Step 2: Create Separate Sheets for Each Section

The template has 5 sections that should each become their own Google Sheets tab. Here's how to split them:

1. Create 4 additional tabs by clicking the `+` button at the bottom four times. Name them:

   - **Habit Dashboard**
   - **Daily Tracker**
   - **Weekly Review**
   - **Monthly Summary**
   - **Habit Library**
2. Rename your first tab "Habit Dashboard."
3. In the imported sheet, find the block of rows between `--- SHEET: Habit Dashboard ---` and `--- SHEET: Daily Tracker ---`. Select those rows, cut (Ctrl+X), and paste into your Habit Dashboard tab starting at A1.
4. Repeat for each subsequent section, moving each block into its corresponding tab.
5. Delete the marker rows (`--- SHEET: ---`) and any leftover blank rows from each tab.

**Tip:** After separating, delete the now-empty original import tab.

---

## Step 3: Activate Formulas

Formulas in the CSV are stored as text strings (beginning with `=`). To activate them:

1. Use Find & Replace (Ctrl+H):

   - Find: `=`
   - Replace: `=`
   - This forces Google Sheets to recognize every formula.
2. If any cells still show formula text instead of calculated values, click the cell, press F2, then press Enter.

Do this on all five sheets.

---

## Step 4: Replace the Example Habits With Yours

The template comes pre-filled with 20 example habits. Here's how to customize it:

### Habit Dashboard Tab
- Column B (Habit Name): Type your own habit name over each example.
- Column C (Category): Options are Health / Productivity / Learning / Wellness / Social / Financial / Morning Routine — pick whichever fits.
- Column D (Frequency): Enter Daily or Weekly.
- Columns E and F (Current Streak / Best Streak): Enter 0 to start fresh, or enter your existing streak if you're already tracking.
- Column G (Completion Rate %): Enter 0% initially — this will fill in as you track.
- Column H (Status): Update manually or set a formula (see below).

**Status formula for column H:**
```
=IF(E2>=30,"Streak Master!",IF(E2>=14,"On Fire!",IF(G2="0%","Restart Needed",IF(VALUE(LEFT(G2,LEN(G2)-1))<50,"Struggling","Active"))))
```
Paste this into each Status cell for automatic status updates.

### How to add or remove habits:
- **Add:** Insert a new row, fill in columns B through H, and copy the formula from an adjacent row into the Completion Rate cell.
- **Remove:** Delete the row. The Summary Stats section at the bottom uses COUNTA/COUNTIF and will update automatically.

---

## Step 5: Set Up the Daily Tracker

The Daily Tracker is your main day-to-day sheet. To use it:

1. The rows in column A should list your habits in the same order as the Habit Dashboard.
2. Columns B through AF represent days 1–31 of the month.
3. Each day, enter `X` in the cell where the row (habit) meets the column (date).
4. Leave cells blank for missed days.
5. The "Done" column counts your X marks using COUNTIF. The "Rate %" column divides Done by Possible.

**At the start of each new month:**
1. Duplicate the Daily Tracker tab (right-click the tab > Duplicate).
2. Rename the copy with the current month name (e.g., "May 2026").
3. Clear all X entries from the grid (select the data range, press Delete).
4. Update the month label in row 1.
5. Update the "Possible" column to reflect the number of days in the new month (e.g., 28 for February, 31 for March).

---

## Step 6: Set Up Category and Frequency Dropdowns (Optional)

For cleaner data entry in the Habit Dashboard:

1. Select column C (Category) in the Habit Dashboard.
2. Go to **Data > Data validation > Add rule**.
3. Set criteria to **Dropdown** and enter the options:
   `Health, Productivity, Learning, Wellness, Social, Financial, Morning Routine`
4. Repeat for column D (Frequency):
   `Daily, Weekly, Monthly`

---

## Step 7: Set Up Conditional Formatting for Streaks and Completion

Make your tracker visually motivating:

### Highlight completed habit cells (Daily Tracker):
1. Select the data grid (B6:AF25 or your equivalent range).
2. Go to **Format > Conditional formatting**.
3. Rule: **Text is exactly** `X` → Format: Green fill.
4. Add another rule: **Is empty** → Format: Light gray fill.

### Color-code completion rates (Habit Dashboard):
1. Select the Completion Rate % column (G7:G26).
2. Format > Conditional formatting.
3. Rule: **Less than** `60%` → Red.
4. Rule: **Between** `60%` and `80%` → Yellow.
5. Rule: **Greater than or equal to** `80%` → Green.

### Highlight streak length (Habit Dashboard):
1. Select the Current Streak column (E7:E26).
2. Color scale formatting (Format > Conditional formatting > Color scale).
3. Minimum: white. Maximum: deep green.

---

## Step 8: Connect the Habit Library to Your Dashboard

The Habit Library tab contains 50 pre-populated habits. Use it as a menu:

1. Browse categories to find habits you want to try.
2. Copy the habit name from the library.
3. Paste it into an empty row in your Habit Dashboard.
4. Set the frequency based on the library's suggestion.
5. Start tracking it in the Daily Tracker.

**Recommended approach for beginners:** Start with 3-5 habits maximum. Research shows that fewer habits tracked consistently outperforms many habits tracked poorly.

---

## Step 9: Weekly Review Workflow

Every week (Sunday evenings work well for most people):

1. Open the **Weekly Review** tab.
2. Add a new row for the completed week.
3. Fill in:

   - Date range (e.g., Apr 28 – May 4)
   - Total completions (count X marks from the Daily Tracker for that week)
   - Total possible (number of habits × 7 for daily habits, plus weekly habit opportunities)
   - Completion % (the formula calculates this)
   - Top Habit: which habit had your best rate this week
   - Most Missed: which habit needs attention
   - Reflection Notes: one or two sentences on what made the week go well or poorly
4. Check the 4-week rolling average to see your trajectory.

---

## Step 10: Monthly Summary Workflow

At the end of each month:

1. Open the **Monthly Summary** tab.
2. Add the month's data to the next empty row.
3. Pull total completions from your Daily Tracker (count all X marks).
4. Note any new habits started, habits dropped, and streak milestones hit.
5. Add any notes on what defined that month for your habit practice.

The Year-at-a-Glance grid gives you a bird's-eye view of your consistency across the entire year.

---

## Tips and Best Practices

**Keep the tracker visible.** Pin the spreadsheet as a browser bookmark or add it to your phone's home screen. Out of sight is out of habit.

**Log completions at the same time each day.** Many people update their tracker right before bed as part of a wind-down ritual. Whatever time you choose, make it consistent.

**Don't track too many habits at once.** The research on habit formation suggests building one or two habits at a time. The tracker supports up to 20 habits, but starting with 3-5 gives you a much higher success rate.

**Use the Habit Library strategically.** When a habit drops below 50% for two consecutive weeks, consider swapping it for something from the library that excites you more — or reducing its frequency from daily to weekly.

**Protect your streak psychology.** If you miss one day, the most important thing is not to miss two in a row. Research by behavioral scientists calls this the "never miss twice" rule. Log it, note what happened, and start fresh the next day.

**Share for accountability.** Give a trusted friend view access to your tracker. Knowing someone can see your X marks is a surprisingly powerful motivator.

**Review Best Streaks monthly.** Your Best Streak column shows your personal record for each habit. Trying to beat your own record is more motivating than abstract goals.

---

## Common Questions

**Q: Can I add more than 20 habits?**
A: Yes — insert rows in the Daily Tracker between the last habit row and the Daily Completions row. Copy the formulas from adjacent rows into the new rows. Update the Daily Completions COUNTIF ranges to include the new rows, and update the `/20` divisor in the daily percentage row to match your new total.

**Q: How do I calculate streaks automatically?**
A: Automated streak calculation in Google Sheets requires an array formula. For a fully automated approach: select your habit row in the Daily Tracker, and use the formula `=ARRAYFORMULA(MAX(FREQUENCY(IF(B6:AF6="X",COLUMN(B6:AF6)),IF(B6:AF6<>"X",COLUMN(B6:AF6)))))` to calculate the longest streak in that row. Note: This is an advanced formula — the manual approach (updating the streak number in the Dashboard yourself) works reliably and keeps the tracker accessible to all skill levels.

**Q: What if I want to track a habit monthly instead of weekly or daily?**
A: Add the habit to the Dashboard and Daily Tracker as normal. In the Daily Tracker, only mark it on the days you complete it. At the end of the month, your completion rate will reflect how often you hit the goal.

**Q: Can I use this offline?**
A: Yes — go to File > Make available offline in Google Sheets. Your spreadsheet will sync when you reconnect to the internet.
