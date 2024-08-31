class BitSet:
    """64 Bit"""

    def __init__(self, n: int):
        self.n = n
        self.buf = [0] * ((n + 63) // 64)

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
        sz = min(len(self.buf), len(other.buf))
        for i in range(sz):
            self.buf[i] |= other.buf[i]
        return self

    def __xor__(self, other: "BitSet") -> "BitSet":
        sz = min(len(self.buf), len(other.buf))
        for i in range(sz):
            self.buf[i] ^= other.buf[i]
        return self

    def tostr(self) -> str:
        res = ["1" if self[i] else "0" for i in range(self.n)]
        return "".join(res)

    def copy(self) -> "BitSet":
        res = BitSet(self.n)
        res.buf = self.buf[:]
        return res
