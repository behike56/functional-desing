from basical_fp import recursive
import pytest


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, 120),
        (0, 1),
        (1, 1),
    ],
)
def test_factorial_r(n, expected):
    assert recursive.factorial_r(n) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, [2, 3], [[4, 5], 6]], 21),
        ([], 0),
        ([1, 2, 3], 6),
    ],
)
def test_sum_nested_list(lst, expected):
    assert recursive.sum_nested_list(lst) == expected


@pytest.mark.parametrize(
    "document, expected",
    [
        ("this is a test sentence", "sentence"),
        ("one two three", "three"),
        ("", ""),
    ],
)
def test_find_longest_word(document, expected):
    assert recursive.find_longest_word(document) == expected


@pytest.mark.parametrize(
    "nested_documents, target_document_id, expected",
    [
        ({1: {3: {}}, 2: {}}, 3, 2),
        ({1: {3: {}}, 2: {}}, 1, 1),
        ({1: {3: {}}, 2: {}}, 4, -1),
    ],
)
def test_count_nested_levels(nested_documents, target_document_id, expected):
    assert (
        recursive.count_nested_levels(nested_documents, target_document_id) == expected
    )
