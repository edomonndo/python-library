# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_path_sum
from data_structure.link_cut_tree import LinkCutTree

N, Q = map(int, input().split())
A = [int(x) for x in input().split()]
T = LinkCutTree(lambda x, y: x + y, 0, A)

for _ in range(N - 1):
    u, v = map(int, input().split())
    T.evert(u)
    T.link(u, v)

ans = []
for i in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        u, v, w, x = q
        T.evert(u)
        T.cut(v)
        T.evert(w)
        T.link(w, x)
    elif t == 1:
        p, x = q
        T.add(p, x)
    else:
        u, v = q
        ans.append(str(T.path_query(u, v)))
print(*ans, sep="\n")
