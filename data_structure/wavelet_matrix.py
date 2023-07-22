# https://miti-7.hatenablog.com/entry/2018/04/28/152259
# https://miti-7.hatenablog.com/entry/2018/04/15/155638
# https://atcoder.jp/contests/abc202/submissions/25000501

from heapq import heappush, heappop
from collections import deque


class BitVector:
    # 簡潔データ構造
    # B := 長さnの01列
    def __init__(self, B: list):
        self.n = len(B)
        self.B = B
        # 累積和
        self.SB = [0]
        for b in B:
            self.SB.append(self.SB[-1] + b)

    def access(self, i: int) -> int:
        # B[i]を返す
        return self.B[i]

    def rank0(self, i: int) -> int:
        # Bに対して、i番目までに出現する0の個数
        return i - self.rank1(i)

    def rank1(self, i: int) -> int:
        # Bに対して、i番目までに出現する1の個数
        return self.SB[i]

    def select0(self, k: int) -> int:
        # Bに対して、先頭からk番目の0のindexを求める
        l, r = 0, len(self.SB)
        if not k < r - 1 - self.SB[r - 1]:
            return -1
        while r - l > 1:
            mid = l + r >> 1
            if mid - self.SB[mid] <= k:
                l = mid
            else:
                r = mid
        return l

    def select1(self, k: int) -> int:
        # Bに対して、先頭からk番目の1のindexを求める
        l, r = 0, len(self.SB)
        if not k < self.SB[r - 1]:
            return -1
        while r - l > 1:
            mid = l + r >> 1
            if self.SB[mid] <= k:
                l = mid
            else:
                r = mid
        return l


class WaveletMatrix:
    # 完備辞書
    # s := bit長
    # A := 長さnの配列
    def __init__(self, A):
        self.bit_size = len(bin(max(A))) - 2
        self.A = A
        self.n = len(A)
        T = A[:]
        self.B = []
        for i in range(self.bit_size)[::-1]:
            L = []
            R = []
            _T = []
            for b in T:
                if b >> i & 1 == 0:
                    _T.append(0)
                    L.append(b)
                else:
                    _T.append(1)
                    R.append(b)
            bit_vector = BitVector(_T)
            self.B.append((bit_vector.rank0(self.n), bit_vector))
            T = L + R
        self.B = self.B[::-1]

    def access(self, i: int) -> int:
        # Aのi番目の要素を取得する
        return self.A[i]

    def accessFromB(self, i: int) -> int:
        # Aのi番目の要素を取得する
        # 通常accessで取得すれば良い。高速化が必要なとき、こちらを利用するとself.Aの配列を持たなくて良い
        # 実際に速くなるかは不明
        res = 0
        for j in range(self.bit_size)[::-1]:
            _, bit_vector = self.B[j]
            # 1
            if bit_vector.access(i):
                res += 1 << j
                i = (bit_vector.n - bit_vector.SB[-1]) + bit_vector.rank1(i)
            # 0
            else:
                i = bit_vector.rank0(i)
        return res

    def rank(self, l, r, value):
        # A[l,r)にvalueが出現する数を返す
        if l >= r:
            return 0
        for i in range(self.bit_size)[::-1]:
            z, bit_vector = self.B[i]
            # 1
            if value >> i & 1:
                l = z + bit_vector.rank1(l)
                r = z + bit_vector.rank1(r)
            # 0
            else:
                l = bit_vector.rank0(l)
                r = bit_vector.rank0(r)
        return r - l

    def select(self, value, k):
        # Aに対して、k番目のvalueのIndexを返す(0-index)
        # valueが出現する数が以下のとき、-1を返す
        if self.rank(0, self.n, value) <= k:
            return -1
        ind = 0
        for i in range(self.bit_size)[::-1]:
            z, bit_vector = self.B[i]
            # 1
            if value >> i & 1:
                ind = z + bit_vector.rank1(ind)
            # 0
            else:
                ind = bit_vector.rank0(ind)
        ind += k
        for i in range(self.bit_size):
            z, bit_vector = self.B[i]
            # 0
            if ind < z:
                ind = bit_vector.select0(ind)
            # 1
            else:
                ind = bit_vector.select1(ind - z)
        return ind

    def quantile(self, l, r, k):
        # A[l, r)のk番目に小さい値を返す
        if k >= r - l:
            return -1
        ret = 0
        for i in range(self.bit_size)[::-1]:
            z, bit_vector = self.B[i]
            zeros = bit_vector.rank0(r) - bit_vector.rank0(l)
            # 0
            if zeros > k:
                l = bit_vector.rank0(l)
                r = bit_vector.rank0(r)
            # 1
            else:
                k -= zeros
                ret |= 1 << i
                l = z + bit_vector.rank1(l)
                r = z + bit_vector.rank1(r)
        return ret

    def topk(self, l, r, k):
        # A[l,r)の中で出現回数が多い順にk個の値と頻度を返す
        # 頻度が同じ場合は値が小さいものが優先される
        # キューは最大のwidthをキーとするため、マイナスをつける
        res = []
        pq = [(-(self.bit_size - 1), 0, 0, l, r)]  # -width, depth, value, left, right
        while pq and k > 0:
            _, depth, value, left, right = heappop(pq)
            if depth >= self.bit_size:
                res.append((value, right - left))
                k -= 1
                continue

            z, bit_vector = self.B[self.bit_size - depth - 1]
            # 0
            l0 = bit_vector.rank0(left)
            r0 = bit_vector.rank0(right)
            if l0 < r0:
                heappush(pq, (-(r0 - l0), depth + 1, value, l0, r0))
            # 1
            l1 = z + bit_vector.rank1(left)
            r1 = z + bit_vector.rank1(right)
            if l1 < r1:
                nv = value | (1 << (self.bit_size - depth - 1))
                heappush(pq, (-(r1 - l1), depth + 1, nv, l1, r1))
        return res

    def sum(self, l, r):
        # A[l,r)の合計を返す
        return sum(value * freq for value, freq in self.topk(l, r, r - l))

    def intersect(self, l1, r1, l2, r2):
        # A[l1,r1)とA[l2,r2)の間で共通して出現する値と頻度を返す
        assert l1 < r1
        assert l2 < r2
        res = []
        que = deque([(l1, r1, l2, r2, 0, 0)])  # l1, r1, l2, r2, depth, value
        while que:
            left1, right1, left2, right2, depth, value = que.popleft()
            if depth >= self.bit_size:
                res.append((value, right1 - left1, right2 - left2))
                continue
            z, bit_vector = self.B[self.bit_size - depth - 1]
            # 0
            l1_0 = bit_vector.rank0(left1)
            r1_0 = bit_vector.rank0(right1)
            l2_0 = bit_vector.rank0(left2)
            r2_0 = bit_vector.rank0(right2)
            if l1_0 < r1_0 and l2_0 < r2_0:
                que.append((l1_0, r1_0, l2_0, r2_0, depth + 1, value))
            # 1
            l1_1 = z + bit_vector.rank1(left1)
            r1_1 = z + bit_vector.rank1(right1)
            l2_1 = z + bit_vector.rank1(left2)
            r2_1 = z + bit_vector.rank1(right2)
            if l1_1 < r1_1 and l2_1 < r2_1:
                nv = value | (1 << (self.bit_size - depth - 1))
                que.append((l1_1, r1_1, l2_1, r2_1, depth + 1, nv))

        return res

    def rangefreq_to(self, l, r, value):
        # A[l,r)に出現する0<=z<valueを満たすzの数を返す
        if not value:
            return 0
        if l >= r:
            return 0
        ret = 0
        for i in range(self.bit_size)[::-1]:
            z, bit_vector = self.B[i]
            # 1
            if value >> i & 1:
                ret += bit_vector.rank0(r) - bit_vector.rank0(l)
                l = z + bit_vector.rank1(l)
                r = z + bit_vector.rank1(r)
            # 0
            else:
                l = bit_vector.rank0(l)
                r = bit_vector.rank0(r)
        return ret

    def rangefreq(self, l, r, x, y):
        # A[l,r)に出現するx<=z<yを満たすzの数を返す
        if x >= y:
            return 0
        return self.rangefreq_to(l, r, y) - self.rangefreq_to(l, r, x)


if __name__ == "__main__":
    T = [5, 4, 5, 5, 2, 1, 5, 6, 1, 3, 5, 0]
    WM = WaveletMatrix(3, T)

    assert WM.n == len(T)
    assert WM.A == T
    for i, t in enumerate(T):
        assert t == WM.access(i)
        assert t == WM.accessFromB(i)
    rank = WM.rank(0, 6, 5)
    assert rank == 3, rank

    select = WM.select(5, 3)
    assert select == 6, select

    quantile = WM.quantile(1, 11, 8)
    assert quantile == 5, quantile

    quantile = WM.quantile(1, 11, 8)
    assert quantile == 5, quantile

    topk = WM.topk(1, 10, 2)
    assert topk == [(5, 3), (1, 2)], topk

    sum = WM.sum(1, 10)
    assert sum == 32, sum

    intersect = WM.intersect(0, 6, 6, 11)
    assert intersect == [(1, 1, 1), (5, 3, 2)], intersect

    rangefreq_to = WM.rangefreq_to(2, 7, 3)
    assert rangefreq_to == 2, rangefreq_to

    rangefreq = WM.rangefreq(0, 12, 3, 6)
    assert rangefreq == 7, rangefreq
