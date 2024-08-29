import sys
import pytest
from gendiff.scripts.gendiff import main


def test_parser_with_missing_files():
    sys.argv = ['gendiff']
    with pytest.raises(SystemExit):
        main()


def test_help_output(capsys):
    sys.argv = ['gendiff', '--help']
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    result = 'Compares two configuration files and shows a difference.'
    assert result in captured.out
