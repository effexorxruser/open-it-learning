# Research Batch #002 — verified-source research and multilingual IT courses

[← Research journal](../README.md) · [Original research cards](cards/) · [Source audit](editorial-review-2026-10-29.md) · [Catalog policy](../../docs/CATALOG_POLICY.md)

## Results as of the editorial follow-up on 29 October 2026

**11 distinct candidates researched; 10 source-reviewed cards staged for publication in Draft PR #6; 1 deliberately held under review.** The staged catalog records enter public `main` only after the maintainer authorizes the merge. These 10 courses add **12 typed result entries** (10 course certificates/badges plus 2 Saylor CEU benefits). Together with Batch #001, the catalog will contain **21 course records and 27 typed outcomes** after merge.

The research encompasses **seven provider/platform groups**: Stepik (three Russian-language courses), HP LIFE (two courses), Saylor University (two), IBM SkillsBuild, Microsoft Learn, Kaggle Learn, and 1С (one withheld). The four Russian-language research candidates include the restricted Moscow 1С program, which is **not** counted among the ten staged records. No new learner accounts, exams or credential-receipt tests were used.

| Research candidate | Issuer / platform | Outcome reviewed | Review decision |
| --- | --- | --- | --- |
| [Введение в Linux](cards/stepik-introduction-to-linux-73.json) | Институт биоинформатики / Stepik | Free certificate, **100** points; distinction **113** | Staged |
| [Интерактивный тренажер по SQL](cards/stepik-interactive-sql-63054.json) | Stepik | Free certificate, **136** points; distinction **144** | Staged |
| [Введение в программирование (C++)](cards/stepik-yandex-cpp-363.json) | Академия Яндекса / Stepik | Free certificate, **90** points; distinction **106** | Staged |
| [Introduction to Cybersecurity Awareness](cards/hp-life-cybersecurity-awareness.json) | HP LIFE / HP Foundation | Free completion certificate | Staged |
| [AI for Beginners](cards/hp-life-ai-for-beginners.json) | HP LIFE / HP Foundation / UNIDO | Free completion certificate | Staged |
| [CS101: Introduction to Programming I](cards/saylor-cs101-introduction-to-programming.json) | Saylor University | Free completion certificate + **2.6 CEUs** shown on it | Staged |
| [CS302: Software Engineering](cards/saylor-cs302-software-engineering.json) | Saylor University | Free completion certificate + **3.6 CEUs** shown on it | Staged |
| [AI Literacy](cards/ibm-skillsbuild-ai-literacy.json) | IBM SkillsBuild | Free **digital badge**, not a professional certification | Staged |
| [Describe cloud computing](cards/microsoft-learn-describe-cloud-compute.json) | Microsoft Learn | Free *module achievement badge*, not Microsoft Certified | Staged |
| [Intro to Machine Learning](cards/kaggle-intro-to-machine-learning.json) | Kaggle Learn | Free course completion certificate | Staged |
| [Разработка на 1С: игры, приложения и ИИ](cards/one-c-future-code-element-2026.json) | 1С / Код будущего | Module completion certificate; **issuance fee unknown** | **Under review: not staged** |

## Official source verification — previously unresolved

- **Stepik's own public API** supplies exact course-specific regular/distinction thresholds, explicitly states `is_certificate_issued: true` and `is_certificate_auto_issued: true` for [Linux](https://stepik.org/api/courses/73), [SQL](https://stepik.org/api/courses/63054) and [C++](https://stepik.org/api/courses/363). All three promotion pages label learning free and advertise certificates. [Issuer documentation](https://help.stepik.org/article/54825) says enabling certificates for free courses is a free platform bonus; [student help](https://help.stepik.org/article/54735) describes score, issuance and timing. Thresholds can change, so they are dated evidence.
- **1С:** The [provider announcement](https://x.1c-uc3.ru/about/news/besplatnoe-obuchenie-programmirovaniyu-dlya-shkolnikov-v-ramkakh-proekta-kod-budushchego/) is dated September 2026. It documents free learning for grades 8–11 and eligible college students at an **in-person Moscow venue**, enrolment through Госуслуги, entry testing and module certificates. It does **not** state a separate issuance fee. The draft keeps `cost_to_obtain: null`; this is unknown, not zero. It must not be copied to the verified directory unless this and current enrolment availability are resolved.
- **IBM:** The issuer's [canonical AI Literacy badge](https://www.credly.com/org/ibm-skillsbuild/badge/ai-literacy) is issued by IBM SkillsBuild, requires prescribed modules and **80%+** on each end-of-module quiz, costs nothing and documents adult and school pathways. The incorrect earlier Credly URL under `/org/ibm/` was corrected.
- **Saylor:** [CS101 syllabus](https://learn.saylor.org/mod/page/view.php?id=84727) and [CS302 syllabus](https://learn.saylor.org/mod/page/view.php?id=71746) explicitly document standard free certificates after passing the free final with **70%+**. CS101 imposes a 14-day retake wait and a three-attempt limit; CS302 has a seven-day certificate-exam wait. CS302's optional separately proctored ACE credit exam costs **$5** and is **not needed** for the free ordinary certificate. Their **2.6 and 3.6 CEUs** are displayed on those free completion certificates; they are `training_credit` benefits, **not** separate qualifications or automatically transferable academic credit.
- **HP LIFE:** Official course pages specifically promise completion certificates for [Cybersecurity Awareness](https://www.life-global.org/course/346-introduction-to-cybersecurity-awareness) and [AI for Beginners](https://www.life-global.org/course/391-ai-). The [issuer homepage](https://www.life-global.org/) documents free learning and free certificates; the AI course was co-developed with UNIDO.
- **Microsoft Learn:** The [module](https://learn.microsoft.com/en-us/training/modules/describe-cloud-compute/) is free and requires completing its units and passing its knowledge assessment; the [official FAQ](https://learn.microsoft.com/en-us/training/support/faq) explicitly distinguishes an Achievement badge for a module from paid professional credentials. Azure lab subscriptions are not represented as a free external certification.
- **Kaggle:** [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) is no-cost with an estimated three-hour completion time. [Kaggle course-certificate help](https://www.kaggle.com/learn-course-certificates) explicitly says every finished course yields a certificate accessible from the Completed tab.

## Admission controls and limits

Original research cards remain in `cards/` **without `review` metadata**, even when a reviewed copy is staged for merge. Publication copies in `catalog/verified/` contain a dated **independent AI-assisted public-source review**, not a human course completion audit. The 1С record is intentionally excluded.

Draft 2020-12 JSON Schema tests validate each staged card, its agreement with the original proposal except `review`, all new evidence claim paths, the absence of false free fees, and deduplication against the existing 11 records. Each source outcome is typed, with CPD/CEU points not misrepresented as accreditation or a separate degree.

No paywall circumvention, exams, new learner accounts, paid APIs, recipient-specific certificate lookup, automatic Wiki publishing or automatic merge.

**Final publication gate:** latest-head GitHub Actions must pass and the maintainer must explicitly approve this precise PR before it enters `main`.
