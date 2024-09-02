# verification-helper: PROBLEM https://yukicoder.me/problems/no/235

from graph.tree.template import Tree
from graph.tree.heavy_light_decomposition import HLD
from data_structure.segtree.lazy_segment_tree import LazySegtree

MOD = 1_000_000_007
BS = 30
MSK = (1 << 30) - 1

ID = 0


def op(x, y):
    xs, xc = x >> BS, x & MSK
    ys, yc = y >> BS, y & MSK
    return ((xs + ys) % MOD) << BS | (xc + yc) % MOD


def mapping(f: int, x):
    s, c = x >> BS, x & MSK
    return ((s + f * c % MOD) % MOD) << BS | c


def composition(f: int, g: int) -> int:
    return (f + g) % MOD


n = int(input())
A = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
g = Tree.from_input(n, 1)
hld = HLD(n, g)
vs = hld.build_list([A[i] << BS | C[i] for i in range(n)])
seg = LazySegtree(vs, op, 0, mapping, composition, 0)

q = int(input())
for _ in range(q):
    qs = [int(x) for x in input().split()]
    if qs[0] == 0:
        u, v, w = qs[1:]
        u -= 1
        v -= 1
        for l, r in hld.path_query(u, v, False):
            seg.apply(l, r, w)
    else:
        u, v = qs[1:]
        u -= 1
        v -= 1
        ans = 0
        for l, r in hld.path_query(u, v, False):
            ans = op(ans, seg.prod(l, r))
        print(ans >> BS)
