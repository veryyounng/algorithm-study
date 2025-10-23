def solution(data, ext, val_ext, sort_by):
    key_index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    filtered = list(filter(lambda x: x[key_index[ext]] < val_ext, data))

    sorted_data = sorted(filtered, key=lambda x: x[key_index[sort_by]])

    return sorted_data