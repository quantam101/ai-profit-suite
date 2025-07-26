# AI Profit Suite

Utilities to support the Contributor-to-Creator Program.

## Volunteer Hours Tracker

`volunteer_tracker.py` records volunteer hours and automatically generates a PDF certificate whenever a volunteer reaches a milestone (50, 100 or 500 hours).

### Requirements

- Python 3
- `fpdf` library (`pip install fpdf`)

### Usage

Add hours for a volunteer:

```bash
python volunteer_tracker.py "Alice Smith" 5
```

List all volunteers and their totals:

```bash
python volunteer_tracker.py --list
```

Certificates are placed in the `certificates/` folder.
