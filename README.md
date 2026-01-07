# Programming Language Comparison

A side-by-side comparison of popular programming languages. Compare syntax and concepts across 21+ programming languages including Python, JavaScript, Rust, Java, Go, and more.

🌐 **Live Site**: [https://prog-lang-compare.netlify.app](https://prog-lang-compare.netlify.app)

## Features

- 🔍 **21+ Programming Languages**: Compare syntax across Python, JavaScript, Rust, Java, Go, TypeScript, Ruby, Swift, Kotlin, and more
- 📚 **108+ Programming Concepts**: From basic datatypes to advanced concepts
- 🎨 **Modern UI**: Dark mode support with beautiful syntax highlighting
- 🤖 **AI-Generated Content**: All explanations generated using OpenAI API
- ⚡ **2,500+ Static Pages**: SEO-optimized for search engines
- 📱 **Fully Responsive**: Works great on mobile, tablet, and desktop

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+ (for JavaScript tests)
- OpenAI API key (for content generation)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/srix/prog-lang-compare.git
   cd prog-lang-compare
   ```

2. **Set up Python environment**:
   ```bash
   # Using uv (recommended)
   uv venv .venv-3.11 --python 3.11
   source .venv-3.11/bin/activate
   uv pip install -r requirements.txt

   # Or using standard pip
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API keys**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API credentials
   ```

4. **Build the site**:
   ```bash
   ./build.sh
   ```

5. **Preview locally**:
   ```bash
   cd docs && python -m http.server 8000
   # Visit http://localhost:8000
   ```

## Testing

### Python Tests

Run tests for builder scripts:

```bash
# Activate virtual environment first
source .venv-3.11/bin/activate

# Run all tests
pytest

# Run with coverage
pytest --cov=builder --cov-report=html

# Run specific test file
pytest tests/test_helper.py

# View coverage report
open htmlcov/index.html
```

**Current Test Coverage**:
- ✅ 17 tests passing
- ✅ 100% coverage on `plccache.py`
- ✅ 89% coverage on `helper.py`

### JavaScript Tests

Run tests for frontend code:

```bash
# Install dependencies
npm install

# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch
```

See [TESTING.md](TESTING.md) for detailed testing documentation.

## Project Structure

```
.
├── builder/                    # Python build scripts
│   ├── main.py                # AI content generator
│   ├── generate_static_pages.py
│   ├── generate_sitemap.py
│   ├── helper.py              # Utility functions
│   └── plccache.py            # Cache management
├── docs/                      # GitHub Pages deployment
│   ├── index.html             # Main page
│   ├── script.js              # Frontend JavaScript
│   ├── styles.css             # Styling
│   ├── prog_lang_concepts.yaml
│   ├── prog_langs.yaml
│   └── concepts/              # 2,500+ static pages
├── tests/                     # Python tests
│   ├── test_helper.py
│   └── test_plccache.py
├── __tests__/                 # JavaScript tests
│   └── script.test.js
├── build.sh                   # One-command build script
├── requirements.txt           # Python dependencies
├── package.json               # JavaScript dependencies
└── TESTING.md                 # Testing guide
```

## Development Workflow

### Adding New Concepts

1. Edit `docs/prog_lang_concepts.yaml`:
   ```yaml
   NewCategory:
     NewConcept: "Explain {concept} in {lang} with examples."
   ```

2. Run the builder:
   ```bash
   python builder/main.py
   ```

3. Generate static pages:
   ```bash
   python builder/generate_static_pages.py
   ```

4. Or use the all-in-one script:
   ```bash
   ./build.sh
   ```

### Adding New Languages

1. Edit `docs/prog_langs.yaml`:
   ```yaml
   Programming Languages:
     - Python 3.10
     - Your New Language
   ```

2. Rebuild:
   ```bash
   ./build.sh
   ```

## Architecture

### Content Generation Pipeline

```
prog_lang_concepts.yaml + prog_langs.yaml
    ↓
builder/main.py (OpenAI API + caching)
    ↓
docs/content-autogen/gpt_3_5_turbo/{language}.json
    ↓
builder/generate_static_pages.py
    ↓
docs/concepts/{language}/{concept}.html (2,500+ pages)
    ↓
builder/generate_sitemap.py
    ↓
docs/sitemap.xml
```

### Key Features

- **Smart Caching**: Only regenerates content when prompts change
- **Concurrent API Calls**: Parallel processing for faster generation
- **SEO Optimized**: Meta tags, structured data, sitemap
- **Responsive Design**: Mobile-first with dark mode
- **Syntax Highlighting**: Custom themes for light and dark modes

## Technologies

### Backend
- **Python 3.11**: Build scripts
- **OpenAI API**: Content generation
- **PyYAML**: Configuration management
- **pytest**: Testing framework

### Frontend
- **Vanilla JavaScript**: No framework dependencies
- **jQuery & DataTables**: Interactive comparison table
- **Highlight.js**: Syntax highlighting
- **Marked.js**: Markdown rendering

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest && npm test`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Testing Guidelines

- Write tests for new utility functions
- Maintain >80% code coverage
- Run `pytest` before committing
- See [TESTING.md](TESTING.md) for detailed guidelines

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Content generated using OpenAI API
- UI inspired by modern developer tools
- Community contributions and feedback

## Links

- 🌐 [Live Website](https://prog-lang-compare.netlify.app)
- 📦 [GitHub Repository](https://github.com/srix/prog-lang-compare)
- 🐛 [Report Issues](https://github.com/srix/prog-lang-compare/issues)
- 📖 [Testing Guide](TESTING.md)

---

Made with ❤️ by the Programming Language Comparison community
