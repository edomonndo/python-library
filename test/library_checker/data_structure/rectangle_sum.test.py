# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum

from geometory.offline_static_rectangle_sum import solve

n, q = map(int, input().split())
ps = [None] * n
for i in range(n):
    ps[i] = tuple(map(int, input().split()))
qs = [None] * q
for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    qs[i] = (x1, y1, x2, y2)

ans = solve(ps, qs)
print(*ans, sep="\n")
