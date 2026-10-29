# Independent source review — Research Batch #001

**Review date:** 2026-10-29 (UTC)  
**Reviewing method:** separate ChatGPT assistant/tool session inspecting the complete Draft PR #4 record bundle and official public issuer pages; **not** the originating Codex or its same-agent Doublecheck pass  
**Decision:** course-level claims corroborated; editorial corrections completed; **awaiting maintainer publication approval**

> A separate AI-assisted source review is not proof of enrolment, exam submission, account eligibility or actual reward delivery. No course has been taken and no award has been issued to a test account. The human maintainer retains final approval of publication.

## Record-by-record evidence decision

| Proposed ID | Authoritative course-specific proof | Source-review result |
| --- | --- | --- |
| `cs50-x` | [CS50x certificate](https://cs50.harvard.edu/x/certificate/) · [CS50x FAQ](https://cs50.harvard.edu/x/faqs/) | Free CS50 Certificate with ≥70% on each required problem set and final project; enrollment and deadline documented |
| `cs50-python` | [CS50 Python certificate](https://cs50.harvard.edu/python/certificate/) · [FAQ](https://cs50.harvard.edu/python/faqs/) | Free CS50 Certificate after required problems and project |
| `cs50-ai` | [CS50 AI certificate](https://cs50.harvard.edu/ai/certificate/) · [FAQ](https://cs50.harvard.edu/ai/faqs/) | Free CS50 Certificate after passing each required project; prerequisites reported |
| `cs50-sql` | [CS50 SQL certificate](https://cs50.harvard.edu/sql/certificate/) · [FAQ](https://cs50.harvard.edu/sql/faqs/) | Free CS50 Certificate after required problems and final project |
| `cs50-cybersecurity` | [CS50 Cybersecurity certificate](https://cs50.harvard.edu/cybersecurity/certificate/) · [FAQ](https://cs50.harvard.edu/cybersecurity/faqs/) | Free CS50 Certificate after required problems and final project |
| `cs50-web` | [CS50 Web certificate](https://cs50.harvard.edu/web/certificate/) · [FAQ](https://cs50.harvard.edu/web/faqs/) | Free CS50 Certificate after project-based graded completion; prerequisites reported |
| `openlearn-cyber-security` | [OpenLearn course](https://www.open.edu/openlearn/digital-computing/introduction-cyber-security-stay-safe-online/content-section-overview) · [course-specific badge rules](https://www.open.edu/openlearn/mod/oucontent/view.php?id=50885&section=1.2) | Free participation statement, free badge, and 24 CPD points documented separately |
| `openlearn-introducing-computing` | [OpenLearn course](https://www.open.edu/openlearn/digital-computing/introducing-computing-and-it/content-section-0) · [issuer FAQ](https://www.open.edu/openlearn/about-openlearn/frequently-asked-questions-on-openlearn) | Free participation statement; no additional badge or CPD award inferred |
| `openlearn-digital-skills` | [OpenLearn course](https://www.open.edu/openlearn/digital-computing/digital-skills-succeeding-digital-world/content-section-overview) · [course-specific badge rules](https://www.open.edu/openlearn/mod/oucontent/view.php?id=108797&section=_unit1.1.2) | Free participation statement, free badge and 24 CPD points documented separately |
| `freecodecamp-python-v9` | [freeCodeCamp Python v9 announcement](https://www.freecodecamp.org/news/freecodecamps-new-python-certification-is-now-live) · [current learning path](https://www.freecodecamp.org/learn/python-v9/) | Free platform certification follows five projects, a separate exam, and manual moderation; not the retired legacy curriculum |

## Important distinctions resolved

### CS50

The six CS50 records refer only to the **free CS50-issued certificate**, not to a purchased edX verified certificate, professional certification or academic credit. Per-course certificate pages specify **70% or more on each required problem/project** (not 70% of the syllabus).

The current FAQ sets the **overall course submission deadline** at **2027-06-30 23:59 UTC**. CS50 also advises downloading the free certificate by that deadline. The deadline may later be extended and **is not represented as the lifetime expiration of an issued certificate**.

### OpenLearn badges

For **Introduction to cyber security** and **Digital skills**, the provider's *course-specific* badge guide states:
- Read all eight weeks.
- Score 50% or more on **each** of the Week 4 and Week 8 badge quizzes.
- Most questions allow three attempts; true/false questions typically allow one. Later correct answers may earn fewer points.
- If an entire badge quiz is failed, the **whole quiz** may be attempted again **after 24 hours**, as often as necessary.

Both course pages explicitly offer a free OU digital badge and Statement of Participation. OU badges are **not accredited OU academic qualifications**.

### CPD points

Both OpenLearn course pages explicitly state an award of **24 CPD points on successful course completion**, evidenced on the **free Statement of Participation**. We model these as `training_credit` with `kind: benefit` to distinguish CPD from the separate digital badge and statement. This does **not** assert university degree credit, transferability, independent accreditation of the individual award, or any separately issued CPD certificate. The issuer lists no extra charge for the points recorded on its free statement.

`Introducing computing and IT` is **not** assigned a badge or CPD points absent separate course-specific confirmation.

### freeCodeCamp Python v9

The issuer's course announcement identifies the current v9 certification as distinct from the older Scientific Computing with Python curriculum. Five certification projects and the required 50-question exam are not interchangeable with merely finishing lessons. Staff moderation and applicable exam restrictions are recorded; no automatic instant issuance is promised.

## Evidence footprint

- **10** distinct proposed courses.
- **14** typed official outcomes / course-linked CPD benefits.
- **63** dated, claim-specific evidence entries across **54** course-scoped claim paths and **26** unique official source URLs.
- No duplicated URL or record ID against the existing verified Responsive Web Design entry.
- No candidate is labeled `verified_free_outcome` or given a fabricated `review` object in the source proposals.

The proposal bundle's source-check timestamps remain intact. Newly added outcome/retake evidence has its own 29 October 2026 check timestamp.

## Final publication gate (pending)

1. Confirm this exact diff and the distinction between badges, statements and CPD benefits.
2. Re-run full JSON Schema validation and repository integrity CI.
3. Obtain **maintainer approval** for the exact records and set genuine `review.status`, `reviewed_at` and `recheck_after` only at publication time.
4. Then create one reviewed JSON record per course under `catalog/verified/`, update all index/count references in EN, RU, UK and ZH-CN, merge the reviewed PR, and manually run the Wiki publication workflow if Wiki sources change.

**This report is an independent evidence review, not final publication authorization.** Do not promote unapproved records automatically.
