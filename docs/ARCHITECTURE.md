# Public repository structure

[← Home](../README.md) · [Catalog policy](CATALOG_POLICY.md) · [Roadmap](ROADMAP.md)

This repository is **a course library and a collection of reusable learning resources**. Readers can browse the catalog and use the text resources directly on GitHub.

## Directory map

```text
open-it-learning/
├── catalog/
│   ├── README.md          Verified-course index
│   ├── verified/          Approved, source-reviewed records
│   └── schema/            Data format and validation
├── prompts/               Ready-to-copy research and planning prompts
├── skills/                Portable course-verification skills
├── integrations/          Future public interfaces (MCP proposal, exports)
├── journal/               Optional research and curation field notes
├── docs/                  Editorial policy and user documentation
├── assets/                Minimal visual identity for README
├── scripts/               Offline repository-integrity checks
├── wiki-source/           Reviewed pages for the separate GitHub Wiki
└── .github/               Contribution templates, PR checks and Wiki publishing
```

The design optimizes for plain GitHub browsing first: records and methods should be readable without installing an application.

## Course publication flow

```mermaid
flowchart LR
  A["Official source"] --> B["Candidate + evidence"]
  B --> C["Independent review"]
  C --> D{"Official outcome verified?"}
  D -->|"Yes"| E["catalog/verified"]
  D -->|"No"| F["Keep out of verified index"]
  E --> G["Paths / exports / future MCP"]
```

The publication gate concerns **official outcome availability, costs and conditions**, not whether a browser could load a page.

## Record boundaries

A public record may contain provider, course and official outcome data; official evidence URLs; short supporting excerpts; and review dates. It must not contain local browser traces, API keys, account identifiers, authentication cookies, or private experimental data.

The difference between course and credential cost must remain explicit. A badge or achievement icon is not automatically a certificate.

## Ready-to-use tools

Prompts and skills are versioned text files. They can be copied into compatible assistants, reviewed, modified and reused independently of the catalog. An MCP interface is only a proposal until implemented.

See the [catalog inclusion policy](CATALOG_POLICY.md) for the publication requirements.
