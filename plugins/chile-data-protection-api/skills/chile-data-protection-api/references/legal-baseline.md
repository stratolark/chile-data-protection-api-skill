# Chilean legal baseline

Use this packaged reference for legal scoping and minimum product capabilities. Refresh official sources only when the user asks.

Last verified: 2026-08-09.

## Official sources

- Law No. 21.719: https://www.bcn.cl/leychile/navegar?idNorma=1209272
- Law No. 21.806, which modified Law No. 21.719: https://www.bcn.cl/leychile/navegar?idNorma=1221118
- Consolidated Law No. 19.628 through 2026-11-30: https://www.bcn.cl/leychile/Navegar?dt=open&idLey=19628
- Consolidated Law No. 19.628 effective 2026-12-01: https://www.bcn.cl/leychile/Navegar?idNorma=141599&idVersion=2026-12-01
- Diario Oficial: https://www.diariooficial.interior.gob.cl/
- Official publications of the Chilean Data Protection Agency when available

As last verified on 9 August 2026, the current consolidated text applies through 30 November 2026. The principal reform is scheduled for 1 December 2026.

## Applicable period

State one period before making legal claims:

- **Current law through 30 November 2026**: Use the current consolidated version. Do not present deferred rights, deadlines, Agency procedures, or sanctions as effective
- **Transition preparation for the reform scheduled for 1 December 2026**: Design for the amended rules while keeping them separate from current obligations
- **Amended law from 1 December 2026**: Use only for relevant dates on or after the verified effective date and after official sources confirm that the reform is in force

If the date is missing, use current law for present claims and describe reform work as transition preparation.

## Interpretive boundary

The law defines rights and duties, not REST routes, schemas, identifiers, or service topology.

Code alone cannot establish controller role, processing purpose, lawful basis, necessity, retention period, legal hold, exception, transfer mechanism, impact-assessment requirement, or legal significance of an automated decision. Apply the legal-blocker test in `developer-decision-guide.md` when one of these facts is missing.

### Deferred amended-law source map

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

## Rights baseline

Current Law No. 19.628 already provides information or access, modification, cancellation, and blocking rights in Articles 6 and 12. Article 3 also permits opposition to use for advertising, market research, or opinion polling.

| Capability | Current law through 2026-11-30 | Deferred amended law from 2026-12-01 |
| --- | --- | --- |
| Access or information | Article 12 | Articles 4 and 5 |
| Rectification or modification | Articles 6 and 12 | Articles 4 and 6 |
| Erasure or cancellation | Articles 6 and 12, subject to conditions and exceptions | Articles 4 and 7 |
| Objection | Article 3 for advertising, market research, and opinion polling. Article 12 also addresses voluntary or commercial-communication data | Articles 4 and 8 provide a broader right |
| Blocking | Articles 6 and 12 | Articles 4 and 8 ter |
| Portability | No general right identified in the current consolidated text | Articles 4 and 9 |
| Automated decisions | No equivalent general right identified in the current consolidated text | Article 8 bis |

Article 11 of the deferred amended text provides a normal response period of 30 calendar days, one extension of up to another 30 calendar days, and a response to a founded temporary-blocking request within two business days. Verify these periods before changing the packaged deadline ruleset when the user requests current-source research.

## Notice and consent

A privacy notice may need to communicate the controller and representative, contact channel, data categories and subject groups, purposes and lawful bases, sources, recipients and processors, retention, transfers, rights channels, consent withdrawal, significant automated decisions, version, and effective date.

Consent must be purpose-specific and evidenced. Keep notice presentation, contract acceptance, and optional consent distinct. Do not treat viewing a notice as consent, preselect optional consent, condition service on optional processing, or make withdrawal harder than granting it.

Withdrawal affects future processing and dependent systems. It does not by itself erase evidence of earlier processing.

## Access, rectification, and erasure

Access can extend beyond a profile response. The applicable regime may require personal data being processed, source, purposes, recipients, retention information, legitimate interests, and information about significant automated decisions.

Rectification applies to inaccurate or incomplete personal data and can require effects beyond the authoritative record when derived data or recipients remain inaccurate.

Erasure or cancellation is subject to the applicable conditions, retention duties, holds, claims, and exceptions. Account closure and erasure are not the same legal or technical action. Reversible pseudonymization is not irreversible anonymization.

## Objection and blocking

Under current law, Article 3 covers opposition to advertising, market research, and opinion polling, while Article 12 also addresses voluntary or commercial-communication data. The amended Article 8 provides a broader objection right.

Blocking suspends prohibited processing while permitting storage or other operations allowed by the applicable rule. Its scope may depend on the subject, processing activity, purpose, data, and effective period.

## Portability

No general portability right was identified in the current consolidated law. Deferred Article 9 applies only when its legal conditions are met. Do not present a generic export endpoint as proof that portability obligations are satisfied.

## Automated decisions

Deferred Article 8 bis addresses significant automated decisions and profiling. When applicable, the capability may need an understandable explanation, a way for the person to provide information, human intervention, correction of inaccurate inputs, review, and a communicated outcome.

Do not add a review workflow when repository evidence shows that no applicable significant automated decision exists.

## Personal identifiers and RUT

- A natural person's RUT or RUN is personal data because it identifies or makes a natural person identifiable
- A name, personal email, phone number, or address is personal data when linked or reasonably linkable to a natural person
- A company RUT or generic company contact is not personal data solely because it identifies a legal entity. Reassess when the record identifies or concerns a natural person
- RUT, name, email, phone, and address are not sensitive data merely by statutory category. Context or combination can reveal sensitive information or create higher impact
- Public availability does not stop information from being personal data. Current public-source exceptions are specific, and amended law does not make public availability a universal lawful basis

Under the current regime, consider Article 4 authorization, consent, and exceptions, Articles 6 and 9 deletion, blocking, accuracy, and purpose rules, Article 7 secrecy, Article 11 due diligence and responsibility, and Article 12 rights.

From the verified effective date, amended Article 3 adds explicit purpose, proportionality, security, and responsibility principles. Articles 14 quáter and 14 quinquies require privacy by design and default and risk-appropriate security. Encryption and pseudonymization are examples of measures, not universal mandates.

Modulo 11 validation proves syntax only. Exact RUT lookup or contact deduplication is not authentication and cannot by itself authorize access, correction, export, blocking, or erasure.

## Incidents

Do not import the GDPR 72-hour deadline as Chilean law. If incident notification is in scope and the user requests a refresh, verify the current Chilean threshold, recipient, timing, and wording. Coordinate with Law No. 21.663 and applicable sector cybersecurity rules.

## Processors and international transfers

Primary hosting location does not establish that all data stays in Chile. Backups, support access, logs, notification providers, analytics, identity services, and subprocessors can create additional locations and recipients.

Establish each current party's role, purpose, data categories, regions, subprocessors, applicable terms, transfer mechanism, and return or deletion behavior from organizational evidence.

## Impact-assessment flags

Flag for legal review systematic evaluation, significant automated decisions, large-scale processing, systematic monitoring of public areas, sensitive data, biometric identification, children's data, high-risk dataset combinations, or novel technology with material effects on people.
