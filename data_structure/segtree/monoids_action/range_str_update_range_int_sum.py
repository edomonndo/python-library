MOD = 998244353

power10 = [1] * (200_001)
one = [0] * (200_001)
for i in range(200_000):
    power10[i + 1] = (power10[i] * 10) % MOD
    one[i + 1] = (one[i] * 10 + 1) % MOD


class S:
    def __init__(self, value=0, size=0):
        self.value = value % MOD
        self.size = size

    def __str__(self) -> str:
        return f"S({self.value},{self.size})"

    __repr__ = __str__

    def __add__(self, other: "S"):
        return __class__(
            self.value * power10[other.size] + other.value,
            self.size + other.size,
        )


class F:
    def __init__(self, digit=0):
        self.digit = digit

    def __str__(self) -> str:
        return f"F({self.digit})"

    __repr__ = __str__


def op(l: S, r: S) -> S:
    return l + r


def mapping(f: F, x: S) -> S:
    if f.digit == 0:
        return x
    return S(f.digit * one[x.size], x.size)


def composition(f: F, g: F) -> F:
    if f.digit == 0:
        return g
    return f
