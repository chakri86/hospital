# Financial assumptions and interpretation

The model is a transparent scenario exercise in INR. Every commercial input is unvalidated. It is designed to expose the assumptions behind costs and profits, not provide an investment recommendation, loan projection, company valuation or guaranteed return.

## Files and reproducibility

`assumptions.json` is the editable source. `scripts/financial_model.py` calculates 60 monthly periods, writes `results.json` and generates `RESULTS.md`. There are no external dependencies. Use Python 3.10 or newer. Relative year numbers start at funded kickoff, not a claimed calendar launch date.

## Price and customer mix

60% clinics at ₹3,000/month + 30% small-hospital outpatient deployments at ₹18,000/month + 10% laboratories at ₹8,000/month = ₹8,000 weighted monthly recurring revenue per facility. Mix is held constant for tractability; it is not an observed customer portfolio. Full inpatient hospital software is outside these prices.

Standard setup revenue is ₹20,000 for each new paying facility. Gross additions in the model are paid go-lives after free discovery/pilot work. The monthly first-year additions smooth the rollout for planning; if live approvals are delayed, shift those additions and reforecast. Do not count free pilots as subscription customers.

| Scenario | Monthly churn | Gross new paying facilities/month in Y1 / Y2 / Y3 / Y4 / Y5 |
|---|---:|---|
| Downside | 2.5% | 1 / 4 / 10 / 18 / 25 |
| Base | 1.5% | 2 / 8 / 20 / 35 / 50 |
| Upside | 1.0% | 3 / 12 / 30 / 55 / 80 |

The model uses expected-value fractional facilities, not literal fractional contracts. Monthly churn is applied to opening customers. New facilities contribute half a month of subscription and direct service cost; setup, acquisition and onboarding are fully recognized in their go-live month. Mix, pricing and churn remain constant within each scenario. No price escalation is assumed.

## Cost model

- Acquisition: ₹22,000 per gross new paying facility, an incremental sales-cost allowance. Include attributable sales effort when validating actual CAC.
- Onboarding: ₹12,000 per new facility, separate from acquisition; covers bounded configuration, training and import effort.
- Direct recurring service: ₹1,600 per average billable facility per month. This includes incremental usage and service delivery; shared fixed staffing is separate. Measure and revise support effort, messaging and document usage.
- Fixed operations/month by year: ₹6 / ₹9 / ₹15 / ₹24 / ₹36 lakh. Includes shared payroll, founder allowance, clinical/professional advice and administrative overhead. The first-year staffing bridge is in the delivery plan.
- Fixed cloud/platform/month: ₹0.4 / ₹0.7 / ₹1.2 / ₹2 / ₹3 lakh. These are budget allowances, not provider quotes. Include HA, backups, logs, security and required disaster recovery when obtaining quotes.
- Capex at each year's start: ₹5 / ₹3 / ₹8 / ₹10 / ₹15 lakh for equipment and similar purchases. Engineering costs are expensed rather than capitalized in this planning model.
- Bad debt: 2% of subscription plus setup revenue. This is an allowance; modeled collections exclude the same 2%, avoiding a second cash deduction.

Fixed envelopes rise with scale but are held the same across scenarios to show the effect of slower or faster demand. The upside assumes that this staffing can support the volume; validate before interpreting upside profit. In the downside, management would ordinarily re-scope costs; the unadjusted case deliberately shows the cost of failing to do so.

## Monthly formulas

Opening facilities = previous month's ending facilities. Churn = opening × churn rate. Retained = opening − churn. Ending = retained + new. Average billable facilities = retained + new/2.

Subscription = average × weighted monthly price. Setup = new × setup fee. Revenue = subscription + setup. Bad debt = revenue × bad-debt fraction.

Cash operating cost = direct service + acquisition + onboarding + fixed operations + fixed cloud. EBITDA = revenue − bad debt − cash operating cost.

Collections = collectible revenue from the month specified by the collection lag; there are no opening receivables. Cash flow = collections − cash operating cost − capex. Cumulative cash flow starts at zero before financing.

Peak funding deficit = absolute value of the lowest cumulative monthly cash balance, floored at zero. Funding allowance = peak deficit × 1.20. The 20% buffer is a management assumption and is not also deducted as an expense. Exit ARR = ending facilities × monthly subscription × 12; setup fees are excluded.

Model reconciliation: cumulative EBITDA − capex − closing net receivables = cumulative cash flow. Annual outputs sum monthly values; profit is not computed from ending-customer run rate.

## Break-even and sensitivity

Recurring monthly contribution = ₹8,000 × 98% − ₹1,600 = ₹6,240 in the baseline. CAC-only payback = ₹22,000/₹6,240, approximately 3.53 months. This is optimistic unless the CAC includes all relevant sales effort and retention is demonstrated. It excludes onboarding and shared overhead; it is not payback on total company investment.

At the Year 1 fixed expense level, recurring contribution covers fixed operations and cloud at 103 average billable facilities. At Year 3 it requires 260. These simple break-even points exclude replacement/growth acquisition, onboarding, capex and setup contribution. Use the full monthly results for funding decisions.

Sensitivity runs reduce subscription prices by 20%, increase direct service cost by 50%, and combine both. Setup pricing remains unchanged. Growth/churn are held constant to isolate economic effects; real price changes can also change adoption and retention.

## Important exclusions

Tax/GST, withholding, financing costs, depreciation/amortization, founder distributions, valuation, inflation beyond stepwise expense envelopes, irregular billing disputes, supplier credit terms and foreign-exchange changes are not modeled. Obtain an accountant-reviewed statutory and cash forecast before committing capital. Revenue is exclusive of GST; do not assume healthcare-related software is automatically tax-exempt.

Custom vendor integration fees, unusually large hardware deployments, broad paper digitization, full imaging archives, 24-hour on-site support and government procurement/security obligations must be quoted and added if contracted. No government, research, grant, insurance or pharmaceutical revenue is assumed. No patient-identifiable data sales are assumed.

## Investment decision

First approve a capped discovery tranche, then revise inputs using signed pilot terms and quotations. Fund live pilot preparation only after confirming scope, clinical review capacity and legal authority. Evaluate collected revenue, renewal and customer support cost before releasing regional growth capital. A profitable annual EBITDA number can coexist with a large cumulative cash deficit and does not represent owner profit.
