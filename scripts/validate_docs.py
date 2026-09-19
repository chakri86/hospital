#!/usr/bin/env python3
"""Check local documentation links and the financial model's accounting identities."""
from __future__ import annotations

import json
import math
import re
from pathlib import Path
from financial_model import simulate, validate_inputs

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors, links = [], 0
    docs = sorted(ROOT.rglob("*.md"))
    for path in docs:
        content = path.read_text()
        if len(re.findall(r"^```", content, re.MULTILINE)) % 2:
            errors.append(f"Unbalanced code fence: {path.relative_to(ROOT)}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if re.match(r"^[a-zA-Z]+:", target) or target.startswith("#"):
                continue
            links += 1
            local = target.split("#", 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f"Missing link target in {path.relative_to(ROOT)}: {target}")
    a = json.loads((ROOT / "finance/assumptions.json").read_text())
    validate_inputs(a)
    saved = json.loads((ROOT / "finance/results.json").read_text())
    if saved["assumptions"] != a:
        errors.append("Financial output assumptions are stale")
    for name in a["scenarios"]:
        if saved["scenarios"][name] != simulate(a, name):
            errors.append(f"Stale scenario results: {name}")
    sensitivity_inputs = {
        "Subscription prices -20%": (0.8, 1.0),
        "Direct service cost +50%": (1.0, 1.5),
        "Both changes": (0.8, 1.5),
    }
    for name, (price, direct) in sensitivity_inputs.items():
        if saved["sensitivities"][name] != simulate(a, "base", price, direct):
            errors.append(f"Stale sensitivity: {name}")
    # Independent small arithmetic check against a fixed fixture, not user-editable inputs.
    fixture = dict(a)
    fixture.update(subscription_mix=[dict(share=1.0, monthly_price=8000)],
                   setup_fee_per_new_facility=20000, acquisition_cost_per_new_facility=22000,
                   onboarding_cost_per_new_facility=12000,
                   direct_monthly_cost_per_average_facility=1600, bad_debt_fraction=0.02,
                   collection_lag_months=1, fixed_operating_monthly_by_year=[600000]*5,
                   fixed_cloud_monthly_by_year=[40000]*5, capex_at_start_of_year=[500000]*5,
                   scenarios={"fixture": dict(monthly_churn=0.015, gross_adds_per_month_by_year=[2]*5)})
    trial = simulate(fixture, "fixture")
    expected = [("ending_facilities", 2), ("revenue", 48000), ("ebitda", -662560),
                ("cash_flow", -1209600)]
    for field, value in expected:
        if not math.isclose(trial["monthly"][0][field], value, abs_tol=0.01):
            errors.append(f"Independent month-one arithmetic failed: {field}")
    if not math.isclose(trial["monthly"][1]["collections"], 47040):
        errors.append("Collection lag/bad-debt check failed")
    if not math.isclose(trial["monthly"][1]["ending_facilities"], 3.97):
        errors.append("Churn cohort check failed")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(docs)} Markdown documents; {links} local links; balanced fences; "
          "three scenarios and three sensitivities current; independent cohort/cash checks passed.")


if __name__ == "__main__":
    main()
