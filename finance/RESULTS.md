# Financial results — generated

Version 0.1.0 · Assumptions dated 2026-09-19 · All money in INR lakh unless stated.

Reproduce with `python3 scripts/financial_model.py`. Edit assumptions, not this file. These are hypothetical scenarios, not verified forecasts or investment promises.

## Scenario comparison

| Scenario | Y5 ending facilities | Y5 revenue | Y5 EBITDA | First profitable EBITDA year | Peak cash deficit | Funding +20% buffer |
|---|---:|---:|---:|---|---:|---:|
| Downside | 478.3 | 430.09 | -222.53 | None in five years | 798.62 | 958.35 |
| Base | 1,091.6 | 954.27 | 96.33 | Year 5 | 354.92 | 425.91 |
| Upside | 1,846.6 | 1,586.84 | 481.74 | Year 3 | 211.90 | 254.28 |

Funding is the modeled peak cumulative monthly deficit plus buffer, excluding tax, financing and omitted contract-specific costs. A downside that continues losing money requires a stop/re-scope decision; more funding alone does not make it viable.

## Downside — annual detail

| Year | Avg paying facilities | Ending facilities | Subscription | Setup | Total revenue | Cash operating costs | Bad debt | EBITDA | Capex | Net cash flow | Exit ARR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.4 | 10.5 | 5.22 | 2.40 | 7.62 | 81.92 | 0.15 | -74.45 | 5.00 | -80.43 | 10.06 |
| 2 | 30.7 | 49.7 | 29.46 | 9.60 | 39.06 | 138.61 | 0.78 | -100.34 | 3.00 | -106.88 | 47.67 |
| 3 | 96.7 | 141.4 | 92.81 | 24.00 | 116.81 | 253.76 | 2.34 | -139.29 | 8.00 | -155.42 | 135.79 |
| 4 | 218.4 | 293.0 | 209.62 | 43.20 | 252.82 | 427.36 | 5.06 | -179.60 | 10.00 | -202.74 | 281.31 |
| 5 | 385.5 | 478.3 | 370.09 | 60.00 | 430.09 | 644.02 | 8.60 | -222.53 | 15.00 | -253.15 | 459.13 |

Sustained positive monthly EBITDA: not achieved within the horizon. This means at least six observed positive months followed by no later negative month in the model. Positive annual EBITDA does not mean accumulated investment has been recovered.

Closing net receivables: ₹41.42 lakh. Five-year cumulative cash flow before financing: ₹-798.62 lakh.

## Base — annual detail

| Year | Avg paying facilities | Ending facilities | Subscription | Setup | Total revenue | Cash operating costs | Bad debt | EBITDA | Capex | Net cash flow | Exit ARR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 11.3 | 22.1 | 10.86 | 4.80 | 15.66 | 87.13 | 0.31 | -71.79 | 5.00 | -78.83 | 21.23 |
| 2 | 65.3 | 106.9 | 62.71 | 19.20 | 81.91 | 161.58 | 1.64 | -81.31 | 3.00 | -91.90 | 102.63 |
| 3 | 210.2 | 310.3 | 201.74 | 48.00 | 249.74 | 316.35 | 4.99 | -71.60 | 8.00 | -97.43 | 297.92 |
| 4 | 479.6 | 645.9 | 460.44 | 84.00 | 544.44 | 546.89 | 10.89 | -13.34 | 10.00 | -52.00 | 620.05 |
| 5 | 869.0 | 1,091.6 | 834.27 | 120.00 | 954.27 | 838.85 | 19.09 | 96.33 | 15.00 | 44.03 | 1,047.98 |

Sustained positive monthly EBITDA: month 52. This means at least six observed positive months followed by no later negative month in the model. Positive annual EBITDA does not mean accumulated investment has been recovered.

Closing net receivables: ₹93.43 lakh. Five-year cumulative cash flow before financing: ₹-276.13 lakh.

## Upside — annual detail

| Year | Avg paying facilities | Ending facilities | Subscription | Setup | Total revenue | Cash operating costs | Bad debt | EBITDA | Capex | Net cash flow | Exit ARR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 17.3 | 34.1 | 16.61 | 7.20 | 23.81 | 92.36 | 0.48 | -69.03 | 5.00 | -77.17 | 32.72 |
| 2 | 101.2 | 166.6 | 97.11 | 28.80 | 125.91 | 184.78 | 2.52 | -61.39 | 3.00 | -76.19 | 159.89 |
| 3 | 329.1 | 488.5 | 315.97 | 72.00 | 387.97 | 379.99 | 7.76 | 0.22 | 8.00 | -35.84 | 468.93 |
| 4 | 775.1 | 1,057.9 | 744.07 | 132.00 | 876.07 | 685.21 | 17.52 | 173.33 | 10.00 | 114.77 | 1,015.54 |
| 5 | 1,453.0 | 1,846.6 | 1,394.84 | 192.00 | 1,586.84 | 1,073.37 | 31.74 | 481.74 | 15.00 | 400.98 | 1,772.73 |

Sustained positive monthly EBITDA: month 38. This means at least six observed positive months followed by no later negative month in the model. Positive annual EBITDA does not mean accumulated investment has been recovered.

Closing net receivables: ₹157.32 lakh. Five-year cumulative cash flow before financing: ₹326.55 lakh.

## Base unit economics and operating break-even

Weighted monthly subscription: ₹8,000. Recurring contribution after modeled bad debt and direct service cost: ₹6,240/facility/month (78.0%). CAC-only payback: 3.53 months of this contribution, excluding onboarding, fixed overhead, tax and financing.

| Cost year | Fixed operations + cloud per month, lakh | Average billable facilities to cover those costs |
|---|---:|---:|
| 1 | 6.40 | 103 |
| 2 | 9.70 | 156 |
| 3 | 16.20 | 260 |
| 4 | 26.00 | 417 |
| 5 | 39.00 | 625 |

Break-even here excludes acquisition and onboarding for replacement/growth customers, setup contribution and capex. It is an operating sensitivity, not a sustainable total-business break-even guarantee. The monthly model includes those cash costs.

## Base sensitivities

| Change | Y5 revenue | Y5 EBITDA | Funding +20% buffer | First profitable EBITDA year |
|---|---:|---:|---:|---|
| Subscription prices -20% | 787.41 | -67.19 | 682.35 | None |
| Direct service cost +50% | 954.27 | 12.90 | 551.54 | 5 |
| Both changes | 787.41 | -150.62 | 868.96 | None |

## First-year expense bridge — base

| Item | INR lakh |
|---|---:|
| Fixed operating expense | 72.00 |
| Fixed cloud/platform | 4.80 |
| Direct facility service | 2.17 |
| Customer acquisition | 5.28 |
| Facility onboarding | 2.88 |
| Equipment/capital purchases | 5.00 |
| Gross cash spending before collections | 92.13 |
| Cash collections | 13.30 |
| Net cash outflow | 78.83 |

## Interpretation

Recognized revenue uses average billable facilities, not ending customers. Exit ARR includes subscriptions only. EBITDA includes a 2% modeled bad-debt expense; it is not net profit or distributable cash. Cash costs are paid in the month incurred; collections follow the input lag. Capex is paid at each year's start. No terminal value, tax benefit, funding proceeds, government subsidy, research sale or valuation is assumed.

Full unrounded monthly values are in [results.json](results.json). Rounding can create small visible total differences. See [ASSUMPTIONS.md](ASSUMPTIONS.md) for exclusions and formulas.
