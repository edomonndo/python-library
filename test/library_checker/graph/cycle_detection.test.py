# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection

from graph.find_cycle_directed import cycle_detection

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[u].append((v, i))

cycle = cycle_detection(N, G)
if len(cycle) == 0:
    print(-1)
else:
    print(len(cycle))
    print(*cycle, sep="\n")
