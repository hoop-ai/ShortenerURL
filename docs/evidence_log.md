# Evidence Log

| Timestamp (local) | Command / Action | Outcome | Notes |
|-------------------|------------------|---------|-------|
| 2025-10-29 12:58 | `git clone https://github.com/TomasVales/ShortenerURL.git` | Success | Repository imported into project workspace. |
| 2025-10-29 13:00 | `python -m venv .venv` | Success | Created isolated Python 3.12 environment. |
| 2025-10-29 13:01 | `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` | Success | Installed FastAPI, pytest, Hypothesis, SQLAlchemy, etc. |
| 2025-10-29 13:05 | `.\.venv\Scripts\python.exe -m pip install coverage` | Success | Added coverage metrics tooling. |
| 2025-10-29 13:06 | `.\.venv\Scripts\coverage.exe run -m pytest -q` | Success (11 passed) | Verified functional, structural, and property tests under coverage instrumentation. |
| 2025-10-29 13:06 | `.\.venv\Scripts\coverage.exe report -m` | Total cover 99% | Only uncovered branch: line 22 in `app/routes/url.py` (random-collision loop not triggered). |
| 2025-10-29 13:29 | `uvicorn app.main:app --port 8000` + `Invoke-RestMethod POST /shorten` | HTTP 200 + short URL | Manual validation created short code `1uCvMq`. |
| 2025-10-29 13:29 | `Invoke-WebRequest GET /r/1uCvMq -MaximumRedirection 0` | HTTP 307 | Confirmed redirect target `https://fastapi.tiangolo.com/docs`. |
| 2025-10-29 13:31 | `schemathesis run http://127.0.0.1:8000/openapi.json --checks all` | Success w/ warnings | 234 generated tests, no failures; warnings logged about random 404 responses. |
| 2025-10-29 13:32 | `.\.venv\Scripts\python.exe -m pytest -q` | Success (11 passed) | Final verification after documentation updates. |

## Artefact Checklist
- [ ] Screenshot of pytest output (green bar / terminal capture).
- [ ] Screenshot of coverage summary (or captured terminal output).
- [ ] Screenshot of Schemathesis summary (with warnings footnote).
- [ ] Screenshot of Swagger UI (`/docs`) showing `POST /shorten` and `GET /r/{short_code}`.
- [ ] Optional: SQLite browser screenshot showing stored URLs & click counts.
- [ ] Video capture demonstrating manual validation steps (for presentation).

## Reproduction Notes
- Run Schemathesis with `PYTHONIOENCODING=utf-8` in Windows consoles to avoid Unicode errors.
- `tests/conftest.py` clears the `urls` table before each test; no manual DB reset required.
- To silence Schemathesis 404 warnings, seed a known short code (POST `/shorten`) before executing the contract fuzzing command.
