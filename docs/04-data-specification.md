# Data specification and quality controls

This is a logical design; final database migrations and exchange-profile conformance remain implementation tasks.

## Common conventions

Use generated immutable internal identifiers, UTC storage for event timestamps and Asia/Kolkata display for local users. Record occurrence time separately from entry/import time and preserve the source timezone when relevant. Distinguish unknown, not collected, not applicable and withheld. Clinical and administrative deletion semantics differ.

Every clinical record carries tenant, patient, encounter where applicable, source, author, status, creation time and revision. Every coded value preserves code system, code, display and terminology version; retain original text beside mappings. Store units explicitly. Never invent clinical values to improve completeness.

## Logical entities

| Entity | Key fields | Relationship / invariant |
|---|---|---|
| Facility | tenant_id, facility_id, name, address, external_registry_id | Registry ID optional until verified |
| User membership | user_id, tenant_id, role, active_from/to | Server-authorized role context |
| Patient | patient_id, tenant_id, local_mrn, name, birth_date/age_estimate | MRN unique within facility scope |
| Identifier | patient_id, issuer, value, verification_status | ABHA optional; restrict identifier access |
| Contact | patient_id, type, value, verified, relationship | Phone can be shared; not a unique key |
| Encounter | encounter_id, patient_id, facility_id, occurrence_time, type, status | Same-tenant references |
| Observation | observation_id, encounter_id, code, value, unit, observed_at, status | Value/unit and status validated |
| Condition | condition_id, encounter_id, code/text, certainty, onset | Suspected and confirmed distinguished |
| Allergy record | patient_id, substance, reaction, status, source | Unknown does not imply absent |
| Prescription | prescription_id, encounter_id, prescriber, signed_at, revision | Signed by permitted clinician |
| Medication item | prescription_id, medication, strength, dose/unit, route, frequency, duration | Ambiguous dosing prevents sign-off |
| Lab order | order_id, encounter_id, test, requester, status | Unique source order identifier |
| Specimen | specimen_id, order_id, accession, collection_time, status | Traceable sample identity |
| Lab result | result_id, order_id, source_lab, value/text, unit, range, status, revision | Corrected versions remain traceable |
| Review task | task_id, record_id, owner, due_at, status | Explicit acknowledgment required |
| Follow-up | task_id, encounter_id, due_date, owner, outcome | Reminder is separate from attendance |
| Document | document_id, owner_record_id, object_key, hash, mime_type, source | No public object URLs |
| Permission record | purpose, subject, recipient/scope, basis_ref, notice_version, effective/expiry/revoked_at | More than a yes/no flag |
| Audit event | actor, tenant, action, resource_ref, purpose, occurred_at, outcome | Restricted; no complete note text |
| Sync operation | device_id, tenant_id, operation_id, hash, base_version, outcome | Unique scoped operation |
| Provenance | source_system, source_id, imported_at, mapping_version, reviewer | Links transformations to original |

## Minimum encounter dataset

Required to open a visit: facility-local patient reference, facility, visit time and encounter type. A patient may be provisionally registered under the facility's identity policy; guessed identity data is prohibited. To sign a visit: responsible clinician, complaint/assessment, diagnosis text or justified absence, allergy review state, treatment/plan, and follow-up decision. Vitals are required only for the agreed clinical template or with a reason for absence.

Adult chronic-care extension: existing diagnosis with certainty, medication review, available relevant observations, laboratory test date/source, follow-up plan and attendance status. Clinical thresholds and treatment decisions are determined by the clinical lead using approved guidance, not embedded as unverified defaults in this planning document.

## Geography and population

Store facility location separately from patient residence. Use versioned official geographic reference data when acquired; district and mandal boundaries can change. Retain the original geographic code/version and map historical records intentionally. Do not infer residence from the hospital's district or treat a PIN code as an exact village.

Collect precise address only where needed for the care workflow. Shared analytics normally uses a coarser approved geography and age band. Avoid caste, religion, precise geolocation or other additional sensitive attributes unless a specific lawful clinical/program purpose has been approved.

## Quality rules

Reject impossible data types and missing units; flag clinically unusual measurements for review without silently changing them. Detect duplicates through source keys and review candidates. Separate patient-level duplication from repeated legitimate encounters. Measure lab order linkage, import rejection, source freshness and missing fields by facility.

A clinical steward approves mappings; an engineer cannot decide that two laboratory tests with similar names are medically equivalent. Preserve distinct methods, units and reference ranges. Imported PDFs remain documentary evidence, with any extraction marked unverified until reviewed.

## Analytical definitions

| Metric | Numerator | Denominator / limits |
|---|---|---|
| Encounter completeness | Eligible signed visits with all required fields or approved absence reasons | All eligible signed visits; report missingness separately |
| Capture coverage | Eligible visits represented in platform | Eligible visits in facility source register |
| Follow-up attendance | Due patients with a qualifying completed follow-up in agreed window | Patients due within the period; define loss to follow-up |
| Result linkage | Received results linked to correct order after review | All received results including exceptions |
| Facility retention | Opening paying facilities still paying at period end | Opening paying facilities; exclude new additions |
| Observed condition proportion | Distinct participating patients meeting approved condition definition | Distinct eligible patients seen; not state prevalence |

Use clinical occurrence date for care trends and receipt date for ingestion monitoring. All dashboards display refresh time, site coverage and denominator. Recompute affected aggregates after corrections, and retain definition/version history so previously published reports remain explainable.

## Data retention and exit

Create an approved schedule by class: clinical records, audit/security logs, temporary exports, offline cache, raw import files, research extracts and financial records. Required periods are unresolved pending legal/contract review. Preserve legal holds and document deletion propagation to processors and backup expiry. Export a facility's authorized data in a documented format, reconcile counts and hashes, then follow the termination agreement.
