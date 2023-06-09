# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

from data_structure.segment_tree import Segtree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

INF = 1 << 60
Seg = Segtree(A, min, INF)

for _ in range(Q):
    l, r = map(int, input().split())
    print(Seg.prod(l, r))
