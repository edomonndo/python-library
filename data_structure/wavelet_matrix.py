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
        self.bit_size = len(bin(max(A))) - 2 if A else 0
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
            bv = BitVector(_T)
            self.B.append((bv.rank0(self.n), bv))
            T = L + R

    def access(self, i: int) -> int:
        # Aのi番目の要素を取得する
        return self.A[i]

    def accessFromB(self, i: int) -> int:
        # Aのi番目の要素を取得する
        # 通常accessで取得すれば良い。高速化が必要なとき、こちらを利用するとself.Aの配列を持たなくて良い
        # 実際に速くなるかは不明
        assert 0 <= i < self.n
        res = 0
        for z, bv in self.B:
            bit = bv.access(i)
            res = (res << 1) | bit
            if bit:
                i = z + bv.rank1(i)
            else:
                i = bv.rank0(i)
        return res

    def rank(self, l, r, value):
        # A[l,r)にvalueが出現する数を返す
        if l >= r:
            return 0
        for i, (z, bv) in enumerate(self.B):
            # 1
            if (value >> (self.bit_size - i - 1)) & 1:
                l = z + bv.rank1(l)
                r = z + bv.rank1(r)
            # 0
            else:
                l = bv.rank0(l)
                r = bv.rank0(r)
        return r - l

    def select(self, value, k):
        # Aに対して、k番目のvalueのIndexを返す(0-index)
        # valueが出現する数が以下のとき、-1を返す
        if self.rank(0, self.n, value) <= k:
            return -1
        idx = 0
        for i, (z, bv) in enumerate(self.B):
            # 1
            if (value >> (self.bit_size - i - 1)) & 1:
                idx = z + bv.rank1(idx)
            # 0
            else:
                idx = bv.rank0(idx)
        idx += k
        for z, bv in self.B[::-1]:
            # 0
            if idx < z:
                idx = bv.select0(idx)
            # 1
            else:
                idx = bv.select1(idx - z)
        return idx

    def quantile(self, l, r, k):
        # A[l, r)のk番目に小さい値を返す(0-index)
        if k >= r - l:
            return -1
        ret = 0
        for i, (z, bv) in enumerate(self.B):
            zeros = bv.rank0(r) - bv.rank0(l)
            # 0
            if zeros > k:
                l = bv.rank0(l)
                r = bv.rank0(r)
            # 1
            else:
                k -= zeros
                ret |= 1 << (self.bit_size - i - 1)
                l = z + bv.rank1(l)
                r = z + bv.rank1(r)
        return ret

    def quantilerange(self, l, r, k):
        # A[l, r)のk番目に小さい値のindexを返す(kは0-index)
        assert 0 <= l < r and r <= self.n
        assert k < r - l

        val = 0
        for z, bv in self.B:
            num_of_zero_l = bv.rank0(l)
            num_of_zero_r = bv.rank0(r)
            num_or_zero = num_of_zero_r - num_of_zero_l  # lからrまでにある0の数
            bit = 0 if k < num_or_zero else 1  # k番目の値の上からi番目のbit値

            if bit:
                k -= num_or_zero
                l = z + l - num_of_zero_l
                r = z + r - num_of_zero_r
            else:
                l = num_of_zero_l
                r = num_of_zero_l + num_or_zero
            val = (val << 1) | bit

        left = 0
        for i, (z, bv) in enumerate(self.B):
            bit = (val >> (self.bit_size - i - 1)) & 1  # 上からi番目のbit値
            if bit:
                left = z + bv.rank1(left)
            else:
                left = bv.rank0(left)
        rank = l + k - left
        return self.select(val, rank)

    def maxrange(self, l, r):
        # A[l,r)で最大値のindexを返す
        return self.quantilerange(l, r, r - l - 1)

    def minrange(self, l, r):
        # A[l,r)で最小値のindexを返す
        return self.quantilerange(l, r, 0)

    def topk(self, l, r, k):
        # A[l,r)の中で出現回数が多い順にk個の値と頻度を返す
        # 頻度が同じ場合は値が小さいものが優先される
        # キューは最大のwidthをキーとするため、マイナスをつける
        res = []
        pq = [(-(r - l), 0, 0, l, r)]  # -width, depth, value, left, right
        while pq and k > 0:
            _, depth, value, left, right = heappop(pq)
            if depth >= self.bit_size:
                res.append((value, right - left))
                k -= 1
                continue

            z, bv = self.B[depth]
            # 0
            l0 = bv.rank0(left)
            r0 = bv.rank0(right)
            if l0 < r0:
                heappush(pq, (-(r0 - l0), depth + 1, value, l0, r0))
            # 1
            l1 = z + bv.rank1(left)
            r1 = z + bv.rank1(right)
            if l1 < r1:
                nv = value | (1 << (self.bit_size - depth - 1))
                heappush(pq, (-(r1 - l1), depth + 1, nv, l1, r1))
        return res

    def rangesum(self, l, r):
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
            z, bv = self.B[depth]
            # 0
            l1_0 = bv.rank0(left1)
            r1_0 = bv.rank0(right1)
            l2_0 = bv.rank0(left2)
            r2_0 = bv.rank0(right2)
            if l1_0 < r1_0 and l2_0 < r2_0:
                que.append((l1_0, r1_0, l2_0, r2_0, depth + 1, value))
            # 1
            l1_1 = z + bv.rank1(left1)
            r1_1 = z + bv.rank1(right1)
            l2_1 = z + bv.rank1(left2)
            r2_1 = z + bv.rank1(right2)
            if l1_1 < r1_1 and l2_1 < r2_1:
                nv = value | (1 << (self.bit_size - depth - 1))
                que.append((l1_1, r1_1, l2_1, r2_1, depth + 1, nv))

        return res

    def rangefreq_to(self, l, r, value):
        # A[l,r)に出現する0<=z<valueを満たすzの数を返す
        if not value:
            return 0
        if l >= r or self.n == 0:
            return 0
        ret = 0
        for i, (z, bv) in enumerate(self.B):
            # 1
            if (value >> (self.bit_size - i - 1)) & 1:
                ret += bv.rank0(r) - bv.rank0(l)
                l = z + bv.rank1(l)
                r = z + bv.rank1(r)
            # 0
            else:
                l = bv.rank0(l)
                r = bv.rank0(r)
        return ret

    def rangefreq(self, l, r, x, y):
        # A[l,r)に出現するx<=z<yを満たすzの数を返す
        if x >= y or self.n == 0:
            return 0
        return self.rangefreq_to(l, r, y) - self.rangefreq_to(l, r, x)

    def prevvalue(self, l, r, x, y):
        # A[l,r)に出現するx<=c<yを満たす最大のcを返す
        assert l < r and 0 < r <= self.n
        assert 0 <= x < y

        y = min(y, self.n)
        y -= 1  # 　閉区間A[l,r]にする

        stack = [(l, r, 0, 0, True)]  # l,r,depth,z,tight
        while stack:
            l, r, depth, c, tight = stack.pop()
            if depth == self.bit_size:
                if c >= x:
                    return c
                continue
            bit = (y >> (self.bit_size - depth - 1)) & 1
            z, bv = self.B[depth]
            rank0_l = bv.rank0(l)
            rank0_r = bv.rank0(r)
            rank1_l = l - rank0_l
            rank1_r = r - rank0_r

            # 0
            l0 = rank0_l
            r0 = rank0_r
            if l0 != r0:
                c0 = (c << 1) | 0
                stack.append((l0, r0, depth + 1, c0, tight and bit == 0))
            # 1
            l1 = z + rank1_l
            r1 = z + rank1_r
            if l1 != r1:
                if not tight or bit == 1:
                    c1 = (c << 1) | 1
                    stack.append((l1, r1, depth + 1, c1, tight))
        # 見つからないとエラー
        return -1

    def nextvalue(self, l, r, x, y):
        # A[l,r)に出現するx<=c<yを満たす最小のcを返す
        assert l < r and 0 < r <= self.n
        assert 0 <= x < y

        stack = [(l, r, 0, 0, True)]  # l,r,depth,z,tight
        while stack:
            l, r, depth, c, tight = stack.pop()
            if depth == self.bit_size:
                if c < y:
                    return c
                continue
            bit = (x >> (self.bit_size - depth - 1)) & 1
            z, bv = self.B[depth]
            rank0_l = bv.rank0(l)
            rank0_r = bv.rank0(r)
            rank1_l = l - rank0_l
            rank1_r = r - rank0_r

            # 1
            l1 = z + rank1_l
            r1 = z + rank1_r
            if l1 != r1:
                c1 = (c << 1) | 1
                stack.append((l1, r1, depth + 1, c1, tight and bit == 1))
            # 0
            l0 = rank0_l
            r0 = rank0_r
            if l0 != r0:
                if not tight or bit == 0:
                    c0 = (c << 1) | 0
                    stack.append((l0, r0, depth + 1, c0, tight))
        # 見つからないとエラー
        return -1
