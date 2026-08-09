# Repository-first implementation patterns

Use only the section needed for the requested capability. Adapt it to the host application. Do not copy field lists, status models, endpoints, or service names from this reference.

## Core rules

- Inspect public contracts, stored data, jobs, and tests before choosing a design
- Reuse existing authentication, authorization, tenancy, persistence, audit, configuration, and job patterns
- Add a record only when the current slice reads or writes it
- Add an index only for a current query or integrity constraint
- Add a service or interface only when it owns an invariant or isolates a real boundary
- Preserve public and stored-data compatibility unless the requested behavior requires a migration
- Implement one end-to-end slice with its failure path and tests

When repository evidence is unavailable, describe required behavior and decision points. Do not invent exact routes, headers, states, fields, tables, or identifier formats.

## Runtime configuration

Use the application's existing configuration system. Add only values consumed by runtime code.

Keep each value near the feature that enforces it. Do not create one generic privacy policy object.

Validate a required value at the existing startup or feature boundary. When a law-bound value is absent, apply the exact safe behavior from `references/developer-decision-guide.md`.

Persist versions only when historical values affect runtime behavior or evidence. Do not add approval tables, draft states, or lifecycle machinery unless the product needs that workflow.

## Purpose and optional processing

For one fixed processing purpose, use the existing domain model or a validated server-side constant.

Add a runtime purpose catalog only when the product supports multiple purposes that vary at runtime. The server owns the lawful-basis mapping. A client can choose an optional preference, but it must not choose its lawful basis.

Keep new optional processing off while its purpose or lawful basis is unknown.

## Privacy notices

Use immutable notice versions when the system must prove which content was shown. Link the relevant collection or registration event to that version.

Keep display, terms acceptance, and optional consent as separate facts. Do not record a notice as accepted merely because it was displayed.

If final content is missing, implement draft storage or rendering only when the current product needs it. Keep publication disabled.

## Consent

Record grant and withdrawal durably by purpose. Reuse the existing audit or history mechanism.

Add a current-state projection only when a read path needs it. Do not introduce event sourcing for consent alone.

Propagate withdrawal to every current downstream consumer of that purpose. Use the existing job or event mechanism. Add retries, idempotency, and visible failure state when the boundary can fail after the local transaction commits.

## Rights request workflow

Treat a rights request as a case with enough state to answer these questions:

- Who made the request and for which controller or tenant
- Which right, data, or processing activity is in scope
- Whether identity and representative authority are verified
- When the request was received and when a response is due
- Which work is pending, completed, partially completed, refused, or cancelled
- Which result and reason were communicated

Reuse an existing case or workflow model when it can preserve those facts. Add only the states needed by the current capability. Keep deadline, temporary block, and execution outcome separate if one combined state permits invalid combinations.

Reuse the existing audit trail. Add request history only when current transitions need durable evidence that the existing mechanism cannot provide. Never copy request payloads into both history and application logs.

## Deadlines

Use a direct date function when one component owns the calculation. Use a service boundary only when several current consumers share changing rules or calendar data.

- Use `America/Santiago`
- Use a maintained Chilean holiday source when the rule uses business days
- Persist the source timestamps and calculation rule needed to explain a deadline
- Implement extensions only when the selected legal period permits them
- Alert on overdue work without automatically closing it

Do not equate business days with Monday through Friday.

## Identity verification

Choose the least intrusive method that gives enough confidence for the requested action.

Prefer existing mechanisms in this order when they fit the risk:

1. Current authenticated session
2. Existing step-up authentication
3. Existing verified recovery channel bound to the account
4. Existing external identity provider
5. Manual review of limited evidence

Support representatives only when the requested product flow needs them. Verify their authority separately from the subject's identity.

Do not store identity documents permanently by default. If evidence must be uploaded, use the application's access control, storage protection, malware checks, and short-lived cleanup.

Do not create a strategy interface for one verification path.

## Connecting data stores

Use each domain's existing service or repository boundary.

For one store, implement the operation directly. Introduce a shared contract only when several current stores need the same operation or when it isolates an external processor boundary.

Every affected store must return enough information to distinguish success, a lawful exclusion, a retryable failure, and a permanent failure. Adapt these outcomes to existing repository types instead of creating a new universal result enum.

If silent omission of a store creates an incomplete result, register the current handlers explicitly.

## Access and portability exports

- Collect only the in-scope data required by the applicable right
- Redact another person's data under the applicable rule
- Use a stable, documented export structure when consumers rely on it
- Generate asynchronously only when size or downstream latency makes a request-bound response unsafe
- Protect the artifact according to its exposure and lifetime
- Use short-lived authenticated retrieval
- Use safe filenames without RUT, email, phone, or name
- Remove the artifact under the configured retention rule

For direct transfer, use verified destinations or existing allowlisted connectors. Never post personal data to an arbitrary user-supplied URL. Protect the connector from SSRF, redirect abuse, and partial delivery.

## Rectification

- Validate the proposed value
- Update the authoritative source
- Update or invalidate current caches, indexes, projections, and derived values
- Propagate to current recipients when required
- Make downstream failure visible and retryable

Use an existing domain event when one already carries the change. Add an outbox only when atomic database-to-message delivery is a current correctness requirement.

## Blocking and objection

Enforce the restriction at each current path that performs the affected processing, including API services, jobs, consumers, exports, analytics, and support tools.

Keep scope explicit by subject, purpose or activity, operation, data category, and tenant when those dimensions exist in the product.

Centralize the decision only when several current consumers need the same invariant. For one path, a direct domain check is simpler.

Fail safely when a required block state is unavailable. Allow only operations that the applicable rule permits, such as storage required by a legal hold.

## Erasure

- Check applicable retention, legal holds, claims, and exceptions before destructive work
- Support partial fulfillment when some data cannot be erased
- Delete or irreversibly anonymize each in-scope copy
- Invalidate caches, search documents, files, and derived views
- Propagate to current processors and track failures
- Prevent backup restore, import, or stale events from recreating erased data

Use the repository's existing deletion marker, audit, or replay mechanism. Add a tombstone only when restoration or asynchronous replay can recreate the data and no existing mechanism prevents it.

Use dry run and bounded batches when destructive scope or recovery risk warrants them.

## RUT storage and migration

Treat a natural-person RUT as personal data, not as authentication.

For an existing plaintext RUT:

1. Find every current copy, index, relationship, public contract, export, and telemetry path
2. Confirm whether exact lookup is required
3. Preserve existing stronger protection
4. Under the legal baseline, choose the least-complex adequate storage and lookup controls from the actual threat model
5. Under the strict security default, use a surrogate subject identifier, protect recoverable canonical RUT, and add keyed lookup only when exact lookup is required
6. Backfill safely and use dual read or write only when deployment compatibility requires it
7. Validate counts and lookup behavior without printing RUT
8. Remove legacy plaintext only after rollout validation and recovery planning

Use proven encryption and keyed hashing libraries. Keep keys outside the primary data store. Add key versions and rotation behavior when the selected protection requires rotation.

## Retention and legal holds

Model retention by the current purpose and data category when their rules differ. Do not use account age as a universal proxy.

When the period or hold rule is unresolved, implement eligibility discovery and dry-run reporting. Keep destructive execution off only when the legal-blocker test passes.

A production executor needs bounded selection, hold checks, idempotent deletion or anonymization, outcome recording, retry behavior, safe metrics, and monitoring. Reuse the existing job framework.

## Disclosures and processors

Record only the metadata needed to identify a current recipient and propagate correction, objection, blocking, or erasure. Do not copy full payloads merely to create a registry.

Reuse existing vendor, webhook, or delivery records. Add a new disclosure record only when the product must prove or retry a disclosure and no current record can do so.

## Incidents

Reuse the existing security incident workflow. Add personal-data impact fields only when the requested slice needs them.

Create an external submission boundary only when the application has a verified authority or sector endpoint, multiple current destinations, or testable submission behavior. Do not hard-code an Agency URL or payload before an official interface exists.

## Operator actions

Add administration only when the current slice needs a human decision, retry, or result delivery. Reuse existing admin surfaces and authorization.

Apply separation of duties when the threat model or organization requires it. Do not expose operator actions as ordinary user routes.

Update an existing runbook only when the implementation adds an operator action, recovery step, key rotation, or monitored failure mode.

## Scope check

Create functional code, migrations, consumed runtime configuration, behavior tests, and changed API or event contracts.

Do not create inventory files, decision logs, gap reports, policy summaries, or a privacy documentation tree by default.

Do not scaffold another capability unless the user requests it or the first slice needs it for correctness.
