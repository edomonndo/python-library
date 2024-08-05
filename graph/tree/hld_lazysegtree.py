from data_structure.segtree.lazy_segment_tree import LazySegtree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from typing import Callable, TypeVar

T = TypeVar("T")
F = TypeVar("F")


class HldLazySegTree:
    def __init__(
        self,
        op: Callable[[T, T], T],
        e: T,
        mapping: Callable[[F, T], T],
        composition: Callable[[F, F], F],
        id_: F,
        v: list[int],
        n: int,
        edges: list[int, int],
        root: int = 0,
    ):
        # assert n == len(v)
        self.hld = HeavyLightDecomposition(n, edges, root)
        nv = self.hld.build_list(v)
        self.seg = LazySegtree(nv, op, e, mapping, composition, id_)
        self.rseg = LazySegtree(nv[::-1], op, e, mapping, composition, id_)
        self.op = op
        self.e = e
        self.mapping = mapping
        self.compositon = composition
        self.id = id_

    def path_prod(self, u: int, v: int) -> T:
        head, into, depth, n = self.hld.head, self.hld.into, self.hld.depth, self.hld.n
        seg, rseg, par, op = self.seg, self.rseg, self.hld.par, self.op

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

    def path_apply(self, u: int, v: int, f: F) -> None:
        head, into, depth = self.hld.head, self.hld.into, self.hld.depth
        seg, par = self.seg, self.hld.par

        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            seg.apply(into[head[u]], into[u] + 1, f)
            u = par[head[u]]
        if depth[u] < depth[v]:
            u, v = v, u
        seg.apply(into[v], into[u] + 1, f)

    def subtree_prod(self, v: int) -> T:
        return self.seg.prod(self.hld.into[v], self.hld.out[v])

    def subtree_apply(self, v: int, f: F) -> None:
        self.seg.apply(self.hld.into[v], self.hld.out[v], f)

    def get(self, k: int) -> T:
        return self.seg.get(self.hld.into[k])

    def set(self, k: int, v: T) -> None:
        k = self.hld.into[k]
        self.seg.set(k, v)
        self.rseg[self.hld.n - k - 1] = v
