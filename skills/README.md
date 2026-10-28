# Agent skills

[← Home](../README.md) · [Prompts](../prompts/README.md)

Small, readable workflow instructions that can be adapted for assistants supporting reusable skills.

| Skill | Purpose |
| --- | --- |
| [Course Verifier](course-verifier/SKILL.md) | Examine official sources, check certificate conditions and return a structured admission decision. |

These files do not require Harness², ComfyUI, Codex, Claude Code or a particular provider. They describe **what an agent should verify**, not credentials or infrastructure to run.

Adapt the skill to your tool permissions; browser access is needed for fresh verification. No network access means **no new verified claim**. Always review generated results before publishing.

Submit proposed skills using the [contribution guidelines](../CONTRIBUTING.md).
