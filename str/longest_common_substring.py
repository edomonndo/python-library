from str.suffix_array import suffix_array, lcp_array


def find_lcs_idx(S: str, T: str) -> tuple[int, int, int, int]:
    n = len(S)
    S = S + "_" + T
    N = len(S)
    sa = suffix_array(S)
    lcp = lcp_array(S, sa)

    m = 0
    vs = [[] for _ in range(N)]
    for i in range(N - 1):
        vs[lcp[i]].append(i)
        if lcp[i] > m and (sa[i] < n) != (sa[i + 1] < n):
            m = lcp[i]
    if m > 0:
        for i in vs[m]:
            if (sa[i] < n) != (sa[i + 1] < n):
                if sa[i] < n:
                    return (sa[i], sa[i] + m, sa[i + 1] - n - 1, sa[i + 1] + m - n - 1)
                else:
                    return (sa[i + 1], sa[i + 1] + m, sa[i] - n - 1, sa[i] + m - n - 1)
    else:
        return (0, 0, 0, 0)
