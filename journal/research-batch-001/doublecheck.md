# Doublecheck — Batch #001

## Summary

One-shot claim extraction, primary-source checking and adversarial review using the installed Doublecheck skill. The same Codex performed both research and this second pass. **This is not independent model review or independent catalog approval.** The final 63 evidence entries cover 54 distinct course-scoped material claim paths; these counts describe coverage, not measured factual accuracy.

## Flagged items and corrections

| Issue examined | Finding | Result |
| --- | --- | --- |
| Free CS50 versus paid edX verification | The issuer distinguishes the routes | Only the free CS50 outcome is proposed; no professional or academic-credit claim |
| CS50 completion threshold | 70% applies to each required assignment, not 70% of the syllabus | Course-specific problem/project requirements retained |
| Registration and deadline | Each FAQ requires edX registration; current deadline is 30 June 2027 | Gradebook, redemption and deadline conditions retained |
| OpenLearn badge versus participation | Separate conditions and outcome types | Cyber security and Digital skills each have participation + badge outcomes; no accredited-degree implication |
| OpenLearn quiz retries | Later correct answers can earn fewer points; a whole failed badge quiz may be re-attempted after 24 hours | Both course-specific retake rules and per-question limits retained |
| Legacy versus current freeCodeCamp Python | Different curricula and claiming paths | Current Python v9 only; existing RWD v9 deduplicated |
| Zero price without a stated currency | Inventing USD would add an unsupported fact | Explicit zero with null currency; unknown price remains invalid |
| Same-agent review versus publication approval | No independent approval was obtained | No saved `review` metadata; verified catalog unchanged |

## Source verification

For each proposal, `evidence` in [proposals.json](proposals.json) links the exact official course, certificate, FAQ or announcement supporting its learning cost and official outcome. Course-specific CS50 certificate pages and FAQs were opened in Playwright. OpenLearn pages were read through the ordinary official-page reader after a browser challenge; the current freeCodeCamp course was opened in Playwright and its issuer announcement read separately. No search snippet was promoted to proof.

The learning/free-outcome claims in these proposals have supporting issuer sources. A separate [editorial source review](editorial-review-2026-10-29.md) confirmed the two OpenLearn badged-course requirements and the 24 CPD points reflected on free participation statements. CPD is classified as non-academic `training_credit` (a course-linked benefit); the issuer does not represent it as a separate OU degree or award document. Cisco award issuance remains **UNVERIFIED** and is excluded. Claims that the free CS50 certificate equals a paid verified edX certificate, or that the legacy freeCodeCamp curriculum is the current Python v9 path, are **DISPUTED** by the respective issuer pages and are not present in the proposals.

## Internal consistency

Record identities and URLs are distinct and do not duplicate the existing verified course. This batch includes 14 source-backed result entries across 10 proposed courses. Free-learning, free-outcome and requirement claims are separately evidenced. The missing `review` object is intentional, not a claim that editorial approval has happened.

## What was not checked

Actual account eligibility, enrolment, assignment submission, exam completion, award delivery and recipient-specific verification URLs. The page reader can return indexed content; its read timestamp is not a guarantee that every upstream fact changed at that instant. Additional benefits not represented in a proposal have not been approved. A human reviewer must consider these limits before publication.

## Limitations

- This accelerates human verification; it does not replace it.
- Search may omit recent or access-restricted sources.
- The adversarial pass uses the same model and may repeat its mistakes.
- Supporting sources can themselves be wrong or change later.
- Missing contradictory evidence is not proof of correctness.
