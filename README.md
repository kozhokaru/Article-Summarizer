# Article-Summarizer

A simple, configurable CLI tool that fetches any web article and uses OpenAI’s GPT model to generate a concise summary.

## Features

- **Fetch & Extract**: Downloads the page and extracts main text by joining all `<p>` tags
- **AI Summarization**: Generates 3–5 bullet points (≤30 words each) using the OpenAI API
- **CLI Interface**: Handy command-line tool with optional file output
- **Testing**: Fully tested with `pytest` and mocks for reliable CI
- **CI/CD**: GitHub Actions workflow for automated testing on push and PR
- **Packaging**: Installable via `pip` and exposes a `article-summarizer` console script

## Prerequisites

- Python 3.9 or higher
- An OpenAI API key (set in a `.env` file)

## Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/kozhokaru/article-summarizer.git
   cd article-summarizer
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**\
   Create a `.env` file in the project root:

   ```text
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Summarize to stdout

```bash
article-summarizer https://example.com/some-article
```

### Summarize and save to file

```bash
article-summarizer https://example.com/some-article -o summary.txt
```

## Running Tests

All core functionality is covered by unit tests. To run them:

```bash
pytest
```

## Continuous Integration

A GitHub Actions workflow is provided at `.github/workflows/ci.yml`. It will:

- Check out your code
- Set up Python (3.9, 3.10, 3.11)
- Install dependencies
- Run `pytest`

## Packaging & Distribution

The project is configured with `setup.py`. Once published to PyPI, you can install via:

```bash
pip install article-summarizer
```

And invoke the tool with:

```bash
article-summarizer <URL>
```

## Logging & Error Handling

- Uses Python’s `logging` module to report fetch errors
- CLI will exit with an error code and message if something goes wrong

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -m "feat: add foo"`)
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request

Please ensure new features include tests and adhere to the existing style.

## License

MIT © Lev Kozhokaru
