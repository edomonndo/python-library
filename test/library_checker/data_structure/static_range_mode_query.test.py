# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_mode_query
from data_structure.static_range_mode_query import StaticRangeModeQuery

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
RMQ = StaticRangeModeQuery(A)
for _ in range(q):
    l, r = map(int, input().split())
    print(*RMQ.query(l, r))
