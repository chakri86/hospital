# Maintaining this project

This is the project-definition baseline, not an implemented hospital system.

1. Use a focused branch and pull request for subsequent work.
2. State the problem, changed behavior, evidence and remaining limitations.
3. Give every new requirement an identifier and measurable acceptance criterion.
4. Record architecture decisions and unresolved choices in the decision register.
5. Update primary sources and verification dates for regulatory claims.
6. Regenerate financial outputs whenever model inputs change.
7. Run `python3 scripts/financial_model.py` and `python3 scripts/validate_docs.py`.
8. Require a clinical reviewer for clinical fields or workflows and a security reviewer for identity, authorization, synchronization or data export.

Never include real patient data in issues, commits, screenshots, tests or support reproductions. Use invented patients and non-contactable example identifiers. Handle future vulnerability reports privately through an owner-designated channel; that channel must be configured before a live product exists.

Version 0.1.0 documents the proposal. Future release notes must distinguish planned, implemented, tested, piloted and released features. Do not mark a capability as completed solely because it appears in this report.
