import sys

sys.setrecursionlimit(10**5)


def low_link(
    N: int, G: list[list[int]], start: int = 0
) -> tuple[list[int], list[tuple[int, int]]]:
    INF = float("inf")
    articulation = []
    bridge = []
    order = [None] * N
    low = [INF] * N

    def _dfs(cur, pre, k):
        order[cur] = low[cur] = k
        is_articulation = False
        cnt = 0
        for nxt in G[cur]:
            if order[nxt] is None:
                cnt += 1
                _dfs(nxt, cur, k + 1)
                if low[cur] > low[nxt]:
                    low[cur] = low[nxt]
                is_articulation |= pre >= 0 and low[nxt] >= order[cur]
                if order[cur] < low[nxt]:
                    if cur < nxt:
                        bridge.append((cur, nxt))
                    else:
                        bridge.append((nxt, cur))
            elif nxt != pre and low[cur] > order[nxt]:
                low[cur] = order[nxt]
        is_articulation |= pre < 0 and cnt > 1
        if is_articulation:
            articulation.append(cur)

    _dfs(start, -1, 0)

    return articulation, bridge
