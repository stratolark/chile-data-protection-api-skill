# Developer decisions and legal preconditions

Use this guide when a missing legal or business fact affects implementation. Give the developer a working technical path and keep any disabled behavior as narrow as possible.

## Separate facts from design choices

The skill must decide technical matters from repository evidence and established engineering practice. Examples include:

- Route and command shape
- Module and service boundaries
- Database schema and migration mechanics
- Runtime configuration placement
- Identifier representation
- Authentication and identity-verification mechanics
- Authorization and tenant enforcement
- Validation, error handling, telemetry, jobs, and tests
- Rollout, retries, idempotency, and recovery when the current boundary needs them

Do not ask legal or privacy teams to approve these choices unless the organization already has a relevant deployment control.

The skill cannot invent facts that belong to the controller or applicable law. Examples include:

- Who the controller is for the processing activity
- Why the data is processed and which lawful basis applies
- The final notice content
- A retention period or statutory hold
- A legal exception, refusal ground, or transfer mechanism

These facts do not stop unrelated engineering work.

## Legal-blocker test

Keep a production action disabled only when all four statements are true:

1. A provision in the selected legal regime or a verified sector rule makes the missing fact a precondition for that action
2. The fact cannot be established from the repository or the user's supplied context
3. Performing the action without the fact creates a concrete legal violation or a false required representation
4. No safe, reversible implementation assumption can allow that same action to run

If any statement is false, do not call it a legal blocker. Select the technical solution and continue.

Always cite the provision or verified rule. If the source is unclear, report a legal limitation and offer a source refresh. Do not stop implementation on an uncited concern.

## Common decisions

| Domain concept | Technical solution the skill must provide | Fact the skill must not invent | Narrow action that can remain disabled |
| --- | --- | --- | --- |
| Controller and tenancy | Match controller lookup and request scope to existing tenancy and authorization | Which organization controls each processing activity | Publishing a controller claim when the required identity is unknown |
| Purpose and lawful basis | Separate required service behavior from optional processing and enforce purpose at the server boundary | The actual purpose and lawful basis | Enabling the new processing activity |
| Privacy notice | Implement versioned draft, preview, publication, and evidence only when the product needs them | Final notice content and effective date | Publishing the notice or starting processing that legally requires it |
| Rights requests | Reuse authentication for current users and a proportionate recovery or manual-review path for others | A legal refusal ground or exception | Disclosure, erasure, or automatic refusal when its legal precondition is unresolved |
| Retention and holds | Implement eligibility calculation, dry run, bounded execution, audit, and recovery using existing job patterns | The retention period, start event when legally defined, and applicable hold | Destructive deletion for the affected category |
| International transfer | Reuse the current vendor and region boundaries, restrict destinations, and record delivery | The applicable transfer mechanism or permitted recipient | Sending personal data to the unresolved destination |

Identity verification is normally a technical and risk decision. Choose the least intrusive method that gives enough confidence for the requested action. A valid RUT check digit is never proof of identity.

## Safe defaults

- Keep new optional processing off when its purpose or lawful basis is unknown
- Keep draft notice text unpublished
- Accept and track a rights request before identity or scope review is complete
- Route uncertain exceptions and refusals to manual review
- Run retention discovery and deletion in dry-run mode until the deletion preconditions are known
- Preserve current production behavior when a new configuration value is missing

Add configuration only when runtime code reads it. Keep a missing value absent and validate it at the existing configuration boundary. Do not add placeholder records, generic policy objects, approval tables, or decision logs.

Persist versions only when previous values affect behavior or evidence. Notices and consent records often need versions. Static contact configuration usually does not.

## Developer-facing response

Lead with the solution you selected:

```text
Recommended implementation: <repository-consistent design>
Why: <current evidence and tradeoff>
Runtime effect: <code, configuration, migration, or deployment change>
Safe behavior now: <what can run immediately>
Legal precondition, if any: <missing fact, cited rule, and exact disabled action>
Owner: <business, privacy, or legal role that can supply the fact>
Alternative: <include only when it has a material current tradeoff>
```

Do not return numbered legal placeholders, a blank questionnaire, or a request for a policy document.
