# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching

from graph.bipartite_matching import bipartite_matching


L, R, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
match_l, match_q = bipartite_matching(L, R, edges)

matched = [(i, match_l[i]) for i in range(L) if match_l[i] != -1]
print(len(matched))
for u, v in matched:
    print(u, v)
