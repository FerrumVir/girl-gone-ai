# Meal Prep Master Planner — Notion Template

> Duplicate this page into your Notion workspace to get started. All five databases are pre-linked with macro calculations, grocery auto-generation from meal plans, and batch cooking workflow scheduling built in. Read the Quick-Start Guide at the bottom before entering real data.

---

## DATABASES

---

### 1. Recipes

**Purpose:** Your personal recipe library with full nutritional data, ingredient lists, and prep details. Every recipe can be dropped into a weekly meal plan and automatically generates its ingredients on the grocery list.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Recipe Name | Title | Dish name |
| Category | Select | Breakfast / Lunch / Dinner / Snack / Side / Sauce / Dessert / Drink / Base (rice, grains) |
| Cuisine | Select | American / Mexican / Italian / Asian / Mediterranean / Indian / Thai / Japanese / Korean / French / Middle Eastern / Other |
| Protein Source | Select | Chicken / Beef / Pork / Fish / Shrimp / Tofu / Tempeh / Beans / Eggs / None |
| Dietary Tags | Multi-select | Vegetarian / Vegan / Gluten-Free / Dairy-Free / Keto / Paleo / Low-Carb / High-Protein / Low-Sodium / Nut-Free / Whole30 / Kid-Friendly |
| Servings | Number | How many servings this recipe makes |
| Prep Time (min) | Number | Hands-on preparation time |
| Cook Time (min) | Number | Cooking/baking time |
| Total Time (min) | Formula | `prop("Prep Time (min)") + prop("Cook Time (min)")` |
| Total Time Display | Formula | `if(prop("Total Time (min)") < 60, format(prop("Total Time (min)")) + " min", format(floor(prop("Total Time (min)") / 60)) + "h " + format(mod(prop("Total Time (min)"), 60)) + "m")` |
| Difficulty | Select | Easy / Medium / Hard |
| Calories (per serving) | Number | Total calories |
| Protein (g) | Number | Grams of protein per serving |
| Carbs (g) | Number | Grams of carbohydrates per serving |
| Fat (g) | Number | Grams of fat per serving |
| Fiber (g) | Number | Grams of fiber per serving |
| Macro Breakdown | Formula | `"P:" + format(prop("Protein (g)")) + "g \| C:" + format(prop("Carbs (g)")) + "g \| F:" + format(prop("Fat (g)")) + "g \| " + format(prop("Calories (per serving)")) + " cal"` |
| Protein % | Formula | `if(prop("Calories (per serving)") == 0, 0, round(prop("Protein (g)") * 4 / prop("Calories (per serving)") * 100))` |
| Ingredients | Text | Full ingredient list with quantities |
| Instructions | Text | Step-by-step cooking instructions |
| Equipment Needed | Multi-select | Oven / Stovetop / Slow Cooker / Instant Pot / Air Fryer / Blender / Sheet Pan / Grill / No Cook / Microwave |
| Batch Friendly | Checkbox | Can this be doubled/tripled easily? |
| Freezer Friendly | Checkbox | Freezes and reheats well? |
| Freezer Life | Select | 1 week / 2 weeks / 1 month / 2 months / 3 months / 6 months / Does Not Freeze |
| Reheat Method | Select | Microwave / Oven / Stovetop / Air Fryer / No Reheat Needed |
| Storage Container | Select | Glass Container / Plastic Container / Zip Bag / Mason Jar / Wrap / Freezer Bag |
| Rating | Select | 5 Stars / 4 Stars / 3 Stars / 2 Stars / 1 Star / Not Yet Rated |
| Times Made | Number | How many times you've cooked this |
| Last Made | Date | Most recent preparation date |
| Family Approval | Select | Everyone Loves / Most Like / Mixed / Picky Eaters Reject / New |
| Source | Text | Where the recipe came from (cookbook, website, family) |
| Source URL | URL | Link to original recipe |
| Photo | Files & media | Photo of the finished dish |
| Linked Meal Plans | Relation | -> Weekly Meal Plans |
| Cost Per Serving | Number (USD) | Estimated cost per serving |
| Total Cost | Formula | `prop("Cost Per Serving") * prop("Servings")` |
| Notes | Text | Tips, substitutions, what worked |
| Tags | Multi-select | Quick / Weeknight / Weekend / Comfort Food / Healthy / Indulgent / Crowd Pleaser / Meal Prep Star / One Pot / Sheet Pan / No Cook |

**Views:**

- **All Recipes** — Table, sorted by Recipe Name
- **By Category** — Table, grouped by Category
- **Quick Meals (< 30 min)** — Filter: Total Time (min) < 30
- **High Protein** — Filter: Protein (g) > 30, sorted by Protein descending
- **Batch Cooking** — Filter: Batch Friendly = true AND Freezer Friendly = true
- **By Cuisine** — Table, grouped by Cuisine
- **Favorites** — Filter: Rating = 5 Stars or 4 Stars
- **Family Approved** — Filter: Family Approval = Everyone Loves
- **Keto** — Filter: Dietary Tags contains Keto
- **Vegetarian** — Filter: Dietary Tags contains Vegetarian
- **Not Made Recently** — Sorted by Last Made ascending (rediscover old favorites)
- **By Equipment** — Table, grouped by Equipment Needed
- **Recipe Cards** — Gallery with Photo, showing Macro Breakdown and Total Time Display

---

### 2. Weekly Meal Plans

**Purpose:** Plan your meals for each week. Assigns recipes to specific days and meal slots. Once a plan is set, the grocery list generates from it. One entry per meal slot per day.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Meal Entry | Title | "[Day] — [Meal Type]" (e.g., "Monday — Lunch") |
| Week | Select | Current Week / Next Week / Week of [date] (or use a text date) |
| Week Start Date | Date | Monday of the planned week |
| Day | Select | Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday |
| Meal Type | Select | Breakfast / AM Snack / Lunch / PM Snack / Dinner / Evening Snack |
| Recipe | Relation | -> Recipes database |
| Recipe Name | Rollup | From Recipe relation |
| Custom Meal | Text | If not from recipe database (e.g., "Leftovers", "Eating out") |
| Servings Planned | Number | How many servings to prepare |
| Calories | Rollup | Calories per serving from linked Recipe |
| Protein | Rollup | Protein from linked Recipe |
| Carbs | Rollup | Carbs from linked Recipe |
| Fat | Rollup | Fat from linked Recipe |
| Prep Required | Select | Full Cook / Reheat Only / No Prep / Assemble / Thaw + Reheat |
| Prep Day | Select | Sunday / Monday / Tuesday / Wednesday / Same Day |
| Prepped | Checkbox | Has this been prepared? |
| Batch Source | Text | "From Sunday batch" or which batch session |
| Notes | Text | Substitutions, portion adjustments |

**Views:**

- **This Week** — Table, filtered to current week, grouped by Day, sorted by Meal Type
- **Next Week** — Table, filtered to next week
- **By Day** — Board, grouped by Day
- **Prep Schedule** — Filter: Prep Required != No Prep, grouped by Prep Day
- **Not Prepped** — Filter: Prepped = false AND Prep Day has passed
- **Dinner Plan** — Filter: Meal Type = Dinner, this week
- **Calendar** — Calendar view by Week Start Date
- **Macro Summary** — Table showing Day, total Calories/Protein/Carbs/Fat per day

---

### 3. Grocery List

**Purpose:** Auto-generated (or manually built) grocery list organized by store section. Pulls ingredients from the weekly meal plan's recipes and consolidates quantities. Check items off as you shop.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Item | Title | Ingredient name |
| Quantity | Text | Amount needed (e.g., "2 lbs", "3 cups", "1 bunch") |
| Store Section | Select | Produce / Meat & Seafood / Dairy / Frozen / Bakery / Deli / Canned & Dry / Grains & Pasta / Condiments & Sauces / Spices / Snacks / Beverages / Health & Beauty / Household / Other |
| Purchased | Checkbox | Got it! |
| Week | Date | Which week's plan this is for |
| Source Recipe | Relation | -> Recipes database (which recipe needs this) |
| Recipe Name | Rollup | From Source Recipe relation |
| Priority | Select | Essential / Flexible / Optional (nice to have) |
| Estimated Cost | Number (USD) | Approximate cost |
| Actual Cost | Number (USD) | What you actually paid |
| Store | Select | Primary Store / Costco / Trader Joe's / Specialty / Online / Any |
| Have at Home | Checkbox | Already in pantry/fridge (skip buying) |
| Substitution OK | Text | Acceptable alternatives |
| Organic | Checkbox | Buy organic for this item? |
| Notes | Text | Brand preference, size, specific variety |
| Tags | Multi-select | Staple / Seasonal / Sale Item / Bulk / Perishable / Pantry |

**Views:**

- **Shopping List** — Filter: Purchased = false AND Have at Home = false, grouped by Store Section (MAIN SHOPPING VIEW)
- **By Store** — Table, grouped by Store
- **All Items** — Table, sorted by Store Section
- **Already Have** — Filter: Have at Home = true (don't buy these)
- **Purchased** — Filter: Purchased = true (for cost tracking)
- **By Recipe** — Table, grouped by Recipe Name (see what each recipe needs)
- **Budget View** — Table showing Estimated Cost and Actual Cost totals
- **Staples** — Filter: Tags contains Staple (recurring items to always keep stocked)

---

### 4. Batch Cooking Workflow

**Purpose:** Structured batch cooking sessions with time-blocked schedules. Plans what to cook in what order for maximum efficiency — parallel tasks, oven scheduling, and cooling times all accounted for.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Session Name | Title | "Batch Cook — [Date]" or theme (e.g., "Sunday Protein Prep") |
| Date | Date | When this session happens |
| Total Duration (hr) | Number | Expected total time |
| Recipes to Prep | Relation | -> Recipes database |
| Recipe Count | Rollup | Count of Recipes to Prep |
| Status | Select | Planned / In Progress / Completed / Skipped |
| Session Type | Select | Full Week Prep / Protein Only / Grains & Veg / Breakfast Prep / Snack Prep / Freezer Meals |
| Step 1 | Text | First task with time estimate |
| Step 2 | Text | Second task |
| Step 3 | Text | Third task |
| Step 4 | Text | Fourth task |
| Step 5 | Text | Fifth task |
| Step 6 | Text | Sixth task |
| Step 7 | Text | Seventh task |
| Step 8 | Text | Eighth task |
| Parallel Tasks | Text | What can happen simultaneously (e.g., "While rice cooks, chop vegetables") |
| Oven Schedule | Text | When oven is used and at what temp (prevents conflicts) |
| Equipment Needed | Multi-select | Oven / Stovetop / Instant Pot / Slow Cooker / Air Fryer / Sheet Pans / Cutting Board / Blender / Food Processor |
| Containers Needed | Text | How many and what type of containers to have ready |
| Grocery Complete | Checkbox | All ingredients purchased? |
| Meals Produced | Number | Total servings/meals this session yields |
| Cost Per Meal | Formula | `if(prop("Meals Produced") == 0, 0, round(prop("Total Session Cost") / prop("Meals Produced") * 100) / 100)` |
| Total Session Cost | Number (USD) | Total ingredient cost for this batch |
| Time Per Meal | Formula | `if(prop("Meals Produced") == 0, 0, round(prop("Total Duration (hr)") * 60 / prop("Meals Produced")))` |
| Lessons Learned | Text | What to do differently next time |
| Rating | Select | Excellent / Good / OK / Rough / Disaster |
| Photo | Files & media | Photo of prepped containers |
| Tags | Multi-select | Sunday Prep / Weeknight Quick / Freezer Stock / Holiday Prep |

**Views:**

- **Upcoming** — Filter: Status = Planned, sorted by Date ascending
- **All Sessions** — Table, sorted by Date descending
- **Completed** — Filter: Status = Completed, sorted by Date descending
- **By Type** — Table, grouped by Session Type
- **Calendar** — Calendar view by Date
- **Best Sessions** — Filter: Rating = Excellent (replicate these)

### Sample Batch Cook Schedule (Sunday, 2.5 hours)

```
TIME    TASK                           PARALLEL TASK
0:00    Preheat oven to 400F          Dice all vegetables
0:10    Season chicken thighs          Rice in Instant Pot (set & forget)
0:15    Chicken in oven (25 min)       Prep overnight oats x5
0:25    -                              Chop salad veg for weekday lunches
0:35    Start ground turkey            Overnight oats in fridge
        on stovetop
0:40    Flip chicken in oven           Continue ground turkey
0:45    Roast vegetables (20 min)      Portion ground turkey into containers
0:55    Check rice (should be done)    -
1:00    Chicken out, rest 5 min        Hard boil eggs (10 min)
1:05    Portion rice into containers   Prep smoothie freezer bags x5
1:15    Slice chicken, portion         Eggs into ice bath
1:25    Vegetables out of oven         Peel eggs, portion
1:30    Portion vegetables             Assemble snack boxes x5
1:45    Label all containers           Clean as you go
2:00    Everything in fridge/freezer   Final kitchen cleanup
2:15    Done! 20+ meals prepped

YIELDS:
- 5 chicken + rice + veg lunches
- 5 ground turkey bowls (add fresh greens day-of)
- 5 overnight oats (breakfast)
- 5 smoothie bags (breakfast option 2)
- 5 hard boiled eggs (snacks)
- 5 snack boxes (snacks)
```

---

### 5. Freezer Inventory

**Purpose:** Tracks everything in your freezer — what's in there, when it was frozen, and when it needs to be used by. Prevents mystery containers and food waste from freezer burn.

**Properties:**

| Property | Type | Notes |
|---|---|---|
| Item | Title | What's in the container |
| Recipe | Relation | -> Recipes database (if from a recipe) |
| Category | Select | Protein / Complete Meal / Soup/Stew / Grain / Vegetable / Fruit / Bread / Sauce / Dessert / Smoothie Bag / Stock / Other |
| Quantity | Number | Number of servings or containers |
| Container Type | Select | Glass Container / Freezer Bag / Vacuum Sealed / Foil Wrapped / Ice Cube Tray / Original Packaging |
| Frozen Date | Date | When it went into the freezer |
| Use By | Date | Based on freezer life guidelines |
| Days Until Expiry | Formula | `if(empty(prop("Use By")), "No date", if(prop("Use By") < now(), "EXPIRED - use or toss!", format(dateBetween(prop("Use By"), now(), "days")) + " days left"))` |
| Expiring Soon | Formula | `if(and(not(empty(prop("Use By"))), dateBetween(prop("Use By"), now(), "days") <= 14, dateBetween(prop("Use By"), now(), "days") >= 0), true, false)` |
| Expired | Formula | `if(and(not(empty(prop("Use By"))), prop("Use By") < now()), true, false)` |
| Location | Select | Top Shelf / Middle Shelf / Bottom Shelf / Door / Deep Freeze / Drawer |
| Thaw Method | Select | Fridge Overnight / Counter 2hr / Microwave / Cook From Frozen / Cold Water |
| Reheat Instructions | Text | How to best reheat this item |
| Dietary Tags | Multi-select | Vegetarian / Vegan / Gluten-Free / Dairy-Free / Keto / High-Protein |
| Label Color | Select | Red / Blue / Green / Yellow / White / None (for physical label matching) |
| Used Up | Checkbox | Removed from freezer (eaten or discarded) |
| Used Date | Date | When it was consumed |
| Notes | Text | Portion size, serving suggestions, what to pair with |
| Tags | Multi-select | Emergency Meal / Guest Worthy / Weeknight Quick / Slow Thaw Required / Kids Approved |

**Views:**

- **Current Inventory** — Filter: Used Up = false, grouped by Category
- **Expiring Soon** — Filter: Expiring Soon = true, sorted by Use By ascending (eat these first!)
- **Expired** — Filter: Expired = true (toss or evaluate)
- **By Location** — Table, grouped by Location (physical inventory check)
- **By Category** — Table, grouped by Category
- **All Items** — Table, sorted by Frozen Date descending
- **Emergency Meals** — Filter: Tags contains Emergency Meal AND Used Up = false
- **Quick Thaw** — Filter: Thaw Method = Microwave or Cook From Frozen (same-day options)
- **Used History** — Filter: Used Up = true, sorted by Used Date (track what you actually eat)

---

## DASHBOARD

> Create this as the top-level page. Your meal prep command center showing this week's plan, what needs cooking, and what's in the freezer ready to go.

### Dashboard Layout

```
+------------------------------------------------------------------+
|  MEAL PREP HQ                                    Week of May 5     |
+----------+----------+----------+----------+----------+-----------+
|  Meals   |  Prepped |  Grocery |  Freezer |  Avg     |  Weekly   |
|  Planned |  Status  |  List    |  Items   |  Cal/Day |  Cost     |
|  21/21   |  12/21   |  6 items |  14      |  1,850   |  $87      |
+----------+----------+----------+----------+----------+-----------+
|                                                                    |
|  THIS WEEK'S MEAL PLAN                                            |
|  [Linked view -> Weekly Meal Plans, this week, by Day]            |
|                                                                    |
|       Breakfast    Lunch           Dinner                          |
|  Mon  Oatmeal     Turkey Bowl     Sheet Pan Chicken               |
|  Tue  Smoothie    Leftovers       Stir Fry                        |
|  Wed  Eggs        Salad           Slow Cooker Chili               |
|  Thu  Oatmeal     Chili (leftover) Salmon + Veg                   |
|  Fri  Smoothie    Salmon Bowl     Pizza (eat out)                 |
|                                                                    |
+----------------------------------+-------------------------------+
|  GROCERY LIST                    |  BATCH COOK SCHEDULE          |
|  [Linked view -> Grocery List,   |  [Linked view -> Batch Cook,  |
|   Purchased = false, grouped     |   Upcoming]                   |
|   by Store Section]              |                               |
|                                  |  Sunday 9am: Full Week Prep   |
|  Produce: 8 items               |  Wed evening: Quick refresh   |
|  Protein: 3 items               |                               |
|  Dairy: 2 items                 |                               |
+----------------------------------+-------------------------------+
|  FREEZER: USE SOON               |  RECIPE IDEAS                 |
|  [Linked view -> Freezer,        |  [Linked view -> Recipes,     |
|   Expiring Soon = true]          |   Not Made Recently, sorted   |
|                                  |   by Rating desc]             |
+----------------------------------+-------------------------------+
|  MACRO TARGETS vs ACTUAL                                          |
|  Calories: 1,850 / 2,000 target                                  |
|  Protein: 142g / 150g target                                     |
|  Carbs: 180g / 200g target                                       |
|  Fat: 68g / 75g target                                           |
+------------------------------------------------------------------+
```

---

## GROCERY AUTO-GENERATION WORKFLOW

### How to Build a Grocery List from Your Meal Plan

1. Open your **Weekly Meal Plan** for the upcoming week
2. Note all Recipes assigned to meal slots
3. For each Recipe, copy the Ingredients into **Grocery List** as individual entries
4. Consolidate duplicates (e.g., if two recipes need onions, combine into one entry)
5. Check "Have at Home" for anything already in your pantry
6. Assign Store Section to each item
7. The "Shopping List" view now shows only what you need, organized by aisle

### Consolidation Tips

- Same ingredient across recipes: add quantities together
- Bulk items (rice, oats, oil): check pantry first, only buy if low
- Fresh items (herbs, lettuce): only buy 3-4 days worth to prevent waste
- Freezer items: check Freezer Inventory before adding to list

### Cost Tracking

After shopping, fill in "Actual Cost" on Grocery List items. Sum for total weekly grocery spend. Divide by number of meals planned for cost-per-meal metric.

---

## MACRO TRACKING FORMULAS

### Recipe Macro Breakdown

```
"P:" + format(prop("Protein (g)")) + "g | C:" + format(prop("Carbs (g)")) + "g | F:" + format(prop("Fat (g)")) + "g | " + format(prop("Calories (per serving)")) + " cal"
```

### Protein Percentage of Calories

```
if(
  prop("Calories (per serving)") == 0,
  0,
  round(prop("Protein (g)") * 4 / prop("Calories (per serving)") * 100)
)
```

Protein has 4 calories per gram. This shows what % of the recipe's calories come from protein. Target: 25-35% for high-protein meals.

### Daily Macro Totals

Sum across all meal plan entries for a given day:

- Total Calories = sum of all Calories for that day's meals
- Total Protein = sum of all Protein values
- Total Carbs = sum of all Carbs values
- Total Fat = sum of all Fat values

Compare against your daily targets in the Macro Summary view.

### Cost Per Serving

Track on each Recipe and use for meal plan budgeting:
```
prop("Cost Per Serving") * prop("Servings")
```

### Batch Cook Cost Per Meal

```
if(
  prop("Meals Produced") == 0,
  0,
  round(prop("Total Session Cost") / prop("Meals Produced") * 100) / 100
)
```

---

## FREEZER MANAGEMENT FORMULAS

### Days Until Expiry

```
if(
  empty(prop("Use By")),
  "No date",
  if(
    prop("Use By") < now(),
    "EXPIRED - use or toss!",
    format(dateBetween(prop("Use By"), now(), "days")) + " days left"
  )
)
```

### Expiring Soon Flag (within 14 days)

```
if(
  and(
    not(empty(prop("Use By"))),
    dateBetween(prop("Use By"), now(), "days") <= 14,
    dateBetween(prop("Use By"), now(), "days") >= 0
  ),
  true,
  false
)
```

### Expired Detection

```
if(
  and(
    not(empty(prop("Use By"))),
    prop("Use By") < now()
  ),
  true,
  false
)
```

### Freezer Storage Guidelines

| Food Type | Freezer Life | Container | Thaw Method |
|---|---|---|---|
| Cooked chicken | 2-3 months | Airtight container or bag | Fridge overnight |
| Ground meat (cooked) | 2-3 months | Freezer bag, flat | Fridge overnight |
| Soups & stews | 3-4 months | Glass container (leave headspace) | Fridge overnight or stovetop |
| Cooked rice/grains | 1-2 months | Freezer bag, flat | Microwave |
| Smoothie bags | 2-3 months | Freezer bag | Blend from frozen |
| Baked goods | 2-3 months | Foil + freezer bag | Counter 1-2 hours |
| Raw meat | 3-6 months | Vacuum sealed or freezer bag | Fridge overnight |
| Casseroles | 2-3 months | Foil pan or glass | Oven from frozen (350F, covered) |
| Sauces | 3-6 months | Ice cube tray then bag | Stovetop |
| Vegetables (blanched) | 8-12 months | Freezer bag | Cook from frozen |

---

## QUICK-START GUIDE

### Step 1 — Add Your Favorite Recipes (20 minutes)

- Open the **Recipes** database
- Add 15-20 recipes your household already eats regularly
- Required: Recipe Name, Category, Servings, Ingredients, and Instructions
- Helpful: add Calories and Protein if you're tracking macros
- Mark Batch Friendly and Freezer Friendly for meal prep stars
- Tag with Dietary Tags for easy filtering

### Step 2 — Plan Your First Week (10 minutes)

- Open **Weekly Meal Plans** and create entries for the coming week
- Start simple: plan Dinner for each day, then Lunch
- Breakfast can be the same 2-3 options rotated
- Link a Recipe to each entry (or write "Leftovers" or "Eating out" in Custom Meal)
- Identify which meals can be batch-prepped (mark Prep Day as Sunday)

### Step 3 — Generate Your Grocery List (10 minutes)

- Open **Grocery List** and add all ingredients from this week's recipes
- Consolidate duplicates and check pantry for items you already have
- Mark Store Section for each item
- Check "Have at Home" for anything in stock
- Sort by Store for efficient shopping

### Step 4 — Plan Your Batch Cook Session (5 minutes)

- Open **Batch Cooking Workflow** and create a session for your prep day
- Link the recipes you'll prep
- Write out steps with timing (use the Sample Schedule as a template)
- Note Parallel Tasks — this is where you save hours
- Set Containers Needed so you have everything ready

### Step 5 — Stock Your Freezer (ongoing)

- After each batch cook session, add items to **Freezer Inventory**
- Set Frozen Date and Use By date (refer to Storage Guidelines)
- Note Location and Thaw Method
- Check Freezer Inventory before meal planning each week — use what you have!

### Step 6 — Build Your Dashboard

- Create the top-level page following the Dashboard Layout
- Pin to sidebar for weekly reference

### Weekly Meal Prep Rhythm

**Thursday or Friday (10 minutes):**

- Plan next week's meals using Recipes database
- Generate grocery list from plan
- Check freezer inventory for anything to thaw/use
- Check "Expiring Soon" and build meals around those items

**Saturday (30 minutes):**

- Shop using the Shopping List view (organized by store section)
- Update Actual Cost for budget tracking

**Sunday (2-3 hours):**

- Execute Batch Cook Session following your workflow steps
- Portion into containers and label
- Add new items to Freezer Inventory
- Mark meal plan items as Prepped

**Daily (2 minutes):**

- Check meal plan for today
- Thaw anything needed for tomorrow
- Note any adjustments (leftovers extending a meal, etc.)

### Pro Tips

- The Recipes database is a living library. After every meal, update Rating and Family Approval. After 3 months, you'll have a perfectly curated collection of proven winners.
- Plan meals around protein first, then build sides. This ensures macro targets are hit and prevents the "five pasta dishes" week.
- The Freezer Inventory prevents food waste and saves money. A full freezer is like having 14+ meals available with zero daily prep — but only if you know what's in there.
- Batch cooking works best when you prep components, not just complete meals. Cooked chicken, rice, and roasted vegetables can be recombined into 5+ different meals throughout the week.
- The "Not Made Recently" view in Recipes prevents dinner boredom. If you haven't made something in 30+ days, it's fresh again.
- Always plan at least one "No Cook" or "Reheat Only" dinner per week. You need a break. Leftovers, frozen meals from your inventory, or assembly meals (salads, wraps) fill this slot.
- Cost Per Meal tracking reveals that meal prep is dramatically cheaper than eating out. When you can show the actual number ($3.50/meal vs. $12-15 eating out), the Sunday prep motivation stays strong.
- Label everything in the freezer with contents AND date. Unlabeled containers become mystery food that never gets eaten. Use masking tape and a sharpie — it doesn't have to be fancy.
