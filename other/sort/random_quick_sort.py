from random import randrange
import sys

sys.setrecursionlimit(1000000)


def quick_sort(A: list[int]) -> list[int]:
    n = len(A)
    if n <= 1:
        return A
    x = randrange(0, n)
    pivot = A[x]
    L, R = [], []
    for i, a in enumerate(A):
        if i == x:
            continue
        if a < pivot:
            L.append(a)
        elif a > pivot:
            R.append(a)
        elif randrange(0, 2) == 1:
            L.append(a)
        else:
            R.append(a)

    return quick_sort(L) + pivot + quick_sort(R)
