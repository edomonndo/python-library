class BitSet:
    """Bit size: 63"""

    def __init__(self, n: int):
        self.n = n
        self.buf = [0] * ((n + 62) // 63)

    @staticmethod
    def _bit_count(n: int) -> int:
        c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
        c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
        c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
        c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
        c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
        c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
        return c

    def __repr__(self) -> str:
        return f"<BitSet[{self.tostr()}]>"

    def __getitem__(self, idx: int) -> int:
        return self.buf[idx >> 6] >> (idx & 63) & 1

    def __setitem__(self, idx: int, b: int) -> None:
        # assert b == 0 or b == 1
        if b:
            self.buf[idx >> 6] |= 1 << (idx & 63)
        else:
            self.buf[idx >> 6] &= ~(1 << (idx & 63))

    def __and__(self, other: "BitSet") -> "BitSet":
        return self.__xor__(other)

    def __or__(self, other: "BitSet") -> "BitSet":
        for i in range(min(len(self.buf), len(other.buf))):
            self.buf[i] |= other.buf[i]
        return self

    def __xor__(self, other: "BitSet") -> "BitSet":
        for i in range(min(len(self.buf), len(other.buf))):
            self.buf[i] ^= other.buf[i]
        return self

    def bit_count(self):
        res = 0
        for i in range(len(self.buf)):
            res += self._bit_count(self.buf[i])
        return res

    def ctz(self):
        res = 0
        i = 0
        while i < len(self.buf) and self.buf[i] == 0:
            res += 63
            i += 1
        if i < len(self.buf):
            for sub_czt in range(63):
                if self.buf[i] >> sub_czt & 1:
                    break
            res += sub_czt
        return min(res, self.n)

    def xor_hint(self, other: "BitSet", hint: int) -> "BitSet":
        for i in range(hint >> 6, min(len(self.buf), len(other.buf))):
            self.buf[i] ^= other.buf[i]
        return self

    def tostr(self) -> str:
        res = ["1" if self[i] else "0" for i in range(self.n)]
        return "".join(res)

    def copy(self) -> "BitSet":
        res = BitSet(self.n)
        res.buf = self.buf[:]
        return res
