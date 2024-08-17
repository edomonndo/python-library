# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc

from graph.scc import scc

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

groups, _ = scc(n, edges)
print(len(groups))
for group in groups:
    print(len(group), *group)
