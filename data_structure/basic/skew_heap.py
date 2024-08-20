from typing import Optional


class SHNode:
    def __init__(self, val: int):
        self.l = None
        self.r = None
        self.val = val
        self.lazy = 0

    def lazy_propagate(self):
        if self.l is not None:
            self.l.lazy += self.lazy
        if self.r is not None:
            self.r.lazy += self.lazy
        self.val += self.lazy
        self.lazy = 0


class SkewHeap:
    def __init__(self):
        self.root = None

    def _meld(self, a: Optional[SHNode], b: Optional[SHNode]) -> SHNode:
        if a is None:
            return b
        if b is None:
            return a
        if b.val + b.lazy < a.val + a.lazy:
            a, b = b, a
        a.lazy_propagate()
        a.r = self._meld(a.r, b)
        a.l, a.r = a.r, a.l
        return a

    @property
    def min(self) -> int:
        self.root.lazy_propagate()
        return self.root.val

    def push(self, val: int) -> None:
        node = SHNode(val)
        self.root = self._meld(self.root, node)

    def pop(self) -> int:
        root = self.root
        root.lazy_propagate()
        self.root = self._meld(root.l, root.r)
        return root.val

    def meld(self, other: "SkewHeap") -> None:
        self.root = self._meld(self.root, other.root)

    def add(self, val: int) -> None:
        self.root.lazy += val

    def empty(self) -> bool:
        return self.root is None
