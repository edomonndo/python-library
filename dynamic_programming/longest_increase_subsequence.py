def naive(A: list[int], less_than: bool = True) -> int:
    n = len(A)
    dp = [0] * n
    size = 0
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if less_than:
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            else:
                if A[j] <= A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        if size < dp[i]:
            size = dp[i]
    return size


def calc_lis(
    A: list[int], less_than: bool = True, restore: bool = False
) -> int | tuple[int, list[int]]:
    from bisect import bisect_left, bisect_right

    n = len(A)
    inf = float("inf")
    dp = [inf] * n
    if restore:
        prev = [-1] * n

    size = 0
    for i, a in enumerate(A):
        j = bisect_left(dp, a) if less_than else bisect_right(dp, a)
        if restore:
            prev[i] = j
        dp[j] = a
        if j + 1 > size:
            size = j + 1
    if not restore:
        return size

    res = [0] * size
    j = size - 1
    for i in reversed(range(n)):
        if prev[i] == j:
            res[j] = i
            j -= 1
    return size, res


def calc_lis_segtree(
    A: list[int], less_than: bool = True, restore: bool = False
) -> int | tuple[int, list[int]]:
    from atcoder.segtree import SegTree

    # 座標圧縮 1-indexed
    dic = {e: i for i, e in enumerate(sorted(set(A)), 1)}
    A2 = list(map(dic.__getitem__, A))

    n = len(A2)
    seg = SegTree(max, -1, [0] * (n + 1))
    if restore:
        prev = [-1] * n

    size = 0
    for i, a in enumerate(A2):
        j = seg.prod(0, a) if less_than else seg.prod(0, a + 1)
        if restore:
            prev[i] = j
        if seg.get(a) < j + 1:
            seg.set(a, j + 1)
            size = max(size, j + 1)
    if not restore:
        return size

    res = [0] * size
    j = size - 1
    for i in reversed(range(n)):
        if prev[i] == j:
            res[j] = i
            j -= 1
    return size, res
