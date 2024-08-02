from collections import deque


def get_ccc(adj: list[list[int]]) -> list[list[int]]:
    """Return conntected components of complement graph of adj graph."""

    n = len(adj)
    idx = [-1] * n
    flg = [0] * n
    st = list(range(n))
    cnt = 0
    while st:
        r = st.pop()
        idx[r] = cnt
        q = deque([r])
        while q:
            v = q.popleft()
            for u in adj[v]:
                flg[u] = 1
            nex = []
            for u in st:
                if flg[u]:
                    nex.append(u)
                elif idx[u] == -1:
                    idx[u] = cnt
                    q.append(u)
            for u in adj[v]:
                flg[u] = 0
            st = nex
        cnt += 1

    res = [[] for _ in range(cnt)]
    for v in range(n):
        res[idx[v]].append(v)
    return res
