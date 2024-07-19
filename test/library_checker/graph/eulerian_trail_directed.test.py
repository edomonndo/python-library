# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_directed

from graph.eulerian_trail import EulerianTrail


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    g = EulerianTrail(n, edges, False)
    start, eids = g.get_edge_order()
    if start == -1:
        print("No")
    else:
        print("Yes")
        path = g.get_verticle_order(start, eids)
        print(*path)
        print(*eids)
