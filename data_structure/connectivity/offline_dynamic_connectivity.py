from typing import Callable
from collections import defaultdict

from data_structure.rollback_unionfind import RollbackUnionFind


class OfflineDynamicConnectivity:

    def __init__(self, n: int):
        self.n = n
        self.bit = n.bit_length() + 1
        self.msk = (1 << self.bit) - 1
        self.query_count = 0
        self.edge = defaultdict(list)
        self.uf = RollbackUnionFind(n)

    def build(self, edges: list[tuple[int, int]]):
        bit, edge = self.bit, self.edge
        for u, v in edges:
            if u > v:
                u, v = v, u
            edge[u << bit | v].append(0)
        self.query_count += 1

    def add_value(self, u: int, w: int) -> None:
        self.uf.add(u, w)

    def add_value_group(self, u: int, w: int) -> None:
        self.uf.add_group(u, w)

    def group_sum(self, u: int) -> int:
        return self.uf.group_sum(u)

    def add_edge(self, u: int, v: int) -> None:
        assert 0 <= u < self.n and 0 <= v < self.n
        if u > v:
            u, v = v, u
        self.edge[u << self.bit | v].append(self.query_count << 1)
        self.query_count += 1

    def delete_edge(self, u: int, v: int) -> None:
        assert 0 <= u < self.n and 0 <= v < self.n
        if u > v:
            u, v = v, u
        self.edge[u << self.bit | v].append(self.query_count << 1 | 1)
        self.query_count += 1

    def add_relax(self) -> None:
        self.query_count += 1

    def run(self, out: Callable[[int], None]) -> None:
        # O(qlogqlogn)
        uf, bit, msk, q = self.uf, self.bit, self.msk, self.query_count
        log = (q - 1).bit_length()
        size = 1 << log
        data = [[] for _ in range(size << 1)]
        for k, v in self.edge.items():
            LR = []
            i = 0
            cnt = 0
            while i < len(v):
                if v[i] & 1 == 0:
                    cnt += 1
                if cnt > 0:
                    LR.append(v[i] >> 1)
                    i += 1
                    while i < len(v) and cnt > 0:
                        if v[i] & 1 == 0:
                            cnt += 1
                        else:
                            cnt -= 1
                            if cnt == 0:
                                LR.append(v[i] >> 1)
                        i += 1
                    i -= 1
                i += 1
            if cnt > 0:
                LR.append(q)
            LR.reverse()
            while LR:
                l = LR.pop() + size
                r = LR.pop() + size
                while l < r:
                    if l & 1:
                        data[l].append(k)
                        l += 1
                    if r & 1:
                        data[r ^ 1].append(k)
                    l >>= 1
                    r >>= 1

        todo = [1]
        while todo:
            v = todo.pop()
            if v >= 0:
                for uv in data[v]:
                    uf.merge(uv >> bit, uv & msk)
                todo.append(~v)
                if v << 1 | 1 < size + size:
                    todo.append(v << 1 | 1)
                    todo.append(v << 1)
                elif v - size < q:
                    out(v - size)
            else:
                for _ in data[~v]:
                    uf.undo()

    def __repr__(self):
        return f"OfflineDynamicConnectivity({self.n}, {self.q})"
