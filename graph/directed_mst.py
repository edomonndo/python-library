from typing import Optional

from graph.connectivity.unionfind import UnionFind
from data_structure.basic.skew_heap import SkewHeap


def directed_mst(
    n: int, edges: list[tuple[int, int, int]], root: int = 0
) -> Optional[list[int]]:
    bs = 20
    msk = (1 << 20) - 1

    heaps = [SkewHeap() for _ in range(n)]
    for ei, (_, v, w) in enumerate(edges):
        heaps[v].push(w << bs | ei)

    uf = UnionFind(n)
    from_ = [0] * n
    cost = [0] * n
    used = [0] * n
    used[root] = 2
    stem = [-1] * n
    eis = []
    m = len(edges)
    par_e = [-1] * m

    for v in range(n):
        if used[v] != 0:
            continue
        selected, st, cnt = [], [], 0
        while used[v] != 2:
            used[v] = 1
            selected.append(v)
            if heaps[v].empty():
                return None
            node = heaps[v].pop()
            cost[v], ei = node >> bs, node & msk
            from_[v] = uf.leader(edges[ei][0])
            if stem[v] == -1:
                stem[v] = ei
            if from_[v] == v:
                continue
            eis.append(ei)
            while cnt:
                par_e[st.pop()] = ei
                cnt -= 1
            st.append(ei)
            if used[from_[v]] == 1:
                p = v
                while True:
                    if not heaps[p].empty():
                        heaps[p].add(-(cost[p] << bs))
                    if p != v:
                        uf.merge(v, p)
                        heaps[v].meld(heaps[p])
                    p = uf.leader(from_[p])
                    nv = uf.leader(v)
                    if v != nv:
                        heaps[nv] = heaps[v]
                        v = nv
                    cnt += 1
                    if p == v:
                        break
            else:
                v = from_[v]
        for v in selected:
            used[v] = 2

    used = [0] * m
    res = []
    for ei in eis[::-1]:
        if used[ei]:
            continue
        res.append(ei)
        x = stem[edges[ei][1]]
        while x != ei:
            used[x] = 1
            x = par_e[x]
    return res
