# Detailed Action Plan

## Phase 0 – Environment Setup
1. Install Python 3.11+ and Git.
2. Clone repository: `git clone https://github.com/TomasVales/ShortenerURL.git`.
3. Create and activate virtual environment. Windows example: `py -m venv .venv` then `.venv\Scripts\activate`.
4. Install dependencies:
   - `pip install -r requirements.txt`
   - `pip install -r requirements-dev.txt` (for Schemathesis, coverage, etc.).

## Phase 1 – Baseline Verification
1. Run automated suite: `pytest -q` → expect `11 passed`.
2. Launch API for manual validation: `uvicorn app.main:app --reload`.
3. Capture evidence (terminal logs, screenshots) immediately after each command.

## Phase 2 – Functional Testing (Black-box)
1. Execute and review scenarios in `tests/test_functional.py`:
   - Happy path: POST `/shorten` then GET `/r/{code}` (200 → 307).
   - Unsupported method: GET `/shorten` → 405.
   - Unknown code: GET `/r/{code}` with random value → 404.
   - Click counter increments in the database.
2. Optional enhancements:
   - Add tests for malformed/empty JSON payloads.
   - Define behaviour for duplicate URLs (reuse vs. regenerate).

## Phase 3 – Structural Testing (White-box)
1. Review `tests/test_structural.py`:
   - Regex enforcement for generated codes.
   - Length override behaviour.
   - ORM default values after commit (`clicks == 0`).
   - Randomness sampling (≥50% unique codes across 50 iterations).
2. Consider advanced checks:
   - Statistical entropy evaluation.
   - Validation of database constraints (unique index on `short_code`).

## Phase 4 – Property-based Testing
1. Run Hypothesis (part of `pytest -q`).
2. Record failing examples or seeds if Hypothesis reports issues.
3. Extend properties if time permits:
   - Stateful test ensuring `shorten → redirect`.
   - Idempotency: shortening the same URL returns the same code (if design requires).

## Phase 5 – Contract Fuzzing / Runtime Verification
1. While uvicorn is running, execute:
   ```powershell
   $env:PYTHONIOENCODING='utf-8'
   schemathesis run http://127.0.0.1:8000/openapi.json --checks all
   Remove-Item Env:PYTHONIOENCODING
   ```
2. Optionally POST a known URL before the run to reduce 404 warnings.
3. Store the Schemathesis log (seed, warnings, summary) for appendices.

## Phase 6 – Coverage Analysis
1. Run `coverage run -m pytest -q`.
2. Generate summary via `coverage report -m` (expect ~99% coverage, missing collision branch).
3. Archive the report output and note untested lines for discussion.

## Phase 7 – Reporting
1. Populate the template in `docs/final_report.md` (already drafted).
2. Drop in tables: tool review, test matrix, coverage, Schemathesis warnings, CLO mapping.
3. Cite FastAPI testing docs, Hypothesis documentation, Schemathesis quick start, and course textbooks.
4. Export to PDF and verify formatting before submission.

## Phase 8 – Presentation Preparation
1. Build slides using `presentation/slide_outline.md` as the blueprint.
2. Follow the scripts in `presentation/speaker1.md` and `presentation/speaker2.md`.
3. Embed evidence screenshots (pytest, coverage, Schemathesis, Swagger).
4. Rehearse to keep each speaker within the 5-minute limit, then record the video.

## Phase 9 – Final Checks & Submission
1. Re-run `pytest -q` and Schemathesis to confirm green status.
2. Clean workspace for submission (exclude `.venv`, `__pycache__`, coverage artefacts).
3. Submit:
   - PDF report.
   - Slide deck (PPTX or PDF).
   - Presentation video.
   - Optional evidence bundle (logs, screenshots).
4. Upload to Microsoft Teams before 16 January 2026 17:30 and back up locally/OneDrive.
