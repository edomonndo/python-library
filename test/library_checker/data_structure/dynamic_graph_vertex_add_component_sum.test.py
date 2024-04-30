# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_graph_vertex_add_component_sum

from data_structure.offline_dynamic_connectivity import OfflineDynamicConnectivity

n, q = map(int, input().split())
A = [int(x) for x in input().split()]
dc = OfflineDynamicConnectivity(n)
for i, a in enumerate(A):
    dc.add_value(i, a)
qs = [list(map(int, input().split())) for _ in range(q)]
for t, *qu in qs:
    if t == 0:
        u, v = qu
        dc.add_edge(u, v)
    elif t == 1:
        u, v = qu
        dc.delete_edge(u, v)
    else:
        dc.add_relax()


def out(k):
    t, *qu = qs[k]
    if t == 2:
        v, x = qu
        dc.uf.add(v, x)
    elif t == 3:
        v = qu[0]
        print(dc.uf.group_sum(v))


dc.run(out)
