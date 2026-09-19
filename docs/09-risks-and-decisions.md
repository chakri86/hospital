# Risk, assumption and decision register

All owners below are roles to be assigned. No person or institution has accepted an assignment merely by appearing in this plan.

## Risk register

| ID | Risk | Rating | Mitigation and early warning | Owner |
|---|---|---|---|---|
| R-01 | Staff reject added documentation | High | Observe workflow; pause if capture <80% or median extra time >2 minutes | Product/clinical |
| R-02 | Price insufficient for service cost | High | Measure hours and collections; paid continuation gate | Commercial/finance |
| R-03 | Cross-tenant disclosure | Critical | Defense in depth and T-01 across APIs, jobs and objects | Security |
| R-04 | Wrong-patient merge | Critical | No automatic demographic merge; reviewed reversible linkage | Clinical/data |
| R-05 | Medication or result corruption | Critical | Sign-off, revisions, unit validation and exception queues | Clinical/engineering |
| R-06 | Offline loss/stale permissions | High | Bounded cache/lease, no offline sharing, recovery workflow | Engineering |
| R-07 | Unlawful secondary use | Critical | Purpose review, contracts, ethics process and controlled output | Privacy/governance |
| R-08 | Government payment/procurement delay | High | Exclude revenue from baseline; cost contract separately | Sponsor/finance |
| R-09 | Vendor blocks interface | High | Confirm contract/API/export rights before sale | Integration |
| R-10 | Biased state-level conclusions | High | Coverage labels, denominators and epidemiological review | Analytics |
| R-11 | Cash exhausted before retention proven | High | Monthly cash forecast, tranche gates, downside reserve | Finance |
| R-12 | Over-customization | High | Standard scope and paid change orders | Product |
| R-13 | Voice/OCR clinical errors | High | Defer; human review and separate safety evidence | Clinical |
| R-14 | False certification/market claims | High | Evidence register; distinguish proposed from approved | Sponsor |

## Decisions

| ID | Decision | Current position | Evidence needed / deadline |
|---|---|---|---|
| D-01 | Repository | chakri86/hospital, specified by user | Established |
| D-02 | Launch cluster | Unselected; choose strongest accessible clinical network | Interviews, by G0 |
| D-03 | Initial clinical scope | Proposed adult outpatient chronic-care workflow | Clinical and buyer agreement, G0 |
| D-04 | Funding | Owner budget unprovided; use scenario envelopes | Capital/runway decision before hiring |
| D-05 | Legal entity | Unselected | Incorporation/counsel before contracts |
| D-06 | Clinical partner | Unappointed | Named reviewer before clinical design sign-off |
| D-07 | Cloud/vendor | Unselected; India-region managed baseline | Quotes and review before G2 |
| D-08 | Offline finalization | Draft-only in v0.1 | Separate approval to expand |
| D-09 | Data commercialization | Subscriptions/services; research only per approved project | No dataset-sale assumption |
| D-10 | Product name/license | Working description only; no license granted | Owner/trademark/legal review |
| D-11 | ABDM production scope | Planned, no access or approval yet | Current onboarding requirements |
| D-12 | Report baseline | v0.1.0 proposal | Revise after discovery |

## Assumptions to replace with evidence

The price mix, monthly gross customer additions, churn, direct support cost, acquisition cost, onboarding effort, salary envelope, bad debt, collection lag, capex and cloud expense are all model inputs. Facility count, disease burden, procurement probability, integration prices and clinical outcomes are not validated. The two-state ambition does not establish market size or permission to use state data.

## Stop or re-scope conditions

Do not expand if critical safety/security controls fail, legal authority to process data is unresolved, paid continuation is below the pilot gate or contribution economics remain negative after pricing/service redesign. If clinical capture is rejected but integration demand exists, investigate a narrower connector/reporting product. Reduce burn while testing the revised hypothesis; do not solve weak adoption by increasing the sales target.
