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
- Configuration loading, validation, ownership, and environment overrides
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
- Which admin roles can view or process each request

Describe unclear contractual allocation as a missing legal or business fact.

Infer the technical scope from repository evidence. Use `references/developer-decision-guide.md` only if the unresolved role affects the requested production behavior.

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

Apply the simplicity gate before recommending a new privacy service, adapter layer, queue, event model, dependency, or cryptographic subsystem. Identify the current requirement, existing repository pattern, operational cost, and the smallest complete alternative.

## Findings

For each confirmed gap, return:

```text
title
basis_when_material
file_or_symbol_evidence
current_behavior
risk
smallest_code_change
test
missing_law_bound_fact
priority
```

Keep findings in the response. Do not create a gap file unless the user asks.

Suggested priority scale:

- `P0`: active exposure, unauthorized access, cross-tenant leak, destructive defect, or raw personal data in high-volume telemetry
- `P1`: missing right, unenforced blocking, incomplete erasure, unprotected export, or deadline failure likely to affect users
- `P2`: incomplete propagation, weak auditability, brittle operations, or significant documentation gap
- `P3`: hardening, maintainability, or lower-risk completeness improvement

Do not inflate priority solely because an endpoint name differs from the illustrative blueprint. Do not assign legal impact to a missing stricter security control. Report its security benefit and implementation cost separately.

## Migration review

When existing records contain RUT or other personal data, select the migration controls from `references/engineering-postures.md`:

- Identify plaintext columns, indexes, foreign keys, cache keys, and downstream copies
- Under every posture, identify applicable legal duties, material risks, and existing stronger controls
- Under the strict security default, design surrogate identifiers and add encrypted values, keyed lookup when exact lookup is required, and key-version fields
- Under the legal baseline, select the least-complex adequate storage and lookup controls from the actual threat model. Do not claim that omitted strict controls are universally unnecessary
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
2. Packaged baseline date, applicable legal period, and security posture
3. Confirmed findings with exact evidence, separating legal gaps from stricter security recommendations
4. The smallest code change and tests for each finding
5. Any law-bound fact that disables a production action, with the cited rule and narrow effect

Lead with the recommended implementation path. Make technical decisions from repository evidence. Do not return blank legal forms or repeat the same blocker.

Do not modify files in audit-only mode.
