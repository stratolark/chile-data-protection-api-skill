# Repository-first implementation patterns

Load only the section needed for the requested capability. Adapt every pattern to the host application. Do not copy example routes, fields, states, or service names without repository evidence.

## Purpose and optional processing

For one fixed purpose, use the existing domain model or a validated server-owned constant. Add a runtime catalog only when multiple current purposes vary at runtime.

The server owns the lawful-basis mapping. A client may choose an optional preference, but it must not choose its lawful basis. Add purpose or lawful-basis fields only when runtime behavior or historical reconstruction reads them.

Keep new optional processing off while its purpose or lawful basis is unknown.

## Privacy notices

Use immutable notice versions when the system must prove which content was shown. Associate the collection or registration event with that version.

Keep notice presentation, terms acceptance, and optional consent as separate facts. Keep draft content unpublished.

## Consent

Record grant and withdrawal durably by purpose. Reuse the current audit or history mechanism. Add a current-state projection only when a read path needs it.

Propagate withdrawal to each current downstream consumer. When propagation crosses a fallible boundary after the local transaction, use the repository's retry, idempotency, and visible-failure mechanism.

## Rights requests

Reuse an existing case or workflow model when it can preserve:

- Subject, requester, tenant, and representative authority
- Requested right, data, or processing scope
- Identity-verification state
- Receipt time, due time, and any permitted extension
- Pending, completed, partial, refused, and cancelled outcomes needed by the flow
- Result and reason communicated to the requester

Keep deadline, temporary block, and execution outcome separate when combining them would allow invalid states. Reuse the existing audit trail unless current transitions require evidence it cannot preserve.

## Deadlines

Use a direct date function when one component owns the calculation. Introduce a shared service only when several current consumers use the same changing calendar rules.

- Use `America/Santiago`
- Use a maintained Chilean holiday source for business-day rules
- Preserve timestamps and the applied calculation rule when deadlines must be explained
- Alert on overdue work without silently closing it

Do not model business days as Monday through Friday alone.

## Identity verification

Choose the least intrusive method that gives enough confidence for the action. Prefer, when appropriate:

1. Current authenticated session
2. Existing step-up authentication
3. Existing verified recovery channel
4. Existing external identity provider
5. Manual review of limited evidence

Verify representative authority separately. Do not retain identity documents by default. If evidence must be uploaded, apply current access control, protected storage, malware checks, and short-lived cleanup.

## Connecting data stores

Use each domain's existing service or repository boundary. Introduce a shared contract only when several current stores need the same operation or it isolates a current processor boundary.

Each store operation must distinguish success, an applicable exclusion, a retryable failure, and a permanent failure using existing result types where possible. Register handlers explicitly when silent omission could produce an incomplete result.

## Access and portability exports

- Collect only the data required by the applicable request
- Redact another person's data under the applicable rule
- Use a stable documented structure when consumers rely on it
- Generate asynchronously only when size or downstream latency requires it
- Use short-lived authenticated retrieval and safe filenames
- Remove artifacts under the configured retention rule

For direct transfer, use verified destinations or current allowlisted connectors. Protect them from SSRF, redirects, DNS rebinding, and partial delivery. Never post personal data to an arbitrary user-provided URL.

## Rectification

Validate the proposed value, update the authoritative source, and update or invalidate current caches, indexes, projections, exports, and derived values. Make recipient-propagation failures visible and retryable.

Use an existing domain event when it already carries the change. Add an outbox only when atomic database-to-message delivery is a current correctness requirement.

## Blocking and objection

Enforce the restriction at every current path that performs the affected processing, including APIs, jobs, consumers, exports, analytics, and support tools.

Keep scope explicit by subject, purpose or activity, operation, category, and tenant when those dimensions exist. Centralize the decision only when multiple consumers need the same invariant.

Fail safely when a required block state is unavailable. Permit only processing allowed by the applicable rule, such as storage required by a verified hold.

## Erasure

- Check retention, holds, claims, and exceptions before destructive work
- Support partial fulfillment when some data cannot be erased
- Delete or irreversibly anonymize each in-scope copy
- Invalidate caches, search, files, and derived views
- Propagate to current processors and expose failures
- Prevent backup restoration, imports, or stale events from recreating erased data

Reuse an existing deletion marker, audit mechanism, or replay protection. Add a tombstone only when restoration or asynchronous replay can recreate the data and no current mechanism prevents it. Use dry runs and bounded batches when scope or recovery risk warrants them.

## RUT storage and migration

Treat natural-person RUT as personal data, not authentication.

1. Find every current copy, index, relationship, contract, export, and telemetry path
2. Confirm whether exact lookup is required
3. Preserve existing stronger protection
4. Select controls from `engineering-postures.md`
5. Use dual read or write only when deployment compatibility requires it
6. Backfill without printing personal values and verify counts and lookup behavior
7. Remove legacy plaintext only after rollout validation and recovery planning

Use established encryption and keyed-hashing libraries. Keep keys outside the primary data store. Add key versions only when the chosen protection needs rotation.

## Retention and legal holds

Model retention by current purpose and data category when their rules differ. Use an existing configured value unless the repository marks it as a draft or placeholder.

If no value exists, select a configurable provisional default from the purpose and lifecycle. Use these defaults for short-lived technical artifacts when no repository rule applies:

- Password-reset secrets: scrub when delivery is terminal or the token expires
- Personal-data export artifacts: 24 hours
- Identity evidence: 30 days after the request closes
- Terminal notification payloads: scrub immediately and retain minimal delivery evidence
- Operational telemetry: 30 days unless a current need justifies more

Do not use one numeric default for core business records. Begin with eligibility and dry-run output when deletion scope, recovery, or hold coverage is uncertain.

A production executor needs bounded selection, hold checks, idempotent deletion or anonymization, outcome recording, retry behavior, safe metrics, and monitoring. Reuse the current job framework.

## Disclosures and processors

Reuse current vendor, webhook, or delivery records. Store only metadata needed to identify a recipient, prove or retry a disclosure, and propagate later correction, objection, blocking, or erasure.

## Incidents

Reuse the security incident workflow. Add personal-data impact fields only when the current incident process needs them.

Create an authority-submission boundary only when a verified interface or current destination exists. Do not hard-code an Agency endpoint or payload before an official interface exists.

## Operator actions

Add administration only when a human must decide, retry, recover, or deliver a result. Reuse current admin surfaces and authorization. Update a runbook only for a new operator action, recovery step, key rotation, or monitored failure mode.
