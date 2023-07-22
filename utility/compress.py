def compress_to_dict(arr):
    return {e: i for i, e in enumerate(sorted(set(arr)))}


def compress_to_list(arr):
    # 0-index
    return list(map({e: i for i, e in enumerate(sorted(set(arr)), 0)}.__getitem__, arr))


def compress(arr):
    dic = {e: i for i, e in enumerate(sorted(set(arr)))}
    lst = list(map(dic.__getitem__, arr))
    return dic, lst


if __name__ == "__main__":
    # １次元
    A = [4, 90, 25, 30, 30, 8, 90, 90]
    dic = compress_to_dict(A)
    lst = compress_to_list(A)
    assert dic == {4: 0, 8: 1, 25: 2, 30: 3, 90: 4}
    assert lst == [0, 4, 2, 3, 3, 1, 4, 4], lst
    assert compress(A) == (dic, lst)
