# Contributing to Open IT Learning

[← Home](README.md) · [Catalog](catalog/README.md) · [Admission policy](docs/CATALOG_POLICY.md)

**Open IT Learning** collects free IT courses that offer officially documented **certificates, digital badges, diplomas, awards, participation documents or other real provider-linked benefits**. It also shares reusable prompts and skills.

## Suggest a course

Provide:

1. Exact issuer, official course title and direct official URL.
2. Evidence that **learning content** is free, including restrictions.
3. One or more **specifically named official results** obtainable through that course (badge, certificate, diploma, award, record, exam voucher, etc.).
4. A source from the issuer spelling out how the result is earned/redeemed.
5. Any separate issuance, exam or redemption fee and relevant eligibility conditions.
6. Short evidence excerpts, links and date checked in UTC.

Be precise about type: a digital badge is a valid result but is not automatically a certificate; a voucher is a benefit, not proof of qualification. If the evidence is incomplete, the proposal remains **under review**.

[Suggest a course](https://github.com/effexorxruser/open-it-learning/issues/new/choose).

## Improve prompts or skills

Propose helpful research prompts, learning-path planners, verification workflows, translations and interface ideas. They should be portable and understandable without our internal maintenance tools.

## Report corrections

If an official badge is discontinued, a certificate cost changes, an exam voucher expires or a course becomes paid, provide the relevant official sources and dates. Don't silently remove past evidence.

## Pull requests

- Keep changes scoped and explain their practical value.
- Include issuer sources for new or changed official claims.
- Separate training price, recognition/benefit issuance fees and exam cost.
- Classify all outcomes accurately.
- Keep unknown requirements as unknown; never treat excerpt matches alone as proof.
- Never upload API keys, cookies, private agent logs or copyrighted course content in bulk.
- Run `python3 scripts/check_integrity.py` before opening a PR. GitHub Actions runs the same dependency-free integrity check on PRs and pushes to `main`; it checks file links, JSON and basic catalog structure, **not** whether an award is genuinely offered by a provider.

## Repository boundaries

Our internal research and development stack stays private and is **not** required to use the public catalog, prompts or skills.

## Licensing

No formal project license is selected yet. Do not assume all material can be reused under an open-source license merely because the repository is public. Please avoid importing content with unclear third-party rights.
