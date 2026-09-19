# Privacy, security and data governance

This is a proposed control design and legal-review checklist. It is not a legal opinion or certification. Applicable duties depend on the processing purpose, entity roles, commencement notifications, contracts and clinical setting.

## Verified legal context and unresolved detail

The [PIB announcement of 14 November 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) confirms DPDP Rules notification and phased implementation. It describes purpose-specific notices, breach communication, individual rights and special safeguards with limited exceptions. Obtain the current primary legal texts and create a provision-level applicability/commencement matrix before production. The retrieved MeitY framework page did not expose usable legal text; no exact launch-date compliance conclusion is asserted here.

The [CERT-In directions of 28 April 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) require covered entities to report specified cyber incidents within six hours of notice and maintain ICT logs for a rolling 180 days within India. Have counsel confirm applicability and any later amendments; this security-log rule is not a universal retention period for clinical records.

## Processing register

| Activity | Proposed decision owner | Access/control design | Required evidence |
|---|---|---|---|
| Facility clinical care | Facility; platform processes under agreed instructions | Care-team scope and approved retention | Executed service/data agreement and role assessment |
| Patient record access | Relevant facility and authorized platform workflow | Verified requester; scoped export | Identity and disclosure procedure |
| Cross-provider sharing | Parties defined by exchange arrangement | Purpose, recipient, record range and validity | Applicable permission/basis and exchange agreement |
| Operational facility reporting | Facility | Tenant-scoped minimum necessary data | Contracted purpose and access policy |
| Cross-facility benchmarking | Separately determined and reviewed | Approved aggregate outputs, disclosure review | Participation terms and legal basis |
| Research | Sponsor/institution and other parties as assessed | Approved protocol, restricted workspace | Ethics/legal determination and data-use agreement |
| Product telemetry | Platform for documented operating purpose | Exclude clinical text and direct identifiers | Telemetry inventory and vendor review |
| Reminders | Facility-defined care communication | Separate preferences; minimum message content | Notice, contact verification and provider agreement |

Do not automatically classify the company as only a processor for all activities. Independent determination of purposes can alter responsibilities. Do not treat a hospital contract alone as permission for every secondary use of patient information.

## Proposed privacy controls

- Keep data collection tied to stated care, operating or approved research purposes.
- Provide notices in accessible Telugu and English, with version history and a contact for questions.
- Record the appropriate permission or lawful-basis reference per purpose; counsel approves exceptions rather than engineers inventing them.
- Do not condition local registration on optional ABHA linkage or research participation.
- Separate reminders, external record sharing, research and marketing choices.
- Review patient access/correction/erasure requests with identity checks and retention/hold assessment.
- Keep a subprocessor register covering hosting, messaging, support, analytics, transcription and backups.
- Do not send real records to public AI tools or use them for model training by default.
- Do not store unrestricted clinical content in logs, support tickets or product analytics.

## Withdrawal, retention and disclosure

Permission records must support recipient, purpose, data types, date range, expiry and withdrawal time. Stop queued/future processing under a withdrawn permission where applicable and notify relevant processors/recipients through the agreed process. Do not promise that already received records can always be recalled or erased where another lawful retention duty applies.

The retention schedule needs legal review for both states and for each facility type, specialty and record class. A single “delete after X years” setting is insufficient. Backup expiry, legal holds, export expiry and device caches require separate handling. India-region hosting is a project choice; cross-border support and subprocessors need specific assessment.

## Research and aggregate data access

Create a data-access committee comprising a clinical lead, privacy/legal lead, data steward and an independent reviewer when appropriate. Require a defined research question, minimum dataset, approved protocol, funding/conflict declaration, legal basis and ethics determination. Research-specific consent or a justified ethics/legal pathway is evaluated for each project. Routine clinical records do not automatically form a compliant clinical-trial electronic data-capture system.

Use a restricted analysis environment. Keep reidentification keys separate; audit queries and review exports. Set a preliminary small-cell suppression threshold of ten for shared aggregate reports, with complementary suppression and repeated-query controls. This is a proposed minimum control, not a guarantee of anonymization: rare conditions, combinations, free text and external datasets can still reveal identity. Privacy review can require larger cells, coarser geography or denial of release.

Do not publish rankings or prevalence estimates without assessing selection bias, missingness and denominator validity. Commercial data-access approval must not be controlled solely by the sales team. Fees pay for authorized analytical services and project delivery; they do not create data-use rights.

## Security baseline and evidence

Mandatory pilot evidence: tenant-isolation tests; user lifecycle and MFA for privileged users; encryption and key ownership; managed device controls; object-download authorization; audit tamper detection; backup restoration; incident tabletop exercise; redacted logs; vulnerability review; and verified handling of support access.

Use short-lived credentials, workload roles and secrets management. Restrict production access to approved personnel and record privileged operations. Review permissions monthly during the pilot and on every role change. Define a private vulnerability channel before live deployment.

## Legal review deliverables before live data

L-01: entity incorporation and contracts. L-02: DPDP commencement/applicability matrix plus transitional IT/privacy duties. L-03: facility/state/specialty record retention. L-04: notice, consent, rights and guardian workflows. L-05: CERT-In and applicable breach reporting plan. L-06: hosting and subprocessors. L-07: ABDM terms and role claims. L-08: medical-device/clinical-software assessment if decision-support functionality is introduced. L-09: research ethics and secondary use. L-10: messaging, insurance or government-program obligations when those modules enter scope.

Each item needs a named reviewer, review date, source text and signed determination. All remain open in this planning baseline.
