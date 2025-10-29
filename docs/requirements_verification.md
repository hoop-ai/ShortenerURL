# Requirements Verification Matrix

This document traces each course/project requirement to the specific artefacts we produced.

| Requirement | Description | Evidence / Artefact |
|-------------|-------------|---------------------|
| **Part 1 – Review of Automated Tools (35 pts)** | Provide an overview of automated V&V/testing tools | Report Section 3 (`docs/final_report.md:24-44`); slide 4; discussion of pytest, Hypothesis, Schemathesis, coverage, future tools |
| **Part 2 – Verification & Validation Activities (35 pts)** | Analyse/test the chosen project using functional & structural approaches | Report Section 4 (`docs/final_report.md:46-78`); tests in `tests/`; manual validation log in `docs/evidence_log.md`; coverage run |
| **Functional testing examples** | Demonstrate black-box testing of endpoints | `tests/test_functional.py`; evidence log entries (2025-10-29 13:29 POST/GET); Slide 5 |
| **Structural testing examples** | Demonstrate white-box testing of internals | `tests/test_structural.py`; coverage report (99%); Slide 6 |
| **Property-based testing** | Apply Hypothesis or similar | `tests/test_properties.py`; Report Section 4.3 |
| **Runtime/contract verification** | Use tools like Schemathesis | Schemathesis command in evidence log; Report Section 4.4; Slide 8 |
| **Manual validation** | Show service working manually | Uvicorn + PowerShell logs (`docs/evidence_log.md`); slides mention Swagger demo |
| **Part 3 – Report (20 pts)** | Introduction, scope, test cases, recommendations | `docs/final_report.md` (sections 1–7) |
| **Report exportable to PDF** | Final deliverable format | Markdown ready for conversion; instructions to export before submission |
| **Part 4 – Presentation (10 pts)** | Video presentation ≤5 min per speaker | Slide outline (`presentation/slide_outline.md`); scripts (`presentation/speaker1.md`, `presentation/speaker2.md`) |
| **Course Learning Outcomes (CLO1–CLO6)** | Demonstrate achievement | CLO mapping table in `docs/final_report.md:101-110`; Slide 11 |
| **Evidence capture** | Screenshots/logs of tests, tools | `docs/evidence_log.md` checklist; coverage output; Schemathesis log; manual curl responses |
| **Original requirements trace** | Include official brief for reference | `docs/requirements_reference.md` stores the instructor’s assignment description |
| **Future improvements / limitations** | Describe possibilities & limitations | Report Sections 6–7; slides 10 (Findings & Recommendations) |
| **Presentation tone** | Conversational scripts aligning with slides | Updated scripts in `presentation/speaker1.md` and `presentation/speaker2.md` (see latest version) |
| **Additional explanation** | Plain-language summary for non-technical readers | `docs/project_explanation.md`; `docs/explanation.md` (overview) |
| **FAQ preparation** | Anticipate teammate/instructor questions | `docs/faqs.md` with peer-facing and instructor-facing answers |

Use this matrix during final review to ensure every grading rubric item is addressed before submission.
