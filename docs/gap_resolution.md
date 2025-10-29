# Gap Analysis Resolution – Draft vs. Actual Implementation

## Summary of Identified Gaps
| Draft Statement | Status in Original Draft | Actual Project State | Resolution |
|-----------------|--------------------------|----------------------|------------|
| Technology stack: Flask app with `unittest`, no property testing | Draft focused on a Flask/regex/Blake2b implementation and claimed Hypothesis was unavailable | Project uses FastAPI, SQLAlchemy, pytest, Hypothesis, and Schemathesis | Report, code comments, and presentation materials now describe the FastAPI architecture, pytest suite, and successful Hypothesis execution |
| Endpoints described as `/shorten_url` (POST/GET) | Draft referenced the reference project rather than the current API | Real API exposes `POST /shorten` and `GET /r/{short_code}` with 307 redirects | Router updated to return documented status codes; report and slides updated to reference `/shorten` and `/r/{code}` |
| Property-based tests marked as “skipped” | Hypothesis said to be missing | Hypothesis installed and executed as part of pytest suite | `tests/test_properties.py` committed; report cites actual results and shrink behaviour |
| Contract testing omitted | No mention of OpenAPI-driven testing | Schemathesis run exposes contract conformance | Schemathesis integrated into requirements-dev, run output captured, warnings documented |
| Manual validation not described | Draft lacked uvicorn/manual steps | Manual validation executed via Swagger/curl | `docs/action_plan.md` and final report document commands and observations |
| Persistence described as in-memory | Draft referenced a dictionary store | Implementation uses SQLite via SQLAlchemy | Documentation corrected to highlight SQLite persistence and test fixtures |
| Limitations outdated | Draft mentioned missing Hypothesis/tests | Real limitations relate to Schemathesis warnings, mutation/static analysis | Limitations section rewritten to match actual state; recommendations updated |

## Remediation Actions
1. **Code alignment**  
   - `app/routes/url.py` now documents 200/307/404/422 responses and returns short URLs under `/r/{code}`.  
   - Test suite expanded (`tests/` package) to cover functional, structural, and property validations with shared fixtures.

2. **Toolchain updates**  
   - Hypothesis retained in `requirements.txt`; Schemathesis and coverage recorded in `requirements-dev.txt`.  
   - Automated checks confirmed: `pytest -q` (11 passed), Schemathesis (234 tests, warnings only), `coverage.py` (99 %).

3. **Documentation refresh**  
   - `docs/final_report.md` rewritten to match FastAPI solution, including coverage metrics and contract-testing evidence.  
   - `docs/action_plan.md` and `docs/evidence_log.md` provide reproducible steps and timestamps.  
   - Presentation assets rewritten with ASCII-safe text and updated talking points.

4. **Traceability**  
   - `docs/requirements_reference.md` stores the original project brief for citation.  
   - `docs/gap_resolution.md` (this file) summarises how discrepancies were addressed.

## Remaining Recommendations
- Seed a known short code before Schemathesis to eliminate 404 warnings in the report/video.  
- Add mutation testing (e.g., `mutmut`) and static analysis (ruff, bandit) for additional evidence.  
- Extend property-based tests to cover idempotency or stateful scenarios if time permits.  
- Update README and final PDF appendices with links to evidence (logs, screenshots) before submission.
