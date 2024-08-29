class BitSet:
    """64 Bit"""

    def __init__(self, n: int):
        self.n = n
        self.buf = [0] * ((n + 63) // 64)

    def __repr__(self) -> str:
        return f"<BitSet[{self.tostr()}]>"

    def __getitem__(self, idx: int) -> int:
        return self.buf[idx >> 6] >> (idx & 0x3F) & 1

    def __setitem__(self, idx: int, b: int) -> None:
        # assert b == 0 or b == 1
        if b:
            self.buf[idx >> 6] |= 1 << (idx & 0x3F)
        else:
            self.buf[idx >> 6] &= ~(1 << (idx & 0x3F))

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

    def ctz(self):
        res = 0
        i = 0
        while i < len(self.buf) and self.buf[i] == 0:
            res += 64
            i += 1
        if i < len(self.buf):
            for sub_czt in range(64):
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
