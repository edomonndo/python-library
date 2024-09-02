# verification-helper: PROBLEM https://yukicoder.me/problems/no/650

from graph.tree.heavy_light_decomposition import HLD
from data_structure.segtree.segment_tree import Segtree

MOD = 1_000_000_007


class S:
    def __init__(self, a=1, b=0, c=0, d=1):
        self.a = a % MOD
        self.b = b % MOD
        self.c = c % MOD
        self.d = d % MOD

    def __str__(self):
        return f"S({self.a},{self.b},{self.c},{self.d})"

    def get(self):
        return self.a, self.b, self.c, self.d


def op(x, y):
    a, b, c, d = x.get()
    p, q, r, s = y.get()
    return S(
        a * p % MOD + b * r % MOD,
        a * q % MOD + b * s % MOD,
        c * p % MOD + d * r % MOD,
        c * q % MOD + d * s % MOD,
    )


n = int(input())
g = [[] for _ in range(n)]
edges = []
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    edges.append((u, v))
hld = HLD(n, g)
vs = hld.build_list([S() for _ in range(n)])
seg = Segtree(vs, op, S())

eis = [0] * (n - 1)
for i, (u, v) in enumerate(edges):
    if hld.par[u] == v:
        eis[i] = hld.index(u)
    else:
        eis[i] = hld.index(v)

q = int(input())
for _ in range(q):
    query = input().split()
    if query[0] == "x":
        i, a, b, c, d = map(int, query[1:])
        seg.set(eis[i], S(a, b, c, d))
    else:
        i, j = map(int, query[1:])
        ans = S()
        for l, r in hld.path_query(i, j, True):
            ans = op(ans, seg.prod(l, r))
        print(ans.a, ans.b, ans.c, ans.d)
