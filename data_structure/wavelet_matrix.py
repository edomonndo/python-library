from array import array
from heapq import *
from collections import deque


class BitVector:
    # 簡潔データ構造
    def __init__(self, n: int):
        self.n = n
        self.block_size = (n + 31) >> 5
        b = bytes(4 * (self.block_size + 1))
        # Unsigned int
        self.bit = array("I", b)
        self.acc = array("I", b)

    @staticmethod
    def _popcount(x: int) -> int:
        x = x - ((x >> 1) & 0x55555555)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = x + (x >> 4) & 0x0F0F0F0F
        x += x >> 8
        x += x >> 16
        return x & 0x0000007F

    def set(self, k: int) -> None:
        self.bit[k >> 5] |= 1 << (k & 31)

    def build(self) -> None:
        acc, bit = self.acc, self.bit
        for i in range(self.block_size):
            acc[i + 1] = acc[i] + self._popcount(bit[i])

    def access(self, k: int) -> int:
        return (self.bit[k >> 5] >> (k & 31)) & 1

    def rank0(self, k: int) -> int:
        """k番目までに出現する0の個数"""
        return k - self.rank1(k)

    def rank1(self, k: int) -> int:
        """k番目までに出現する1の個数"""
        return self.acc[k >> 5] + self._popcount(
            self.bit[k >> 5] & ((1 << (k & 31)) - 1)
        )

    def rank01(self, k: int) -> tuple[int, int]:
        one = self.rank1(k)
        zero = k - one
        return zero, one

    def select0(self, k: int) -> int:
        """先頭からk番目の0のindexを求める"""
        if k < 0 or self.rank0(self.n) <= k:
            return -1
        l, r = 0, self.block_size + 1
        while r - l > 1:
            m = (l + r) >> 1
            if m * 32 - self.acc[m] > k:
                r = m
            else:
                l = m
        idx = 32 * l
        k = k - (l * 32 - self.acc[l]) + self.rank0(idx)
        l, r = idx, idx + 32
        while r - l > 1:
            m = (l + r) >> 1
            if self.rank0(m) > k:
                r = m
            else:
                l = m
        return l

    def select1(self, k: int) -> int:
        """先頭からk番目の1のindexを求める"""
        if k < 0 or self.rank1(self.n) <= k:
            return -1
        l, r = 0, self.block_size + 1
        while r - l > 1:
            m = (l + r) >> 1
            if self.acc[m] > k:
                r = m
            else:
                l = m
        idx = 32 * l
        k = k - self.acc[l] + self.rank1(idx)
        l, r = idx, idx + 32
        while r - l > 1:
            m = (l + r) >> 1
            if self.rank1(m) > k:
                r = m
            else:
                l = m
        return l


class WaveletMatrix:
    def __init__(self, A: list[int], max_value: int = 10**9):
        self.A = A
        self.n = len(A)
        self.max_value = max_value
        self.bit_size = max_value.bit_length()
        # Unsigned int
        self.mid = array("I", bytes(4 * self.bit_size))
        self.b = [BitVector(self.n) for _ in range(self.bit_size)]
        self._build()

    def _build(self) -> None:
        A = self.A[:]
        for i in range(self.bit_size - 1, -1, -1):
            b = self.b[i]
            zero, one = [], []
            for j, a in enumerate(A):
                if a >> i & 1:
                    b.set(j)
                    one.append(a)
                else:
                    zero.append(a)
            b.build()
            self.mid[i] = len(zero)
            A = zero + one

    def access(self, k: int) -> int:
        """Aのk番目の要素を取得する"""
        return self.A[k]

    def accessFromB(self, k: int) -> int:
        """Aのk番目の要素を取得する.通常accessで取得すれば良い.メモリ削減が必要なとき,こちらを利用するとself.Aの配列を持たなくて良い"""
        if k < 0:
            k += self.n
        assert 0 <= k < self.n
        b, mid = self.b, self.mid
        res = 0
        for i in range(self.bit_size - 1, -1, -1):
            if b[i].access(k):
                res |= 1 << i
                k = b[i].rank1(k) + mid[i]
            else:
                k = b[i].rank0(k)
        return res

    def _rank(self, r: int, value: int) -> int:
        """A[0,r)にvalueが出現する数を返す"""
        assert r <= self.n
        if r < 1:
            return 0
        l, b, mid = 0, self.b, self.mid
        for i in range(self.bit_size - 1, -1, -1):
            if value >> i & 1:
                l = b[i].rank1(l) + mid[i]
                r = b[i].rank1(r) + mid[i]
            else:
                l = b[i].rank0(l)
                r = b[i].rank0(r)
        return r - l

    def rank(self, l: int, r: int, value: int) -> int:
        """A[l,r)にvalueが出現する数を返す"""
        if l >= r:
            return 0
        return self._rank(r, value) - self._rank(l, value)

    def select(self, value: int, k: int) -> int:
        """Aに対して,k番目のvalueのIndexを返す(0-index). valueが出現する数が以下のとき,-1を返す"""
        if self._rank(self.n, value) <= k:
            return -1
        b = self.b
        idx = 0
        for i in range(self.bit_size - 1, -1, -1):
            if value >> i & 1:
                idx = b[i].rank0(self.n) + b[i].rank1(idx)
            else:
                idx = b[i].rank0(idx)
        idx += k
        for i in range(self.bit_size):
            if value >> i & 1:
                idx = b[i].select1(idx - b[i].rank0(self.n))
            else:
                idx = b[i].select0(idx)
        return idx

    def kth_smallest(self, l: int, r: int, k: int) -> int:
        """A[l, r)のk番目に小さい値を返す(0-index)"""
        assert 0 <= l <= r <= self.n
        if k >= r - l:
            return -1
        b, mid = self.b, self.mid
        res = 0
        for i in range(self.bit_size - 1, -1, -1):
            l0, r0 = b[i].rank0(l), b[i].rank0(r)
            zero_cnt = r0 - l0
            if zero_cnt <= k:
                res |= 1 << i
                k -= zero_cnt
                l += mid[i] - l0
                r += mid[i] - r0
            else:
                l, r = l0, r0
        return res

    quantile = kth_smallest

    def kth_largest(self, l: int, r: int, k: int) -> int:
        if k >= r - l:
            return -1
        return self.kth_smallest(l, r, r - l - k - 1)

    def quantilerange(self, l: int, r: int, k: int) -> int:
        """A[l, r)のk番目に小さい値のindexを返す(kは0-index)"""
        assert 0 <= l < r and r <= self.n
        assert k <= r - l
        val = self.quantile(l, r, k)
        cnt_left = self._rank(l, val)
        return self.select(val, cnt_left)

    def maxrange(self, l: int, r: int) -> int:
        """A[l,r)で最大値のindexを返す"""
        return self.quantilerange(l, r, r - l - 1)

    def minrange(self, l: int, r: int) -> int:
        """A[l,r)で最小値のindexを返す"""
        return self.quantilerange(l, r, 0)

    def topk(self, l: int, r: int, k: int) -> list[tuple[int, int]]:
        """
        A[l,r)の中で出現回数が多い順にk個の値と頻度を返す.
        頻度が同じ場合は値が小さいものが優先される.
        """
        res = []
        b, mid = self.b, self.mid
        pq = [(-(r - l), 0, l, self.bit_size - 1)]  # -width, value, left, bit
        while pq:
            w, v, l, i = heappop(pq)
            w = -w
            if i == -1:
                res.append((v, w))
                k -= 1
                if k == 0:
                    break
            else:
                r = l + w
                l0, l1 = b[i].rank01(l)
                r0, r1 = b[i].rank01(r)
                if l0 < r0:
                    heappush(pq, (-(r0 - l0), v, l0, i - 1))
                l1 += mid[i]
                r1 += mid[i]
                if l1 < r1:
                    heappush(pq, (-(r1 - l1), v | (1 << i), l1, i - 1))
        return res

    def rangesum(self, l: int, r: int) -> int:
        """A[l,r)の合計を返す"""
        return sum(value * freq for value, freq in self.topk(l, r, r - l))

    def intersect(self, l1: int, r1: int, l2: int, r2: int) -> list[tuple[int, int]]:
        """A[l1,r1)とA[l2,r2)の間で共通して出現する値と頻度を返す"""
        # Not verify
        assert l1 < r1
        assert l2 < r2
        b, mid = self.b, self.mid
        res = []
        q = deque([(l1, r1, l2, r2, 0, self.bit_size - 1)])  # l1, r1, l2, r2, value, i
        while q:
            left1, right1, left2, right2, value, i = q.popleft()
            if i == -1:
                res.append((value, right1 - left1, right2 - left2))
                continue
            l1_0 = b[i].rank0(left1)
            r1_0 = b[i].rank0(right1)
            l2_0 = b[i].rank0(left2)
            r2_0 = b[i].rank0(right2)
            if l1_0 < r1_0 and l2_0 < r2_0:
                q.append((l1_0, r1_0, l2_0, r2_0, value, i - 1))
            l1_1 = mid[i] + b[i].rank1(left1)
            r1_1 = mid[i] + b[i].rank1(right1)
            l2_1 = mid[i] + b[i].rank1(left2)
            r2_1 = mid[i] + b[i].rank1(right2)
            if l1_1 < r1_1 and l2_1 < r2_1:
                q.append((l1_1, r1_1, l2_1, r2_1, value | (1 << i), i - 1))
        return res

    def rangefreq_to(self, l: int, r: int, value: int) -> int:
        """A[l,r)に出現する0<=z<valueを満たすzの数を返す"""
        if value <= 0:
            return 0
        if l >= r or self.n == 0:
            return 0
        res = 0
        b, mid = self.b, self.mid
        for i in range(self.bit_size - 1, -1, -1):
            l0, r0 = b[i].rank0(l), b[i].rank0(r)
            if value >> i & 1:
                res += r0 - l0
                l += mid[i] - l0
                r += mid[i] - r0
            else:
                l, r = l0, r0
        return res

    def rangefreq(self, l: int, r: int, x: int, y: int) -> int:
        """A[l,r)に出現するx<=z<yを満たすzの数を返す"""
        if x >= y or self.n == 0:
            return 0
        return self.rangefreq_to(l, r, y) - self.rangefreq_to(l, r, x)

    def prevvalue(self, l: int, r: int, x: int) -> int:
        """A[l,r)に出現するc<xを満たす最大のcを返す"""
        assert l < r and 0 < r <= self.n
        assert 0 <= x
        cnt = self.rangefreq_to(l, r, x)
        if cnt == 0:
            return -1
        return self.kth_smallest(l, r, cnt - 1)

    def nextvalue(self, l: int, r: int, x: int) -> int:
        """A[l,r)に出現するx<=cを満たす最小のcを返す"""
        assert l < r and 0 < r <= self.n
        assert 0 <= x
        cnt = self.rangefreq_to(l, r, x)
        if cnt == r - l:
            return -1
        return self.kth_smallest(l, r, cnt)
