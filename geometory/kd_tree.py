from collections import defaultdict
import bisect


class KDTree:
    def __init__(self, N, XY):
        self.N = N
        self.id = {v: i for i, v in enumerate(XY)}
        data = defaultdict(list)
        for i, (x, y) in enumerate(XY):
            data[x].append(y)
        for ys in data.values():
            ys.sort()
        self.X = sorted(data.keys())
        self.data = data

    def query(self, sx, sy, tx, ty):
        res = []
        l = bisect.bisect_left(self.X, sx)
        r = bisect.bisect_right(self.X, tx)
        for x in self.X[l:r]:
            yl = bisect.bisect_left(self.data[x], sy)
            yr = bisect.bisect_right(self.data[x], ty)
            for y in self.data[x][yl:yr]:
                res.append(self.id[(x, y)])
        return res
