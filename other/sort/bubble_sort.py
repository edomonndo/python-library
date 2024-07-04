def bubble_sort(A: list[int]) -> list[int]:
    n = len(A)
    ok = False
    for i in range(n):
        if ok:
            break
        ok = True
        for j in range(n - i - 1):
            if A[j] < A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                ok = False
    return A
