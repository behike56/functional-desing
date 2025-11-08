from functional_py import main


def test_change_bullet_style():
    document = "- line 1\n- line 2\n* line 3"
    expected = "* line 1\n* line 2\n* line 3"
    assert main.change_bullet_style(document) == expected


def test_convert_line():
    assert main.convert_line("- line") == "* line"
    assert main.convert_line("* line") == "* line"
    assert main.convert_line("line") == "line"


def test_remove_invalid_lines():
    document = "- line 1\n* line 2\n- line 3\nline 4"
    expected = "* line 2\nline 4"
    assert main.remove_invalid_lines(document) == expected


def test_is_start_with_asta():
    assert main.is_start_with_asta("* line") is True
    assert main.is_start_with_asta("- line") is False
    assert main.is_start_with_asta("line") is True


def test_join_first_sentences():
    sentences = ["hello", "world", "this", "is", "a", "test"]
    assert main.join_first_sentences(sentences, 3) == "helloworldthis"
    assert main.join_first_sentences(sentences, 1) == "hello"
    assert main.join_first_sentences(sentences, 0) == ""
from functional_py.main import main
import io
import sys

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "* password: kakarot1989\n* user: goku_fanatic\n"
