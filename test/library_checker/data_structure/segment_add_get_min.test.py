# verification-helper: PROBLEM https://judge.yosupo.jp/problem/segment_add_get_min

from data_structure.li_chao_tree import LiChaoTree

n, q = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(n)]
qs = []
inf = 1 << 60
xs = []
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        l, r, a, b = qu
        qs.append((0, a, b, l, r))
    else:
        x = qu[0]
        xs.append(x)
        qs.append((1, x))

LCT = LiChaoTree(xs, inf)
for l, r, a, b in lines:
    LCT.add_segment(a, b, l, r - 1)
for i in range(q):
    if qs[i][0] == 0:
        _, a, b, l, r = qs[i]
        LCT.add_segment(a, b, l, r - 1)
    else:
        x = qs[i][1]
        res = LCT.query(x)
        if res == inf:
            print("INFINITY")
        else:
            print(res)
