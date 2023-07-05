# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection
from typing import List


def find_cycle(N: int, G: List[List[int]]) -> List[int]:
    visited = [False] * N
    finished = [False] * N
    stc = []
    for i in range(N):
        if visited[i]:
            continue
        # 非再帰dfs
        que = [(1, i, -1), (0, i, -1)]
        visited[i] = True
        while que:
            t, v, idx = que.pop()
            if t == 0:
                # 行きがけ順
                if finished[v]:
                    continue
                visited[v] = True
                stc.append((v, idx))
                for u, id in G[v]:
                    if finished[v]:
                        continue

                    if visited[u] and finished[u] == 0:
                        cycle = [id]
                        while stc:
                            v, id = stc.pop()
                            if v == u:
                                break
                            cycle.append(id)
                        return cycle[::-1]

                    elif not visited[u]:
                        que.append((1, u, id))
                        que.append((0, u, id))
            else:
                # 帰りがけ順
                if finished[v]:
                    continue
                stc.pop()
                finished[v] = True

    return []


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    G[u].append((v, i))

cycle = find_cycle(N, G)
if len(cycle) == 0:
    print(-1)
else:
    print(len(cycle))
    print(*cycle, sep="\n")
