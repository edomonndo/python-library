def tim_sort(A: list[int]) -> list[int]:
    def insert_sort(A: list[int], l: int = 0, r: int = None):
        if r is None:
            r = len(A)
        for i in range(l + 1, r):
            tmp = A[i]
            j = i - 1
            while j >= 0 and A[j] > tmp:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = tmp
        return

    def merge_sort(A: list[int], l: int, m: int, r: int):
        L, R = A[l : m + 1], A[m + 1 : r + 1]
        L.reverse()
        R.reverse()
        for i in range(l, r + 1):
            if len(L) == 0:
                A[i] = R.pop()
            elif len(R) == 0:
                A[i] = L.pop()
            elif L[-1] <= R[-1]:
                A[i] = L.pop()
            else:
                A[i] = R.pop()

    n = len(A)
    if n < 64:
        insert_sort(A)
        return A
    bucket_size = 64
    for l in range(0, n, bucket_size):
        r = min(l + bucket_size, n)
        insert_sort(A, l, r)
    size = 64
    while size < n:
        for l in range(0, n, 2 * size):
            m = min(n - 1, l + size - 1)
            r = min(n - 1, l + 2 * size - 1)
            merge_sort(A, l, m, r)
        size *= 2
    return A
