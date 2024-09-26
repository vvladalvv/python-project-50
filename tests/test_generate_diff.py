from gendiff import generate_diff
import json


def test_generate_diff_empty_and_filled_files():
    file_json1 = 'tests/fixtures/empty2.json'
    file_json2 = 'tests/fixtures/filepath1.json'
    file_yaml1 = 'tests/fixtures/empty2.yaml'
    file_yaml2 = 'tests/fixtures/filepath1.yaml'
    with open('tests/fixtures/result_test/result_empty_and_filled.txt') as f:
        expected = f.read()
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == expected
    assert result_yaml == expected


def test_generate_diff_empty_files():
    file_json1 = 'tests/fixtures/empty1.json'
    file_json2 = 'tests/fixtures/empty2.json'
    file_yaml1 = 'tests/fixtures/empty1.yaml'
    file_yaml2 = 'tests/fixtures/empty2.yaml'
    expected = '{}'
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    result_json_and_yaml = generate_diff(file_json1, file_yaml1)
    assert result_json == expected
    assert result_yaml == expected
    assert result_json_and_yaml == expected


def test_generate_diff_same_format():
    file_json1 = 'tests/fixtures/filepath1.json'
    file_json2 = 'tests/fixtures/filepath2.json'
    file_yaml1 = 'tests/fixtures/filepath1.yaml'
    file_yaml2 = 'tests/fixtures/filepath2.yaml'
    with open('tests/fixtures/result_test/result_same_format.txt') as f:
        expected = f.read()
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == expected
    assert result_yaml == expected


def test_generate_diff_same_files():
    file_json1 = 'tests/fixtures/filepath1.json'
    file_json2 = 'tests/fixtures/filepath1_copy.json'
    file_yaml1 = 'tests/fixtures/filepath1.yaml'
    file_yaml2 = 'tests/fixtures/filepath1_copy.yaml'
    with open('tests/fixtures/result_test/result_same_file.txt') as f:
        expected = f.read()
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == expected
    assert result_yaml == expected


def test_generate_diff_json_and_yaml():
    file1_json = 'tests/fixtures/filepath1.json'
    file2_yaml = 'tests/fixtures/filepath2.yaml'
    result = generate_diff(file1_json, file2_yaml)
    with open('tests/fixtures/result_test/result_json_and_yaml.txt') as f:
        expected = f.read()
    assert result == expected


def test_generate_diff_nested_file_json_and_yaml():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.yaml'
    result = generate_diff(file1, file2)
    with open('tests/fixtures/result_test/result_stylish.txt') as f:
        res = f.read()
    assert result == res


def test_generate_diff_plain_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.yaml'
    result = generate_diff(file1, file2, format_file='plain')
    with open('tests/fixtures/result_test/result_plain.txt') as f:
        res = f.read()
    assert result == res


def test_generate_diff_json_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    result = generate_diff(file1, file2, format_file='json')
    parsed_result = json.loads(result)
    assert 'common' in parsed_result
    assert parsed_result['common']['status'] == 'children'
    assert 'follow' in parsed_result['common']['value']
    assert parsed_result['common']['value']['follow']['status'] == 'added'
    assert parsed_result['common']['value']['setting3']['status'] == 'updated'
    assert 'setting6' in parsed_result['common']['value']
    assert 'doge' in parsed_result['common']['value']['setting6']['value']
