Slide 1 - Title & Team
- Title text: “FastAPI URL Shortener – Software V&V Project (SEN4013)”
- Subtitle: “Verification & Validation via Automated and Manual Techniques”
- Team members + roles (Speaker A: tool review & testing strategy, Speaker B: property/contract testing & findings)
- Visuals: [Screenshot: FastAPI logo + SQLite icon side-by-side], [Text overlay: Course code SEN4013]
---
Slide 2 - Agenda
- Bullet list: Tool review, V&V activities, Test outcomes & evidence, Findings & recommendations, CLO mapping, Q&A
- Visuals: [Diagram: simple timeline showing flow Tool Review → Activities → Results → Findings → Q&A]
---
Slide 3 - Project Overview
- Bullet points:
  - Based on TomasVales/ShortenerURL (FastAPI + SQLite)
  - Endpoints: POST /shorten → http://localhost:8000/r/{code}, GET /r/{code} → 307 redirect + click counter
  - Scope exclusions: authentication, distributed deployment, advanced storage
- Visuals: [Diagram: Flow showing Client → FastAPI app → SQLite DB], [Screenshot: Swagger /docs overview]
---
Slide 4 - Why This Project
- Reasons:
  - Small but realistic API with OpenAPI schema
  - SQLite bundled, no external services
  - Existing pytest scaffold encourages V&V experimentation
  - Easy to extend with property-based and contract testing
- Visuals: [Screenshot: GitHub repo landing page], [Icon row: pytest, Hypothesis, Schemathesis, coverage.py]
---
Slide 5 - Automated Tool Stack
- Table-style bullets:
  - pytest + FastAPI TestClient (unit/integration)
  - Hypothesis (property-based)
  - Schemathesis (runtime contract testing)
  - coverage.py (structural coverage, 99% statement coverage)
  - Planned: mutmut, ruff, bandit
- Visuals: [Screenshot: requirements-dev.txt snippet], [Checklist graphic labeling each tool with CLO alignment]
---
Slide 6 - Functional Testing (Black-box)
- Content:
  - tests/test_functional.py scenarios (happy path, GET /shorten 405, unknown code 404, click counter)
  - Manual validation via Swagger /docs and curl
  - Fixture-driven DB reset to ensure determinism
- Visuals: [Screenshot: pytest output highlighting test_functional], [Screenshot: Swagger try-it POST /shorten], [Screenshot: curl/PowerShell response showing 307 redirect]
---
Slide 7 - Structural Testing (White-box)
- Content:
  - tests/test_structural.py verifying code format, length override, ORM defaults, randomness sample
  - coverage run -m pytest -q → coverage report (only collision branch uncovered)
  - Mention future plan to force collision for 100% coverage
- Visuals: [Screenshot: coverage report terminal], [Code snippet: utils.generate_short_code + model default], [Icon: magnifying glass over code]
---
Slide 8 - Property-based Testing
- Content:
  - Hypothesis generates arbitrary strings, filters real URLs with assume, expects 400/422
  - Value: automatic shrinking, exposure of edge cases beyond handcrafted data
  - File reference: tests/test_properties.py
- Visuals: [Code snippet: Hypothesis test block], [Screenshot: pytest run showing property test executed], [Graphic: random input cloud → validation gate]
---
Slide 9 - Contract Fuzzing with Schemathesis
- Content:
  - Command: schemathesis run http://127.0.0.1:8000/openapi.json --checks all (with PYTHONIOENCODING set)
  - Outcome: 234 requests, zero failures, warnings about random 404s (plan to seed known code)
  - Emphasize runtime verification and OpenAPI alignment
- Visuals: [Screenshot: Schemathesis summary “No issues found”], [Command snippet box], [Icon: OpenAPI document + shield]
---
Slide 10 - Results & Evidence Snapshot
- Table summarizing:
  - Functional tests: 4 cases → Pass
  - Structural tests: 4 cases → Pass
  - Property test: invalid URL rejection → Pass
  - Contract fuzzing: 234 cases → Pass w/ warnings
  - Coverage: 99% statements (collision branch pending)
- Visuals: [Table graphic], [Screenshot: docs/evidence_log.md entries], [Badge icons: PASS/Warning]
---
Slide 11 - Manual Validation Walkthrough
- Steps:
  - Start uvicorn app.main:app --reload
  - POST /shorten for https://www.hoopai.com/docs → receive http://localhost:8000/r/qy4H6B
  - GET /r/qy4H6B → 307 redirect to original URL, click counter increments
- Visuals: [Screenshot: PowerShell POST response], [Screenshot: PowerShell 307 headers], [Optional: Browser address bar showing redirect]
---
Slide 12 - Findings & Recommendations
- Resolved:
  - Documented 405 and 404 responses, updated OpenAPI metadata
  - Redirect path moved to /r/{code} to avoid method conflicts
- Recommendations:
  - Seed known code before Schemathesis to remove warnings
  - Add mutation testing (mutmut) and static analysis (ruff, bandit)
  - Handle duplicate URL submissions, explore stateful/formal verification
- Visuals: [Bullet infographic], [Icon set: wrench, bug, shield]
---
Slide 13 - Course Learning Outcomes Mapping
- Map table:
  - CLO1: Tool review (Section 3, Slide 5)
  - CLO2: Future formal/stateful testing recommendations
  - CLO3: Schemathesis runtime verification
  - CLO4: Selection of functional, structural, property, contract tests
  - CLO5: Coverage metrics + limitations discussion
  - CLO6: Hands-on tool usage (pytest, Hypothesis, Schemathesis, coverage)
- Visuals: [Table graphic], [Flow arrow from activities to CLOs]
---
Slide 14 - Lessons Learned
- Points:
  - Combining verification (structural) and validation (functional) exposes different issues
  - Property-based and contract testing find edge cases humans might miss
  - Maintaining evidence (logs, screenshots) simplifies grading and presentations
- Visuals: [Quote bubble], [Checklist graphic emphasizing “Evidence”, “Automation”, “Traceability”]
---
Slide 15 - Q&A / Thank You
- Text: “Questions? Thank you for your time!”
- Provide repo link or QR code (include short URL if desired)
- Visuals: [QR code placeholder linking to repo], [Email or contact icons], [Course logo]
---
