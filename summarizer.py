# article_summarizer/summarizer.py

import requests
from bs4 import BeautifulSoup

def fetch_article_text(url: str) -> str:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    # Naïve approach: join all <p> tags
    paragraphs = soup.find_all("p")
    return "\n\n".join(p.get_text() for p in paragraphs)

def summarize_url(url: str) -> str:
    article = fetch_article_text(url)
    # placeholder until AI integration
    return article[:500] + "...\n\n(…truncated…)"
