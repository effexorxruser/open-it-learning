# Integrations — future proposals

[← Home](../README.md) · [Catalog](../catalog/README.md)

The core public product is a **browseable collection of free IT courses and their issuer-confirmed outcomes**, plus prompts and skills. Integrations should be optional and should use the **published catalog**, not require the maintainer's private infrastructure.

## Potential MCP interface

A future read-only Model Context Protocol tool might expose:

| Proposed tool | Purpose |
| --- | --- |
| `search_courses` | Search reviewed free courses by skill, provider, language, or result type: badge, certificate, diploma, award, voucher and more |
| `get_course` | Retrieve the course and separately typed official results and benefit details |
| `get_outcome_evidence` | Retrieve dated official-source evidence for a particular reward or eligibility claim |
| `find_learning_path` | Suggest a sequence of published courses by goal and prerequisites, without inventing missing rewards |

**No MCP server is implemented here yet.** These names are interface ideas, not commands users can execute today.

## Other possible features

- JSON and CSV exports of reviewed records.
- Static browsing and filtering by skill and outcome type.
- Editor integrations and portable assistant skills.
- Github Issues-based suggestions and corrections.

The catalog must remain readable without installing a server or logging into a paid model provider.
