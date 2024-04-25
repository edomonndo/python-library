def solve1(A):
    n = len(A)
    Sn = sum(A)
    res = Si = 0
    for i in range(n - 1):
        Si += A[i]
        res += A[i] * (Sn - Si)
    return res


def solve2(A):
    n = len(A)
    res = 0
    for i, a in enumerate(sorted(A), 1):
        res += a * (n - i)
    return res


def solve3(A):
    n = len(A)
    Sn1 = Tn1 = 0
    for i in range(n - 1):
        Sn1 += A[i]
        Tn1 += A[i] * Sn1
    Sn = Sn1 + A[n - 1]
    Si = Ti = 0
    res = 0
    for i in range(n - 2):
        Si += A[i]
        Ti += A[i] * Si
        res += A[i] * (Sn * (Sn1 - Si) - (Tn1 - Ti))
    return res


def solve4(A):
    n = len(A)
    res = 0
    for i, a in enumerate(sorted(A), 1):
        res += a * (n - i) * (n - 1 - i) // 2
    return res


def solve5(A):
    n = len(A)
    cnt = [0] * 31
    for a in A:
        for k in range(31):
            if a >> k & 1:
                cnt[k] += 1
    res = 0
    for i, a in enumerate(A, 1):
        for k in range(31):
            if a >> k & 1:
                cnt[k] -= 1
                res += (n - i - cnt[k]) * (1 << k)
            else:
                res += cnt[k] * (1 << k)
    return res


def solve6(A):
    n = len(A)
    Sn = sum(A)
    Tn = sum(a**2 for a in A)
    res = 0
    Si = Ti = 0
    for i, a in enumerate(A, 1):
        Si += a
        Ti += a**2
        res += a * a * (n - i) - 2 * a * (Sn - Si) + Tn - Ti
    return res
