# Security, testing, and definition of done

Use this reference before finalizing any audit or implementation.

## Contents

- Authentication, exports, telemetry, and abuse resistance
- Unit, integration, security, contract, and migration tests
- Operational and documentation checks
- Prohibited shortcuts and definition of done

## Authentication and authorization

- Map an authenticated principal to an opaque subject identifier
- Prevent IDOR across privacy requests, artifacts, decisions, and admin actions
- Test cross-tenant isolation
- Use step-up authentication for high-risk result delivery and changes
- Support former users without forcing account recreation
- Support representatives through an approved verification workflow
- Restrict service accounts to necessary stores and operations
- Require MFA for privileged privacy operations where supported
- Use separation of duties when organizational risk requires it

## Export security

- Generate asynchronously when nontrivial
- Encrypt at rest
- Use short-lived authenticated or signed retrieval
- Use safe filenames without RUT, email, or name
- Set cache-control and content-disposition correctly
- Expire and remove artifacts under an approved rule
- Avoid ordinary email attachments containing personal data
- Record retrieval success and failure without logging contents
- Prevent token reuse when one-time retrieval is required

## Telemetry and redaction

Inspect and test:

- Application logs
- Reverse-proxy and load-balancer logs
- Framework access logs
- Exceptions and crash reports
- Distributed traces
- Metrics labels
- Audit events
- Queue payload inspection
- Dead-letter queues
- APM and analytics

Redact RUT, names, emails, phones, addresses, identity evidence, consent evidence, request content, and export data.

Do not use personal values as high-cardinality metric labels. Capture actual test telemetry and assert that sensitive values are absent.

## Abuse resistance

- Rate-limit registration, recovery, verification, lookup, rights request, and export operations
- Use generic responses when details enable enumeration
- Use idempotency for retry-prone request creation and administrative actions
- Limit evidence file type, size, lifetime, and access
- Apply the application's malware-scanning policy to uploads
- Protect direct-transfer connectors against SSRF, DNS rebinding, open redirects, and data exfiltration
- Validate content type and safe archive extraction

## Unit tests

Cover at least:

- RUT normalization and valid or invalid check digits
- Keyed lookup and key-version behavior
- Deadline calculation across month boundaries, daylight-saving changes, weekends, and Chilean holidays
- State transitions and invalid transitions
- One-extension limit
- Purpose-scoped consent and objection
- Block-policy decisions
- Retention and legal holds
- Redaction helpers
- Artifact-expiry decisions

## Integration and end-to-end tests

Cover at least:

- Registration without optional consent
- Notice version presentation
- Consent grant and withdrawal propagation
- Access request from an active user
- Request from a former user
- Representative workflow when supported
- Rectification with cache and index propagation
- Full erasure
- Partial erasure because of an approved legal hold
- Temporary blocking enforced in an API request
- Temporary blocking enforced in a worker or consumer
- Objection stopping direct marketing
- Portability artifact generation, retrieval, expiry, and cleanup
- Retry and dead-letter behavior for processor failure
- Duplicate request submission and idempotency
- Overdue request monitoring
- Correction or erasure propagation acknowledgements

## Security tests

Cover at least:

- IDOR between users
- Cross-tenant access
- Privilege escalation into admin operations
- Enumeration through registration and verification responses
- Raw RUT or other personal data in logs, traces, metrics, URLs, tokens, filenames, and errors
- Export retrieval after expiration
- Reuse of an export credential
- SSRF through a portability destination
- Unauthorized block release or override
- Background processing continuing after consent withdrawal or objection
- Restore of erased data from a backup fixture without tombstone replay
- Stale event recreating an erased subject

## Contract and migration tests

- Update OpenAPI, GraphQL, RPC, AsyncAPI, or event schemas
- Validate backward compatibility where required
- Test migrations on representative existing data
- Test backfill resumability and idempotency
- Verify rollback or recovery behavior
- Verify safe failure when encryption or HMAC keys are missing
- Verify no plaintext personal data appears in migration logs
- Verify tenant-scoped uniqueness and lookup behavior

## Operational checks

Confirm:

- Overdue requests produce alerts
- Failed propagation is visible and retryable
- Dead letters have an owner and runbook
- Retention jobs are monitored
- Backup restoration replays erasure tombstones
- Key rotation has a documented procedure
- Export cleanup is scheduled and observed
- Incident reporting is configurable
- Processor deletion acknowledgements can be tracked
- Administrative access is periodically reviewable

## Documentation checks

Document:

- Legal-verification date and sources
- Controller or processor assumptions
- Data-processing inventory
- Purpose and lawful-basis placeholders or approvals
- Retention and legal-hold decisions
- API and event contracts
- Identity-verification strategies
- Deadline rules and calendar source
- Encryption and key configuration without exposing secrets
- RUT migration and rotation
- Rights-request operations
- Backup restoration and erasure replay
- Incident and processor propagation runbooks
- Remaining `LEGAL_INPUT_REQUIRED` items

## Prohibited shortcuts

Do not:

- Add only `DELETE /me` and call erasure complete
- Add controllers without tracing downstream data
- Use RUT as a primary key, public ID, password, or authentication factor
- Put raw RUT in routes, tokens, logs, metrics, traces, filenames, or cache keys
- Let clients choose a lawful basis
- Treat a displayed notice as consent
- Bundle optional consent into required terms
- Hard-code Monday through Friday as the complete business-day calendar
- Hard-code an unverified Agency endpoint or payload
- Import GDPR's 72-hour breach deadline as Chilean law
- Email ordinary personal-data export attachments
- Post exports to arbitrary user URLs
- Keep identity evidence permanently by default
- Ignore former users or representatives
- Treat encryption alone as a privacy implementation
- Ignore processors, caches, search, queues, analytics, logs, replicas, or backups
- Delete data under a legal hold without an approved decision
- Hide uncertainty behind confident wording

## Definition of done

Do not call the work complete until every applicable item is true:

- The existing API was reviewed or the greenfield architecture was stated
- The responsibility and tenant model is documented or marked `LEGAL_INPUT_REQUIRED`
- The processing inventory covers all known stores, queues, processors, exports, telemetry, and backups
- RUT is absent from prohibited identifiers and telemetry
- Notice presentation, contract acceptance, and optional consent are separate
- Privacy requests have durable intake, verification, deadline, decision, execution, result, and audit behavior
- Access, rectification, erasure, objection, blocking, and portability are implemented or explicitly not applicable with approved reasoning
- Account closure is separate from erasure
- Blocking is enforced in APIs and background systems
- Erasure covers downstream systems and backup restoration
- Consent withdrawal and objection propagate to future processing
- Exports are authenticated, short-lived, and removed safely
- Admin operations are authorized and audited
- Incident reporting uses a configurable adapter
- Tested telemetry contains no raw personal data
- API or event contracts are updated
- Migrations and backfills are safe and documented
- Relevant tests pass, or failures and unrun tests are reported exactly
- Operational runbooks exist
- Legal assumptions remain visible
- The final report does not claim or guarantee compliance

## Final implementation report

Return:

1. Scope and mode
2. Legal verification status
3. Architecture and data-flow decisions
4. Files and symbols changed
5. Migrations and backfill behavior
6. Endpoints or equivalent operations
7. Jobs, events, processors, and adapters
8. Security controls
9. Tests added
10. Exact commands run and results
11. Deployment, keys, configuration, and rollout
12. Remaining limitations and `LEGAL_INPUT_REQUIRED` decisions

Never state that tests passed when they were not run. Never hide a partial implementation behind a general statement of completion.
