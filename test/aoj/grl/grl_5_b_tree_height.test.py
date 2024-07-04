# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_B

from graph.tree.tree_dp import TreeDp

N = int(input())
G = [[] for _ in range(N)]
W = dict()
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    W[(u, v)] = w
    W[(v, u)] = w

TDP = TreeDp(N, G)
e = 0
merge = lambda a, b: max(a, b)
adj_bu = lambda a, v, p: a + W[(v, p)]
adj_td = lambda a, v, p: a + W[(v, p)]
adj_fin = lambda a, v: a

res = TDP.rerooting(e, merge, adj_bu, adj_td, adj_fin)
print(*res, sep="\n")
