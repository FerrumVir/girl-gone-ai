# Small Business Inventory Tracker — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Track stock levels, manage SKUs, get reorder alerts, and monitor costs all in one place.

---

> **SETUP GUIDE — Get Running in 20 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 7 tabs/sheets and name them: Product Catalog, Stock Levels, Stock Movements, Purchase Orders, Supplier Directory, Reports, Dashboard
> 3. Copy each section below into its corresponding sheet
> 4. Enter the formulas as documented (all formulas are marked with `FORMULA:`)
> 5. Start by entering your product catalog with current stock counts
> 6. Set reorder points for each product based on your sales velocity
>
> **Tip:** Update stock levels after every sale or shipment received. If daily updates aren't possible, do a weekly stock count — accuracy prevents overselling and stockouts.

---

---

# SHEET 1: PRODUCT CATALOG

> Master list of every product you carry. One row per SKU.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SKU** | **Product Name** | **Category** | **Variant** | **Unit Cost** | **Selling Price** | **Margin %** | **Weight** | **Dimensions** | **Barcode/UPC** | **Primary Supplier** | **Status** | **Notes** |

## Status (Dropdown)
- Active
- Discontinued
- Seasonal
- Coming Soon
- Clearance

## SKU Format Guide

| Pattern | Example | Description |
|---------|---------|-------------|
| CAT-PROD-VAR | APP-TSHIRT-BLK-M | Category-Product-Color-Size |
| DEPT-NUM | HW-00142 | Department-Sequential Number |
| BRAND-STYLE | NK-AF1-WHT-10 | Brand-Style-Color-Size |

---

## Sample Entries

| SKU | Product Name | Category | Variant | Unit Cost | Selling Price | Margin % | Weight | Dimensions | Barcode | Supplier | Status | Notes |
|-----|-------------|----------|---------|-----------|--------------|----------|--------|-----------|---------|----------|--------|-------|
| CN-001-NAT | Soy Candle | Candles | Natural / 8oz | $4.50 | $18.00 | 75% | 12oz | 3x3x4 in | 123456789012 | Wax Supply Co | Active | Best seller |
| CN-002-LAV | Soy Candle | Candles | Lavender / 8oz | $4.75 | $18.00 | 74% | 12oz | 3x3x4 in | 123456789013 | Wax Supply Co | Active | |
| SP-001-EUC | Room Spray | Sprays | Eucalyptus / 4oz | $2.80 | $12.00 | 77% | 5oz | 2x2x6 in | 123456789014 | Essential Oils Inc | Active | |
| GF-001-SET | Gift Set | Bundles | Candle + Spray | $7.30 | $28.00 | 74% | 1lb | 8x6x4 in | 123456789015 | — | Seasonal | Holiday set |

`FORMULA: Margin % = (Selling Price - Unit Cost) / Selling Price * 100`

---

---

# SHEET 2: STOCK LEVELS

> Real-time inventory status for every SKU. This is your daily reference sheet.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| **SKU** | **Product Name** | **Current Stock** | **Reserved/Committed** | **Available** | **Reorder Point** | **Reorder Qty** | **Max Stock** | **Stock Status** | **Days of Stock Left** | **Last Updated** |

---

## Stock Status Logic

| Status | Condition | Color Code |
|--------|-----------|-----------|
| IN STOCK | Available > Reorder Point | Green |
| LOW STOCK | Available <= Reorder Point AND Available > 0 | Yellow |
| OUT OF STOCK | Available = 0 | Red |
| OVERSTOCK | Available > Max Stock | Blue |
| ON ORDER | Available = 0 AND PO exists | Orange |

`FORMULA: Available = Current Stock - Reserved`
`FORMULA: Stock Status = IF(E2=0, "OUT OF STOCK", IF(E2<=F2, "LOW STOCK", IF(E2>H2, "OVERSTOCK", "IN STOCK")))`
`FORMULA: Days of Stock Left = Available / Average Daily Sales`

---

## Sample Entries

| SKU | Product | Current | Reserved | Available | Reorder Pt | Reorder Qty | Max | Status | Days Left | Updated |
|-----|---------|---------|----------|-----------|-----------|-------------|-----|--------|-----------|---------|
| CN-001-NAT | Soy Candle Natural | 45 | 8 | 37 | 20 | 50 | 100 | IN STOCK | 18 | 2026-01-15 |
| CN-002-LAV | Soy Candle Lavender | 12 | 3 | 9 | 15 | 50 | 80 | LOW STOCK | 6 | 2026-01-15 |
| SP-001-EUC | Room Spray Eucalyptus | 0 | 0 | 0 | 10 | 30 | 60 | OUT OF STOCK | 0 | 2026-01-15 |
| GF-001-SET | Gift Set | 85 | 0 | 85 | 10 | 20 | 50 | OVERSTOCK | 170 | 2026-01-15 |

---

## Reorder Alerts (Auto-Generated)

| Priority | SKU | Product | Available | Reorder Point | Suggested Order Qty | Est. Cost | Supplier |
|----------|-----|---------|-----------|--------------|--------------------:|-----------|----------|
| URGENT | | | | | | $ | |
| URGENT | | | | | | $ | |
| WARNING | | | | | | $ | |
| WARNING | | | | | | $ | |

`FORMULA: Priority = IF(Available=0, "URGENT", IF(Available<=Reorder_Point, "WARNING", ""))`
`FORMULA: Suggested Order Qty = Reorder Qty (or Max Stock - Available, whichever strategy you prefer)`

---

---

# SHEET 3: STOCK MOVEMENTS

> Log every stock change — receiving, sales, adjustments, returns, transfers.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| **Date** | **SKU** | **Product Name** | **Movement Type** | **Quantity** | **Reference #** | **From Location** | **To Location** | **Reason** | **Entered By** |

## Movement Type (Dropdown)
- Received (Purchase Order)
- Sold (Order)
- Returned (Customer Return)
- Damaged
- Shrinkage/Loss
- Adjustment (Count Correction)
- Transfer (Between Locations)
- Reserved (Committed to Order)
- Unreserved (Order Cancelled)

---

## Sample Entries

| Date | SKU | Product | Type | Qty | Reference | From | To | Reason | By |
|------|-----|---------|------|-----|-----------|------|-----|--------|-----|
| 2026-01-10 | CN-001-NAT | Soy Candle Natural | Received | +50 | PO-2026-003 | Supplier | Warehouse | Restock | Admin |
| 2026-01-11 | CN-001-NAT | Soy Candle Natural | Sold | -3 | ORD-1045 | Warehouse | Customer | Online order | System |
| 2026-01-12 | CN-002-LAV | Soy Candle Lavender | Damaged | -2 | — | Warehouse | Waste | Broken in transit | Admin |
| 2026-01-12 | SP-001-EUC | Room Spray Eucalyptus | Returned | +1 | RET-0089 | Customer | Warehouse | Wrong scent | Admin |
| 2026-01-13 | CN-001-NAT | Soy Candle Natural | Adjustment | +3 | ADJ-015 | — | Warehouse | Count correction | Admin |

---

## Movement Summary (Monthly)

| Month | Received | Sold | Returned | Damaged | Adjustments | Net Change |
|-------|----------|------|----------|---------|-------------|-----------|
| January | | | | | | |
| February | | | | | | |
| March | | | | | | |
| April | | | | | | |
| May | | | | | | |
| June | | | | | | |

`FORMULA: Net Change = Received + Returned + Adjustments - Sold - Damaged`
`FORMULA: Each cell = SUMIFS(Quantity, Month, [month], Movement_Type, [type])`

---

---

# SHEET 4: PURCHASE ORDERS

> Track orders to suppliers from creation through delivery.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| **PO Number** | **Supplier** | **Date Ordered** | **Expected Delivery** | **Actual Delivery** | **Status** | **Total Amount** | **Payment Status** | **Payment Terms** | **Tracking #** | **Notes** |

## PO Status (Dropdown)
- Draft
- Submitted
- Confirmed
- Shipped
- Partially Received
- Received
- Cancelled
- Disputed

## Payment Status (Dropdown)
- Not Yet Due
- Due
- Paid
- Overdue
- Partial

---

## PO Line Items (Sub-Table)

| PO Number | SKU | Product | Qty Ordered | Unit Cost | Line Total | Qty Received | Qty Outstanding |
|-----------|-----|---------|-------------|-----------|-----------|--------------|----------------|
| PO-2026-001 | CN-001-NAT | Soy Candle Natural | 50 | $4.50 | $225.00 | 50 | 0 |
| PO-2026-001 | CN-002-LAV | Soy Candle Lavender | 50 | $4.75 | $237.50 | 48 | 2 |
| PO-2026-002 | SP-001-EUC | Room Spray Eucalyptus | 30 | $2.80 | $84.00 | 0 | 30 |

`FORMULA: Line Total = Qty Ordered * Unit Cost`
`FORMULA: Qty Outstanding = Qty Ordered - Qty Received`

---

## Sample PO Summary

| PO # | Supplier | Ordered | Expected | Status | Amount | Payment |
|------|----------|---------|----------|--------|--------|---------|
| PO-2026-001 | Wax Supply Co | 2026-01-02 | 2026-01-12 | Received | $462.50 | Paid |
| PO-2026-002 | Essential Oils Inc | 2026-01-10 | 2026-01-20 | Shipped | $84.00 | Not Yet Due |
| PO-2026-003 | Wax Supply Co | 2026-01-15 | 2026-01-25 | Confirmed | $350.00 | Not Yet Due |

---

---

# SHEET 5: SUPPLIER DIRECTORY

> Contact info and performance tracking for all suppliers.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| **Supplier Name** | **Contact Person** | **Email** | **Phone** | **Website** | **Products Supplied** | **Payment Terms** | **Lead Time (days)** | **MOQ** | **Rating (1-5)** | **Notes** |

---

## Sample Entries

| Supplier | Contact | Email | Phone | Website | Products | Terms | Lead Time | MOQ | Rating | Notes |
|----------|---------|-------|-------|---------|----------|-------|-----------|-----|--------|-------|
| Wax Supply Co | Sarah Johnson | sarah@waxsupply.com | 555-0101 | waxsupply.com | Candles, wax, wicks | Net 30 | 10 days | 50 units | 4.5 | Reliable, good quality |
| Essential Oils Inc | Mark Chen | mark@essoils.com | 555-0202 | essoils.com | Room sprays, oils | COD | 8 days | 30 units | 4.0 | Fast shipping |
| PackRight | Lisa Torres | lisa@packright.com | 555-0303 | packright.com | Boxes, labels, bags | Net 15 | 5 days | 100 pcs | 3.5 | Minimum order increasing |

---

## Supplier Performance Log

| Date | Supplier | PO # | On Time? | Quality Issue? | Issue Description | Resolved? |
|------|----------|------|----------|---------------|-------------------|-----------|
| | | | Yes/No | Yes/No | | Yes/No |
| | | | Yes/No | Yes/No | | Yes/No |

---

## Supplier Scorecard

| Supplier | On-Time Rate | Quality Rate | Communication | Price Competitiveness | Overall Score |
|----------|-------------|-------------|---------------|----------------------|--------------|
| Wax Supply Co | % | % | /5 | /5 | /20 |
| Essential Oils Inc | % | % | /5 | /5 | /20 |
| PackRight | % | % | /5 | /5 | /20 |

`FORMULA: On-Time Rate = POs Delivered On Time / Total POs * 100`
`FORMULA: Quality Rate = POs Without Issues / Total POs * 100`

---

---

# SHEET 6: REPORTS

> Pre-built report templates that auto-calculate from your data.

---

## Inventory Valuation Report

| SKU | Product | Current Stock | Unit Cost | **Total Value** | % of Total Inventory |
|-----|---------|--------------|-----------|-----------------|---------------------|
| | | | $ | $ | % |
| | | | $ | $ | % |
| | | | $ | $ | % |
| **TOTAL** | | | | **$** | **100%** |

`FORMULA: Total Value = Current Stock * Unit Cost`
`FORMULA: % of Total = Item Value / Sum of All Values * 100`

---

## Stock Turnover Report (Monthly)

| SKU | Product | Avg Stock | Units Sold | Turnover Rate | Days to Sell |
|-----|---------|-----------|-----------|--------------|-------------|
| | | | | | |
| | | | | | |
| **AVERAGE** | | | | | |

`FORMULA: Turnover Rate = Units Sold / Average Stock`
`FORMULA: Days to Sell = 30 / Turnover Rate`

---

## Dead Stock Report (Items Not Sold in 60+ Days)

| SKU | Product | Current Stock | Last Sale Date | Days Since Sale | Value Tied Up | Action Needed |
|-----|---------|--------------|---------------|----------------|--------------|--------------|
| | | | | | $ | Discount / Bundle / Liquidate |
| | | | | | $ | |
| **TOTAL** | | | | | **$** | |

`FORMULA: Days Since Sale = TODAY() - Last Sale Date`

---

## Shrinkage Report

| Month | Expected Stock (system) | Actual Count | Variance | Shrinkage % | Value Lost |
|-------|------------------------|-------------|----------|-------------|-----------|
| January | | | | % | $ |
| February | | | | % | $ |
| March | | | | % | $ |

`FORMULA: Variance = Expected - Actual`
`FORMULA: Shrinkage % = Variance / Expected * 100`
`FORMULA: Value Lost = Variance * Unit Cost`

---

## Best Sellers Report (Monthly)

| Rank | SKU | Product | Units Sold | Revenue | Margin | Stock Remaining | Reorder? |
|------|-----|---------|-----------|---------|--------|----------------|----------|
| 1 | | | | $ | % | | Yes/No |
| 2 | | | | $ | % | | Yes/No |
| 3 | | | | $ | % | | Yes/No |
| 4 | | | | $ | % | | Yes/No |
| 5 | | | | $ | % | | Yes/No |

---

---

# SHEET 7: DASHBOARD

> At-a-glance inventory health metrics.

---

## Inventory Overview

| Metric | Value |
|--------|-------|
| Total SKUs (Active) | |
| Total Units in Stock | |
| Total Inventory Value | $ |
| Items In Stock | |
| Items Low Stock | |
| Items Out of Stock | |
| Items Overstock | |
| Open Purchase Orders | |

---

## Key Performance Indicators

| KPI | This Month | Last Month | Change | Target |
|-----|-----------|-----------|--------|--------|
| Inventory Turnover Rate | | | | |
| Stockout Rate | % | % | | <5% |
| Shrinkage Rate | % | % | | <2% |
| Order Fill Rate | % | % | | >95% |
| Avg Days to Sell | | | | |
| Dead Stock % | % | % | | <10% |

---

## Alerts

| Priority | Alert | SKU | Action Required |
|----------|-------|-----|-----------------|
| URGENT | Out of Stock | | Reorder immediately |
| URGENT | Out of Stock | | Reorder immediately |
| WARNING | Low Stock | | Place order this week |
| WARNING | Low Stock | | Place order this week |
| INFO | Overstock | | Consider promotion |
| INFO | Dead Stock | | Review for clearance |

---

## Monthly Inventory Value Trend

| Month | Total Units | Total Value | Change vs. Prior | COGS (month) |
|-------|-----------|-------------|-----------------|-------------|
| January | | $ | $ | $ |
| February | | $ | $ | $ |
| March | | $ | $ | $ |
| April | | $ | $ | $ |
| May | | $ | $ | $ |
| June | | $ | $ | $ |

---

---

# FORMULA REFERENCE GUIDE

---

## Stock Level Formulas

**Available Stock:**
```
=Current_Stock - Reserved
```

**Stock Status:**
```
=IF(Available=0, "OUT OF STOCK", IF(Available<=Reorder_Point, "LOW STOCK", IF(Available>Max_Stock, "OVERSTOCK", "IN STOCK")))
```

**Days of Stock:**
```
=Available / AVERAGEIFS(Sold_Qty, SKU_Col, This_SKU, Date_Col, ">="&TODAY()-30) * 30
```

## Valuation

**Total Inventory Value:**
```
=SUMPRODUCT(Stock_Levels!C:C, Product_Catalog!E:E)
```

**Turnover Rate:**
```
=Units_Sold_This_Month / ((Beginning_Stock + Ending_Stock) / 2)
```

## Reorder Logic

**Auto Reorder Alert:**
```
=IF(Available <= Reorder_Point, "REORDER: "&Reorder_Qty&" units from "&Supplier, "")
```

## Purchase Orders

**PO Total:**
```
=SUMIFS(Line_Total, PO_Number, This_PO)
```

**Outstanding Qty:**
```
=Qty_Ordered - Qty_Received
```

---

> **NOTE:** This inventory system works for businesses with up to ~500 SKUs in Google Sheets. For larger catalogs or multi-location businesses with high transaction volume, consider dedicated inventory software. This spreadsheet is ideal for small businesses, Etsy sellers, local retail, and early-stage e-commerce operations.
