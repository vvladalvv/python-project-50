import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    if data1 or data2:
        all_keys = sorted(set(data1.keys()) | set(data2.keys()))
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
