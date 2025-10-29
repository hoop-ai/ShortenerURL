# Project Explanation - FastAPI URL Shortener V&V
---
## 1. Why This Project
- Small but realistic web API (FastAPI + SQLite) that already exposes an OpenAPI schema.
- Zero external setup: SQLite database lives in the repo, so we could start testing immediately.
- Native support for pytest/TestClient makes it ideal for experimenting with multiple V&V techniques.
- Easy to extend with property-based testing (Hypothesis), contract fuzzing (Schemathesis), and coverage.
---
## 2. What the Service Does
1. Creating a short link  
   - Send POST /shorten with JSON like {"original_url": "https://fastapi.tiangolo.com/docs"}.  
   - The server generates a six-character code (e.g., 1uCvMq), stores it alongside the original URL in SQLite, and returns http://localhost:8000/r/1uCvMq.  
2. Using the short link  
   - Visiting http://localhost:8000/r/1uCvMq looks up the code, increments a click counter, and replies with an HTTP 307 redirect to the original URL.  
   - Unknown codes return 404 {"detail": "Short URL not found"}.  
3. Guardrails  
   - Input must be a valid HTTP/HTTPS URL; invalid strings are rejected automatically by Pydantic.  
   - Short codes allow letters and digits, keeping links URL safe.  
   - Clear JSON error messages are returned for invalid requests.  
4. Data storage  
   - Mappings live in shortener.db, a lightweight SQLite file.  
   - SQLAlchemy underpins the models so implementation stays simple.
---
## 3. Verification & Validation Techniques (Plain Language)
- Functional testing (black-box): call the API like a user, verify responses for shorten, redirect, 405, 404. Tool: pytest + TestClient.  
- Structural testing (white-box): inspect helpers and ORM defaults (generate_short_code, click counter). Tool: targeted pytest units + coverage.py.  
- Property-based testing: Hypothesis generates random strings and ensures non-URLs yield 400/422 responses.  
- Contract testing (runtime verification): Schemathesis reads the OpenAPI schema and fuzzes endpoints to catch specification mismatches.  
- Coverage: coverage.py measures which lines executed (99% statement coverage; collision loop remains).  
- Manual validation: run uvicorn, shorten a link via Swagger, follow the redirect in browser or curl to prove end-to-end behaviour.
---
### Quick Analogy
- Functional testing: checking if the remote control changes the TV channel.  
- Structural testing: examining the remote’s circuitry to confirm everything is wired correctly.  
- Property-based testing: saying “no matter what button sequence you press, the remote should never break the TV.”  
- Contract testing: comparing the remote’s behaviour to what the user manual promises.
---
## 4. Key Enhancements Delivered
- Updated routing so redirects use /r/{code} with documented 307/404/422 responses.  
- Added full pytest suite (functional, structural, property-based) with fixtures to clean the DB.  
- Integrated Schemathesis contract fuzzing and recorded results.  
- Instrumented the tests with coverage.py (99% statement coverage).  
- Produced documentation: final report, action plan, evidence log, FAQ, presentation outlines, speaker notes.
---
## 5. Talking Points for the Presentation
- Project choice rationale (size, tooling, OpenAPI).  
- Testing mix (functional, structural, property, contract, manual).  
- Evidence on hand (pytest, coverage, Schemathesis logs, Swagger screenshots, curl output).  
- CLO mapping (Section 8 of docs/final_report.md).  
- Limitations and next steps (seed code before Schemathesis, mutation testing, static analysis, duplicate-URL handling).
---
## 6. Optional Future Work
- Seed a known short code prior to Schemathesis runs to remove 404 warnings.  
- Introduce mutation testing (mutmut) and static analysis (ruff, bandit).  
- Add stateful Hypothesis tests or formal modelling (TLA+, Alloy) to reason about alias uniqueness.  
- Enhance duplicate URL handling rules and corresponding tests.
---
Use this summary when explaining the project to non-technical stakeholders or at the start of the presentation.
