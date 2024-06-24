MOD = 998244353


class S:
    def __init__(self, a=0, b=0, ab=0, size=0):
        self.a = a % MOD
        self.b = b % MOD
        self.ab = ab % MOD
        self.size = size

    def __str__(self) -> str:
        return f"({self.a},{self.b},{self.ab}{self.size})"

    __repr__ = __str__

    def __add__(self, other: "S"):
        return __class__(
            self.a + other.a,
            self.b + other.b,
            self.ab + other.ab,
            self.size + other.size,
        )


class F:
    def __init__(self, a=0, b=0):
        self.a = a % MOD
        self.b = b % MOD

    def __str__(self) -> str:
        return f"({self.a},{self.b})"

    __repr__ = __str__

    def __add__(self, other: "S"):
        return __class__(self.a + other.a, self.b + other.b)


def op(l: S, r: S) -> S:
    return l + r


def mapping(f: F, x: S) -> S:
    sz = x.size
    a = x.a + f.a * sz % MOD
    b = x.b + f.b * sz % MOD
    ab = x.ab + f.b * x.a % MOD + f.a * x.b % MOD + f.a * f.b * sz % MOD
    return S(a, b, ab, sz)


def composition(f: F, g: F) -> F:
    return f + g
