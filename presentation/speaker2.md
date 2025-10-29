Speaker 2 Script (approx. 5 minutes)
---
Slide 7 - Property-based Testing
- "Thanks, <Speaker 1>. I'll walk through the property-based and contract testing results."
- "In tests/test_properties.py we used Hypothesis to generate random strings up to 64 characters."
- "Our property says any string that is not a valid URL must lead to HTTP 400 or 422. Hypothesis shrinks failing examples automatically, which boosts confidence in the validation logic."
---
Slide 8 - Contract Fuzzing with Schemathesis
- "We ran schemathesis run http://127.0.0.1:8000/openapi.json --checks all while the API was served by uvicorn."
- "The latest run generated 234 requests with zero failures. Schemathesis still warns that random codes return 404, so we plan to seed a known short code before fuzzing."
- "That gives us runtime-verification evidence and complements the pytest suites."
---
Slide 9 - Results Snapshot
- "All pytest suites passed: 11 tests covering functional, structural, and property-based categories."
- "coverage.py reported 99 percent statement coverage with only the random collision branch uncovered."
- "Schemathesis logged 'no issues found'; we captured the terminal output, Swagger screenshots, and coverage report for the appendix."
---
Slide 10 - Findings & Recommendations
- "Key improvement: the API now documents every status code it emits, eliminating the contract mismatches we saw at the start."
- "Recommendations include seeding a short code before Schemathesis, adding mutation testing (mutmut), and introducing static analysis (ruff, bandit)."
- "We also propose Hypothesis stateful tests or model checking to reason about alias uniqueness."
---
Slide 11 - Lessons Learned / CLO Mapping
- "Our final report maps each activity to the six course learning outcomes so reviewers can trace practice back to theory."
- "We emphasised the difference between functional and structural testing, and how property and contract testing add depth."
---
Slide 12 - Q&A
- "Thank you. We're ready for questions about the tooling, test evidence, or next steps."
