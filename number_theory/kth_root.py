class KthRoot:

    @staticmethod
    def floor(real: int, k: int) -> int:
        # assert k != 0
        if real <= 1 or k == 1:
            return real
        if k >= 64:
            return 1

        def check(a: int, k: int) -> bool:
            res = 1
            while k:
                if k & 1:
                    res *= a
                    if res > real:
                        return False
                k >>= 1
                a *= a
            return res <= real

        res = int(pow(real, 1 / k))
        while not check(res):
            res -= 1
        while check(res + 1):
            res += 1
        return res

    @classmethod
    def ceil(cls, real: int, k: int) -> int:
        if real <= 1 or k == 1:
            return real
        if k >= 64:
            return 2
        res = cls.floor(real, k)
        x, a = 1, res
        while k:
            if k & 1:
                x *= a
            k >>= 1
            a *= a
        if x != real:
            res += 1
        return res
