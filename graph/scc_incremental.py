from graph.scc import scc


def incremental_scc(n: int, edges: list[tuple[int, int]]) -> list[int]:
    m = len(edges)
    inf = float("inf")
    merge_time = [inf] * m
    dat = [(ei, u, v) for ei, (u, v) in enumerate(edges)]

    new_idx = [-1] * n
    cnt = 1
    st = [(0, m, dat)]
    while st:
        l, r, dat = st.pop()
        mid = (l + r + 1) >> 1
        start = cnt
        for i in range(len(dat)):
            ei, u, v = dat[i]
            if new_idx[u] < start:
                new_idx[u] = cnt
                cnt += 1
            if new_idx[v] < start:
                new_idx[v] = cnt
                cnt += 1
            dat[i] = (ei, new_idx[u] - start, new_idx[v] - start)

        _, comp = scc(cnt - start, [(u, v) for ei, u, v in dat if ei < mid])
        if l + 1 == r:
            for ei, u, v in dat:
                if comp[u] == comp[v]:
                    merge_time[ei] = r
            continue
        j = 0
        k = len(dat)
        for _ in range(len(dat)):
            ei, u, v = dat[j]
            if ei < mid and comp[u] == comp[v]:
                j += 1
            else:
                dat[j] = (ei, comp[u], comp[v])
                k -= 1
                dat[j], dat[k] = dat[k], dat[j]
        st.append((mid, r, dat[j:]))
        st.append((l, mid, dat[:j]))
    return merge_time
