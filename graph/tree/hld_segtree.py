from atcoder.segtree import SegTree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from typing import Callable, TypeVar

T = TypeVar("T")


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
        nv = self.hld.build_list(v)
        self.seg = SegTree(op, e, nv)
        self.op = op
        self.e = e

    def path_prod(self, u: int, v: int) -> T:
        head, into, depth = self.hld.head, self.hld.into, self.hld.depth
        seg, par, op = self.seg, self.hld.par, self.op

        res = self.e
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u, v = v, u
            res = op(res, seg.prod(into[head[u]], into[u] + 1))
            u = par[head[u]]
        if depth[u] < depth[v]:
            u, v = v, u
        return op(res, seg.prod(into[v], into[u] + 1))

    def subtree_prod(self, v: int) -> T:
        return self.seg.prod(self.hld.into[v], self.hld.out[v])

    def get(self, k: int) -> T:
        return self.seg.get(self.hld.into[k])

    def set(self, k: int, v: T) -> None:
        k = self.hld.into[k]
        self.seg.set(k, v)
