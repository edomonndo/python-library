# verification-helper: PROBLEM https://judge.yosupo.jp/problem/closest_pair

from geometory.closest_pair import closest_pair

t = int(input())
for _ in range(t):
    n = int(input())
    ps = [tuple(map(int, input().split())) for _ in range(n)]
    _, p, q = closest_pair(ps)
    i = j = -1
    for k, (x, y) in enumerate(ps):
        if p.x == x and p.y == y and i == -1:
            i = k
        elif q.x == x and q.y == y and j == -1:
            j = k
    print(i, j)
