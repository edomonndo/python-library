# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_lis_query

from data_structure.static_range_lis_query import StaticRangeLISQuery

n, q = map(int, input().split())
P = [int(x) + 1 for x in input().split()]
Q = [tuple(map(int, input().split())) for _ in range(q)]
ans = StaticRangeLISQuery(P, Q)
print(*ans, sep="\n")
