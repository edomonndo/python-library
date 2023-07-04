def combination_mod(n: int, r: int, mod=10**9 + 7) -> int:
    num = 1
    denom = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        denom = (denom * (r - i)) % mod

    return num * pow(denom, mod - 2, mod)
