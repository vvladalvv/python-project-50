from gendiff import generate_diff


def test_generate_diff_empty_and_filled_files():
    file_json1 = 'tests/fixtures/empty2.json'
    file_json2 = 'tests/fixtures/filepath1.json'
    file_yaml1 = 'tests/fixtures/empty2.yaml'
    file_yaml2 = 'tests/fixtures/filepath1.yaml'
    expected = '''{
  + follow: false
  + host: "hexlet.io"
  + proxy: "123.234.53.22"
  + timeout: 50
}'''
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == expected
    assert result_yaml == expected


def test_generate_diff_empty_files():
    file_json1 = 'tests/fixtures/empty1.json'
    file_json2 = 'tests/fixtures/empty2.json'
    file_yaml1 = 'tests/fixtures/empty1.yaml'
    file_yaml2 = 'tests/fixtures/empty2.yaml'
    expected = '{}'  # '{\n\n}'
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    result_json_and_yaml = generate_diff(file_json1, file_yaml1)
    assert result_json == expected
    assert result_yaml == expected
    assert result_json_and_yaml == expected


def test_generate_diff_flat_json():
    file_json1 = 'tests/fixtures/filepath1.json'
    file_json2 = 'tests/fixtures/filepath2.json'
    file_yaml1 = 'tests/fixtures/filepath1.yaml'
    file_yaml2 = 'tests/fixtures/filepath2.yaml'
    expected = '''{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == expected
    assert result_yaml == expected


def test_generate_diff_same_files():
    file_json1 = 'tests/fixtures/filepath1.json'
    file_json2 = 'tests/fixtures/filepath1_copy.json'
    file_yaml1 = 'tests/fixtures/filepath1.yaml'
    file_yaml2 = 'tests/fixtures/filepath1_copy.yaml'
    expected = '''{
    follow: false
    host: "hexlet.io"
    proxy: "123.234.53.22"
    timeout: 50
}'''
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == expected
    assert result_yaml == expected


def test_generate_diff_json_and_yaml():
    file1_json = 'tests/fixtures/filepath1.json'
    file2_yaml = 'tests/fixtures/filepath2.yaml'
    result = generate_diff(file1_json, file2_yaml)
    expected = '''{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert result == expected
