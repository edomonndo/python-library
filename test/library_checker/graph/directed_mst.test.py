# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst


from graph.directed_mst import directed_mst

n, m, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
eis = directed_mst(n, edges, r)
assert eis

cost = 0
par = [-1] * n
for ei in eis:
    u, v, w = edges[ei]
    cost += w
    par[v] = u
par[r] = r
print(cost)
print(*par)
