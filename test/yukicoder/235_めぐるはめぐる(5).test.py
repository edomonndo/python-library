# verification-helper: PROBLEM https://yukicoder.me/problems/no/235


from graph.tree.heavy_light_decomposition import HeavyLightDecomposition
from data_structure.segtree.lazy_segment_tree import LazySegtree

MOD = 10**9 + 7
BS=30
MSK=(1<<30)-1

ID = 0


def op(x: S, y: S) -> S:
    xs,xc = x>>BS, x&MSK
    ys,yc = y>>BS, y&MSK
    return ((xs+ys)%MOD)<<BS | (xc+yc)%MOD

def mapping(f: int, x: S) -> S:
    s,c = x>>BS, x&MSK
    return ((s+f*c%MOD)%MOD)<<BS | c


def composition(f: int, g: int) -> int:
    return (f + g) % MOD


n = int(input())
A = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]
hld = HeavyLightDecomposition(n, edges, 0, False)
vs = hld.build_list([A[i]<<BS | C[i] for i in range(n)])
seg = LazySegtree(vs, op, 0, mapping, composition, 0)


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
        ans = 0
        hld.path_query(u, v, func, False)
        print(ans>>BS)
