# Independent primary-source editorial review — Batch #002

**Reviewed:** 2026-10-29T15:20:31.775Z  
**Method:** separate ChatGPT session revisited course pages, first-party certificate rules, public Stepik REST API and issuer-hosted IBM badge via Credly. Not the same initial card-generation pass.  
**Scope:** publicly documented free access, course-specific issuer recognition, conditions, fees and classifications. **Not actual enrollment, completion, award delivery or professional accreditation testing.**

## Decisions

| ID | Source review | Disposition |
| --- | --- | --- |
| `hp-life-ai-for-beginners` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `hp-life-cybersecurity-awareness` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `ibm-skillsbuild-ai-literacy` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `kaggle-intro-to-machine-learning` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `microsoft-learn-describe-cloud-compute` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `one-c-future-code-element-2026` | Official 1C announcement lacks an explicit certificate issuance price and eligibility is limited | **UNDER REVIEW — excluded from verified** |
| `saylor-cs101-introduction-to-programming` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `saylor-cs302-software-engineering` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `stepik-interactive-sql-63054` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `stepik-introduction-to-linux-73` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |
| `stepik-yandex-cpp-363` | Official training and course-specific recognition/conditions corroborated | **SOURCE REVIEWED — staged on PR** |

## Substantive corrections

1. **Exact Stepik thresholds confirmed without enrolling.** Public `https://stepik.org/api/courses/{course_id}` exposes `certificate_regular_threshold`, `certificate_distinction_threshold`, `is_certificate_issued` and `is_certificate_auto_issued`. The verified values today are Linux **100/113**, SQL **136/144**, and C++ **90/106** respectively. The issuer's `help.stepik.org/article/54825` confirms that certificates enabled on free courses are a no-cost bonus. Retest these values in the future; do not generalize one course threshold to another.
2. **Canonical IBM evidence link corrected** to `https://www.credly.com/org/ibm-skillsbuild/badge/ai-literacy`. Its issuer is **IBM SkillsBuild**, the award is a free *digital badge*, and its criteria are an approved learning plan and **80%+** end-of-module quiz scores.
3. **Explicit Kaggle claim source:** The provider's `https://www.kaggle.com/learn-course-certificates` confirms that completing a course gives a certificate accessible through the Completed tab. A course's estimated learning hours are not minimum study hours.
4. **CEUs on Saylor certificates:** The CS101 and CS302 official syllabi state **2.6** and **3.6** continuing-education units respectively, recorded **on** ordinary free course completion certificates, without a separate fee. They are modelled as `training_credit` course-linked benefits to prevent implying they are independently issued degrees, professional licenses or guaranteed academic-transfer credit.
5. **1C remains a hold.** The official September 2026 provider announcement confirms funded **in-person Moscow** training with restricted student eligibility and a module certificate, but does not expressly state the price of issuing the latter. `cost_to_obtain: null` is deliberately preserved. Adding a fabricated zero would violate the existing `docs/CATALOG_POLICY.md`.

## Publishing controls

- **Eleven** research cards, **ten** source-reviewed publication copies; the 1C draft stays outside `catalog/verified/`.
- **Twelve** typed new outcome entries, including the two Saylor CEU benefits.
- All positive publication review states are tied to an actual independent **public-source** review, not to recipient-specific examination, tested issuing workflows, human academic accreditation or course attendance.
- Original research drafts retain no `review` object; they are archival evidence, not authorized publication claims.
- The maintainer's merge approval is still required. Do not auto-publish or imply Wiki is already synchronized.
