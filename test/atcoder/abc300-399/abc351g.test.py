# verification-helper: PROBLEM https://atcoder.jp/contests/abc351/tasks/abc351_g

from graph.tree.static_top_tree import StaticTopTree

mod = 998244353


def vertex(k):
    return 1 << 30 | A[k]


def add_edge(d):
    return d & mask


def add_vertex(d, i):
    return d << 30 | A[i]


def compress(p, c):
    x, y = p >> 30, p & mask
    z, w = c >> 30, c & mask
    return (x * z % mod) << 30 | ((x * w + y) % mod)


def rake(l, r):
    return l * r % mod


n, q = map(int, input().split())
P = [int(x) - 1 for x in input().split()]
A = [int(x) for x in input().split()]

children = [[] for _ in range(n)]
for i, p in enumerate(P, 1):
    children[p].append(i)

mask = (1 << 30) - 1
T = StaticTopTree(vertex, add_edge, add_vertex, compress, rake, 1 << 30, 1, children)

for _ in range(q):
    v, x = map(int, input().split())
    v -= 1
    A[v] = x
    while v != -1:
        T.update(v)
        v = T.parent[v]
    print(T.solve() & mask)
