# Security and verification

Apply only the sections relevant to the changed behavior. Preserve existing stronger controls.

## Access control

- Map the authenticated principal to the repository's stable subject identity
- Use a non-RUT opaque public identifier under the strict security default
- Enforce object ownership, role, and tenant scope in the service that owns the action
- Test cross-user, cross-role, and cross-tenant denial
- Use step-up authentication when the current action has high disclosure or takeover impact
- Give service accounts access only to the stores and operations they need
- Support former users or representatives only when the requested flow requires them

Do not treat RUT, name, email, phone, or a valid check digit as authentication.

## Exports

- Protect stored artifacts according to their exposure and lifetime
- Under the strict security default, encrypt personal-data artifacts at rest
- Use short-lived authenticated retrieval
- Keep personal data out of filenames, object names, URLs, and access tokens
- Set safe cache and download headers
- Remove artifacts under the configured retention rule
- Record success and failure without logging contents

Generate asynchronously only when result size or downstream latency makes a request-bound response unsafe.

## Telemetry

Inspect logs, access logs, exceptions, traces, metrics, audit events, queue inspection, dead letters, APM, and analytics touched by the changed path.

Keep raw RUT, names, emails, phones, addresses, identity evidence, request content, and export data out of telemetry unless a specific operational need and proportionate protection justify the field.

Never use personal values as metric labels. Under the strict security default, capture actual test telemetry and assert that raw personal values are absent. Permit an exception only when the user provides a current operational need and the design bounds access and retention.

## Input and abuse resistance

Apply the controls relevant to the endpoint:

- Validate shape, size, type, and tenant scope at entry
- Rate-limit registration, recovery, verification, lookup, request, and export operations when abuse is credible
- Use generic responses when details enable enumeration
- Use idempotency for retry-prone writes
- Bound uploaded evidence by type, size, lifetime, and access
- Apply the application's malware checks to uploads when available
- Protect direct-transfer destinations against SSRF, DNS rebinding, redirects, and exfiltration
- Extract archives with path, size, and file-count limits

## Behavior tests

Test the changed slice, not the whole privacy domain.

Always include:

- Successful authorized behavior
- Unauthenticated and unauthorized denial
- Cross-tenant denial when the application is multi-tenant
- Invalid and boundary input
- Missing runtime configuration and its exact safe failure
- Retry or duplicate behavior when the boundary can repeat work
- Telemetry assertions for personal-data exposure

Add only the cases that match the feature:

- RUT normalization and valid or invalid check digits
- Notice version presentation
- Purpose-scoped consent grant and withdrawal
- Authenticated or recovery-path rights request
- Representative authority review
- Deadline calculations across month, timezone, and Chilean holiday boundaries
- Rectification through authoritative and derived stores
- Full and partial erasure
- Blocking or objection in synchronous and background paths
- Export generation, retrieval, expiry, and cleanup
- Processor failure, retry, and visible final outcome
- Retention eligibility, hold checks, dry run, and bounded deletion
- Backup restore or stale-event behavior after erasure

Do not build a capability merely to satisfy a checklist item.

## Contract and migration tests

When the change affects a public contract or stored data:

- Update the checked-in API or event contract
- Verify required backward compatibility
- Test migrations with representative existing data
- Test backfill resumability and idempotency when a backfill exists
- Verify rollback or recovery behavior
- Keep personal values out of migration logs
- Verify tenant-scoped uniqueness and lookup behavior when required
- Verify safe startup or feature failure when selected encryption or lookup keys are absent

## Operational checks

Check only the machinery introduced or changed by the slice:

- Failed propagation is visible and retryable
- Dead letters have an existing owner and recovery path
- Scheduled work is monitored
- Export cleanup runs and reports failure
- Backup restoration preserves erasure when relevant
- Selected key protection has a rotation and recovery path
- New operator actions have authorization and an existing or updated runbook

Do not create a runbook for code with no operator action or recovery procedure.

## Prohibited shortcuts

Do not:

- Add only account deletion and call legal erasure complete
- Add a controller without tracing the stores changed by its behavior
- Let a client choose a lawful basis
- Treat a displayed notice as consent
- Bundle optional consent into required terms
- Hard-code Monday through Friday as a Chilean business-day calendar
- Import the GDPR 72-hour incident deadline as Chilean law
- Email ordinary personal-data export attachments
- Send exports to arbitrary user URLs
- Keep identity evidence indefinitely by default
- Describe encryption alone as a privacy implementation
- Ignore current processors, caches, search, queues, analytics, logs, replicas, or backups
- Delete data while an applicable legal hold is unresolved
- Stop reversible implementation because a non-technical value is missing
- Publish placeholder controller details or draft notice text
- Enable new optional processing without its purpose and lawful basis
- Run destructive retention while a law-bound deletion precondition is missing
- Automatically refuse a request without an established legal ground

Under the strict security default, also do not:

- Use natural-person RUT as a primary key or public identifier
- Put raw natural-person RUT in routes, tokens, sessions, logs, metrics, traces, analytics, filenames, object names, queue names, cache keys, partition keys, or idempotency keys
- Use an unkeyed hash for exact RUT lookup
- Store recoverable RUT without the selected protection and key-management design

## Done

The changed slice is done when:

- Authorization, tenant scope, and input validation are enforced
- Every affected current store, job, vendor, telemetry path, export, and backup path has correct behavior
- Any missing law-bound value fails safely at the exact dependent action
- Runtime configuration is consumed, validated, and tested
- Migrations and backfills have a recovery path
- Changed contracts match the implementation
- Relevant tests pass, or the final response reports failures and unrun tests
- New operator actions and failure modes use an existing runbook or a focused update
- The final response states assumptions and any narrow legal production precondition
- The final response does not claim or guarantee compliance

For the legal baseline, confirm that the result uses established repository architecture and that omitted stricter controls are not reported as legal failures.

For the strict security default, confirm that each applicable identifier, storage, lookup, telemetry, export, and enumeration control is implemented and tested. Report skipped controls only when they affect the changed slice.

If the user selects individual strict controls, test those controls and state their current tradeoffs. Do not create a control log.

## Final report

Return:

1. Implemented behavior and exact files changed
2. Runtime configuration, migrations, and rollout impact
3. Tests run and exact results
4. Any remaining law-bound action, its cited rule, and the missing fact owner

Never state that tests passed when they were not run. Never hide a partial implementation behind a general completion claim.
