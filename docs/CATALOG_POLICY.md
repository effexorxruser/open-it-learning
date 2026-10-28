# Catalog inclusion policy

[← Home / Главная](../README.md) · [Catalog / Каталог](../catalog/README.md) · [Record format](DATA_CONTRACT.md)

## The point of Open IT Learning

The verified index is for **free IT courses that offer at least one officially documented, obtainable outcome or benefit**.

The outcome may be a certificate, a digital badge, a diploma, a commendation, an official completion record, an exam voucher, a training credit, or another named, provider-issued recognition or perk. The catalog is **not restricted to certificates**.

It must be tied to the **specific course**. A provider's generic claims about awards are not sufficient.

## Accepted outcome types

| Type | Meaning | Important distinction |
| :--- | :--- | :--- |
| `completion_certificate` | Provider-issued course completion certificate | Not automatically a professional qualification |
| `professional_certificate` | Named industry or professional credential | Check exams, issuer and fees separately |
| `digital_badge` | Issuer-awarded digital badge or achievement | Does not automatically count as a certificate |
| `diploma` | Named diploma or formal document of completion | Do not imply accredited academic degree status |
| `award` | Official award, commendation, competition prize or certificate of merit | State eligibility and what was actually awarded |
| `participation_record` | Official participation letter, transcript or completion statement | Not automatically a graded qualification |
| `exam_voucher` | Official exam voucher or exam discount tied to course completion | Not an earned exam pass or credential |
| `training_credit` | Provider-issued learning credits, credits toward a program or lab access | Do not infer formal academic credit or unlimited access |
| `other_official_benefit` | Another specifically documented, course-linked benefit | Must be identified, not described vaguely as “perks” |

**Evidence must describe the particular outcome**, its issuer, how to earn it, and its cost. Individual credential verification may be available but is **not** assumed; note the method or `null` if unavailable.

## Admission checks

A verified course must pass **all** checks:

1. **Authentic course.** A live, canonical official URL; matching title and issuer.
2. **Free learning.** The actual training content is available without a required payment. Free samples, limited trials and promotional discounts do not qualify without clearly supported free access conditions.
3. **Official outcome.** An issuer's official page confirms an identifiable reward, record or benefit can be obtained **for this course**. A menu item labeled “Achievements” or generic promise does not establish this.
4. **Earnability.** Required modules, assessments, enrollment, geography, eligibility, expiry and redemption steps are sufficiently documented. Material unknowns block a verified label.
5. **Transparent costs.** Separate learning fees from outcome/issuance fees and exam fees. Outcomes may be paid; the fee must be disclosed and known, not guessed. An exam voucher may reduce an exam fee without certifying exam completion.
6. **Traceable source.** Claim-level official URLs, short excerpts, evidence dates and review notes are stored.
7. **Review completed.** A reviewer checks meaning, not only string matches, and records when the claim was verified.

## Record status

| Status | Meaning |
| :--- | :--- |
| `verified_free_outcome` | Free learning and at least one documented **free** obtainable official outcome |
| `verified_paid_outcome` | Free learning and documented obtainable official outcome with known issuance or exam cost |
| `under_review` | Source proof, conditions, costs or semantics are incomplete — **not published** in the verified index |
| `recheck_required` | Previously confirmed claim may be stale, broken or conflicting; no current verified claim until rechecked |
| `rejected` | Not a qualifying free course or no documented official outcome is obtainable |

An outcome record must always disclose its **type**; the status alone never implies “certificate”. A free digital badge is welcome if the issuer and conditions are confirmed; a paid certificate is allowed if clearly labeled and course access is free.

## Example: Cisco research

A dated snapshot of [Cisco Introduction to Cybersecurity](../journal/2026-10-28-cisco-introduction-to-cybersecurity.md) showed free course access, “6 HOURS”, and the phrase “Badges you can earn in this course”.

This is evidence that the course page **advertises badges**. It does not independently establish the particular badge, issuer's issuance conditions or whether the user earns it without additional cost. Therefore **under review** until checked.

## Handling later changes

Keep the original issuer source and review timestamp. Track course closures, renamed credentials, discontinued badges, changed fees and expired vouchers. If an outcome becomes unavailable, re-evaluate status rather than silently leaving a stale verified listing online.

## Public scope

Catalog editors may use manual research or automation, but **the public repository is only the collection, prompts, skills, editorial guidance and optional high-level research notes**. Private agent-development infrastructure is not a product requirement.
