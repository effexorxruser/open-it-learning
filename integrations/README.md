# Integrations — proposals, not shipped software

[← Home](../README.md)

The public course library should remain useful as plain files and GitHub pages. Integrations are **optional** convenience layers, not dependencies on any maintainer's private development setup.

## Potential MCP interface

A future read-only Model Context Protocol integration could expose verified catalog data to compatible assistants:

| Proposed tool | Purpose |
| --- | --- |
| `search_courses` | Search published, reviewed course records by skill, provider, region and credential type |
| `get_course` | Read a course, its credential details and source references |
| `find_learning_path` | Find candidate sequences based on prerequisites, without inventing missing edges |
| `check_evidence` | Retrieve the documented source evidence and review timestamp for a claim |

**No MCP server is implemented in this repository.** Tool names and contracts may change. When implemented, it should be read-only by default, versioned, rate-limited, and source-aware.

## Other possible interfaces

- Downloadable JSON / CSV catalog exports.
- A static website for filtering verified courses.
- Editor plugins or chat-assistant skills using public records.
- Community-submitted corrections through GitHub Issues.

The goal is to make the **course database and learning materials easy to use**, not to publish or require the internal scraping and agent-development stack.
