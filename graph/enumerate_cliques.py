from typing import Callable, TypeVar

T = TypeVar("T")


def enumerate_cliques(
    n: int,
    edges: tuple[int, int],
    calc: Callable[[T, T], T],
    merge: Callable[[T, T], T],
    e: T = 0,
    include_empty: bool = False,
) -> T:
    g = [[0] * n for _ in range(n)]
    deg = [0] * n
    for u, v in edges:
        g[u][v] = g[v][u] = 1
        deg[u] += 1
        deg[v] += 1

    m = len(edges)
    sm = 0
    while (sm + 1) ** 2 <= 2 * m:
        sm += 1

    def compress(g: list[list[int]], sz: int, tmp: list[int]) -> list[int]:
        bit = [0] * sz
        for i in range(sz):
            for j in range(i):
                if not g[tmp[i]][tmp[j]]:
                    bit[i] |= 1 << j
                    bit[j] |= 1 << i
        return bit

    def f(g: list[list[int]], tmp: list[int], include_empty: bool, inner: bool) -> None:
        nonlocal res

        sz = len(tmp) - inner
        bit = compress(g, sz, tmp)

        for S in range(1 << sz):
            ok = 1
            for i in range(sz):
                if (S >> i) & 1 and S & bit[i]:
                    ok = 0
                    break
            if ok and (S or include_empty):
                vs = [tmp[-1]] if inner else []
                for i in range(sz):
                    if (S >> i) & 1:
                        vs.append(tmp[i])
                res = merge(res, calc(vs))
        return

    V = [1] * n
    res = e
    while True:
        tmp = []
        for u in range(n):
            if V[u] and deg[u] < sm:
                for v in range(n):
                    if u != v and V[v] and g[u][v]:
                        tmp.append(v)
                tmp.append(u)
                break
        if not tmp:
            break
        f(g, tmp, True, True)

        u = tmp[-1]
        V[u] = deg[u] = 0
        for v in range(n):
            if u != v and V[v] and g[u][v]:
                deg[v] -= 1

    tmp = [u for u in range(n) if V[u]]
    f(g, tmp, include_empty, False)
    return res
