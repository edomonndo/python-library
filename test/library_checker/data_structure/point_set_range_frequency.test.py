# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_frequency

from data_structure.fenwick_tree.point_set_range_frequency import PointSetRangeFrequency

n, q = map(int, input().split())
A = [int(x) for x in input().split()]

solver = PointSetRangeFrequency(A)

for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        p, x = qu
        solver.add_set_query(p, x)
    else:
        l, r, x = qu
        solver.add_freq_query(l, r, x)
print(*solver.solve(), sep="\n")
