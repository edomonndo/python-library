# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_decomposition_width_2

from graph.tree_decomposition_width2 import TreeDecompositionWidth2

p, tw, n, m = input().split()
n, m = int(n), int(m)
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

g = TreeDecompositionWidth2(n, edges)
res = g.build()
if res is None:
    print(-1)
else:
    bag, edges = res
    k = len(bag)
    print("s", "td", k, 2, n)
    for i in range(k):
        print("b", i + 1, *[v + 1 for v in bag[i]])
    for u, v in edges:
        print(u + 1, v + 1)
