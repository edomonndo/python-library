# verification-helper: PROBLEM https://judge.yosupo.jp/problem/general_weighted_matching

from graph.general_weighted_matching import GeneralWeightedMatching


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

solver = GeneralWeightedMatching(n, edges)
ans, cnt = solver.solve()
print(cnt, ans)
for v in range(n):
    u = solver.match[v]
    if u > v:
        print(v, u)
