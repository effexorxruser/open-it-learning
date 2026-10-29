# Catalog navigation architecture · v1

[← Catalog](../catalog/README.md) · [Browse by IT direction](../catalog/navigation/README.md) · [Editorial policy](CATALOG_POLICY.md)

This document defines the **navigation classification** of verified Open IT Learning records. It does **not** create new issuer statements, certification statuses, learning fees, geographic eligibility, or course prerequisites.

## Two separate types of information

1. **Source-backed course record** — the canonical `catalog/verified/{course-id}.json` file. Provider, outcomes, evidence, fees, languages and original `category` keywords remain in this record. This is the unique authoritative item for each verified course.
2. **Editorial navigation** — the standalone, versioned `catalog/navigation/` files. They answer where a record appears in the directory and which other records a learner could explore.

Keep this separation to avoid evidence drift, moving the same course JSON into multiple folders, or making it seem that course authors formally endorse our learning paths.

## Taxonomy model

```text
IT functional domain (domain.id)
└── Specialization (specialization.id)
    └── Verified course reference (placements.records[].course_id)
         ├── Exactly one primary_specialization
         └── Zero or more additional_specializations
```

The **primary** specialization determines counting and display priority. Additional placements are *cross-listings* for discovery and do **not** increase the distinct-course total. Counts in domain index pages should reflect **primary** courses only.

The first version covers six domains and fourteen specializations. `enterprise-it / erp-and-1c` exists with zero verified courses, and the unapproved Moscow `1С / Код будущего` research candidate is linked only as research, not indexed as a verified course.

**Important distinction:** the six domains are **IT job/practice fields**, not market-sector industries. A later, orthogonal industry-application facet could include retail, manufacturing, banking, healthcare, public sector and education, but only when descriptions support such a mapping. Do not infer that a general-purpose Python/SQL course is specific to one market sector simply because it can be used there.

## Machine-readable files

| Path | Purpose |
| --- | --- |
| [taxonomy.json](../catalog/navigation/taxonomy.json) | Version, domain IDs, specialization IDs, bilingual labels and descriptions |
| [placements.json](../catalog/navigation/placements.json) | One record per verified course ID; primary and secondary specializations |
| [learning-paths.json](../catalog/navigation/learning-paths.json) | Editorial ordered course ID sequences and localized descriptions |
| [relationships.json](../catalog/navigation/relationships.json) | Curated alternative/related links between existing course IDs |
| [Navigation README](../catalog/navigation/README.md) | Human-facing directory of domains, counts and routes |
| [Domain pages](../catalog/navigation/domains/) | Markdown pages grouped by the taxonomy |

**Stable IDs:** IDs are lower-case kebab-case. Renaming a domain or specialization is a breaking change for consumers, even if a label translation changes. Prefer adding or deprecating rather than silently changing IDs.

A `related` edge connects complementary subject areas; `alternative` suggests a choice of different approaches. Neither type means **issuer-declared prerequisite**, credit recognition, enrollment entitlement, or official program articulation.

## Editorial learning paths

Each path is an ordered list, not a directed credential dependency graph. The progression reflects the curator's view of knowledge sequencing and may be modified without changing course evidence. For genuine prerequisites, record a separate provider-cited assertion in a future schema extension; **do not infer formal requirements from path order**.

Learning paths can mix languages, providers and award types. Check each course's `languages`, `learning.conditions`, `outcomes[].requirements` and `review.recheck_after` before recommending a path to an individual.

## Adding a course or branch

1. Complete normal issuer/source review and merge the approved course into `catalog/verified/`.
2. Inspect its existing `category` keywords and choose **one primary specialization**, plus optional additional specializations. Add a new specialization to `taxonomy.json` only if existing ones do not fit.
3. Add exactly one mapping to `placements.json`. Never duplicate the official course JSON to create category pages.
4. Update the affected human-readable [domain page](../catalog/navigation/domains/) and navigation index/counters. Add a learning-path step or a relation **only when pedagogically useful**, without inventing prerequisites.
5. Update navigation links/README/Wiki if category names or structure change. Edit EN/RU labels first; expand UK/ZH-CN translations as maintained.
6. Run `python3 scripts/check_integrity.py` and `python3 -m unittest discover -s tests -v`. The CI contract tests enforce referential integrity and exact classification of every currently verified course.
7. Require a reviewed PR for structural changes; keep `main` and the GitHub Wiki publication as separate approval gates.

## Future facets — not invented today

- Topic/tag filters from the existing `category` field.
- Outcome type, language, difficulty, duration and separate fees from original records.
- Geographic and eligibility facets, but only where validated by each issuer.
- Specific market industries (independent of IT practice areas).
- Issuer-cited prerequisite relations with explicit evidence links and dates.
- Generated indexes and read-only JSON/MCP/website search, if the catalog volume justifies it.

**Quality rule:** navigation must never make an under-review candidate look verified or imply issuer promises that are absent from official course records.
