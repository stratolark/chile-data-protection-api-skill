# Legal and product baseline

Use this reference for legal scoping and the minimum product capabilities. Verify the current official text before treating any legal detail as current.

Last verified: 2026-08-09.

## Contents

- Official sources and legal operating regime
- Interpretive boundary and source map
- Rights, notices, consent, and request handling
- Personal identifiers, RUT, incidents, processors, and transfers
- Impact-assessment flags

## Official sources

Primary sources:

- Law No. 21.719, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/navegar?idNorma=1209272
- Law No. 21.806, which modified Law No. 21.719, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/navegar?idNorma=1221118
- Current consolidated Law No. 19.628 through 2026-11-30, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/Navegar?dt=open&idLey=19628
- Consolidated Law No. 19.628 effective 2026-12-01, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/Navegar?idNorma=141599&idVersion=2026-12-01
- Diario Oficial: https://www.diariooficial.interior.gob.cl/
- Official publications of the Chilean Data Protection Agency when available

As last verified on 9 August 2026, the current consolidated text applies through 30 November 2026 and the principal reform is scheduled for 1 December 2026. Verify whether this remains correct at execution time.

## Select the legal operating regime

State one regime before making legal claims:

- `CURRENT_LAW_THROUGH_2026_11_30`: Use the current consolidated version. Do not present deferred rights, deadlines, Agency procedures, or sanctions as already effective.
- `TRANSITION_PREPARATION_FOR_2026_REFORM`: Design or implement future readiness, but label the amended rules as deferred and keep current obligations separate.
- `AMENDED_LAW_FROM_2026_12_01`: Use only when the relevant date is on or after the verified effective date and official sources confirm that the reform is in force.

If the relevant date is missing, use current law for current legal claims and treat reform work as transition preparation. Do not infer the regime only from the user's use of “Law No. 21.719.”

## Interpretive boundary

The law does not mandate REST endpoints. The endpoints in this skill are technical mechanisms for making rights and duties operational.

Do not decide the following from code alone:

- Controller, processor, or joint-controller status
- Processing purpose
- Lawful basis
- Whether a field is necessary
- Retention period
- Legal hold or exception
- International-transfer mechanism
- Whether a data-protection impact assessment is legally required
- Whether an automated decision is legally significant

Mark each unresolved item `LEGAL_INPUT_REQUIRED`.

Use these labels when the distinction is unclear:

- `LAW`: A claim tied to a verified official provision and operating regime
- `STANDARD_ENGINEERING_PRACTICE`: A repository-consistent correctness, security, testing, migration, or maintainability practice that is not attributed to an exact statutory design
- `RISK_BASED_CONTROL`: A technical or organizational measure selected to satisfy a risk-based duty in the actual system
- `STRICT_DEFAULT`: A conservative engineering control that is not prescribed in that exact form by law
- `ENGINEERING_RECOMMENDATION`: A general technical recommendation. Classify it as `RISK_BASED_CONTROL` or `STRICT_DEFAULT` before reporting or implementing it
- `LEGAL_INPUT_REQUIRED`: A decision that code or this skill cannot resolve

### Deferred amended-law source map

The article numbers below refer to the consolidated version scheduled for 1 December 2026:

| Capability | Provision |
| --- | --- |
| General data-subject rights | Article 4 |
| Access | Article 5 |
| Rectification | Article 6 |
| Erasure | Article 7 |
| Objection | Article 8 |
| Automated decisions and profiling | Article 8 bis |
| Blocking | Article 8 ter |
| Portability | Article 9 |
| Exercise channels and procedure | Articles 10 and 11 |

## Rights baseline

Current Law No. 19.628 already provides rights and duties concerning information or access, modification, cancellation, and blocking in Articles 6 and 12. Article 3 also permits opposition to use for advertising, market research, or opinion polling. Do not imply that all data-subject rights begin with Law No. 21.719.

| Capability | Current law through 2026-11-30 | Deferred amended law from 2026-12-01 |
| --- | --- | --- |
| Access or information | Article 12 | Articles 4 and 5 |
| Rectification or modification | Articles 6 and 12 | Articles 4 and 6 |
| Erasure or cancellation | Articles 6 and 12, subject to conditions and exceptions | Articles 4 and 7 |
| Objection | Article 3 for advertising, market research, and opinion polling. Article 12 also addresses voluntary or commercial-communication data | Articles 4 and 8 provide a broader right |
| Blocking | Articles 6 and 12 | Articles 4 and 8 ter |
| Portability | No general right identified in the current consolidated text | Articles 4 and 9 |
| Automated decisions | No equivalent general right identified in the current consolidated text | Article 8 bis |

Reverify the applicable provisions and exceptions for the specific processing activity.

Article 11 of the deferred amended text includes:

- A normal response period of 30 calendar days from receipt
- One extension of up to another 30 calendar days
- A response to a founded temporary-blocking request within two business days of receipt

Reverify these periods. Use `America/Santiago` and a configurable Chilean business-day calendar. Do not equate business days with Monday through Friday without a holiday source.

## Registration and privacy notice

Record this information during registration:

- Notice version presented
- Contract or terms acceptance separately
- Optional consent events separately by purpose
- Server-approved purpose and lawful-basis identifiers

The client must not choose the lawful basis.

A privacy-notice representation supports this information:

- Controller and representative where applicable
- Privacy contact channel
- Data categories and subject groups
- Purposes and approved lawful bases
- Sources
- Recipients and processors
- Retention information
- International transfers
- Rights and request channels
- Consent withdrawal
- Significant automated decisions and review rights when applicable
- Version and effective date

Publish only high-level security information. Do not expose topology, key identifiers, firewall rules, secrets, or exploit-relevant details.

## Consent

Model notice, contract, and consent separately.

Consent must be purpose-specific and evidenced. Use append-only events such as:

```text
CONSENT_GRANTED
CONSENT_WITHDRAWN
NOTICE_VERSION_CHANGED
CONSENT_RECONFIRMED
```

Do not:

- Use one mandatory checkbox for all processing
- Treat viewing a notice as consent
- Preselect optional consent
- Condition service on optional processing
- Make withdrawal harder than granting consent
- Over-collect IP, device, or identity data as supposed evidence

Withdrawal affects future processing and must propagate to dependent systems. It does not by itself erase earlier processing evidence.

## Access

Deferred amended-law source: Article 5.

Access is broader than `GET /me`. A response or export must be capable of including:

- Personal data being processed
- Source or origin
- Purposes
- Recipients or recipient categories as required
- Retention information
- Applicable legitimate interests when relevant
- Meaningful information about significant automated decisions when relevant

Use adapters to collect data from all in-scope stores. Redact another person's data in shared records according to an approved policy.

## Rectification

Deferred amended-law source: Article 6.

Rectification must address authoritative and derived data.

- Validate the requested correction where needed
- Update authoritative records
- Update or invalidate caches, indexes, projections, and exports
- Propagate corrections to recipients when required
- Record propagation failures and retries
- Do not retain obsolete personal data indefinitely merely for convenience

## Erasure

Deferred amended-law source: Article 7.

Erasure is not a single row deletion.

- Evaluate approved legal holds, statutory retention, contractual needs, claims, and exceptions
- Support partial fulfillment with a reasoned result
- Cover databases, replicas, caches, search, object storage, queues, analytics, exports, support tools, processors, and backups
- Use deletion tombstones or replayable erasure events so restored backups do not reactivate erased data
- Distinguish irreversible anonymization from reversible pseudonymization

Account closure and erasure must be separate concepts.

## Objection

Deferred amended-law source: Article 8.

Scope an objection to a processing activity or purpose.

- Stop future processing where the approved policy requires it
- Make direct-marketing opt-out especially simple
- Propagate the objection to jobs, analytics, campaigns, exports, and processors
- Do not require account authentication merely to stop marketing when a secure unsubscribe token is sufficient

## Blocking

Deferred amended-law source: Article 8 ter.

Blocking suspends prohibited processing while allowing permitted storage or legal-hold operations.

Represent blocks by:

```text
subject
purpose_or_scope
reason
effective_at
released_at
related_request
allowed_operations
```

Enforce blocks in:

- API reads and writes
- Workers and schedulers
- Event consumers
- Analytics and warehouses
- Search and indexing
- Exports
- Support and administrative tools

A single boolean on the user table is usually insufficient.

## Portability

Deferred amended-law source: Article 9.

Determine whether the approved legal conditions apply before exporting.

- Use structured, commonly used formats such as JSON, CSV, and ZIP with a manifest
- Include schema version, generation time, scope, and integrity metadata
- Deliver through a short-lived authenticated download
- For direct transfer, use verified allowlisted destinations, explicit authorization, delivery receipts, and SSRF protections
- Never accept an arbitrary destination URL and post personal data to it

## Automated decisions

Deferred amended-law source: Article 8 bis.

Add a review workflow only when applicable to significant automated decisions or profiling.

Support:

- Understandable explanation
- The person's statement and supporting information
- Human intervention
- Correction of inaccurate inputs
- Review outcome and communication
- Model, rule, or policy version needed for reconstruction

When not applicable, document the evidence for that conclusion. Do not add a decorative endpoint with no real human workflow.

## Personal identifiers and RUT

### Legal classification

- A natural person's RUT or RUN is personal data because it identifies or makes a natural person identifiable.
- A name, personal email, phone number, or address is personal data when it is linked or reasonably linkable to a natural person.
- A company RUT or generic company contact is not personal data solely because it identifies a legal entity. Reassess when the record identifies or concerns a natural person.
- RUT, name, email, phone, and address are not sensitive data merely by category under the current or deferred statutory definitions. Their context or combination can reveal sensitive information or create higher security impact.
- Public availability does not stop information from being personal data. Under current law, specific public-source exceptions can affect authorization and purpose rules. Do not generalize those exceptions. Under amended law, public availability is not a universal lawful basis.

### Current-law duties

Under the current regime, classify the following as `LAW` when applicable:

- Article 4: legal authorization, consent, and statutory exceptions
- Articles 6 and 9: deletion, blocking, accuracy, and purpose rules
- Article 7: secrecy for data from non-public sources and related database information
- Article 11: due diligence and responsibility for damage
- Article 12: information, modification, cancellation, and blocking rights

The current law does not universally prescribe UUIDs, field-level encryption, HMAC lookup columns, or a categorical list of prohibited infrastructure locations.

### Deferred amended-law duties

From the verified effective date, Article 3 adds explicit purpose, proportionality, security, and responsibility principles. Articles 14 quáter and 14 quinquies require privacy by design/default and risk-appropriate security. Encryption and pseudonymization are examples of possible measures, not mandatory universal implementations.

Use `references/engineering-postures.md` to select identifier, storage, lookup, telemetry, and migration controls. Treat Modulo 11 validation only as syntax validation. It does not prove that a RUT exists, belongs to the claimant, or authenticates a person.

## Incidents

Maintain an internal incident record with:

```text
discovered_at
affected_systems
data_categories
estimated_subject_count
cause
impact
containment
risk_assessment
authority_notification_decision
authority_notification_status
subject_notification_decision
subject_notification_status
sectoral_notifications
```

- Do not import the GDPR 72-hour deadline as Chilean law
- Reverify the current Chilean threshold and wording
- Put authority submission behind an adapter because forms, APIs, and authentication may change
- Preserve submission receipts and communication evidence
- Coordinate with Law No. 21.663 and sector-specific cybersecurity duties when applicable

## Processors and international transfers

Inventory hosting, storage, backups, email, SMS, CRM, analytics, support, observability, identity, payment, and other vendors.

For each, record:

```text
role
service
processing_purpose
data_categories
regions
subprocessors
contract_or_dpa_reference
international_transfer_mechanism
return_or_deletion_behavior
owner
```

Do not infer that data stays in Chile because the primary database is hosted there. Logs, backups, support access, notification services, and subprocessors may cross borders.

## Impact-assessment flags

Flag for legal review:

- Systematic and extensive evaluation
- Significant automated decisions
- Large-scale processing
- Systematic monitoring of public areas
- Sensitive or specially protected data
- Biometric identification
- Children's data
- High-risk dataset combinations
- Novel technology with material effects on people
