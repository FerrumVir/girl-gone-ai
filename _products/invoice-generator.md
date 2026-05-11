# Setup Guide: Professional Invoice Generator — Google Sheets & Excel

---

## Quick-Start Guide

If you want to send your first invoice in under 15 minutes, follow these four steps:

1. Create a new Google Sheets (or Excel) workbook and rename it **Invoice System**.
2. Build the **Standard Invoice** template from the layout in Section 1 below, or use the cell-by-cell instructions to set it up in about 20 minutes.
3. Enter your business information in the yellow-highlighted cells at the top of the invoice sheet.
4. Fill in the client name, service description, and amount — the subtotal, tax, and total calculate automatically.

For the full system — auto-numbering, client database, payment tracking, and year-end summary — work through the sections in order. Total setup time is 30–45 minutes.

---

## Workbook Structure

Create one workbook with the following sheets (tabs):

| Tab Name | Purpose |
|---|---|
| `INV-Standard` | Standard single-service invoice template |
| `INV-Itemized` | Line-item invoice for detailed billing |
| `INV-Retainer` | Recurring / retainer billing template |
| `Clients` | Client database with auto-fill data |
| `Invoice Log` | Master log of all invoices sent |
| `Payment Tracker` | Dashboard: paid / unpaid / overdue status |
| `Year-End Summary` | Monthly totals and per-client breakdown |
| `Settings` | Invoice number counter, tax rates, currency |

Name each tab by double-clicking the tab label at the bottom of the screen.

---

## Section 1: Standard Invoice Template

### Layout (INV-Standard sheet)

The Standard Invoice fits cleanly on one printed page. Build it using the cell positions below. Merged cells are noted with a range (e.g., A1:D1 means those columns are merged into one cell).

```
  A           B           C           D           E
  +-----------+-----------+-----------+-----------+-----------+
1 | [LOGO]                            | INVOICE               |
  | A1:B3 (image)                     | D1:E1 (large text)    |
  +-----------+-----------+-----------+-----------+-----------+
2 |                                   | Invoice #: [auto]     |
  |                                   | D2: label, E2: value  |
  +-----------+-----------+-----------+-----------+-----------+
3 |                                   | Date: [auto-today]    |
  |                                   | D3: label, E3: value  |
  +-----------+-----------+-----------+-----------+-----------+
4 |                                   | Due Date: [auto]      |
  |                                   | D4: label, E4: value  |
  +-----------+-----------+-----------+-----------+-----------+
5 | [YOUR BUSINESS NAME]              |                       |
  | A5:B5                             |                       |
  +-----------+-----------+-----------+-----------+-----------+
6 | [Street Address]                  |                       |
7 | [City, State ZIP]                 |                       |
8 | [Email]                           |                       |
9 | [Phone]                           |                       |
  +-----------+-----------+-----------+-----------+-----------+
11| BILL TO:                          |                       |
  | A11 (bold label)                  |                       |
  +-----------+-----------+-----------+-----------+-----------+
12| [Client Name]     (auto-fill)     |                       |
13| [Client Address]  (auto-fill)     |                       |
14| [City, State ZIP] (auto-fill)     |                       |
15| [Client Email]    (auto-fill)     |                       |
  +-----------+-----------+-----------+-----------+-----------+
17| DESCRIPTION       (header)| QTY  | RATE      | AMOUNT    |
  | A17:B17 merged            | C17  | D17       | E17       |
  +-----------+-----------+-----------+-----------+-----------+
18| [Service description line 1]| 1  | [rate]    | [=C18*D18]|
19| [Service description line 2]| 1  | [rate]    | [=C19*D19]|
20| (rows 18-27 available)      |    |           |           |
  +-----------+-----------+-----------+-----------+-----------+
28|                           |        | Subtotal: | [=SUM]   |
29|                           |        | Tax Rate: | [input]  |
30|                           |        | Tax:      | [formula]|
31|                           |        | TOTAL DUE:| [formula]|
  +-----------+-----------+-----------+-----------+-----------+
33| Payment Terms: [auto-fill]        |                       |
34| Make checks payable to: [name]    |                       |
35| Bank transfer details: [optional] |                       |
  +-----------+-----------+-----------+-----------+-----------+
37| Notes / Thank you message         |                       |
  | A37:E37 merged                    |                       |
  +-----------+-----------+-----------+-----------+-----------+
```

### Cell-by-Cell Setup: Standard Invoice

**Header — Your Business Information (enter once, never change):**

| Cell | Content | Notes |
|---|---|---|
| A5 | Your business name | Bold, font size 14 |
| A6 | Street address | |
| A7 | City, State ZIP | |
| A8 | Email address | |
| A9 | Phone number | |
| D1 | `INVOICE` | Bold, font size 24, right-aligned |

**Invoice Metadata (calculated automatically):**

| Cell | Formula | What it does |
|---|---|---|
| E2 | `=Settings!B3` | Pulls current invoice number from Settings sheet |
| E3 | `=TODAY()` | Today's date, updates when you open the file |
| E4 | `=E3+Settings!B5` | Due date = today + payment terms (days) from Settings |

**Client Information (auto-fill from Clients sheet):**

| Cell | Formula | What it does |
|---|---|---|
| A12 | `=IFERROR(VLOOKUP(E12,Clients!A:F,2,0),"")` | Client name |
| A13 | `=IFERROR(VLOOKUP(E12,Clients!A:F,3,0),"")` | Street address |
| A14 | `=IFERROR(VLOOKUP(E12,Clients!A:F,4,0),"")` | City, State ZIP |
| A15 | `=IFERROR(VLOOKUP(E12,Clients!A:F,5,0),"")` | Email |
| E12 | *(client code — you type this)* | Enter the client code here to trigger all auto-fills |

Note: E12 is the only cell you type in for client information. The rest populate automatically. You can hide row 12's column E label if it looks odd by formatting it in white text.

**Line Items (rows 18–27):**

| Cell | Formula | Notes |
|---|---|---|
| E18 | `=IF(C18="","",C18*D18)` | Qty x Rate; blank if no qty entered |
| E19 | `=IF(C19="","",C19*D19)` | Repeat for rows 19–27 |

Enter the description in columns A–B (merged). Enter quantity in C and rate in D. The amount in E calculates automatically. Rows with nothing in column C stay blank.

**Totals Section:**

| Cell | Formula | What it does |
|---|---|---|
| E28 | `=SUM(E18:E27)` | Subtotal of all line items |
| E29 | *(input cell)* | Tax rate — type e.g. `0.08` for 8%. Links to Settings if you want a default |
| E30 | `=IF(IFERROR(VLOOKUP(E12,Clients!A:F,6,0),"")<>"EXEMPT",E28*E29,0)` | Tax amount (0 if client is tax-exempt) |
| E31 | `=E28+E30` | Grand total due |

**Due Date and Terms:**

| Cell | Formula | Notes |
|---|---|---|
| A33 | `="Payment Terms: "&IFERROR(VLOOKUP(E12,Clients!A:G,7,0),Settings!B6)` | Pulls per-client terms, falls back to default |
| A34 | `="Make checks payable to: "&A5` | Uses your business name from A5 |

---

## Section 2: Itemized Invoice Template

### Layout (INV-Itemized sheet)

The Itemized Invoice is structurally similar to the Standard Invoice but replaces the simple description/qty/rate block with a full line-item table that includes a date column and task category.

```
  A         B         C         D         E         F
  +---------+---------+---------+---------+---------+---------+
1 | [LOGO]                      | INVOICE                     |
2 |                             | Invoice #:       | [auto]   |
3 |                             | Date:            | [auto]   |
4 |                             | Due Date:        | [auto]   |
5 | [YOUR BUSINESS NAME]        |                             |
  ... (rows 5–9 same as Standard) ...
11| BILL TO:                    |                             |
  ... (rows 12–15 same as Standard, same VLOOKUP formulas) ...
  +---------+---------+---------+---------+---------+---------+
17| DATE     | TASK/DESCRIPTION      | HOURS| RATE  | AMOUNT  |
  | A17      | B17:C17 merged        | D17  | E17   | F17     |
  +---------+---------+---------+---------+---------+---------+
18| [date]   | [task description]    | [hrs]| [rate]| [=D*E]  |
19| [date]   | [task description]    | [hrs]| [rate]| [=D*E]  |
   ... rows 18–37 available (20 line items) ...
  +---------+---------+---------+---------+---------+---------+
38|                              | Total Hours:     | [=SUM]  |
39|                              | Subtotal:        | [=SUM]  |
40|                              | Tax Rate:        | [input] |
41|                              | Tax:             | [formula|
42|                              | TOTAL DUE:       | [formula|
  +---------+---------+---------+---------+---------+---------+
44| Notes:                                                     |
  +---------+---------+---------+---------+---------+---------+
```

### Cell-by-Cell Setup: Itemized Invoice

**Line Items (rows 18–37):**

| Cell | Formula | Notes |
|---|---|---|
| A18 | *(date input)* | Format as date: Format > Number > Date |
| B18:C18 | *(task description — merged cells)* | Merge B18:C18 |
| D18 | *(hours/qty input)* | |
| E18 | *(rate input)* | Format as currency |
| F18 | `=IF(D18="","",D18*E18)` | Auto-calculates; blank if hours empty |

Repeat F18 formula for F19:F37.

**Totals:**

| Cell | Formula | What it does |
|---|---|---|
| F38 | `=SUM(D18:D37)` | Total hours worked |
| F39 | `=SUM(F18:F37)` | Subtotal |
| F40 | *(input)* | Tax rate |
| F41 | `=IF(IFERROR(VLOOKUP(E12,Clients!A:F,6,0),"")<>"EXEMPT",F39*F40,0)` | Tax |
| F42 | `=F39+F41` | Total due |

**Date Auto-Fill Tip:**

To fill today's date in A18 automatically when you start a new line: select A18:A37, go to Data > Data validation, and set a custom rule. Alternatively, press Ctrl+; (Windows) or Cmd+; (Mac) to insert the current date as a static value in any cell.

---

## Section 3: Retainer / Recurring Invoice Template

### Layout (INV-Retainer sheet)

The Retainer Invoice handles monthly (or weekly) clients where you bill a fixed amount plus any overages.

```
  A              B              C              D
  +--------------+--------------+--------------+--------------+
1 | [LOGO]                      | INVOICE                     |
2 |                             | Invoice #:    | [auto]      |
3 |                             | Date:         | [auto]      |
4 |                             | Billing Period| [auto range]|
5 | [YOUR BUSINESS NAME]                                       |
  ... (rows 5–9 same structure) ...
11| BILL TO:                                                   |
  ... (rows 12–15 same VLOOKUP auto-fill) ...
  +--------------+--------------+--------------+--------------+
17| RETAINER BILLING SUMMARY                                   |
  +--------------+--------------+--------------+--------------+
18| Monthly Retainer Fee:                       | [input]     |
19| Included Hours:                             | [input]     |
20| Hours Used This Period:                     | [input]     |
21| Overage Hours:                              | [formula]   |
22| Overage Rate (per hour):                    | [input]     |
23| Overage Charges:                            | [formula]   |
24|                             +--------------+--------------+
25| Additional Items / Expenses:                              |
  +--------------+--------------+--------------+--------------+
26| [description]                               | [amount]    |
27| [description]                               | [amount]    |
28| [description]                               | [amount]    |
  +--------------+--------------+--------------+--------------+
30|                             | Subtotal:     | [formula]   |
31|                             | Tax Rate:     | [input]     |
32|                             | Tax:          | [formula]   |
33|                             | TOTAL DUE:    | [formula]   |
  +--------------+--------------+--------------+--------------+
35| RETAINER HISTORY (this client)                            |
36| Date Sent | Invoice # | Period | Amount | Paid | Balance  |
37| [auto log] ...                                            |
  +--------------+--------------+--------------+--------------+
```

### Cell-by-Cell Setup: Retainer Invoice

**Billing Period Auto-Fill:**

| Cell | Formula | What it does |
|---|---|---|
| D4 | `=TEXT(DATE(YEAR(D3),MONTH(D3),1),"MMM 1")&" – "&TEXT(EOMONTH(D3,0),"MMM D, YYYY")` | Formats billing period as "Apr 1 – Apr 30, 2026" |

**Overage Calculation:**

| Cell | Formula | What it does |
|---|---|---|
| D21 | `=MAX(0,D20-D19)` | Overage hours = hours used minus included hours, minimum 0 |
| D23 | `=D21*D22` | Overage charges = overage hours x overage rate |

**Subtotal with Additional Items:**

| Cell | Formula | What it does |
|---|---|---|
| D30 | `=D18+D23+SUM(D26:D28)` | Retainer fee + overage + any additional items |
| D32 | `=IF(IFERROR(VLOOKUP(E12,Clients!A:F,6,0),"")<>"EXEMPT",D30*D31,0)` | Tax (exempt check) |
| D33 | `=D30+D32` | Total due |

---

## Section 4: Settings Sheet

The Settings sheet is the control panel for the entire system. Set it up once.

### Settings Layout

| Row | Column A (Label) | Column B (Value) | Notes |
|---|---|---|---|
| 1 | **INVOICE SETTINGS** | | Header row |
| 2 | Invoice Prefix | `INV` | Change to your preferred prefix (e.g., `2026-INV`) |
| 3 | Next Invoice Number | `1001` | Auto-increments; update after each invoice |
| 4 | Invoice Number Format | `=B2&"-"&TEXT(B3,"0000")` | Produces e.g. `INV-1001` |
| 5 | Default Payment Terms (days) | `30` | Change to 14, 15, or 45 as needed |
| 6 | Default Payment Terms Text | `Net 30` | Displayed on invoice footer |
| 7 | **TAX SETTINGS** | | |
| 8 | Default Tax Rate | `0.08` | 8% — change to your rate |
| 9 | Tax Label | `Sales Tax` | Or "GST", "VAT", "HST", etc. |
| 10 | Multi-Jurisdiction Tax: Rate 1 | `0.06` | e.g., State rate |
| 11 | Multi-Jurisdiction Tax: Rate 1 Label | `State Tax` | |
| 12 | Multi-Jurisdiction Tax: Rate 2 | `0.02` | e.g., County rate |
| 13 | Multi-Jurisdiction Tax: Rate 2 Label | `County Tax` | |
| 14 | **CURRENCY SETTINGS** | | |
| 15 | Currency Symbol | `$` | |
| 16 | Currency Code | `USD` | |
| 17 | **BUSINESS DETAILS** | | |
| 18 | Business Name | *(your name)* | |
| 19 | Business Address | *(your address)* | |
| 20 | Business City/State/ZIP | *(your city)* | |
| 21 | Business Email | *(your email)* | |
| 22 | Business Phone | *(your phone)* | |

---

## Section 5: Auto-Numbering System

### How It Works

The invoice number is stored as a counter in Settings!B3. Each time you create a new invoice:

1. Copy your current invoice template sheet (right-click the tab > Duplicate).
2. Rename the duplicate to the invoice number (e.g., `INV-1001`).
3. The new sheet reads the current counter from Settings!B3 and displays it as the invoice number.
4. After confirming the invoice looks correct, increment the counter: go to Settings!B3 and increase the number by 1 (e.g., change 1001 to 1002).

### Auto-Increment Formula Option

If you prefer the counter to increment automatically, use this approach:

In Settings!B3, instead of a raw number, use:
```
=MAX('Invoice Log'!B:B)+1
```

This reads the highest invoice number recorded in the Invoice Log and adds 1. As long as you log each invoice in the Invoice Log sheet, the counter always knows the next available number.

### Invoice Number Format Examples

Change the prefix in Settings!B2 to get different formats:

| Prefix | Counter | Result |
|---|---|---|
| `INV` | 1001 | `INV-1001` |
| `2026` | 1001 | `2026-1001` |
| `SMITH` | 1001 | `SMITH-1001` |
| *(blank)* | 1001 | `1001` |

The format formula in Settings!B4 (`=B2&"-"&TEXT(B3,"0000")`) applies zero-padding to keep numbers consistent in length. Change `"0000"` to `"00000"` if you need five-digit numbers.

---

## Section 6: Tax Calculation

### Single-Rate Tax

The standard tax formula used in all three invoice templates:

```
=IF(IFERROR(VLOOKUP(ClientCode,Clients!A:F,6,0),"")<>"EXEMPT", Subtotal * TaxRate, 0)
```

This checks whether the client's tax status (column F in the Clients sheet) is "EXEMPT". If it is, tax is $0. Otherwise, it multiplies the subtotal by the tax rate.

To apply: replace `ClientCode` with your client code cell (e.g., `E12`) and `Subtotal` and `TaxRate` with their respective cell references.

### Tax-Exempt Clients

In the Clients sheet, column F is the Tax Status column. For tax-exempt clients, enter `EXEMPT` in this column. The invoice tax formula detects this and sets tax to zero. For all other clients, leave the cell blank or enter `TAXABLE`.

### Multi-Jurisdiction Tax (Two Rates)

For billing situations that require two separate tax rates (e.g., state + county, or federal GST + provincial PST):

Replace the single tax row in your invoice with two rows:

| Cell | Label | Formula |
|---|---|---|
| E29 | Tax Rate 1 label | `=Settings!B11` (pulls "State Tax" label) |
| F29 | Tax Rate 1 amount | `=IF([exempt check],E28*Settings!B10,0)` |
| E30 | Tax Rate 2 label | `=Settings!B13` (pulls "County Tax" label) |
| F30 | Tax Rate 2 amount | `=IF([exempt check],E28*Settings!B12,0)` |
| E31 | Total Tax | `Total Tax:` |
| F31 | Total tax amount | `=F29+F30` |
| E32 | **TOTAL DUE** | `TOTAL DUE:` |
| F32 | Grand total | `=E28+F31` |

Full exempt-check formula for two-rate tax:
```
=IF(IFERROR(VLOOKUP(E12,Clients!A:F,6,0),"")<>"EXEMPT", E28*Settings!B10, 0)
```

### VAT / GST Invoices

For VAT or GST billing (common outside the US), change the Tax Label in Settings!B9 to `VAT` or `GST`. No formula changes are required — the label is cosmetic. The calculation is identical.

---

## Section 7: Currency Formatting

### Applying Currency Format in Google Sheets

1. Select the cells you want to format as currency (rate, amount, subtotal, tax, total columns).
2. Go to **Format > Number > Custom number format**.
3. Paste one of the format codes from the table below.
4. Click **Apply**.

### Currency Format Codes

| Currency | Code | Format String |
|---|---|---|
| US Dollar | USD | `$#,##0.00` |
| Euro | EUR | `€#,##0.00` |
| British Pound | GBP | `£#,##0.00` |
| Canadian Dollar | CAD | `CA$#,##0.00` |
| Australian Dollar | AUD | `A$#,##0.00` |
| Japanese Yen | JPY | `¥#,##0` (no decimals) |
| Swiss Franc | CHF | `CHF #,##0.00` |
| Indian Rupee | INR | `₹#,##0.00` |
| Mexican Peso | MXN | `MX$#,##0.00` |
| Brazilian Real | BRL | `R$#,##0.00` |

### Applying Currency Format in Excel

1. Select the cells.
2. Press **Ctrl+1** to open Format Cells.
3. Go to the **Number** tab > **Custom**.
4. Enter the format string from the table above.
5. Click OK.

### Displaying Currency Code Instead of Symbol

If you invoice internationally and prefer to show "USD 1,250.00" instead of "$1,250.00":

Custom format: `"USD "#,##0.00`

Replace `"USD "` with your currency code. The quotes make it a literal text prefix.

---

## Section 8: Clients Sheet

### Layout

The Clients sheet is your client database. Every row is one client. Your invoice templates look up data here using the client code.

| Col | Field | Example |
|---|---|---|
| A | Client Code | `ACME01` |
| B | Client Name | `Acme Corporation` |
| C | Street Address | `123 Main Street` |
| D | City, State ZIP | `Springfield, IL 62701` |
| E | Email | `accounts@acme.com` |
| F | Tax Status | `TAXABLE` or `EXEMPT` |
| G | Payment Terms | `Net 30` |
| H | Default Rate | `150` |
| I | Notes | Internal notes about the client |

Row 1 is a header row. Client data starts in row 2.

### Adding a New Client

1. Add a new row at the bottom of the Clients sheet.
2. Enter the client code in column A. Use a short, memorable code (no spaces): `SMITH01`, `GLOBEX`, `JDOE`.
3. Fill in columns B through I.
4. When creating an invoice, type the client code into cell E12 of any invoice template. All client information fills in automatically.

### Using Default Rate Per Client

Column H stores the client's standard billing rate. To pull this into an invoice rate cell automatically:

```
=IFERROR(VLOOKUP(E12,Clients!A:H,8,0),"")
```

Place this formula in the Rate column of your first line item. When you enter the client code, the rate pre-fills. You can overwrite it for any line that has a different rate.

---

## Section 9: Invoice Log Sheet

The Invoice Log records every invoice you send. It is the source of truth for the Payment Tracker and Year-End Summary.

### Layout

| Col | Field | Notes |
|---|---|---|
| A | Date Sent | Date you sent the invoice |
| B | Invoice Number | e.g., `INV-1001` |
| C | Client Code | Matches Clients sheet column A |
| D | Client Name | `=IFERROR(VLOOKUP(C2,Clients!A:B,2,0),"")` |
| E | Description | Brief description of the work |
| F | Subtotal | Invoice subtotal before tax |
| G | Tax | Tax amount |
| H | Total | `=F2+G2` |
| I | Due Date | Date payment is due |
| J | Date Paid | Date payment was received (leave blank if unpaid) |
| K | Amount Paid | Actual amount received (usually = total, but may differ) |
| L | Status | Formula: Paid / Unpaid / Overdue (see below) |
| M | Notes | Late payment notes, partial payments, etc. |

### Status Formula (Column L)

```
=IF(J2<>"","Paid",IF(TODAY()>I2,"Overdue","Unpaid"))
```

This formula reads: if a payment date has been entered (column J), status is "Paid". If no payment date and today is past the due date, status is "Overdue". Otherwise, status is "Unpaid".

### Conditional Formatting for Status Column

Color-code the Status column for instant visibility:

1. Select the entire Status column (L2:L1000).
2. Go to **Format > Conditional formatting**.
3. Add three rules:
   - Text is exactly `Paid` → Green fill
   - Text is exactly `Unpaid` → Yellow fill
   - Text is exactly `Overdue` → Red fill

---

## Section 10: Payment Tracker Dashboard

The Payment Tracker is a summary view built entirely from formulas that read the Invoice Log.

### Layout

```
  A                         B           C
  +--------------------------+-----------+-----------+
1 | PAYMENT TRACKER          |           |           |
  +--------------------------+-----------+-----------+
3 | Summary                  |           |           |
4 | Total Invoiced (YTD):    |           | [formula] |
5 | Total Collected (YTD):   |           | [formula] |
6 | Outstanding Balance:     |           | [formula] |
7 | Number of Open Invoices: |           | [formula] |
8 | Number of Overdue:       |           | [formula] |
  +--------------------------+-----------+-----------+
10| Aged Receivables         |           |           |
11| Current (not yet due):   |           | [formula] |
12| 1–30 days overdue:       |           | [formula] |
13| 31–60 days overdue:      |           | [formula] |
14| 61–90 days overdue:      |           | [formula] |
15| 90+ days overdue:        |           | [formula] |
  +--------------------------+-----------+-----------+
17| This Month               |           |           |
18| Invoiced this month:     |           | [formula] |
19| Collected this month:    |           | [formula] |
  +--------------------------+-----------+-----------+
```

### Dashboard Formulas

Place these formulas in column C, rows 4–19. All reference the Invoice Log sheet.

**Summary Section:**

| Cell | Formula | What it calculates |
|---|---|---|
| C4 | `=SUM('Invoice Log'!H:H)` | Total of all invoice amounts (YTD) |
| C5 | `=SUMIF('Invoice Log'!L:L,"Paid",'Invoice Log'!K:K)` | Total amount received for paid invoices |
| C6 | `=C4-C5` | Outstanding (invoiced minus collected) |
| C7 | `=COUNTIF('Invoice Log'!L:L,"Unpaid")+COUNTIF('Invoice Log'!L:L,"Overdue")` | Count of all open invoices |
| C8 | `=COUNTIF('Invoice Log'!L:L,"Overdue")` | Count of overdue invoices |

**Aged Receivables:**

These formulas count only unpaid/overdue invoices and bucket them by how many days past due they are.

| Cell | Formula |
|---|---|
| C11 | `=SUMPRODUCT(('Invoice Log'!L$2:L$1000<>"Paid")*('Invoice Log'!I$2:I$1000>=TODAY())*('Invoice Log'!H$2:H$1000))` |
| C12 | `=SUMPRODUCT(('Invoice Log'!L$2:L$1000="Overdue")*(TODAY()-'Invoice Log'!I$2:I$1000>=1)*(TODAY()-'Invoice Log'!I$2:I$1000<=30)*('Invoice Log'!H$2:H$1000))` |
| C13 | `=SUMPRODUCT(('Invoice Log'!L$2:L$1000="Overdue")*(TODAY()-'Invoice Log'!I$2:I$1000>=31)*(TODAY()-'Invoice Log'!I$2:I$1000<=60)*('Invoice Log'!H$2:H$1000))` |
| C14 | `=SUMPRODUCT(('Invoice Log'!L$2:L$1000="Overdue")*(TODAY()-'Invoice Log'!I$2:I$1000>=61)*(TODAY()-'Invoice Log'!I$2:I$1000<=90)*('Invoice Log'!H$2:H$1000))` |
| C15 | `=SUMPRODUCT(('Invoice Log'!L$2:L$1000="Overdue")*(TODAY()-'Invoice Log'!I$2:I$1000>90)*('Invoice Log'!H$2:H$1000))` |

**This Month:**

| Cell | Formula | What it calculates |
|---|---|---|
| C18 | `=SUMPRODUCT((MONTH('Invoice Log'!A$2:A$1000)=MONTH(TODAY()))*(YEAR('Invoice Log'!A$2:A$1000)=YEAR(TODAY()))*('Invoice Log'!H$2:H$1000))` | Total invoiced this calendar month |
| C19 | `=SUMPRODUCT((MONTH('Invoice Log'!J$2:J$1000)=MONTH(TODAY()))*(YEAR('Invoice Log'!J$2:J$1000)=YEAR(TODAY()))*('Invoice Log'!K$2:K$1000))` | Total collected this calendar month |

---

## Section 11: Year-End Summary Sheet

### Layout

The Year-End Summary has two tables: monthly revenue totals and per-client totals.

```
  A              B        C        D        E
  +--------------+---------+---------+---------+---------+
1 | YEAR-END SUMMARY — [year]                            |
  +--------------+---------+---------+---------+---------+
3 | Month         | Invoiced| Collected| Tax    | Net     |
4 | January       | [formula]...                         |
5 | February      | ...                                  |
...
15| December      | ...                                  |
16| TOTAL         | [SUM]   | [SUM]   | [SUM]  | [SUM]   |
  +--------------+---------+---------+---------+---------+
18| Per-Client Summary                                   |
19| Client        | Invoiced| Collected| Unpaid |         |
20| [auto from log]...                                   |
  +--------------+---------+---------+---------+---------+
```

### Monthly Revenue Formulas

For the January row (row 4), with your Invoice Log data in `'Invoice Log'!A:H`:

| Cell | Formula | What it calculates |
|---|---|---|
| B4 | `=SUMPRODUCT((MONTH('Invoice Log'!A$2:A$1000)=1)*(YEAR('Invoice Log'!A$2:A$1000)=YEAR(TODAY()))*('Invoice Log'!H$2:H$1000))` | Total invoiced in January |
| C4 | `=SUMPRODUCT((MONTH('Invoice Log'!J$2:J$1000)=1)*(YEAR('Invoice Log'!J$2:J$1000)=YEAR(TODAY()))*('Invoice Log'!K$2:K$1000))` | Total collected in January |
| D4 | `=SUMPRODUCT((MONTH('Invoice Log'!A$2:A$1000)=1)*(YEAR('Invoice Log'!A$2:A$1000)=YEAR(TODAY()))*('Invoice Log'!G$2:G$1000))` | Tax collected in January |
| E4 | `=B4-D4` | Net revenue (before tax, January) |

Change the month number (the `=1` part) for each subsequent row: February is `=2`, March is `=3`, and so on through December `=12`.

**Totals row (row 16):**
```
=SUM(B4:B15)   =SUM(C4:C15)   =SUM(D4:D15)   =SUM(E4:E15)
```

### Per-Client Summary Formulas

For each client row in the Per-Client table, use SUMIF with the client code:

| Cell | Formula |
|---|---|
| B20 | `=SUMIF('Invoice Log'!C:C,A20,'Invoice Log'!H:H)` (total invoiced for client in A20) |
| C20 | `=SUMIF('Invoice Log'!C:C,A20,'Invoice Log'!K:K)` (total collected) |
| D20 | `=B20-C20` (outstanding balance) |

You can either manually enter client codes in column A, or use a UNIQUE formula (Google Sheets):
```
=UNIQUE('Invoice Log'!C2:C1000)
```
This auto-populates the client list from the Invoice Log without any manual entry.

### Getting the Year Right

The year in the formulas above uses `YEAR(TODAY())` which always refers to the current calendar year. To review a prior year, replace `YEAR(TODAY())` with the year number directly, e.g., `2025`.

---

## Section 12: Print and PDF Export Formatting

### Setting the Print Area in Google Sheets

1. Select the cells you want to print (the invoice area — typically A1:E37 for the Standard template).
2. Go to **View > Set print area** (or use **File > Print** and manually adjust).
3. In the Print dialog:
   - Paper size: **Letter** (US) or **A4** (international)
   - Orientation: **Portrait**
   - Scale: **Fit to width** (this ensures the invoice fits on one page)
   - Margins: **Normal** or **Narrow** if your content is tight

### Setting the Print Area in Excel

1. Select the invoice range (e.g., A1:E37).
2. Go to **Page Layout > Print Area > Set Print Area**.
3. Go to **Page Layout > Page Setup** (click the small arrow in the corner):
   - Paper: Letter or A4
   - Orientation: Portrait
   - Scaling: Fit to 1 page wide x 1 page tall

### Exporting as PDF in Google Sheets

1. Go to **File > Download > PDF document (.pdf)**.
2. In the PDF settings dialog:
   - Export: **Current sheet**
   - Paper size: Letter or A4
   - Page orientation: Portrait
   - Scale: **Fit to page** or **100%**
   - Margins: Narrow
   - Uncheck "Show gridlines" and "Show notes"
   - Check "Repeat frozen rows" if you have frozen header rows
3. Click **Export**.

### Exporting as PDF in Excel

1. Go to **File > Export > Create PDF/XPS**.
2. In the dialog, select **PDF** and click **Options** to confirm the print area is set correctly.
3. Click **Publish**.

Alternatively: **File > Print > Microsoft Print to PDF**.

### Formatting Tips for Clean PDF Output

**Hide helper columns before printing.** If you have columns used only for formulas or references (like a hidden client code column), right-click those column headers and select "Hide column" before exporting to PDF. Unhide them afterward.

**Freeze header rows so they print correctly.** In Google Sheets: View > Freeze > 1 row. In Excel: View > Freeze Panes > Freeze Top Row. This doesn't affect printing directly but ensures headers appear on the screen as expected.

**Remove gridlines from the invoice area.** For a clean, professional look, remove all borders except the ones you intentionally set. Select all cells (Ctrl+A), remove all borders, then reapply only the borders you want around the invoice body.

**Set row heights manually for consistent spacing.** Right-click a row number, select "Resize row," and set a specific pixel height. Standard invoice rows look good at 20–24 pixels height.

**Use a white or light gray header band for the company name section.** Select A1:E4, apply a background color (Format > Fill color). Use hex color `#1a3a5c` for dark navy, `#2d6a4f` for dark green, or `#4a4a4a` for neutral charcoal — all look professional on a printed invoice.

---

## Section 13: Common Questions and Troubleshooting

**Q: My VLOOKUP returns #N/A instead of client information.**
A: The client code in the invoice sheet (cell E12) doesn't match any code in the Clients sheet column A. Check for extra spaces (a common cause) — use `=TRIM(E12)` to clean the code, or format both columns as plain text.

**Q: The Due Date formula keeps showing a date from years ago.**
A: Cell E3 (the invoice date) is probably set to a static date from when the template was created, rather than `=TODAY()`. Click E3 and replace whatever is there with `=TODAY()`.

**Q: My formulas show as text instead of calculating.**
A: The cells are formatted as Text instead of General. Select the affected cells, go to Format > Number > General, then click into each cell and press Enter to force re-evaluation. For bulk fixing: Edit > Find and Replace, find `=`, replace with `=`, check "Match entire cell contents" is OFF.

**Q: How do I send the invoice as a PDF without showing my formulas sheet?**
A: Before exporting, hide any sheets you don't want printed (right-click the tab > Hide sheet). Export the invoice sheet to PDF. Then unhide the sheets afterward (right-click any tab > Unhide).

**Q: Can I have multiple businesses using the same workbook?**
A: Not easily — the Settings sheet and your business info at the top of each invoice template are set up for one business. Create a separate workbook (File > Make a copy) for each business you operate.

**Q: How do I record a partial payment?**
A: In the Invoice Log, enter the partial amount in column K (Amount Paid) and the date received in column J. Change the Notes column to indicate it's partial (e.g., "Partial — $500 of $1,200 received"). Leave the Status formula as-is — it will show "Paid" once column J has any date. You may want to add a "Partial" status option by modifying the formula:
```
=IF(K2>=H2,"Paid",IF(AND(K2>0,K2<H2),"Partial",IF(TODAY()>I2,"Overdue","Unpaid")))
```

**Q: The Aged Receivables totals don't match my expectations.**
A: The aged receivables formulas reference rows 2 through 1000 in the Invoice Log. If your Invoice Log has data beyond row 1000, extend the range (change `1000` to `2000` or higher throughout).

---

## Daily Workflow Summary

**When you complete a project:**

1. Open the workbook and duplicate the appropriate invoice template tab.
2. Type the client code in cell E12 — client info fills in automatically.
3. Add your service description(s) and amounts.
4. Check the invoice number, date, and due date.
5. Export to PDF (File > Download > PDF).
6. Email the PDF to the client.
7. Add a row to the Invoice Log with the invoice details.
8. Increment the counter in Settings!B3.

**When you receive payment:**

1. Find the invoice row in the Invoice Log.
2. Enter today's date in column J and the amount received in column K.
3. The status automatically updates to "Paid."
4. The Payment Tracker and Year-End Summary update immediately.

**At year-end:**

1. Open the Year-End Summary sheet — all monthly totals are already there.
2. Review the Per-Client Summary for outstanding balances.
3. Export the Year-End Summary to PDF for your records or accountant.
4. Make a copy of the workbook before January 1 as your permanent archive (File > Make a copy, name it "Invoice System 2026").
5. Reset the invoice counter in Settings if you want to start fresh numbering for the new year (optional).
