# Research Batch #001 — source-checked proposals

[← Journal](../README.md) · [Record format](../../docs/DATA_CONTRACT.md) · [Proposals and evidence](proposals.json) · [Doublecheck pass](doublecheck.md)

**Ten new course proposals are ready for independent editorial review. They are not additions to the verified catalog.** Each record body contains dated, claim-level official evidence. The `review` object is intentionally absent: it must be supplied only after the required independent review. Tests validate record fields using an in-memory publication projection, without manufacturing an approval in the saved data.

## Results

| Proposal | Official outcome researched | Material conditions |
| --- | --- | --- |
| [CS50x](https://cs50.harvard.edu/x/) | Free CS50 Certificate | At least 70% on required problem sets and final project |
| [CS50 Python](https://cs50.harvard.edu/python/) | Free CS50 Certificate | At least 70% on required problems and final project |
| [CS50 AI](https://cs50.harvard.edu/ai/) | Free CS50 Certificate | At least 70% on each required project |
| [CS50 SQL](https://cs50.harvard.edu/sql/) | Free CS50 Certificate | At least 70% on required problems and final project |
| [CS50 Cybersecurity](https://cs50.harvard.edu/cybersecurity/) | Free CS50 Certificate | At least 70% on required problems and final project |
| [CS50 Web](https://cs50.harvard.edu/web/) | Free CS50 Certificate | At least 70% on each project, including final project |
| [OpenLearn cyber security](https://www.open.edu/openlearn/digital-computing/introduction-cyber-security-stay-safe-online/content-section-overview) | Participation record and free OU digital badge | Enrolment and completion; badge additionally requires reading every week and at least 50% in both Week 4 and Week 8 badge quizzes |
| [Introducing computing and IT](https://www.open.edu/openlearn/digital-computing/introducing-computing-and-it/content-section-0) | Free participation record | Account, enrolment, all pages and applicable quizzes |
| [Digital skills](https://www.open.edu/openlearn/digital-computing/digital-skills-succeeding-digital-world/content-section-overview) | Free participation record | Same issuer participation rules; additional badge/CPD benefits are outside this proposal |
| [freeCodeCamp Python v9](https://www.freecodecamp.org/learn/python-v9/) | Free issuer certification | Projects, exam and staff moderation; see record for exam restrictions |

CS50's free certificate is distinct from paid edX verification or academic credit. Its current FAQs require edX registration and the CS50 Gradebook, with GitHub sign-in for redemption. All six FAQs currently state a deadline of **30 June 2027**; recheck before enrolment or redemption. Course-specific requirements and evidence are in the JSON, not inferred from another CS50 course.

## Repeated preflight and exclusions

- OpenLearn's official course page and specific badge instructions support no-fee badge issuance. The badge is not an OU academic qualification. Attempt limits and score deductions matter; eventually answering every question correctly need not produce a passing score. Browser retrieval met a Cloudflare challenge; ordinary provider-page reading supplied evidence without bypassing that challenge.
- Cisco Introduction to Cybersecurity still shows free learning, but specific outcome conditions and issuance fees remain unestablished. It is excluded from the ten proposals.
- freeCodeCamp's legacy Scientific Computing with Python is not substituted for its current Python v9 certification. The v9 learning page was opened in Playwright and checked against its course-specific issuer announcement.
- The existing verified Responsive Web Design v9 record was excluded as an already published course and remains unchanged.

## Method and publication gate

Discovery used the permitted built-in search and the official CS50 catalog. Search excerpts were not used as evidence. Actual provider pages were read separately; Playwright confirmed CS50 certificate/FAQ pages, Cisco's course and current freeCodeCamp Python. A working replacement search path was sufficient to proceed; availability of any particular search MCP was not an admission criterion.

The [evidence journal](proposals.json) stores short excerpts, URLs, UTC review times and interpretation. There are 52 evidence entries covering 45 distinct claim paths across ten records. These are source-check results, not completion or actual award-issuance tests. No registration, enrolment, exam or payment was performed. No universal geographic eligibility, employment guarantee or academic accreditation is claimed.

Explicitly free amounts are represented by `0` and `currency: null` when the issuer states no currency. This does not turn unknown prices into zero. Existing currency strings remain valid; positive costs still require a currency. Tests cover these boundaries and ensure unreviewed proposals are not accepted as publication records.

Before copying a proposal into `catalog/verified/`, an independent reviewer must recheck the primary sources, approve the exact record and supply real review metadata. No automatic promotion, merge or Wiki publication is part of this batch.
