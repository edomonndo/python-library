# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dominatortree

from tree.dominator_tree import dominator_tree

n, m, r = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

print(*dominator_tree(g, r))
