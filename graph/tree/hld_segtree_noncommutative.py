from typing import Callable, TypeVar

T = TypeVar("T")

from data_structure.segtree.segment_tree import Segtree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition


class HldSegTree:
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
        v_hld = self.hld.build_list(v)
        self.seg = Segtree(v_hld, op, e)
        self.rseg = Segtree(v_hld[::-1], op, e)
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
        return self.seg.get(self.hld.into[k])

    def set(self, k: int, v: T) -> None:
        k = self.hld.into[k]
        self.seg.set(k, v)
        self.rseg.set(self.hld.n - k - 1, v)
