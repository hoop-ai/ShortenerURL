Slide 1 - Title & Team
- Title: "FastAPI URL Shortener - Software V&V Project (SEN4013)"
- List team members and roles (Speaker 1: tool review & test design, Speaker 2: property/contract testing & results)
- Objective: "Validate the service end-to-end with functional, structural, property-based, and contract testing"
---
Slide 2 - Agenda
- Automated tools reviewed
- V&V activities performed
- Test results, coverage, evidence
- Key findings, recommendations, CLO mapping
---
Slide 3 - Project Overview
- Architecture: FastAPI + SQLAlchemy + SQLite
- Endpoints: POST /shorten -> http://localhost:8000/r/{code}; GET /r/{code} -> 307 redirect + click counter
- Scope: no authentication, single-node deployment, SQLite persistence
---
Slide 4 - Automated Tool Stack (Part 1)
- pytest + TestClient for unit/integration checks (CLO1, CLO4)
- Hypothesis for property-based fuzzing of invalid URLs (CLO4, CLO6)
- Schemathesis for OpenAPI-driven contract fuzzing (CLO3, CLO6)
- coverage.py delivers 99% statement coverage; note future static analysis (ruff, bandit) and mutation testing (mutmut) for CLO5
---
Slide 5 - Functional Testing
- Scenarios in tests/test_functional.py: happy path (200 -> 307), GET /shorten 405, unknown code 404, click counter increment
- Placeholder for pytest output or summary table
- Manual validation: Swagger /docs + curl log snippet
---
Slide 6 - Structural Testing
- tests/test_structural.py: regex enforcement, length override, click default = 0, randomness sample
- Mention fixture in tests/conftest.py clearing URLs table each test
- Cite coverage report highlighting the collision branch still uncovered
---
Slide 7 - Property-based Testing
- Show Hypothesis snippet (tests/test_properties.py)
- Explain strategy: generate arbitrary strings, filter real URLs with assume, expect 400/422
- Benefit: automatic shrinking and broad input exploration
---
Slide 8 - Contract Fuzzing with Schemathesis
- Command: schemathesis run http://127.0.0.1:8000/openapi.json --checks all
- Results: 234 requests, zero failures; warnings about random 404s (plan to seed known code)
- Tie to runtime verification and how it complements pytest suites
---
Slide 9 - Results & Coverage Snapshot
- Table summarising test categories vs outcomes (functional, structural, property, contract)
- Coverage summary: 99% total with a single uncovered collision branch
- Evidence references: pytest log, coverage report, Schemathesis summary, Swagger screenshot
---
Slide 10 - Findings & Recommendations
- Resolved: documented 405/404 responses, aligned OpenAPI metadata
- Open: seed short code before Schemathesis, add mutation/static analysis, handle duplicate URLs
- Future: configurable base URL, persistent fixtures, explore stateful/formal verification
---
Slide 11 - Lessons Learned & CLO Mapping
- Graphic/table linking activities to CLOs (CLO1: tool review, CLO3: Schemathesis run, CLO5: coverage & limitations)
- Note impact on QA mindset and automation strategy
---
Slide 12 - Q&A / Thank You
- Invite questions
- Optional: repo link or QR code
