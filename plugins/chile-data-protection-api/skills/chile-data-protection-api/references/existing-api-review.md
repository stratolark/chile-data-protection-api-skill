# Existing API evidence review

Use this reference to locate evidence in an existing repository. Follow the output contract in `SKILL.md`.

## Start with ordinary user journeys

Identify the public operations through which a person can:

- Register, sign in, recover access, or manage a profile
- Submit, view, correct, export, block, object to, or erase personal data
- Grant or withdraw optional consent
- Close an account or unsubscribe from marketing

Trace enough evidence to determine technical readiness and the highest-impact gaps. Perform an exhaustive inventory only when the user requests it.

## Repository discovery

Inspect the repository's established boundaries before proposing new ones:

- Application entry points, routing, middleware, and dependency composition
- Authentication, authorization, tenancy, and stable subject identity
- Domain services, persistence, migrations, schemas, and validation
- Configuration, jobs, queues, events, retries, and idempotency
- Files, search, caches, analytics, exports, and backups
- Vendors for hosting, identity, notifications, support, observability, CRM, and payments
- API contracts, tests, CI configuration, runbooks, and deployment topology

Check repository guidance and current Git state before edits. During an audit, inspect tests and CI as evidence without executing project code unless `SKILL.md` permits it.

## Trace the in-scope data

For each relevant field or category, follow:

1. Ingress and server-side validation
2. Subject, tenant, account, or other ownership association
3. Authoritative storage and indexes
4. Jobs, events, caches, projections, files, and search
5. Logs, traces, metrics, analytics, and support tooling
6. Processors, recipients, exports, and international paths
7. Retention, deletion, anonymization, backup, and restoration behavior

Record the trace in working analysis. Use exact file, symbol, route, table, job, or contract evidence in findings.

Do not treat the primary database as the whole data flow. Stop tracing a branch when repository evidence shows that it cannot read, copy, disclose, or recreate the in-scope data.

## Responsibility and tenancy

Determine from evidence:

- Which authenticated principal maps to the subject
- Which controller, processor, tenant, or customer owns the operation
- Whether administrators, service accounts, representatives, or former users require separate paths
- Where object ownership and tenant isolation are enforced
- Whether background work preserves the same scope

Do not infer a legal role from storage alone. Report unresolved role or ownership facts as limitations unless they pass the legal-blocker test.

## Reuse existing capabilities

Search for current mechanisms before proposing a privacy-specific subsystem:

- Case, ticket, or workflow records
- Audit history or domain events
- Export generation and secure downloads
- Profile correction or account closure
- Marketing preferences and consent history
- Retention, cleanup, or legal-hold behavior
- Incident response and operator tooling
- Vendor, webhook, or delivery records
- RUT normalization, lookup, protection, or migration

Describe how the existing mechanism can be extended. Add a new component only when the current boundary cannot preserve a required invariant or failure state.

## Confirm findings

A technical gap needs repository evidence of missing or unsafe behavior. Distinguish it from:

- A legal or business fact not represented in source code
- An optional strict-security improvement
- An amended-law capability whose triggering conditions are absent from the product's actual processing

For every confirmed gap, identify the affected journey, data flow, implementation surface, security controls, tests, and evidence. Keep findings in the response unless the user requests a repository artifact.

## Contract and migration evidence

When stored data or a public contract must change, inspect:

- Current producers and consumers
- Identifier exposure in paths, payloads, tokens, files, and events
- Existing rows, uniqueness, indexes, and tenant scope
- Backfill size, resumability, dual-read or dual-write needs, and rollback
- Generated contracts and compatibility tests
- Logging and metrics used during migration

Use `implementation-blueprint.md` for the selected migration design and `engineering-postures.md` for identifier protection. Do not recommend replacing an existing identifier until the current exposure and compatibility constraints are known.

## Runtime and operational evidence

Confirm that introduced or affected behavior has:

- Visible and retryable downstream failures
- Bounded scheduled or batch work
- Monitored cleanup and propagation
- Recovery behavior for backups, stale events, and partial execution
- Authorized operator actions and an owner for manual review
- Key rotation and recovery when the design introduces protected lookup or encrypted values

Recommend a runbook change only when the implementation adds an operator action, recovery step, or monitored failure mode.
