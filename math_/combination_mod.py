class Comb:
    def __init__(self, n: int, mod=10**9 + 7):
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], -1, mod)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
        self.fact = fact
        self.inv_fact = inv_fact
        self.mod = mod

    def nCr(self, n: int, r: int) -> int:
        if not 0 <= r <= n:
            return 0
        return (
            self.fact[n] * self.inv_fact[r] % self.mod * self.inv_fact[n - r] % self.mod
        )

    def nPr(self, n: int, r: int) -> int:
        if not 0 <= r <= n:
            return 0
        return self.fact[n] * self.inv_fact[n - r] % self.mod

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
        return self.fact[n] * self.inv_fact[n // 2] // (2 ^ (n // 2))

    def move(self, r: int, c: int) -> int:
        return self.nCr(r + c, r)
