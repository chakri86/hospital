# Operations, clinical safety and validation

All service levels are proposed targets pending measurement and contract approval.

## Recovery and availability

| Scenario | Pilot target | Method and limitation |
|---|---|---|
| Common online workflows | 99.5% monthly availability | External monitoring with agreed measurement scope |
| Recover committed server data | RPO ≤15 minutes, RTO ≤4 hours | Tested backup/PITR and restore procedure |
| Cloud-region disaster | RPO ≤24 hours, RTO ≤24 hours initially | Approved independent India-region backup copy and recovery exercise |
| Offline drafts | No guarantee before server acknowledgment | Managed-device cache, visible pending count and reconciliation |
| Later commercial maturity | Evaluate 99.9% and tighter recovery | Adopt only after costed, demonstrated capability |

RPO means acceptable potential data loss; RTO means target restoration time. Multi-zone availability does not by itself provide regional disaster recovery. Backups require separate access control and successful restore evidence. Review these targets with clinical operations before live use; a facility requiring continuous emergency/inpatient dependence is outside the pilot scope.

## Operating routines

Daily: review failed imports, unmatched lab results, overdue clinical review tasks, backup success, queue lag and device sync exceptions. Weekly: reconcile facility encounter coverage, inspect data quality, review security alerts and unresolved tickets. Monthly: restore a sample dataset, review access and costs, examine churn and release defects. Quarterly or before major change: rehearse regional recovery and incident coordination.

Monitor uptime, latency, error rate, database capacity, queue age, object access failures, oldest unsynchronized draft, pending clinical acknowledgments and support load. Do not place patient names or diagnosis text in observability labels.

## Incident process

Appoint an incident commander and maintain a current escalation roster. Record discovery time, preserve relevant evidence, contain access, assess clinical impact, involve the facility and legal/security leads, and apply the current notification obligations. Avoid destructive cleanup before evidence is preserved. Restore service through a verified procedure and reconcile any paper or offline records. Complete a post-incident review with corrective actions and owners.

The legal-review register defines reporting deadlines and recipients. Technical staff must escalate immediately; they must not wait to establish every fact before initiating the incident workflow.

## Validation matrix

| Test ID | Requirement/risk | Meaningful test | Evidence required |
|---|---|---|---|
| T-01 | PR-01, tenant isolation | User from facility A requests B's patient, export and object URL; worker replay too | Every unauthorized path denied and audited |
| T-02 | PR-02/03, identity | Two people share name and phone; import repeats a source ID | Separate patients preserved; duplicate source handled correctly |
| T-03 | PR-07, clinical amendment | Signed prescription corrected during concurrent edit | Original retained, new revision approved, stale version rejected |
| T-04 | PR-08, lab safety | Wrong accession, unmatched patient, corrected result and duplicate import | Quarantine/review and correct traceability |
| T-05 | PR-04/11, withdrawal | Withdraw permission while export waits in queue | Export blocked or reevaluated under valid authority |
| T-06 | PR-13, offline | Network loss, repeat retry, expired lease, revoked device and version conflict | No duplicate, no silent merge, clear recovery state |
| T-07 | Recovery | Restore committed synthetic data to isolated environment | Counts, hashes, key access and measured RPO/RTO |
| T-08 | Analytics | Repeat patients, missing fields and changing site coverage | Correct denominators, missingness and labels |
| T-09 | Localization | Telugu and English workflow with representative staff | No critical translation/usability errors |
| T-10 | Security | Auth bypass, injection, insecure download, logs and secrets | Independent review; critical issues resolved |
| T-11 | Portability | Full authorized facility export and re-import rehearsal | Reconciled records and no other-tenant data |
| T-12 | Clinical review | Missing units, unknown allergy, wrong-patient selection | Blocks/warnings approved by clinical lead |

These tests are specifications for future application work; running the repository's documentation validator does not execute them.

## Release gate

Require complete P0 workflows, no unresolved critical security/clinical-safety defects, documented high-risk exceptions approved by the responsible authority, signed agreements, trained facility users, contact/escalation roster, restore evidence and clinical acceptance. Begin with restricted enrollment and daily review. Define rollback triggers and a procedure to preserve/reconcile records written after release.

## Clinical hazard log

Track hazard, cause, affected patient/workflow, severity, likelihood, preventive control, test and reviewer. Initial hazards: wrong-person linkage; medication dose ambiguity; stale offline history; lost lab results; unreviewed corrected results; misleading allergy status; unauthorized chart access; and erroneous population statistics. The clinical lead signs the residual-risk assessment, not the engineering team alone.

## Customer support and exit

Pilot support covers contracted outpatient operating hours, with a technical/security escalation contact. Do not imply round-the-clock clinical support. Use synthetic reproductions or approved restricted access, never screenshots sent to public chat groups. At termination, verify requester authority, export and reconcile authorized records, revoke integrations and follow the agreed retention/deletion schedule.
