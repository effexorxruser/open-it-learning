# Course record format

[← Home](../README.md) · [Catalog policy](CATALOG_POLICY.md) · [Course catalog](../catalog/README.md)

> **Draft** public catalog record. Schema: [course.schema.json](../catalog/schema/course.schema.json). This structure describes free IT courses and their **official outcomes**, not just certificates.

## Model

One course can offer multiple different outcomes: a completion certificate, a badge, a provider-issued diploma, an award, a participation record or an exam voucher.

Do **not** merge them into an ambiguous `certificate` field. Each official outcome has its **own type, issuer, requirements, price and evidence**.

```json
{
  "id": "illustrative-provider-course",
  "title": "Illustrative IT course",
  "provider": "Example Provider",
  "official_url": "https://example.org/courses/example",
  "category": ["networking"],
  "level": "beginner",
  "languages": ["en"],
  "duration_hours": null,
  "learning": {
    "free": true,
    "conditions": "Free learning access; subject to registration",
    "cost": 0,
    "currency": "USD"
  },
  "outcomes": [
    {
      "kind": "recognition",
      "type": "digital_badge",
      "name": "Illustrative course badge",
      "issuer": "Example Provider",
      "obtainable": true,
      "requirements": "Complete every course module and required assessment",
      "cost_to_obtain": 0,
      "currency": "USD",
      "official_evidence_url": "https://example.org/courses/example/badges",
      "individual_verification_url": null
    }
  ],
  "evidence": [
    {
      "claim": "learning.free",
      "source_url": "https://example.org/courses/example",
      "short_quote": "Example text from an official course page",
      "checked_at": "2026-10-28T00:00:00Z",
      "review_note": "Supports free access under the stated conditions"
    },
    {
      "claim": "outcomes[0].obtainable",
      "source_url": "https://example.org/courses/example/badges",
      "short_quote": "Example text confirming badge availability",
      "checked_at": "2026-10-28T00:00:00Z",
      "review_note": "Explains how the specific badge is earned"
    },
    {
      "claim": "outcomes[0].cost_to_obtain",
      "source_url": "https://example.org/courses/example/badges",
      "short_quote": "Example wording for no badge issuance fee",
      "checked_at": "2026-10-28T00:00:00Z",
      "review_note": "Supports the recorded free badge issuance cost"
    }
  ],
  "review": {
    "status": "verified_free_outcome",
    "reviewed_at": "2026-10-28T00:00:00Z",
    "recheck_after": null
  }
}
```

**Every example name, URL and evidence excerpt above is fictional and must never be imported into the catalog.**

## Key fields

- `learning.free`: required and true for the verified catalog.
- `outcomes`: one or more confirmed outcomes, each typed as **recognition** or **benefit**.
- `outcomes[].type`: exact category such as `digital_badge`, `diploma`, `award`, `exam_voucher`.
- `outcomes[].cost_to_obtain`: a numeric amount **only when official evidence supports it**; unknown costs prevent verification.
- `outcomes[].individual_verification_url`: optional online credential lookup or verification link; null if not offered. Do not equate this with official issuance proof.
- `evidence`: dated official sources supporting specific material fields, including outcome requirements and costs.
- `review.status`: `verified_free_outcome` or `verified_paid_outcome` in published records. Candidates with missing information stay outside `catalog/verified/`.

## Zero cost and currency

Use `cost: 0` or `cost_to_obtain: 0` only with official evidence of a free offering. For an explicitly zero amount with no currency stated by the issuer, use `currency: null`. This means **no currency denomination was supplied**, not an unknown price. Never assign an arbitrary currency to a free result.

A positive outcome cost still requires a three-letter uppercase currency code. Existing records with `0` and a currency string remain valid for compatibility. Unknown prices remain in research candidates, outside the verified index; a null price is not accepted by the publication schema.

## Admission and semantic checks

Schema validation ensures structural consistency; it does not establish whether sources are trustworthy or claims are true. A human or independent review must confirm that cited evidence means what the record says.

For credits, diplomas, exam discounts and access perks, describe exactly what the issuer promises. **No implication of academic accreditation, professional licensure or exam passing** without explicit supporting evidence.

**CPD points:** If an issuer explicitly awards continuing professional development points on successful course completion, they may be represented as `type: training_credit` with `kind: benefit`. State their exact point count, issuer and conditions, and link the evidence. When CPD proof is included on a free Statement of Participation, do not imply a separate certificate, academic transfer credit, professional license, or paid redeemable voucher. Keep the participation statement and CPD benefit as separate typed outcomes only when both are documented.

## Versioning

The current schema is preliminary and may change before the first verified catalog release. Do not include credentials, cookies, secret tokens or copyrighted course dumps in public records.
