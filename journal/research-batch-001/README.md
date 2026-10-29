# Research Batch #001 — source-checked proposals

[← Journal](../README.md) · [Record format](../../docs/DATA_CONTRACT.md) · [Proposals and evidence](proposals.json) · [Doublecheck pass](doublecheck.md)

**Ten source-checked proposals have undergone a separate AI-assisted official-source review. Each now has a corresponding structured record staged in `catalog/verified/` on Draft PR #4, pending maintainer approval for merge into `main`.** Each record body contains dated, claim-level official evidence. The original research bundle intentionally has **no** `review` object. The ten **staged catalog copies** carry genuine source-review timestamps and a 90-day recheck date; tests verify each staged copy exactly matches the underlying proposal apart from review metadata. No human completion test or maintainer approval is implied.

## Results

| Proposal | Official outcome researched | Material conditions |
| --- | --- | --- |
| [CS50x](https://cs50.harvard.edu/x/) | Free CS50 Certificate | At least 70% on required problem sets and final project |
| [CS50 Python](https://cs50.harvard.edu/python/) | Free CS50 Certificate | At least 70% on required problems and final project |
| [CS50 AI](https://cs50.harvard.edu/ai/) | Free CS50 Certificate | At least 70% on each required project |
| [CS50 SQL](https://cs50.harvard.edu/sql/) | Free CS50 Certificate | At least 70% on required problems and final project |
| [CS50 Cybersecurity](https://cs50.harvard.edu/cybersecurity/) | Free CS50 Certificate | At least 70% on required problems and final project |
| [CS50 Web](https://cs50.harvard.edu/web/) | Free CS50 Certificate | At least 70% on each project, including final project |
| [OpenLearn cyber security](https://www.open.edu/openlearn/digital-computing/introduction-cyber-security-stay-safe-online/content-section-overview) | Free participation record, OU digital badge and 24 CPD points | Enrol and complete all material; badge needs ≥50% in both Week 4 and Week 8 quizzes. Whole failed badge quiz retry after 24h |
| [Introducing computing and IT](https://www.open.edu/openlearn/digital-computing/introducing-computing-and-it/content-section-0) | Free participation record | Account, enrolment, all pages and applicable quizzes |
| [Digital skills](https://www.open.edu/openlearn/digital-computing/digital-skills-succeeding-digital-world/content-section-overview) | Free participation record, OU digital badge and 24 CPD points | Enrol and complete all material; badge needs ≥50% in both Week 4 and Week 8 quizzes. Whole failed badge quiz retry after 24h |
| [freeCodeCamp Python v9](https://www.freecodecamp.org/learn/python-v9/) | Free issuer certification | Projects, exam and staff moderation; see record for exam restrictions |

CS50's free certificate is distinct from paid edX verification or academic credit. Its current FAQs require edX registration and the CS50 Gradebook, with GitHub sign-in for redemption. All six FAQs currently state a **course submission deadline of 30 June 2027 at 23:59 UTC**. The issuer also advises downloading the free certificate before the deadline; this is **not** a claim that an already issued certificate expires on that date. Recheck before enrolment or redemption. Course-specific requirements and evidence are in the JSON, not inferred from another CS50 course.

## Repeated preflight and exclusions

- OpenLearn's official course pages and course-specific badge guides support **free badges for the cyber security and Digital skills courses**, in addition to their free participation records. Each requires reading eight weeks and ≥50% in **both** Week 4 and Week 8 badge quizzes; failing a whole badge quiz allows a new attempt **after 24 hours**, repeatedly if needed. Per-question attempt limits and decreasing points still apply. These badges are not OU academic degrees.
- Both courses also offer **24 CPD points** on successful completion, evidenced **on the free Statement of Participation**. The JSON represents these as `training_credit`/`benefit`, not as separately issued qualifications, transferable academic credit, or an independently purchased credential. No CPD points are inferred for Introducing computing and IT.
- OpenLearn browser retrieval met a Cloudflare challenge in the original run; ordinary provider-page reading supplied evidence without bypassing that challenge.
- Cisco Introduction to Cybersecurity still shows free learning, but specific outcome conditions and issuance fees remain unestablished. It is excluded from the ten proposals.
- freeCodeCamp's legacy Scientific Computing with Python is not substituted for its current Python v9 certification. The v9 learning page was opened in Playwright and checked against its course-specific issuer announcement.
- The existing verified Responsive Web Design v9 record was excluded as an already published course and remains unchanged.

## Method and publication gate

Discovery used the permitted built-in search and the official CS50 catalog. Search excerpts were not used as evidence. Actual provider pages were read separately; Playwright confirmed CS50 certificate/FAQ pages, Cisco's course and current freeCodeCamp Python. A working replacement search path was sufficient to proceed; availability of any particular search MCP was not an admission criterion.

The [evidence journal](proposals.json) stores short excerpts, URLs, UTC review times and interpretation. There are **63 dated evidence entries covering 54 course-specific claim paths across ten proposed records and 14 outcome entries**. The 29 October editorial follow-up independently re-opened the issuer's primary pages and documented the findings in [editorial review](editorial-review-2026-10-29.md). These are source-check results, not completion or actual award-issuance tests. No registration, enrolment, exam or payment was performed. No universal geographic eligibility, employment guarantee or academic accreditation is claimed.

Explicitly free amounts are represented by `0` and `currency: null` when the issuer states no currency. This does not turn unknown prices into zero. Existing currency strings remain valid; positive costs still require a currency. Tests cover these boundaries and ensure unreviewed proposals are not accepted as publication records.

The separate source review found no disqualifying course-level contradiction, but **this is not an enrollment or credential issuance test**. Ten source-reviewed records have been prepared as individual JSON files on the **Draft PR branch only**. **Maintainer approval for merge remains required**; there is no automatic publication to `main` or Wiki. The staged review timestamps document the actual independent AI-assisted source check and are not presented as a human award-delivery audit.
