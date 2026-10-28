# Course record format

[← Home](../README.md) · [Catalog policy](CATALOG_POLICY.md) · [Catalog](../catalog/README.md)

> Draft contract for **public verified course records**. The first release of the catalog is not yet populated.

## What a record must prove

A verified record establishes that (1) the course itself is real and has a direct official link, (2) learning content is free under stated conditions, and (3) **this course offers an obtainable certificate**, with documented requirements and price.

A digital badge alone is insufficient for certificate verification.

## Proposed structure

```json
{
  "id": "provider-course-slug",
  "title": "Official course title",
  "provider": "Official provider name",
  "official_url": "https://provider.example/course",
  "category": ["cybersecurity"],
  "level": null,
  "languages": [],
  "duration_hours": null,
  "learning": {
    "free": true,
    "conditions": "Confirmed free enrollment or access conditions",
    "cost": 0,
    "currency": "USD"
  },
  "certificate": {
    "available": true,
    "type": "completion_certificate",
    "requirements": "Officially documented completion/assessment conditions",
    "cost": 0,
    "currency": "USD",
    "official_evidence_url": "https://provider.example/certificate-policy"
  },
  "badges": [],
  "evidence": [
    {
      "claim": "certificate.available",
      "source_url": "https://provider.example/certificate-policy",
      "short_quote": "Short excerpt from the official source",
      "checked_at": "2026-10-28T00:00:00Z",
      "review_note": "How the excerpt establishes the claim"
    }
  ],
  "review": {
    "status": "verified_free_certificate",
    "reviewed_at": "2026-10-28T00:00:00Z",
    "recheck_after": null
  }
}
```

**All values and links above are illustrative placeholders.** This is not a real verified course. Never copy a fabricated example into `catalog/verified` as data.

## Required evidence

A record must cite official sources for:
- Course identity and free learning access.
- Certificate issuance, specific eligibility requirements and price.
- Any claimed expiry dates, regional restrictions and credential validity.

Additional claims such as duration, badge, level, languages and prerequisites should also cite primary sources when filled. Keep evidence excerpts short and preserve dates.

## Allowed review statuses

- `verified_free_certificate`: free course and free obtainable certificate verified.
- `verified_paid_certificate`: free course and paid obtainable certificate verified, fee disclosed.
- `under_review`: proof incomplete; not allowed in the verified directory.
- `recheck_required`: published claim needs fresh verification; do not assert current status until reviewed.
- `rejected`: outside the catalog's inclusion rules.

## Quality rules

The stored review decision is not an AI-model confidence score. Quote matching and URL reachability alone are not enough; a human or independent review must validate the claim's meaning. The exact JSON Schema will be versioned and checked before bulk records are accepted.

No tracking cookies, credentials, personal records or large copyrighted source dumps should appear in public records.
