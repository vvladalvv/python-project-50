def formater_plain(val):
    if isinstance(val, dict):
        return '[complex value]'
    elif isinstance(val, bool):
        return "false" if val is False else "true"
    elif val is None:
        return 'null'
    return f"'{val}'"


def find_path(tree, target, current_path=""):
    if isinstance(tree, dict):
        if target in tree:
            return f"{current_path}.{target}" if current_path else target
        for key, value in tree.items():
            new_path = f"{current_path}.{key}" if current_path else key
            if key == 'value' and isinstance(value, dict):
                result = find_path(value, target, current_path)
            else:
                result = find_path(value, target, new_path)
            if result:
                return result
    return None


def plain(diff):
    lines = []

    def walk(value):
        for key, val in value.items():
            status = val['status']
            if status == 'added':
                val_ = formater_plain(val['value'])
                res = (
                    f"Property '{find_path(diff, key)}' "
                    f"was added with value: {val_}"
                )
                lines.append(res)
            if status == 'updated':
                old = formater_plain(val['old_value'])
                new = formater_plain(val['new_value'])
                res = (
                    f"Property '{find_path(diff, key)}' "
                    f"was updated. From {old} to {new}"
                )
                lines.append(res)
            if status == 'removed':
                lines.append(f"Property '{find_path(diff, key)}' was removed")
            if status == 'children':
                walk(val['value'])
        return "\n".join(lines)
    return walk(diff)
