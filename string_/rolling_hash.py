class RollingHash:
    def __init__(self, S, base=317, mod=1 << 61 - 1):
        self.S = S
        self.mod = mod
        self.pow_base = [1]
        self.hash = [0]
        for s in S:
            self.hash.append((self.hash[-1] * base + ord(s)) % self.mod)
            self.pow_base.append((self.pow_base[-1] * base) % self.mod)

    def get(self, l, r):
        return (self.hash[r] - self.hash[l] * self.pow_base[r - l]) % self.mod
