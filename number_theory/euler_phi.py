def euler_phi(N: int) -> int:
    res = N
    upper = int(N**0.5)
    for i in range(2, upper + 1):
        if N % i == 0:
            res -= res // i
            while N % i == 0:
                N //= i
    if N > 1:
        res -= res // N
    return res
