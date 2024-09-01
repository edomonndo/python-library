# verification-helper: PROBLEM https://yukicoder.me/problems/no/235


from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.segtree.lazy_segment_tree import LazySegtree

MOD = 10**9 + 7


class S:
    def __init__(self, s=0, c=0):
        self.s = s % MOD
        self.c = c % MOD


ID = 0


def op(x: S, y: S) -> S:
    return S(x.s + y.s, x.c + y.c)


def mapping(f: int, x: S) -> S:
    return S(x.s + f * x.c % MOD, x.c)


def composition(f: int, g: int) -> int:
    return (f + g) % MOD


n = int(input())
A = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
hld = HeavyLightDecomposition(n, edges, 0, False)
vs = hld.build_list([S(A[i], C[i]) for i in range(n)])
seg = LazySegtree(vs, op, S(), mapping, composition, 0)


def func(l: int, r: int):
    global ans
    ans = op(ans, seg.prod(l, r))


q = int(input())
for _ in range(q):
    qs = [int(x) for x in input().split()]
    if qs[0] == 0:
        u, v, w = qs[1:]
        u -= 1
        v -= 1
        hld.path_query(u, v, lambda l, r: seg.apply(l, r, w), False)
    else:
        u, v = qs[1:]
        u -= 1
        v -= 1
        ans = S()
        hld.path_query(u, v, func, False)
        print(ans.s)
