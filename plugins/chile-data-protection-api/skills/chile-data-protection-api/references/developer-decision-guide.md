# Missing facts and safe defaults

Use this reference when a legal or business fact is missing. Keep the distinction between facts supplied by the organization and technical choices the developer can make.

## Facts and design choices

Legal or business owners must establish facts such as:

- Controller or processor role
- Processing purpose and lawful basis
- Required retention period, statutory start event, hold, or exception
- Final notice text and controller contact
- Grounds for refusing or limiting a request
- Applicable sector rule or transfer mechanism

Developers can choose routes, schemas, configuration placement, jobs, validation, authorization, identity-verification mechanics, migration strategy, telemetry controls, and test design. Make these choices from repository evidence and standard engineering practice.

Missing source-code evidence does not prove that an existing purpose, lawful basis, notice, contract, or approval is absent.

## Legal-blocker test

Disable a production action only when all four conditions are true:

1. The action would perform processing whose legality depends on the missing fact
2. A cited provision or verified sector rule makes that fact a precondition
3. No repository evidence supplies the fact
4. No narrower safe behavior can preserve the action

Name the one action that remains disabled. Continue schemas, configuration, dry runs, tests, manual review, and other reversible work.

An internal approval process is an organizational dependency unless a cited rule makes approval a legal precondition.

## Default decisions

| Area | Implement now | Fact still needed | Narrow safe behavior |
| --- | --- | --- | --- |
| Purpose and lawful basis | Separate required service behavior from optional processing. Enforce purpose server-side | Actual purpose and lawful basis | Keep only new optional processing off |
| Notice | Implement versioned presentation and evidence when the product needs them | Approved content and controller details | Keep draft content unpublished |
| Rights requests | Implement intake, tenant scope, status, deadlines, and manual review | Refusal grounds and exceptional handling | Accept requests but do not disclose or erase before identity is verified |
| Identity verification | Reuse the least intrusive existing method appropriate to the action | Organization-specific exceptional rules | Route uncertain cases to manual review |
| Retention and holds | Use an existing consumed value or choose a provisional runtime default | Any controlling statutory period, hold, or exception | Start with eligibility and dry-run output when deletion risk is uncertain |
| Processors and transfers | Reuse current vendor and delivery records | Roles, contractual terms, and transfer mechanism | Avoid adding a new recipient or transfer until its basis is known |

A valid RUT check digit proves syntax only. It does not identify or authenticate the person.

## Retention defaults

Use an existing consumed retention value unless repository evidence marks it as a draft or placeholder. Otherwise:

1. Select a provisional period from the data's purpose and lifecycle
2. Put the value in the existing runtime configuration system
3. Record the assumption in the implementation response
4. Add bounded selection, hold checks, dry run, outcome recording, and recovery appropriate to the deletion risk
5. Do not keep destructive execution off solely because a legal or business value is missing unless the legal-blocker test passes

An executor can still remain in dry-run mode for a confirmed engineering safety gap such as unbounded scope, missing hold checks, or no recovery path. Report that as a technical gap, not a legal blocker.

Do not invent one universal duration for core business records. Technical artifacts may use the short-lived defaults in `implementation-blueprint.md`.
