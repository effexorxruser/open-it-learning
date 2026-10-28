# Prompt: Design a verified-credential learning path

Use with an assistant that can browse current course and credential sources.

```text
Design an achievable IT learning path using official courses.

GOAL: <target role or skill>
CURRENT EXPERIENCE: <beginner/intermediate/etc.>
HOURS PER WEEK: <number>
TIME HORIZON: <weeks or months>
LANGUAGE / REGION: <preferences>
CREDENTIAL BUDGET: <amount and currency, or zero>

Prioritize courses whose learning content is free and whose certificate
availability, exact conditions and price are supported by official sources.

For every recommended course:
- Give the direct canonical official URL.
- Explain what prerequisite it covers and why it is in this sequence.
- Separate learning cost from certificate/exam cost.
- Classify the credential (completion certificate, digital badge,
  professional certification, or none).
- Link official evidence for obtainable certificates.
- State if the credential is unverified; don't present it as confirmed.
- Include realistic duration and any course availability caveats.

Return a phased path with estimated study hours, milestones, verified
credential checkpoints, total disclosed cost, uncertain costs and source
check dates. Do not fabricate completion guarantees or job placement.

Use the Open IT Learning catalog if it has relevant verified records;
otherwise clearly label externally researched recommendations separately.
```

Related: [course verification prompt](verify-course.md).
