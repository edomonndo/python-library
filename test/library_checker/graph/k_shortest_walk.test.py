# verification-helper: PROBLEM https://judge.yosupo.jp/problem/k_shortest_walk

from graph.shortest_paths import shortest_paths

n, m, s, t, k = map(int, input().split())
es = [tuple(map(int, input().split())) for _ in range(m)]
ans = shortest_paths(n, es, s, t, k)
while len(ans) < k:
    ans.append(-1)
print(*ans, sep="\n")
