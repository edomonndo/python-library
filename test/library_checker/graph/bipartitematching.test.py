# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching

from graph.bipartite_matching import BipartiteMatching


L, R, K = map(int, input().split())
bm = BipartiteMatching(L, R)
for _ in range(K):
    a, b = map(int, input().split())
    bm.add_edge(a, b)
res = bm.solve()
print(len(res))
for a, b in res:
    print(a, b)
