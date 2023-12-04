def sum_of_difference(n, arr):
    accum = [0]
    for item in arr:
        accum.append(accum[-1] + item)
    res = accum[n] * n
    for i, item in enumerate(arr):
        res -= accum[i] + (n - i) * item
    return res
