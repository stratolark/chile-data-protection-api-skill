# Chile Data Protection API Codex Skill

An installable Codex skill for auditing, designing, and implementing backend API capabilities related to personal-data processing in Chile.

The skill covers RUT handling, privacy notices, consent, data-subject requests, retention, blocking, erasure, portability, automated decisions, incidents, and downstream propagation. It adapts its recommendations to the host repository instead of imposing a framework or fixed API design.

> [!IMPORTANT]
> This project is an engineering aid. It does not provide legal advice, certify compliance, or replace review by qualified Chilean legal counsel.

## Legal status

The skill requires every invocation to verify the applicable legal regime from official sources.

- Law No. 19.628 remains the current consolidated regime through November 30, 2026.
- The principal amendments introduced by Law No. 21.719 are scheduled to enter into force on December 1, 2026.
- Future amendments, regulations, Agency instructions, and sector-specific rules must be checked at execution time.

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

Invoke the skill explicitly:

```text
$chile-data-protection-api Audit this API for Chilean personal-data engineering gaps.
```

Other examples:

- Audit a NestJS, FastAPI, Go, .NET, or Rust API without changing files.
- Design RUT storage and lookup without using RUT as a public identifier.
- Implement access, rectification, erasure, objection, blocking, and portability workflows.
- Review consent withdrawal, retention jobs, downstream deletion, or telemetry redaction.

The skill should not activate for generic CRUD, non-Chilean GDPR work, privacy-policy copywriting, or requests for a final legal opinion.

## Repository layout

```text
.agents/plugins/marketplace.json
plugins/chile-data-protection-api/
  .codex-plugin/plugin.json
  skills/chile-data-protection-api/
    SKILL.md
    agents/openai.yaml
    references/
evals/cases.json
scripts/validate_repository.py
```

Repository documentation and tests stay outside the skill payload so installed agents load only the instructions they need.

## Validate

Run the dependency-free repository validator:

```text
python scripts/validate_repository.py
```

The validator checks plugin and marketplace metadata, skill frontmatter, reference paths, legal-regime guardrails, UI metadata, evaluation fixtures, and common secret or placeholder patterns.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution requirements and [SECURITY.md](SECURITY.md) for private vulnerability reporting. Do not place real personal data, credentials, identity documents, or production logs in issues, pull requests, or evaluation fixtures.

## Resumen en español

Este proyecto contiene una habilidad instalable para auditar, diseñar e implementar capacidades técnicas de protección de datos personales en APIs con alcance chileno.

No entrega asesoría legal ni certifica cumplimiento. La habilidad debe verificar en fuentes oficiales qué régimen legal está vigente, distinguir los requisitos actuales de la preparación para la reforma y marcar las decisiones jurídicas pendientes como `LEGAL_INPUT_REQUIRED`.

## License

MIT. See [LICENSE](LICENSE).
