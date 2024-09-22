def formater(val):
    if isinstance(val, bool):
        return " false" if val is False else " true"
    elif val == "":
        return ""
    elif val is None:
        return " null"
    else:
        return f" {val}"


def get_indent(depth, indent_value=" ", indent_space=4, offset=0):
    return indent_value * (indent_space * depth - offset)


def process_dict(dictt, depth=1):
    if isinstance(dictt, dict):
        lines = ["{"]

        def walk(di):
            nonlocal depth
            for key, val in di.items():
                if isinstance(val, dict):
                    depth += 1
                    lines.append(f"{get_indent(depth)}{key}: {{")
                    walk(val)
                    depth -= 1
                else:
                    lines.append(f"{get_indent(depth+1)}{key}: {val}")
            lines.append(f"{get_indent(depth)}}}")
        walk(dictt)
        return '\n'.join(lines)
    return dictt


def stringify(diff):
    lines = ["{"]

    def walk(diff_dict, depth=1):
        for key, val in diff_dict.items():
            status = val['status']
            if status == 'added':
                value = formater(process_dict(val['value'], depth))
                lines.append(f"{get_indent(depth, offset=2)}+ {key}:{value}")
            if status == "children":
                lines.append(f"{get_indent(depth)}{key}: {{")
                walk(val['value'], depth + 1)
            if status == 'updated':
                new = formater(process_dict(val['new_value'], depth))
                old = formater(process_dict(val['old_value'], depth))
                lines.append(f"{get_indent(depth, offset=2)}- {key}:{old}")
                lines.append(f"{get_indent(depth, offset=2)}+ {key}:{new}")
            if status == 'unchanged':
                value = formater(process_dict(val['value'], depth + 1))
                lines.append(f"{get_indent(depth, offset=2)}  {key}:{value}")
            if status == 'removed':
                value = formater(process_dict(val['value'], depth))
                lines.append(f"{get_indent(depth, offset=2)}- {key}:{value}")
        lines.append(f'{get_indent(depth-1)}}}')
    walk(diff)
    return '\n'.join(lines)
