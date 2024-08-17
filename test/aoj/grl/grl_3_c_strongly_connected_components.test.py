# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_C

from graph.scc import scc

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

groups, comp_num = scc(n, edges)

q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    print(1 if comp_num[s] == comp_num[t] else 0)
