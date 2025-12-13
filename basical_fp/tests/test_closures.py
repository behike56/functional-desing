from basical_fp import closures
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("hello world", 2),
        ("this is a test", 6),
        ("one", 7),
    ],
)
def test_word_count_aggregator(word, expected):
    aggregator = closures.word_count_aggregator()
    assert aggregator(word) == expected


@pytest.mark.parametrize(
    "docs, new_doc, expected",
    [
        (["doc1", "doc2"], ["doc1", "doc2", "doc3"]),
        (["doc1", "doc2"], ["doc1", "doc2", "doc3", "doc4"]),
        (
            ["doc1", "doc2"],
            ["doc1", "doc2", "doc3", "doc4"],
            ["doc1", "doc2", "doc3", "doc4"],
        ),
    ],
)
def test_new_collection(docs, new_doc, expected):
    add_doc = closures.new_collection(docs)
    assert add_doc("doc3") == expected
