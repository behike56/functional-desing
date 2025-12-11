from functional_py import recursive


def test_factorial_r():
    assert recursive.factorial_r(5) == 120
    assert recursive.factorial_r(0) == 1
    assert recursive.factorial_r(1) == 1


def test_zipmap():
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    assert recursive.zipmap(keys, values) == {"a": 1, "b": 2, "c": 3}
    assert recursive.zipmap([], []) == {}
    assert recursive.zipmap(["a"], [1]) == {"a": 1}


def test_sum_nested_list():
    lst = [1, [2, 3], [[4, 5], 6]]
    assert recursive.sum_nested_list(lst) == 21
    assert recursive.sum_nested_list([]) == 0
    assert recursive.sum_nested_list([1, 2, 3]) == 6


def test_list_files():
    parent_directory = {
        "Documents": {
            "Proposal.docx": None,
            "Receipts": {
                "January": {"receipt1.txt": None, "receipt2.txt": None},
                "February": {"receipt3.txt": None},
            },
        },
    }
    expected = [
        "Documents/Proposal.docx",
        "Documents/Receipts/January/receipt1.txt",
        "Documents/Receipts/January/receipt2.txt",
        "Documents/Receipts/February/receipt3.txt",
    ]
    assert sorted(recursive.list_files(parent_directory)) == sorted(expected)


def test_find_longest_word():
    document = "this is a test sentence"
    assert recursive.find_longest_word(document) == "sentence"
    assert recursive.find_longest_word("one two three") == "three"
    assert recursive.find_longest_word("") == ""


def test_count_nested_levels():
    nested_documents = {1: {3: {}}, 2: {}}
    assert recursive.count_nested_levels(nested_documents, 3) == 2
    assert recursive.count_nested_levels(nested_documents, 1) == 1
    assert recursive.count_nested_levels(nested_documents, 2) == 1
    assert recursive.count_nested_levels(nested_documents, 4) == -1
