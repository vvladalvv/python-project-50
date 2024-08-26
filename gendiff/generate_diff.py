import json

def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    # print(f'data1 = {data1}')
    # print(f'data2 = {data2}')
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    # print(f'all_keys = {all_keys}')
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
    # print(f'result перед return = {result}')
    return "{\n" + "\n".join(result) + "\n}"
