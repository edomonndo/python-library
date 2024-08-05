# verification-helper: PROBLEM https://judge.yosupo.jp/problem/minimum_spanning_tree

from graph.connectivity.unionfind import UnionFind

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w, i))

edges.sort(key=lambda x: x[2])
uf = UnionFind(n)

X = 0
es = []
for u, v, w, i in edges:
    if uf.same(u, v):
        continue
    uf.merge(u, v)
    X += w
    es.append(i)

es.sort()
print(X)
print(*es)
