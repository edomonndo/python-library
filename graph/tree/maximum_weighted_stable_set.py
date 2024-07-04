from graph.tree.rooted_tree import rooted_tree


def max_stable_set(adj: list[list[int]], weight=list[int], r: int = 0) -> int:
    n = len(adj)

    # dp[0][v] := 頂点vを根とする部分木について、頂点vを含む安定集合のうち、重みの最大値
    # dp[1][v] := 頂点vを根とする部分木について、頂点vを含まない安定集合のうち、重みの最大値
    dp = [[0] * n for _ in range(2)]
    stack = [(~r, -1), (r, -1)]
    while stack:
        v, p = stack.pop()
        if v >= 0:
            dp[0][v] = weight[v]
            for u in adj[v]:
                if u != p:
                    stack += [(~u, v), (u, v)]
            continue
        if p == -1:
            continue
        v = ~v
        # 頂点vを選ぶ場合、子頂点はどれも選ぶことができない
        dp[0][p] += dp[1][v]
        # 頂点vを選ばない場合、子頂点は選んでも選ばなくても構わない
        dp[1][p] += max(dp[0][v], dp[1][v])

    return max(dp[0][r], dp[1][r])
