# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C

from graph.scc import SCC

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

scc = SCC(n)
for u, v in edges:
    scc.add_edge(u, v)
cc = scc.get_mapping()
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    print(1 if cc[s] == cc[t] else 0)
