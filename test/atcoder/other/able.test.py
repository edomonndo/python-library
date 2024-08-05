# verification-helper: IGNORE https://atcoder.jp/contests/abl/tasks/abl_e

from data_structure.segtree.monoids_action.range_str_update_range_int_sum import *
from data_structure.segtree.lazy_segment_tree import LazySegtree


n, q = map(int, input().split())
seg = LazySegtree([S(1, 1) for _ in range(n)], op, S(), mapping, composition, F())

for _ in range(q):
    l, r, d = map(int, input().split())
    seg.apply(l - 1, r, F(d))
    print(seg.all_prod().value)
