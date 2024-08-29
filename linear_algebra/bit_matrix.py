from typing import Optional

from utility.bitset import BitSet


class BitMatrix:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.flip = False
        if n > m:
            self.flip = True
            n, m = m, n
        self.bss = [BitSet(m) for _ in range(n)]

    def __getitem__(self, idx: int) -> BitSet:
        return self.bss[idx]

    @staticmethod
    def from_input(n: int, m: int) -> "BitMatrix":
        res = BitMatrix(n, m)
        for i in range(n):
            row = input()
            # assert len(row) == m
            for j, c in enumerate(row):
                if c == "1":
                    res.set(i, j, 1)
        return res

    @staticmethod
    def from_str(s: list[str]) -> "BitMatrix":
        n = len(s)
        m = len(s[0])
        res = BitMatrix(n, m)
        for i in range(n):
            for j, c in enumerate(s[i]):
                if c == "1":
                    res.set(i, j, 1)
        return res

    def copy(self) -> "BitMatrix":
        res = BitMatrix(0, 0)
        res.n, res.m, res.flip = self.n, self.m, self.flip
        res.bss = [bs.copy() for bs in self.bss]
        return res

    def tostr(self) -> str:
        res = []
        for row in self.bss:
            res.append(row.tostr())
        return "\n".join(res)

    def set(self, i: int, j: int, x: int) -> None:
        # assert x == 0 or x == 1
        if self.flip:
            i, j = j, i
        # assert 0 <= i < self.n
        # assert 0 <= j < self.m
        self.bss[i][j] = x

    def get(self, i: int, j: int) -> int:
        if self.flip:
            i, j = j, i
        # assert 0 <= i < self.n
        # assert 0 <= j < self.m
        return self.bss[i][j]

    def transpose(self, do_flip: bool = True) -> "BitMatrix":
        if do_flip:
            res = BitMatrix(self.m, self.n)
            for i in range(self.n):
                for j in range(self.m):
                    if self.get(i, j):
                        res.set(j, i, 1)
            return res
        else:
            bss = [BitSet(self.n) for _ in range(self.m)]
            for i in range(self.n):
                for j in range(self.m):
                    if self.get(i, j):
                        bss[j][i] = 1
            res = BitMatrix(0, 0)
            res.n, res.m, res.flip, res.bss = self.m, self.n, False, bss
            return res

    def __mul__(self, other: "BitMatrix") -> "BitMatrix":
        assert self.m == other.n
        n, k = self.n, other.m
        res = BitMatrix(0, 0)
        res.n, res.m, res.flip = self.n, other.m, False
        bss = [BitSet(k) for _ in range(n)]
        if other.flip:
            other = other.transpose(False)
            # assert other.flip = False
        for i in range(self.n):
            for j in range(self.m):
                if self.get(i, j):
                    bss[i] ^= other[j]
        res.bss = bss
        return res

    def rank(self):
        if self.n == 0 or self.m == 0:
            return 0
        n, m = self.n, self.m
        if self.flip:
            n, m = m, n
        nonzero = []
        lead = []
        for i in range(n):
            ai = self.bss[i].copy()
            for aj, z in zip(nonzero, lead):
                if ai[z]:
                    ai ^= aj
            bj = -1
            for j in range(m):
                if ai[j]:
                    bj = j
                    break
            if bj >= 0:
                nonzero.append(ai.copy())
                lead.append(bj)
        return len(nonzero)

    def det(self) -> int:
        assert self.n == self.m
        assert self.flip == False
        n, bss = self.n, [bs.copy() for bs in self.bss]
        lead = [0] * n
        for i in range(n):
            for j in range(i):
                if bss[i][lead[j]]:
                    bss[i].xor_hint(bss[j], lead[j])
            lead[i] = bss[i].ctz()
            if lead[i] == n:
                return 0
        return 1

    def inv(self) -> Optional["BitMatrix"]:
        assert self.n == self.m
        assert self.flip == False
        n = self.n
        bss = [BitSet(n << 1) for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if self.get(i, j):
                    bss[i][j] = 1
        lead = [0] * n
        for i in range(n):
            bss[i][n + i] = 1
            for j in range(i):
                if bss[i][lead[j]]:
                    bss[i].xor_hint(bss[j], lead[j])
            lead[i] = bss[i].ctz()
            if lead[i] >= n:
                return None
            for j in range(i):
                if bss[j][lead[i]]:
                    bss[j].xor_hint(bss[i], lead[i])
        res = BitMatrix(n, n)
        for i in range(n):
            while lead[i] != i:
                bss[i], bss[lead[i]] = bss[lead[i]], bss[i]
                lead[i], lead[lead[i]] = lead[lead[i]], lead[i]
            for j in range(n):
                if bss[i][j + n]:
                    res.set(i, j, 1)
        return res
