# Product requirements baseline

Status: proposed, not implemented. Priority P0 is required for a live pilot, P1 is post-pilot, P2 is expansion.

## Roles and boundaries

Reception handles demographics and visit queues. Nurses capture permitted observations. Clinicians review and sign clinical records. Laboratory staff handle specimens and results within their authorization. Administrators manage facility membership and operational reports. Patients access their own records through a verified process. Platform support has no routine permission to read clinical data; time-limited support access requires approval and audit.

## Functional requirements

| ID | Priority | Requirement | Acceptance criterion |
|---|---|---|---|
| PR-01 | P0 | Facility and user enrollment | Disabled membership loses online access; users cannot grant themselves clinical privileges |
| PR-02 | P0 | Patient registration | Separate facility-local ID; unknown DOB supported with age estimate and date; phone/ABHA not mandatory for local care |
| PR-03 | P0 | Identity and duplicate review | Similar names or shared phones produce review candidates; no automatic cross-facility merge |
| PR-04 | P0 | Purpose and notice records | Store notice version, language, time, actor, purpose and applicable permission/basis reference |
| PR-05 | P0 | Consultation record | Author, encounter date, assessment, status and required missing-data reasons retained |
| PR-06 | P0 | Allergy and vital capture | Unknown/none-known/present remain distinct; value requires unit and observation time |
| PR-07 | P0 | Prescription lifecycle | Clinician signs; correction creates linked revision; old version remains auditable |
| PR-08 | P0 | Lab workflow | Order → specimen → result → reviewer acknowledgment; unmatched result is quarantined |
| PR-09 | P0 | Follow-up task | Due date, owner, status and attempt history; reminder delivery is not visit completion |
| PR-10 | P0 | Telugu and English | Representative users complete core workflow; clinician approves medical translation |
| PR-11 | P0 | Patient export | Identity checked; authorized records only; export logged and link expires |
| PR-12 | P0 | Facility dashboards | Reconcile encounter counts and denominator definitions to source records |
| PR-13 | P0 | Limited offline drafts | Retry creates no duplicate encounter; conflict visible; external exchange blocked offline |
| PR-14 | P0 | Audit | View, create, amend, permission change and export events recorded without full clinical payloads in logs |
| PR-15 | P1 | ABDM production exchange | Complete applicable sandbox and production onboarding evidence before advertising availability |
| PR-16 | P1 | Existing HIS/lab connectors | Agreed field mapping, replay and reconciliation; source-vendor permissions documented |
| PR-17 | P1 | Optional voice/OCR draft | Human verifies every clinical field before finalization; no automatic medication approval |
| PR-18 | P2 | Specialty modules | New clinical data definitions, workflow owner, safety validation and business case |

## Lifecycle and exception behavior

An encounter is draft, signed, amended or entered-in-error. “Entered-in-error” is a visible correction state, not silent deletion. Preserve author and timestamps. Do not silently overwrite a signed record during sync or import.

A prescription includes medication identifier/text, strength, dose, unit, route, frequency, duration and instructions appropriate to the clinician's order. Missing or ambiguous dose units block finalization. The product does not generate clinical treatment recommendations in the MVP.

A laboratory result includes source laboratory, order/accession reference, specimen information when available, observation time, report status and reviewer. A corrected report is linked to the superseded report; recipients see that it changed. A lab-specific critical-result workflow requires a named responsible person and acknowledgment; a generic notification alone is insufficient.

On consent withdrawal, record effective time and scope, stop subsequent sharing under that permission, cancel applicable queued exports and retain the audit trail. Route deletion requests through the approved retention/legal-hold process. Separate permission to send reminders from permission for external record sharing.

## Offline workflow

Pilot users may save bounded drafts while disconnected. Display last-sync time and pending count. Do not present an unsynchronized note as a confirmed server record. Final prescribing and lab result release require the approved online workflow in v0.1; paper downtime procedures cover clinical work during outages. Extending final clinical actions offline requires a separate safety assessment.

On reconnect, reauthenticate if needed, re-evaluate permission, upload drafts with unique operation IDs and compare record versions. A conflict goes to the responsible clinician; medication and diagnosis fields never use silent last-write-wins. If a device is revoked, reject its uploads into a controlled recovery queue rather than accepting them under a stale session.

## Non-functional targets

Proposed pilot online availability is 99.5% monthly, later 99.9% after measured operating evidence. Define exclusions and measurement points contractually. Target p95 common record reads below two seconds under an agreed representative workload; report internet and backend components separately. Recovery targets are documented in the operations plan. Accessibility includes readable text, keyboard navigation, clear validation and a workflow that does not require the patient to own a smartphone.

## Explicit non-goals

The first release is not a full inpatient HIS, an emergency-care decision engine, a pharmacy dispensing system, an insurance adjudicator, a population census or an authorized research registry. It does not automatically infer a patient's diagnosis from billing codes. It must integrate with the facility's established clinical responsibility and downtime process.
