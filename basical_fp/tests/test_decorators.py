from basical_fp import decorators
import pytest


@pytest.mark.parametrize(
    "doc, file_type, expected",
    [
        ("doc1", "pdf", ("Processing doc: 'doc1'. File Type: pdf", {"pdf": 1})),
        ("doc2", "pdf", ("Processing doc: 'doc2'. File Type: pdf", {"pdf": 2})),
        (
            "doc3",
            "txt",
            ("Processing doc: 'doc3'. File Type: txt", {"pdf": 2, "txt": 1}),
        ),
    ],
)
def test_process_doc(doc, file_type, expected):
    result, counts = decorators.process_doc(doc, file_type)
    assert result == expected[0]
    assert counts == expected[1]


@pytest.mark.parametrize(
    "args, expected",
    [
        (("arg1", "arg2"), "1. arg1\n2. arg2\n"),
        (("arg1", "arg2", "arg3"), "1. arg1\n2. arg2\n3. arg3\n"),
    ],
)
def test_args_logger(capsys, args, expected):
    decorators.args_logger(*args)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        (("arg1", "arg2"), "1. arg1\n2. arg2\n"),
        (("arg1", "arg2", "arg3"), "1. arg1\n2. arg2\n3. arg3\n"),
    ],
)
def test_args_logger_kwargs(capsys, args, expected):
    decorators.args_logger(*args)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        ((), {"path": "~/backups", "prefix": "copy_", "extension": ".txt"}),
        (
            ("path", "/new/path"),
            {"path": "/new/path", "prefix": "copy_", "extension": ".txt"},
        ),
    ],
)
def test_configure_backups(args, expected):
    assert decorators.configure_backups(*args) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        ((), {"user": None, "password": None, "token": None}),
        (("user", "testuser"), {"user": "testuser", "password": None, "token": None}),
    ],
)
def test_configure_login(args, expected):
    assert decorators.configure_login(*args) == expected
