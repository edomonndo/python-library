# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc

from graph.scc import SCC

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

scc = SCC(n)
for u, v in edges:
    scc.add_edge(u, v)
ans = scc.get_mapping()
print(len(ans))
for group in ans:
    print(len(group), *group)
