# verification-helper: PROBLEM https://judge.yosupo.jp/problem/dynamic_tree_vertex_set_path_composite
from graph.connectivity.link_cut_tree import LinkCutTree

MOD = 998244353
N, Q = map(int, input().split())
A = [(a << 32) | b for a, b in (map(int, input().split()) for _ in range(N))]

mask = (1 << 32) - 1


def op(x, y):
    ax, bx = x >> 32, x & mask
    ay, by = y >> 32, y & mask
    return (ax * ay % MOD) << 32 | (ay * bx + by) % MOD


T = LinkCutTree(op, 1 << 32, A)
for _ in range(N - 1):
    u, v = map(int, input().split())
    T.evert(u)
    T.link(u, v)

ans = []
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 0:
        u, v, w, x = q
        T.evert(u)
        T.cut(v)
        T.evert(w)
        T.link(w, x)
    elif t == 1:
        p, c, d = q
        T.set(p, (c << 32) | d)
    else:
        u, v, x = q
        c = T.path_query(u, v)
        a, b = c >> 32, c & mask
        ans.append((a * x + b) % MOD)

print(*ans, sep="\n")
