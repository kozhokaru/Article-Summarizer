# article_summarizer/cli.py

import argparse
from .summarizer import summarize_url

def main():
    parser = argparse.ArgumentParser(
        description="Fetch an article and get an AI-powered summary."
    )
    parser.add_argument("url", help="URL of the article to summarize")
    parser.add_argument(
        "-o", "--output", help="File to write summary to (defaults to stdout)"
    )
    args = parser.parse_args()

    summary = summarize_url(args.url)

    if args.output:
        with open(args.output, "w") as f:
            f.write(summary)
        print(f"Summary saved to {args.output}")
    else:
        print("\n=== Summary ===\n")
        print(summary)
