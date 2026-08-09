# Security and verification

Apply only the controls and tests relevant to the audited or changed behavior. Preserve stronger controls already present in the repository. Follow the audit execution rules and output contract in `SKILL.md`.

## Access control

- Map the authenticated principal to the repository's stable subject identity
- Enforce object ownership, role, and tenant scope in the service that owns the action
- Test unauthenticated, cross-user, cross-role, and cross-tenant denial where applicable
- Use step-up authentication for actions with high disclosure or takeover impact when the threat model warrants it
- Give service accounts only the stores and operations they need

Never treat RUT, name, email, phone, or a valid check digit as authentication.

## Exports

- Protect stored artifacts according to exposure and lifetime
- Use short-lived authenticated retrieval
- Keep personal data out of filenames, object names, URLs, and access tokens
- Set safe cache and download headers
- Remove artifacts under the configured retention rule
- Record success and failure without logging content

Under the strict security default, encrypt stored personal-data artifacts. Generate asynchronously only when size or downstream latency requires it.

## Telemetry

Inspect logs, access logs, exceptions, traces, metrics, audit events, queue inspection, dead letters, APM, and analytics touched by the behavior.

Keep raw RUT, names, emails, phones, addresses, identity evidence, request content, and export data out of telemetry unless a current operational need and proportionate protection justify them. Never use personal values as metric labels.

Under the strict security default, capture representative test telemetry and assert that raw personal values are absent.

## Input and abuse resistance

- Validate shape, size, type, and tenant scope at entry
- Rate-limit registration, recovery, verification, lookup, request, and export operations when abuse is credible
- Use generic responses when details enable enumeration
- Use idempotency for retry-prone writes
- Bound uploaded evidence by type, size, lifetime, and access
- Apply current malware checks to uploads
- Protect direct transfers from SSRF, DNS rebinding, redirects, and exfiltration
- Extract archives with path, size, and file-count limits

## Behavior tests

Test the changed slice rather than the whole privacy domain. Cover the applicable cases:

- Successful authorized behavior
- Unauthenticated and unauthorized denial
- Cross-tenant denial
- Invalid and boundary input
- Missing runtime configuration and its exact safe failure
- Retry or duplicate behavior across a repeatable boundary
- Absence of personal data in telemetry
- RUT normalization and check-digit validation
- Notice-version presentation
- Purpose-scoped consent grant and withdrawal
- Rights-request authentication or recovery path
- Representative authority review
- Deadlines across timezone and Chilean holiday boundaries
- Rectification through authoritative and derived stores
- Full and partial erasure
- Blocking or objection in synchronous and background paths
- Export generation, retrieval, expiry, and cleanup
- Processor failure, retry, and final outcome
- Retention eligibility, holds, dry run, and bounded deletion
- Backup restoration or stale-event behavior after erasure

Do not build a capability merely to satisfy a checklist item.

## Contract and migration tests

When a public contract or stored data changes:

- Update the checked-in API or event contract
- Verify required backward compatibility
- Test migrations with representative existing data
- Test backfill resumability and idempotency
- Verify rollback or recovery behavior
- Keep personal values out of migration logs
- Verify tenant-scoped uniqueness and lookup behavior
- Verify safe startup or feature failure when selected encryption or lookup keys are absent

## Operational checks

Check only machinery introduced or affected by the slice:

- Failed propagation is visible and retryable
- Scheduled and cleanup work is monitored
- Dead letters have an owner and recovery path
- Backup restoration preserves erasure when relevant
- Selected key protection has rotation and recovery behavior
- New operator actions have authorization and an existing or focused runbook

## Security shortcuts to reject

- Account deletion presented as complete legal erasure
- A controller added without tracing affected stores
- Client-selected lawful basis
- Displayed notice treated as consent
- Monday-through-Friday logic used as a Chilean business-day calendar
- Personal-data export sent as an ordinary email attachment or to an arbitrary URL
- Identity evidence retained indefinitely without need
- Current processors, caches, search, queues, analytics, logs, replicas, or backups ignored
- Destructive deletion performed despite an applicable unresolved hold
- Placeholder controller details or draft notice published
- Automated refusal without an established ground

Under the strict security default, also reject:

- Natural-person RUT as a primary key or public identifier
- Raw RUT in routes, tokens, sessions, telemetry, filenames, object names, queue names, cache keys, partition keys, or idempotency keys
- Unkeyed hashing for exact RUT lookup
- Recoverable RUT stored without the selected protection and key-management design

## Completion check

The changed slice is complete when authorization, tenant scope, validation, affected data paths, safe configuration failure, migrations, contracts, tests, and operational recovery are covered. Any remaining missing legal fact must affect only the exact production action identified by the legal-blocker test.
