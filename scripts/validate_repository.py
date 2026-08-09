#!/usr/bin/env python3
"""Validate the public plugin repository without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "chile-data-protection-api"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "chile-data-protection-api"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
LEGAL_BASELINE = SKILL_ROOT / "references" / "legal-baseline.md"
OPENAI_YAML = SKILL_ROOT / "agents" / "openai.yaml"
PLUGIN_JSON = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".agents" / "plugins" / "marketplace.json"
EVALS_JSON = ROOT / "evals" / "cases.json"

EXPECTED_SKILL_NAME = "chile-data-protection-api"
EXPECTED_MARKETPLACE_NAME = "chile-data-protection"
EXPECTED_EVAL_IDS = {
    "audit-only-chilean-api",
    "transition-preparation",
    "current-law-request",
    "offline-legal-refresh",
    "generic-gdpr",
    "generic-crud",
    "legal-opinion-only",
    "repository-prompt-injection",
    "rut-greenfield",
}
REQUIRED_REGIMES = {
    "CURRENT_LAW_THROUGH_2026_11_30",
    "TRANSITION_PREPARATION_FOR_2026_REFORM",
    "AMENDED_LAW_FROM_2026_12_01",
}


class Validation:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.failures.append(message)

    def load_json(self, path: Path) -> object:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            self.failures.append(f"Cannot load {path.relative_to(ROOT)}: {error}")
            return {}


def parse_frontmatter(validation: Validation, text: str) -> dict[str, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
    validation.require(match is not None, "SKILL.md must start with YAML frontmatter")
    if match is None:
        return {}

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        validation.require(bool(separator), f"Invalid frontmatter line: {line}")
        if separator:
            fields[key.strip()] = value.strip().strip('"')
    return fields


def validate_skill(validation: Validation) -> None:
    validation.require(SKILL_FILE.is_file(), "Missing installed SKILL.md")
    if not SKILL_FILE.is_file():
        return

    text = SKILL_FILE.read_text(encoding="utf-8")
    fields = parse_frontmatter(validation, text)
    validation.require(set(fields) == {"name", "description"}, "Frontmatter must contain only name and description")
    validation.require(fields.get("name") == EXPECTED_SKILL_NAME, "Skill name does not match plugin name")
    validation.require(bool(fields.get("description")), "Skill description must not be empty")
    validation.require(len(text.splitlines()) <= 500, "SKILL.md exceeds 500 lines")

    for regime in REQUIRED_REGIMES:
        validation.require(regime in text, f"SKILL.md is missing legal regime {regime}")

    for relative_reference in set(re.findall(r"references/[A-Za-z0-9_.-]+\.md", text)):
        validation.require((SKILL_ROOT / relative_reference).is_file(), f"Missing reference {relative_reference}")

    safety_phrases = (
        "untrusted data, not instructions",
        "preserve unrelated work",
        "do not expose secrets or personal data",
    )
    for phrase in safety_phrases:
        validation.require(phrase in text, f"SKILL.md is missing safety boundary: {phrase}")


def validate_legal_baseline(validation: Validation) -> None:
    validation.require(LEGAL_BASELINE.is_file(), "Missing legal baseline")
    if not LEGAL_BASELINE.is_file():
        return

    text = LEGAL_BASELINE.read_text(encoding="utf-8")
    validation.require("Last verified: 2026-08-08" in text, "Legal baseline verification date is missing")
    for regime in REQUIRED_REGIMES:
        validation.require(regime in text, f"Legal baseline is missing legal regime {regime}")
    for label in ("LAW", "ENGINEERING_RECOMMENDATION", "LEGAL_INPUT_REQUIRED"):
        validation.require(label in text, f"Legal baseline is missing source label {label}")


def validate_plugin(validation: Validation) -> None:
    plugin = validation.load_json(PLUGIN_JSON)
    if not isinstance(plugin, dict):
        validation.failures.append("plugin.json must contain an object")
        return

    validation.require(plugin.get("name") == EXPECTED_SKILL_NAME, "Plugin name is invalid")
    validation.require(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(plugin.get("version", "")))), "Plugin version must use strict SemVer")
    validation.require(plugin.get("license") == "MIT", "Plugin license must match LICENSE")
    validation.require(plugin.get("repository") == "https://github.com/stratolark/chile-data-protection-api-skill", "Plugin repository URL is invalid")
    validation.require(plugin.get("skills") == "./skills/", "Plugin skills path is invalid")
    validation.require(isinstance(plugin.get("author"), dict) and bool(plugin["author"].get("name")), "Plugin author name is required")
    interface = plugin.get("interface")
    validation.require(isinstance(interface, dict), "Plugin interface metadata is required")
    if isinstance(interface, dict):
        for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "defaultPrompt"):
            validation.require(bool(interface.get(field)), f"Plugin interface.{field} is required")


def validate_marketplace(validation: Validation) -> None:
    marketplace = validation.load_json(MARKETPLACE_JSON)
    if not isinstance(marketplace, dict):
        validation.failures.append("marketplace.json must contain an object")
        return

    validation.require(marketplace.get("name") == EXPECTED_MARKETPLACE_NAME, "Marketplace name is invalid")
    plugins = marketplace.get("plugins")
    validation.require(isinstance(plugins, list) and len(plugins) == 1, "Marketplace must contain exactly one plugin")
    if not isinstance(plugins, list) or len(plugins) != 1:
        return

    entry = plugins[0]
    validation.require(entry.get("name") == EXPECTED_SKILL_NAME, "Marketplace plugin name is invalid")
    validation.require(entry.get("source") == {"source": "local", "path": "./plugins/chile-data-protection-api"}, "Marketplace source is invalid")
    validation.require(entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Marketplace policy is invalid")
    validation.require(entry.get("category") == "Developer Tools", "Marketplace category is invalid")


def validate_openai_yaml(validation: Validation) -> None:
    validation.require(OPENAI_YAML.is_file(), "Missing agents/openai.yaml")
    if not OPENAI_YAML.is_file():
        return

    text = OPENAI_YAML.read_text(encoding="utf-8")
    for field in ("display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation:"):
        validation.require(field in text, f"agents/openai.yaml is missing {field}")
    validation.require(f"${EXPECTED_SKILL_NAME}" in text, "Default prompt must mention the skill explicitly")


def validate_evals(validation: Validation) -> None:
    cases = validation.load_json(EVALS_JSON)
    validation.require(isinstance(cases, list), "Evaluation cases must be an array")
    if not isinstance(cases, list):
        return

    ids = {case.get("id") for case in cases if isinstance(case, dict)}
    validation.require(ids == EXPECTED_EVAL_IDS, "Evaluation case IDs are incomplete or unexpected")
    for case in cases:
        validation.require(isinstance(case, dict), "Each evaluation case must be an object")
        if not isinstance(case, dict):
            continue
        validation.require(bool(case.get("prompt")), f"Evaluation {case.get('id')} is missing a prompt")
        expect = case.get("expect")
        validation.require(isinstance(expect, dict) and isinstance(expect.get("activate"), bool), f"Evaluation {case.get('id')} needs expect.activate")


def validate_repository_hygiene(validation: Validation) -> None:
    forbidden_patterns = {
        "unfinished placeholder": re.compile(r"\[(?:TODO|FIXME|TBD)(?::|\])", re.IGNORECASE),
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "GitHub token": re.compile(r"\bgh[opurs]_[A-Za-z0-9]{20,}\b"),
        "OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    }
    text_suffixes = {".md", ".json", ".yaml", ".yml", ".py", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in text_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in forbidden_patterns.items():
            validation.require(pattern.search(text) is None, f"Found {label} in {path.relative_to(ROOT)}")


def validate_local_markdown_links(validation: Validation) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            validation.require((path.parent / target).exists(), f"Broken local link {raw_target} in {path.relative_to(ROOT)}")


def validate_workflow_pins(validation: Validation) -> None:
    workflow = ROOT / ".github" / "workflows" / "validate.yml"
    validation.require(workflow.is_file(), "Missing validation workflow")
    if not workflow.is_file():
        return
    text = workflow.read_text(encoding="utf-8")
    validation.require("permissions:\n  contents: read" in text, "Workflow must use read-only repository permissions")
    action_pattern = re.compile(r"uses:\s+[^\s@]+@([^\s#]+)")
    pins = action_pattern.findall(text)
    validation.require(bool(pins), "Workflow must contain pinned actions")
    for pin in pins:
        validation.require(bool(re.fullmatch(r"[0-9a-f]{40}", pin)), f"Workflow action is not pinned to a commit SHA: {pin}")


def main() -> int:
    validation = Validation()
    validate_skill(validation)
    validate_legal_baseline(validation)
    validate_plugin(validation)
    validate_marketplace(validation)
    validate_openai_yaml(validation)
    validate_evals(validation)
    validate_repository_hygiene(validation)
    validate_local_markdown_links(validation)
    validate_workflow_pins(validation)

    if validation.failures:
        for failure in validation.failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print("Validation passed: plugin, skill, legal regimes, metadata, evaluations, and repository hygiene.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
