from data_structure.SortedSet import SortedSet


class IntervalManager:
    class Node:
        def __init__(self, l: int, r: int, x: int):
            self.l = l
            self.r = r
            self.x = x

        def __lt__(self, other):
            if self.l == other.l:
                return self.r < other.r
            return self.l < other.l

        def __le__(self, other):
            if self.l == other.l:
                return self.r <= other.r
            else:
                return self.l <= other.l

        def __ge__(self, other):
            return not self.__lt__(other)

        def __repr__(self):
            return "[{0},{1})-{2}".format(self.l, self.r, self.x)

    inf = 10**9 + 1

    def __init__(self, arr: list[int], add, remove):
        setter = []
        n = len(arr)
        l = 0
        while l < n:
            r = l
            while r < n and arr[l] == arr[r]:
                r += 1
            setter.append(self.Node(l, r, arr[l]))
            add(l, r, arr[l])
            l = r
        self.s = SortedSet(setter)
        self._add = add
        self._remove = remove

    def _getNode(self, m: int):
        z = self.s.le(self.Node(m, self.inf, None))
        if z is not None and z.l <= m < z.r:
            return z
        return None

    def update(self, l: int, r: int, x: int):
        s = self.s
        it = s.ge(self.Node(l, 0, x))
        while it != None and it.l <= r:
            if it.l == r:
                if it.x == x:
                    self._remove(r, it.r, x)
                    r = it.r
                    _, it = s.discard(it), s.ge(it)
                break
            if it.r <= r:
                self._remove(it.l, it.r, it.x)
                _, it = s.discard(it), s.ge(it)
            else:
                if it.x == x:
                    r = it.r
                    self._remove(it.l, it.r, it.x)
                    _, it = s.discard(it), s.ge(it)
                else:
                    self._remove(it.l, r, it.x)
                    z = self.Node(r, it.r, it.x)
                    s.discard(it)
                    s.add(z)
                    it = z
        idx = s.index(it) if it != None else len(s)
        if idx:
            it = s[idx - 1]
            if it.r == l:
                if it.x == x:
                    self._remove(it.l, it.r, it.x)
                    l = it.l
                    _, it = s.discard(it), s.ge(it)
            elif l < it.r:
                if it.x == x:
                    self._remove(it.l, it.r, it.x)
                    if it.l < l:
                        l = it.l
                    if it.r > r:
                        r = it.r
                    _, it = s.discard(it), s.ge(it)
                else:
                    if r < it.r:
                        s.add(self.Node(r, it.r, it.x))
                    self._remove(l, min(r, it.r), it.x)
                    s.discard(it)
                    z = self.Node(it.l, l, it.x)
                    s.add(z)
                    it = z
        self._add(l, r, x)
        s.add(self.Node(l, r, x))

    def __repr__(self):
        return "".join(*self.s)
