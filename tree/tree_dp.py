MOD = 998244353


class TreeDp:
    def __init__(self, n, adj, r=0):
        par = [-1] * n
        children = [[] for _ in range(n)]
        stack = [r]
        order = []
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if par[u] != v:
                    par[v] = u
                    children[u].append(v)
                    stack.append(v)
        self.n = n
        self.par = par
        self.children = children
        self.order = order

    def calc(self, MAX):
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

    def size(self):
        res = [1] * self.n
        for v in self.order[1:][::-1]:
            res[self.par[v]] += res[v]
        return res

    def dp(self, e, op):
        res = [e] * self.n
        for v in self.order[1:][::-1]:
            p = self.par[v]
            res[p] = op(res[p], res[v])
        return res

    def rerooting(self, e, merge, adj_bu, adj_td, adj_fin):
        cum_bu = [e] * self.n
        cum_td = [e] * self.n
        res = [0] * self.n

        for u in self.order[1:][::-1]:
            res[u] = adj_bu(cum_bu[u], u, self.par[u])
            p = self.par[u]
            cum_bu[p] = merge(cum_bu[p], res[u])
        r = self.order[0]
        res[r] = adj_fin(cum_bu[r], r)

        for u in self.order:
            cum = cum_td[u]
            for v in self.children[u]:
                cum_td[v] = cum
                cum = merge(cum, res[v])
            cum = e
            for v in self.children[u][::-1]:
                cum_td[v] = adj_td(merge(cum_td[v], cum), v, u)
                cum = merge(cum, res[v])
                res[v] = adj_fin(merge(cum_bu[v], cum_td[v]), v)
        return res
