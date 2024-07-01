# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection_undirected


from graph.find_cycle_undirected import cycle_detection

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    G[u].append((v, i))
    G[v].append((u, i))


cycle_v, cycle_e = cycle_detection(N, M, G)

if cycle_v:
    print(len(cycle_v))
    print(*cycle_v)
    print(*cycle_e)

else:
    print(-1)
