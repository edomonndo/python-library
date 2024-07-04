# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_A

from graph.tree.diameter import diameter

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a].append((b, c))
    G[b].append((a, c))

diam = diameter(N, G)
print(diam)
