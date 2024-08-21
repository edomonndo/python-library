# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartite_edge_coloring


from graph.bipartite_edge_coloring import *

l, r, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
rg = RegularBipartiteGlaph(l, r, edges)
bec = BipartiteEdgeColoring(rg)
bec.solve()

print(rg.k)
print(*bec.color[:m], sep="\n")
