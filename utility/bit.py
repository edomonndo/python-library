class Bit64:
    @staticmethod
    def popcount(x: int) -> int:
        """Count number of 1 bit"""
        x = ((x >> 1) & 0x5555555555555555) + (x & 0x5555555555555555)
        x = ((x >> 2) & 0x3333333333333333) + (x & 0x3333333333333333)
        x = ((x >> 4) & 0x0F0F0F0F0F0F0F0F) + (x & 0x0F0F0F0F0F0F0F0F)
        x = ((x >> 8) & 0x00FF00FF00FF00FF) + (x & 0x00FF00FF00FF00FF)
        x = ((x >> 16) & 0x0000FFFF0000FFFF) + (x & 0x0000FFFF0000FFFF)
        x = ((x >> 32) & 0x00000000FFFFFFFF) + (x & 0x00000000FFFFFFFF)
        return x

    @staticmethod
    def bit_reverse(x: int) -> int:
        """Flip 1 and 0 bit"""
        x = (x >> 32) | (x << 32)
        x = ((x >> 16) & 0x0000FFFF0000FFFF) | ((x << 16) & 0xFFFF0000FFFF0000)
        x = ((x >> 8) & 0x00FF00FF0FF00FF) | ((x << 8) & 0xFF00FF00FF00FF00)
        x = ((x >> 4) & 0x0F0F0F0F0F0F0F0F) | ((x << 4) & 0xF0F0F0F0F0F0F0F0)
        x = ((x >> 2) & 0x3333333333333333) | ((x << 2) & 0xCCCCCCCCCCCCCCCC)
        x = ((x >> 1) & 0x5555555555555555) | ((x << 1) & 0xAAAAAAAAAAAAAAAA)
        return x

    @classmethod
    def ctz(cls, x: int) -> int:
        """Count trailing zeros"""
        if x == 0:
            return -1
        return cls.popcount(~x & (x - 1))

    @classmethod
    def clz(cls, x: int) -> int:
        """Count leading zeros"""
        return cls.ctz(cls.bit_reverse(x))


class Bit32:
    @staticmethod
    def popcount(x: int) -> int:
        """Count number of 1 bit"""
        x = ((x >> 1) & 0x55555555) + (x & 0x55555555)
        x = ((x >> 2) & 0x33333333) + (x & 0x33333333)
        x = ((x >> 4) & 0x0F0F0F0F) + (x & 0x0F0F0F0F)
        x = ((x >> 8) & 0x00FF00FF) + (x & 0x00FF00FF)
        x = ((x >> 16) & 0x0000FFFF) + (x & 0x0000FFFF)
        return x

    @staticmethod
    def bit_reverse(x: int) -> int:
        """Flip 1 and 0 bit"""
        x = (x >> 16) | (x << 16)
        x = ((x >> 8) & 0x00FF00FF) | ((x << 8) & 0xFF00FF00)
        x = ((x >> 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)
        x = ((x >> 2) & 0x33333333) | ((x << 2) & 0xCCCCCCCC)
        x = ((x >> 1) & 0x55555555) | ((x << 1) & 0xAAAAAAAA)
        return x

    @classmethod
    def ctz(cls, x: int) -> int:
        """Count trailing zeros"""
        if x == 0:
            return -1
        return cls.popcount(~x & (x - 1))

    @classmethod
    def clz(cls, x: int) -> int:
        """Count leading zeros"""
        return cls.ctz(cls.bit_reverse(x))
