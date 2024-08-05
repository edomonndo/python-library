from geometory.basic.point import Point


import sys

sys.setrecursionlimit(1_000_000)


class LeftHull:
    class Node:
        def __init__(self, bl: int, br: int, L: int, R: int, lchd: int, rchd: int):
            self.bl, self.br = bl, br
            self.L, self.R = L, R
            self.lchd, self.rchd = lchd, rchd

    def __init__(self, ps: list[Point]):
        self.ps = ps
        self.nodes = [self.Node(0, 0, 0, 0, 0, 0) for _ in range(len(ps) << 1)]
        self.root = 0
        self._build(0, 0, len(ps))

    def _is_leaf(self, idx: int) -> bool:
        node = self.nodes[idx]
        return node.lchd == node.rchd == -1

    @staticmethod
    def _cross3(a: Point, b: Point, c: Point) -> int:
        return (b - a).cross(c - a)

    def _pull(self, idx: int) -> None:
        # assert not self._is_leaf(idx)
        nodes, ps = self.nodes, self.ps
        l, r = nodes[idx].lchd, nodes[idx].rchd
        split_y = ps[nodes[r].L].y
        while not self._is_leaf(l) or not self._is_leaf(r):
            a, b = nodes[l].bl, nodes[l].br
            c, d = nodes[r].bl, nodes[r].br
            if a != b and self._cross3(ps[a], ps[b], ps[c]) > 0:
                l = nodes[l].lchd
            elif c != d and self._cross3(ps[b], ps[c], ps[d]) > 0:
                r = nodes[r].rchd
            elif a == b:
                r = nodes[r].lchd
            elif c == d:
                l = nodes[l].rchd
            else:
                s1 = self._cross3(ps[a], ps[b], ps[c])
                s2 = self._cross3(ps[b], ps[a], ps[d])
                # assert s1 + s2 >= 0
                if s1 + s2 == 0 or s1 * ps[d].y + s2 * ps[c].y < split_y * (s1 + s2):
                    l = nodes[l].rchd
                else:
                    r = nodes[r].lchd

        nodes[idx].bl = nodes[l].L
        nodes[idx].br = nodes[r].L
        return

    def _build(self, idx: int, L: int, R: int) -> None:
        node = self.nodes[idx]
        node.L = L
        node.R = R
        if R - L == 1:
            node.lchd = node.rchd = -1
            node.bl = node.br = L
        else:
            M = (L + R) // 2
            node.lchd = idx + 1
            node.rchd = idx + 2 * (M - L)
            self._build(node.lchd, L, M)
            self._build(node.rchd, M, R)
            self._pull(idx)
        return

    def _erase(self, idx: int, L: int, R: int) -> int:
        node = self.nodes[idx]
        if R <= node.L or L > node.R:
            return idx
        if L <= node.L and R >= node.R:
            return -1
        node.lchd = self._erase(node.lchd, L, R)
        node.rchd = self._erase(node.rchd, L, R)
        if node.lchd == -1:
            return node.rchd
        if node.rchd == -1:
            return node.lchd
        self._pull(idx)
        return idx

    def _get_hull(self, idx: int, l: int, r: int, res: list[int]) -> None:
        node = self.nodes[idx]
        if self._is_leaf(idx):
            res.append(node.L)
        elif r <= node.bl:
            self._get_hull(node.lchd, l, r, res)
        elif l >= node.br:
            self._get_hull(node.rchd, l, r, res)
        else:
            # assert l <= node.bl and node.br <= r
            self._get_hull(node.lchd, l, node.bl, res)
            self._get_hull(node.rchd, node.br, r, res)
        return

    def get_hull(self) -> list[int]:
        if self.root == -1:
            return []
        res = []
        self._get_hull(self.root, 0, len(self.ps) - 1, res)
        return res

    def erase(self, L: int) -> None:
        self.root = self._erase(self.root, L, L + 1)


bs = 20
msk = (1 << bs) - 1

n = int(input())
ps = [None] * n
idx = dict()
for i in range(n):
    x, y = map(int, input().split())
    ps[i] = Point(x, y)
    idx[x << bs | y] = i

ps.sort(key=lambda p: (p.y, p.x))
left = LeftHull(ps)
qs = []
for i in range(n):
    x, y = ps[i].x, ps[i].y
    qs.append(Point(-x, -y))
qs.sort(key=lambda p: (p.y, p.x))
right = LeftHull(qs)
l, cnt = 1, 0
layer = dict()
while cnt < n:
    hull = set()
    for i in left.get_hull():
        hull.add(i)
    for i in right.get_hull():
        hull.add(n - 1 - i)
    for i in hull:
        cnt += 1
        layer[i] = l
        left.erase(i)
        right.erase(n - 1 - i)
    l += 1

ans = [0] * n
for i, p in enumerate(ps):
    ans[idx[p.x << bs | p.y]] = layer[i]
print(*ans, sep="\n")
