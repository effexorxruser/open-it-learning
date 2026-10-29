# Research Batch #002 — Russian-language and industry-specific IT tracks

[← Research journal](../README.md) · [Course policy](../../docs/CATALOG_POLICY.md) · [Source-backed proposals](proposals.json)

**10 newly researched course/lesson proposals, none published to the verified catalog yet.** The existing 11 confirmed courses remain unchanged. This batch explicitly includes Russian-language offerings and business automation/1C instead of repeating the six-course CS50 concentration.

## Candidates

| Proposal | Issuer / learning domain | Language | Proposed official outcome | Editorial status |
| --- | --- | --- | --- | --- |
| [Быстрая разработка приложений](https://console.datalesson.ru/lessons/fast-app-development) | Урок цифры / АНО «Цифровая экономика», материалы фирмы «1С» · low-code, business-automation | ru | participation_record — Электронный сертификат «Урок цифры» — Быстрая разработка приложений | **ready_for_independent_source_review** |
| [«Поколение Python»: курс для начинающих](https://stepik.org/course/58852/promo) | Авторы курса / Stepik · python, programming | ru | completion_certificate — Сертификат о прохождении — «Поколение Python»: курс для начинающих | **under_review** |
| [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575/promo) | Авторы курса / Stepik · quality-assurance, test-automation | ru | completion_certificate — Сертификат о прохождении — Автоматизация тестирования с помощью Selenium и Python | **under_review** |
| [Введение в Data Science и машинное обучение](https://stepik.org/course/4852/promo) | Институт биоинформатики / Stepik · data-science, machine-learning | ru | completion_certificate — Сертификат о прохождении — Введение в Data Science и машинное обучение | **under_review** |
| [Introduction to Cybersecurity Awareness](https://www.life-global.org/en/course/346-introduction-to-cybersecurity-awareness) | HP LIFE / HP Foundation · cybersecurity, digital-literacy | en | completion_certificate — HP LIFE Certificate of Completion — Introduction to Cybersecurity Awareness | **ready_for_independent_source_review** |
| [Data Science & Analytics](https://www.life-global.org/en/course/344-data-science-and-analytics) | HP LIFE / HP Foundation · data-analytics, artificial-intelligence | en | completion_certificate — HP LIFE Certificate of Completion — Data Science & Analytics | **ready_for_independent_source_review** |
| [CS105: Introduction to Python](https://learn.saylor.org/course/cs105) | Saylor University · python, programming | en | completion_certificate — Saylor University Course Completion Certificate — CS105: Introduction to Python | **ready_for_independent_source_review** |
| [CS260: Introduction to Cryptography and Network Security](https://learn.saylor.org/course/cs260) | Saylor University · cybersecurity, cryptography | en | completion_certificate — Saylor University Course Completion Certificate — CS260: Introduction to Cryptography and Network Security | **ready_for_independent_source_review** |
| [AI Literacy (Earn a digital credential!)](https://skills.yourlearning.ibm.com/activity/PLAN-1C903152880C) | IBM SkillsBuild · artificial-intelligence, ai-literacy | en | digital_badge — AI Literacy — IBM SkillsBuild digital credential | **ready_for_independent_source_review** |
| [Data Modeling](https://trailhead.salesforce.com/content/learn/modules/data_modeling) | Salesforce Trailhead · crm, salesforce-administration | en | digital_badge — Data Modeling — Salesforce Trailhead badge | **ready_for_independent_source_review** |

## Result and evidence coverage

- **10 distinct canonical URLs**, **53 dated claim-level evidence entries** and **18 distinct cited first-party/course-source URLs**.
- **Four Russian-language courses**: a 1C-authored low-code lesson with an official completion certificate, plus three free Stepik courses in Python programming, Selenium UI testing, and Data Science. Language and region are recorded separately; no claim of global availability.
- **Six English-language entries**: HP LIFE cybersecurity and data analytics; Saylor CS105 Python and CS260 cryptography; IBM SkillsBuild AI Literacy; Salesforce Trailhead Data Modeling.
- **7 records have strong public course-specific outcome evidence and are ready for separate source review**, **3 Stepik records remain under review** because their exact certificate point thresholds have not yet been independently read in an authenticated course progress view. A platform-wide certificate rule alone cannot fill an unknown threshold.
- The **1C-authored lesson is from the historical 2021/22 “Урок цифры” season**. The official website currently publishes a completion-certificate instruction, but archived trainer availability and actual certificate generation are not independently tested. Confirm these before publishing it as verified.
- The free introductory 1C course from Yandex Practicum is **excluded**, because its official public course page does not document a specific completion certificate or badge; a third-party course aggregator claiming one is not sufficient.
- The 2026 1C “Код будущего” program is **under review**: official issuer sources prove funded free instruction for eligible 8–11 grade students / IT-college students, but the precise free reward issuance conditions are not confirmed by a first-party page.
- Paid 1C development courses on Stepik are rejected under the catalog's free-learning admission rule, regardless of whether they offer 1C certificates.

## Certification semantics

- A Stepik certificate is platform-issued, not an accredited academic qualification. The registered learner must meet the particular course's configured points threshold; the issuer determines the exact number. Free courses with enabled certificates receive that service without charge.
- HP LIFE provides free course-completion certificates, not professional industry licenses.
- Saylor requires **at least 70% on the course-specific Certificate Final Exam**, with a **maximum of three attempts** separated by **14 days**. The completion certificate also lists CEUs, which are not transferable university credit by default. This batch records the certificate only (no duplicate CEU award object).
- IBM AI Literacy is a free digital badge requiring prescribed modules and **80%+ on end-of-module quizzes**. Course-specific badge issuer criteria are published on the IBM SkillsBuild Credly badge page.
- Trailhead Data Modeling is a free **learning badge with 1,500 Trailhead points**, not a Salesforce professional certification. Finish three named units and required challenges.
- The “Урок цифры” 1C lesson issues an electronic training-completion document, **not** 1C:Профессионал or other paid professional examination credentials.

## Review and publication gate

1. Validate every proposed record's **content fields** with the current catalog JSON Schema using an ephemeral `review` test projection; never add fake approval to saved proposals.
2. Reopen each issuer page and verify quotes, restrictions, current availability and price. For Stepik, verify exact thresholds from the course's own grading page. For the old 1C trainer, confirm practical access and actual certificate issue pathway.
3. Only after an independent review and maintainer acceptance stage individual records under `catalog/verified/`; update English/Russian/Ukrainian/Chinese README and Wiki counts at the time of publication.
4. Keep this PR in Draft, do not merge or dispatch Wiki. No paid APIs, account creation, actual course enrollment or issuing recipients' certificates were performed.

**Editorial source review is not proof of an individual's course completion.**
