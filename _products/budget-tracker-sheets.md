# Setup Guide: Personal Budget Tracker — Google Sheets

## Step 1: Import the CSV Into Google Sheets

1. Go to [sheets.google.com](https://sheets.google.com) and open a new blank spreadsheet.
2. Go to **File > Import**.
3. Click **Upload** and select `template.csv` from your downloads folder.
4. In the import settings:
   - Import location: **Replace spreadsheet**
   - Separator type: **Comma**
   - Convert text to numbers and dates: **Yes**
5. Click **Import data**.

The entire template will load into Sheet 1. You'll see `--- SHEET: ---` markers indicating where new sheets should begin.

---

## Step 2: Split Into Separate Sheets

Because CSV is a single-sheet format, the multi-sheet template is separated by markers (`--- SHEET: Monthly Budget ---`, `--- SHEET: Transaction Log ---`, etc.). Here's how to set up each sheet properly:

1. Look for the row containing `--- SHEET: Monthly Budget ---` — this is the start of Sheet 1. Your data begins below it.
2. Create a new tab at the bottom (click the `+` button) and name it **Transaction Log**.
3. Find the rows between `--- SHEET: Transaction Log ---` and `--- SHEET: Annual Overview ---` in the imported data. Select those rows, cut them (Ctrl+X), switch to your new tab, and paste (Ctrl+V) into cell A1.
4. Repeat for **Annual Overview** and **Debt Payoff Tracker**.
5. Delete the now-empty marker rows from each sheet.

**Tip:** Rename your tabs from the bottom tab bar by double-clicking each tab name.

---

## Step 3: Activate Formulas

The template includes formulas written as text strings (e.g., `=SUM(D5:D9)`) so they survive CSV export. To activate them:

1. Click any cell containing a formula (they start with `=`).
2. The formula text should already be recognized. If a cell shows the formula as text, click the cell, press F2 to enter edit mode, then press Enter.
3. For columns with formulas that need to extend down (like the Running Balance in the Transaction Log), select the cell with the formula and drag the blue fill handle downward to apply it to new rows.

**Bulk activation shortcut:** If many cells show formulas as text, use Find & Replace (Ctrl+H):
- Find: `=`
- Replace: `=`
- This forces Google Sheets to re-evaluate all formula strings.

---

## Step 4: Set Up Category Dropdowns (Transaction Log)

To enable a dropdown for the Category column in the Transaction Log:

1. Select the entire column C in the Transaction Log sheet (click the column letter C).
2. Go to **Data > Data validation**.
3. Click **Add rule**.
4. Set Criteria to **Dropdown (from a range)**.
5. Enter the range where your category list lives (the category reference section at the top of the Transaction Log sheet, e.g., `'Transaction Log'!A8:A32`).
6. Click **Done**.

Now every cell in column C will have a dropdown with all your category options.

---

## Step 5: Set Up the Payment Method Dropdown

Repeat the same process for column E (Payment Method) in the Transaction Log:

1. Select column E.
2. Data > Data validation > Add rule > Dropdown.
3. Manually enter options: `Credit Card, Debit Card, Cash, ACH Transfer, Check, Direct Deposit, Venmo/PayPal, Other`
4. Click Done.

---

## Step 6: Customize Your Income and Expenses

### Monthly Budget Sheet

- **Income Section:** Replace the example figures in column B with your actual income sources. Change "Salary" to your employer's name, add or delete rows as needed.
- **Fixed Expenses:** Update every amount in column B to match your actual bills. Delete rows for expenses you don't have.
- **Variable Expenses:** Set your own monthly budget targets in column B. Update column C with actual spending at the end of each month.
- **Savings Goals:** Enter your goal name, target amount, current saved amount, and monthly contribution. The "Months to Goal" formula calculates automatically.

### How to Add or Delete Rows

- **Add a row:** Right-click a row number and select **Insert 1 row above/below**. Copy the formula from an adjacent row into the new row.
- **Delete a row:** Right-click the row number and select **Delete row**. Google Sheets will update formula ranges automatically in most cases. Double-check SUM ranges after deleting rows.

---

## Step 7: Set Up Conditional Formatting for Over-Budget Items

Make it easy to spot overspending at a glance:

1. In the Monthly Budget sheet, select the "Remaining" column for Variable Expenses (column D, rows for variable items).
2. Go to **Format > Conditional formatting**.
3. Add a rule: **Less than** `0` → Format: Red background.
4. Add another rule: **Greater than or equal to** `0` → Format: Green background.
5. Click **Done**.

Now overspent categories will turn red automatically.

---

## Step 8: Create Charts From the Annual Overview

1. Go to the **Annual Overview** sheet.
2. Select the Chart Data section (the Month / Income / Total Expenses / Savings table at the bottom).
3. Go to **Insert > Chart**.
4. Google Sheets will auto-suggest a chart. Choose **Line chart** for trend visualization.
5. In the Chart Editor:
   - X-axis: Month column
   - Series: Income, Total Expenses, Savings
   - Customize colors, title, and legend as desired.
6. Click the chart and drag it to your preferred position on the sheet.

---

## Step 9: Monthly Workflow

**Start of month:**
- Update the Month label in the Monthly Budget sheet.
- Review and adjust your budget targets if needed.
- Carry forward any changes to Fixed Expenses (new bills, rate changes).

**Throughout the month:**
- Log every transaction in the Transaction Log as it happens (or batch weekly).
- Update the "Actual Spent" column in Variable Expenses periodically.

**End of month:**
- Finalize all transactions in the Transaction Log.
- Enter the month's totals into the Annual Overview sheet.
- Review your savings progress and adjust contributions if needed.
- If paying down debt, update the Debt Payoff Tracker with new balances.

---

## Tips and Tricks

**Freeze header rows:** Go to View > Freeze > 1 row to keep column headers visible while scrolling.

**Protect formula cells:** Select your formula cells, right-click > Protect range, to prevent accidental edits.

**Use Google Sheets on mobile:** Install the Google Sheets app and log transactions from your phone right after purchases — this dramatically improves accuracy.

**Share with a partner:** Click the Share button (top right) and invite your partner as an Editor. You can both update the sheet in real time.

**Make a monthly copy:** At the end of each month, duplicate the entire spreadsheet (File > Make a copy) as a permanent record before starting the new month fresh.

**Color-code your sheets:** Right-click each tab at the bottom and choose a color to visually distinguish sections at a glance.

---

## Common Questions

**Q: Can I add more expense categories?**
A: Yes — simply add new rows in the relevant sections and update any SUM formulas to include the new rows.

**Q: What if my income varies month to month?**
A: Budget based on your lowest expected monthly income. Enter your actual income at the start of each month — any surplus over your budget is a bonus.

**Q: How do I track credit card spending without double-counting?**
A: Log individual purchases as expenses when they happen. Do not log your credit card payment as an expense — that would double-count the spending.

**Q: Can I use this on Excel?**
A: Yes. Open Excel, go to File > Open, and open the CSV file directly. The formulas and structure work in Excel as well, though you may need to reformat some cells.
