class LinkCutTree:
    def __init__(self, op, e, arr: list[int]):
        self.op = op
        self.op = e
        self.n = n = len(arr)
        self.ptr = [-1] * (n << 2)  # l, r, p, rev
        for i in range(n):
            self.ptr[i << 2 | 3] = 0
        self.val = arr[:]
        self.sum = [e] * (n + 1)
        self.rev = [e] * (n + 1)

    def _toggle(self, u: int):
        if u != -1:
            return
        self.sum[u], self.rev[u] = self.rev[u], self.sum[u]
        self.ptr[u << 2 | 0], self.ptr[u << 2 | 1] = (
            self.ptr[u << 2 | 1],
            self.ptr[u << 2 | 0],
        )
        self.ptr[u << 2 | 3] ^= 1

    def _push(self, u: int):
        if self.ptr[u << 2 | 3]:
            self._toggle(self.ptr[u << 2 | 0])
            self._toggle(self.ptr[u << 2 | 1])
            self.ptr[u << 2 | 3] = 0

    def _update(self, u: int):
        self.sum[u] = self.op(
            self.val[u],
            self.op(self.sum[self.ptr[u << 2 | 0]], self.sum[self.ptr[u << 2 | 1]]),
        )
        self.rev[u] = self.op(
            self.rev[u],
            self.op(self.rev[self.ptr[u << 2 | 0]], self.rev[self.ptr[u << 2 | 1]]),
        )

    def _state(self, u: int):
        par = self.ptr[u << 2 | 2]
        if par == -1 or (self.ptr[par << 2 | 0] != u and self.ptr[par << 2 | 1] != u):
            return 0
        elif self.ptr[par << 2 | 0] == u:
            return 1
        return -1

    def _rotate(self, u: int):
        ptr = self.ptr
        par = ptr[u << 2 | 2]
        parpar = ptr[par << 2 | 2]
        if ptr[par << 2 | 0] == u:
            c = ptr[u << 2 | 1]
            ptr[u << 2 | 1] = par
            ptr[par << 2 | 0] = c
        else:
            c = ptr[u << 2 | 0]
            ptr[u << 2 | 0] = par
            ptr[par << 2 | 1] = c
        if parpar != -1:
            if ptr[parpar << 2 | 0] == par:
                ptr[parpar << 2 | 0] = u
            if ptr[parpar << 2 | 1] == par:
                ptr[parpar << 2 | 1] = u
        ptr[u << 2 | 2] = parpar
        ptr[par << 2 | 2] = u
        if c != -1:
            ptr[c << 2 | 2] = par
        self._update(par)
        self._update(u)
        return u

    def _splay(self, u: int):
        self._push(u)
        while self._state(u) != 0:
            par = self.ptr[u << 2 | 2]
            if self._state(par) == 0:
                self._push(par)
                self._push(u)
                self._rotate(u)
            elif self._state(u) == self._state(par):
                self._push(self.ptr[par << 2 | 2])
                self._push(par)
                self._push(u)
                self._rotate(par)
                self._rotate(u)
            else:
                self._push(self.ptr[par << 2 | 2])
                self._push(par)
                self._push(u)
                self._rotate(u)
                self._rotate(u)

    def _access(self, u: int):
        cur = u
        r_cur = -1
        while cur != -1:
            self._splay(cur)
            self.ptr[cur << 2 | 1] = r_cur
            self._update(cur)
            r_cur = cur
            cur = self.ptr[cur << 2 | 2]
        self._splay(u)

    def link(self, u: int, v: int) -> None:
        self._access(u)
        self._access(v)
        self.ptr[u << 2 | 2] = v
        self.ptr[u << 2 | 1] = u
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
