MOD = 998244353

from typing import Callable, TypeVar

T = TypeVar("T")
V = TypeVar("V")


class TreeDp:
    def __init__(self, n: int, adj: list[list[int]], r: int = 0):
        par = [-1] * n
        children = [[] for _ in range(n)]
        order = []
        st = [r]
        while st:
            u = st.pop()
            order.append(u)
            for v in adj[u]:
                if par[u] != v:
                    par[v] = u
                    children[u].append(v)
                    st.append(v)
        self.n = n
        self.par = par
        self.children = children
        self.order = order

    def calc(self, MAX: int = 200001) -> tuple[list[int], list[int], list[int]]:
        fa = [1] * (MAX + 1)
        fainv = [1] * (MAX + 1)
        inv = [1] * (MAX + 1)
        for i in range(MAX):
            fa[i + 1] = fa[i] * (i + 1) % MOD
        fainv[-1] = pow(fa[-1], MOD - 2, MOD)
        for i in range(MAX)[::-1]:
            fainv[i] = fainv[i + 1] * (i + 1) % MOD
        for i in range(1, MAX)[::-1]:
            inv[i] = fainv[i] * fa[i - 1]
        return fa, fainv, inv

    def size(self) -> list[int]:
        order, par = self.order, self.par
        res = [1] * self.n
        for v in order[1:][::-1]:
            res[par[v]] += res[v]
        return res

    def dp(self, e: T, merge: Callable[[T, T], T]) -> list[T]:
        order, par = self.order, self.par
        res = [e] * self.n
        for v in order[1:][::-1]:
            p = par[v]
            res[p] = merge(res[p], res[v])
        return res

    def rerooting(
        self,
        e: T,
        merge: Callable[[T, T], T],
        op_bu: Callable[[T, V, V], T],
        op_td: Callable[[T, V, V], T],
        op_fin: Callable[[T, V], T],
    ):
        order, par, children = self.order, self.par, self.children

        cum_bu = [e] * self.n
        cum_td = [e] * self.n
        res = [0] * self.n

        for u in order[1:][::-1]:
            p = par[u]
            res[u] = op_bu(cum_bu[u], u, p)
            cum_bu[p] = merge(cum_bu[p], res[u])
        r = order[0]
        res[r] = op_fin(cum_bu[r], r)

        for u in order:
            cum = cum_td[u]
            for v in children[u]:
                cum_td[v] = cum
                cum = merge(cum, res[v])
            cum = e
            for v in children[u][::-1]:
                cum_td[v] = op_td(merge(cum_td[v], cum), v, u)
                cum = merge(cum, res[v])
                res[v] = op_fin(merge(cum_bu[v], cum_td[v]), v)
        return res
