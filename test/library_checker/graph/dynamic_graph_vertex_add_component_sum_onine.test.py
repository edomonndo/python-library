# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_graph_vertex_add_component_sum

from graph.connectivity.dynamic_connectivity import DynamicConnectivity

n, k = map(int, input().split())
dc = DynamicConnectivity(n, lambda x, y: x + y, 0)
A = [int(x) for x in input().split()]
for i, a in enumerate(A):
    dc.update(i, a)
for i in range(k):
    t, *qu = map(int, input().split())
    if t == 0:
        u, v = qu
        dc.link(u, v)
    elif t == 1:
        u, v = qu
        dc.cut(u, v)
    elif t == 2:
        v, x = qu
        dc.update(v, x)
    else:
        v = qu[0]
        print(dc.get_sum(v))
