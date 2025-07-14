# tests/test_summarizer.py

import pytest
from article_summarizer.summarizer import fetch_article_text, call_openai, summarize_url
from unittest.mock import patch

def test_fetch_article_text(monkeypatch):
    html = "<html><body><p>First.</p><p>Second.</p></body></html>"
    class Dummy:
        text = html
        status_code = 200
        def raise_for_status(self): pass
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: Dummy())
    text = fetch_article_text("http://example.com")
    assert "First." in text and "Second." in text

@patch("article_summarizer.summarizer.openai.ChatCompletion.create")
def test_call_openai(mock_create):
    mock_create.return_value = type("X", (), {"choices": [{"message": {"content": "Got it"}}]})
    out = call_openai("Hello")
    assert out == "Got it"

@patch("article_summarizer.summarizer.call_openai")
def test_summarize_url(mock_call):
    mock_call.return_value = "Summary!"
    # also patch fetch_article_text to avoid HTTP
    with patch("article_summarizer.summarizer.fetch_article_text", return_value="Text"):
        out = summarize_url("url")
    assert out == "Summary!"
