# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_C

from tree.euler_tour import EulerTour

N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    k, *es = map(int, input().split())
    for e in es:
        G[i].append((e, 1))
        G[e].append((i, 1))

et = EulerTour(G, 0, [0] * N)
Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    print(et.lca(u, v))
