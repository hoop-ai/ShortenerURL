# Frequently Asked Questions (FAQ) Pack
---
Use these canned answers to stay aligned with your teammate and to handle likely instructor questions during the presentation.
---
## A. Team Discussion FAQs (Peer-to-Peer)
---
**Q1. Why did we pick the FastAPI URL shortener instead of the Flask or Node options?**  
A: It is small, runs on SQLite (no external services), exposes an OpenAPI schema, and already had a pytest layout—so we could focus on verification techniques instead of setup.
---
**Q2. What does the app actually do?**  
A: `POST /shorten` takes an HTTP/HTTPS URL, generates a six-character code, stores it in SQLite, and returns `http://localhost:8000/r/{code}`. `GET /r/{code}` looks up the original URL, increments a click counter, and returns a 307 redirect. Unknown codes return 404.
---
**Q3. Where are the tests and how do I run them?**  
A: All tests live in the `tests/` folder. Activate the virtual environment and run `pytest -q`. For coverage, run `coverage run -m pytest -q` followed by `coverage report -m`.
---
**Q4. What is the difference between functional and structural tests in our project?**  
A: Functional (“black-box”) tests call the API like a user (shorten, redirect, 405 on `GET /shorten`). Structural (“white-box”) tests inspect internals such as `generate_short_code` and the SQLAlchemy model defaults.
---
**Q5. How did we implement property-based testing?**  
A: Using Hypothesis. The test generates random strings, filters out those that look like real URLs, and ensures the endpoint rejects everything else with 400/422. See `tests/test_properties.py`.
---
**Q6. What did Schemathesis tell us?**  
A: `schemathesis run http://127.0.0.1:8000/openapi.json --checks all` fired 234 requests, found zero failures, but warned that random short codes return 404. Seeding a known code before the run would remove that warning.
---
**Q7. What evidence do we have ready?**  
A: Terminal output for pytest, coverage, Schemathesis; Swagger screenshots; manual curl logs. All timestamps are recorded in `docs/evidence_log.md`.
---
**Q8. What tasks remain if we want bonus points?**  
A: Run mutation testing (`mutmut`), add static analysis (`ruff`, `bandit`), seed a short code before Schemathesis, and explore stateful property tests or formal modelling.
---
## B. Presentation FAQs (Instructor-Facing)
---
**Q1. How does this project satisfy Part 1 (tool review)?**  
A: Section 3 of the report compares pytest/TestClient, Hypothesis, Schemathesis, coverage.py, and recommended static-analysis/mutation tools, linking each to the relevant course learning outcomes.
---
**Q2. Where do we demonstrate functional versus structural testing?**  
A: Functional testing appears in `tests/test_functional.py` and in manual Swagger/curl checks; structural testing is in `tests/test_structural.py` plus the coverage report. Both are explained in the report and presentation.
---
**Q3. How did property-based testing add value beyond the integration test?**  
A: Hypothesis explored a wide range of random inputs and shrank failures automatically, surfacing edge cases beyond handcrafted examples and validating input-handling rules.
---
**Q4. What did the Schemathesis run reveal, and how are we handling the warnings?**  
A: The run confirmed the API matches the OpenAPI contract (zero failures) but warned about 404s for random short codes. We plan to seed a known code before fuzzing so the redirect path is hit.
---
**Q5. How did you verify structural coverage?**  
A: We ran `coverage run -m pytest` followed by `coverage report -m`, achieving 99% statement coverage. The only uncovered line is the collision branch in `app/routes/url.py` which would require forcing duplicate codes.
---
**Q6. Which course learning outcomes does this project hit?**  
A: CLO1 (tool review theory), CLO3 (runtime verification via Schemathesis), CLO4 (selecting diverse V&V techniques), CLO5 (coverage metrics and limitations), CLO6 (hands-on automation). CLO2 is addressed in the recommendations for future formal/stateful testing.
---
**Q7. How do you plan to extend or improve the test suite?**  
A: Add mutation testing, run static analysis, define duplicate-URL handling tests, and explore Hypothesis stateful checks—documented in Section 7 of the report.
---
**Q8. What manual validation evidence is included?**  
A: Logs showing `POST /shorten` returning a short URL and `GET /r/{code}` returning a 307 redirect, plus Swagger screenshots—all listed in the evidence log.
---
**Q9. How does this project demonstrate combining verification and validation?**  
A: Verification checks the code against design (structural tests, coverage, contract checking) while validation confirms real-world behaviour (functional tests, manual Swagger run). Using both surfaces issues one approach alone might miss.
---
**Q10. If Schemathesis reports were to fail, how would you debug?**  
A: Reproduce the failing request using the curl command Schemathesis prints, compare the response to the schema, adjust either the implementation or the OpenAPI docs, and rerun. This is how we resolved the initial 405/404 mismatch.
