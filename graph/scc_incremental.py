from graph.scc import scc


def incremental_scc(n: int, edges: list[tuple[int, int]]):
    m = len(edges)
    inf = float("inf")
    merge_time = [inf] * m
    dat = [(i, u, v) for i, (u, v) in enumerate(edges)]

    st = [(0, m + 1, dat)]
    while st:
        l, r, dat = st.pop()
        mid = (l + r) >> 1
        n_ = 0
        new_idx = [-1] * n
        for _, u, v in dat:
            if new_idx[u] == -1:
                new_idx[u] = n_
                n_ += 1
            if new_idx[v] == -1:
                new_idx[v] = n_
                n_ += 1
        es = [(new_idx[u], new_idx[v]) for i, u, v in dat if i < mid]
        cc = scc(n_, es)
        comp = [0] * n_
        for i in range(len(cc)):
            for j in cc[i]:
                comp[j] = i
        dat1, dat2 = [], []
        for i, u, v in dat:
            u, v = new_idx[u], new_idx[v]
            if i < mid:
                if comp[u] == comp[v]:
                    if merge_time[i] > mid:
                        merge_time[i] = mid
                        dat1.append((i, u, v))
                else:
                    dat2.append((i, comp[u], comp[v]))
            else:
                dat2.append((i, comp[u], comp[v]))
        if dat2 and r - mid > 1:
            st.append((mid, r, dat2))
        if dat1 and mid - l > 1:
            st.append((l, mid, dat1))
    return merge_time
