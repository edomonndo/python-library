def bucket_sort(A: list[int], max_value: int) -> list[int]:
    # asserr len(A) == len(set(A))
    n = len(A)
    bin = [None] * (max_value + 1)
    for a in A:
        bin[a] = a
    j = 0
    for i in range(max_value + 1):
        if bin[i] is not None:
            A[j] = bin[i]
            j += 1
    return A
