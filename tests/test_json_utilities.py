import pytest
import json
from json_utilities import load_words_from_json


def test_load_words_from_json_list(tmp_path):
    """Test loading and normalizing a list of words from a JSON file."""
    json_file = tmp_path / "test_words.json"
    json_file.write_text(json.dumps(["Cat", "DOG", "  Apple  "]), encoding="utf-8")

    words = load_words_from_json(str(json_file))
    assert words == ["cat", "dog", "apple"]


def test_load_words_from_json_file_not_found():
    """Test that FileNotFoundError is raised when the dictionary file is missing."""
    with pytest.raises(FileNotFoundError):
        load_words_from_json("non_existent_file.json")
