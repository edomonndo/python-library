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

MOD = 998244353


def get_permutation_order(A: list):
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


def kth_permutation(n: int, k: int) -> list:
    """
    0<=i<nからなる順列のk番目を返す. kは0-indexed
    """
    tmp = [i for i in range(n)]

    surplus = [-1] * n
    for i in range(1, n):
        surplus[n - i] = k % i
        k = k // i
    surplus[0] = k

    res = [-1] * n
    for i in range(n):
        res[i] = tmp[surplus[i]]
        for j in range(surplus[i], n - 1):
            tmp[j] = tmp[j + 1]
    return res
