# AI Profit Suite

This repository provides simple tools for generating weekly tutorials based on trending topics. The tutorials can be used to create content for your community or to offer educational material for sale.

## Requirements
- Python 3.11+
- `requests`
- `beautifulsoup4`

Required packages can be installed with:

```bash
pip install -r requirements.txt
```

## Usage

Generate beginner-level tutorials from GitHub trending repositories:

```bash
python tutorial_generator.py
```

Specify the difficulty level or provide custom topics:

```bash
python tutorial_generator.py --level expert --topics "Data Science" "Machine Learning"
```

The script creates Markdown files in the `tutorials` directory with a timestamp in the filename.

