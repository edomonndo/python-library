# verification-helper: PROBLEM https://judge.yosupo.jp/problem/general_matching

from graph.general_matching import GeneralMatching

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
solver = GeneralMatching(n, edges)
ans = solver.solve()
print(len(ans))
for u, v in ans:
    print(u, v)
