from typing import Callable, TypeVar

T = TypeVar("T")


class Segtree2d:
    def __init__(
        self,
        h: int,
        w: int,
        op: Callable[[T, T], T],
        e: T,
        ps: list[tuple[int, int, T]],
    ):
        self.h = self.w = 1
        while self.h < h:
            self.h <<= 1
        while self.w < w:
            self.w <<= 1
        self.op = op
        self.e = e
        self.seg = [e for _ in range((self.h * self.w) << 2)]
        self._build(ps)

    def _id(self, h: int, w: int) -> int:
        return h * 2 * self.w + w

    def _build(self, ps: list[tuple[int, int, T]]):
        seg, _id, op = self.seg, self._id, self.op

        for h, w, x in ps:
            seg[_id(h + self.h, w + self.w)] = x

        for w in range(self.w, self.w << 1):
            for h in range(self.h - 1, 0, -1):
                seg[_id(h, w)] = op(seg[_id(h << 1, w)], seg[_id(h << 1 | 1, w)])
        for h in range(self.h << 1):
            for w in range(self.w - 1, 0, -1):
                seg[_id(h, w)] = op(seg[_id(h, w << 1)], seg[_id(h, w << 1 | 1)])

    def get(self, h: int, w: int) -> T:
        return self.seg[self._id(h + self.h, w + self.w)]

    def set(self, h: int, w: int, x: T) -> None:
        seg, _id, op = self.seg, self._id, self.op
        h += self.h
        w += self.w
        seg[_id(h, w)] = x
        i = h >> 1
        while i:
            seg[_id(i, w)] = op(seg[_id(i << 1, w)], seg[_id(i << 1 | 1, w)])
            i >>= 1
        while h:
            j = w >> 1
            while j:
                seg[_id(h, j)] = op(seg[_id(h, j << 1)], seg[_id(h, j << 1 | 1)])
                j >>= 1
            h >>= 1

    def _inner_query(self, h: int, w1: int, w2: int) -> T:
        seg, _id, op = self.seg, self._id, self.op
        res = self.e
        while w1 < w2:
            if w1 & 1:
                res = op(res, seg[_id(h, w1)])
                w1 += 1
            if w2 & 1:
                w2 -= 1
                res = op(res, seg[_id(h, w2)])
            w1 >>= 1
            w2 >>= 1
        return res

    def prod(self, h1: int, w1: int, h2: int, w2: int) -> T:
        if h1 >= h2 or w1 >= w2:
            return self.e
        op, _inner_query = self.op, self._inner_query
        res = self.e
        h1 += self.h
        h2 += self.h
        w1 += self.w
        w2 += self.w
        while h1 < h2:
            if h1 & 1:
                res = op(res, _inner_query(h1, w1, w2))
                h1 += 1
            if h2 & 1:
                h2 -= 1
                res = op(res, _inner_query(h2, w1, w2))
            h1 >>= 1
            h2 >>= 1
        return res
