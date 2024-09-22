import yaml
import json


def open_json_files(file1):
    data1 = json.load(open(file1))
    return data1


def open_yaml_files(file1):
    data1 = yaml.safe_load(open(file1))
    return data1


def open_file_json_or_yaml(file):
    if file.endswith('.json'):
        file_1 = open_json_files(file)
    file_1 = open_yaml_files(file)
    return file_1
