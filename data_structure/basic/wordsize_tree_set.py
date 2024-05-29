from array import array


class WordsizeTreeSet:

    def __init__(self, n: int, a: list[int] = None):
        self.n = n
        data = []
        len_ = 0
        if a:
            n >>= 5
            A = array("I", bytes(4 * (n + 1)))
            for a_ in a:
                if A[a_ >> 5] >> (a_ & 31) & 1 == 0:
                    len_ += 1
                    A[a_ >> 5] |= 1 << (a_ & 31)
            data.append(A)
            while n:
                a = array("I", bytes(4 * ((n >> 5) + 1)))
                for i in range(n + 1):
                    if A[i]:
                        a[i >> 5] |= 1 << (i & 31)
                data.append(a)
                A = a
                n >>= 5
        else:
            while n:
                n >>= 5
                data.append(array("I", bytes(4 * (n + 1))))
        self.data = data
        self.len = len_
        self.len_data = len(data)

    def add(self, x: int) -> bool:
        if self.data[0][x >> 5] >> (x & 31) & 1:
            return False
        for a in self.data:
            a[x >> 5] |= 1 << (x & 31)
            x >>= 5
        self.len += 1
        return True

    def discard(self, x: int) -> bool:
        if self.data[0][x >> 5] >> (x & 31) & 1 == 0:
            return False
        self.len -= 1
        for a in self.data:
            a[x >> 5] &= ~(1 << (x & 31))
            x >>= 5
            if a[x]:
                break
        return True

    def ge(self, x: int) -> int:
        assert 0 <= x < self.n
        d = 0
        data = self.data
        while True:
            if d >= self.len_data or x >> 5 >= len(data[d]):
                return -1
            m = data[d][x >> 5] & ((~0) << (x & 31))
            if m == 0:
                d += 1
                x = (x >> 5) + 1
            else:
                x = (x >> 5 << 5) + (m & -m).bit_length() - 1
                if d == 0:
                    break
                x <<= 5
                d -= 1
        return x

    def gt(self, x: int) -> int:
        assert 0 <= x < self.n
        if x + 1 == self.n:
            return -1
        return self.ge(x + 1)

    def le(self, x: int) -> int:
        assert 0 <= x < self.n
        d = 0
        data = self.data
        while True:
            if x < 0 or d >= self.len_data:
                return -1
            m = data[d][x >> 5] & ~((~1) << (x & 31))
            if m == 0:
                d += 1
                x = (x >> 5) - 1
            else:
                x = (x >> 5 << 5) + m.bit_length() - 1
                if d == 0:
                    break
                x <<= 5
                x += 31
                d -= 1
        return x

    def le(self, x: int) -> int:
        assert 0 <= x < self.n
        return self.le(x - 1)

    def member(self, x):
        return self.data[0][x >> 5] >> (x & 31) & 1
