# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_B

from graph.mincost_arborescence import MinCostArborescence

N, M, r = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
MCA = MinCostArborescence(N, edges, r)
print(MCA.calc_min_cost())
