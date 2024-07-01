# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum

from tree.euler_tour import EulerTour

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append((v, 1))
    g[v].append((u, 1))
et = EulerTour(g, 0, A)
ans = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 0:
        cur = A[a]
        et.update_verticle(a, cur + b)
        A[a] = cur + b
    else:
        ans.append(et.path_verticle_sum(a, b))
print(*ans, sep="\n")
