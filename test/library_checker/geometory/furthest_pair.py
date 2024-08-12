# verification-helper: PROBLEM https://judge.yosupo.jp/problem/furthest_pair

from geometory.diameter import diameter

t = int(input())
for _ in range(t):
    n = int(input())
    ps = [tuple(map(int, input().split())) for _ in range(n)]
    _, p, q = diameter(ps)
    i = j = -1
    for k, (x, y) in enumerate(ps):
        if i == -1:
            if p.x == x and p.y == y:
                i = k
            elif q.x == x and q.y == y:
                i = k
                p, q = q, p
        else:
            if i != k and q.x == x and q.y == y:
                j = k
                break
    print(i, j)
