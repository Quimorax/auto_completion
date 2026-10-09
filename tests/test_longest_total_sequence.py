from main import find_longest_total_sequence


def test_exact_match():
    """Test exact matching between two identical strings."""
    assert find_longest_total_sequence("nice", "nice") == 4
    assert find_longest_total_sequence("python", "python") == 6


def test_empty_strings():
    """Test behavior with empty input strings."""
    assert find_longest_total_sequence("", "init") == 0
    assert find_longest_total_sequence("work", "") == 0
    assert find_longest_total_sequence("", "") == 0


def test_partial_match():
    """Test subsequence matching with character skips and typos."""
    assert find_longest_total_sequence("cat", "car") == 2
    assert find_longest_total_sequence("cat", "crate") == 3


def test_no_common_characters():
    """Test strings with no overlapping characters."""
    assert find_longest_total_sequence("abc", "xyz") == 0


def test_case_sensitivity():
    """Test case sensitivity for non-normalized input strings."""
    assert find_longest_total_sequence("bob", "BOB") == 0