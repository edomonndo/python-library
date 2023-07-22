def next_permutation(a: list, l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(a) - 1
    for i in range(r - 1, l - 1, -1):
        if a[i] < a[i + 1]:
            for j in range(r, i, -1):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False


def prev_permutation(a: list, l: int = 0, r: int = None) -> bool:
    if r is None:
        r = len(a) - 1
    for i in range(r - 1, l - 1, -1):
        if a[i] > a[i + 1]:
            for j in range(r, i, -1):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    p, q = i + 1, r
                    while p < q:
                        a[p], a[q] = a[q], a[p]
                        p += 1
                        q -= 1
                    return True
    return False


import bisect


def nth_permutations(A: list, MOD: int = 10**18):
    """
    順列のうちaとなるのは何番目か？
    返り値は0-indexed
    """
    n = len(A)
    fact = [1]
    for i in range(n - 1):
        x = (fact[-1] * (i + 1)) % MOD
        fact.append(x)
    B = []
    ans = 0
    for i in range(n - 1):
        a = A[i]
        k = bisect.bisect(B, a)
        B.insert(k, a)
        a1 = a - 1 - k
        ans += a1 * fact[n - 1 - i]
        ans %= MOD
    return ans


if __name__ == "__main__":
    n = 3
    a = [0, 1, 2]
    res = []
    while True:
        res.append(a[:])
        if not next_permutation(a, 0, n - 1):
            break
    assert res == [
        [0, 1, 2],
        [0, 2, 1],
        [1, 0, 2],
        [1, 2, 0],
        [2, 0, 1],
        [2, 1, 0],
    ], res

    a = [2, 1, 0]
    res = []
    while True:
        res.append(a[:])
        if not prev_permutation(a, 0, n - 1):
            break
    assert res == [
        [2, 1, 0],
        [2, 0, 1],
        [1, 2, 0],
        [1, 0, 2],
        [0, 2, 1],
        [0, 1, 2],
    ], res

    n = 3
    a = [3, 1, 5, 4, 2]
    assert nth_permutations(a) == 53
