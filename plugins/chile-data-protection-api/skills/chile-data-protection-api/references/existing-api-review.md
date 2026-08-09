# Existing API review workflow

Use this reference before modifying an existing service and whenever the user requests an audit.

## Contents

- Repository and data-flow discovery
- Responsibility, tenancy, and existing capabilities
- Gap, migration, and public-contract review
- Runtime checks and audit output

## Repository discovery

Identify:

- Language, framework, runtime, package manager, and build system
- Service boundaries and deployment units
- Route or resolver registration
- Domain and application layers
- Persistence technologies and migration tooling
- Authentication, sessions, service accounts, and tenant isolation
- Validation, serialization, and error conventions
- Jobs, queues, schedulers, events, consumers, and dead letters
- Caches, search, object storage, analytics, warehouses, and exports
- External processors and recipients
- Logging, tracing, metrics, APM, and crash reporting
- Backup, restore, replication, import, and disaster-recovery behavior
- Existing contracts and tests

Reference exact files and symbols. Do not summarize from filenames alone when code inspection is possible.

## Data-flow inventory

For every personal-data field or category, trace:

```text
ingress
validation
normalization
business use
primary storage
secondary storage
cache
search
queue_or_event
analytics
external_recipient
export
telemetry
retention
deletion
backup_restore
```

Include derived identifiers and metadata when they can relate to a person.

## Responsibility and tenancy

Determine:

- Who decides purposes and means for each activity
- Whether the platform is controller or processor for each tenant
- Whether a request spans one tenant, several tenants, or the platform itself
- Whether subject identifiers are globally unique or tenant-scoped
- Which admin roles may view or process each request

Mark unclear contractual allocation `LEGAL_INPUT_REQUIRED`.

## Existing capability search

Before adding code, search for existing:

- User export or account archive
- Account deletion or deactivation
- Consent or communication preferences
- Privacy notices and terms versions
- Audit logs and append-only events
- Retention or cleanup jobs
- Legal holds
- Data classification or masking helpers
- Encryption and key management
- RUT validation and normalization
- Incident records and notification workflows
- Admin case-management screens or APIs
- Vendor deletion or webhook adapters

Reuse reliable capabilities rather than building duplicates.

## Gap matrix

For each gap, provide:

```text
id
requirement_or_capability
current_behavior
evidence
affected_data_and_users
risk
recommended_change
files_or_components
dependency
legal_input_needed
test_needed
priority
```

Suggested priority scale:

- `P0`: active exposure, unauthorized access, cross-tenant leak, destructive defect, or raw personal data in high-volume telemetry
- `P1`: missing right, unenforced blocking, incomplete erasure, unprotected export, or deadline failure likely to affect users
- `P2`: incomplete propagation, weak auditability, brittle operations, or significant documentation gap
- `P3`: hardening, maintainability, or lower-risk completeness improvement

Do not inflate priority solely because an endpoint name differs from the illustrative blueprint.

## Migration review

When existing records contain RUT or other personal data:

- Identify plaintext columns, indexes, foreign keys, cache keys, and downstream copies
- Design new opaque identifiers and relationship migration
- Add encrypted value and keyed lookup fields
- Version keys
- Backfill in bounded, resumable batches
- Avoid printing personal data in migration logs
- Use dual read or dual write where zero-downtime rollout requires it
- Rebuild indexes safely
- Update unique constraints at the correct tenant scope
- Remove legacy plaintext only after validation and rollback planning
- Test restore and rollback behavior

## Public contract review

Check:

- RUT in paths, queries, request identifiers, and response links
- RUT or personal data in JWTs and session claims
- Enumeration through status codes and validation messages
- IDOR in user, request, export, and admin routes
- Whether `DELETE /me` is incorrectly documented as legal erasure
- Whether privacy-request results can be fetched by another user or tenant
- Whether export links are long-lived or reusable
- Whether request creation is safely retryable

Preserve compatibility when possible. When a breaking change is needed, document migration and deprecation behavior.

## Runtime and operations review

Inspect:

- Worker authorization and tenant context
- Whether blocked or objecting subjects continue through campaigns or analytics
- Retry and dead-letter behavior for correction and erasure propagation
- Whether processor failures are visible
- Whether retention jobs are monitored
- Whether backup restoration replays erasure tombstones
- Whether operators can find overdue requests
- Whether incident decisions and notifications are recorded
- Whether admin actions have separation of duties where needed

## Audit-only output

Return:

1. Scope and detected architecture
2. Legal-verification status
3. Controller and processor assumptions
4. Processing inventory summary
5. Confirmed findings with evidence
6. Unknowns and `LEGAL_INPUT_REQUIRED` decisions
7. Prioritized remediation sequence
8. Proposed code areas and tests
9. Operational and migration risks

Do not modify files in audit-only mode.
