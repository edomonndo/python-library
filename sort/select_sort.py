def select_sort(A: list[int]) -> list[int]:
    n = len(A)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if A[j] < A[k]:
                k = j
        A[i], A[k] = A[k], A[i]
    return A
