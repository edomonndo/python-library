# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/1/ITP1_1_A


def greedy1(A):
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += A[i] * A[j]
    return res


def greedy2(A):
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += min(A[i], A[j])
    return res


def greedy3(A):
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                res += A[i] * A[j] * A[k]
    return res


def greedy4(A):
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                res += min(A[i], A[j], A[k])
    return res


def greedy5(A):
    n = len(A)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += A[i] ^ A[j]
    return res


def greedy6(A):
    n = len(A)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += (A[i] - A[j]) ** 2
    return res


def greedy7(A):
    n = len(A)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += abs(A[i] - A[j])
    return res


if __name__ == "__main__":
    from other.typical_problems_of_sum import *

    import random

    testcase = 10
    for _ in range(testcase):
        n = 100
        A = [random.randrange(1, 10**9) for _ in range(n)]
        assert greedy1(A) == solve1(A)
        assert greedy2(A) == solve2(A)
        assert greedy3(A) == solve3(A)
        assert greedy4(A) == solve4(A)
        assert greedy5(A) == solve5(A)
        assert greedy6(A) == solve6(A)
        assert greedy7(A) == solve7(A)

    print("Hello World")
