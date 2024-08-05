# verification-helper: PROBLEM https://judge.yosupo.jp/problem/counting_spanning_tree_directed


from graph.matrix_tree_theorem import MatrixTreeTheorem

n, m, r = map(int, input().split())
g = MatrixTreeTheorem(n, False, r)
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

print(g.solve())
