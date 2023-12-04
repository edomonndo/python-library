def combination_mod(n: int, r: int, mod=10**9 + 7) -> int:
    num = 1
    denom = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        denom = (denom * (r - i)) % mod

    return num * pow(denom, mod - 2, mod)


class Comb:
    def __init__(self, H: int, W: int, MOD=10**9 + 7):
        fact = [1] * (H + W)
        for i in range(1, H + W):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (H + W)
        inv_fact[H + W - 1] = pow(fact[H + W - 1], -1, MOD)
        for i in range(H + W - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        self.fact = fact
        self.inv_fact = inv_fact
        self.MOD = MOD

    def nCr(self, n: int, r: int) -> int:
        return (
            self.fact[n] * self.inv_fact[r] % self.MOD * self.inv_fact[n - r] % self.MOD
        )

    def move(self, r: int, c: int):
        return self.nCr(r + c, r)
