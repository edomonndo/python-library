# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum
from tree.euler_tour import EulerTour

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for v, p in enumerate(P, 1):
    g[p].append((v, 1))
    g[v].append((p, 1))

et = EulerTour(g, 0, A)
ans = []
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        a, b = qu
        cur = A[a]
        et.update_verticle(a, cur + b)
        A[a] = cur + b
    else:
        a = qu[0]
        ans.append(et.subtree_verticle_sum(a))
print(*ans, sep="\n")
