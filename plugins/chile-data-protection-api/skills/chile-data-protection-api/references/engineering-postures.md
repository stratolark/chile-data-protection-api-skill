# Engineering postures

Use this reference for every audit, design, or implementation. Select the applicable legal period first, then select a security posture independently.

## Contents

- Posture selection
- Recommendation basis
- Simplicity and standard-practice gate
- Legal baseline posture
- Strict engineering posture
- Tailored posture
- Identifier and RUT controls
- Audit and implementation behavior

## Select one posture

- **Legal baseline**: Implement verified legal requirements for the selected period and the least-complex technical and organizational controls justified by actual risk. This is not a low-security mode and does not certify compliance.
- **Strict security default**: Apply the legal baseline plus conservative security and privacy defaults. Recommend this posture for a new system that processes natural-person RUT or other high-impact identifiers.
- **Tailored controls**: Apply the legal baseline plus a selected subset of stricter controls supported by the threat model and operational constraints.

The posture does not decide the purpose, lawful basis, necessity, retention period, legal hold, controller role, or statutory exception. Describe an unresolved item by its domain name, such as `retention period`, instead of assigning an internal code.

Do not stop implementation for every unresolved fact. Use `references/developer-decision-guide.md` to select a reversible path and apply the legal-blocker test.

Never remove or weaken an existing stronger control merely because the legal baseline is selected. Treat removal as a separate security change requiring evidence and user authorization.

## Explain the basis only when it matters

Use plain language to distinguish:

- A legal requirement tied to a cited provision and applicable period
- Standard engineering practice needed for a correct production system
- A risk-based control selected for an identified threat or legal duty
- A stricter security choice that the law does not prescribe in that exact form
- A missing legal or business fact that code cannot establish
- A reversible implementation assumption

Do not add a classification tag to every finding. State the basis where the distinction changes priority, scope, or the user's understanding.

Do not report a missing stricter control as legal noncompliance. The legal baseline never permits omission of authentication, authorization, tenant isolation, confidentiality, integrity, availability, or controls needed for an identified material risk.

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

For a nontrivial recommendation, name the current requirement or risk, the repository pattern reused, the smallest complete control, and its operational cost. Add expansion criteria only when a known near-term change requires them.

If no present requirement or proportionate safety benefit justifies a mechanism, do not recommend it.

## Legal baseline

Implement only:

1. Applicable legal requirements for the verified period
2. Standard engineering controls consistent with the repository and deployment model
3. Risk-based measures supported by the system's data flows, threat model, sector, and operational context
4. Existing repository security requirements and stronger controls already in place

Prefer the smallest durable design. Explain a rejected strict control only when it affects the current request. Legal or privacy owners supply legal conclusions. The security owner accepts material residual risk under the organization's normal process.

Examples:

- The law requires appropriate security or due diligence. It does not universally require application-level field encryption.
- A stable surrogate database key can be sufficient internally. A UUID is not legally required.
- Personal data can appear in necessary operational records. Apply access controls, the applicable retention rule, and suitable protection. Do not copy it into telemetry without a defined purpose.

## Strict security default

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

## Tailored controls

Implement the legal baseline plus the stricter controls selected by the user or supported by the current threat model. State the selected controls and their current tradeoff. Mention an omitted strict control only when it materially affects the requested slice.

## Identifier and RUT controls

Treat classification and implementation separately.

| Concern | Legal baseline | Strict security default |
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

RUT, name, email, phone, and address are not sensitive data merely by category. Context or combination can reveal sensitive information or create high impact. As a result, the risk classification can be higher than the statutory category suggests.

## Audit behavior

If the user does not select a posture, produce a dual-track audit:

1. Legal gaps and required risk controls
2. Stricter security recommendations with cost and benefit

Keep legal impact and strict-security impact in separate fields. Do not ask a blocking posture question when both tracks can be reported.

## Implementation behavior

If the user selects a posture, implement it. If no posture is selected, recommend the strict security default as a reversible implementation assumption.

Do not pause only to ask which posture to use. Ask only when the choice creates a material cost, migration, compatibility, or operational tradeoff.

When a choice is necessary, provide at most three options. Recommend one option from repository evidence and state the cost of each option.

Before editing, select the posture and applicable controls in working analysis. After editing, report strict controls only when they changed the requested slice. Under the legal baseline, explain a material omitted strict control through the identified risk. Do not claim that it is legally unnecessary in every context.

Add runtime configuration only for values that code consumes. Use the repository's existing configuration mechanism.

Do not create a generic privacy configuration object, approval workflow, or decision log. Keep missing values absent and fail safely at the dependent action.

When a legal or business fact is missing, implement draft states and safe failure behavior. Disable a production action only when the legal-blocker test passes.
