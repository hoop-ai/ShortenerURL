Speaker Notes (Shared)
---
Slide 1 - Title (Speaker 1)
- Greet the audience and introduce both presenters.
- Briefly state the objective: demonstrate V&V techniques applied to the FastAPI shortener.
---
Slide 2 - Agenda (Speaker 1)
- Walk through the agenda quickly.
- Emphasize that automation, verification activities, and results will be the main focus.
---
Slide 3 - Project Overview (Speaker 1)
- Describe the architecture and endpoints.
- Mention decisions about scope (no auth, single instance).
---
Slide 4 - Why This Project (Speaker 1)
- Explain the rationale for choosing this repo (size, tooling compatibility).
- Highlight that the choice allowed focus on V&V depth.
---
Slide 5 - Automated Tool Stack (Speaker 1)
- Cover each tool and its purpose.
- Tie each tool back to relevant CLOs.
---
Slide 6 - Functional Testing (Speaker 1)
- Outline the scenarios in tests/test_functional.py.
- Mention manual Swagger/curl validation and DB fixture reset.
---
Slide 7 - Structural Testing (Speaker 1)
- Discuss tests/test_structural.py and coverage results.
- Note the single uncovered collision branch and future plan to trigger it.
---
Slide 8 - Property-based Testing (Speaker 2)
- Explain Hypothesis workflow and benefits (random inputs, shrinking).
- Reference tests/test_properties.py and the validation rule.
---
Slide 9 - Contract Fuzzing (Speaker 2)
- Describe the Schemathesis command and outcome (234 requests, warnings).
- Explain mitigation plan (seed known code) and runtime verification angle.
---
Slide 10 - Results & Evidence (Speaker 2)
- Summarize passed tests, coverage, and evidence artifacts.
- Point to docs/evidence_log.md for timestamps.
---
Slide 11 - Manual Validation (Speaker 2)
- Narrate the POST/GET demo for https://www.hoopai.com/docs.
- Mention the click counter increment and redirect header.
---
Slide 12 - Findings & Recommendations (Speaker 2)
- List resolved issues and open recommendations.
- Highlight plans for mutation testing, static analysis, duplicate URL handling.
---
Slide 13 - CLO Mapping (Speaker 1)
- Walk through the mapping table, tying activities to outcomes.
- Note future work covering CLO2 (formal/model-based techniques).
---
Slide 14 - Lessons Learned (Speaker 2)
- Share key takeaways about verification vs validation, automation, evidence keeping.
- Acknowledge limitations (Schemathesis warnings, pending tools).
---
Slide 15 - Q&A / Thank You (Both)
- Invite questions and thank the audience.
- Offer to revisit demos or logs if needed.
