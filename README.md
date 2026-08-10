# Chile Data Protection API Codex Skill

An installable Codex skill for auditing, designing, and implementing backend API capabilities related to personal-data processing in Chile.

The skill covers RUT handling, privacy notices, consent, data-subject requests, retention, blocking, erasure, portability, automated decisions, incidents, and downstream propagation. It adapts its recommendations to the host repository instead of imposing a framework or fixed API design.

For audits and implementations, it uses the complete amended Law No. 19.628 framework scheduled for 1 December 2026 as the default engineering target. It keeps that legal baseline separate from the chosen security posture:

- **Legal baseline** implements verified legal requirements and the least-complex controls justified by actual risk.
- **Strict security default** adds conservative identifier, encryption, lookup, telemetry, export, and abuse-resistance defaults.

The user can add individual strict controls to the legal baseline without creating another posture.

An audit with no posture specified reports legal gaps and strict-security recommendations separately. An implementation uses strict mode as the recommended default unless the user selects another posture.

The skill gives developers a complete implementation path. It makes technical decisions from repository evidence and explains alternatives only when they change a current tradeoff. A production action stays disabled only when a cited law makes a missing fact a precondition for that action. Code, migrations, tests, runtime configuration, and dry runs can continue.

Audit mode gives a technical-readiness verdict for ordinary user journeys. It leads with four high-impact tasks and keeps every other confirmed gap in a compact next-actions table. It inspects existing tests and CI but does not run project code unless the user asks or a finding needs runtime reproduction.

The implementation is code-first. The skill does not create inventories, decision logs, gap reports, policy summaries, or documentation trees unless the user asks.

Every posture keeps normal production engineering practices. Strict mode strengthens applicable controls. It does not automatically add microservices, queues, event sourcing, custom cryptography, or new dependencies. Recommendations must reuse the repository's established mechanisms. Each complex recommendation must address a current requirement or concrete risk.

> [!IMPORTANT]
> This project is an engineering aid. It does not provide legal advice, certify compliance, or replace review by qualified Chilean legal counsel.

## Legal target

The skill uses its packaged legal baseline by default. It does not browse or refresh legal sources every time it loads.

- Law No. 19.628 remains the current consolidated regime through November 30, 2026.
- The principal amendments introduced by Law No. 21.719 are scheduled to enter into force on December 1, 2026.
- Audits and implementations use the complete amended framework as required scope now. They do not defer portability, automated-decision safeguards, amended deadlines, or other applicable capabilities because the effective date has not arrived.
- Before December 1, the skill notes the current legal status without weakening the technical verdict or implementation plan.
- The user can request a source refresh when current legal research is needed.
- If a deployment date falls outside the packaged baseline, the skill offers a refresh and continues reversible engineering work.

## Install from GitHub

After this repository is published, add its marketplace and install the plugin:

```text
codex plugin marketplace add stratolark/chile-data-protection-api-skill
codex plugin add chile-data-protection-api@chile-data-protection
```

Start a new Codex thread after installation.

For standalone local experimentation, ask `$skill-installer` to install `chile-data-protection-api` from:

```text
https://github.com/stratolark/chile-data-protection-api-skill/tree/main/plugins/chile-data-protection-api/skills/chile-data-protection-api
```

## Update

Refresh the marketplace snapshot to update the installed plugin:

```text
codex plugin marketplace upgrade chile-data-protection
```

Run `codex plugin list` to confirm the installed version, then start a new Codex thread.

## Remove

Remove the installed plugin:

```text
codex plugin remove chile-data-protection-api@chile-data-protection
```

To also remove the marketplace source:

```text
codex plugin marketplace remove chile-data-protection
```

## Use

Open Codex in the API repository. Then invoke the skill explicitly.

### Technical-readiness audit

```text
$chile-data-protection-api Audit this API against the complete amended Chilean personal-data framework effective 1 December 2026. Tell me whether ordinary users can use it safely. Lead with the four highest-impact implementation tasks, then list every remaining confirmed gap in a compact next-actions table. Include exact routes, jobs, data changes, security controls, tests to add, and file evidence. Do not modify files or run project tests.
```

### API design review

```text
$chile-data-protection-api Review this API design for Chilean personal-data processing. Recommend the exact endpoints, internal jobs, data model, migrations, security controls, and practical defaults. Separate legal minimums from optional strict security.
```

### Implement rights-request intake

```text
$chile-data-protection-api Implement one authenticated rights-request workflow for access, rectification, cancellation, and blocking. Reuse the existing authentication, authorization, persistence, audit, and API conventions. Include migrations, OpenAPI changes, and focused tests.
```

### Implement retention

```text
$chile-data-protection-api Connect the existing retention configuration to the maintenance job. Use current repository values as engineering defaults unless they are marked as drafts. Add dry-run output, hold checks, bounded deletion, retry behavior, and focused tests. Do not add a public retention endpoint unless the existing admin API needs one.
```

### Add selected strict controls

```text
$chile-data-protection-api Use the legal baseline. Also add encrypted recoverable RUT storage, keyed exact lookup, opaque public identifiers, and telemetry redaction. Keep unrelated strict controls out of scope.
```

### Refresh legal sources

```text
$chile-data-protection-api Refresh the official Chilean legal sources first. Then revalidate this API against the complete amended framework. Cite the official sources that changed the implementation plan.
```

The skill does not activate for generic CRUD, non-Chilean GDPR work, privacy-policy copywriting, or requests for a final legal opinion.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/chile-data-protection-api/
  .codex-plugin/plugin.json
  skills/chile-data-protection-api/
    SKILL.md
    agents/openai.yaml
    references/
scripts/validate_repository.py
```

Repository documentation and tests stay outside the skill payload so installed agents load only the instructions they need.

## Validate

Run the dependency-free repository validator:

```text
python scripts/validate_repository.py
```

The validator checks plugin and marketplace metadata, skill frontmatter, reference paths, official-source metadata, UI metadata, workflows, links, and repository hygiene.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution requirements and [SECURITY.md](SECURITY.md) for private vulnerability reporting. Do not place real personal data, credentials, identity documents, or production logs in issues, pull requests, or test prompts.

## Resumen en español

Este proyecto contiene una habilidad instalable para auditar, diseñar e implementar capacidades técnicas de protección de datos personales en APIs con alcance chileno.

No entrega asesoría legal ni certifica cumplimiento. La habilidad usa una base legal incluida y solo actualiza las fuentes cuando el usuario lo solicita.

La habilidad recomienda una solución técnica y ofrece opciones concretas. Solo agrega configuración que el código usa. No crea registros de decisiones ni documentos de seguimiento por defecto.

El equipo puede elegir la base legal o la postura de seguridad estricta. También puede agregar controles estrictos concretos a la base legal. Si no elige, la habilidad usa la postura estricta como supuesto recomendado.

## License

MIT. See [LICENSE](LICENSE).
