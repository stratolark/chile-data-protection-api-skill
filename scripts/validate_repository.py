#!/usr/bin/env python3
"""Validate the public plugin repository without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "chile-data-protection-api"
SKILL_ROOT = PLUGIN_ROOT / "skills" / "chile-data-protection-api"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
LEGAL_REFERENCE = SKILL_ROOT / "references" / "legal-baseline.md"
OPENAI_YAML = SKILL_ROOT / "agents" / "openai.yaml"
PLUGIN_JSON = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_JSON = ROOT / ".agents" / "plugins" / "marketplace.json"
VALIDATION_WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"
RELEASE_WORKFLOW = ROOT / ".github" / "workflows" / "release.yml"

EXPECTED_SKILL_NAME = "chile-data-protection-api"
EXPECTED_MARKETPLACE_NAME = "chile-data-protection"
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".py", ".txt"}


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


def repository_text_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and path.suffix.lower() in TEXT_SUFFIXES
    ]


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

    linked_references = set(re.findall(r"references/[A-Za-z0-9_./-]+\.md", text))
    available_references = {
        path.relative_to(SKILL_ROOT).as_posix()
        for path in (SKILL_ROOT / "references").rglob("*.md")
    }
    validation.require(
        linked_references == available_references,
        f"SKILL.md reference links do not match packaged references: linked={sorted(linked_references)}, available={sorted(available_references)}",
    )


def validate_legal_reference(validation: Validation) -> None:
    validation.require(LEGAL_REFERENCE.is_file(), "Missing legal baseline")
    if not LEGAL_REFERENCE.is_file():
        return

    text = LEGAL_REFERENCE.read_text(encoding="utf-8")
    verified_match = re.search(r"(?m)^Last verified:\s*(\d{4}-\d{2}-\d{2})\.$", text)
    validation.require(verified_match is not None, "Legal baseline needs an ISO verification date")
    if verified_match is not None:
        try:
            date.fromisoformat(verified_match.group(1))
        except ValueError:
            validation.failures.append("Legal baseline verification date is invalid")

    official_urls = set(re.findall(r"https://www\.bcn\.cl/leychile/[^\s)]+", text))
    validation.require(len(official_urls) >= 2, "Legal baseline needs current and amended official BCN sources")


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
        required_fields = ("displayName", "shortDescription", "longDescription", "developerName", "category", "defaultPrompt")
        for field in required_fields:
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
    required_keys = ("display_name", "short_description", "default_prompt", "allow_implicit_invocation")
    for key in required_keys:
        validation.require(re.search(rf"(?m)^\s*{key}:\s*\S", text) is not None, f"agents/openai.yaml is missing {key}")
    validation.require(f"${EXPECTED_SKILL_NAME}" in text, "Default prompt must mention the skill explicitly")


def validate_repository_hygiene(validation: Validation) -> None:
    secret_patterns = {
        "unfinished placeholder": re.compile(r"\[(?:TODO|FIXME|TBD)(?::|\])", re.IGNORECASE),
        "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        "GitHub token": re.compile(r"\bgh[opurs]_[A-Za-z0-9]{20,}\b"),
        "OpenAI key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    }

    legacy_postures = (
        "LEGAL" + "_BASELINE",
        "STRICT" + "_ENGINEERING_DEFAULT",
        "TAILORED" + "_CONTROL_SET",
    )
    forbidden_terms = {
        "numbered legal placeholder": re.compile(r"\b(?:LEGAL|GATE)-\d{3}\b"),
        "legal-input marker": re.compile(r"\b" + "LEGAL" + "_INPUT_REQUIRED" + r"\b"),
        "law-gap marker": re.compile(r"\b" + "LAW" + "_GAP" + r"\b"),
        "strict-gap marker": re.compile(r"\b" + "STRICT" + "_DEFAULT_GAP" + r"\b"),
        "enum-style posture": re.compile(r"\b(?:" + "|".join(map(re.escape, legacy_postures)) + r")\b"),
        "named third posture": re.compile(r"\b" + "Tailored" + r"\s+" + "controls" + r"\b", re.IGNORECASE),
    }
    forbidden_artifacts = {
        "/".join(("docs", "privacy", "data-processing-inventory.md")),
        "/".join(("docs", "privacy", "privacy-implementation-decisions.md")),
        "/".join(("docs", "privacy", "privacy-gap-report.md")),
    }

    for path in repository_text_files():
        text = path.read_text(encoding="utf-8")
        relative_path = path.relative_to(ROOT)
        for label, pattern in secret_patterns.items():
            validation.require(pattern.search(text) is None, f"Found {label} in {relative_path}")
        for label, pattern in forbidden_terms.items():
            validation.require(pattern.search(text) is None, f"Found {label} in {relative_path}")
        for artifact in forbidden_artifacts:
            validation.require(artifact not in text, f"Found generated privacy artifact recommendation in {relative_path}: {artifact}")


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
    validation.require(VALIDATION_WORKFLOW.is_file(), "Missing validation workflow")
    if not VALIDATION_WORKFLOW.is_file():
        return

    text = VALIDATION_WORKFLOW.read_text(encoding="utf-8")
    read_only_permissions = re.search(r"(?m)^permissions:\s*\n\s+contents:\s*read\s*$", text)
    validation.require(read_only_permissions is not None, "Validation workflow must use read-only repository permissions")
    pins = re.findall(r"uses:\s+[^\s@]+@([^\s#]+)", text)
    validation.require(bool(pins), "Validation workflow must contain pinned actions")
    for pin in pins:
        validation.require(bool(re.fullmatch(r"[0-9a-f]{40}", pin)), f"Workflow action is not pinned to a commit SHA: {pin}")


def validate_release_workflow(validation: Validation) -> None:
    validation.require(RELEASE_WORKFLOW.is_file(), "Missing release workflow")
    if not RELEASE_WORKFLOW.is_file():
        return

    text = RELEASE_WORKFLOW.read_text(encoding="utf-8")
    validation.require(re.search(r'(?m)^\s+-\s+"v\*"\s*$', text) is not None, "Release workflow must run for version tags")
    write_permissions = re.search(r"(?m)^permissions:\s*\n\s+contents:\s*write\s*$", text)
    validation.require(write_permissions is not None, "Release workflow must permit release creation")
    validation.require('--repo "$GITHUB_REPOSITORY"' in text, "Release workflow must select its repository without a checkout")


def main() -> int:
    validation = Validation()
    validate_skill(validation)
    validate_legal_reference(validation)
    validate_plugin(validation)
    validate_marketplace(validation)
    validate_openai_yaml(validation)
    validate_repository_hygiene(validation)
    validate_local_markdown_links(validation)
    validate_workflow_pins(validation)
    validate_release_workflow(validation)

    if validation.failures:
        for failure in validation.failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print("Validation passed: plugin, skill structure, sources, metadata, links, workflows, and repository hygiene.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
