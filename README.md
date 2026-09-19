# Andhra Pradesh & Telangana Health Data Platform

**Project owner:** Chakravarthi  
**Documentation version:** 0.1.0 — 19 September 2026  
**Status:** Project definition and feasibility baseline. No clinical application, production deployment, hospital partnership or regulatory approval is represented as completed.

This repository defines a proposed health-data business serving hospitals, clinics and laboratories in Andhra Pradesh and Telangana. It covers clinical data capture, authorized record exchange, facility operations and governed analytics. “State health data” describes the intended geography; this is not an official state-government system.

Start with the [complete project report](PROJECT_REPORT.md). All prices, budgets, growth assumptions and service targets are proposals until validated through quotations, customer interviews, signed agreements and testing.

## Documentation map

| Document | Purpose |
|---|---|
| [Project report](PROJECT_REPORT.md) | Business case, scope, costs, delivery strategy and investment gates |
| [Market and adoption](docs/01-market-and-adoption.md) | Customer discovery, procurement, sales, pricing experiments and competition |
| [Product requirements](docs/02-product-requirements.md) | Personas, clinical workflows, MVP boundaries and acceptance criteria |
| [Architecture](docs/03-architecture.md) | Hosting, tenant isolation, offline synchronization and scaling |
| [Data specification](docs/04-data-specification.md) | Entities, minimum fields, terminology, provenance and analytical definitions |
| [Privacy and governance](docs/05-privacy-and-governance.md) | Proposed controls, research access and legal review register |
| [Interoperability](docs/06-interoperability.md) | ABDM work plan, interfaces and migration strategy |
| [Delivery and staffing](docs/07-delivery-and-staffing.md) | Phases, owners, milestone gates and first 90 days |
| [Financial assumptions](finance/ASSUMPTIONS.md) | Editable five-year model, cost definitions and funding limits |
| [Financial results](finance/RESULTS.md) | Generated monthly-model summaries and sensitivity analysis |
| [Operations and validation](docs/08-operations-and-validation.md) | Security, recovery, clinical safety, test evidence and support |
| [Risk and decision register](docs/09-risks-and-decisions.md) | Unresolved decisions, mitigations and stop conditions |
| [Sources and verification](docs/10-sources-and-verification.md) | Primary sources, checked claims and unresolved legal details |

## Reproduce the financial model

Requires Python 3.10 or newer; no external Python packages are needed.

```bash
python3 scripts/financial_model.py
python3 scripts/validate_docs.py
```

Edit `finance/assumptions.json`, then regenerate `finance/RESULTS.md` and `finance/results.json`. The model is a planning tool, not audited accounts or an investment return forecast. It includes three scenarios, monthly customer movement, collection lag, acquisition and onboarding costs, and a cash funding calculation.

## First build milestone

Complete 20 facility interviews, observe five consultation workflows and obtain three written pilot expressions of interest. In parallel, prototype registration → encounter → clinician-approved prescription → follow-up using synthetic data. The full implementation backlog is in the delivery plan.

## Repository rules

- Commit synthetic examples only. Never commit patient records, patient photographs, prescriptions, identifiers, passwords, keys or production exports.
- Keep proposals, verified facts and operating evidence visibly distinct.
- Update the source register when changing legal or interoperability claims.
- Update the input model rather than manually changing generated financial results.
- Use reviewed pull requests for future changes; the initial report establishes the baseline in this previously empty repository.
- Source-code licensing and any future commercial licensing remain an owner decision; this repository does not grant an open-source license.

See [CONTRIBUTING.md](CONTRIBUTING.md) for documentation maintenance.
