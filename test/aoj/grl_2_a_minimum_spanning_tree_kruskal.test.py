# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A

from data_structure.unionfind import UnionFind

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
G = UnionFind(N)
ans = 0
for u, v, w in edges:
    if G.same(u, v):
        continue
    G.merge(u, v)
    ans += w

print(ans)
