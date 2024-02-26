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

    def _toggle(self, u: int):
        if u == -1:
            return
        self.sum[u], self.rev[u] = self.rev[u], self.sum[u]
        self.ptr[u << 2 | 0], self.ptr[u << 2 | 1] = (
            self.ptr[u << 2 | 1],
            self.ptr[u << 2 | 0],
        )
        self.ptr[u << 2 | 3] ^= 1

    def _push(self, u: int):
        if u == -1 or not self.ptr[u << 2 | 3]:
            return
        self._toggle(self.ptr[u << 2 | 0])
        self._toggle(self.ptr[u << 2 | 1])
        self.ptr[u << 2 | 3] = 0

    def _update(self, u: int):
        self.sum[u] = self.op(
            self.op(self.sum[self.ptr[u << 2 | 0]], self.val[u]),
            self.sum[self.ptr[u << 2 | 1]],
        )
        self.rev[u] = self.op(
            self.op(self.rev[self.ptr[u << 2 | 1]], self.val[u]),
            self.rev[self.ptr[u << 2 | 0]],
        )

    def _state(self, u: int):
        p = self.ptr[u << 2 | 2]
        if self.ptr[p << 2 | 0] == u:
            return 1
        elif self.ptr[p << 2 | 1] == u:
            return -1
        else:
            return 0

    def _rotate(self, u: int):
        s = self._state(u)
        if s == 0:
            return
        ptr = self.ptr
        p = ptr[u << 2 | 2]
        pp = ptr[p << 2 | 2]
        t = self._state(p)
        if s == 1:
            r = ptr[u << 2 | 1]
            ptr[u << 2 | 1] = p
            ptr[p << 2 | 0] = r
            if r != -1:
                ptr[r << 2 | 2] = p
        else:
            l = ptr[u << 2 | 0]
            ptr[u << 2 | 0] = p
            ptr[p << 2 | 1] = l
            if l != -1:
                ptr[l << 2 | 2] = p
        ptr[p << 2 | 2] = u
        ptr[u << 2 | 2] = pp
        self._update(p)
        self._update(u)
        if t == 0:
            return
        elif t == 1:
            ptr[pp << 2 | 0] = u
        else:
            ptr[pp << 2 | 1] = u

    def _splay(self, u: int):
        self._push(u)
        while True:
            s = self._state(u)
            if not s:
                break
            p = self.ptr[u << 2 | 2]
            t = self._state(p)
            if t == 0:
                self._push(p)
                self._push(u)
                self._rotate(u)
            elif s == t:
                self._push(self.ptr[p << 2 | 2])
                self._push(p)
                self._push(u)
                self._rotate(p)
                self._rotate(u)
            else:
                self._push(self.ptr[p << 2 | 2])
                self._push(p)
                self._push(u)
                self._rotate(u)
                self._rotate(u)

    def _access(self, u: int):
        c = u
        r = -1
        while u != -1:
            self._splay(u)
            self.ptr[u << 2 | 1] = r
            self._update(u)
            r = u
            u = self.ptr[u << 2 | 2]
        self._splay(c)

    def link(self, u: int, v: int) -> None:
        self._access(u)
        self._access(v)
        self.ptr[u << 2 | 2] = v
        self.ptr[v << 2 | 1] = u
        self._update(v)

    def cut(self, u: int) -> None:
        self._access(u)
        self.ptr[self.ptr[u << 2 | 0] << 2 | 2] = -1
        self.ptr[u << 2 | 0] = -1
        self._update(u)

    def root(self, u: int) -> int:
        self._access(u)
        while self.ptr[u << 2 | 0] != -1:
            u = self.ptr[u << 2 | 0]
        return u

    def evert(self, u: int) -> None:
        self._access(u)
        self._toggle(u)
        self._push(u)

    def set(self, u: int, x: int) -> None:
        self._access(u)
        self.val[u] = x

    def add(self, u: int, x: int) -> None:
        self._access(u)
        self.val[u] += x

    def path_query(self, u: int, v: int) -> int:
        self.evert(u)
        self._access(v)
        return self.sum[v]
