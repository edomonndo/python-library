from bisect import bisect_left
from data_structure.fenwick_tree.fenwick_tree import FenwickTree


class OfflinePointAddRectangleSum:
    def __init__(self):
        self.qs = []
        self.q_cnt = [0]

    def add_point(self, x: int, y: int, w: int) -> None:
        self.qs.append((-1, x, y, w))
        self.q_cnt.append(self.q_cnt[-1])

    def add_query(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.qs.append((self.q_cnt[-1], x1, y1, x2, y2))
        self.q_cnt.append(self.q_cnt[-1] + 1)

    def solve(self) -> list[int]:
        res = [0] * self.q_cnt[-1]
        stack = [(0, len(self.qs))]
        while stack:
            l, r = stack.pop()
            if r - l < 2:
                continue
            m = (l + r) >> 1
            stack += [(l, m), (m, r)]

            l_point = (m - l) - (self.q_cnt[m] - self.q_cnt[l])
            r_query = self.q_cnt[r] - self.q_cnt[m]

            # 狭い場合は愚直
            if l_point * r_query < 200:
                tmp = [self.qs[i] for i in range(l, m) if self.qs[i][0] == -1]
                for i in range(m, r):
                    if self.qs[i][0] != -1:
                        qi, x1, y1, x2, y2 = self.qs[i]
                        for _, x, y, w in tmp:
                            if x1 <= x < x2 and y1 <= y < y2:
                                res[qi] += w
                continue

            # add_pointに対して，y座標でソート&座圧
            toY, P = [], []
            for i in range(l, m):
                if self.qs[i][0] == -1:
                    toY.append(self.qs[i][2])
                    P.append(self.qs[i])
            toY.sort()
            for i in range(l_point):
                _, x, y, w = P[i]
                y_ = bisect_left(toY, y)
                P[i] = (x, y_, w)

            # イベントソート
            Q = []
            for i in range(m, r):
                if self.qs[i][0] != -1:
                    qi, x1, y1, x2, y2 = self.qs[i]
                    y1_ = bisect_left(toY, y1)
                    y2_ = bisect_left(toY, y2)
                    Q += [(~qi, x1, y1_, y2_), (qi, x2, y1_, y2_)]

            # x座標でソート
            P.sort(key=lambda p: p[0])
            Q.sort(key=lambda q: q[1])

            # 平面走査
            fw = FenwickTree(len(toY))
            pi, qi = 0, 0
            while qi < len(Q):
                if pi == len(P) or Q[qi][1] <= P[pi][0]:
                    i, x, y1, y2 = Q[qi]
                    s = fw.sum(y1, y2)
                    if i < 0:
                        res[~i] -= s
                    else:
                        res[i] += s
                    qi += 1
                else:
                    x, y, w = P[pi]
                    fw.add(y, w)
                    pi += 1
        return res
