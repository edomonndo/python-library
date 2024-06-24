MOD = 998244353


class S:
    def __init__(self, a=0, size=0):
        self.a = a % MOD
        self.size = size

    def __str__(self) -> str:
        return f"({self.a},{self.size})"

    __repr__ = __str__

    def __add__(self, other: "S"):
        return __class__(
            self.a + other.a,
            self.size + other.size,
        )


class F:
    def __init__(self, a=0):
        self.a = a % MOD

    def __str__(self) -> str:
        return f"({self.a})"

    __repr__ = __str__

    def __add__(self, other: "S"):
        return __class__(self.a + other.a)


def op(l: S, r: S) -> S:
    return l + r


def mapping(f: F, x: S) -> S:
    return S(x.a + f.a * x.size, x.size)


def composition(f: F, g: F) -> F:
    return f + g
