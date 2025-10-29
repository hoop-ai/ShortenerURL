# Software V&V Project Report Outline

## 1. Introduction
- Purpose: demonstrate verification and validation of the FastAPI URL shortener using automated and manual techniques.
- Context: Based on `TomasVales/ShortenerURL`, enhanced with comprehensive pytest suites, Hypothesis property tests, Schemathesis contract fuzzing, and coverage metrics.
- Deliverables: tool review, V&V activities, results and recommendations, evidence appendix, presentation.

## 2. Objectives & Scope
- **Endpoints**: `POST /shorten` returns `http://localhost:8000/r/{code}`; `GET /r/{code}` issues a 307 redirect and increments click counters.
- **Technology**: FastAPI, SQLAlchemy, SQLite, pytest, Hypothesis, Schemathesis, coverage.py.
- **Assumptions**: No authentication, single instance, fixtures reset database state.
- **Out of scope**: Distributed scaling, persistent fixtures for Schemathesis, formal modelling (not yet implemented).

## 3. Automated Tool Review (Part 1 – 35 pts)
| Technique | Purpose & Theory | Tools / Notes | References |
|-----------|------------------|---------------|------------|
| Unit & integration testing | Validate concrete scenarios quickly (CLO1, CLO4) | `pytest`, FastAPI `TestClient`, fixtures (`tests/conftest.py`) | FastAPI testing docs |
| Structural testing | Exercise internal logic and invariants (CLO1, CLO4) | `tests/test_structural.py`, coverage confirms branches | Software Testing & Analysis (textbook) |
| Property-based testing | Explore broad input domains, shrink failures (CLO4, CLO6) | Hypothesis (`tests/test_properties.py`) rejects invalid URLs | hypothesis.readthedocs.io |
| Contract fuzzing / runtime verification | Detect schema/implementation drift (CLO3, CLO6) | Schemathesis `run ... --checks all`, warnings noted | schemathesis.readthedocs.io |
| Coverage metrics | Measure breadth of suite (CLO5) | `coverage run -m pytest`, 99% statement coverage | coverage.py docs |
| Static analysis & mutation (planned) | Strengthen future assurance (CLO5) | Recommended: `ruff`, `bandit`, `mutmut` | Course references |

## 4. V&V Activities (Part 2 – 35 pts)
### 4.1 Functional (black-box)
- `tests/test_functional.py`: shorten/redirect flow, 405 for GET `/shorten`, 404 for unknown codes, click counter verification.
- Manual validation via uvicorn + Swagger/curl (commands logged in evidence log).

### 4.2 Structural (white-box)
- `tests/test_structural.py`: regex & length checks, ORM defaults, randomness sampling.
- Shared fixture cleans database between tests; coverage highlights only collision branch untouched.

### 4.3 Property-based
- Hypothesis generates arbitrary strings (1–64 chars); non-URLs yield 400/422.
- Discuss how `assume` filters real URLs and how Hypothesis shrinks failing examples.

### 4.4 Contract fuzzing
- Schemathesis run with `--checks all`, 234 tests, zero failures, warnings about random 404s (recommend seeding short code).

### 4.5 Coverage
- `coverage run -m pytest` + `coverage report -m` → 99% total, only collision loop unexecuted.
- Include table or screenshot in appendix.

## 5. Test Cases & Results (Part 3 – 20 pts)
- Provide table listing functional, structural, property, contract cases with references to specific test functions.
- Include coverage summary and Schemathesis warning notes.

## 6. Findings & Incidents
- Document resolved issues: undocumented 404/405 fixed, `/r/{code}` path introduced.
- Open incidents: Schemathesis warnings (lack of seeded data), duplicate URL strategy undefined.

## 7. Recommendations (Part 4 – 10 pts)
1. Seed known short code before Schemathesis to eliminate warnings.
2. Integrate coverage reporting and add mutation testing (`mutmut`) to CI.
3. Add negative tests for malformed JSON & duplicate submissions.
4. Run static analysis (ruff, bandit) and document findings.
5. Explore Hypothesis stateful tests or formal verification (TLA+, Alloy) for alias uniqueness.

## 8. Evidence & Appendices
- Terminal captures: pytest, coverage, Schemathesis, manual curl.
- Swagger screenshot, database snapshot (optional).
- Mapping of CLOs to activities (table).
- Reference list: FastAPI docs, Hypothesis docs, Schemathesis quick start, course textbooks.
