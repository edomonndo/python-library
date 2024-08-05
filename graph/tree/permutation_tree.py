from data_structure.segtree.lazy_segment_tree import LazySegtree

inf = 1 << 30


class PermutationTree:

    class Node:
        def __init__(
            self,
            l: int = inf,
            r: int = -1,
            mn: int = inf,
            mx: int = -1,
            t: int = 0,
            par: int = -1,
        ):
            self.l = l
            self.r = r
            self.mn = mn
            self.mx = mx
            self.type = t  # 0: prime, 1: asc, -1: desc
            self.par = par

        def __str__(self):
            return f"Node<l={self.l}, r={self.r}>, p={self.par}>"

        __repr__ = __str__

    def __init__(self, P: list[int]):
        self.n = n = len(P)
        self.nodes = [self.Node(i, i + 1, P[i], P[i] + 1, 0, -1) for i in range(n)]
        # 区間加算・区間最小値
        self.seg = LazySegtree(
            [0] * n, min, inf, lambda f, x: f + x, lambda f, g: f + g, 0
        )
        self._build(P)

    def _add_child(self, v: int, p: int) -> None:
        cur, par = self.nodes[v], self.nodes[p]
        cur.par = p
        if par.l > cur.l:
            par.l = cur.l
        if par.r < cur.r:
            par.r = cur.r
        if par.mn > cur.mn:
            par.mn = cur.mn
        if par.mx < cur.mx:
            par.mx = cur.mx
        return

    def _build(self, P: list[int]) -> None:
        seg, nodes, add_child = self.seg, self.nodes, self._add_child
        mxs = [-1]
        mns = [-1]
        st = []
        for i in range(self.n):
            while mxs[-1] != -1 and P[mxs[-1]] < P[i]:
                mx = mxs.pop()
                seg.apply(mxs[len(mxs) - 1] + 1, mx + 1, P[i] - P[mx])
            while mns[-1] != -1 and P[mns[-1]] > P[i]:
                mn = mns.pop()
                seg.apply(mns[len(mns) - 1] + 1, mn + 1, P[mn] - P[i])
            mxs.append(i)
            mns.append(i)
            seg.apply(0, i, -1)
            cur = i
            while st:
                t = st[-1]
                nt, nc = nodes[t], nodes[cur]
                if (nt.type == 1 and nt.mx == nc.mn) or (
                    nt.type == -1 and nt.mn == nc.mx
                ):
                    add_child(cur, t)
                    st.pop()
                    cur = t
                elif nt.mx == nc.mn or nt.mn == nc.mx:
                    p = len(nodes)
                    nodes.append(self.Node())
                    nodes[p].type = 1 if nt.mx == nc.mn else -1
                    add_child(cur, p)
                    add_child(t, p)
                    st.pop()
                    cur = p
                elif seg.prod(0, nc.l) == 0:
                    p = len(nodes)
                    nodes.append(self.Node())
                    np = nodes[p]
                    np.type = 0
                    add_child(cur, p)
                    while True:
                        add_child(st.pop(), p)
                        if np.r - np.l == np.mx - np.mn:
                            break
                    cur = p
                else:
                    break
            st.append(cur)

        for i in range(self.n):
            nodes[i].type = 1
        return

    def par(self, v: int) -> int:
        return self.nodes[v].par

    def left(self, v: int) -> int:
        return self.nodes[v].l

    def right(self, v: int) -> int:
        return self.nodes[v].r

    def max(self, v: int) -> int:
        return self.nodes[v].mx

    def min(self, v: int) -> int:
        return self.nodes[v].mn

    def type(self, v: int) -> int:
        return self.nodes[v].type

    def size(self) -> int:
        return len(self.nodes)

    def is_lineaer(self, v: int) -> bool:
        return self.nodes[v].type != 0

    def is_prime(self, v: int) -> bool:
        return self.nodes[v].type == 0

    def gen_graph(self) -> tuple[int, list[list[int]]]:
        n = len(self.nodes)
        adj = [[] for _ in range(n)]
        for i in range(n):
            if self.nodes[i].par != -1:
                adj[self.nodes.par].append(i)
            else:
                root = i
        return root, adj


n = int(input())
P = [int(x) for x in input().split()]
pt = PermutationTree(P)
print(pt.size())
for i in range(pt.size()):
    print(
        pt.par(i),
        pt.left(i),
        pt.right(i) - 1,
        "linear" if pt.is_lineaer(i) else "prime",
    )
