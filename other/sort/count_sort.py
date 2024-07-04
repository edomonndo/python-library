def count_sort(A: list[int], max_value: int) -> list[int]:
    cnt = [0] * (max_value + 1)
    n = len(A)
    for a in A:
        cnt[a] += 1
    for i in range(max_value):
        cnt[i + 1] += cnt[i]
    res = [None] * n
    for i in range(n - 1, -1, -1):
        cnt[A[i]] -= 1
        res[cnt[A[i]]] = A[i]
    return res
