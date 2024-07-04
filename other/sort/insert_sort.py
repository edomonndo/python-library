def insert_sort(A: list[int]) -> list[int]:
    n = len(A)
    for i in range(1, n):
        tmp = A[i]
        j = i - 1
        while j >= 0 and A[j] > tmp:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = tmp
    return A
