def radix_sort(A: list[int], max_value: int) -> list[int]:
    n = len(A)
    mask = 0xFF
    tmp = [None] * n
    for bit in range(0, 32, 8):
        cnt = [0] * (max_value + 1)
        for i in range(n):
            cnt[A[i] >> bit & mask] += 1
        for i in range(max_value):
            cnt[i + 1] += cnt[i]
        for i in range(n - 1, -1, -1):
            j = A[i] >> bit & mask
            cnt[j] -= 1
            tmp[cnt[j]] = A[i]
        for i in range(n):
            A[i] = tmp[i]
    return A
