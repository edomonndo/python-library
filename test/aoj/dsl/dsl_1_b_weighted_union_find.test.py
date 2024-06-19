# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B

from data_structure.connectivity.weighted_union_find import WeightedUnionFind

N, Q = map(int, input().split())
G = WeightedUnionFind(N)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        x, y, z = q
        G.merge(y, x, z)
    else:
        x, y = q
        ans = G.diff(y, x)
        print(ans if ans is not None else "?")
