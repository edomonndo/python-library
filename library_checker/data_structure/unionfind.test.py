# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind

from data_structure.unionfind import UnionFind

N, Q = map(int, input().split())
UF = UnionFind(N)

for _ in range(Q):
    t, u, v = map(int, input().split())

    if t == 0:
        UF.merge(u, v)

    elif t == 1:
        print(1 if UF.same(u, v) else 0)
