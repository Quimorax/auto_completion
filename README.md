# Auto-Complete CLI

A lightweight Python command-line tool for fuzzy prefix autocompletion using a **Longest Common Subsequence (LCS)** Dynamic Programming algorithm.

## ✨ Features

- **LCS Prefix Matching**: Compares input queries against word prefixes using Dynamic Programming.
- **Multi-Criteria Ranking**: Results are ordered hierarchically by:
  1. Exact prefix match priority
  2. LCS similarity score ($0.0$ to $1.0$)
  3. Word length penalty
- **JSON Dictionary**: Loads dictionary entries from standard JSON files
- **CLI Customization**: Configurable min similarity (`--min_similarity`) and result output limits (`--top-n`).
- **Unit Testing**: Includes unit tests for the core algorithm, CLI parser, and JSON utilities.

## 📁 Project Structure

```
auto_completion/
├── main.py                             # Core algorithm & CLI entry point
├── json_utilities.py                   # JSON loader & saver helpers
├── words.json                          # Dictionary data source
└── tests/                              # Test suite
    ├── test_json_utilities.py          # Tests for JSON utilities
    ├── test_longest_total_sequence.py  # Tests for LCS DP algorithm
    └── test_main.py                    # Tests for autocompletion and CLI parser
```

## 🚀 Quick Start

### Requirements
- Python 3.8+
- pytest

### Usage

Run autocompletion with a search query:

```cmd
python main.py <query>
```

#### Examples

**Basic query:**
```cmd 
python main.py cat
```

**Custom similarity threshold and limit:**
```cmd
python main.py cat --min_similarity 0.6 --top-n 3
```

#### CLI Options

| Argument | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `query` | `str` | `""` | Search word or prefix |
| `--min_similarity` | `float` | `0.5` | Minimum similarity score required ($0.0$ – $1.0$) |
| `--top-n` | `int` | `5` | Maximum number of suggestions to return |

## 🧪 Running Tests

Execute the unit test suite using `pytest` or Python's built-in `unittest`:

```cmd
# Using pytest
pytest

# Using standard unittest
python -m unittest discover tests
```