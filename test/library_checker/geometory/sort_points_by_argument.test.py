# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument

from geometory.arg_sort import arg_sort

n = int(input())
ps = [tuple(map(int, input().split())) for _ in range(n)]

ans = arg_sort(ps)
for x, y in ans:
    print(x, y)
