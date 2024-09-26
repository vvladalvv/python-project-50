def formation_of_diff(f_1, f_2):
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
                        "value": formation_of_diff(f_1[key], f_2[key])
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
