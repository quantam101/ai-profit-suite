# AI Profit Suite

Python utility suite for content drafts, contributor tracking, product review, and PDF summary reporting.

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Verify

```bash
python -m py_compile *.py scripts/generate_summary.py
python scripts/generate_summary.py sample_data.json output/daily_summary.pdf
pytest -q
```

## Utilities

- `volunteer_tracker.py`: track contributor hours and create certificates.
- `tutorial_generator.py`: create reusable tutorial drafts.
- `detect_and_alert.py`: review product CSV rows and create discount CSV output.
- `daily_summary.py`: send metric summaries when messaging settings are configured.
- `scripts/generate_summary.py`: create PDF summaries.
- `resource_uploader.py`: store approved local resources or reference links.
