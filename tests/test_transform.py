from functional_py import transform
import pytest


def test_get_logger(capsys):
    logger = transform.get_logger(transform.colon_delimit)
    logger("first", "second")
    captured = capsys.readouterr()
    assert captured.out == "first: second\n"

    logger = transform.get_logger(transform.dash_delimit)
    logger("first", "second")
    captured = capsys.readouterr()
    assert captured.out == "first - second\n"


def test_colon_delimit():
    assert transform.colon_delimit("a", "b") == "a: b"


def test_dash_delimit():
    assert transform.dash_delimit("a", "b") == "a - b"


def test_doc_format_checker_and_converter():
    checker = transform.doc_format_checker_and_converter(
        transform.capitalize_content, ["txt", "md"]
    )
    assert checker("file.txt", "hello") == "HELLO"
    with pytest.raises(ValueError, match="invalid file format"):
        checker("file.pdf", "hello")

    checker = transform.doc_format_checker_and_converter(
        transform.reverse_content, ["txt"]
    )
    assert checker("file.txt", "hello") == "olleh"


def test_capitalize_content():
    assert transform.capitalize_content("hello") == "HELLO"


def test_reverse_content():
    assert transform.reverse_content("hello") == "olleh"
