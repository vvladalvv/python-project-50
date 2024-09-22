from gendiff.parser import open_file_json_or_yaml
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json_format import json_format


def generate_diff(file1, file2, format_file='stylish'):
    data1 = open_file_json_or_yaml(file1)
    data2 = open_file_json_or_yaml(file2)
    if data1 == {} and data2 == {}:
        return '{}'

    def walk(f_1, f_2):
        result = {}
        all_keys = sorted(set(f_1.keys()) | set(f_2.keys()))
        for key in all_keys:
            if key in f_1 and key in f_2:
                if f_2[key] != f_1[key]:
                    check_form_f_1 = isinstance(f_1[key], dict)
                    check_form_f_2 = isinstance(f_2[key], dict)
                    if check_form_f_1 and check_form_f_2:
                        result[key] = {
                            "status": "children",
                            "value": walk(f_1[key], f_2[key])
                        }
                    else:
                        result[key] = {
                            "status": "updated",
                            "old_value": f_1[key],
                            "new_value": f_2[key]
                        }
                else:
                    result[key] = {"status": 'unchanged', 'value': f_1[key]}
            elif key in f_1 and key not in f_2:
                result[key] = {"status": "removed", "value": f_1[key]}
            else:
                result[key] = {"status": "added", "value": f_2[key]}
        return result
    if format_file == 'stylish':
        return stylish(walk(data1, data2))
    if format_file == 'plain':
        return plain(walk(data1, data2))
    if format_file == 'json':
        return json_format(walk(data1, data2))
    return walk(data1, data2)
