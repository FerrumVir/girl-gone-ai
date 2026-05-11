# Crypto Portfolio Tracker & Tax Helper — Google Sheets Template

> Make a copy of this spreadsheet to start using it. Track every crypto transaction, calculate cost basis using FIFO/LIFO, monitor your portfolio allocation, and generate tax-ready reports — all without connecting API keys or sharing data with third parties.

---

> **SETUP GUIDE — Get Running in 20 Minutes**
>
> 1. Create a new Google Sheets document
> 2. Create 7 tabs/sheets and name them: Transaction Log, Portfolio Dashboard, P&L Per Coin, Allocation Data, DCA Tracker, Tax Lots, Tax Summary
> 3. Copy each section below into its corresponding sheet
> 4. Enter all formulas as documented (marked with `FORMULA:`)
> 5. Start by entering your transaction history in the Transaction Log
> 6. For current prices, use GOOGLEFINANCE() or enter manually
>
> **Tip:** Import CSV exports from your exchanges into the Transaction Log. Most exchanges (Coinbase, Binance, Kraken) allow CSV download of your full history.

---

---

# SHEET 1: TRANSACTION LOG

> Every buy, sell, swap, staking reward, and airdrop goes here. This is your master ledger.

---

## Column Headers

| A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Date** | **Type** | **Asset** | **Quantity** | **Price Per Unit (USD)** | **Total Value (USD)** | **Fee (USD)** | **Fee (Asset)** | **Exchange/Wallet** | **Notes** | **Tx Hash** | **Cost Basis (USD)** |

## Type (Dropdown Values)
- Buy
- Sell
- Swap-Out (asset you gave up)
- Swap-In (asset you received)
- Staking Reward
- Airdrop
- Transfer-In
- Transfer-Out
- Mining Income

---

## Formulas

`FORMULA (F2): =D2 * E2`
Total Value = Quantity * Price Per Unit

`FORMULA (L2 for Buy): =F2 + G2`
Cost Basis for a buy = Total Value + Fee

`FORMULA (L2 for Staking/Airdrop): =F2`
Cost Basis for income = Fair Market Value at time of receipt

`FORMULA (L2 for Sell): Leave blank (cost basis comes from Tax Lots sheet)`

---

## Sample Data

| Date | Type | Asset | Qty | Price | Value | Fee | Fee Asset | Exchange | Notes | Tx Hash | Cost Basis |
|------|------|-------|-----|-------|-------|-----|-----------|----------|-------|---------|------------|
| 2025-01-15 | Buy | BTC | 0.25 | $42,000 | $10,500 | $15.75 | 0 | Coinbase | DCA buy | | $10,515.75 |
| 2025-02-01 | Buy | ETH | 5.0 | $2,300 | $11,500 | $17.25 | 0 | Coinbase | DCA buy | | $11,517.25 |
| 2025-02-15 | Buy | BTC | 0.15 | $44,500 | $6,675 | $10.01 | 0 | Kraken | | | $6,685.01 |
| 2025-03-01 | Staking Reward | ETH | 0.012 | $2,450 | $29.40 | $0 | 0 | Lido | Auto-compound | | $29.40 |
| 2025-03-10 | Swap-Out | ETH | 2.0 | $2,500 | $5,000 | $8.50 | 0 | Uniswap | ETH to SOL | 0xabc... | |
| 2025-03-10 | Swap-In | SOL | 35.0 | $142.86 | $5,000 | $0 | 0 | Uniswap | From ETH swap | 0xabc... | $5,008.50 |
| 2025-04-01 | Sell | BTC | 0.10 | $52,000 | $5,200 | $7.80 | 0 | Coinbase | Taking profits | | |
| 2025-04-15 | Airdrop | ARB | 500 | $1.20 | $600 | $0 | 0 | Wallet | Arbitrum drop | | $600.00 |

---

---

# SHEET 2: PORTFOLIO DASHBOARD

> Current holdings, values, and unrealized P&L at a glance.

---

## Holdings Summary

| Asset | Total Qty Held | Avg Cost Basis/Unit | Total Cost Basis | Current Price | Current Value | Unrealized P&L ($) | Unrealized P&L (%) | Allocation % |
|-------|---------------|--------------------:|----------------:|-------------:|-------------:|-------------------:|-------------------:|-------------:|
| BTC | | $ | $ | $ | $ | $ | % | % |
| ETH | | $ | $ | $ | $ | $ | % | % |
| SOL | | $ | $ | $ | $ | $ | % | % |
| ARB | | $ | $ | $ | $ | $ | % | % |
| | | | | | | | | |
| **TOTAL** | | | **$** | | **$** | **$** | **%** | **100%** |

---

## Formulas

`FORMULA (Total Qty Held): =SUMIFS(TransactionLog!D:D, TransactionLog!C:C, A2, TransactionLog!B:B, "Buy") + SUMIFS(TransactionLog!D:D, TransactionLog!C:C, A2, TransactionLog!B:B, "Swap-In") + SUMIFS(TransactionLog!D:D, TransactionLog!C:C, A2, TransactionLog!B:B, "Staking Reward") + SUMIFS(TransactionLog!D:D, TransactionLog!C:C, A2, TransactionLog!B:B, "Airdrop") - SUMIFS(TransactionLog!D:D, TransactionLog!C:C, A2, TransactionLog!B:B, "Sell") - SUMIFS(TransactionLog!D:D, TransactionLog!C:C, A2, TransactionLog!B:B, "Swap-Out")`

`FORMULA (Avg Cost Basis/Unit): =TotalCostBasis / TotalQtyHeld`

`FORMULA (Total Cost Basis): =SUMIFS(TransactionLog!L:L, TransactionLog!C:C, A2, TransactionLog!B:B, "Buy") + SUMIFS(TransactionLog!L:L, TransactionLog!C:C, A2, TransactionLog!B:B, "Swap-In") + SUMIFS(TransactionLog!L:L, TransactionLog!C:C, A2, TransactionLog!B:B, "Staking Reward") - CostBasisOfSoldLots`

`FORMULA (Current Price — manual or auto):`
```
=GOOGLEFINANCE("CRYPTO:"&A2&"USD")
```
Note: GOOGLEFINANCE supports BTC, ETH, and some major coins. For others, enter manually.

`FORMULA (Current Value): =B2 * E2`

`FORMULA (Unrealized P&L $): =CurrentValue - TotalCostBasis`

`FORMULA (Unrealized P&L %): =UnrealizedPL / TotalCostBasis * 100`

`FORMULA (Allocation %): =CurrentValue / TotalPortfolioValue * 100`

---

## Portfolio Metrics

| Metric | Value |
|--------|-------|
| Total Portfolio Value | $ |
| Total Cost Basis (all holdings) | $ |
| Total Unrealized Gain/Loss | $ |
| Overall Return % | % |
| Number of Assets Held | |
| Largest Position (%) | |
| Smallest Position (%) | |

`FORMULA (Overall Return %): =TotalUnrealizedPL / TotalCostBasis * 100`
`FORMULA (Largest Position): =MAX(AllocationColumn)`

---

---

# SHEET 3: P&L PER COIN

> Detailed profit/loss breakdown for each asset including realized and unrealized gains.

---

## Per-Asset Performance

| Asset | Total Bought (USD) | Total Sold (USD) | Realized P&L | Unrealized P&L | Total P&L | ROI % | Holding Period |
|-------|-------------------:|-----------------:|-------------:|---------------:|----------:|------:|---------------|
| BTC | $ | $ | $ | $ | $ | % | Long/Short/Mix |
| ETH | $ | $ | $ | $ | $ | % | Long/Short/Mix |
| SOL | $ | $ | $ | $ | $ | % | Long/Short/Mix |
| ARB | $ | $ | $ | $ | $ | % | Long/Short/Mix |
| **TOTAL** | **$** | **$** | **$** | **$** | **$** | **%** | |

---

## Formulas

`FORMULA (Total Bought): =SUMIFS(TransactionLog!F:F, TransactionLog!C:C, A2, TransactionLog!B:B, "Buy") + SUMIFS(TransactionLog!F:F, TransactionLog!C:C, A2, TransactionLog!B:B, "Swap-In")`

`FORMULA (Total Sold): =SUMIFS(TransactionLog!F:F, TransactionLog!C:C, A2, TransactionLog!B:B, "Sell") + SUMIFS(TransactionLog!F:F, TransactionLog!C:C, A2, TransactionLog!B:B, "Swap-Out")`

`FORMULA (Realized P&L): =SUM from Tax Lots sheet for this asset where Status="Closed"`

`FORMULA (ROI %): =TotalPL / TotalBought * 100`

`FORMULA (Holding Period): =IF(all lots held >365 days, "Long", IF(all lots held <365 days, "Short", "Mix"))`

---

## Realized Gains Detail

| Date Sold | Asset | Qty Sold | Proceeds | Cost Basis (FIFO) | Gain/Loss | Short/Long Term |
|-----------|-------|---------|----------|-------------------|-----------|-----------------|
| | | | $ | $ | $ | |
| | | | $ | $ | $ | |
| **TOTAL** | | | **$** | **$** | **$** | |

`FORMULA (Gain/Loss): =Proceeds - CostBasis - Fees`
`FORMULA (Short/Long): =IF(SellDate - BuyDate > 365, "Long-Term", "Short-Term")`

---

---

# SHEET 4: ALLOCATION DATA

> Data structured for pie chart creation. Tracks target vs. actual allocation.

---

## Current Allocation

| Asset | Current Value | Allocation % | Target Allocation % | Difference | Action Needed |
|-------|-------------:|-------------:|--------------------:|-----------:|---------------|
| BTC | $ | % | % | % | Buy/Sell/Hold |
| ETH | $ | % | % | % | Buy/Sell/Hold |
| SOL | $ | % | % | % | Buy/Sell/Hold |
| Stablecoins | $ | % | % | % | Buy/Sell/Hold |
| Altcoins | $ | % | % | % | Buy/Sell/Hold |
| **TOTAL** | **$** | **100%** | **100%** | | |

`FORMULA (Allocation %): =CurrentValue / TotalValue * 100`
`FORMULA (Difference): =ActualAllocation - TargetAllocation`
`FORMULA (Action Needed): =IF(Difference > 5, "Sell", IF(Difference < -5, "Buy", "Hold"))`

---

## Rebalancing Calculator

| Asset | Current Value | Target Value | Difference ($) | Action |
|-------|-------------:|------------:|---------------:|--------|
| BTC | $ | $ | $ | Buy/Sell $X |
| ETH | $ | $ | $ | Buy/Sell $X |
| SOL | $ | $ | $ | Buy/Sell $X |

`FORMULA (Target Value): =TotalPortfolio * TargetAllocation%`
`FORMULA (Difference): =TargetValue - CurrentValue`
`FORMULA (Action): =IF(Difference>0, "Buy $"&TEXT(ABS(Difference),"0.00"), "Sell $"&TEXT(ABS(Difference),"0.00"))`

---

## Category Breakdown (for pie chart)

| Category | Assets Included | Total Value | % of Portfolio |
|----------|----------------|------------:|---------------:|
| Large Cap (Top 10) | BTC, ETH, SOL | $ | % |
| Mid Cap | | $ | % |
| Small Cap / Altcoins | | $ | % |
| DeFi Tokens | | $ | % |
| Stablecoins | USDC, USDT | $ | % |
| NFTs / Other | | $ | % |

---

---

# SHEET 5: DCA TRACKER

> Track your dollar-cost averaging strategy. See your average buy price evolve over time.

---

## DCA Schedule

| Asset | Frequency | Amount Per Buy | Start Date | Total Invested | Total Qty | Avg Price Paid | Current Price | DCA Return % |
|-------|-----------|---------------:|------------|---------------:|----------:|--------------:|-------------:|-------------:|
| BTC | Weekly | $100 | 2025-01-01 | $ | | $ | $ | % |
| ETH | Bi-weekly | $75 | 2025-01-01 | $ | | $ | $ | % |
| SOL | Monthly | $50 | 2025-03-01 | $ | | $ | $ | % |

`FORMULA (Total Invested): =SUMIFS(TransactionLog!F:F, TransactionLog!C:C, A2, TransactionLog!B:B, "Buy")`
`FORMULA (Avg Price Paid): =TotalInvested / TotalQty`
`FORMULA (DCA Return %): =(CurrentPrice - AvgPricePaid) / AvgPricePaid * 100`

---

## DCA Buy History

| Date | Asset | Amount Invested | Price at Purchase | Qty Acquired | Running Avg Price | Running Total Qty | Running Total Invested |
|------|-------|----------------:|------------------:|-------------:|------------------:|------------------:|-----------------------:|
| 2025-01-06 | BTC | $100 | $43,200 | 0.00231 | $43,200 | 0.00231 | $100 |
| 2025-01-13 | BTC | $100 | $41,800 | 0.00239 | $42,500 | 0.00470 | $200 |
| 2025-01-20 | BTC | $100 | $44,100 | 0.00227 | $43,033 | 0.00697 | $300 |
| 2025-01-27 | BTC | $100 | $43,500 | 0.00230 | $43,150 | 0.00927 | $400 |
| 2025-02-03 | BTC | $100 | $45,200 | 0.00221 | $43,560 | 0.01148 | $500 |

`FORMULA (Running Avg Price): =RunningTotalInvested / RunningTotalQty`
`FORMULA (Running Total Qty): =PreviousRunningQty + CurrentQty`
`FORMULA (Running Total Invested): =PreviousRunningInvested + CurrentInvestment`

---

## DCA vs. Lump Sum Comparison

| Metric | DCA Strategy | Lump Sum (same total, Day 1) |
|--------|-------------|------------------------------|
| Total Invested | $ | $ |
| Current Value | $ | $ |
| Return % | % | % |
| Max Drawdown | % | % |
| Avg Cost Per Unit | $ | $ |

`FORMULA (Lump Sum Qty): =TotalInvested / PriceOnDay1`
`FORMULA (Lump Sum Value): =LumpSumQty * CurrentPrice`

---

---

# SHEET 6: TAX LOTS

> FIFO and LIFO cost basis tracking. Each purchase creates a "lot." When you sell, lots are matched to determine gain/loss.

---

## Tax Lot Ledger (FIFO — First In, First Out)

| Lot # | Date Acquired | Asset | Qty Acquired | Cost/Unit | Total Cost Basis | Qty Remaining | Status | Date Disposed | Proceeds | Gain/Loss | Term |
|-------|--------------|-------|-------------:|----------:|-----------------:|--------------:|--------|--------------|----------:|----------:|------|
| 1 | 2025-01-15 | BTC | 0.25 | $42,063 | $10,515.75 | 0.15 | Partial | 2025-04-01 | $5,200 | $993.70 | Short |
| 2 | 2025-02-15 | BTC | 0.15 | $44,567 | $6,685.01 | 0.15 | Open | | | | |
| 3 | 2025-02-01 | ETH | 5.0 | $2,303.45 | $11,517.25 | 3.0 | Partial | 2025-03-10 | $5,000 | $393.10 | Short |
| 4 | 2025-03-01 | ETH | 0.012 | $2,450 | $29.40 | 0.012 | Open | | | | |
| 5 | 2025-03-10 | SOL | 35.0 | $143.10 | $5,008.50 | 35.0 | Open | | | | |

---

## FIFO Matching Logic

When a SELL occurs:
1. Find the OLDEST open lot for that asset
2. Match sell quantity against that lot
3. If sell qty < lot qty: partially close lot, reduce "Qty Remaining"
4. If sell qty > lot qty: fully close lot, move excess to next oldest lot
5. Calculate gain: Proceeds - (Qty Sold * Cost/Unit of matched lot) - Fees

`FORMULA (Gain/Loss for full lot close): =Proceeds - TotalCostBasis - Fees`
`FORMULA (Gain/Loss for partial): =(SellPrice * QtySold) - (Cost/Unit * QtySold) - Fees`
`FORMULA (Term): =IF(DateDisposed - DateAcquired > 365, "Long", "Short")`

---

## LIFO Alternative (Last In, First Out)

Same structure but matching logic reversed — sell against NEWEST lot first. To switch:

`FORMULA (LIFO Sort): =SORT(OpenLots, DateAcquired, FALSE)`

| Method | When to Use |
|--------|------------|
| FIFO | Default IRS method. Use unless you specifically elect otherwise. Results in long-term gains sooner. |
| LIFO | Matches against most recent purchases. Can result in smaller gains if recent prices are higher. Must elect with IRS. |
| Specific ID | Choose exactly which lot to sell. Maximum tax optimization. Requires documentation. |

---

---

# SHEET 7: TAX SUMMARY

> Year-end tax report. Separates short-term and long-term gains, staking income, and provides totals for Schedule D and Form 8949.

---

## Tax Year Summary (enter year at top)

**Tax Year:** 2025

---

## Capital Gains Summary

| Category | Proceeds | Cost Basis | Gain/Loss |
|----------|--------:|-----------:|----------:|
| **Short-Term Capital Gains** (held < 1 year) | $ | $ | $ |
| **Long-Term Capital Gains** (held > 1 year) | $ | $ | $ |
| **Total Capital Gains** | **$** | **$** | **$** |

`FORMULA (Short-Term Proceeds): =SUMIFS(TaxLots!Proceeds, TaxLots!Term, "Short", YEAR(TaxLots!DateDisposed), TaxYear)`
`FORMULA (Short-Term Basis): =SUMIFS(TaxLots!TotalCostBasis, TaxLots!Term, "Short", YEAR(TaxLots!DateDisposed), TaxYear)`
`FORMULA (Gain/Loss): =Proceeds - CostBasis`

---

## Ordinary Income (Staking, Mining, Airdrops)

| Income Type | Total Received (USD) | Number of Events |
|-------------|---------------------:|-----------------:|
| Staking Rewards | $ | |
| Mining Income | $ | |
| Airdrops | $ | |
| Other Crypto Income | $ | |
| **Total Ordinary Income** | **$** | |

`FORMULA: =SUMIFS(TransactionLog!F:F, TransactionLog!B:B, "Staking Reward", YEAR(TransactionLog!A:A), TaxYear)`

---

## Form 8949 Data (Short-Term — Part I)

| Description | Date Acquired | Date Sold | Proceeds | Cost Basis | Gain/Loss |
|-------------|--------------|-----------|--------:|-----------:|----------:|
| 0.10 BTC | 2025-01-15 | 2025-04-01 | $5,200 | $4,206.30 | $993.70 |
| 2.0 ETH (swap) | 2025-02-01 | 2025-03-10 | $5,000 | $4,606.90 | $393.10 |

---

## Form 8949 Data (Long-Term — Part II)

| Description | Date Acquired | Date Sold | Proceeds | Cost Basis | Gain/Loss |
|-------------|--------------|-----------|--------:|-----------:|----------:|
| (entries for assets held > 365 days) | | | | | |

---

## Tax Liability Estimate

| Bracket | Rate Applied | Amount | Tax Owed |
|---------|-------------|-------:|---------:|
| Short-Term Gains (taxed as ordinary income) | % | $ | $ |
| Long-Term Gains | 0% / 15% / 20% | $ | $ |
| Staking/Mining Income | % | $ | $ |
| **Estimated Total Crypto Tax** | | | **$** |

---

## Wash Sale Warning

Crypto is NOT currently subject to wash sale rules (as of 2025 tax year), but this may change. Track 30-day repurchases for awareness:

| Asset Sold at Loss | Date Sold | Loss Amount | Repurchased Within 30 Days? | Repurchase Date |
|-------------------|-----------|------------:|:---------------------------:|----------------|
| | | $ | Yes/No | |

---

---

# FORMULA REFERENCE GUIDE

---

## Portfolio Calculations

**Current value of holdings:**
```
=Quantity * CurrentPrice
```

**Unrealized gain/loss:**
```
=CurrentValue - CostBasis
```

**Portfolio allocation:**
```
=AssetValue / TotalPortfolioValue * 100
```

## Cost Basis (FIFO)

**Cost basis for a sell (FIFO):**
```
=QtySold * CostPerUnit_of_oldest_open_lot
```

**Gain/Loss on sale:**
```
=Proceeds - CostBasis - Fees
```

## DCA Calculations

**Running average cost:**
```
=SUMIFS(Value, Asset, "BTC", Type, "Buy") / SUMIFS(Qty, Asset, "BTC", Type, "Buy")
```

## Tax Categorization

**Holding period:**
```
=IF(DAYS(SellDate, BuyDate) > 365, "Long-Term", "Short-Term")
```

## Conditional Formatting Rules

**Positive P&L (green):**
```
=G2 > 0
```

**Negative P&L (red):**
```
=G2 < 0
```

**Overweight position (orange, >5% over target):**
```
=E2 - F2 > 5
```

**Stale price warning (yellow, price not updated in 7 days):**
```
=TODAY() - LastUpdateDate > 7
```

---

> **NOTE:** This tracker is completely offline and private. No API connections are required. For current prices, you can use Google Sheets' GOOGLEFINANCE function for major coins, or manually update prices from CoinGecko/CoinMarketCap. All tax calculations are estimates — consult a CPA familiar with cryptocurrency for final tax filing. This template follows US tax rules; adjust for your jurisdiction.
