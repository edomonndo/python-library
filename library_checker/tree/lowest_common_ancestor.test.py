# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter

from tree.lca import LcaDoubling

N, Q = map(int, input().split())
parent = list(map(int, input().split()))
G = [[] for _ in range(N)]
for v, p in enumerate(parent, start=1):
    G[v].append(p)
    G[p].append(v)

lca = LcaDoubling(N, G)
for _ in range(Q):
    u, v = map(int, input().split())
    print(lca.lca(u, v))
