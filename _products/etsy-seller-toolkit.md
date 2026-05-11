# Etsy Seller Toolkit — Shop Management System

> Duplicate this page into your Notion workspace to get started. All databases are pre-linked and formulas are pre-built. Follow the Quick-Start Guide at the bottom before adding real data.

---

## DATABASES

---

### 1. Products

**Purpose:** Master catalog of every product in your shop — pricing, costs, inventory, performance, and true profit margin in one record.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Product Name | Title | Exact listing title on Etsy |
| SKU | Text | Your internal product code — e.g. "CNDL-LAV-8OZ" |
| Category | Select | e.g. Candles / Jewelry / Prints / Clothing / Home Decor / Stickers / Digital / Vintage / Supplies |
| Sub-Category | Text | e.g. "Soy Candles — Seasonal" |
| Status | Select | Active / Inactive / Draft / Sold Out / Discontinued / Seasonal |
| Sales Channel | Multi-select | Etsy / Website / Craft Fair / Wholesale / Amazon Handmade / Other |
| Listing URL | URL | Direct link to your Etsy listing |
| Date Listed | Date | When this product first went live |
| Photos | Number | How many listing photos are uploaded (Etsy allows 10) |
| Retail Price | Number (USD) | What you charge the customer |
| Material Cost | Number (USD) | Raw materials per unit |
| Labor Time (hours) | Number | Time to produce one unit (use decimals: 0.5 = 30 min) |
| Labor Rate | Number (USD) | Your hourly rate for production — e.g. $20/hr |
| Labor Cost | Formula | `prop("Labor Time (hours)") * prop("Labor Rate")` |
| Packaging Cost | Number (USD) | Box, tissue paper, stickers, thank you card per unit |
| Shipping Cost | Number (USD) | Average shipping cost per unit (if you offer free shipping, this is your cost) |
| Etsy Listing Fee | Formula | `0.20` |
| Etsy Transaction Fee | Formula | `prop("Retail Price") * 0.065` |
| Etsy Processing Fee | Formula | `(prop("Retail Price") * 0.03) + 0.25` |
| Offsite Ads Fee | Formula | `if(prop("Offsite Ads Eligible"), prop("Retail Price") * 0.15, 0)` |
| Offsite Ads Eligible | Checkbox | Check if this product has sold via Etsy Offsite Ads |
| Total Etsy Fees | Formula | `prop("Etsy Listing Fee") + prop("Etsy Transaction Fee") + prop("Etsy Processing Fee")` |
| Total Cost | Formula | `prop("Material Cost") + prop("Labor Cost") + prop("Packaging Cost") + prop("Shipping Cost") + prop("Total Etsy Fees")` |
| Profit Per Unit | Formula | `prop("Retail Price") - prop("Total Cost")` |
| Profit Margin % | Formula | `if(prop("Retail Price") > 0, round((prop("Profit Per Unit") / prop("Retail Price")) * 100), 0)` |
| Inventory Count | Number | Current units on hand |
| Reorder Threshold | Number | Minimum stock before you need to reorder/produce more |
| Low Stock Alert | Formula | `if(prop("Inventory Count") <= prop("Reorder Threshold"), "LOW STOCK", if(prop("Inventory Count") == 0, "OUT OF STOCK", "OK"))` |
| Total Units Sold | Rollup | Count of linked Orders |
| Total Revenue | Rollup | Sum of Order Total from linked Orders |
| Average Rating | Number | Average review rating for this product (1-5) |
| Review Count | Number | Total reviews received for this listing |
| Bestseller | Checkbox | Has this product earned an Etsy bestseller badge? |
| Seasonal | Checkbox | Is this a seasonal product? |
| Season | Select | Spring / Summer / Fall / Winter / Holiday / Valentine's / Mother's Day / Back to School |
| Production Notes | Text | Special instructions, supplier info, batch size notes |
| Tags | Multi-select | Best Seller / New / Featured / Clearance / Limited Edition / Custom / Personalized |
| Linked Orders | Relation | -> Orders database |
| Linked Keywords | Relation | -> Keywords database |

**Views:**

- **All Products** — Table, sorted by Category then Product Name
- **Active Listings** — Filter: Status = Active, sorted by Product Name
- **Profit Leaderboard** — Filter: Status = Active, sorted by Profit Margin % descending
- **Low Profit Alert** — Filter: Profit Margin % < 25, Status = Active (products that may need repricing)
- **Low Stock** — Filter: Low Stock Alert = "LOW STOCK" or "OUT OF STOCK"
- **By Category** — Table, grouped by Category, sorted by Total Units Sold descending
- **Seasonal Products** — Filter: Seasonal = true, grouped by Season
- **Bestsellers** — Filter: Bestseller = true
- **Product Cards** — Gallery view, grouped by Status

---

### 2. Orders

**Purpose:** Every sale from receipt to shipment to review. Your fulfillment command center.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Order # | Title | Etsy order number |
| Product | Relation | -> Products database |
| Product Name | Rollup | Product Name from linked Product |
| Customer Name | Text | Buyer's name |
| Customer Email | Email | Optional — for your records |
| Order Date | Date | When the order was placed |
| Ship By Date | Date | Deadline per Etsy's processing time |
| Days Until Ship | Formula | `if(empty(prop("Ship By Date")), "No date", dateBetween(prop("Ship By Date"), now(), "days"))` |
| Shipping Urgency | Formula | `if(prop("Status") == "Shipped" or prop("Status") == "Delivered" or prop("Status") == "Complete", "Done", if(prop("Days Until Ship") < 0, "OVERDUE", if(prop("Days Until Ship") <= 1, "SHIP TODAY", if(prop("Days Until Ship") <= 2, "SHIP SOON", "On Track"))))` |
| Status | Select | Received / In Production / Ready to Ship / Shipped / Delivered / Complete / Cancelled / Refunded / Disputed |
| Quantity | Number | Number of units ordered |
| Order Total | Number (USD) | Total amount paid by customer |
| Shipping Paid | Number (USD) | What the customer paid for shipping (0 if free shipping) |
| Etsy Fees | Formula | `(prop("Order Total") * 0.065) + (prop("Order Total") * 0.03) + 0.25 + 0.20` |
| Net Revenue | Formula | `prop("Order Total") - prop("Etsy Fees")` |
| Personalization | Text | Custom text, color choice, size, or other personalization details |
| Gift | Checkbox | Is this a gift order? |
| Gift Message | Text | Customer's gift message, if any |
| Shipping Method | Select | USPS First Class / USPS Priority / UPS Ground / FedEx / International / Local Pickup |
| Tracking Number | Text | Shipping tracking number |
| Shipped Date | Date | When you actually shipped |
| Delivered Date | Date | When delivery was confirmed |
| Processing Time (days) | Formula | `if(and(not(empty(prop("Shipped Date"))), not(empty(prop("Order Date")))), dateBetween(prop("Shipped Date"), prop("Order Date"), "days"), 0)` |
| Review Received | Checkbox | Has the customer left a review? |
| Review Rating | Select | 5 Stars / 4 Stars / 3 Stars / 2 Stars / 1 Star |
| Review Text | Text | Full text of the review |
| Customer Note | Text | Any note the customer included with the order |
| Internal Notes | Text | Your private notes — production issues, customer communication, etc. |
| Repeat Customer | Checkbox | Has this customer ordered before? |
| Source | Select | Etsy Search / Etsy Ads / Social Media / Direct Link / Offsite Ads / Other |
| Month | Formula | `formatDate(prop("Order Date"), "MMMM YYYY")` |
| Week | Formula | `formatDate(prop("Order Date"), "W")` |

**Views:**

- **All Orders** — Table, sorted by Order Date descending
- **Fulfillment Pipeline** — Kanban, grouped by Status (primary working view)
- **Ship Today** — Filter: Shipping Urgency = "SHIP TODAY" or "OVERDUE", sorted by Ship By Date ascending
- **In Production** — Filter: Status = In Production or Received
- **This Month** — Filter: Order Date is this month, sorted by Order Date descending
- **Revenue by Month** — Table, grouped by Month, with sum of Order Total and Net Revenue
- **Reviews Received** — Filter: Review Received = true, sorted by Review Rating descending
- **By Product** — Table, grouped by Product Name, with count and sum of Order Total
- **Repeat Customers** — Filter: Repeat Customer = true
- **Calendar** — Calendar view, by Ship By Date

---

### 3. Keywords

**Purpose:** Track every SEO keyword you're targeting or monitoring. Your Etsy search optimization command center.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Keyword | Title | The exact search term — e.g. "lavender soy candle" |
| Search Volume | Select | High / Medium / Low / Very Low / Unknown |
| Competition | Select | High / Medium / Low |
| Opportunity Score | Formula | `if(and(or(prop("Search Volume") == "High", prop("Search Volume") == "Medium"), or(prop("Competition") == "Low", prop("Competition") == "Medium")), "HIGH OPPORTUNITY", if(and(prop("Search Volume") == "High", prop("Competition") == "High"), "Competitive", if(prop("Search Volume") == "Low", "Niche", "Standard")))` |
| Category | Select | Match your product categories — e.g. Candles / Jewelry / Prints / etc. |
| Keyword Type | Select | Primary / Long-Tail / Seasonal / Trending / Brand / Competitor |
| Used In Listings | Relation | -> Products database |
| Listing Count | Rollup | Count of linked Products |
| In Title | Checkbox | Is this keyword used in a listing title? |
| In Tags | Checkbox | Is this keyword used in listing tags? |
| In Description | Checkbox | Is this keyword used in a listing description? |
| Ranking Position | Text | Your observed rank for this term — e.g. "Page 1, Row 3" or "Not ranking" |
| Last Checked | Date | When you last searched for this keyword and noted your position |
| Ranking Trend | Select | Improving / Stable / Declining / New / Not Ranking |
| Seasonal | Checkbox | Does this keyword spike at certain times of year? |
| Peak Season | Select | Spring / Summer / Fall / Winter / Holiday / Valentine's / Mother's Day |
| Source | Select | Etsy Search Suggest / eRank / Marmalead / Competitor Analysis / Manual Research |
| Notes | Text | Observations, strategy notes, related keywords to test |
| Priority | Select | Target Now / Watch / Archive |
| Date Added | Date | When you added this keyword to tracking |

**Views:**

- **All Keywords** — Table, sorted by Keyword alphabetically
- **High Opportunity** — Filter: Opportunity Score = "HIGH OPPORTUNITY", sorted by Search Volume
- **By Category** — Table, grouped by Category
- **Target Now** — Filter: Priority = Target Now
- **Seasonal Keywords** — Filter: Seasonal = true, grouped by Peak Season
- **Not Used Yet** — Filter: Listing Count = 0, Priority = Target Now (keywords you should be using but aren't)
- **Ranking Tracker** — Table sorted by Last Checked ascending (shows what needs re-checking)
- **Keyword Board** — Kanban, grouped by Priority

---

### 4. Competitors

**Purpose:** Track competing shops and products to inform your pricing, positioning, and product development.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Competitor Name | Title | Shop name or product listing name |
| Shop URL | URL | Link to their Etsy shop |
| Category | Select | Match your product categories |
| Competing Products | Text | Which of your products compete directly with theirs |
| Their Price Range | Text | e.g. "$18 - $32" |
| Your Price | Text | Your price for the competing product(s) |
| Price Position | Select | We're Higher / Similar / We're Lower |
| Their Review Count | Number | Total reviews on their shop or product |
| Their Average Rating | Number | Their star rating (1-5) |
| Their Bestsellers | Text | Note their bestseller products and estimated prices |
| Their Shipping | Select | Free Shipping / Paid Shipping / Mixed |
| Their Processing Time | Text | e.g. "3-5 business days" |
| Strengths | Text | What they do better than you — be honest |
| Weaknesses | Text | Where you have an advantage |
| Opportunities | Text | Gaps in their offerings you could fill |
| Threats | Text | Ways they could take your market share |
| Photo Quality | Select | Professional / Good / Average / Poor |
| Listing Quality | Select | Excellent / Good / Average / Poor |
| SEO Observations | Text | Keywords they use in titles, tags you've noticed |
| Status | Select | Active Competitor / Watch List / Inactive / New Entrant |
| Last Reviewed | Date | When you last checked their shop |
| Notes | Text | General observations, strategy thoughts |
| Date Added | Date | When you started tracking them |
| Tags | Multi-select | Direct Competitor / Indirect / Price Leader / Quality Leader / New / Growing Fast |

**Views:**

- **All Competitors** — Table, sorted by Status then Competitor Name
- **Active Competitors** — Filter: Status = Active Competitor
- **By Category** — Table, grouped by Category
- **Price Comparison** — Table showing Competitor Name, Their Price Range, Your Price, Price Position
- **SWOT Overview** — Table showing Competitor Name, Strengths, Weaknesses, Opportunities, Threats
- **Needs Review** — Filter: Last Reviewed is more than 30 days ago (time to check again)
- **Competitor Cards** — Gallery view, grouped by Status

---

## DASHBOARD

> Create this as a Notion page that pulls from all four databases using linked views and summary blocks.

### Dashboard Layout

```
+-------------------------------------------------------------+
|  ETSY SHOP HQ — [Your Shop Name]          April 2026         |
+--------------+--------------+--------------+-----------------+
|  Active      |  Orders to   |  Low Stock   |  Monthly        |
|  Listings    |  Ship Today  |  Alerts      |  Revenue        |
|    47        |     3        |     5        |   $1,240        |
+--------------+--------------+--------------+-----------------+
|  FULFILLMENT PIPELINE                                        |
|  [Linked view -> Orders, Kanban grouped by Status]           |
|                                                              |
|  Received    In Production    Ready to Ship    Shipped        |
|  --------    -------------    -------------    --------      |
|  Order card  Order card       Order card       Order card    |
|  Order card  Order card                        Order card    |
+-------------------------------------------------------------+
|  SHIP TODAY / OVERDUE                                        |
|  [Linked view -> Orders, filter: Shipping Urgency =          |
|   SHIP TODAY or OVERDUE, sorted by Ship By Date]             |
+-----------------------------+-------------------------------+
|  TOP PRODUCTS (BY MARGIN)   |  LOW STOCK ALERTS              |
|  [Linked view -> Products,  |  [Linked view -> Products,     |
|   sorted by Profit Margin   |   filter: Low Stock Alert =    |
|   % descending, limit 10]   |   LOW STOCK or OUT OF STOCK]   |
+-----------------------------+-------------------------------+
|  KEYWORD OPPORTUNITIES                                       |
|  [Linked view -> Keywords, filter: Opportunity Score =       |
|   HIGH OPPORTUNITY, Priority = Target Now]                   |
+-------------------------------------------------------------+
|  REVENUE THIS MONTH                                          |
|  [Linked view -> Orders, filter: this month, sum of          |
|   Order Total and Net Revenue]                               |
+-------------------------------------------------------------+
|  RECENT REVIEWS                                              |
|  [Linked view -> Orders, filter: Review Received = true,     |
|   sorted by Order Date descending, limit 5]                  |
+-------------------------------------------------------------+
```

### Key Formula Reference

**Profit Per Unit (Products database):**
```
prop("Retail Price") - (
  prop("Material Cost") +
  prop("Labor Cost") +
  prop("Packaging Cost") +
  prop("Shipping Cost") +
  prop("Etsy Listing Fee") +
  prop("Etsy Transaction Fee") +
  prop("Etsy Processing Fee")
)
```

**Etsy Fee Breakdown (per sale):**
```
Listing Fee:     $0.20 (per listing, renews every 4 months or on sale)
Transaction Fee: 6.5% of item price + shipping
Processing Fee:  3% of order total + $0.25
Offsite Ads:     15% of order total (if sold via Etsy ads, shops <$10K/yr)
                 12% (shops >$10K/yr)
```

**Shipping Urgency (Orders database):**
```
if(
  or(
    prop("Status") == "Shipped",
    prop("Status") == "Delivered",
    prop("Status") == "Complete"
  ),
  "Done",
  if(
    prop("Days Until Ship") < 0,
    "OVERDUE",
    if(
      prop("Days Until Ship") <= 1,
      "SHIP TODAY",
      if(
        prop("Days Until Ship") <= 2,
        "SHIP SOON",
        "On Track"
      )
    )
  )
)
```

**Keyword Opportunity Score (Keywords database):**
```
if(
  and(
    or(prop("Search Volume") == "High", prop("Search Volume") == "Medium"),
    or(prop("Competition") == "Low", prop("Competition") == "Medium")
  ),
  "HIGH OPPORTUNITY",
  if(
    and(prop("Search Volume") == "High", prop("Competition") == "High"),
    "Competitive",
    if(
      prop("Search Volume") == "Low",
      "Niche",
      "Standard"
    )
  )
)
```

---

## LISTING OPTIMIZATION CHECKLIST

Use this checklist every time you create or review a listing. Open the checklist alongside the Etsy listing editor.

### Title (140 characters max)
- [ ] Primary keyword appears in the first 40 characters
- [ ] Secondary keywords included naturally
- [ ] No keyword stuffing — title reads like a human wrote it
- [ ] Most important descriptors first (what it is + key feature + audience)
- [ ] Example structure: "[Product Type] — [Key Feature] — [Material/Style] — [Use Case/Gift For]"

### Tags (13 tags max, 20 characters each)
- [ ] All 13 tag slots are used
- [ ] Primary keyword is a tag
- [ ] Long-tail variations are included (e.g., "soy candle gift" not just "candle")
- [ ] Seasonal tags included if applicable
- [ ] No single-word tags (multi-word phrases perform better)
- [ ] Tags match what your Keywords database shows as high-opportunity

### Photos (up to 10)
- [ ] Minimum 5 photos, ideally all 10 slots used
- [ ] First photo (thumbnail) is clean, bright, and product-focused
- [ ] At least 1 lifestyle/in-use photo
- [ ] At least 1 scale/size reference photo
- [ ] At least 1 detail/close-up photo
- [ ] Photos are well-lit with consistent style
- [ ] If applicable: show packaging or gift-ready presentation
- [ ] Video included (Etsy allows 5-15 second video)

### Description
- [ ] First sentence answers: what is it and why should someone buy it?
- [ ] Key features and dimensions are listed clearly
- [ ] Materials/ingredients are specified
- [ ] Care instructions included if applicable
- [ ] Shipping information and processing time stated
- [ ] Return/exchange policy referenced
- [ ] Keywords appear naturally in the description (helps Etsy SEO)

### Pricing
- [ ] Price entered in Products database with full cost breakdown
- [ ] Profit margin is above 30% (minimum viable for sustainability)
- [ ] Competitor pricing checked in Competitors database
- [ ] Shipping cost is accurate (or accounted for in price if free shipping)
- [ ] Sale/coupon strategy considered

---

## QUICK-START GUIDE

### Step 1 — Enter Your Products (15 minutes)
- Open the **Products** database and add your current active listings
- For each product, enter: Product Name, SKU, Category, Retail Price, Material Cost, Labor Time, Labor Rate, Packaging Cost, and Shipping Cost
- The profit calculations will populate automatically
- Set Inventory Count and Reorder Threshold for each product
- Link your Etsy listing URL for quick access

### Step 2 — Enter Recent Orders (10 minutes)
- Open the **Orders** database and enter your last 10-15 orders
- Link each order to its Product
- Set the Status for each order (most recent ones will be in various pipeline stages)
- For shipped orders, enter the Shipped Date and Tracking Number
- For completed orders, note any reviews received

### Step 3 — Research Your Keywords (10 minutes)
- Open the **Keywords** database and enter the 10-15 most important keywords for your shop
- Use Etsy search suggestions, eRank, or Marmalead to estimate Search Volume and Competition
- Link each keyword to the Products that target it
- Set Priority: "Target Now" for keywords you're actively optimizing for

### Step 4 — Log Your Competitors (5 minutes)
- Open the **Competitors** database and add 3-5 shops or products that compete directly with yours
- Note their pricing, review counts, and any quick observations about their strengths
- Set a calendar reminder to review each competitor monthly

### Step 5 — Set Up Your Dashboard
- Pin the Dashboard page to your Notion sidebar
- This is your daily operations center — open it every morning

### Step 6 — Establish Your Daily Routine

**Every morning (5 minutes):**

- Open the Dashboard
- Check "Ship Today" — fulfill any orders due today
- Check "Low Stock Alerts" — reorder materials or start production if needed

**Every time you receive an order:**

- Add it to the Orders database
- Link it to the Product
- Set Status to "Received"
- Move it through the pipeline as you produce, pack, and ship

**Weekly (15 minutes, pick a day):**

- Review your Profit Leaderboard — are your best products getting enough visibility?
- Check "Low Profit Alert" — any products that need repricing?
- Add any new keywords you've discovered to the Keywords database
- Review your revenue for the week

**Monthly (30 minutes):**

- Review each active competitor — update pricing, review counts, and observations
- Run through the Listing Optimization Checklist on your top 5 products
- Check seasonal keyword opportunities for the upcoming month
- Review your overall revenue, margins, and growth trends

### Pro Tips

- Use the "Profit Leaderboard" view to identify your most profitable products — then create more variations of those
- Track your processing time: the Processing Time formula in Orders reveals how long you actually take versus your listed processing time
- When a product's Profit Margin % drops below 25%, either raise the price or reduce costs — don't ignore it
- Use the Competitors database proactively: before launching a new product, research what's already selling in that category
- Log seasonal keywords 2-3 months before the season — Etsy's algorithm favors listings that have been live and gathering data before peak season
- If a keyword shows "Not Ranking" consistently, check if it's in your title and tags, and if your listing has enough sales and reviews to compete for that term
- Review your "Source" data in Orders monthly — if most sales come from Etsy Search, double down on SEO; if from Social Media, invest more in content marketing
