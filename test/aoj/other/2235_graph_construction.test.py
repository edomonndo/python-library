# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2235

from graph.connectivity.dynamic_connectivity import DynamicConnectivity

n, q = map(int, input().split())
dc = DynamicConnectivity(n, lambda _, __: 0, 0)
for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 1:
        dc.link(u, v)
    elif t == 2:
        dc.cut(u, v)
    else:
        print("YES" if dc.same(u, v) else "NO")
