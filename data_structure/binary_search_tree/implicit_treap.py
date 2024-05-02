class ImplicitTreap:
    from typing import Callable, TypeVar

    S = TypeVar("S")
    F = TypeVar("F")

    def __init__(
        self,
        op: Callable[[S, S], S],
        e: S,
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        id_: F,
        arr: list[S],
    ):
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id_
        self.rand = self.__xor64()
        self.__build(arr)

    @staticmethod
    def __xor64():
        x = 88172645463325252
        while True:
            x = x ^ ((x << 7) & 0xFFFFFFFF)
            x = x ^ (x >> 9)
            yield x & 0xFFFFFFFF

    def __build(self, arr: list[S]) -> None:
        n = len(arr)
        self.root = 0
        self.val = val = [self.e] + arr
        self.pri = pri = [1 << 32] + [next(self.rand) for _ in range(n)]
        self.ptr = ptr = [0] * (n * 3 + 3)
        self.cnt = cnt = [0] + [1] * n
        self.cum = cum = [self.e] * (n + 1)
        self.lazy = lazy = [self.id] * (n + 1)
        op = self.op
        par = [0] * (n + 1)
        for i in range(2, n + 1):
            p = i - 1
            l = 0
            while p and pri[i] > pri[p]:
                pp = par[p]
                if l:
                    par[l] = p
                par[p] = i
                l, p = p, pp
            par[i] = p
        for i, p in enumerate(par):
            if not p:
                self.root = i
            elif i < p:
                ptr[p * 3] = i
            else:
                ptr[p * 3 + 1] = i
        stack = [self.root]
        ord = []
        while stack:
            v = stack.pop()
            ord.append(v)
            l, r = ptr[v * 3], ptr[v * 3 + 1]
            if l:
                stack.append(l)
            if r:
                stack.append(r)
        for v in ord[::-1]:
            l, r = ptr[v * 3], ptr[v * 3 + 1]
            cnt[v] = cnt[l] + cnt[r] + 1
            cum[v] = op(op(cum[l], val[v]), cum[r])

    def __newnode(self, x: S) -> int:
        idx = len(self.val)
        self.val.append(x)
        self.pri.append(next(self.rand))
        self.ptr.extend([0, 0, 0])
        self.cnt.append(1)
        self.cum.append(self.e)
        self.lazy.append(self.id)
        return idx

    def __push(self, t: int) -> None:
        ptr, lazy = self.ptr, self.lazy
        if ptr[t * 3 + 2]:
            ptr[t * 3 + 2] = 0
            l, r = ptr[t * 3], ptr[t * 3 + 1] = ptr[t * 3 + 1], ptr[t * 3]
            if l:
                ptr[l * 3 + 2] ^= 1
            if r:
                ptr[r * 3 + 2] ^= 1
        if lazy[t] != self.id:
            l, r = ptr[t * 3], ptr[t * 3 + 1]
            cum, val = self.cum, self.val
            if l:
                lazy[l] = self.composition(lazy[t], lazy[l])
                cum[l] = self.mapping(lazy[t], cum[l])
            if r:
                lazy[r] = self.composition(lazy[t], lazy[r])
                cum[r] = self.mapping(lazy[t], cum[r])
            val[t] = self.mapping(lazy[t], val[t])
            lazy[t] = self.id

    def __update(self, t: int) -> None:
        ptr, cnt, cum, val = self.ptr, self.cnt, self.cum, self.val
        l, r = ptr[t * 3], ptr[t * 3 + 1]
        cnt[t] = cnt[l] + cnt[r] + 1
        cum[t] = self.op(self.op(cum[l], val[t]), cum[r])

    def __split(self, t: int, k: int, update: bool = True) -> tuple[int, int]:
        ptr, cnt = self.ptr, self.cnt
        l = r = 0
        while t:
            self.__push(t)
            p = cnt[ptr[t * 3]] + 1
            if k < p:
                v, ptr[t * 3] = ptr[t * 3], r
                r, t = t, v
            else:
                v, ptr[t * 3 + 1] = ptr[t * 3 + 1], l
                l, t = t, v
                k -= p
        s = 0
        while l:
            v, ptr[l * 3 + 1] = ptr[l * 3 + 1], s
            if update:
                self.__update(l)
            s, l = l, v
        l, s = s, 0
        while r:
            v, ptr[r * 3] = ptr[r * 3], s
            if update:
                self.__update(r)
            s, r = r, v
        r = s
        return l, r

    def __merge(
        self, l: int, r: int, push_lt: bool = False, push_rt: bool = False
    ) -> int:
        ptr, pri = self.ptr, self.pri
        s = 0
        while l:
            if push_lt:
                self.__push(l)
            v, ptr[l * 3 + 1] = ptr[l * 3 + 1], s
            s, l = l, v
        l, s = s, 0
        while r:
            if push_rt:
                self.__push(r)
            v, ptr[r * 3] = ptr[r * 3], s
            s, r = r, v
        r, s = s, 0
        while l or r:
            if pri[l] < pri[r]:
                v, ptr[l * 3 + 1] = ptr[l * 3 + 1], s
                self.__update(l)
                s, l = l, v
            else:
                v, ptr[r * 3] = ptr[r * 3], s
                self.__update(r)
                s, r = r, v
        return s

    def size(self) -> int:
        return self.cnt[self.root]

    def insert(self, p: int, x: S) -> None:
        l, r = self.__split(self.root, p + 1)
        l, _ = self.__split(l, p)
        self.root = self.__merge(self.__merge(l, self.__newnode(x)), r)

    def erase(self, p: int) -> None:
        l, r = self.__split(self.root, p + 1)
        l, _ = self.__split(l, p)
        self.root = self.__merge(l, r)

    def get(self, p: int) -> S:
        t1, t2 = self.__split(self.root, p + 1, True)
        t1, t3 = self.__split(t1, p, True)
        res = self.val[t3]
        self.root = self.__merge(self.__merge(t1, t3), t2)
        return res

    def reverse(self, l: int, r: int) -> None:
        t2, t3 = self.__split(self.root, r)
        t1, t2 = self.__split(t2, l)
        self.ptr[t2 * 3 + 2] ^= 1
        self.root = self.__merge(self.__merge(t1, t2, False, True), t3, True, False)

    def apply(self, l: int, r: int, f: F) -> None:
        t2, t3 = self.__split(self.root, r)
        t1, t2 = self.__split(t2, l)
        self.lazy[t2] = self.composition(f, self.lazy[t2])
        self.root = self.__merge(self.__merge(t1, t2, False, True), t3, True, False)

    def prod(self, l: int, r: int) -> S:
        t2, t3 = self.__split(self.root, r)
        t1, t2 = self.__split(t2, l)
        res = self.cum[t2]
        self.root = self.__merge(self.__merge(t1, t2), t3)
        return res

    def iter(self):
        stack = []
        v = self.root
        while stack or v:
            while v:
                self.__push(v)
                stack.append(v)
                v = self.ptr[v * 3]
            v = stack.pop()
            yield self.val[v]
            v = self.ptr[v * 3 + 1]
