from functional_py import closures


def test_word_count_aggregator():
    aggregator = closures.word_count_aggregator()
    assert aggregator("hello world") == 2
    assert aggregator("this is a test") == 6
    assert aggregator("one") == 7


def test_new_collection():
    initial_docs = ["doc1", "doc2"]
    add_doc = closures.new_collection(initial_docs)
    assert add_doc("doc3") == ["doc1", "doc2", "doc3"]
    assert add_doc("doc4") == ["doc1", "doc2", "doc3", "doc4"]
    assert initial_docs == ["doc1", "doc2"]
