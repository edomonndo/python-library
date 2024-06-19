from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))


from data_structure.fenwick_tree.fenwick_tree import FenwickTree
from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, key: int, value: T):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}, {self.value})"

    __repr__ = __str__

    def __iadd__(self, other: "Node") -> "Node":
        return __class__(self.key + other.key, self.value + other.value)

    def __isub__(self, other: "Node") -> "Node":
        return __class__(self.key - other.key, self.value - other.value)


class ValueRangeSum:

    def __init__(self, arr: list[T], max_value=200000):
        self.n = len(arr)
        self.src = arr[:]
        dat = [[] for _ in range(2)]
        self.tot = [0, 0]
        self.num = [0, 0]
        for x in arr:
            self.tot[x >= 0] += abs(x)
            self.num[x >= 0] += 1
            dat[x >= 0].append(abs(x))
        self.bit = [FenwickTree(max_value + 1, Node(0, 0)) for _ in range(2)]
        for i in range(2):
            for x in dat[i]:
                self.bit[i].add(x, Node(1, x))

    def set(self, p: int, v: T) -> None:
        """A[p] ← v"""
        c = self.src[p]
        self.src[p] = v
        ac, av = abs(c), abs(v)
        self.tot[c >= 0] -= ac
        self.num[c >= 0] -= 1
        self.bit[c >= 0].add(ac, Node(-1, -ac))
        self.tot[v >= 0] += av
        self.num[v >= 0] += 1
        self.bit[v >= 0].add(av, Node(1, av))

    def add(self, p: int, v: T) -> None:
        """A[p] += v"""
        c = self.src[p]
        self.set(p, c + v)

    def sum_lt(self, v: T) -> T:
        """Sum of A[i] where A[i] < v, 0 <= i < n"""
        if v >= 0:
            return -self.tot[0] + self.bit[1].sum0(v).value
        else:
            return -self.tot[0] + self.bit[0].sum0(-v + 1).value

    def sum_le(self, v: T) -> T:
        """Sum of A[i] where A[i] <= v, 0 <= i < n"""
        return self.sum_lt(v + 1)

    def sum_gt(self, v: T) -> T:
        """Sum of A[i] where A[i] > v, 0 <= i < n"""
        if v >= 0:
            return self.tot[1] - self.bit[1].sum0(v + 1).value
        else:
            return self.tot[1] - self.bit[0].sum0(-v).value

    def sum_ge(self, v: T) -> T:
        """Sum of A[i] where A[i] >= v, 0 <= i < n"""
        return self.sum_gt(v - 1)

    def sum_abs_from(self, v: T) -> T:
        """Sum of abs(A[i] - v) where 0 <= i < n"""
        res = 0
        if v >= 0:
            node = self.bit[1].sum0(v)
            res += self.tot[1] - self.num[1] * v - 2 * (node.value - node.key * v)
            res += v * self.num[0] + self.tot[0]
        else:
            node = self.bit[0].sum0(-v)
            res += self.tot[0] + self.num[0] * v - 2 * (node.value + node.key * v)
            res += self.tot[1] - v * self.num[1]
        return res


class CompressedValueRangeSum:

    def __init__(self, arr: list[T], possible_values: set[T], possible_vs: set[T]):
        self.src = arr[:]
        candidates = possible_values | possible_vs
        for v in possible_vs:
            candidates.add(v + 1)
            candidates.add(v - 1)
        self.to = {v: i for i, v in enumerate(sorted(candidates))}
        dat = [[] for _ in range(2)]
        self.tot = [0, 0]
        self.num = [0, 0]
        for x in arr:
            self.tot[x >= 0] += abs(x)
            self.num[x >= 0] += 1
            dat[x >= 0].append(abs(x))
        self.bit = [FenwickTree(len(self.to) + 1, Node(0, 0)) for _ in range(2)]
        for x in arr:
            self.bit[x >= 0].add(self.to[x], Node(1, abs(x)))

    def set(self, p: int, v: T) -> None:
        """A[p] ← v"""
        c = self.src[p]
        self.src[p] = v
        ac, av = abs(c), abs(v)
        self.tot[c >= 0] -= ac
        self.num[c >= 0] -= 1
        self.bit[c >= 0].add(self.to[c], Node(-1, -ac))
        self.tot[v >= 0] += av
        self.num[v >= 0] += 1
        self.bit[v >= 0].add(self.to[v], Node(1, av))

    def add(self, p: int, v: T) -> None:
        """A[p] += v"""
        c = self.src[p]
        self.set(p, c + v)

    def sum_lt(self, v: T) -> T:
        """Sum of A[i] where A[i] < v, 0 <= i < n"""
        if v >= 0:
            return -self.tot[0] + self.bit[1].sum0(self.to[v]).value
        else:
            return -self.bit[0].sum0(self.to[v]).value

    def sum_le(self, v: T) -> T:
        """Sum of A[i] where A[i] <= v, 0 <= i < n"""
        return self.sum_lt(v + 1)

    def sum_gt(self, v: T) -> T:
        """Sum of A[i] where A[i] > v, 0 <= i < n"""
        if v >= 0:
            return self.tot[1] - self.bit[1].sum0(self.to[v] + 1).value
        else:
            return self.tot[1] - self.tot[0] + self.bit[0].sum0(self.to[v]).value

    def sum_ge(self, v: T) -> T:
        """Sum of A[i] where A[i] >= v, 0 <= i < n"""
        return self.sum_gt(v - 1)

    def sum_abs_from(self, v: T) -> T:
        """Sum of abs(A[i] - v) where 0 <= i < n"""
        res = 0
        if v >= 0:
            node = self.bit[1].sum0(self.to[v])  # A[i] < v
            res += self.tot[1] - self.num[1] * v - 2 * (node.value - node.key * v)
            res += v * self.num[0] + self.tot[0]
        else:
            node = self.bit[0].sum0(self.to[v])  # A[i] < v
            res += 2 * (node.key * v + node.value) - self.num[0] * v - self.tot[0]
            res += self.tot[1] - v * self.num[1]
        return res
