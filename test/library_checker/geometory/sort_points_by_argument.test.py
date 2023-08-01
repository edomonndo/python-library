# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument

from geometory.sort_points_by_argument import sortPointsByArgument

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]

ans = sortPointsByArgument(A)
for x, y in ans:
    print(x, y)
