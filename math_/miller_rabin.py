def miller_rabin(n: int) -> bool:
    """Miller-Rabin: ≒ O(1)"""
    assert n < 1 << 64
    if n == 2:
        return True
    if n < 2 or (n & 1) == 0:
        return False
    n1 = n - 1
    d, s = n1, 0
    while (d & 1) == 0:
        d //= 2
        s += 1

    arr = (
        [2, 7, 61]
        if n < 1 << 32
        else [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    )
    for a in arr:
        if a % n == 0:
            continue
        t = pow(a, d, n)
        if t == 1 or t == n1:
            continue
        for _ in range(s):
            t = pow(t, 2, n)
            if t == n1:
                break
        else:
            return False
    return True
