# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query

from data_structure.static_range_inversion_query import StaticRangeInversionQuery

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
Q = [tuple(map(int, input().split())) for _ in range(q)]
ans = StaticRangeInversionQuery(A, Q)
print(*ans, sep="\n")
