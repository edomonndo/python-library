# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching

from graph.bipartite_matching import bipartite_matching


L, R, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
ans = bipartite_matching(L, R, edges)
print(len(ans))
for u, v in ans:
    print(u, v)
