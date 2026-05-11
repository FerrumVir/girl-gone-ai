# Airbnb Pricing Strategy Spreadsheet — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Optimize your nightly rates with seasonal calendars, competitor analysis, occupancy tracking, and dynamic pricing rules — all without paying for expensive pricing tools.

---

> **SETUP GUIDE — Get Running in 20 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 6 tabs/sheets and name them: Rate Calendar, Competitor Rates, Occupancy Tracker, RevPAN Calculator, Cleaning Fee Optimizer, Dynamic Pricing Rules
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Start with your current base rate and fill in the Rate Calendar, then research 5+ competitors
> 6. Update occupancy data weekly for best results
>
> **Tip:** Review and adjust rates every Sunday evening for the coming 2 weeks. Airbnb's algorithm favors listings that update pricing regularly.

---

---

# SHEET 1: RATE CALENDAR

> Your 12-month pricing calendar with base rates, seasonal multipliers, and event-based adjustments.

---

## Property Settings

| Setting | Value |
|---------|-------|
| Property Name | |
| Listing URL | |
| Base Nightly Rate | $ |
| Minimum Rate (floor) | $ |
| Maximum Rate (ceiling) | $ |
| Bedrooms | |
| Max Guests | |
| Cleaning Fee | $ |
| City/Market | |

---

## Season Definitions

| Season | Months | Multiplier | Adjusted Rate |
|--------|--------|:----------:|-------------:|
| Peak (High) | Jun, Jul, Aug | 1.40 | $ |
| Shoulder (Medium-High) | Apr, May, Sep, Oct | 1.15 | $ |
| Standard | Mar, Nov | 1.00 | $ |
| Low | Jan, Feb, Dec (non-holiday) | 0.75 | $ |

`FORMULA (Adjusted Rate): =BaseRate * Multiplier`

---

## Monthly Rate Calendar

| Day | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Week Avg | Occupancy |
|-----|----:|----:|----:|----:|----:|----:|----:|--------:|:---------:|
| Week 1 | $ | $ | $ | $ | $ | $ | $ | $ | /7 |
| Week 2 | $ | $ | $ | $ | $ | $ | $ | $ | /7 |
| Week 3 | $ | $ | $ | $ | $ | $ | $ | $ | /7 |
| Week 4 | $ | $ | $ | $ | $ | $ | $ | $ | /7 |
| Week 5 | $ | $ | $ | $ | $ | $ | $ | $ | /7 |

Repeat for each month (create 12 sections or use one sheet per month).

---

## Day-of-Week Multipliers

| Day | Multiplier | Reasoning |
|-----|:----------:|-----------|
| Monday | 0.85 | Lowest demand |
| Tuesday | 0.85 | Low demand |
| Wednesday | 0.90 | Midweek slight uptick |
| Thursday | 0.95 | Pre-weekend bookings |
| Friday | 1.20 | Weekend premium |
| Saturday | 1.25 | Highest weekend demand |
| Sunday | 0.90 | Check-out day for most |

`FORMULA (Daily Rate): =BaseRate * SeasonMultiplier * DayOfWeekMultiplier`

---

## Special Event / Holiday Calendar

| Date/Range | Event | Rate Multiplier | Adjusted Rate | Min Night Stay | Notes |
|------------|-------|:--------------:|-------------:|:--------------:|-------|
| Dec 20 - Jan 2 | Holiday Season | 1.75 | $ | 3 | |
| Feb 14 | Valentine's Day | 1.30 | $ | 2 | |
| Mar (varies) | Spring Break | 1.50 | $ | 3 | |
| Jul 4 | Independence Day | 1.60 | $ | 3 | |
| Labor Day Weekend | Sept | 1.50 | $ | 3 | |
| Halloween | Oct 31 | 1.20 | $ | 2 | |
| Thanksgiving | Nov (varies) | 1.50 | $ | 3 | |
| [Local Event 1] | | 1.40 | $ | 2 | |
| [Local Event 2] | | 1.40 | $ | 2 | |
| [Local Event 3] | | 1.40 | $ | 2 | |

---

## Last-Minute Discount Rules

| Days Until Check-in | Discount | Adjusted Rate | Logic |
|--------------------:|:--------:|-------------:|-------|
| 14+ days out | 0% | Full rate | Standard pricing |
| 7-13 days | 5% | $ | Slight incentive |
| 3-6 days | 10% | $ | Moderate incentive |
| 1-2 days | 15% | $ | Fill empty night |
| Same day | 20% | $ | Revenue > empty |

`FORMULA (Adjusted Rate): =FullRate * (1 - DiscountPct)`

---

---

# SHEET 2: COMPETITOR RATES

> Track 5-10 similar listings in your area. Update weekly to stay competitive.

---

## Competitor Listings

| # | Listing Name | URL | Bedrooms | Max Guests | Rating | Reviews | Superhost? |
|---|-------------|-----|:--------:|:----------:|:------:|:-------:|:----------:|
| 1 | | | | | | | Y/N |
| 2 | | | | | | | Y/N |
| 3 | | | | | | | Y/N |
| 4 | | | | | | | Y/N |
| 5 | | | | | | | Y/N |
| 6 | | | | | | | Y/N |
| 7 | | | | | | | Y/N |

---

## Weekly Rate Comparison

| Competitor | Weeknight Rate | Weekend Rate | Cleaning Fee | Total (2-Night Stay) | Total (5-Night Stay) | Last Updated |
|-----------|---------------:|-------------:|-------------:|---------------------:|---------------------:|--------------|
| Comp 1 | $ | $ | $ | $ | $ | |
| Comp 2 | $ | $ | $ | $ | $ | |
| Comp 3 | $ | $ | $ | $ | $ | |
| Comp 4 | $ | $ | $ | $ | $ | |
| Comp 5 | $ | $ | $ | $ | $ | |
| **Average** | **$** | **$** | **$** | **$** | **$** | |
| **YOUR Rate** | **$** | **$** | **$** | **$** | **$** | |
| **Difference** | **$** | **$** | **$** | **$** | **$** | |

`FORMULA (Total 2-Night): =(WeekendRate * 2) + CleaningFee`
`FORMULA (Total 5-Night): =(WeekdayRate * 3) + (WeekendRate * 2) + CleaningFee`
`FORMULA (Average): =AVERAGE(B2:B6)`
`FORMULA (Difference): =YourRate - Average`

---

## Competitive Position Analysis

| Metric | Your Listing | Market Average | Your Percentile | Action |
|--------|------------:|---------------:|:---------------:|--------|
| Nightly Rate | $ | $ | % | |
| Cleaning Fee | $ | $ | % | |
| Rating | | | % | |
| Review Count | | | % | |
| Total Cost (2 nights) | $ | $ | % | |

`FORMULA (Percentile): =PERCENTRANK(AllRates, YourRate) * 100`

---

---

# SHEET 3: OCCUPANCY TRACKER

> Track booked vs. available nights. Calculate actual occupancy rates by month.

---

## Monthly Occupancy Log

| Month | Available Nights | Booked Nights | Blocked Nights | Occupancy Rate | Revenue | ADR |
|-------|:----------------:|:-------------:|:--------------:|:--------------:|--------:|----:|
| January | 31 | | | % | $ | $ |
| February | 28 | | | % | $ | $ |
| March | 31 | | | % | $ | $ |
| April | 30 | | | % | $ | $ |
| May | 31 | | | % | $ | $ |
| June | 30 | | | % | $ | $ |
| July | 31 | | | % | $ | $ |
| August | 31 | | | % | $ | $ |
| September | 30 | | | % | $ | $ |
| October | 31 | | | % | $ | $ |
| November | 30 | | | % | $ | $ |
| December | 31 | | | % | $ | $ |
| **TOTAL** | **365** | | | **%** | **$** | **$** |

`FORMULA (Occupancy Rate): =BookedNights / (AvailableNights - BlockedNights) * 100`
`FORMULA (ADR - Average Daily Rate): =Revenue / BookedNights`

---

## Booking Detail Log

| Check-in | Check-out | Nights | Guest Name | Nightly Rate | Cleaning Fee | Service Fee | Total Payout | Platform | Source |
|----------|-----------|:------:|------------|------------:|-------------:|------------:|------------:|----------|--------|
| | | | | $ | $ | $ | $ | Airbnb/VRBO/Direct | |
| | | | | $ | $ | $ | $ | | |
| | | | | $ | $ | $ | $ | | |

`FORMULA (Nights): =CheckOut - CheckIn`
`FORMULA (Total Payout): =(NightlyRate * Nights) + CleaningFee - ServiceFee`

---

## Occupancy Benchmarks

| Occupancy Rate | Assessment | Action |
|:--------------:|-----------|--------|
| 90%+ | Too cheap | Raise rates 10-15% |
| 75-89% | Optimal | Minor adjustments only |
| 60-74% | Slightly low | Reduce rates 5-10% or improve listing |
| 40-59% | Concerning | Major rate reduction or listing overhaul |
| Below 40% | Critical | Re-evaluate market fit, pricing, and listing quality |

---

---

# SHEET 4: RevPAN CALCULATOR

> Revenue Per Available Night — the single most important metric for rental profitability.

---

## RevPAN Dashboard

| Month | Revenue | Available Nights | RevPAN | ADR | Occupancy | Target RevPAN | vs. Target |
|-------|--------:|:----------------:|-------:|----:|:---------:|:------------:|:----------:|
| January | $ | 31 | $ | $ | % | $ | +/- $ |
| February | $ | 28 | $ | $ | % | $ | +/- $ |
| March | $ | 31 | $ | $ | % | $ | +/- $ |
| April | $ | 30 | $ | $ | % | $ | +/- $ |
| May | $ | 31 | $ | $ | % | $ | +/- $ |
| June | $ | 30 | $ | $ | % | $ | +/- $ |
| July | $ | 31 | $ | $ | % | $ | +/- $ |
| August | $ | 31 | $ | $ | % | $ | +/- $ |
| September | $ | 30 | $ | $ | % | $ | +/- $ |
| October | $ | 31 | $ | $ | % | $ | +/- $ |
| November | $ | 30 | $ | $ | % | $ | +/- $ |
| December | $ | 31 | $ | $ | % | $ | +/- $ |
| **Annual** | **$** | **365** | **$** | **$** | **%** | **$** | **$** |

`FORMULA (RevPAN): =Revenue / AvailableNights`
`FORMULA (Alternative): =ADR * OccupancyRate`
`FORMULA (vs. Target): =ActualRevPAN - TargetRevPAN`

---

## RevPAN Optimization Scenarios

| Scenario | ADR | Occupancy | RevPAN | Annual Revenue | Notes |
|----------|----:|:---------:|-------:|--------------:|-------|
| Current | $ | % | $ | $ | Status quo |
| Higher rate, lower occ | $ | % | $ | $ | +$20/night, -10% occ |
| Lower rate, higher occ | $ | % | $ | $ | -$15/night, +15% occ |
| Premium positioning | $ | % | $ | $ | Photos + amenities upgrade |
| Minimum stay 3 nights | $ | % | $ | $ | Fewer turnovers |

`FORMULA (Annual Revenue): =RevPAN * 365`

---

## Break-Even Analysis

| Expense | Monthly | Annual |
|---------|--------:|-------:|
| Mortgage/Rent | $ | $ |
| Utilities | $ | $ |
| Insurance | $ | $ |
| HOA/Condo Fees | $ | $ |
| Property Management | $ | $ |
| Cleaning (per turn) | $ | $ |
| Supplies/Consumables | $ | $ |
| Maintenance Reserve | $ | $ |
| Platform Fees (~3%) | $ | $ |
| Taxes (property + income) | $ | $ |
| **Total Expenses** | **$** | **$** |
| **Break-Even RevPAN** | | **$** |
| **Break-Even Occupancy (at current ADR)** | | **%** |

`FORMULA (Break-Even RevPAN): =TotalAnnualExpenses / 365`
`FORMULA (Break-Even Occupancy): =TotalAnnualExpenses / (ADR * 365) * 100`

---

---

# SHEET 5: CLEANING FEE OPTIMIZER

> Find the cleaning fee sweet spot — high enough to cover costs, low enough not to kill short-stay bookings.

---

## Cleaning Cost Breakdown

| Item | Cost Per Turn |
|------|-------------:|
| Professional cleaner | $ |
| Laundry (sheets, towels) | $ |
| Consumables restocked | $ |
| Wear & tear reserve | $ |
| Your time/coordination | $ |
| **Total Actual Cost** | **$** |

---

## Fee Impact Analysis

| Cleaning Fee | Total Cost (1 night) | Total Cost (2 nights) | Total Cost (3 nights) | Total Cost (7 nights) | Per-Night Impact (2N) |
|-------------:|--------------------:|---------------------:|---------------------:|---------------------:|---------------------:|
| $50 | $ | $ | $ | $ | $ |
| $75 | $ | $ | $ | $ | $ |
| $100 | $ | $ | $ | $ | $ |
| $125 | $ | $ | $ | $ | $ |
| $150 | $ | $ | $ | $ | $ |
| $175 | $ | $ | $ | $ | $ |
| $200 | $ | $ | $ | $ | $ |

`FORMULA (Total Cost): =(NightlyRate * Nights) + CleaningFee`
`FORMULA (Per-Night Impact): =CleaningFee / Nights`

---

## Competitor Cleaning Fee Comparison

| Listing | Cleaning Fee | Nightly Rate | Total (2 Nights) | Your Difference |
|---------|-------------:|-------------:|------------------:|----------------:|
| Comp 1 | $ | $ | $ | $ |
| Comp 2 | $ | $ | $ | $ |
| Comp 3 | $ | $ | $ | $ |
| Comp 4 | $ | $ | $ | $ |
| Comp 5 | $ | $ | $ | $ |
| **Market Avg** | **$** | | | |
| **Your Fee** | **$** | | | |

---

## Cleaning Fee Strategy Matrix

| Stay Length | Recommended Strategy | Example (Base $150/night) |
|------------|---------------------|---------------------------|
| 1 night | Bake into rate, low/no cleaning fee | $200/night, $0 cleaning |
| 2-3 nights | Moderate cleaning fee | $150/night, $85 cleaning |
| 4-6 nights | Standard cleaning fee | $140/night, $100 cleaning |
| 7+ nights | Full cleaning fee, slight rate discount | $130/night, $120 cleaning |

---

---

# SHEET 6: DYNAMIC PRICING RULES

> If/then rules for automated or manual price adjustments based on market conditions.

---

## Rule Engine

| # | Condition | Action | Priority | Active? |
|---|-----------|--------|:--------:|:-------:|
| 1 | Booking is 14+ days out AND occupancy this month < 50% | Reduce rate 10% | 1 | Y |
| 2 | Booking is within 3 days AND night is empty | Reduce rate 15% (floor = minimum) | 2 | Y |
| 3 | Same-day booking request | Reduce rate 20% (floor = minimum) | 3 | Y |
| 4 | Week is 100% booked except 1 gap night | Reduce gap night 25% | 4 | Y |
| 5 | 3+ day stay request | Apply 5% length-of-stay discount | 5 | Y |
| 6 | 7+ day stay request | Apply 12% weekly discount | 6 | Y |
| 7 | 28+ day stay request | Apply 25% monthly discount | 7 | Y |
| 8 | Local event within 5 miles, 1000+ attendees | Increase rate 30-50% | 8 | Y |
| 9 | Weekend (Fri-Sat) during peak season | Increase rate 25% above seasonal | 9 | Y |
| 10 | Returning guest | Offer 10% loyalty discount | 10 | Y |
| 11 | Occupancy this month > 85% | Increase remaining nights 10% | 11 | Y |
| 12 | No booking 30+ days out during peak | Review listing quality, no rate drop | 12 | Y |

---

## Length-of-Stay Discounts

| Stay Length | Discount % | Effective Nightly Rate | Cleaning Fee Impact | Net Per Night |
|------------|:----------:|----------------------:|--------------------:|-------------:|
| 1 night | 0% | $ | $ (per night: $) | $ |
| 2 nights | 0% | $ | $ (per night: $) | $ |
| 3 nights | 5% | $ | $ (per night: $) | $ |
| 4 nights | 5% | $ | $ (per night: $) | $ |
| 5 nights | 8% | $ | $ (per night: $) | $ |
| 6 nights | 8% | $ | $ (per night: $) | $ |
| 7 nights | 12% | $ | $ (per night: $) | $ |
| 14 nights | 18% | $ | $ (per night: $) | $ |
| 28+ nights | 25% | $ | $ (per night: $) | $ |

`FORMULA (Effective Rate): =BaseRate * (1 - Discount%)`
`FORMULA (Net Per Night): =EffectiveRate + (CleaningFee / Nights)`

---

## Seasonal Rate Summary (Full Year)

| Month | Season | Base Mult | Day-of-Week Range | Event Mult | Effective Range (Low-High) |
|-------|--------|:---------:|:-----------------:|:----------:|---------------------------:|
| Jan | Low | 0.75 | 0.85-1.25 | -- | $XX - $XX |
| Feb | Low | 0.75 | 0.85-1.25 | 1.30 (V-Day) | $XX - $XX |
| Mar | Shoulder | 1.15 | 0.85-1.25 | 1.50 (Spr Break) | $XX - $XX |
| Apr | Shoulder | 1.15 | 0.85-1.25 | -- | $XX - $XX |
| May | Shoulder | 1.15 | 0.85-1.25 | 1.40 (Mem Day) | $XX - $XX |
| Jun | Peak | 1.40 | 0.85-1.25 | -- | $XX - $XX |
| Jul | Peak | 1.40 | 0.85-1.25 | 1.60 (July 4) | $XX - $XX |
| Aug | Peak | 1.40 | 0.85-1.25 | -- | $XX - $XX |
| Sep | Shoulder | 1.15 | 0.85-1.25 | 1.50 (Labor Day) | $XX - $XX |
| Oct | Shoulder | 1.15 | 0.85-1.25 | 1.20 (Halloween) | $XX - $XX |
| Nov | Standard | 1.00 | 0.85-1.25 | 1.50 (Thnksgvng) | $XX - $XX |
| Dec | Low/Peak | 0.75/1.75 | 0.85-1.25 | 1.75 (Holidays) | $XX - $XX |

`FORMULA (Low End): =BaseRate * SeasonMult * MIN(DayOfWeekMults)`
`FORMULA (High End): =BaseRate * SeasonMult * MAX(DayOfWeekMults) * EventMult`

---

---

# FORMULA REFERENCE GUIDE

---

## Core Pricing Formulas

**Daily rate calculation:**
```
=BaseRate * SeasonMultiplier * DayOfWeekMultiplier * EventMultiplier
```

**RevPAN (Revenue Per Available Night):**
```
=TotalRevenue / TotalAvailableNights
```

**Occupancy Rate:**
```
=BookedNights / (AvailableNights - BlockedNights) * 100
```

**Average Daily Rate (ADR):**
```
=TotalRevenue / BookedNights
```

**Total guest cost:**
```
=(NightlyRate * Nights) + CleaningFee + ServiceFee
```

## Comparison Formulas

**Your rate vs. market average:**
```
=(YourRate - MarketAverage) / MarketAverage * 100
```

**Percentile rank among competitors:**
```
=PERCENTRANK(CompetitorRates, YourRate)
```

## Conditional Formatting Rules

**Occupancy below 60% (red):**
```
=D2 < 0.6
```

**Occupancy 60-75% (yellow):**
```
=AND(D2 >= 0.6, D2 < 0.75)
```

**Occupancy above 75% (green):**
```
=D2 >= 0.75
```

**Rate above competitors (blue):**
```
=YourRate > MarketAverage * 1.1
```

**Rate below competitors (orange):**
```
=YourRate < MarketAverage * 0.9
```

---

> **NOTE:** Update competitor rates weekly and your occupancy data after every booking. The dynamic pricing rules are meant to be applied manually or used as logic for tools like PriceLabs, Beyond Pricing, or Wheelhouse. This spreadsheet helps you understand your market and make informed decisions even without paid pricing tools. Always check Airbnb's pricing tips in your area and adjust for your specific amenities, location, and guest reviews.
