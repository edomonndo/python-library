# verification-helper: PROBLEM https://judge.yosupo.jp/problem/line_add_get_min

from data_structure.li_chao_tree import LiChaoTree

n, q = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(n)]
queries = []
xs = []
for _ in range(q):
    t, *qu = map(int, input().split())
    if t == 0:
        a, b = qu
        queries.append((a, b))
    else:
        x = qu[0]
        xs.append(x)
        queries.append((None, x))
LCT = LiChaoTree(xs)
for a, b in lines:
    LCT.add_line(a, b)
for a, b in queries:
    if a is None:
        print(LCT.query(b))
    else:
        LCT.add_line(a, b)
