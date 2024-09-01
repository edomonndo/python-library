# verification-helper: PROBLEM https://yukicoder.me/problems/no/235


from graph.tree.hld_lazysegtree import HldLazySegTree

MOD = 1_000_000_007


class S:
    def __init__(self, s=0, c=0):
        self.s = s % MOD
        self.c = c % MOD


ID = 0


def op(x: S, y: S) -> S:
    return S(x.s + y.s, x.c * y.c)


def mapping(f: int, x: S) -> S:
    if f == ID:
        return x
    return S(x.s + f * x.c, x.c)


def composition(f: int, g: int) -> int:
    return f + g


n = int(input())
A = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
edges = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

seg = HldLazySegTree(
    op, S(), mapping, composition, 0, [S(A[i], C[i]) for i in range(n)], n, edges, 0
)

q = int(input())
ans = 0
for _ in range(q):
    qs = [int(x) for x in input().split()]
    if qs[0] == 0:
        u, v, w = qs[1:]
        seg.path_apply(u - 1, v - 1, w, False)
    else:
        u, v = qs[1:]
        print(seg.path_prod(u - 1, v - 1, False).s)
