class LinkCutTree:
    def __init__(self, op, e, arr: list[int]):
        self.op = op
        self.e = e
        self.n = n = len(arr)
        self.ptr = [-1] * (n << 2)  # l, r, p, rev
        for i in range(n):
            self.ptr[i << 2 | 3] = 0
        self.val = arr[:]
        self.sum = [e] * (n + 1)
        self.rev = [e] * (n + 1)

    def _toggle(self, v: int):
        if v == -1:
            return
        self.sum[v], self.rev[v] = self.rev[v], self.sum[v]
        self.ptr[v << 2 | 0], self.ptr[v << 2 | 1] = (
            self.ptr[v << 2 | 1],
            self.ptr[v << 2 | 0],
        )
        self.ptr[v << 2 | 3] ^= 1

    def _push(self, v: int):
        if v == -1 or not self.ptr[v << 2 | 3]:
            return
        self._toggle(self.ptr[v << 2 | 0])
        self._toggle(self.ptr[v << 2 | 1])
        self.ptr[v << 2 | 3] = 0

    def _update(self, v: int):
        self.sum[v] = self.op(
            self.op(self.sum[self.ptr[v << 2 | 0]], self.val[v]),
            self.sum[self.ptr[v << 2 | 1]],
        )
        self.rev[v] = self.op(
            self.op(self.rev[self.ptr[v << 2 | 1]], self.val[v]),
            self.rev[self.ptr[v << 2 | 0]],
        )

    def _state(self, v: int):
        p = self.ptr[v << 2 | 2]
        if self.ptr[p << 2 | 0] == v:
            return 1
        elif self.ptr[p << 2 | 1] == v:
            return -1
        else:
            return 0

    def _rotate(self, v: int):
        s = self._state(v)
        if s == 0:
            return
        ptr = self.ptr
        p = ptr[v << 2 | 2]
        pp = ptr[p << 2 | 2]
        t = self._state(p)
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
        self._update(p)
        self._update(v)
        if t == 0:
            return
        elif t == 1:
            ptr[pp << 2 | 0] = v
        else:
            ptr[pp << 2 | 1] = v

    def _splay(self, v: int):
        self._push(v)
        while True:
            s = self._state(v)
            if not s:
                break
            p = self.ptr[v << 2 | 2]
            t = self._state(p)
            if t == 0:
                self._push(p)
                self._push(v)
                self._rotate(v)
            elif s == t:
                self._push(self.ptr[p << 2 | 2])
                self._push(p)
                self._push(v)
                self._rotate(p)
                self._rotate(v)
            else:
                self._push(self.ptr[p << 2 | 2])
                self._push(p)
                self._push(v)
                self._rotate(v)
                self._rotate(v)

    def _access(self, v: int) -> int:
        c = v
        r = -1
        while v != -1:
            self._splay(v)
            self.ptr[v << 2 | 1] = r
            self._update(v)
            r = v
            v = self.ptr[v << 2 | 2]
        self._splay(c)
        return r

    def link(self, v: int, p: int) -> None:
        """頂点v,pを,pをvの親にして連結する. このときvが根である必要がある"""
        # self.evert(v)
        self._access(v)
        self._access(p)
        self.ptr[v << 2 | 2] = p
        self.ptr[p << 2 | 1] = v
        self._update(p)

    def cut(self, v: int) -> None:
        """頂点vとその親ノードとの辺を取り除く. vがその部分木の根となる."""
        self._access(v)
        self.ptr[self.ptr[v << 2 | 0] << 2 | 2] = -1
        self.ptr[v << 2 | 0] = -1
        self._update(v)

    def root(self, v: int) -> int:
        """頂点vを含む木の根を返す."""
        self._access(v)
        while self.ptr[v << 2 | 0] != -1:
            v = self.ptr[v << 2 | 0]
        return v

    def parent(self, v: int) -> int:
        """頂点vの親を返す."""
        self._access(v)
        v = self.ptr[v << 2 | 0]
        while self.ptr[v << 2 | 1] != -1:
            v = self.ptr[v << 2 | 1]
        return v

    def evert(self, v: int) -> None:
        """頂点vをvを含む木の根にする."""
        self._access(v)
        self._toggle(v)
        self._push(v)

    def set(self, v: int, x: int) -> None:
        """頂点vの値をxにする."""
        self._access(v)
        self.val[v] = x

    def add(self, v: int, x: int) -> None:
        """頂点vの値にxを加算する."""
        self._access(v)
        self.val[v] += x

    def path_query(self, u: int, v: int) -> int:
        """頂点u,v間のパスクエリを返す. ただし,uとvは連結である必要がある."""
        self.evert(u)
        self._access(v)
        return self.sum[v]

    def lca(self, u: int, v: int) -> int:
        """頂点u,vのLCAを返す. Not verified."""
        assert self.root(u) == self.root(v)
        self._access(u)
        return self._access(v)
