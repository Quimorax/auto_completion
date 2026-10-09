import pytest
from main import autocomplete, create_parser


@pytest.fixture
def sample_words():
    """Fixture providing a sample word dictionary for testing."""
    return ["cat", "caterpillar", "category", "car", "cart", "dog", "catalog"]


def test_autocomplete_empty_query(sample_words):
    """Test that empty or whitespace queries return an empty result list."""
    assert autocomplete("", sample_words) == []
    assert autocomplete("   ", sample_words) == []


def test_autocomplete_exact_prefix_priority(sample_words):
    """Test that exact prefix matches take precedence and set is_exact_prefix flag."""
    results = autocomplete("cat", sample_words, min_similarity=0.5, top_n=5)

    assert len(results) > 0
    assert results[0]["word"] == "cat"
    assert results[0]["is_exact_prefix"] is True
    assert results[0]["similarity"] == 1.0

    # Ensure exact prefix matches are grouped before non-exact matches
    exact_flags = [r["is_exact_prefix"] for r in results]
    assert exact_flags == sorted(exact_flags, reverse=True)


def test_autocomplete_min_similarity_filtering(sample_words):
    """Test that candidates below min_similarity threshold are filtered out."""
    results = autocomplete("dog", sample_words, min_similarity=0.7, top_n=5)

    assert len(results) == 1
    assert results[0]["word"] == "dog"


def test_autocomplete_top_n_limit(sample_words):
    """Test that the number of returned suggestions does not exceed top_n limit."""
    results = autocomplete("ca", sample_words, min_similarity=0.1, top_n=3)
    assert len(results) == 3


def test_create_parser_defaults():
    """Test CLI argument parser default values."""
    parser = create_parser()
    args = parser.parse_args([])

    assert args.query == ""
    assert args.word == ""
    assert args.dict == "words.json"
    assert args.min_similarity == 0.5
    assert args.top_n == 5


def test_create_parser_custom_args():
    """Test CLI argument parser with explicitly provided custom parameters."""
    parser = create_parser()
    args = parser.parse_args([
        "cat",
        "--dict", "custom_words.json",
        "--min_similarity", "0.8",
        "--top-n", "10"
    ])

    assert args.query == "cat"
    assert args.dict == "custom_words.json"
    assert args.min_similarity == 0.8
    assert args.top_n == 10