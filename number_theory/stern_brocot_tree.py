class SternBrocotTree:
    @staticmethod
    def encode(a: int, b: int) -> list[tuple[bool, int]]:
        path = []
        q, r = divmod(a, b)
        if q > 0:
            path.append((True, q))

        a, b = b, r
        is_right = False
        while b:
            q, r = divmod(a, b)
            path.append((is_right, q))
            a, b = b, r
            is_right ^= True

        is_right, k = path.pop()
        if k > 1:
            path.append((is_right, k - 1))
        return path

    @staticmethod
    def _decode_interval(code: list[tuple[bool, int]]) -> tuple[int, int, int, int]:
        p, q, r, s = 0, 1, 1, 0
        for is_right, k in code:
            if is_right:
                p += k * r
                q += k * s
            else:
                r += k * p
                s += k * q
        return p, q, r, s

    @classmethod
    def decode(cls, code: list[tuple[bool, int]]) -> tuple[int, int]:
        p, q, r, s = cls._decode_interval(code)
        return p + r, q + s

    @classmethod
    def lca(cls, a: int, b: int, c: int, d: int) -> tuple[int, int]:
        if (a, b) == (1, 1) or (c, d) == (1, 1):
            return (1, 1)

        code1 = cls.encode(a, b)
        code2 = cls.encode(c, d)
        if code1[0][0] != code2[0][0]:
            return (1, 1)

        lca_code = []
        for (t, k), (_, l) in zip(code1, code2):
            lca_code.append((t, min(k, l)))
            if k != l:
                break
        return cls.decode(lca_code)

    @classmethod
    def depth(cls, a: int, b: int) -> int:
        code = cls.encode(a, b)
        return sum(k for _, k in code)

    @classmethod
    def ancestor(cls, a: int, b: int, k: int, default=None) -> tuple[int, int]:
        code = []
        for is_right, l in cls.encode(a, b):
            l = min(k, l)
            code.append((is_right, l))
            k -= l
            if k == 0:
                return cls.decode(code)
        else:
            return default

    @classmethod
    def range(cls, a: int, b: int) -> tuple[int, int, int, int]:
        return cls._decode_interval(cls.encode(a, b))
