# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_spanning_tree_undirected


from graph.matrix_tree_theorem import MatrixTreeTheorem

n, m = map(int, input().split())
g = MatrixTreeTheorem(n, True)
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

print(g.solve())
