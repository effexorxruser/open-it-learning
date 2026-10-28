# Course data contract

> **Draft schema / proposal.** No production dataset is published yet.

[← Overview](../README.md) · [Architecture](ARCHITECTURE.md)

## Design requirements

A course is not the same as an assertion about a course. Each substantive claim has a value, an evidence set and a verification state. A valid URL is necessary but does not prove that a certificate is free.

A minimal conceptual record:

```json
{
  "id": null,
  "provider": {
    "name": null,
    "official_url": null
  },
  "course": {
    "title": null,
    "canonical_url": null,
    "language_codes": [],
    "duration_hours": null,
    "level": null
  },
  "access": {
    "learning_price": null,
    "currency": null,
    "conditions": null
  },
  "credentials": {
    "type": null,
    "available": null,
    "price": null,
    "requirements": null
  },
  "skills": [],
  "claims": [],
  "verification": {
    "status": "unverified",
    "checked_at": null
  }
}
```

This is a **field example**, not a completed course record or a versioned JSON Schema.

## Claim-level evidence

```json
{
  "field": "access.learning_price",
  "value": null,
  "status": "unverified",
  "evidence": [
    {
      "source_url": null,
      "retrieved_at": null,
      "excerpt": null,
      "location": null
    }
  ],
  "review_note": null
}
```

A quote match verifies that a quoted string appeared in a captured source; it does **not** by itself establish that the quote semantically supports the claim.

## Verification states

| State | Meaning | Publication behavior |
| --- | --- | --- |
| `verified` | Source and claim have passed the required checks | Eligible for catalog publication |
| `unverified` | Insufficient or incomplete supporting evidence | Staging only |
| `conflicting` | Official sources or statements materially disagree | Staging and manual review |
| `stale` | Evidence is older than the applicable freshness policy | Recheck before asserting current status |
| `unavailable` | Source cannot currently be inspected | Preserve history, do not infer current facts |

Status is **per claim** where possible. A course record may contain verified title and URL while credential price remains unverified.

## Credential vocabulary

Do not collapse these categories:
- **Course completion**: completion or participation, possibly without a credential.
- **Digital badge**: a badge awarded under stated conditions.
- **Course certificate**: a certificate granted for a course or assessment.
- **Professional certification**: a separate credential, often exam-based, with its own pricing and validity.

`learning_price`, `exam_price` and `credential_price` must be independent fields in the eventually implemented schema.

## Identity and provenance

Canonical identifiers, redirect resolution, provider mergers, renamed programs and duplicate courses need explicit policies. Evidence should retain the source URL, retrieval time, and, where permitted, a bounded source excerpt or content fingerprint.

Keep raw captures, intermediate candidate records, and published records separate. Never silently upgrade an unverified candidate to a verified catalog entry.

## What needs validation before implementation

- Stable identifiers and deduplication policy.
- Skill taxonomy and relationship semantics.
- Localization, currencies and partial discounts.
- Claim freshness thresholds and recheck schedules.
- Source quoting limits and retention policy.
- JSON Schema versioning and migration rules.

Feedback is welcome via [contributions](../CONTRIBUTING.md).
