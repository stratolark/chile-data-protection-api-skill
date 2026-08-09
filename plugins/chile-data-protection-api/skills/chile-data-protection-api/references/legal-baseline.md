# Legal and product baseline

Use this reference for legal scoping and the minimum product capabilities. Verify the current official text before treating any legal detail as current.

Last verified: 2026-08-08.

## Contents

- Official sources and legal operating regime
- Interpretive boundary and source map
- Rights, notices, consent, and request handling
- RUT, incidents, processors, and transfers
- Impact-assessment flags

## Official sources

Primary sources:

- Law No. 21.719, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/navegar?idNorma=1209272
- Current consolidated Law No. 19.628 through 2026-11-30, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/Navegar?dt=open&idLey=19628
- Consolidated Law No. 19.628 effective 2026-12-01, Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/Navegar?idNorma=141599&idVersion=2026-12-01
- Diario Oficial: https://www.diariooficial.interior.gob.cl/
- Official publications of the Chilean Data Protection Agency when available

As last verified on 8 August 2026, the current consolidated text applies through 30 November 2026 and the principal reform is scheduled for 1 December 2026. Verify whether this remains correct at execution time.

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

Use these labels when the distinction could be unclear:

- `LAW`: A claim tied to a verified official provision and operating regime
- `ENGINEERING_RECOMMENDATION`: A technical control that helps implement or secure a capability but is not prescribed as that exact design by law
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

The deferred amended framework recognizes these rights. Before its verified effective date, treat this list as transition preparation rather than a statement of current law:

```text
ACCESS
RECTIFICATION
ERASURE
OBJECTION
PORTABILITY
BLOCKING
```

Article 11 of the deferred amended text includes:

- A normal response period of 30 calendar days from receipt
- One extension of up to another 30 calendar days
- A response to a founded temporary-blocking request within two business days of receipt

Reverify these periods. Use `America/Santiago` and a configurable Chilean business-day calendar. Do not equate business days with Monday through Friday without a holiday source.

## Registration and privacy notice

Registration should record:

- Notice version presented
- Contract or terms acceptance separately
- Optional consent events separately by purpose
- Server-approved purpose and lawful-basis identifiers

The client must not choose the lawful basis.

A privacy-notice representation should be capable of covering:

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

## RUT

Treat a natural person's RUT as personal data and an identity attribute.

The storage and lookup design below is an `ENGINEERING_RECOMMENDATION`, not a claim that the law prescribes these exact fields or cryptographic primitives.

### Ingress

- Normalize to one canonical representation on the server
- Validate the check digit with a tested Chilean Modulo 11 implementation
- Accept display formatting only at the boundary
- Use generic errors when detailed validation or duplicate responses create enumeration risk

### Storage and lookup

Prefer an equivalent of:

```text
data_subjects
  id: opaque UUID or equivalent
  rut_ciphertext: encrypted canonical RUT
  rut_lookup_hmac: deterministic keyed lookup value
  rut_key_version
  created_at
```

- Encrypt the recoverable RUT
- Use a keyed HMAC for exact lookup
- Do not use plain SHA-256 because the possible RUT space is enumerable
- Keep keys outside the database in an approved secret or key-management system
- Include rotation and backfill behavior
- Scope uniqueness by tenant or controller where needed

Never use raw RUT in URLs, JWTs, sessions, logs, traces, metrics, analytics, filenames, object names, queue names, cache keys, partition keys, or idempotency keys. Never use RUT alone as authentication.

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
