# article_summarizer/summarizer.py

import requests
from bs4 import BeautifulSoup
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # reads .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return resp.choices[0].message.content.strip()

def summarize_url(url: str) -> str:
    article = fetch_article_text(url)
    prompt = (
        "Summarize the following article in 3–5 bullet points, "
        "each no more than 30 words:\n\n" + article
    )
    return call_openai(prompt)

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
