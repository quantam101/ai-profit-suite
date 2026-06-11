from pathlib import Path

import main
from tutorial_generator import generate_tutorial_content


def test_status_command_runs(capsys):
    assert main.main(["status"]) == 0
    captured = capsys.readouterr().out
    assert "ai-profit-suite" in captured
    assert "ready" in captured


def test_tutorial_generation(tmp_path):
    assert main.main(["tutorial", "--topics", "AI automation", "--output-dir", str(tmp_path)]) == 0
    output = tmp_path / "beginner_tutorials.md"
    assert output.exists()
    assert "AI automation" in output.read_text(encoding="utf-8")


def test_tutorial_template_contains_steps():
    content = generate_tutorial_content("field dispatch", "beginner")
    assert "field dispatch" in content
    assert "1." in content
