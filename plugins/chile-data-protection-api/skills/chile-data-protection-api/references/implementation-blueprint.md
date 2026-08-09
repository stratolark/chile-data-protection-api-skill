# Framework-agnostic implementation blueprint

Adapt these concepts to the host application. Do not create every table or service blindly.

## Contents

- API and domain building blocks
- Notices, consent, requests, deadlines, and identity
- Data adapters and rights orchestration
- RUT migration, retention, disclosures, and incidents
- Administration, documentation, and implementation order

## Illustrative API surface

```text
POST   /v1/users
GET    /v1/me
PATCH  /v1/me
POST   /v1/account-closure

GET    /v1/privacy/notice

POST   /v1/privacy/requests
GET    /v1/privacy/requests/{requestId}
GET    /v1/privacy/requests/{requestId}/result

GET    /v1/me/consents
PUT    /v1/me/consents/{purpose}
DELETE /v1/me/consents/{purpose}

POST   /v1/automated-decisions/{decisionId}/review   # conditional
```

GraphQL, RPC, or event-driven systems should implement equivalent operations and guarantees.

## Domain building blocks

Reuse existing models when possible. Common concepts include:

```text
data_subjects
processing_purposes
privacy_notice_versions
notice_presentation_events
consent_events
privacy_requests
privacy_request_events
privacy_request_artifacts
identity_verification_cases
processing_blocks
data_disclosures
retention_rules
legal_holds
deletion_jobs
automated_decisions
automated_decision_reviews
privacy_incidents
outbox_events
```

Add indexes for operational deadlines, subject lookup, request status, tenant scope, retry state, and retention execution. Avoid plaintext-personal-data indexes.

## Processing-purpose catalog

Keep a server-owned, versioned catalog capable of representing:

```text
purpose_id
description
approved_lawful_basis
data_fields_or_categories
required_or_optional
retention_rule_id
notice_version
controller_or_tenant_scope
downstream_processors
active_from
active_to
```

The API client may select an optional product preference. It must not choose the legal basis.

## Privacy notice

Store immutable versions. A registration or collection event should reference the version presented.

Do not mark a notice as “accepted” when it was merely displayed. Use separate events for terms acceptance and consent.

## Consent model

Use append-only events and a current-state projection.

```text
consent_event
  id
  subject_id
  tenant_or_controller_scope
  purpose_id
  action
  notice_version
  policy_version
  occurred_at
  source_channel
  actor_id
  evidence_reference_or_hash
  idempotency_key
```

Process withdrawal through a durable propagation job. Track per-destination outcomes.

## Privacy request model

A request should be able to record:

```text
request_id
subject_id_or_pending_identity
tenant_or_controller_scope
type
purpose_or_data_scope
reason_when_relevant
proposed_values_when_relevant
temporary_block_requested
reply_channel
representative_information
verification_status
received_at
response_due_at
blocking_decision_due_at
calculation_rule_version
extension_count
status
final_outcome
created_by
```

Avoid duplicating raw evidence. Store secure references when possible.

### Main status

```text
RECEIVED
IDENTITY_VERIFICATION_PENDING
IN_REVIEW
EXECUTION_PENDING
FULFILLED
PARTIALLY_FULFILLED
DENIED
CANCELLED
```

### Separate dimensions

```text
temporary_block_status: NONE | REQUESTED | APPLIED | DENIED | RELEASED
extension_count: 0 | 1
overdue: derived boolean
```

An extension should normally be an event and deadline update, not a status that hides the request's actual work state.

### Request event history

Store append-only events containing:

```text
event_id
request_id
event_type
actor_type
actor_id
occurred_at
reason_code
safe_metadata
correlation_id
```

Do not log the same personal-data payload into events and application logs.

## Deadline service

Create an interface such as:

```text
calculate_response_deadline(received_at, rule_version)
calculate_blocking_decision_deadline(received_at, calendar_version)
extend_response_deadline(request_id, reason, actor)
```

Requirements:

- Use `America/Santiago`
- Use a configurable Chilean holiday calendar
- Persist source timestamps and calculation versions
- Permit one extension only under the verified rule
- Generate overdue alerts without auto-closing the request
- Preserve evidence that an extension or final response was communicated

## Identity verification policy

Use a configurable policy engine or strategy interface.

Potential strategies:

- Authenticated session
- Step-up authentication
- Verified email or phone challenge already bound to the account
- Approved external identity provider
- Manual review of limited evidence
- Representative authorization review

Do not hard-code permanent document storage. Apply strict access, encryption, malware scanning where relevant, and short retention.

## Data inventory adapters

Define an adapter per domain or store:

```text
collect_for_access
rectify
apply_block
release_block
erase_or_anonymize
export_for_portability
report_recipients
```

Each operation should return structured outcomes:

```text
completed
skipped
legal_hold
retryable_failure
permanent_failure
not_applicable
evidence_reference
```

Register adapters explicitly so a new datastore cannot silently escape privacy workflows.

## Access export

- Collect from all registered adapters
- Redact third-party data in shared records according to approved policy
- Use a versioned manifest and schema
- Generate asynchronously when the result is nontrivial
- Encrypt the artifact at rest
- Deliver through short-lived authenticated retrieval
- Delete according to approved artifact retention

## Rectification orchestration

- Validate the proposed change
- Update the authoritative source
- Update projections, caches, indexes, and derived values
- Emit an outbox event
- Propagate to recipients and processors
- Retry failures
- Record final per-destination results

## Blocking enforcement

Create a centralized policy check that accepts:

```text
subject_id
purpose
operation
data_scope
tenant_or_controller_scope
```

Use it in:

- Synchronous business services
- Workers and schedulers
- Event consumers
- Analytics and indexing pipelines
- Exports
- Support tools

Fail closed for prohibited processing when block state is unavailable. Permit only approved operations such as storage or legal hold.

## Erasure orchestration

A deletion plan should contain per-adapter actions and outcomes.

- Evaluate legal holds before destructive work
- Support partial fulfillment
- Delete or irreversibly anonymize according to the approved map
- Invalidate caches and search documents
- Remove or detach files
- Request deletion from processors
- Track acknowledgements and failures
- Write a tombstone or durable erasure event
- Reapply tombstones during backup restoration and imports
- Prevent stale events from recreating deleted subjects

Use a dry-run mode for operational review where practical.

## Portability export and direct transfer

For downloadable portability:

- Use JSON, CSV, and ZIP as appropriate
- Include a manifest, schema version, scope, generation time, and integrity information
- Use safe filenames without RUT, email, or name
- Expire retrieval credentials and artifacts

For direct transfer:

- Verify the destination controller
- Use allowlisted connectors, not arbitrary URLs
- Require explicit authorization
- Protect against SSRF and DNS rebinding
- Encrypt transport
- Record delivery receipts
- Handle partial and retryable failures

## RUT storage migration

For existing plaintext RUT:

1. Add opaque subject identifiers if missing
2. Add encrypted RUT, keyed lookup, and key-version fields
3. Backfill in bounded, resumable batches
4. Add dual read or dual write when zero downtime requires it
5. Validate counts and lookup correctness without printing RUT
6. Update foreign references and API contracts
7. Remove plaintext indexes and columns only after rollout validation
8. Preserve rollback or recovery instructions

Key rotation should support multiple active lookup versions during migration when needed.

## Retention and legal holds

Represent retention by purpose and data category, not merely by account age.

A retention executor should:

- Select eligible records
- Check legal holds
- Produce a dry-run report
- Execute bounded jobs
- Record outcomes
- Retry failures
- Emit metrics without personal-data labels
- Alert on stalled or overdue cleanup

## Disclosure and recipient registry

Record enough to propagate corrections, objections, and erasure:

```text
subject_or_scope
recipient_or_processor
data_category
purpose
sent_at
transfer_mechanism
correlation_id
propagation_status
```

Store references and safe metadata rather than copies of full payloads.

## Incident reporting adapter

Define an interface such as:

```text
assess_incident(incident)
prepare_authority_report(incident)
submit_authority_report(incident)
notify_affected_subjects(incident, audience)
record_receipt(receipt)
```

Do not hard-code an Agency URL or payload until an official interface is verified. Keep sectoral notifications separate because their authorities and deadlines may differ.

## Administrative case management

Provide internal operations under strict authorization for:

- Request search and assignment
- Identity-verification decision
- Temporary-block decision
- Deadline extension
- Legal-hold review
- Final decision and reason
- Execution and retry
- Result publication
- Communication logging
- Incident assessment and notification

Use separation of duties where the organization's risk warrants it. Do not expose these operations as unauthenticated or ordinary user routes.

## Documentation artifacts

Create or update repository documents such as:

```text
docs/privacy/data-processing-inventory.md
docs/privacy/privacy-api-contract.md
docs/privacy/privacy-implementation-decisions.md
docs/privacy/privacy-operations-runbook.md
docs/privacy/privacy-gap-report.md
```

Adapt names to the repository. Do not put secrets or exploit-relevant internals into public documentation.

## Implementation order

1. Legal and scope record
2. Discovery and data-flow inventory
3. Opaque subject identity and RUT migration
4. Purpose, notice, and consent models
5. Rights-request case management and deadlines
6. Data inventory adapters
7. Access and rectification
8. Blocking and objection
9. Erasure, retention, holds, and backup behavior
10. Portability
11. Conditional automated decisions and incidents
12. Documentation, rollout, tests, and operations
