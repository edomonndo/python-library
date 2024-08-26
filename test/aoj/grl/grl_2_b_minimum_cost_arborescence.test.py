# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_B

from graph.directed_mst import directed_mst

n, m, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
eis = directed_mst(n, edges, r)
ans = 0
for ei in eis:
    ans += edges[ei][2]
print(ans)
