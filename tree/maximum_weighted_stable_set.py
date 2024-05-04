from tree.rooted_tree import rooted_tree


def max_stable_set(adj: list[list[int]], weight=list[int]) -> int:
    n = len(adj)
    children, par = rooted_tree(adj, 0)

    deg = [0] * n
    stack = []
    for v in range(n):
        deg[v] = len(children[v])
        if deg[v] == 0:
            stack.append(v)

    # dp[0][v] := 頂点vを根とする部分木について、頂点vを含む安定集合のうち、重みの最大値
    # dp[1][v] := 頂点vを根とする部分木について、頂点vを含まない安定集合のうち、重みの最大値
    dp = [[0] * n for _ in range(2)]
    while stack:
        v = stack.pop()

        dp[0][v] = weight[v]
        for u in children[v]:
            # 頂点vを選ぶ場合、子頂点はどれも選ぶことができない
            dp[0][v] += dp[1][u]
            # 頂点vを選ばない場合、子頂点は選んでも選ばなくても構わない
            dp[1][v] += max(dp[0][u], dp[1][u])

        p = par[v]
        deg[p] -= 1
        if deg[p] == 0:
            stack.append(p)

    return max(dp[0][0], dp[1][0])
