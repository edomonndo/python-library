from typing import Callable, TypeVar, Union

T = TypeVar("T")
F = TypeVar("F")

from data_structure.segtree.lazy_segment_tree import LazySegtree
from graph.tree.heavy_light_decomposition import HeavyLightDecomposition


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
        edges: list[Union[tuple[int, int] | tuple[int, int, int]]],
        root: int = 0,
        directed: bool = False,
    ):
        # assert n == len(v)
        self.hld = HeavyLightDecomposition(n, edges, root, directed)
        nv = self.hld.build_list(v)
        self.seg = LazySegtree(nv, op, e, mapping, composition, id_)
        self.op = op
        self.e = e
        self.mapping = mapping
        self.compositon = composition
        self.id = id_

    def all_prod(self) -> T:
        return self.seg.all_prod()

    def path_prod(self, u: int, v: int, edge: bool = False) -> T:
        hld, seg = self.hld, self.seg
        res = self.e

        def _f(l: int, r: int) -> None:
            nonlocal res
            res = self.op(res, seg.prod(l, r))

        hld.path_query(u, v, _f, edge)
        return res

    def path_apply(self, u: int, v: int, f: F, edge: bool = False) -> None:
        hld, seg = self.hld, self.seg
        hld.path_query(u, v, lambda l, r: seg.apply(l, r, f), edge)

    def subtree_prod(self, v: int) -> T:
        return self.seg.prod(self.hld.into[v], self.hld.out[v])

    def subtree_apply(self, v: int, f: F) -> None:
        self.seg.apply(self.hld.into[v], self.hld.out[v], f)

    def get(self, k: int) -> T:
        return self.seg.get(self.hld.into[k])

    def set(self, k: int, v: T) -> None:
        k = self.hld.into[k]
        self.seg.set(k, v)
