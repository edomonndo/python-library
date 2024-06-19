# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A

from data_structure.basic.unionfind import UnionFind

N, Q = map(int, input().split())
G = UnionFind(N)
for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 0:
        G.merge(x, y)
    else:
        print(1 if G.same(x, y) else 0)
