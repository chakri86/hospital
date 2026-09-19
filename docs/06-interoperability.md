# Interoperability and migration plan

## Standards baseline

The [official NRCeS implementation guide](https://nrces.in/ndhm/fhir/r4/index.html), accessed 19 September 2026, identifies FHIR R4 and document profiles including outpatient consultation, prescription and diagnostic reports. It distinguishes a health information provider from a health information user. The published page displayed version 6.5.0; confirm the required version with the integration environment before implementation.

The following mappings are proposed design targets, not a claim of conformance:

| Internal concept | Candidate FHIR resource/profile family |
|---|---|
| Patient and identifiers | Patient |
| Facility and clinician | Organization, Practitioner, PractitionerRole |
| Visit | Encounter and outpatient consultation document |
| Measurements/results | Observation, DiagnosticReport and diagnostic document |
| Diagnosis and allergy | Condition, AllergyIntolerance |
| Prescription | MedicationRequest and prescription document |
| Documents | DocumentReference, Composition, document Bundle as required |

FHIR exchange structures do not need to be the physical database schema. Preserve original data, coding-system identifiers and mapping versions. A generic FHIR JSON validator alone does not prove ABDM end-to-end conformance.

## Implementation steps

1. Confirm current onboarding process, use case, credentials, environment and applicable contracts with the official sandbox.
2. Determine whether the product is supplying records, requesting them, or both. Scope each role separately.
3. Implement patient linking and verification with the approved flow and no assumption that a shared phone uniquely identifies a person.
4. Implement the applicable authorization/consent callbacks, exchange state machine and timeouts.
5. Map signed clinical documents into the required profiles and validate terminology and references.
6. Test request replay, expiry, revocation, partial failure, duplicate callbacks and source correction.
7. Complete required security/conformance evidence and production onboarding.
8. Document successful production acceptance before advertising the integration as available.

The sandbox entry point is [sandbox.abdm.gov.in](https://sandbox.abdm.gov.in/), linked by the inspected implementation guide. Its detailed current onboarding requirements were not retrieved for this report and must be verified during implementation.

## Proposed internal API contracts

These endpoint names are design proposals, not existing routes.

| Endpoint | Behavior | Important constraint |
|---|---|---|
| POST /v1/patients | Register local patient | Server-derived tenant; scoped idempotency |
| POST /v1/encounters | Create draft | Patient membership verified |
| POST /v1/encounters/{id}/sign | Clinician finalization | Role and version required |
| POST /v1/prescriptions/{id}/amend | Correct signed prescription | New revision, reason and clinical approval |
| POST /v1/lab-results/import | Receive result | Validate source/order; quarantine unmatched |
| POST /v1/sync/batches | Submit offline drafts | Per-operation status; no silent clinical conflict merge |
| POST /v1/exports | Request authorized record export | Purpose and recipient scope verified |
| POST /v1/permissions/{id}/withdraw | Record withdrawal | Recheck queued sharing jobs |

Use pagination, rate limiting, safe error messages, request IDs and versioned contracts. Do not put patient identifiers in URL query parameters or operational logs. Separate external connector service accounts from ordinary user accounts.

## Existing systems and lab integration

Prefer supported vendor APIs or authorized structured exports. Obtain permission, sample schemas with synthetic records, rate limits and interface costs. Define source-of-truth rules per field. If the source system corrects a report, reconcile the correction rather than creating a second apparent test.

Lab analyzers and legacy systems may require vendor-specific adapters. Do not write back to a clinical source database without a reviewed vendor-supported mechanism. A connector must expose import counts, rejections, pending matches, duplicates and last-success time.

## Migration runbook

Agree scope and lawful authority → inventory source → map fields → dry-run synthetic fixtures → authorized restricted staging import → clinical sample review → count/hash reconciliation → facility sign-off → controlled cutover → monitored delta handling → closeout and approved staging deletion.

Prioritize active-patient records and the subset needed for continuity. OCR is a separate assisted workflow. Historical diagnosis or medication data without evidence remains uncertain. Keep original source reference and import date. Choose whether each field is authoritative, historical or unverified.

Before cutover, define rollback trigger, source write freeze if needed, delta capture and responsibility for changes during the transition. Reverting the application must not delete clinical entries created after cutover; export and reconcile those entries first. Facility staff approve clinical reconciliation.

## Conformance evidence

Track profile version, validator version, fixture set, terminology release, callback scenarios, security assessment and environment acceptance. Record vendor API versions and expiry of credentials/contracts. No claims of certification, automatic universal exchange, or access to all state records are made by this repository.
