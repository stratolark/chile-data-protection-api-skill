# Engineering postures

Select security controls separately from the applicable legal period. A posture does not decide the processing purpose, lawful basis, retention period, legal hold, controller role, or statutory exception.

## Choose one posture

- **Legal baseline**: Implement the behavior required by the applicable Chilean regime with proportionate security based on the repository's actual risk
- **Strict security default**: Apply the legal baseline plus conservative controls for identifiers, storage, lookup, telemetry, exports, and enumeration

Honor the user's choice. For an audit without a choice, report legal gaps separately from optional strict controls. For implementation without a choice, recommend the strict security default as a reversible assumption.

Individual strict controls can be added to the legal baseline without creating another named posture.

## Explain why a control exists

Use these descriptions only when the distinction changes the decision:

- `Law`: required by a cited applicable provision
- `Required risk control`: needed to make the current design safe or reliable
- `Standard engineering practice`: established repository or platform practice
- `Strict security`: optional hardening beyond the legal minimum

Do not describe an omitted strict control as legal noncompliance.

## Simplicity gate

Add a mechanism only when at least one condition is present:

- Current behavior or a verified requirement needs it
- It protects authorization, integrity, confidentiality, availability, recovery, or compatibility
- It isolates a real external, persistence, security, ownership, or process boundary
- Multiple current consumers need the same invariant
- Repository evidence shows that a direct implementation would create material duplication or drift

Prefer an established repository pattern. Do not add a service, interface, queue, outbox, event history, approval workflow, policy object, or dependency for a hypothetical future need.

## Legal baseline controls

- Enforce authentication, authorization, ownership, and tenant scope at the service that owns the action
- Validate personal-data inputs needed for correctness and safe processing
- Apply security controls proportionate to the data, exposure, threat model, and platform
- Keep personal data out of telemetry unless a current operational need justifies the field and its protection
- Protect exports and temporary artifacts according to their exposure and lifetime
- Reuse current audit, configuration, migration, job, incident, and vendor mechanisms
- Preserve stronger controls already present in the repository

The legal baseline does not universally require UUIDs, field-level encryption, HMAC lookup columns, a privacy microservice, or a specific infrastructure location.

## Strict security controls

Apply only controls relevant to the data and changed behavior:

- Use opaque surrogate identifiers in public contracts instead of natural-person RUT
- Normalize and validate RUT on the server
- Protect recoverable canonical RUT with established encryption and separate key management
- Use a keyed lookup value such as HMAC only when exact RUT lookup is required
- Keep raw personal identifiers out of routes, tokens, logs, traces, metrics, analytics, filenames, object names, cache keys, and queue metadata
- Encrypt stored personal-data export artifacts
- Use short-lived authenticated export retrieval
- Add enumeration resistance where lookup or recovery endpoints expose whether a person exists
- Test actual telemetry output for personal-data leakage

Use proven platform or library primitives. Never invent encryption or hashing schemes.

## Identifier controls

| Concern | Legal baseline | Strict security default |
| --- | --- | --- |
| Natural-person RUT or RUN | Treat as personal data and justify collection, use, disclosure, retention, and protection | Add a surrogate identity and keep RUT out of public and telemetry identifiers |
| Company RUT | Do not classify it as personal data solely because it identifies a legal entity. Reassess when it concerns a natural person | Do not use it as a credential. Protect it according to business and sector risk |
| Validation | Validate inputs needed for correct processing | Normalize and check natural-person RUT using a tested Modulo 11 implementation |
| Authentication | Require proof appropriate to the requested action | Add step-up authentication for high-impact disclosure or changes |
| Lookup | Authorize the operation and prevent inappropriate enumeration | Use a keyed lookup value when exact search is required |
| Storage | Select access control, encryption, segregation, and retention from risk | Protect recoverable RUT and keep keys outside the primary store |
| Telemetry | Define purpose, access, retention, and redaction for any personal field | Assert through tests that raw personal values are absent |

RUT, name, email, phone, and address are not sensitive data merely by category. Their context or combination can still create high impact and justify stronger controls.
