# Engineering postures

Use this reference for every audit, design, or implementation. Select the legal operating regime first, then select an engineering posture independently.

## Contents

- Posture selection
- Control labels
- Simplicity and standard-practice gate
- Legal baseline posture
- Strict engineering posture
- Tailored posture
- Identifier and RUT controls
- Audit and implementation behavior

## Select one posture

- `LEGAL_BASELINE`: Implement verified legal requirements for the selected regime and the least-complex technical and organizational controls justified by the actual risks. This is not a low-security mode and does not certify compliance.
- `STRICT_ENGINEERING_DEFAULT`: Apply `LEGAL_BASELINE` plus conservative security and privacy defaults. This is the recommended posture for a new system that processes natural-person RUT or other high-impact identifiers.
- `TAILORED_CONTROL_SET`: Apply `LEGAL_BASELINE` plus an explicit, documented subset of strict controls selected from the threat model and operational constraints.

The posture does not decide the purpose, lawful basis, necessity, retention period, legal hold, controller role, or statutory exception. Mark unresolved decisions `LEGAL_INPUT_REQUIRED`.

Never remove or weaken an existing stronger control merely because `LEGAL_BASELINE` is selected. Treat removal as a separate security change requiring evidence and user authorization.

## Label every finding and control

- `LAW`: Source-backed legal requirement under the selected operating regime. Cite the official provision.
- `STANDARD_ENGINEERING_PRACTICE`: Repository-consistent validation, authorization, testing, migration, error handling, observability, or maintainability work needed for a correct production system, without claiming that the law prescribes its exact form.
- `RISK_BASED_CONTROL`: Technical or organizational measure selected to satisfy a risk-based legal or security duty. Record the risk and why the control is adequate.
- `STRICT_DEFAULT`: Conservative engineering control that is not prescribed in that exact form by law.
- `LEGAL_INPUT_REQUIRED`: Legal, contractual, or policy decision that cannot be resolved from code.
- `ASSUMPTION`: Reversible implementation assumption made to continue work.

Do not report a missing `STRICT_DEFAULT` as legal noncompliance. Do not treat `LEGAL_BASELINE` as permission to omit standard software practices or controls needed for authentication, authorization, tenant isolation, confidentiality, integrity, availability, or an identified material risk.

## Simplicity and standard-practice gate

Strict security means stronger justified controls, not more architecture.

Before recommending or adding a table, service, worker, queue, event stream, state machine, dependency, cryptographic layer, configuration flag, or abstraction:

1. Identify the current legal, product, security, or operational requirement it satisfies
2. Confirm that the problem exists in the inspected repository or is a committed deployment requirement
3. Search for an established repository mechanism that can satisfy it
4. Prefer a direct implementation at the existing boundary over a new subsystem
5. Name the failure prevented and verify that the benefit is proportionate to key management, migrations, monitoring, on-call, testing, and maintenance cost
6. Defer speculative extensibility, unused adapters, premature asynchronous processing, and framework changes

Preserve input validation, authorization, data integrity, transaction safety, required idempotency, error handling, rollback, compatibility, operational diagnostics, and behavior-focused tests. Do not call their removal “simplification.”

For each nontrivial recommendation, record:

```text
requirement_or_risk
existing_project_pattern
smallest_complete_control
complexity_and_operational_cost
why_simpler_is_insufficient
conditions_for_later_expansion
```

If no present requirement or proportionate safety benefit justifies a mechanism, do not recommend it.

## `LEGAL_BASELINE`

Implement only:

1. Applicable `LAW` requirements for the verified regime
2. `STANDARD_ENGINEERING_PRACTICE` controls consistent with the repository and deployment model
3. `RISK_BASED_CONTROL` measures supported by the system's data flows, threat model, sector, and operational context
4. Existing repository security requirements and stronger controls already in place

Prefer the smallest durable design. Document rejected strict controls and why they are unnecessary or disproportionate for the current risk. Require legal or privacy approval for legal conclusions and the security owner for material residual risk.

Examples:

- The law requires appropriate security or due diligence. It does not universally require application-level field encryption.
- A stable surrogate database key may be enough internally. A UUID is not legally required.
- Personal data can appear in approved operational records when necessary. Apply access controls, an approved retention period, and suitable protection. Do not copy it into telemetry without a defined purpose.

## `STRICT_ENGINEERING_DEFAULT`

Apply all applicable baseline controls and these defaults unless a control is technically irrelevant or conflicts with a verified legal obligation:

- Use a non-RUT surrogate subject identifier. Use opaque, non-meaningful identifiers in public contracts.
- Normalize and validate natural-person RUT on the server.
- Encrypt recoverable canonical RUT at the application or equivalent protection boundary.
- When exact RUT lookup is required, use a deterministic keyed lookup value such as HMAC. Do not use an unkeyed hash over the enumerable RUT space.
- Keep encryption and lookup keys outside the primary data store with versioning, rotation, and recovery procedures.
- Keep raw personal identifiers out of URLs, bearer tokens, client-visible sessions, logs, traces, metric labels, analytics events, filenames, object names, queue names, cache keys, partition keys, and idempotency keys.
- Use generic external responses and rate limits when validation, registration, or lookup behavior can enable enumeration.
- Use step-up authentication for high-risk exports or identity changes when the host application's risk warrants it.
- Encrypt personal-data export artifacts at rest and deliver them through short-lived authenticated retrieval.

Strict mode is not permission to add unused cryptography, duplicate identifiers, or speculative infrastructure. Skip an irrelevant control and record why it is not applicable.

Reuse the host platform's proven encryption, secret-management, authentication, authorization, validation, migration, job, telemetry, and testing capabilities before adding dependencies or parallel frameworks. Never invent cryptographic primitives. Do not create a privacy microservice, generic adapter framework, queue, outbox, or event-sourced model unless a present boundary or failure mode requires it.

## `TAILORED_CONTROL_SET`

Record:

```text
baseline_controls
selected_strict_controls
rejected_strict_controls
risk_and_tradeoff
approver_or_owner
review_date
```

Do not invent an approval. Mark it `LEGAL_INPUT_REQUIRED` or `ASSUMPTION` as appropriate until the responsible owner decides.

## Identifier and RUT controls

Treat classification and implementation separately.

| Concern | `LEGAL_BASELINE` | `STRICT_ENGINEERING_DEFAULT` |
| --- | --- | --- |
| Natural-person RUT/RUN | Treat as personal data and justify collection, use, disclosure, retention, and security | Baseline plus surrogate identity, field protection, and exclusion from public or telemetry identifiers |
| Company RUT | Do not classify it as personal data solely because it identifies a legal entity. Check whether the record also concerns a natural person | Do not use it as a security credential. Protect it according to business and sector risk |
| Name, email, phone, address | Treat as personal data when linked or reasonably linkable to a natural person | Keep raw values out of telemetry and infrastructure identifiers by default |
| Validation | Validate inputs needed for correctness and safe processing | Normalize and check natural-person RUT using a tested Modulo 11 implementation |
| Identity proof | Do not treat an identifier as authentication | A valid check digit proves syntax, not existence, ownership, or identity |
| Storage | Select access control, encryption, segregation, and retention measures from risk | Encrypt recoverable RUT and segregate keys from the primary store |
| Exact lookup | Use the least-exposing design for the use case | Use keyed deterministic lookup when lookup is required. Omit it when no lookup exists |
| Public identifiers | Enforce authorization regardless of identifier shape | Do not expose natural-person RUT. Prefer opaque non-enumerable identifiers |
| Telemetry | Define purpose, fields, access, retention, and redaction. Reject unjustified raw personal data | Assert that raw personal data is absent unless an explicit reviewed exception exists |

RUT, name, email, phone, and address are not sensitive data merely by category. Context or combination can reveal sensitive information or create high impact, so risk classification may be higher than the statutory category suggests.

## Audit behavior

If the user does not select a posture, produce a dual-track audit:

1. `LAW_GAP` and required risk controls
2. `STRICT_DEFAULT_GAP` recommendations with cost and benefit

Keep legal impact and strict-security impact in separate fields. Do not ask a blocking posture question when both tracks can be reported.

## Implementation behavior

If the user selects a posture, implement it. If no posture is selected, recommend `STRICT_ENGINEERING_DEFAULT` and ask only when interaction is practical. When work must continue without an answer, use `STRICT_ENGINEERING_DEFAULT` as an `ASSUMPTION` because it preserves the skill's safer historical behavior.

Before editing, record the selected posture and applicable controls. After editing, report each strict control that was applied, skipped, or deferred. In `LEGAL_BASELINE`, explain why an omitted strict control does not address the identified risk. Do not claim that it is legally unnecessary in every context.
