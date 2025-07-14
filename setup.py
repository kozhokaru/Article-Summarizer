# setup.py
from setuptools import setup, find_packages

setup(
    name="article-summarizer",
    version="0.1.0",
    description="CLI tool to fetch and AI-summarize web articles",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "python-dotenv",
        "openai"
    ],
    entry_points={
        "console_scripts": [
            "article-summarizer=article_summarizer.cli:main"
        ]
    }
)
