import math
import bisect


class SortedSet:
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a=None) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a) if a is not None else []
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self):
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self):
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x) -> tuple[list, int]:
        "Find the bucket and position which x should be inserted. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                break
        return (a, bisect.bisect_left(a, x))

    def __contains__(self, x) -> bool:
        if self.size == 0:
            return False
        a, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def _pop(self, a: list, i: int):
        ans = a.pop(i)
        self.size -= 1
        if not a:
            self._build()
        return ans

    def discard(self, x) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, i)
        return True

    def lt(self, x):
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect.bisect_left(a, x) - 1]

    def le(self, x):
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect.bisect_right(a, x) - 1]

    def gt(self, x):
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect.bisect_right(a, x)]

    def ge(self, x):
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect.bisect_left(a, x)]

    def __getitem__(self, i: int):
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1):
        "Pop and return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return self._pop(a, i)
        else:
            for a in self.a:
                if i < len(a):
                    return self._pop(a, i)
                i -= len(a)
        raise IndexError

    def index(self, x) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect.bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect.bisect_right(a, x)
            ans += len(a)
        return ans
