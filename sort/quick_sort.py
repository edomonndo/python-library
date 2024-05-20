import sys

sys.setrecursionlimit(1000000)


def quick_sort(A: list[int]) -> list[int]:
    n = len(A)
    if n <= 1:
        return A
    pivot = A[n // 2]
    L, M, R = [], [], []
    for a in A:
        if a < pivot:
            L.append(a)
        elif a == pivot:
            M.append(a)
        else:
            R.append(a)
    return quick_sort(L) + M + quick_sort(R)
