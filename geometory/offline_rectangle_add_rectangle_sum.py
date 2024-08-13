from bisect import bisect_left

from data_structure.fenwick_tree.fenwick_tree import FenwickTree

MOD = 998244353


class Node:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a % MOD
        self.b = b % MOD
        self.c = c % MOD
        self.d = d % MOD

    def __iadd__(self, other) -> "Node":
        a = self.a + other.a
        if a >= MOD:
            a -= MOD
        b = self.b + other.b
        if b >= MOD:
            b -= MOD
        c = self.c + other.c
        if c >= MOD:
            c -= MOD
        d = self.d + other.d
        if d >= MOD:
            d -= MOD
        return Node(a, b, c, d)


class OfflineRectangleAddRectangleSum:
    def __init__(self):
        self.rects = []
        self.qs = []

    def add_rect(self, x1: int, y1: int, x2: int, y2: int, w: int) -> None:
        if x1 == x2 or y1 == y2:
            return
        assert x1 <= x2 and y1 <= y2
        self.rects.append((x1, y1, x2, y2, w))

    def add_query(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.qs.append((x1, y1, x2, y2))

    def solve(self) -> list[int]:
        n, q = len(self.rects), len(self.qs)
        res = [0] * q
        if n == 0 or q == 0:
            return res

        toY = []
        for _, y1, _, y2 in self.qs:
            toY += [y1, y2]
        toY = sorted(set(toY))

        event_rect = []
        for i, (x1, y1, x2, y2, w) in enumerate(self.rects):
            y1_ = bisect_left(toY, y1)
            y2_ = bisect_left(toY, y2)
            event_rect += [(x1, y1_, y2_, 0, i), (x2, y1_, y2_, 1, i)]
        event_rect.sort()

        event_qs = []
        for i, (x1, y1, x2, y2) in enumerate(self.qs):
            y1_ = bisect_left(toY, y1)
            y2_ = bisect_left(toY, y2)
            event_qs += [(x1, y1_, y2_, 0, i), (x2, y1_, y2_, 1, i)]
        event_qs.sort()

        j = 0
        bit = FenwickTree(len(toY) + 1, Node(0, 0, 0, 0))
        for qx, qy1, qy2, qf, qi in event_qs:
            while j < n + n and event_rect[j][0] < qx:
                p1, p2, f, i = event_rect[j][1:]
                rx1, ry1, rx2, ry2, w = self.rects[i]
                if f:
                    bit.add(p1, Node(-w * rx2 * ry1, -w, w * ry1, w * rx2))
                    bit.add(p2, Node(w * rx2 * ry2, w, -w * ry2, -w * rx2))
                else:
                    bit.add(p1, Node(w * rx1 * ry1, w, -w * ry1, -w * rx1))
                    bit.add(p2, Node(-w * rx1 * ry2, -w, w * ry2, w * rx1))
                j += 1

            qu = self.qs[qi]

            sub1 = bit.sum0(qy2 + 1)
            res[qi] += sub1.a
            res[qi] += (sub1.b * qx * qu[3]) % MOD
            res[qi] += (sub1.c * qx) % MOD
            res[qi] += (sub1.d * qu[3]) % MOD
            res[qi] %= MOD

            sub2 = bit.sum0(qy1 + 1)
            res[qi] -= sub2.a
            res[qi] -= (sub2.b * qx * qu[1]) % MOD
            res[qi] -= (sub2.c * qx) % MOD
            res[qi] -= (sub2.d * qu[1]) % MOD

            if not qf:
                res[qi] *= -1

            res[qi] %= MOD

        return res
