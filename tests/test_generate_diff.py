from gendiff import generate_diff
import json


res = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_generate_diff_empty_and_filled_files():
    file_json1 = 'tests/fixtures/empty2.json'
    file_json2 = 'tests/fixtures/filepath1.json'
    file_yaml1 = 'tests/fixtures/empty2.yaml'
    file_yaml2 = 'tests/fixtures/filepath1.yaml'
    expected = '''{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
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


def test_generate_diff_flat():
    file_json1 = 'tests/fixtures/filepath1.json'
    file_json2 = 'tests/fixtures/filepath2.json'
    file_yaml1 = 'tests/fixtures/filepath1.yaml'
    file_yaml2 = 'tests/fixtures/filepath2.yaml'
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
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
    host: hexlet.io
    proxy: 123.234.53.22
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
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert result == expected


def test_generate_diff_nested_file_json_and_yaml():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.yaml'
    result2 = generate_diff(file1, file2)
    assert result2 == res


def test_generate_diff_plain_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    result = generate_diff(file1, file2, format_file='plain')
    result2 = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    assert result == result2


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
