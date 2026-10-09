"""Auto-complete with dynamic program method."""

import argparse
from typing import List, Dict, Any
from json_utilities import load_words_from_json

__version__ = '1.0.1'


def create_parser() -> argparse.ArgumentParser:
    """Create parser that processes command-line parameters."""
    parser = argparse.ArgumentParser(
        prog='auto-complete',
        description="Auto-complete performed using dynamic program method with command line support.",
        epilog=f"auto-complete {__version__} (C) October 2026 Quimorax"
    )
    parser.add_argument('query', type=str, nargs='?', default="", help="Input word or prefix.")
    parser.add_argument("--min_similarity", type=float, default=0.5, help="Minimum similarity threshold (0.0 to 1.0).")
    parser.add_argument("--top-n", type=int, default=5, help="Number of suggestions to display.")
    return parser


def find_longest_total_sequence(user_word: str, file_word: str) -> int:
    """Find the length of the longest common subsequence using dynamic programming."""
    m, n = len(file_word), len(user_word)
    if m == 0 or n == 0:
        return 0

    # matrix of size (m + 1) x (n + 1) to avoid negative index lookup bug
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if file_word[i - 1] == user_word[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[m][n]


def autocomplete(
    query: str,
    words: List[str],
    min_similarity: float = 0.5,
    top_n: int = 5
) -> List[Dict[str, Any]]:
    """Generates autocompletion suggestions using dynamic programming LCS."""
    normalized_query = query.strip().lower()
    if not normalized_query:
        return []

    q_len = len(normalized_query)
    results = []

    for word in words:
        normalized_word = word.strip().lower()
        if not normalized_word:
            continue

        is_exact_prefix = normalized_word.startswith(normalized_query)

        # Compare query with the prefix of target word of matching length
        target_prefix = normalized_word[:q_len]
        lcs_length = find_longest_total_sequence(normalized_query, target_prefix)
        similarity = lcs_length / max(q_len, len(target_prefix))

        if is_exact_prefix or similarity >= min_similarity:
            results.append({
                "word": normalized_word,
                "similarity": round(similarity, 4),
                "is_exact_prefix": is_exact_prefix,
                "_len_penalty": -abs(len(normalized_word) - q_len)
            })

    # Sort by exact prefix, similarity, and length
    results.sort(
        key=lambda x: (x["is_exact_prefix"], x["similarity"], x["_len_penalty"]),
        reverse=True
    )

    # Clean up internal key
    for res in results[:top_n]:
        res.pop("_len_penalty", None)

    return results[:top_n]


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    query = args.query
    if not query:
        print("Error: please specify a query for autocompletion.")
        parser.print_help()
        return

    try:
        words = load_words_from_json("words.json")
    except FileNotFoundError:
        print(f"Error: dictionary 'words.json' not found.")
        return

    suggestions = autocomplete(
        query=query,
        words=words,
        min_similarity=args.min_similarity,
        top_n=args.top_n
    )

    print(f"\nQuery: '{query}' (minimum similarity: {args.min_similarity})")
    print("-" * 50)
    if not suggestions:
        print("No suggestions found.")
        return

    print(f"{'#':<3} | {'Word':<20} | {'Similarity':<10} | {'Exact Prefix'}")
    print("-" * 50)
    for i, res in enumerate(suggestions, 1):
        flag = "Yes" if res["is_exact_prefix"] else "No"
        print(f"{i:<3} | {res['word']:<20} | {res['similarity']:<10} | {flag}")


if __name__ == "__main__":
    main()