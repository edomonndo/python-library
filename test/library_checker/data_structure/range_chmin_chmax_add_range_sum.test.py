# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum

from data_structure.segment_tree_beats import SegtreeBeats

N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
g = SegtreeBeats(A)
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        l, r, b = q
        g.range_ch_max(l, r, b)
    elif t == 1:
        l, r, b = q
        g.range_ch_min(l, r, b)
    elif t == 2:
        l, r, b = q
        g.range_add(l, r, b)
    else:
        l, r = q
        print(g.get_sum(l, r))
