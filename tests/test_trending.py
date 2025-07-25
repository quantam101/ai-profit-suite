import os
import sys

# Ensure the project root is in the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import trending


def test_select_top_five():
    data = [i for i in range(10)]
    assert trending.select_top_five(data) == [0, 1, 2, 3, 4]


def test_fetch_etsy_without_key(monkeypatch):
    monkeypatch.delenv("ETSY_API_KEY", raising=False)
    assert trending.fetch_etsy_trending() == []
