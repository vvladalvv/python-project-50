import json
import yaml


def sort_files(file1, file2):
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    return all_keys


def open_json_files(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))
    return data1, data2


def open_yaml_files(file1, file2):
    data1 = yaml.safe_load(open(file1))
    data2 = yaml.safe_load(open(file2))
    return data1, data2


def check_formal_file(file):
    file_copy = file[:]
    result = ''
    for i in file_copy:
        if i == '.':
            result = ''
            continue
        result += i
    return result


def gen_diff_two_json(file1, file2):
    data1, data2 = open_json_files(file1, file2)
    if data1 or data2:
        all_keys = sort_files(data1, data2)
        result = []
        for key in all_keys:
            if key not in data1:
                result.append(f"  + {key}: {json.dumps(data2[key])}")
            elif key not in data2:
                result.append(f"  - {key}: {json.dumps(data1[key])}")
            elif data1[key] == data2[key]:
                result.append(f"    {key}: {json.dumps(data1[key])}")
            else:
                result.append(f"  - {key}: {json.dumps(data1[key])}")
                result.append(f"  + {key}: {json.dumps(data2[key])}")
        return "{\n" + "\n".join(result) + "\n}"
    return '{}'


def remove_empty_line(string):
    lines = string.split('\n')
    formatted_lines = []
    for line in lines:
        if line.strip():
            if ': ' in line:
                key, value = line.split(': ', 1)
                if not value.strip().lower() in ['true', 'false'] and not value.strip().isdigit():
                    value = f'"{value.strip()}"'
                line = f"{key}: {value}"
            formatted_lines.append(line)
    return '\n'.join(formatted_lines)


def gen_diff_two_yaml(file1, file2):
    data1, data2 = open_yaml_files(file1, file2)
    if data1 or data2:
        all_keys = sort_files(data1, data2)
        result = []
        for key in all_keys:
            if key not in data1:
                result.append(f"  + {key}: {yaml.dump(data2[key])}")
            elif key not in data2:
                result.append(f"  - {key}: {yaml.dump(data1[key])}")
            elif data1[key] == data2[key]:
                result.append(f"    {key}: {yaml.dump(data1[key])}")
            else:
                result.append(f"  - {key}: {yaml.dump(data1[key])}")
                result.append(f"  + {key}: {yaml.dump(data2[key])}")
        res = "{\n" + "".join(result) + "}"
        ress = res.replace('...', '')
        return remove_empty_line(ress)# return "{\n" + "".join(result) + "}".replace('...', '\n')
    return '{}'


def generate_diff(file_path1, file_path2):
    format_file1 = check_formal_file(file_path1)
    print(f'format_file1 = {format_file1}')
    format_file2 = check_formal_file(file_path2)
    if format_file1 == 'json' and format_file2 == 'json':
        return gen_diff_two_json(file_path1, file_path2)
    elif format_file1 == 'yaml' and format_file2 == 'yaml':
        return gen_diff_two_yaml(file_path1, file_path2)
    
        # data1, data2 = open_json_files(file_path1, file_path2)
        # if data1 or data2:
        #     all_keys = sort_json_files(data1, data2)
        #     result = []
        #     for key in all_keys:
        #         if key not in data1:
        #             result.append(f"  + {key}: {json.dumps(data2[key])}")
        #         elif key not in data2:
        #             result.append(f"  - {key}: {json.dumps(data1[key])}")
        #         elif data1[key] == data2[key]:
        #             result.append(f"    {key}: {json.dumps(data1[key])}")
        #         else:
        #             result.append(f"  - {key}: {json.dumps(data1[key])}")
        #             result.append(f"  + {key}: {json.dumps(data2[key])}")
        #     return "{\n" + "\n".join(result) + "\n}"
        # return '{}'
