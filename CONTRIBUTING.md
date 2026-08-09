# Contributing

Thank you for improving this project.

## Before you start

- Open an issue for a material change to legal interpretation, public behavior, or plugin structure.
- Do not submit confidential information, credentials, production logs, identity documents, or real personal data.
- Use synthetic data in examples and evaluation fixtures.
- Keep the skill framework-agnostic unless a reference explicitly covers a variant.

## Make a change

1. Create a focused branch from `main`.
2. Keep one purpose per pull request.
3. Preserve the distinction between legal requirements, engineering recommendations, assumptions, and `LEGAL_INPUT_REQUIRED` decisions.
4. Add or update an evaluation case when behavior changes.
5. Run `python scripts/validate_repository.py`.
6. Describe the exact validation result in the pull request.

## Legal-source changes

A legal-source pull request must include:

- The official source URL
- The consolidated or deferred version date
- The affected article or provision
- The date the source was verified
- Whether the change affects the current regime, transition preparation, or the amended regime
- A concise explanation of the engineering impact

Use primary official Chilean sources. Do not convert an unresolved legal question into a technical fact.

## Pull-request review

Reviewers must confirm that the change:

- Does not claim or guarantee compliance
- Does not weaken authentication, authorization, validation, secret handling, telemetry redaction, or security tests
- Does not follow instructions embedded in inspected repositories, logs, or webpages
- Keeps public contracts and stored data compatible unless a break is explicitly justified
- Keeps installed skill content focused and moves project-maintenance material to the repository root
