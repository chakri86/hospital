#!/usr/bin/env python3
"""Deterministic 60-month planning model. INR, no third-party dependencies."""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_inputs(a):
    assert a["months"] == 60, "This report template models five complete years"
    assert math.isclose(sum(s["share"] for s in a["subscription_mix"]), 1)
    for s in a["subscription_mix"]:
        assert 0 <= s["share"] <= 1 and s["monthly_price"] >= 0
    assert 0 <= a["bad_debt_fraction"] < 1
    assert isinstance(a["collection_lag_months"], int) and a["collection_lag_months"] >= 0
    for k in ("fixed_operating_monthly_by_year", "fixed_cloud_monthly_by_year", "capex_at_start_of_year"):
        assert len(a[k]) == 5 and all(v >= 0 for v in a[k])
    for k in ("setup_fee_per_new_facility", "acquisition_cost_per_new_facility",
              "onboarding_cost_per_new_facility", "direct_monthly_cost_per_average_facility",
              "funding_buffer_fraction"):
        assert a[k] >= 0
    for s in a["scenarios"].values():
        assert 0 <= s["monthly_churn"] < 1
        assert len(s["gross_adds_per_month_by_year"]) == 5
        assert all(v >= 0 for v in s["gross_adds_per_month_by_year"])


def simulate(a, scenario, price_factor=1.0, direct_cost_factor=1.0):
    s = a["scenarios"][scenario]
    arpu = sum(x["share"] * x["monthly_price"] for x in a["subscription_mix"]) * price_factor
    direct_cost = a["direct_monthly_cost_per_average_facility"] * direct_cost_factor
    rows, end_customers, cumulative_cash = [], 0.0, 0.0
    for month in range(1, a["months"] + 1):
        yi = (month - 1) // 12
        opening = end_customers
        churned = opening * s["monthly_churn"]
        retained = opening - churned
        new = s["gross_adds_per_month_by_year"][yi]
        # Expected-value cohorts, with churn at start and additions uniformly in month.
        average = retained + new / 2
        end_customers = retained + new
        subscription = average * arpu
        setup = new * a["setup_fee_per_new_facility"]
        revenue = subscription + setup
        bad_debt = revenue * a["bad_debt_fraction"]
        direct = average * direct_cost
        acquisition = new * a["acquisition_cost_per_new_facility"]
        onboarding = new * a["onboarding_cost_per_new_facility"]
        fixed = a["fixed_operating_monthly_by_year"][yi]
        cloud = a["fixed_cloud_monthly_by_year"][yi]
        cash_cost = direct + acquisition + onboarding + fixed + cloud
        ebitda = revenue - bad_debt - cash_cost
        capex = a["capex_at_start_of_year"][yi] if (month - 1) % 12 == 0 else 0
        collect_index = month - 1 - a["collection_lag_months"]
        if a["collection_lag_months"] == 0:
            collection = revenue - bad_debt
        else:
            collection = rows[collect_index]["revenue"] * (1 - a["bad_debt_fraction"]) if collect_index >= 0 else 0
        cash_flow = collection - cash_cost - capex
        cumulative_cash += cash_flow
        rows.append(dict(month=month, year=yi+1, opening_facilities=opening,
                         churned_facilities=churned, new_facilities=new,
                         average_billable_facilities=average, ending_facilities=end_customers,
                         subscription_revenue=subscription, setup_revenue=setup, revenue=revenue,
                         bad_debt=bad_debt, direct_service_cost=direct,
                         acquisition_cost=acquisition, onboarding_cost=onboarding,
                         fixed_operating_cost=fixed, fixed_cloud_cost=cloud,
                         cash_operating_cost=cash_cost, ebitda=ebitda,
                         collections=collection, capex=capex, cash_flow=cash_flow,
                         cumulative_cash=cumulative_cash, exit_arr=end_customers*arpu*12))
    annual = []
    sum_fields = ["new_facilities", "churned_facilities", "subscription_revenue", "setup_revenue",
                  "revenue", "bad_debt", "direct_service_cost", "acquisition_cost", "onboarding_cost",
                  "fixed_operating_cost", "fixed_cloud_cost", "cash_operating_cost", "ebitda",
                  "collections", "capex", "cash_flow"]
    for year in range(1, 6):
        block = rows[(year-1)*12:year*12]
        item = {k: sum(r[k] for r in block) for k in sum_fields}
        item.update(year=year, ending_facilities=block[-1]["ending_facilities"],
                    average_billable_facilities=sum(r["average_billable_facilities"] for r in block)/12,
                    exit_arr=block[-1]["exit_arr"], cumulative_cash=block[-1]["cumulative_cash"])
        annual.append(item)
    deficit = max(0, -min(r["cumulative_cash"] for r in rows))
    positive_year = next((r["year"] for r in annual if r["ebitda"] > 0), None)
    # First month followed by at least six observed positive months and no later negative month.
    sustained = next((r["month"] for i, r in enumerate(rows)
                      if len(rows)-i >= 6 and all(t["ebitda"] > 0 for t in rows[i:])), None)
    outstanding = sum(r["revenue"]-r["bad_debt"] for r in rows) - sum(r["collections"] for r in rows)
    contribution = arpu * (1-a["bad_debt_fraction"]) - direct_cost
    break_even = [math.ceil((f+c)/contribution) if contribution > 0 else None
                  for f, c in zip(a["fixed_operating_monthly_by_year"], a["fixed_cloud_monthly_by_year"])]
    result = dict(scenario=scenario, monthly_arpu=arpu, monthly_contribution=contribution,
                  recurring_contribution_margin=contribution/arpu if arpu else None,
                  cac_payback_months=a["acquisition_cost_per_new_facility"]/contribution if contribution > 0 else None,
                  operating_break_even_average_facilities=break_even,
                  first_positive_annual_ebitda_year=positive_year,
                  sustained_positive_month=sustained, peak_cash_deficit=deficit,
                  funding_with_buffer=deficit*(1+a["funding_buffer_fraction"]),
                  closing_net_receivables=outstanding, annual=annual, monthly=rows)
    check_reconciliation(result)
    return result


def check_reconciliation(r):
    for m in r["monthly"]:
        close = math.isclose
        assert close(m["opening_facilities"] - m["churned_facilities"] + m["new_facilities"], m["ending_facilities"])
        assert close(m["subscription_revenue"] + m["setup_revenue"], m["revenue"])
        assert close(m["revenue"]-m["bad_debt"]-m["cash_operating_cost"], m["ebitda"], abs_tol=1e-6)
    earnings = sum(y["ebitda"] for y in r["annual"])
    capex = sum(y["capex"] for y in r["annual"])
    assert math.isclose(earnings-capex-r["closing_net_receivables"],
                        r["monthly"][-1]["cumulative_cash"], abs_tol=1e-5)


def lakhs(value):
    return f"{value/100000:,.2f}"


def render(a, results, sensitivity):
    out = ["# Financial results — generated", "",
           f"Version {a['version']} · Assumptions dated {a['as_of']} · All money in INR lakh unless stated.", "",
           "Reproduce with `python3 scripts/financial_model.py`. Edit assumptions, not this file. "
           "These are hypothetical scenarios, not verified forecasts or investment promises.", "",
           "## Scenario comparison", "",
           "| Scenario | Y5 ending facilities | Y5 revenue | Y5 EBITDA | First profitable EBITDA year | Peak cash deficit | Funding +20% buffer |",
           "|---|---:|---:|---:|---|---:|---:|"]
    for name, r in results.items():
        y = r["annual"][-1]
        py = f"Year {r['first_positive_annual_ebitda_year']}" if r["first_positive_annual_ebitda_year"] else "None in five years"
        out.append(f"| {name.title()} | {y['ending_facilities']:,.1f} | {lakhs(y['revenue'])} | {lakhs(y['ebitda'])} | {py} | {lakhs(r['peak_cash_deficit'])} | {lakhs(r['funding_with_buffer'])} |")
    out += ["", "Funding is the modeled peak cumulative monthly deficit plus buffer, excluding tax, financing and omitted contract-specific costs. "
            "A downside that continues losing money requires a stop/re-scope decision; more funding alone does not make it viable."]
    for name, r in results.items():
        out += ["", f"## {name.title()} — annual detail", "",
                "| Year | Avg paying facilities | Ending facilities | Subscription | Setup | Total revenue | Cash operating costs | Bad debt | EBITDA | Capex | Net cash flow | Exit ARR |",
                "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for y in r["annual"]:
            keys = ["subscription_revenue", "setup_revenue", "revenue", "cash_operating_cost", "bad_debt", "ebitda", "capex", "cash_flow", "exit_arr"]
            out.append(f"| {y['year']} | {y['average_billable_facilities']:,.1f} | {y['ending_facilities']:,.1f} | " + " | ".join(lakhs(y[k]) for k in keys) + " |")
        sustained = f"month {r['sustained_positive_month']}" if r["sustained_positive_month"] else "not achieved within the horizon"
        out += ["", f"Sustained positive monthly EBITDA: {sustained}. This means at least six observed positive months followed by no later negative month in the model. "
                "Positive annual EBITDA does not mean accumulated investment has been recovered.", "",
                f"Closing net receivables: ₹{lakhs(r['closing_net_receivables'])} lakh. "
                f"Five-year cumulative cash flow before financing: ₹{lakhs(r['monthly'][-1]['cumulative_cash'])} lakh."]
    b = results["base"]
    out += ["", "## Base unit economics and operating break-even", "",
            f"Weighted monthly subscription: ₹{b['monthly_arpu']:,.0f}. Recurring contribution after modeled bad debt and direct service cost: "
            f"₹{b['monthly_contribution']:,.0f}/facility/month ({b['recurring_contribution_margin']:.1%}). "
            f"CAC-only payback: {b['cac_payback_months']:.2f} months of this contribution, excluding onboarding, fixed overhead, tax and financing.", "",
            "| Cost year | Fixed operations + cloud per month, lakh | Average billable facilities to cover those costs |",
            "|---|---:|---:|"]
    for i, n in enumerate(b["operating_break_even_average_facilities"]):
        out.append(f"| {i+1} | {lakhs(a['fixed_operating_monthly_by_year'][i]+a['fixed_cloud_monthly_by_year'][i])} | {n} |")
    out += ["", "Break-even here excludes acquisition and onboarding for replacement/growth customers, setup contribution and capex. "
            "It is an operating sensitivity, not a sustainable total-business break-even guarantee. The monthly model includes those cash costs.", "",
            "## Base sensitivities", "",
            "| Change | Y5 revenue | Y5 EBITDA | Funding +20% buffer | First profitable EBITDA year |",
            "|---|---:|---:|---:|---|"]
    for label, r in sensitivity.items():
        y = r["annual"][-1]
        py = r["first_positive_annual_ebitda_year"] or "None"
        out.append(f"| {label} | {lakhs(y['revenue'])} | {lakhs(y['ebitda'])} | {lakhs(r['funding_with_buffer'])} | {py} |")
    y1 = b["annual"][0]
    out += ["", "## First-year expense bridge — base", "",
            "| Item | INR lakh |", "|---|---:|"]
    for k, label in [("fixed_operating_cost", "Fixed operating expense"), ("fixed_cloud_cost", "Fixed cloud/platform"),
                     ("direct_service_cost", "Direct facility service"), ("acquisition_cost", "Customer acquisition"),
                     ("onboarding_cost", "Facility onboarding"), ("capex", "Equipment/capital purchases")]:
        out.append(f"| {label} | {lakhs(y1[k])} |")
    out += [f"| Gross cash spending before collections | {lakhs(y1['cash_operating_cost']+y1['capex'])} |",
            f"| Cash collections | {lakhs(y1['collections'])} |",
            f"| Net cash outflow | {lakhs(-y1['cash_flow'])} |", "",
            "## Interpretation", "",
            "Recognized revenue uses average billable facilities, not ending customers. Exit ARR includes subscriptions only. "
            "EBITDA includes a 2% modeled bad-debt expense; it is not net profit or distributable cash. "
            "Cash costs are paid in the month incurred; collections follow the input lag. Capex is paid at each year's start. "
            "No terminal value, tax benefit, funding proceeds, government subsidy, research sale or valuation is assumed.", "",
            "Full unrounded monthly values are in [results.json](results.json). Rounding can create small visible total differences. "
            "See [ASSUMPTIONS.md](ASSUMPTIONS.md) for exclusions and formulas.", ""]
    return "\n".join(out)


def main():
    a = json.loads((ROOT / "finance/assumptions.json").read_text())
    validate_inputs(a)
    results = {name: simulate(a, name) for name in a["scenarios"]}
    sensitivity = {
        "Subscription prices -20%": simulate(a, "base", price_factor=0.8),
        "Direct service cost +50%": simulate(a, "base", direct_cost_factor=1.5),
        "Both changes": simulate(a, "base", price_factor=0.8, direct_cost_factor=1.5),
    }
    (ROOT / "finance/results.json").write_text(json.dumps({"assumptions": a, "scenarios": results,
                                                         "sensitivities": sensitivity}, indent=2) + "\n")
    (ROOT / "finance/RESULTS.md").write_text(render(a, results, sensitivity))
    summary = ["All amounts below are **INR crore**, generated from the same model. These are hypothetical scenarios.", "",
               "| Scenario | Year 5 revenue | Year 5 EBITDA | First positive annual EBITDA | Funding including 20% buffer |",
               "|---|---:|---:|---|---:|"]
    for name, r in results.items():
        y5 = r["annual"][-1]
        first = f"Year {r['first_positive_annual_ebitda_year']}" if r["first_positive_annual_ebitda_year"] else "None in five years"
        summary.append(f"| {name.title()} | {y5['revenue']/10000000:.2f} | {y5['ebitda']/10000000:.2f} | {first} | {r['funding_with_buffer']/10000000:.2f} |")
    b = results["base"]
    y1 = b["annual"][0]
    summary += ["", f"Base first-year gross cash spending is **₹{lakhs(y1['cash_operating_cost']+y1['capex'])} lakh**; "
                f"modeled collections reduce first-year net outflow to **₹{lakhs(-y1['cash_flow'])} lakh**. "
                f"Even with positive Year 5 EBITDA, the base case ends the five years with cumulative pre-financing cash flow of "
                f"**₹{b['monthly'][-1]['cumulative_cash']/10000000:.2f} crore**; the original investment has not yet been recovered."]
    report = ROOT / "PROJECT_REPORT.md"
    replaced, count = re.subn(r"(?s)<!-- FINANCIAL_SUMMARY_START -->.*?<!-- FINANCIAL_SUMMARY_END -->",
                              "<!-- FINANCIAL_SUMMARY_START -->\n" + "\n".join(summary) + "\n<!-- FINANCIAL_SUMMARY_END -->",
                              report.read_text())
    assert count == 1, "Report must have exactly one financial summary block"
    report.write_text(replaced)
    print("Generated finance/RESULTS.md and finance/results.json; customer, earnings and cash reconciliations passed.")
    for name, r in results.items():
        print(f"{name}: Y5 EBITDA INR lakh {lakhs(r['annual'][-1]['ebitda'])}; "
              f"funding with buffer {lakhs(r['funding_with_buffer'])}; first positive year {r['first_positive_annual_ebitda_year']}")


if __name__ == "__main__":
    main()
