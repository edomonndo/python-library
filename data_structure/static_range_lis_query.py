import sys

sys.setrecursionlimit(10**6)


def StaticRangeLISQuery(P: list[int], queries: list[tuple[int, int]]) -> list[int]:
    """
    P は 1 <= P_i <= Nの順列.
    区間[l,r)のLIS最長増加部分列を求める.
    """
    n, q = len(P), len(queries)
    mn = [0] * (1 << 20)
    size = [0] * (n + 1)

    def build(x: int, L: int, R: int) -> None:
        st = [(x, L, R)]
        while st:
            x, L, R = st.pop()
            mn[x] = n + 1
            if L == R:
                size[L] = n + 1
                continue
            m = (L + R) >> 1
            st += [(x << 1, L, m), (x << 1 | 1, m + 1, R)]

    def update(x: int, L: int, R: int, p: int) -> None:
        st = [(x, ~L, R), (x, L, R)]
        while st:
            x, L, R = st.pop()
            if L >= 0:
                if L == R:
                    mn[x] = size[p] = 0
                    continue
                m = (L + R) >> 1
                if p <= m:
                    nx = x << 1
                    st += [(nx, ~L, m), (nx, L, m)]
                else:
                    nx = x << 1 | 1
                    st += [(nx, ~(m + 1), R), (nx, m + 1, R)]
                continue
            mn[x] = min(mn[x << 1], mn[x << 1 | 1])

    def dfs(x: int, L: int, R: int, l: int, r: int) -> None:
        """ToDo 非再帰化（curの処理）"""
        nonlocal cur
        if cur <= mn[x]:
            return
        if L == R:
            size[L] = cur
            mn[x], cur = cur, mn[x]
            return
        m = (L + R) >> 1
        if l <= m:
            dfs(x * 2, L, m, l, r)
        if r > m:
            dfs(x * 2 + 1, m + 1, R, l, r)
        mn[x] = min(mn[x * 2], mn[x * 2 + 1])

    ql = [0] * (q + 1)
    qry = [[] for _ in range(n + 1)]
    for i, (l, r) in enumerate(queries, 1):
        ql[i] = l + 1
        qry[r].append(i)

    build(1, 1, n)

    ip = [0] * (n + 1)
    for i, a in enumerate(P, 1):
        ip[a] = i
    for p in ip:
        update(1, 1, n, p)
        if p < n:
            cur = p
            dfs(1, 1, n, p + 1, n)

    ans = [0] * q
    cnt = [0] * (n + 1)
    for i in range(1, n + 1):
        p = size[i] + 1
        while p <= n:
            cnt[p - 1] += 1
            p += p & -p
        for u in qry[i]:
            ret = 1 - ql[u]
            p = ql[u]
            while p:
                ret += cnt[p - 1]
                p -= p & -p
            ans[u - 1] = ret
    return ans
