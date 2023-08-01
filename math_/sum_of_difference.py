def sum_of_difference(n, arr):
    """Sum of $Ai$ - $Aj$ where $0<=i<j<N$."""
    accum = [0]
    for item in arr:
        accum.append(accum[-1] + item)
    res = accum[n] * n
    for i, item in enumerate(arr):
        res -= accum[i] + (n - i) * item
    return res
