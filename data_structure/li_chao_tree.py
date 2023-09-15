class LiChaoTree:
    def __init__(self, arr):
        """最小値(最大値)を求める頂点の数"""
        arr = sorted(set(arr))
        self.inf = 10**19
        self.L = 1 << (len(arr) - 1).bit_length()
        self.data = [None] * (self.L * 2)
        self.arr = arr + [self.inf] * (self.L - len(arr))  # 長さを揃える
        self.idx = {num: id for id, num in enumerate(arr)}

    def _f(self, line, x):
        """line=(a,b),a*x+bを返す"""
        a, b = line
        return a * x + b

    def _judge(self, line1, line2, x):
        """座標がxの点でline1の方が大きければTrueをそうでないならFalseを返す"""
        return self._f(line1, x) > self._f(line2, x)

    def add_line(self, line):
        """ax+bの直線を追加する"""
        idx = 1
        l, r = 0, self.L
        while True:
            if self.data[idx] is None:
                self.data[idx] = line
                return
            m = (l + r) // 2
            line_d = self.data[idx]
            lx, mx, rx = self.arr[l], self.arr[m], self.arr[r - 1]
            f_l = self._judge(line_d, line, lx)
            f_m = self._judge(line_d, line, mx)
            f_r = self._judge(line_d, line, rx)
            if f_l and f_r:
                self.data[idx] = line
                return
            if not f_l and not f_r:
                return
            if (f_r and f_m) or (f_m and f_l):
                line, self.data[idx] = self.data[idx], line
            if f_l != f_m:
                r = m
                idx *= 2
            else:
                l = m
                idx = 2 * idx + 1

    def query(self, x):
        """座標xにおける直線群の最小値を返す"""
        idx = self.idx[x] + self.L
        ans = self.inf
        while idx > 0:
            if self.data[idx]:
                ans = min(ans, self._f(self.data[idx], x))
            idx >>= 1
        return ans
