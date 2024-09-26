from gendiff.parser import parse_file_json_or_yaml
from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json_format import json_format
from gendiff.files_to_diff import formation_of_diff


def generate_diff(file1, file2, format_file='stylish'):
    data1 = parse_file_json_or_yaml(file1)
    data2 = parse_file_json_or_yaml(file2)
    if data1 == {} and data2 == {}:
        return '{}'
    if format_file == 'stylish':
        return format_stylish(formation_of_diff(data1, data2))
    if format_file == 'plain':
        return format_plain(formation_of_diff(data1, data2))
    if format_file == 'json':
        return json_format(formation_of_diff(data1, data2))
    return formation_of_diff(data1, data2)
