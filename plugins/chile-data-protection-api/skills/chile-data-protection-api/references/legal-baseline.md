# Chilean legal baseline

Use this packaged reference for legal scoping and the complete amended-framework product target. Refresh official sources only when the user asks.

Last verified: 2026-08-09.

## Official sources

- Law No. 21.719: https://www.bcn.cl/leychile/navegar?idNorma=1209272
- Law No. 21.806, which modified Law No. 21.719: https://www.bcn.cl/leychile/navegar?idNorma=1221118
- Consolidated Law No. 19.628 through 2026-11-30: https://www.bcn.cl/leychile/Navegar?dt=open&idLey=19628
- Consolidated Law No. 19.628 effective 2026-12-01: https://www.bcn.cl/leychile/Navegar?idNorma=141599&idVersion=2026-12-01
- Diario Oficial: https://www.diariooficial.interior.gob.cl/
- Official publications of the Chilean Data Protection Agency when available

As last verified on 9 August 2026, the current consolidated text applies through 30 November 2026. The amended framework is scheduled for 1 December 2026.

## Default engineering target

Audit, design, and implement against the complete amended Law No. 19.628 framework scheduled for 1 December 2026. Treat every applicable capability in that framework as required implementation scope even when the work occurs earlier.

- Do not omit a gap because the effective date has not arrived
- Do not classify amended-law capabilities as optional future work
- Use the amended rights, deadlines, principles, security duties, and responsibility rules for technical readiness
- Keep current legal enforceability separate from the engineering target

Before 1 December 2026, accurately note that current Law No. 19.628 remains legally effective. That note does not reduce the implementation plan. Use a current-law-only scope only when the user explicitly asks for it.

## Interpretive boundary

The law defines rights and duties, not REST routes, schemas, identifiers, or service topology.

Code alone cannot establish controller role, processing purpose, lawful basis, necessity, retention period, legal hold, exception, transfer mechanism, impact-assessment requirement, or legal significance of an automated decision. Apply the legal-blocker test in `developer-decision-guide.md` when one of these facts is missing.

### Amended-framework source map

The article numbers below refer to the consolidated version scheduled for 1 December 2026.

| Capability | Provision |
| --- | --- |
| General data-subject rights | Article 4 |
| Access | Article 5 |
| Rectification | Article 6 |
| Erasure | Article 7 |
| Objection | Article 8 |
| Automated decisions and profiling | Article 8 bis |
| Blocking | Article 8 ter |
| Portability | Article 9 |
| Exercise channels and procedure | Articles 10 and 11 |
| Retention proportionality | Article 3 |
| Transparency and notice | Article 14 ter |
| Privacy by design and default | Article 14 quáter |
| Risk-appropriate security | Article 14 quinquies |
| Personal-data incidents | Article 14 sexies |
| Impact assessment | Article 15 ter |

## Rights baseline

Current Law No. 19.628 already provides information or access, modification, cancellation, and blocking rights in Articles 6 and 12. Article 3 also permits opposition to use for advertising, market research, or opinion polling.

Use the complete amended-target column for readiness findings and implementation. The current-law column is legal timing context only.

| Capability | Current law through 2026-11-30 | Complete amended target from 2026-12-01 |
| --- | --- | --- |
| Access or information | Article 12 | Articles 4 and 5 |
| Rectification or modification | Articles 6 and 12 | Articles 4 and 6 |
| Erasure or cancellation | Articles 6 and 12, subject to conditions and exceptions | Articles 4 and 7 |
| Objection | Article 3 for advertising, market research, and opinion polling. Article 12 also addresses voluntary or commercial-communication data | Articles 4 and 8 provide a broader right |
| Blocking | Articles 6 and 12 | Articles 4 and 8 ter |
| Portability | No general right identified in the current consolidated text | Articles 4 and 9 |
| Automated decisions | No equivalent general right identified in the current consolidated text | Article 8 bis |

Use the amended Article 11 deadlines in the default design: respond within 30 calendar days, allow one extension of up to another 30 calendar days, and answer a founded temporary-blocking request within two business days. Make the rules configurable and use `America/Santiago` with a maintained Chilean holiday source.

## Notice and consent

A privacy notice may need to communicate the controller and representative, contact channel, data categories and subject groups, purposes and lawful bases, sources, recipients and processors, retention, transfers, rights channels, consent withdrawal, significant automated decisions, version, and effective date.

Consent must be purpose-specific and evidenced. Keep notice presentation, contract acceptance, and optional consent distinct. Do not treat viewing a notice as consent, preselect optional consent, condition service on optional processing, or make withdrawal harder than granting it.

Withdrawal affects future processing and dependent systems. It does not by itself erase evidence of earlier processing.

## Access, rectification, and erasure

Access can extend beyond a profile response. The applicable regime may require personal data being processed, source, purposes, recipients, retention information, legitimate interests, and information about significant automated decisions.

Rectification applies to inaccurate or incomplete personal data and can require effects beyond the authoritative record when derived data or recipients remain inaccurate.

Erasure or cancellation is subject to the applicable conditions, retention duties, holds, claims, and exceptions. Account closure and erasure are not the same legal or technical action. Reversible pseudonymization is not irreversible anonymization.

Amended Article 3 permits retention only while necessary for the processing purpose, subject to legal exceptions. Article 7 provides erasure grounds when data is no longer necessary, consent is revoked without another legal basis, processing was unlawful, data is stale, deletion follows a binding decision or duty, or a valid objection leaves no other legal basis. Article 7 also preserves processing needed for expression and information, a legal duty or contract, public functions or interests, public health, qualifying historical, statistical or scientific work, and legal claims.

Implement the grounds and exceptions that apply to the product. Route an uncertain exception to manual review instead of disabling unrelated erasure. Article 8 ter governs temporary blocking while a request is resolved and is not the legal basis for a retention schedule.

## Objection and blocking

Under current law, Article 3 covers opposition to advertising, market research, and opinion polling, while Article 12 also addresses voluntary or commercial-communication data. The amended Article 8 provides a broader objection right.

Blocking suspends prohibited processing while permitting storage or other operations allowed by the applicable rule. Its scope may depend on the subject, processing activity, purpose, data, and effective period.

## Portability

Use amended Article 9 for the default readiness assessment. Portability applies when processing is automated and based on the subject's consent. Do not present a generic access export as proof that portability is implemented.

## Automated decisions

Use amended Article 8 bis for the default readiness assessment. When the product makes applicable significant automated decisions or profiles people, require an understandable explanation, a way for the person to provide information, human intervention, correction of inaccurate inputs, review, and a communicated outcome.

Do not add a review workflow when repository evidence shows that no applicable significant automated decision exists.

## Personal identifiers and RUT

- A natural person's RUT or RUN is personal data because it identifies or makes a natural person identifiable
- A name, personal email, phone number, or address is personal data when linked or reasonably linkable to a natural person
- A company RUT or generic company contact is not personal data solely because it identifies a legal entity. Reassess when the record identifies or concerns a natural person
- RUT, name, email, phone, and address are not sensitive data merely by statutory category. Context or combination can reveal sensitive information or create higher impact
- Public availability does not stop information from being personal data. Current public-source exceptions are specific, and amended law does not make public availability a universal lawful basis

Under the current regime, consider Article 4 authorization, consent, and exceptions, Articles 6 and 9 deletion, blocking, accuracy, and purpose rules, Article 7 secrecy, Article 11 due diligence and responsibility, and Article 12 rights.

For the default engineering target, amended Article 3 adds explicit purpose, proportionality, security, and responsibility principles. Articles 14 quáter and 14 quinquies require privacy by design and default and risk-appropriate security. Encryption and pseudonymization are examples of measures, not universal mandates.

Modulo 11 validation proves syntax only. Exact RUT lookup or contact deduplication is not authentication and cannot by itself authorize access, correction, export, blocking, or erasure.

## Incidents

Amended Article 14 sexies requires reporting qualifying personal-data security breaches to the Agency without undue delay when there is a reasonable risk to people's rights and freedoms. It also requires records of the communication. Notice to affected people applies to the categories stated in that article. Do not import the GDPR 72-hour deadline as Chilean law.

Reuse the organization's incident process when it can capture the assessment, affected data and people, effects, response measures, notification decision, content, destination, and evidence. Refresh sources before hard-coding an Agency transport, payload, or deadline that depends on later instructions. Coordinate with Law No. 21.663 and applicable sector cybersecurity rules.

## Processors and international transfers

Primary hosting location does not establish that all data stays in Chile. Backups, support access, logs, notification providers, analytics, identity services, and subprocessors can create additional locations and recipients.

Establish each current party's role, purpose, data categories, regions, subprocessors, applicable terms, transfer mechanism, and return or deletion behavior from organizational evidence.

## Impact-assessment flags

Amended Article 15 ter requires an impact assessment before high-risk processing begins. It always covers systematic and exhaustive evaluation based on automated processing with significant legal effects, large-scale processing, systematic monitoring of public areas, and sensitive or specially protected data processed under a consent exception.

Also flag other processing whose nature, scope, context, technology, or purpose probably creates high risk. Record whether the trigger is applicable, not applicable, or unknown. Do not invent a code subsystem for the assessment. Identify the processing boundary and technical mitigations, then use the organization's existing risk or review process.
