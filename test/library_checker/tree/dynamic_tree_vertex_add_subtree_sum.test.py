# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_vertex_add_subtree_sum

from graph.connectivity.offline_dynamic_connectivity import OfflineDynamicConnectivity

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

dc = OfflineDynamicConnectivity(n)
for i, a in enumerate(A):
    dc.add_value(i, a)
dc.build(edges)

qs = [list(map(int, input().split())) for _ in range(q)]
for t, *qu in qs:
    if t == 0:
        u, v, w, x = qu
        dc.delete_edge(u, v)
        dc.add_edge(w, x)
    elif t == 1:
        dc.add_relax()
        dc.add_relax()
    else:
        v, p = qu
        dc.delete_edge(v, p)
        dc.add_edge(v, p)


def out(k):
    if k == 0:
        return
    k -= 1
    t, *qu = qs[k >> 1]
    if t == 0 or k & 1:
        return
    if t == 1:
        v, x = qu
        dc.add_value(v, x)
    else:
        v, _ = qu
        print(dc.group_sum(v))


dc.run(out)
