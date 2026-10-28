# Catalog inclusion policy

[← Home](../README.md) · [Course index](../catalog/README.md) · [Record schema](DATA_CONTRACT.md)

## What belongs in the verified index

**The core catalog is a collection of free IT courses for which an obtainable certificate is confirmed by official sources.**

Every published record must pass these checks:

1. **Official course identity:** the provider, course title and direct canonical URL resolve to the real course.
2. **Free learning access:** the course content is offered free of charge under the stated conditions. A trial, scholarship, paid plan, or time-limited promotion is not automatically "free."
3. **Certificate exists:** an official source explicitly confirms a certificate of completion or another *clearly identified certificate* obtainable for this course.
4. **Conditions are documented:** required coursework, assessment, eligibility and region restrictions are described, or any remaining ambiguity is clearly stated. A material unknown affecting eligibility blocks verified status.
5. **Credential price is known:** record free certificate, paid certificate/exam, or formally specified conditions. Never infer that credentials are free from free course access.
6. **Evidence is reviewable:** each material claim points to official sources, short excerpts or documented source locations, and a review date.
7. **Independent review:** automated excerpt matching is not enough. Reviewers verify that the source actually supports the meaning of the claim.

A digital badge is tracked **separately** and does not automatically qualify as a certificate. A professional certification is distinct from completing a beginner course.

## Publication decisions

| Decision | Conditions |
| --- | --- |
| **Verified · free certificate** | Free learning and obtainable **free certificate**, including stated conditions, are confirmed. |
| **Verified · paid certificate** | Free learning and obtainable certificate confirmed; certificate or exam carries a clearly disclosed fee. |
| **Under review** | One or more required claims are missing or ambiguous. **Not in the verified index.** |
| **Recheck required** | Old evidence, broken URL, provider policy change, or conflicting information. Temporarily withhold current claims until reviewed. |
| **Rejected** | Not free learning, no certificate, unofficial/imitation provider, or unverifiable course identity. |

## Evidence standards

- Prefer the **course's own official page**, then its provider's official credential policy.
- Store the *final* URL after redirects when relevant, with a stable course identifier.
- Record the retrieval date in UTC and the exact claim each source supports.
- Do not use a search engine snippet as the sole proof.
- Treat pricing as jurisdiction- and date-dependent where applicable.
- Distinguish a certificate of course completion, a verified credential and an industry certification exam.
- Do not paste lengthy copyrighted course materials into repository records.

## When the certificate is unknown

Do not add the course to `catalog/verified/`. You may document a short, dated research note under `journal/` if it teaches something about evidence quality. A note is **not a catalog listing**.

## Re-verification

Records must carry `reviewed_at` and may carry `recheck_after`. If a required claim becomes unavailable or contradictory, flag the record for review and avoid asserting it as current. A fixed global freshness period has not yet been chosen.

## Scope and independence

The public catalog can be maintained with manual verification, any browsing-capable assistant or other tools. Internal developer infrastructure, model providers and Harness² experiments are **not part of the reader's experience** and are not requirements for contributing.
