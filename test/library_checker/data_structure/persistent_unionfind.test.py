# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_unionfind
from persistent_data_structure.persistent_union_find import PersistentUnionFind

N, Q = map(int, input().split())
G = PersistentUnionFind(N)
for _ in range(Q):
    t, k, u, v = map(int, input().split())
    if t == 0:
        G.merge(k, u, v)
    else:
        print(1 if G.same(k, u, v) else 0)
        G.update()
