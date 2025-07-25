# AI Profit Suite

This repository provides simple tools for gathering market insights.

## Scripts

### `main.py`
Prints a startup message.

### `expansion_insights.py`
Fetches Google Trends data for a given search term and lists the top cities/regions with the highest interest. Use this to identify promising areas for expansion.

Example:

```bash
python expansion_insights.py "electric bikes" --top 20
```

`--geo` can be changed to other country codes such as `GB` or left empty for worldwide results.
