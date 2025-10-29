# Software Verification & Validation Project Report  
FastAPI URL Shortener (SEN4013)

---

## 1. Introduction
This project applies software verification and validation (V&V) techniques to a lightweight URL shortener implemented with FastAPI, SQLAlchemy, and SQLite. The aim is to demonstrate how functional, structural, property-based, and contract testing provide confidence that the service satisfies its specification. The work directly supports the SEN4013 learning outcomes by pairing theory with executable evidence.

---

## 2. Objectives and Scope
- **Functional scope**
  - `POST /shorten`: accepts `{"original_url": "<valid URL>"}` and returns `http://localhost:8000/r/{code}`.
  - `GET /r/{code}`: issues an HTTP 307 redirect to the original URL and increments a click counter.
- **Technology**: FastAPI, SQLAlchemy ORM, SQLite database (`shortener.db`), Pydantic validation.
- **Assumptions**: No authentication, single-instance deployment, automated tests reset the database between runs.
- **Out of scope**: High availability, rate limiting, persistent fixtures for Schemathesis, formal state-machine modelling.

---

## 3. Review of Automated V&V Tools (Part 1 – 35 pts)
| Technique | Purpose | Tooling / Notes | References |
|-----------|---------|-----------------|------------|
| Unit and integration testing | Exercise concrete scenarios quickly (CLO1, CLO4) | `pytest`, FastAPI `TestClient`, fixtures in `tests/conftest.py` | FastAPI testing docs |
| Structural (white-box) testing | Inspect internal invariants (CLO1, CLO4) | `tests/test_structural.py` verifies regex, ORM defaults, randomness | Ammann & Offutt, *Introduction to Software Testing* |
| Property-based testing | Explore wide input domains, shrink failures (CLO1, CLO4, CLO6) | Hypothesis (`tests/test_properties.py`) rejects non-URL strings | Hypothesis documentation |
| Contract fuzzing / runtime verification | Detect schema/implementation drift (CLO3, CLO6) | Schemathesis (`schemathesis run ... --checks all`) | Schemathesis quick start |
| Manual validation | Empirical check via Swagger and curl (CLO3, CLO5) | `uvicorn app.main:app --reload`, `Invoke-RestMethod`, `Invoke-WebRequest` | Evidence log screenshots |
| Coverage metrics and future analysis | Quantify breadth, plan mutation/static checks (CLO5) | `coverage.py` (99% statement coverage), mutation and static analysis noted for follow-up | coverage.py docs; Foundations of Software Testing |

---

## 4. Verification and Validation Activities (Part 2 – 35 pts)

### 4.1 Functional / Black-box Testing
- `tests/test_functional.py` covers the shorten/redirect happy path, 405 on `GET /shorten`, 404 on unknown codes, and click counter increments.
- Fixtures wipe the `urls` table before each test, ensuring deterministic results.
- Manual validation: start uvicorn, create a short URL via Swagger or curl, and confirm the redirect to the original location.

### 4.2 Structural / White-box Testing
- `tests/test_structural.py` asserts that generated codes are alphanumeric, length overrides are honoured, ORM defaults set `clicks` to zero, and random sampling yields sufficient variety.
- Coverage tooling highlights that only the collision loop inside `app/routes/url.py` (line 22) remains unexecuted during normal runs.

### 4.3 Property-based Testing
- Hypothesis generates strings of length 1–64. `assume` filters out genuine URLs so only malformed candidates reach the endpoint.
- The property demands a 400 or 422 response for any non-URL input, demonstrating automated edge-case discovery beyond example-based tests.

### 4.4 Contract Testing (Runtime Verification)
- Command:  
  ```powershell
  $env:PYTHONIOENCODING='utf-8'
  schemathesis run http://127.0.0.1:8000/openapi.json --checks all
  Remove-Item Env:PYTHONIOENCODING
  ```
- Result: 234 generated requests, zero failures. Warnings note that random codes return 404; seeding a known code before the run will remove the warning and exercise the redirect path.

### 4.5 Coverage Metrics
- Command: `coverage run -m pytest -q` followed by `coverage report -m`.
- Outcome: 99% statement coverage. The only uncovered line is the while-loop collision branch in `app/routes/url.py`.
- Coverage output (terminal log) is captured in `docs/evidence_log.md`.

---

## 5. Test Cases and Results (Part 3 – 20 pts)
| ID | Category | Description | Expected | Result | Artefact |
|----|----------|-------------|----------|--------|----------|
| TC-FUNC-01 | Functional | Shorten URL then redirect | 200 + 307 with correct `Location` | Pass | `tests/test_functional.py::test_shorten_and_redirect_flow` |
| TC-FUNC-02 | Functional | `GET /shorten` unsupported | 405 Method Not Allowed | Pass | `tests/test_functional.py::test_get_shorten_returns_405` |
| TC-FUNC-03 | Functional | Unknown short code | 404 JSON error | Pass | `tests/test_functional.py::test_redirect_unknown_code_returns_404` |
| TC-FUNC-04 | Functional | Click counter increments | Clicks = 1 after redirect | Pass | `tests/test_functional.py::test_redirect_increments_click_counter` |
| TC-STRUCT-01 | Structural | Regex enforcement and length | Codes are alphanumeric and correct length | Pass | `tests/test_structural.py::test_generate_short_code_uses_url_safe_alphanumerics` |
| TC-STRUCT-02 | Structural | ORM default for `clicks` | Clicks initialises to zero | Pass | `tests/test_structural.py::test_url_model_defaults_clicks_to_zero` |
| TC-PROP-01 | Property | Random invalid strings rejected | HTTP 400/422 | Pass | `tests/test_properties.py::test_shorten_rejects_invalid_urls` |
| TC-CONTRACT-01 | Contract | Schemathesis fuzzing (`--checks all`) | No failures; warnings logged | Pass with warnings | Schemathesis summary |

Evidence: pytest output, coverage report, Schemathesis summary, and manual curl logs are logged in `docs/evidence_log.md`.

---

## 6. Limitations and Open Issues
1. Schemathesis warnings persist because random short codes trigger 404 responses. Seeding a known code before the run would demonstrate the redirect path.
2. Mutation testing has not yet been executed. Tools such as `mutmut` or `MutPy` should be trialled to assess assertion strength.
3. Static analysis (`ruff`, `bandit`) has not been run; recommended to identify style or security issues.
4. Duplicate URL handling is basic: the service currently generates a new code for every POST. Behaviour could be refined and covered by additional tests.
5. Formal modelling (state machines, TLA+, Alloy) has not been attempted; consider Hypothesis stateful testing to reason about alias uniqueness.

---

## 7. Recommendations
1. Seed a known short code prior to Schemathesis runs to remove warnings and hit the redirect path automatically.
2. Automate coverage reporting in CI and introduce mutation testing to quantify test suite strength.
3. Run static analysis (ruff for style, bandit for security) and document findings.
4. Add negative tests for malformed JSON payloads, unsupported schemes, and duplicate submissions.
5. Explore stateful or formal techniques to guarantee alias uniqueness and redirect correctness.
6. Update the project README with testing instructions and evidence references for easier handover.

---

## 8. Course Learning Outcome Mapping
| CLO | Evidence |
|-----|----------|
| CLO1 – Explain V&V concepts | Tool review (Section 3), discussion of functional vs structural testing |
| CLO2 – Model-based / model checking | Recommendations for Hypothesis stateful tests and formal methods |
| CLO3 – Runtime verification | Schemathesis contract fuzzing and manual validation steps |
| CLO4 – Select and apply techniques | Combination of pytest suites, Hypothesis, Schemathesis, manual checks |
| CLO5 – Possibilities and limitations | Limitations section, coverage analysis, and recommendations |
| CLO6 – Use automated tools | Hands-on execution of pytest, Hypothesis, Schemathesis, coverage, uvicorn |

---

## 9. Submission Checklist
- Report exported to PDF with references and appendices.
- Evidence pack (logs, screenshots) stored per `docs/evidence_log.md`.
- Presentation assets prepared in `presentation/`.
- Source code and tests ready for submission.
- Optional extras pending: mutation testing, static analysis.

---

## References
- T. Vales, *ShortenerURL* (GitHub repository).
- FastAPI documentation – Testing: https://fastapi.tiangolo.com/tutorial/testing/
- Hypothesis documentation: https://hypothesis.readthedocs.io/
- Schemathesis quick start: https://schemathesis.readthedocs.io/en/stable/quick-start/
- Ned Batchelder, *coverage.py* documentation: https://coverage.readthedocs.io/
- Pezzè, M., & Young, M., *Software Testing and Analysis: Process, Principles and Techniques*.
- Ammann, P., & Offutt, J., *Introduction to Software Testing*.
