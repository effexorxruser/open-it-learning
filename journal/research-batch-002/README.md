# Research Batch #002 — Russian-language and new IT providers

[← Research journal](../README.md) · [Candidate JSON files](cards/) · [Catalog policy](../../docs/CATALOG_POLICY.md)

**10 new candidate cards prepared, not yet added to verified catalog.** Published index stays at 11 courses and 15 typed outcomes until independent editorial review and maintainer approval.

Research checked: **2026-10-29 UTC**. All candidates are distinct from current catalog URLs. **4 courses have Russian-language instruction**, including specialized 1С development; the batch represents **7 educational platforms/provider groups** and covers ERP/1С, Linux, SQL, C++, cybersecurity, Java, software engineering, AI, cloud and machine learning.

| Candidate | Issuer / platform | Language | Named official outcome | Editorial gate |
| --- | --- | --- | --- | --- |
| [Разработка на 1С: игры, приложения и искусственный интеллект](cards/one-c-future-code-element-2026.json) | 1С-Учебный центр №3 / проект «Код будущего» | ru | completion_certificate | under_review |
| [Введение в Linux](cards/stepik-introduction-to-linux-73.json) | Институт биоинформатики / Stepik | ru | completion_certificate | source_checked_pending_threshold_review |
| [Интерактивный тренажер по SQL](cards/stepik-interactive-sql-63054.json) | Stepik | ru | completion_certificate | source_checked_pending_threshold_review |
| [Введение в программирование (C++)](cards/stepik-yandex-cpp-363.json) | Академия Яндекса / Stepik | ru | completion_certificate | source_checked_pending_threshold_review |
| [Introduction to Cybersecurity Awareness](cards/hp-life-cybersecurity-awareness.json) | HP LIFE / HP Foundation | en | completion_certificate | Independent source review |
| [CS101: Introduction to Programming I](cards/saylor-cs101-introduction-to-programming.json) | Saylor University | en | completion_certificate | Independent source review |
| [CS302: Software Engineering](cards/saylor-cs302-software-engineering.json) | Saylor University | en | completion_certificate | Independent source review |
| [AI Literacy](cards/ibm-skillsbuild-ai-literacy.json) | IBM SkillsBuild / IBM | en | digital_badge | Independent source review |
| [Describe cloud computing](cards/microsoft-learn-describe-cloud-compute.json) | Microsoft Learn | en | digital_badge | Independent source review |
| [Intro to Machine Learning](cards/kaggle-intro-to-machine-learning.json) | Kaggle Learn | en | completion_certificate | Independent source review |

## Critical editorial caveats

- **1С / Код будущего:** The specific [1С-Учебный центр №3 announcement](https://www.1c-uc3.ru/about/news/besplatnoe-obuchenie-programmirovaniyu-dlya-shkolnikov-v-ramkakh-proekta-kod-budushchego/) describes **free, in-person Moscow training** for grade 8–11 pupils and eligible IT college students, entry via Госуслуги plus screening, and certificates for successfully completed modules. It does **not separately specify a certificate issuance fee**. The course must stay under review until the issuer explicitly confirms that module certificates are free; its provisional `0` outcome cost is a **research hypothesis**, not verified proof.
- **Stepik free certificate courses:** The exact promotions advertise both free learning and a certificate, and [Stepik's author help](https://help.stepik.org/article/54825) describes free-course certificates as a free platform bonus. [Student help](https://help.stepik.org/article/54735) states that **individual authors set the points threshold**. Open promotional pages did not confirm the exact numerical threshold of these three courses. Check course-specific certificate settings before promoting any record.
- **Microsoft Learn:** Only a **module Achievement badge** is claimed, not a Microsoft Certified qualification or Applied Skills credential. The [FAQ](https://learn.microsoft.com/en-us/training/support/faq) separates those types and states that learning is free.
- **Saylor CS101/CS302:** Standard free Certificate Final Exams are separate from optional ACE-credit/proctored exams. CS101 syllabus lists a 14-day retake wait and three attempts, while CS302 lists seven days and an optional paid $5 proctored ACE exam.
- **IBM AI Literacy:** The [issuer-hosted Credly criteria](https://www.credly.com/org/ibm/badge/ai-literacy) require prescribed modules and **80%+ on module quizzes**; registration and age-specific tracks apply. Do not substitute a restricted IBM badge for this program.
- **HP LIFE and Kaggle:** Course pages state the free certificate, but this research did not complete a learner account or validate a recipient-specific URL.
- No platform, Microsoft, university, Russian government, or professional accreditation is inferred merely from course completion.

## Review and publication gate

Each [individual candidate JSON](cards/) matches the course record's **field structure except for deliberately missing `review` metadata**. Evidence includes dated source URLs and short exact excerpts. The 1С cost issue and Stepik threshold issues prevent automatic publication under the existing [catalog policy](../../docs/CATALOG_POLICY.md).

Before adding any candidate to `catalog/verified/`, independently re-open all consequential official source pages, resolve the flagged limitations (or exclude the candidate), verify all costs and eligibility conditions, and then add genuine editorial `review` metadata. Run full Draft 2020-12 JSON Schema validation, deduplication and repository CI. No automatic PR merge or Wiki synchronization.

No paid API calls, new accounts, exam attempts, submission, or actual reward issuance testing were performed.

**Source-backed and pending review is not equivalent to verified.**
