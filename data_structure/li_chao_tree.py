class LiChaoTree:
    def __init__(self, xs, inf=10**19):
        """最小値(最大値)を求める頂点の数"""
        xs = sorted(set(xs))
        self.inf = inf
        self.size = 1 << (len(xs) - 1).bit_length()
        self.dat = [None] * (self.size * 2)
        self.xs = xs + [inf] * (self.size - len(xs))  # 長さを揃える
        self.idx = {num: id for id, num in enumerate(xs)}

    def _f(self, line, x):
        """line=(a,b),a*x+bを返す"""
        a, b = line
        return a * x + b

    def _judge(self, line1, line2, x):
        """座標がxの点でline1の方が大きければTrueをそうでないならFalseを返す"""
        return self._f(line1, x) > self._f(line2, x)

    def _add(self, line, idx, l, r):
        while True:
            if self.dat[idx] is None:
                self.dat[idx] = line
                return
            m = (l + r) // 2
            line_d = self.dat[idx]
            lx, mx, rx = self.xs[l], self.xs[m], self.xs[r - 1]
            f_l = self._judge(line_d, line, lx)
            f_m = self._judge(line_d, line, mx)
            f_r = self._judge(line_d, line, rx)
            if f_l and f_r:
                self.dat[idx] = line
                return
            if not f_l and not f_r:
                return
            if f_m:
                line, self.dat[idx] = self.dat[idx], line
            if f_l != f_m:
                r = m
                idx *= 2
            else:
                l = m
                idx = 2 * idx + 1

    def add_line(self, a, b):
        """ax+bの直線を追加する"""
        self._add((a, b), 1, 0, self.size)

    def add_segment(self, a, b, l, r):
        """線分ax+b(l<=x<r)を追加する"""
        line = (a, b)
        lidx, ridx = self.idx[l] + self.size, self.idx[r] + self.size
        l, r = self.idx[l], self.idx[r]
        size = 1
        while lidx < ridx:
            if lidx & 1:
                self._add(line, lidx, l, l + size)
                lidx += 1
                l += size
            if ridx & 1:
                self._add(line, ridx, r, r + size)
                ridx -= 1
                r -= size
                self._add(line, ridx, r, r + size)
            lidx >>= 1
            ridx >>= 1
            size <<= 1

    def query(self, x):
        """座標xにおける直線群の最小値を返す"""
        idx = self.idx[x] + self.size
        ans = self.inf
        while idx > 0:
            if self.dat[idx]:
                ans = min(ans, self._f(self.dat[idx], x))
            idx >>= 1
        return ans
