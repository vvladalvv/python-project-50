import yaml
import json


def parse_json_files(file):
    with open(file) as f:
        return json.load(f)


def parse_yaml_files(file):
    with open(file) as f:
        return yaml.safe_load(f)


def parse_file_json_or_yaml(file):
    if file.endswith('.json'):
        file_1 = parse_json_files(file)
    file_1 = parse_yaml_files(file)
    return file_1
