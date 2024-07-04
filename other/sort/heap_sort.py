from heapq import *


def heap_sort(A: list[int]) -> list[int]:
    pq = heapify(A[:])
    n = len(A)
    return [heappop(pq) for _ in range(n)]
