import sys

sys.setrecursionlimit(1000000)


def merge_sort(A: list[int]) -> list[int]:
    n = len(A)
    if n <= 1:
        return A
    m = n >> 1
    L = merge_sort(A[:m])
    R = merge_sort(A[m:])
    res = []
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    if i < len(L):
        res += L[i:]
    if j < len(R):
        res += R[j:]
    return res
