# verification-helper: IGNORE https://atcoder.jp/contests/abc342/tasks/abc342_g

from data_structure.segtree.dual_segment_tree_commutative import DualSegtreeCommutative
from data_structure.basic.SortedMultiset import SortedMultiset


def op(f: int, S: SortedMultiset):
    if f > 0:
        S.add(f)
    elif f < 0:
        S.discard(-f)


def get(x: int, y: SortedMultiset):
    if len(y) == 0:
        return x
    else:
        return max(x, y[-1])


N = int(input())
A = [SortedMultiset([int(x)]) for x in input().split()]
seg = DualSegtreeCommutative(A, op, None, get, 0)
# 初期化時のシャローコピー回避
for i in range(seg.size):
    seg.d[i] = SortedMultiset()

Q = int(input())
history = []
for _ in range(Q):
    t, *q = map(int, input().split())
    history.append(q)
    if t == 1:
        l, r, x = q
        seg.apply(l - 1, r, x)
    elif t == 2:
        l, r, x = history[q[0] - 1]
        seg.apply(l - 1, r, -x)
    else:
        print(seg.get(q[0] - 1))
