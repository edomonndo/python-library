# verification-helper: IGNORE https://atcoder.jp/contests/abc185/tasks/abc185_e


def edit_distance(
    S: str | list[int],
    T: str | list[int],
    add_cost=None,
    delete_cost=None,
    replace_cost=None,
) -> int:
    n = len(S)
    m = len(T)
    inf = max(n, m)
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        dp[i][0] = i
    for j in range(m):
        dp[0][j] = j
    for i, s in enumerate(S):
        for j, t in enumerate(T):
            if s == t:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
            elif replace_cost is not None:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + replace_cost)

            if add_cost is not None:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j + 1] + add_cost)
            if delete_cost is not None:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i + 1][j] + delete_cost)
    return dp[n][m]
