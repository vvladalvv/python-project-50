import yaml
import json


def open_json_files(file1):
    data1 = json.load(open(file1))
    return data1


def open_yaml_files(file1):
    data1 = yaml.safe_load(open(file1))
    return data1


def check_formal_file(file):
    file_copy = file[:]
    result = ''
    for i in file_copy:
        if i == '.':
            result = ''
        result += i
    return result


def remove_empty_line(string):
    lines = string.split('\n')
    formatted_lines = []
    for line in lines:
        if line.strip():
            if ': ' in line:
                key, value = line.split(': ', 1)
                vsl = value.strip().lower()
                vsi = value.strip().isdigit()
                if vsl not in ['true', 'false'] and not vsi:
                    value = f'"{value.strip()}"'
                line = f"{key}: {value}"
            formatted_lines.append(line)
    return '\n'.join(formatted_lines)


def sort_files(file1, file2):
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    return all_keys
