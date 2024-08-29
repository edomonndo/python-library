def compress_to_dict(arr):
    return {e: i for i, e in enumerate(sorted(set(arr)))}


def compress_tolist(arr):
    # 0-index
    return list(map({e: i for i, e in enumerate(sorted(set(arr)), 0)}.__getitem__, arr))


def compress(arr):
    dic = {e: i for i, e in enumerate(sorted(set(arr)))}
    lst = list(map(dic.__getitem__, arr))
    return dic, lst
