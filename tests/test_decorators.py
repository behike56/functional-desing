from functional_py import decorators
import pytest


def test_process_doc():
    result, counts = decorators.process_doc("doc1", "pdf")
    assert result == "Processing doc: 'doc1'. File Type: pdf"
    assert counts == {"pdf": 1}

    result, counts = decorators.process_doc("doc2", "pdf")
    assert result == "Processing doc: 'doc2'. File Type: pdf"
    assert counts == {"pdf": 2}

    result, counts = decorators.process_doc("doc3", "txt")
    assert result == "Processing doc: 'doc3'. File Type: txt"
    assert counts == {"pdf": 2, "txt": 1}


def test_args_logger(capsys):
    decorators.args_logger("arg1", "arg2", kwarg1="val1", kwarg2="val2")
    captured = capsys.readouterr()
    assert captured.out == "1. arg1\n2. arg2\n* kwarg1: val1\n* kwarg2: val2\n"


def test_configure_backups():
    assert decorators.configure_backups() == {
        "path": "~/backups",
        "prefix": "copy_",
        "extension": ".txt",
    }
    assert decorators.configure_backups(
        ("path", "/new/path"), ("prefix", "backup_")
    ) == {
        "path": "/new/path",
        "prefix": "backup_",
        "extension": ".txt",
    }


def test_configure_login():
    assert decorators.configure_login() == {
        "user": None,
        "password": None,
        "token": None,
    }
    assert decorators.configure_login(("user", "testuser"), ("token", "123")) == {
        "user": "testuser",
        "password": None,
        "token": "123",
    }
