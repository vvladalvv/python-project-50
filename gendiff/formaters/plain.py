def process_value(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, bool):
        return "false" if val is False else "true"
    elif isinstance(val, int):
        return f"{val}"
    elif val is None:
        return 'null'
    else:
        return f"'{val}'"


def find_path(tree, target, current_path="", found_paths=None):
    if found_paths is None:
        found_paths = set()
    if isinstance(tree, dict):
        if target in tree:
            path = f"{current_path}.{target}" if current_path else target
            if path not in found_paths:
                found_paths.add(path)
                return path
        for key, value in tree.items():
            if key in ['old_value', 'new_value']:
                continue
            new_path = f"{current_path}.{key}" if current_path else key
            if key == 'value' and isinstance(value, dict):
                result = find_path(value, target, current_path, found_paths)
            else:
                result = find_path(value, target, new_path, found_paths)
            if result:
                return result
    return None


def format_plain(diff):
    lines = []
    found_paths = set()

    def walk(value):
        for key, val in value.items():
            status = val['status']
            path = find_path(diff, key, found_paths=found_paths)
            if path:
                if status == 'added':
                    val_ = process_value(val['value'])
                    res = (
                        f"Property '{path}' "
                        f"was added with value: {val_}"
                    )
                    lines.append(res)
                elif status == 'updated':
                    old = process_value(val['old_value'])
                    new = process_value(val['new_value'])
                    res = (
                        f"Property '{path}' "
                        f"was updated. From {old} to {new}"
                    )
                    lines.append(res)
                elif status == 'removed':
                    lines.append(f"Property '{path}' was removed")
            if status == 'children':
                walk(val['value'])
        return "\n".join(lines)
    return walk(diff)
