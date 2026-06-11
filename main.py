"""AI Profit Suite command-line entrypoint."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence


def run_tutorial(args: argparse.Namespace) -> int:
    from tutorial_generator import generate_tutorial_content
    topics = args.topics or ["AI automation", "local service lead capture", "field technician dispatch"]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{args.level}_tutorials.md"
    with output_file.open("w", encoding="utf-8") as handle:
        handle.write(f"# {args.level.title()} Tutorials\n\n")
        for topic in topics:
            handle.write(generate_tutorial_content(topic, args.level))
            handle.write("\n")
    print(f"Generated tutorial file: {output_file}")
    return 0


def run_summary(args: argparse.Namespace) -> int:
    from scripts.generate_summary import build_pdf, load_data
    data = load_data(args.input_json)
    build_pdf(data, args.output_pdf)
    print(f"Generated summary PDF: {args.output_pdf}")
    return 0


def run_status(_: argparse.Namespace) -> int:
    modules = {
        "tutorial": "Generate reusable educational content templates.",
        "summary": "Generate daily business summary PDFs."
    }
    print(json.dumps({"service": "ai-profit-suite", "status": "ready", "modules": modules}, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI Profit Suite utility CLI")
    subparsers = parser.add_subparsers(dest="command")

    status_parser = subparsers.add_parser("status", help="Print available modules")
    status_parser.set_defaults(func=run_status)

    tutorial_parser = subparsers.add_parser("tutorial", help="Generate tutorial markdown")
    tutorial_parser.add_argument("--topics", nargs="*")
    tutorial_parser.add_argument("--level", choices=["beginner", "expert"], default="beginner")
    tutorial_parser.add_argument("--output-dir", default="tutorials")
    tutorial_parser.set_defaults(func=run_tutorial)

    summary_parser = subparsers.add_parser("summary", help="Generate a daily summary PDF")
    summary_parser.add_argument("input_json", nargs="?", default="sample_data.json")
    summary_parser.add_argument("output_pdf", nargs="?", default="output/daily_summary.pdf")
    summary_parser.set_defaults(func=run_summary)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        return run_status(args)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
