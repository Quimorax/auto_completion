import json
import os
from typing import List


def load_words_from_json(file_path: str) -> List[str]:
    """Load words list from JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File path not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, list):
        return [str(word).strip().lower() for word in data if word]
    elif isinstance(data, dict):
        return [str(word).strip().lower() for word in data.keys() if word]
    else:
        raise ValueError("Incorrect JSON structure")


def save_words_to_json(words: List[str], file_path: str) -> None:
    """Save words list to JSON file."""
    clean_words = sorted(list({str(word).strip().lower() for word in words if word}))
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(clean_words, file, ensure_ascii=False, indent=2)
