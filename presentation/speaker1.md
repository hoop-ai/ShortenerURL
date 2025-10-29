Speaker 1 Script (approx. 5 minutes)
---
Slide 1 - Title
- "Hi everyone, I'm <Speaker 1>. Together with <Speaker 2> we validated a FastAPI-based URL shortener for SEN4013."
- "Our goal was to apply verification and validation techniques that map directly to the course outcomes."
---
Slide 2 - Agenda
- "First I'll cover the automated tools we reviewed, then walk through the functional and structural test design."
- "After that, <Speaker 2> will take over with property-based testing, Schemathesis results, and our recommendations."
---
Slide 3 - Project Overview
- "We selected Tomas Vales' FastAPI shortener because it's lightweight, uses SQLite, and already ships with an OpenAPI schema."
- "The app exposes POST /shorten, which now returns URLs under /r/{code}, and GET /r/{code}, which redirects and increments a click counter."
- "We kept authentication and multi-node scaling out of scope so we could focus on verification depth."
---
Slide 4 - Automated Tool Stack (Part 1)
- "For unit and integration coverage we standardised on pytest with FastAPI's TestClient, covering CLO1 and CLO4."
- "We added Hypothesis to explore model-agnostic properties; its random input generation and shrinking support CLO4 and CLO6."
- "Schemathesis consumes the OpenAPI spec, giving us runtime verification evidence for CLO3 and CLO6."
- "We instrumented the suite with coverage.py, hitting 99 percent statement coverage, and documented follow-up plans for mutation testing and static analysis."
---
Slide 5 - Functional Testing
- "tests/test_functional.py covers the core black-box scenarios: shorten and redirect, 405 on GET /shorten, 404 on unknown codes, and verifying the click counter."
- "Fixtures in tests/conftest.py wipe the SQLite table between tests so every run is deterministic."
- "We also scripted manual validation using uvicorn, Swagger /docs, and curl to demonstrate a real user flow."
---
Slide 6 - Structural Testing
- "Structural or white-box checks live in tests/test_structural.py."
- "We verify that generate_short_code emits URL-safe codes, honours length overrides, and that the ORM default for clicks is zero after a commit."
- "Those checks plus coverage satisfy the structural-testing requirement and highlight the one uncovered collision branch."
---
Transition to Speaker 2
- "With the tooling and baseline tests covered, I'll hand it over to <Speaker 2> for the property-based testing results, Schemathesis analysis, and overall findings."
