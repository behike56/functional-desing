from functional_py.main import main
import io
import sys

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "* password: kakarot1989\n* user: goku_fanatic\n"
