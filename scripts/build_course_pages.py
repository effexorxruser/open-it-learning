#!/usr/bin/env python3
"""Build human-readable course pages from verified JSON, without altering issuer evidence.

Usage:
  python3 scripts/build_course_pages.py
  python3 scripts/build_course_pages.py --check

The canonical source is catalog/verified/*.json. The taxonomy provides only
editorial display grouping; never infer official prerequisites from navigation.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIED = ROOT / "catalog/verified"
COURSES = ROOT / "catalog/courses"
NAVIGATION = ROOT / "catalog/navigation"

OUTCOME_LABELS = {
    "completion_certificate": "сертификат об окончании",
    "professional_certificate": "профессиональный сертификат",
    "digital_badge": "цифровой бейдж",
    "participation_record": "подтверждение участия",
    "training_credit": "баллы CPD / CEU",
    "diploma": "диплом",
    "award": "награда",
    "exam_voucher": "ваучер на экзамен",
    "other_official_recognition": "официальное признание",
    "other_official_benefit": "другой официальный бонус",
}
LANGUAGES = {"ru": "русский", "en": "английский", "uk": "украинский", "zh-CN": "китайский"}
LEVELS = {"beginner": "начальный", "intermediate": "средний", "advanced": "продвинутый"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def language(course: dict) -> str:
    return ", ".join(LANGUAGES.get(code, code) for code in course["languages"]) or "не указан"


def duration(course: dict) -> str:
    value = course["duration_hours"]
    if value is None:
        return "не указана"
    if value < 1:
        return f"≈{round(value * 60)} мин"
    return f"≈{value:g} ч"


def cost(value, currency) -> str:
    if value == 0:
        return "бесплатно"
    if value is None:
        return "не подтверждена"
    return f"{value:g} {currency or 'валюта не указана'}"


def outcome_summary(course: dict) -> str:
    return ", ".join(dict.fromkeys(
        OUTCOME_LABELS.get(item["type"], item["type"]) for item in course["outcomes"]
    ))


def page(course: dict, location: dict, specialization: dict, domain: dict) -> str:
    ident = course["id"]
    lines = [
        f"# {course['title']}",
        "",
        "[← Все курсы](README.md) · [Все направления](../navigation/README.md)",
        "",
        f"**[Открыть курс на официальном сайте →]({course['official_url']})**",
        "",
        f"> **Обучение:** {cost(course['learning']['cost'], course['learning']['currency'])} · "
        f"**Язык:** {language(course)} · "
        f"**Уровень:** {LEVELS.get(course['level'], 'не указан')} · "
        f"**Длительность:** {duration(course)}",
        "",
        f"**Организатор:** {course['provider']}",
        "",
        f"**Направление:** [{domain['label']['ru']}](../navigation/domains/{domain['id']}.md) "
        f"· **Специализация:** {specialization['label']['ru']}",
        "",
        "## Официальные результаты и условия",
        "",
    ]
    for result in course["outcomes"]:
        lines += [
            f"### {result['name']}",
            "",
            f"**Тип:** {OUTCOME_LABELS.get(result['type'], result['type'])} "
            f"· **Стоимость получения:** {cost(result['cost_to_obtain'], result['currency'])}",
            "",
            result["requirements"],
            "",
            f"[Условия награды на официальном сайте]({result['official_evidence_url']})",
            "",
        ]
    lines += [
        "## Доступ и ограничения",
        "",
        course["learning"]["conditions"],
        "",
        "## Источники и статус",
        "",
        f"- **Публичные условия проверены:** {course['review']['reviewed_at'][:10]}.",
        f"- **Плановая перепроверка:** {course['review']['recheck_after'][:10]}.",
        f"- [Полная JSON-карточка, цитаты и доказательства](../verified/{ident}.json).",
        f"- [Перейти на сайт курса]({course['official_url']}).",
        "",
        "Проверены официально опубликованные правила, а не фактическая выдача награды "
        "после прохождения курса. Редакционные рекомендации не заменяют требований организатора.",
        "",
    ]
    return "\n".join(lines)


def index(courses: dict, placements: dict, taxonomy: dict) -> str:
    lines = [
        "# Бесплатные IT-курсы — открыть и начать обучение",
        "",
        "[← Каталог](../README.md) · [Направления IT](../navigation/README.md) "
        "· [Маршруты обучения](../navigation/learning-paths.md)",
        "",
        f"**{len(courses)} курса с проверенными официальными результатами.** "
        "Название ведёт на понятную страницу с условиями, а ссылка **«Открыть курс»** "
        "— непосредственно на сайт организатора.",
        "",
        "Все ссылки на учебные программы берутся из исходных проверенных JSON-карточек. "
        "Для некоторых платформ потребуется бесплатная регистрация. "
        "Условия могут измениться; дата проверки указана в каждой карточке.",
        "",
    ]
    for domain in taxonomy["domains"]:
        entries = [
            courses[ident] for ident, location in placements.items()
            if location["primary_specialization"] in
            {item["id"] for item in domain["specializations"]}
        ]
        entries.sort(key=lambda item: item["title"].casefold())
        lines += [
            f"## {domain['label']['ru']} / {domain['label']['en']} — {len(entries)}",
            "",
            f"[Все специализации направления](../navigation/domains/{domain['id']}.md)",
            "",
        ]
        if not entries:
            lines += ["Пока нет подтверждённых курсов.", ""]
            continue
        lines += ["| Курс | Организатор | Язык | Что получите | Сайт обучения |",
                  "| --- | --- | --- | --- | --- |"]
        for course in entries:
            ident = course["id"]
            lines.append(
                f"| [{course['title']}]({ident}.md) | {course['provider']} "
                f"| {language(course)} | {outcome_summary(course)} "
                f"| [Открыть курс]({course['official_url']}) |"
            )
        lines.append("")
    lines += [
        "## О прозрачности каталога",
        "",
        "Условия бесплатного обучения и получения результата проверены по официальным "
        "источникам. Типы результатов не смешиваются: бейдж, подтверждение участия, "
        "сертификат и баллы CPD/CEU — разные вещи. "
        "[Проверенные JSON-записи и исходные доказательства](../verified/README.md).",
        "",
        "Программа 1С «Код будущего» пока остаётся в "
        "[журнале исследований](../../journal/research-batch-002/README.md) "
        "и не включена в этот подтверждённый список.",
        "",
    ]
    return "\n".join(lines)


def wiki_index(courses: dict, placements: dict, taxonomy: dict) -> str:
    prefix = "https://github.com/effexorxruser/open-it-learning/blob/main/catalog/courses/"
    lines = [
        "# Все курсы — прямые ссылки",
        "",
        "[← Каталог Wiki](https://github.com/effexorxruser/open-it-learning/wiki/Catalog) "
        "· [Навигация по IT](https://github.com/effexorxruser/open-it-learning/wiki/IT-Directions)",
        "",
        f"**{len(courses)} проверенных IT-курсов.** Нажмите **«Учиться»**, чтобы "
        "попасть на официальный сайт организатора, или **«Условия»**, чтобы прочитать "
        "требования к бесплатной награде и источники.",
        "",
    ]
    for domain in taxonomy["domains"]:
        entries = sorted(
            (courses[ident] for ident, location in placements.items()
             if location["primary_specialization"] in
             {sp["id"] for sp in domain["specializations"]}),
            key=lambda item: item["title"].casefold()
        )
        lines += [f"## {domain['label']['ru']} — {len(entries)}", ""]
        if not entries:
            lines += ["Пока нет подтверждённых курсов.", ""]
            continue
        lines += ["| Курс | Язык | Учиться | Условия |",
                  "| --- | --- | --- | --- |"]
        for course in entries:
            lines.append(
                f"| {course['title']} | {language(course)} "
                f"| [Открыть курс]({course['official_url']}) "
                f"| [Подробнее]({prefix}{course['id']}.md) |"
            )
        lines.append("")
    lines += [
        "Подтверждено наличие бесплатных официальных результатов по опубликованным "
        "правилам провайдеров; получение награды на личном аккаунте не тестировалось.",
        "",
    ]
    return "\n".join(lines)


def expected_pages() -> dict[Path, str]:
    courses = {
        item["id"]: item for item in
        (load(path) for path in sorted(VERIFIED.glob("*.json")))
    }
    taxonomy = load(NAVIGATION / "taxonomy.json")
    placements = {
        item["course_id"]: item
        for item in load(NAVIGATION / "placements.json")["records"]
    }
    if set(courses) != set(placements):
        raise ValueError("Navigation placements must cover exactly all verified course IDs")
    specialties = {
        item["id"]: (item, domain)
        for domain in taxonomy["domains"]
        for item in domain["specializations"]
    }
    pages = {}
    for ident, course in courses.items():
        spec = placements[ident]["primary_specialization"]
        if spec not in specialties:
            raise ValueError(f"Unregistered specialization: {ident} -> {spec}")
        specialization, domain = specialties[spec]
        if not course["official_url"].startswith("https://"):
            raise ValueError(f"Missing HTTPS primary course link: {ident}")
        pages[COURSES / (ident + ".md")] = page(
            course, placements[ident], specialization, domain
        )
    pages[COURSES / "README.md"] = index(courses, placements, taxonomy)
    pages[ROOT / "wiki-source/Courses.md"] = wiki_index(courses, placements, taxonomy)
    return pages


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true",
                        help="fail if generated Markdown is missing or outdated")
    args = parser.parse_args()
    pages = expected_pages()
    extra = set(COURSES.glob("*.md")) - {
        path for path in pages if path.parent == COURSES
    }
    if extra:
        print("Unexpected course pages: " +
              ", ".join(str(p.relative_to(ROOT)) for p in sorted(extra)),
              file=sys.stderr)
        return 1
    dirty = []
    for path, desired in pages.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != desired:
                dirty.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(desired, encoding="utf-8")
    if dirty:
        print("Run python3 scripts/build_course_pages.py; stale: " +
              ", ".join(dirty), file=sys.stderr)
        return 1
    print(f"{'Checked' if args.check else 'Generated'} "
          f"{len(pages) - 2} human course pages, one catalog index and one Wiki directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
