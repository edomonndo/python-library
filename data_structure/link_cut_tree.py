from typing import Callable, TypeVar

T = TypeVar("T")


class LinkCutTree:
    def __init__(
        self,
        op: Callable[[T, T], T],
        e: T,
        arr: list[T],
        edges: list[tuple[int, int]] = None,
        root: int = 0,
    ):
        self.op = op
        self.e = e
        self.n = n = len(arr)
        self.ptr = [-1] * (n << 2)  # l, r, p, rev
        for i in range(n):
            self.ptr[i << 2 | 3] = 0
        self.val = arr[:]
        self.sum = [e] * (n + 1)
        self.rev = [e] * (n + 1)
        if edges:
            ptr = self.ptr
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            used = [0] * n
            used[root] = 1
            st = [root]
            while st:
                v = st.pop()
                for u in adj[v]:
                    if used[u]:
                        continue
                    used[u] = 1
                    ptr[u << 2 | 2] = v
                    ptr[v << 2 | 1] = u
                    st.append(u)

    def __toggle(self, v: int) -> None:
        if v == -1:
            return
        sum_, rev, ptr = self.sum, self.rev, self.ptr
        sum_[v], rev[v] = rev[v], sum_[v]
        l = v << 2
        r, rv = l + 1, l + 3
        ptr[l], ptr[r] = ptr[r], ptr[l]
        ptr[rv] ^= 1

    def __push(self, v: int) -> None:
        ptr = self.ptr
        l = v << 2
        rv = l + 3
        if v == -1 or not ptr[rv]:
            return
        r = l + 1
        self.__toggle(ptr[l])
        self.__toggle(ptr[r])
        ptr[rv] = 0

    def __update(self, v: int) -> None:
        sum_, op, ptr, val, rev = self.sum, self.op, self.ptr, self.val, self.rev
        l = v << 2
        r = l + 1
        lp, rp = ptr[l], ptr[r]
        sum_[v] = op(op(sum_[lp], val[v]), sum_[rp])
        rev[v] = op(op(rev[rp], val[v]), rev[lp])

    def __state(self, v: int) -> int:
        ptr = self.ptr
        p = ptr[v << 2 | 2]
        pl = p << 2
        if ptr[pl] == v:
            return 1
        elif ptr[pl | 1] == v:
            return -1
        else:
            return 0

    def __rotate(self, v: int) -> None:
        s = self.__state(v)
        if s == 0:
            return
        ptr = self.ptr
        p = ptr[v << 2 | 2]
        pp = ptr[p << 2 | 2]
        t = self.__state(p)
        if s == 1:
            r = ptr[v << 2 | 1]
            ptr[v << 2 | 1] = p
            ptr[p << 2 | 0] = r
            if r != -1:
                ptr[r << 2 | 2] = p
        else:
            l = ptr[v << 2 | 0]
            ptr[v << 2 | 0] = p
            ptr[p << 2 | 1] = l
            if l != -1:
                ptr[l << 2 | 2] = p
        ptr[p << 2 | 2] = v
        ptr[v << 2 | 2] = pp
        self.__update(p)
        self.__update(v)
        if t == 0:
            return
        elif t == 1:
            ptr[pp << 2 | 0] = v
        else:
            ptr[pp << 2 | 1] = v

    def __splay(self, v: int) -> None:
        ptr, push, state, rotate = self.ptr, self.__push, self.__state, self.__rotate
        push(v)
        while True:
            s = state(v)
            if not s:
                break
            p = ptr[v << 2 | 2]
            t = state(p)
            if t == 0:
                push(p)
                push(v)
                rotate(v)
            elif s == t:
                push(ptr[p << 2 | 2])
                push(p)
                push(v)
                rotate(p)
                rotate(v)
            else:
                push(ptr[p << 2 | 2])
                push(p)
                push(v)
                rotate(v)
                rotate(v)

    def __access(self, v: int) -> int:
        ptr, splay, update = self.ptr, self.__splay, self.__update
        c = v
        r = -1
        while v != -1:
            splay(v)
            ptr[v << 2 | 1] = r
            update(v)
            r = v
            v = ptr[v << 2 | 2]
        splay(c)
        return r

    def link(self, v: int, p: int) -> None:
        """頂点v,pを,pをvの親にして連結する. このときvが根である必要がある"""
        ptr, access, update = self.ptr, self.__access, self.__update
        # self.evert(v)
        access(v)
        access(p)
        ptr[v << 2 | 2] = p
        ptr[p << 2 | 1] = v
        update(p)

    def cut(self, v: int) -> None:
        """頂点vとその親ノードとの辺を取り除く. vがその部分木の根となる."""
        ptr, access, update = self.ptr, self.__access, self.__update
        access(v)
        ptr[ptr[v << 2 | 0] << 2 | 2] = -1
        ptr[v << 2 | 0] = -1
        update(v)

    def root(self, v: int) -> int:
        """頂点vを含む木の根を返す."""
        ptr, access = self.ptr, self.__access
        access(v)
        while ptr[v << 2 | 0] != -1:
            v = ptr[v << 2 | 0]
        return v

    def parent(self, v: int) -> int:
        """頂点vの親を返す."""
        ptr, access = self.ptr, self.__access
        access(v)
        v = ptr[v << 2 | 0]
        while ptr[v << 2 | 1] != -1:
            v = ptr[v << 2 | 1]
        return v

    def evert(self, v: int) -> None:
        """頂点vをvを含む木の根にする."""
        self.__access(v)
        self.__toggle(v)
        self.__push(v)

    def set(self, v: int, x: T) -> None:
        """頂点vの値をxにする."""
        self.__access(v)
        self.val[v] = x

    def add(self, v: int, x: T) -> None:
        """頂点vの値にxを加算する."""
        self.__access(v)
        self.val[v] += x

    def path_query(self, u: int, v: int) -> T:
        """頂点u,v間のパスクエリを返す. ただし,uとvは連結である必要がある."""
        self.evert(u)
        self.__access(v)
        return self.sum[v]

    def lca(self, u: int, v: int) -> int:
        """頂点u,vのLCAを返す. Not verified."""
        assert self.root(u) == self.root(v)
        self.__access(u)
        return self.__access(v)
