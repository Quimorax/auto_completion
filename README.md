# Auto-Complete CLI

Python CLI tool for word autocompletion.

Instead of relying on rigid exact matches, it uses Dynamic Programming (**Longest Common Subsequence**) to forgive typos and rank suggestions intelligently.

## ⚡ How It Works

When you type a query, the tool scans `words.json` and ranks candidates based on three rules:
1. **Exact prefix match** — words starting with your exact query always come first.
2. **Similarity score** — calculated via LCS against the word's prefix ($0.0$ to $1.0$).
3. **Length proximity** — shorter, closer matches are favored over long words.

## 🚀 Usage

Requires **Python 3.8+**. No external packages needed to run the CLI.

```bash
# Basic search
python main.py cat

# Custom minimum similarity and result limit
python main.py cat --min_similarity 0.6 --top-n 3
```

**Example Output:**
```text
Query: 'cat' (minimum similarity: 0.6)
--------------------------------------------------
#   | Word                 | Similarity | Exact Prefix
--------------------------------------------------
1   | cat                  | 1.0        | Yes
2   | catch                | 1.0        | Yes
3   | category             | 1.0        | Yes
```

### Options

| Argument | Default | Description |
| :--- | :--- | :--- |
| `query` | `""` | Word or prefix to autocomplete. |
| `--min_similarity` | `0.5` | Minimum LCS score required ($0.0$ – $1.0$). |
| `--top-n` | `5` | Maximum number of suggestions to show. |

## 🧪 Testing

The core algorithm, CLI parser, and JSON loaders are covered by unit tests. To run them, install `pytest` and execute:

```bash
pytest
```