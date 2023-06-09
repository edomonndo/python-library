# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

from tree.lca import LcaDoubling

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

lca = LcaDoubling(N, G)
for _ in range(Q):
    s, t, i = map(int, input().split())
    print(lca.jump(s, t, i))
