# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq

from data_structure.dynamic_segtree import DynamicSegtree

n, q = map(int, input().split())
A = list(map(int, input().split()))

inf = 1 << 60
seg = DynamicSegtree(n, min, inf)
for i, a in enumerate(A):
    seg[i] = a

for _ in range(Q):
    l, r = map(int, input().split())
    print(seg.prod(l, r))
