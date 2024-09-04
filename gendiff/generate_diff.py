import yaml
from gendiff.parser import open_json_files, open_yaml_files, check_formal_file, remove_empty_line, sort_files


def gen_diff(file_1, file_2):
    all_keys = sort_files(file_1, file_2)
    result = []
    if file_1 or file_2:
        for key in all_keys:
            if key not in file_1:
                result.append(f"  + {key}: {yaml.dump(file_2[key])}")
            elif key not in file_2:
                result.append(f"  - {key}: {yaml.dump(file_1[key])}")
            elif file_1[key] == file_2[key]:
                result.append(f"    {key}: {yaml.dump(file_1[key])}")
            else:
                result.append(f"  - {key}: {yaml.dump(file_1[key])}")
                result.append(f"  + {key}: {yaml.dump(file_2[key])}")
        res = "{\n" + "".join(result) + "\n}"
        ress = res.replace('...', '')
        return remove_empty_line(ress)
    return '{}'


def gen_diff_json_and_yaml(file1, file2):
    for _ in range(1):
        if file1.endswith('.yaml'):
            file_1 = open_yaml_files(file1)
        elif file1.endswith('yml'):
            file_1 = open_yaml_files(file1)
        elif file1.endswith('.json'):
            file_1 = open_json_files(file1)
    for _ in range(1):
        if file2.endswith('.yaml'):
            file_2 = open_yaml_files(file2)
        elif file2.endswith('yml'):
            file_2 = open_yaml_files(file2)
        elif file2.endswith('.json'):
            file_2 = open_json_files(file2)
    return gen_diff(file_1, file_2)


def gen_diff_two_json(file1, file2):
    data1 = open_json_files(file1)
    data2 = open_json_files(file2)
    return gen_diff(data1, data2)


def gen_diff_two_yaml(file1, file2):
    data1 = open_yaml_files(file1)
    data2 = open_yaml_files(file2)
    return gen_diff(data1, data2)


def generate_diff(file_path1, file_path2):
    format_file1 = check_formal_file(file_path1)
    format_file2 = check_formal_file(file_path2)
    if format_file1 == '.json' and format_file2 == '.json':
        return gen_diff_two_json(file_path1, file_path2)
    elif format_file1 == '.yml' and format_file2 == '.yml':
        return gen_diff_two_yaml(file_path1, file_path2)
    elif format_file1 == '.yaml' and format_file2 == '.yaml':
        return gen_diff_two_yaml(file_path1, file_path2)
    return gen_diff_json_and_yaml(file_path1, file_path2)
