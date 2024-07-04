# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

from graph.tree.lca import LcaDoubling

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

lca = LcaDoubling(n, g)
for _ in range(q):
    s, t, i = map(int, input().split())
    print(lca.jump(s, t, i))
