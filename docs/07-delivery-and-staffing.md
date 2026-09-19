# Delivery plan, staffing and backlog

Dates are relative to funded kickoff. No pilot sites or staff are committed yet.

## Stage gates

| Gate | Target | Required evidence | Accountable role |
|---|---|---|---|
| G0 Discovery | Week 6 | 20 interviews, five observations, three written pilot interests, priced workflow | Founder/product sponsor |
| G1 Prototype | Week 12 | Synthetic workflow demonstration, usability results and revised scope | Technical lead with clinician |
| G2 Live pilot readiness | Months 4–6 | Contracts, legal review, clinical safety, isolation/security review, restore proof, training | Sponsor, clinical and privacy leads |
| G3 Pilot evaluation | Months 9–12 | Eight-site evidence, at least five paid continuations, quality/adoption gates | Product and implementation leads |
| G4 Repeatable rollout | Months 13–24 | Onboarding cost/hours, renewals, support load, cash reforecast | Operations lead |
| G5 Second-state scale | Months 25–60 | Replicable cluster economics, governance, staffing and service evidence | Sponsor and governance board |

ABDM integration discovery can begin early, but production approvals depend on external parties. Do not put a guaranteed certification date into a hospital contract.

## First 90 days

Weeks 1–2: select candidate district, recruit clinical advisor, build interview template and map existing tools. Weeks 3–4: observe roles, measure baseline effort, obtain synthetic field examples and test price proposals. Weeks 5–6: agree minimum dataset, pilot terms, workflow scope and legal-review plan. Weeks 7–8: prototype registration, tenant separation, encounter drafts and prescription review. Weeks 9–10: add sample lab results, follow-up and record export. Weeks 11–12: demonstrate exceptions, offline drafts and usability; revise budget and launch gates.

No real records are needed for the first 90-day synthetic prototype. Live testing starts only after G2. The first-year budget supports the broader preparation and pilot, not only the prototype.

## Work breakdown

| Epic | Main tasks | Dependencies | Definition of done |
|---|---|---|---|
| EP-01 Discovery | Interviews, workflow timing, buyer verification | Local access | Evidence-backed scope and customer hypothesis |
| EP-02 Governance | Processing map, contracts, notices, retention | Clinical scope | Signed review determinations for pilot |
| EP-03 Foundation | Environments, tenant model, auth, audit | Architecture | Isolation and role tests pass |
| EP-04 Clinical capture | Registration, encounter, allergy, prescription | PR-01 to PR-07 | Clinician-approved synthetic demonstration |
| EP-05 Laboratory | Orders, import, exceptions, review | Identifiers and EP-04 | Reconciled fixtures including corrections |
| EP-06 Continuity | Follow-up, patient export, reminders | Authorization model | Scope-limited exports and task evidence |
| EP-07 Offline | Encrypted drafts, sync, conflict handling | Foundation | Loss/reconnect/conflict tests pass |
| EP-08 Analytics | Definitions, quality, facility dashboards | Provenance and clinical data | Counts and denominators reconcile |
| EP-09 Integration | Vendor contracts, mapping, ABDM workstream | External access | Required conformance and acceptance evidence |
| EP-10 Live operations | Recovery, incident process, training, support | All P0 controls | G2 sign-off and facility readiness |
| EP-11 Commercialization | Paid pilots, onboarding package, renewal | Measurable value | Collected revenue and service-cost data |

## Team budget envelope

Proposed first-year monthly fixed operating expense is ₹6 lakh, with cloud/platform expense modeled separately. This is a planning allowance requiring hiring and professional-service quotations.

| Function | Monthly allowance | Notes |
|---|---:|---|
| Technical lead/backend | ₹1.50 lakh | Fully loaded planning amount |
| Application engineer | ₹1.10 lakh | Staff interface and client workflow |
| QA and implementation | ₹0.75 lakh | Synthetic testing and facility training |
| Product/operations including founder allowance | ₹0.65 lakh | Coordination and discovery |
| Part-time clinical and design input | ₹0.65 lakh | Clinical lead must have actual review time |
| Legal/security/professional services reserve | ₹0.70 lakh | Annual ₹8.4 lakh envelope; re-quote if insufficient |
| Administration and fixed overhead | ₹0.65 lakh | Travel/overhead not assigned per sale |
| Total | ₹6.00 lakh | Acquisition, onboarding and direct service costs modeled separately |

Do not double-count expense: site-specific sales commissions/travel belong in acquisition; one-time site training/import belongs in onboarding; ongoing site usage and support belongs in direct service costs. Shared salaried staff remain in fixed expense. Actual time tracking should determine whether the model's variable allowances need adjustment.

## Responsibility matrix

| Deliverable | Accountable | Responsible/support |
|---|---|---|
| Scope and funding | Sponsor | Product/finance |
| Clinical dataset and sign-off | Clinical lead | Nurses, doctors, data steward |
| Platform implementation | Technical lead | Engineering and QA |
| Legal applicability | Engaged legal reviewer | Privacy lead and sponsor |
| Data quality | Clinical/data steward | Facility champions and integration team |
| Facility readiness | Implementation lead | Facility administrator |
| Security/recovery | Technical/security lead | Hosting provider and independent reviewer |
| Research approval | Appropriate institution/governance committee | Legal, clinical and independent reviewers |

## Scaling capacity

At district scale, create a repeatable implementation package before hiring multiple local teams. Measure training hours, import hours, incidents per facility, visits per month, recurring support cost and clinical review time. Add staff when those measured workloads exceed safe capacity. Regional staffing is financed in the model's increasing fixed expense, but the model does not prove the staffing is sufficient; reforecast using pilot evidence.
