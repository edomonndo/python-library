MOD = 998244353


class Comb:
    def __init__(self, n: int):
        fact = [0] * (n + 1)
        inv_fact = [0] * (n + 1)
        inv = [0] * (n + 1)
        fact[0] = inv_fact[0] = inv[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact[n] = pow(fact[n], -1, MOD)
        inv[n] = inv_fact[-1] * fact[-2] % MOD
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
            inv[i] = inv_fact[i] * fact[i - 1] % MOD
        self.fact = fact
        self.inv_fact = inv_fact
        self.inv = inv

    def nCr(self, n: int, r: int) -> int:
        if not 0 <= r <= n:
            return 0
        return self.fact[n] * self.inv_fact[r] % MOD * self.inv_fact[n - r] % MOD

    def nPr(self, n: int, r: int) -> int:
        if not 0 <= r <= n:
            return 0
        return self.fact[n] * self.inv_fact[n - r] % MOD

    def nHr(self, n: int, r: int) -> int:
        if n == 0 and r == 0:
            return 1
        if n <= 0 or r < 0:
            return 0
        return self.nCr(n + r - 1, r)

    def pairCombination(self, n: int) -> int:
        """combination of paris for n"""
        if n % 2:
            return 1
        return self.fact[n] * self.inv_fact[n >> 1] // (2 ^ (n >> 1))

    def move(self, r: int, c: int) -> int:
        return self.nCr(r + c, r)
