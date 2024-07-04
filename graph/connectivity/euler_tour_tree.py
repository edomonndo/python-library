from functools import reduce
from typing import Callable, TypeVar

T = TypeVar("T")


class EulerTourTree:

    class Node:
        def __init__(self, l: int, r: int, e: T):
            self.par = self.left = self.right = None
            self.l, self.r, self.sz = l, r, l == r
            self.val = self.sum = e
            self.exact = self.child_exact = l < r
            self.edge_connected = self.child_edge_connected = False

        def is_root(self) -> bool:
            return self.par is None

    def __init__(self, n: int, op: Callable[[T, T], T], e: T):
        self.n = n
        self.op = op
        self.e = e
        self.ptr = [{i: self.Node(i, i, self.e)} for i in range(n)]

    def _split(self, t: Node) -> tuple[Node, Node]:
        self._splay(t)
        l = t.left
        if l:
            l.par = None
        t.left = None
        return l, self._update(t)

    def _split2(self, t: Node) -> tuple[Node, Node]:
        self._splay(t)
        l, r = t.left, t.right
        if l:
            l.par = None
        t.left = None
        if r:
            r.par = None
        t.right = None
        return l, r

    def _split3(self, s: Node, t: Node) -> tuple[Node, Node, Node]:
        a, b = self._split2(s)
        if self._same(a, t):
            c, d = self._split2(t)
            return c, d, b
        else:
            c, d = self._split2(t)
            return a, c, d

    def _merge(self, s: Node, t: Node) -> Node:
        if not s:
            return t
        if not t:
            return s
        while s.right:
            s = s.right
        self._splay(s)
        s.right = t
        if t:
            t.par = s
        return self._update(s)

    def _size(self, t: Node) -> int:
        return t.sz if t else 0

    def _update(self, t: Node) -> Node:
        t.sum = self.e
        if t.left:
            t.sum = self.op(t.left.sum, t.sum)
        if t.l == t.r:
            t.sum = self.op(t.sum, t.val)
        if t.right:
            t.sum = self.op(t.sum, t.right.sum)
        t.sz = self._size(t.left) + (t.l == t.r) + self._size(t.right)
        t.child_edge_connected = (
            (t.left.child_edge_connected if t.left else False)
            | t.edge_connected
            | (t.right.child_edge_connected if t.right else False)
        )
        t.child_exact = (
            (t.left.child_exact if t.left else False)
            | t.exact
            | (t.right.child_exact if t.right else False)
        )
        return t

    def _push(self, t: Node) -> None:
        # TODO
        pass

    def _rot(self, t: Node, b: bool) -> None:
        p = t.par
        pp = p.par
        if b:
            p.left = t.right
            if p.left:
                t.right.par = p
            t.right = p
        else:
            p.right = t.left
            if p.right:
                t.left.par = p
            t.left = p
        p.par = t
        self._update(p)
        self._update(t)
        t.par = pp
        if t.par:
            if pp.left == p:
                pp.left = t
            if pp.right == p:
                pp.right = t
            self._update(pp)

    def _splay(self, t: Node) -> None:
        self._push(t)
        while not t.is_root():
            p = t.par
            if p.is_root():
                self._push(p)
                self._push(t)
                self._rot(t, p.left == t)
            else:
                pp = p.par
                self._push(pp)
                self._push(p)
                self._push(t)
                b1 = pp.left == p
                b2 = (p.left == t) if b1 else (p.right == t)
                if b2:
                    self._rot(p, b1)
                    self._rot(t, b1)
                else:
                    self._rot(t, not b1)
                    self._rot(t, b1)

    def _get_node(self, l: int, r: int) -> Node:
        if r not in self.ptr[l]:
            self.ptr[l][r] = self.Node(l, r, self.e)
        return self.ptr[l][r]

    @staticmethod
    def _root(t: Node) -> Node:
        if not t:
            return t
        while t.par:
            t = t.par
        return t

    def _same(self, s: Node, t: Node) -> bool:
        if s:
            self._splay(s)
        if t:
            self._splay(t)
        return self._root(s) == self._root(t)

    def _reroot(self, t: Node) -> Node:
        l, r = self._split(t)
        return self._merge(r, l)

    def size(self, v: int) -> int:
        t = self._get_node(v, v)
        self._splay(t)
        return t.sz

    def same(self, u: int, v: int) -> bool:
        return self._same(self._get_node(u, u), self._get_node(v, v))

    def update(self, v: int, x: T) -> Node:
        t = self._get_node(v, v)
        self._splay(t)
        t.val = self.op(t.val, x)
        self._update(t)

    def edge_update(self, v: int, op: Callable[[int, int], None]) -> None:
        t = self._get_node(v, v)
        self._splay(t)
        while t and t.child_exact:
            c = t
            st = [c]
            while st:
                c = st.pop()
                if c.l < c.r and c.exact:
                    self._splay(c)
                    c.exact = False
                    self._update(c)
                    op(c.l, c.r)
                    continue
                if c.left and c.left.child_exact:
                    st.append(c.left)
                else:
                    st.append(c.right)
            self._splay(t)

    def try_reconnect(self, v: int, op: Callable[[int], bool]) -> bool:
        t = self._get_node(v, v)
        self._splay(t)
        while t.child_edge_connected:
            flag = False
            c = t
            st = [c]
            while st:
                c = st.pop()
                if c.edge_connected:
                    self._splay(c)
                    flag = op(c.l)
                    continue
                if c.left and c.left.child_edge_connected:
                    st.append(c.left)
                else:
                    st.append(c.right)
            if flag:
                return True
            self._splay(t)
        return False

    def edge_connected_update(self, v: int, b: bool) -> None:
        t = self._get_node(v, v)
        self._splay(t)
        t.edge_connected = b
        self._update(t)

    def link(self, l: int, r: int) -> bool:
        if self.same(l, r):
            return False
        ll, lr = self._get_node(l, l), self._get_node(l, r)
        rr, rl = self._get_node(r, r), self._get_node(r, l)
        reduce(self._merge, [self._reroot(ll), lr, self._reroot(rr), rl])
        return True

    def cut(self, l: int, r: int) -> bool:
        ptr = self.ptr
        if r not in ptr[l]:
            return False
        s, _, u = self._split3(self._get_node(l, r), self._get_node(r, l))
        self._merge(s, u)
        ptr[l].pop(r)
        ptr[r].pop(l)
        return True

    def get_sum_edge(self, p: int, v: int) -> T:
        self.cut(p, v)
        t = self._get_node(v, v)
        self._splay(t)
        res = t.sum
        self.link(p, v)
        return res

    def get_sum(self, v: int) -> T:
        t = self._get_node(v, v)
        self._splay(t)
        return t.sum
