import pytest
from gendiff import generate_diff


def test_generate_diff_empty_and_filled_files():
    file1 = 'tests/fixtures/empty2.json'
    file2 = 'tests/fixtures/filepath1.json'
    expected = '''{
  + follow: false
  + host: "hexlet.io"
  + proxy: "123.234.53.22"
  + timeout: 50
}'''
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_empty_files():
    file1 = 'tests/fixtures/empty1.json'
    file2 = 'tests/fixtures/empty2.json'
    expected = '{}' #'{\n\n}'
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_flat_json():
    file1 = 'tests/fixtures/filepath1.json'
    file2 = 'tests/fixtures/filepath2.json'
    expected = '''{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_same_files():
    file1 = 'tests/fixtures/filepath1.json'
    file2 = 'tests/fixtures/filepath1_copy.json'
    expected = '''{
    follow: false
    host: "hexlet.io"
    proxy: "123.234.53.22"
    timeout: 50
}'''
    result = generate_diff(file1, file2)
    assert result == expected
