from atcoder.segtree import SegTree
from tree.heavy_light_decomposition import HeavyLightDecomposition
from typing import Callable, TypeVar

T = TypeVar("T")


class HldSegtree:
    def __init__(
        self,
        op: Callable[[T, T], T],
        e: T,
        v: list[int],
        n: int,
        edges: list[int, int],
        root: int = 0,
    ):
        # assert n == len(v)
        self.hld = HeavyLightDecomposition(n, edges, root)
        into = self.hld.into
        nv = [e] * n
        for i, a in enumerate(v):
            k = into[i]
            nv[k] = a
        self.seg = SegTree(op, e, nv)
        self.rseg = SegTree(op, e, nv[::-1])
        self.op = op
        self.e = e

    def prod(self, u: int, v: int) -> T:
        head, into, depth = self.hld.head, self.hld.into, self.hld.depth
        seg, rseg, par, op, n = self.seg, self.rseg, self.hld.par, self.op, self.hld.n

        l, r = self.e, self.e
        while head[u] != head[v]:
            if depth[head[u]] > depth[head[v]]:
                l = op(l, rseg.prod(n - into[u] - 1, n - into[head[u]]))
                u = par[head[u]]
            else:
                r = op(seg.prod(into[head[v]], into[v] + 1), r)
                v = par[head[v]]
        if depth[u] > depth[v]:
            l = op(l, rseg.prod(n - into[u] - 1, n - into[v]))
        else:
            l = op(l, seg.prod(into[u], into[v] + 1))
        return op(l, r)

    def get(self, k: int) -> T:
        return self.seg[self.hld.into[k]]

    def set(self, k: int, v: T) -> None:
        k = self.hld.into[k]
        self.seg[k] = v
        self.rseg[self.hld.n - k - 1] = v
