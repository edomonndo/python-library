# verification-helper: IGNORE https://atcoder.jp/contests/abc032/tasks/abc032_d


def solve1(n: int, w: int, vs: list[int], ws: list[int]) -> int:
    """半分前列挙 n <= 30"""
    n1 = n >> 1
    n2 = n - n1

    cands1 = set()
    for bit in range(1 << n1):
        vw = [0, 0]
        for i in range(n1):
            if (bit >> i) & 1:
                vw[0] += vs[i]
                vw[1] += ws[i]
            if vw[1] <= w:
                cands1.add(tuple(vw))
    cands2 = set()
    for bit in range(1 << n2):
        vw = [0, 0]
        for i in range(n2):
            if (bit >> i) & 1:
                vw[0] += vs[i + n1]
                vw[1] += ws[i + n1]
            if vw[1] <= w:
                cands2.add(tuple(vw))
    res = 0
    for v1, w1 in cands1:
        for v2, w2 in cands2:
            if w1 + w2 <= w:
                res = max(res, v1 + v2)
    return res


def solve2(n: int, w: int, vs: list[int], ws: list[int]) -> int:
    """重さを配列で管理できるとき(w <= 10**5)"""
    dp = [0] * (w + 1)
    for v1, w1 in zip(vs, ws):
        nex = [0] * (w + 1)
        for j in range(w + 1):
            nex[j] = max(nex[j], dp[j])
            if j + w1 <= w:
                nex[j + w1] = max(nex[j + w1], dp[j] + v1)
        dp = nex
    return dp[w]


def solve3(n: int, w: int, vs: list[int], ws: list[int]) -> int:
    """価値の合計を配列で管理できるとき(mv <= 10**5)"""
    mv = sum(vs)
    inf = float("inf")
    dp = [inf] * (mv + 1)
    dp[0] = 0
    for v1, w1 in zip(vs, ws):
        nex = [inf] * (mv + 1)
        for j in range(mv + 1):
            if dp[j] == inf:
                continue
            nex[j] = min(nex[j], dp[j])
            if j + v1 <= mv:
                nex[j + v1] = min(nex[j + v1], dp[j] + w1)
        dp = nex
    for j in range(mv, -1, -1):
        if dp[j] <= w:
            return j
