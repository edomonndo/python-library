from utility.bit32_operation import *


def chromatic_number(n: int, edges: list[tuple[int, int]]) -> int:
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    dp = [0] * (1 << n)
    cur = [0] * (1 << n)

    dp[0] = 1
    for bit in range(1, 1 << n):
        v = ctz(bit)
        dp[bit] = dp[bit ^ (1 << v)] + dp[(bit ^ (1 << v)) & (~adj[v])]

    for bit in range(1 << n):
        if (n - popcount(bit)) & 1:
            cur[bit] = -1
        else:
            cur[bit] = 1

    for k in range(1, n):
        tmp = 0
        for bit in range(1 << n):
            cur[bit] *= dp[bit]
            tmp += cur[bit]
        if tmp != 0:
            res = k
            break
    else:
        res = n
    return res
