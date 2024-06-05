class LiChaoTree:
    def __init__(self, points: list[int], inf: int = 1 << 60):
        """最小値(最大値)を求める頂点集合"""
        xs = sorted(set(points)) if points else [0]
        self.n = n = len(xs)
        self.inf = inf
        self.sz = sz = 2 << n.bit_length() if n & (n - 1) else n
        sz2 = self.sz << 1
        self.bl = [0] * sz2
        self.br = [0] * sz2
        self.dat = [(0, inf)] * sz2
        for i in range(n):
            self.bl[sz + i] = self.br[sz + i] = xs[i]
        for i in range(n, self.sz):
            self.bl[sz + i] = self.br[sz + i] = xs[n - 1]
        for i in range(sz - 1, 0, -1):
            self.bl[i] = self.bl[i << 1]
            self.br[i] = self.br[i << 1 | 1]

    def add_line(self, a: int, b: int, idx: int = 1) -> None:
        """ax+bの直線を追加する"""
        bl, br, dat = self.bl, self.br, self.dat
        while True:
            a2, b2 = dat[idx]
            l, r = bl[idx], br[idx]
            lv = a2 * l + b2
            rv = a2 * r + b2
            nlv = a * l + b
            nrv = a * r + b
            if (lv <= nlv) == (rv <= nrv):
                if nlv < lv:
                    dat[idx] = (a, b)
                return
            m = br[idx << 1]
            mv = a2 * m + b2
            nmv = a * m + b
            if nmv < mv:
                dat[idx], (a, b) = (a, b), dat[idx]
                lv, nlv = nlv, lv
            idx = (idx << 1) if nlv < lv else (idx << 1 | 1)

    def add_segment(self, a: int, b: int, l: int, r: int, idx: int = 1) -> None:
        """線分ax+b(l<=x<=r)を追加する"""
        L, R, bl, br, add_line = l, r, self.bl, self.br, self.add_line
        st = [idx]
        while st:
            idx = st.pop()
            l, r = bl[idx], br[idx]
            if R < l or r < L:
                continue
            if L <= l and r <= R:
                add_line(a, b, idx)
                continue
            st += [idx << 1 | 1, idx << 1]

    def query(self, x: int) -> int:
        """座標xにおける直線群の最小値を返す"""
        idx = 1
        a, b = self.dat[idx]
        res = a * x + b
        while idx < self.sz:
            idx <<= 1
            if x > self.br[idx]:
                idx += 1
            a, b = self.dat[idx]
            res = min(res, a * x + b)
        return res
