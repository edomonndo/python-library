def find_cycle(
    N: int, M: int, G: list[list[int]]
) -> tuple[int, int, int, list[int], list[int]]:
    visited = [0] * N
    finished = [0] * M
    par_v = [None] * N
    par_e = [None] * N

    for i in range(N):
        if visited[i]:
            continue
        stack = [(i, -1, -1)]
        while stack:
            v, p, e = stack.pop()  # v: 頂点番号､p: vの親頂点,e: vと接続する辺
            if e != -1 and finished[e]:
                continue
            if visited[v]:
                par_v[v] = p
                if e != -1:
                    par_e[v] = e
                return v, p, e, par_v, par_e
            visited[v] = 1
            if e != -1:
                par_e[v] = e
                finished[e] = 1
            par_v[v] = p
            for u, e in G[v]:
                if finished[e]:
                    continue
                stack.append((u, v, e))

    return -1, -1, -1, par_v, par_e


def cycle_detection(N: int, M: int, G: list[int]):

    v, p, e, par_v, par_e = find_cycle(N, M, G)
    if p == -1:
        return [], []
    else:
        cycle_v = [p]
        cycle_e = [e]
        while v != p:
            e = par_e[p]
            p = par_v[p]
            cycle_v.append(p)
            cycle_e.append(e)
        return cycle_v[::-1], cycle_e[::-1]
