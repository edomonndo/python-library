MOD = 998244353

from collections import defaultdict


def solve(A: list[int]) -> int:
    n = len(A)

    dp = defaultdict(int)
    ans = 1

    for a in A:
        tmp = dp[a]
        dp[a] = ans
        ans = (ans * 2 - tmp) % MOD

    # 空列は含めない
    return (ans - 1) % MOD
