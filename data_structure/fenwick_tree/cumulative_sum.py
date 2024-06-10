from typing import TypeVar

T = TypeVar("T")


class CumulativeSum:
    def __init__(self, arr: list[int], e: T = 0):
        self.n = n = len(arr)
        self.e = e
        self.dat = [e for _ in range(n + 1)]
        for i in range(n):
            self.dat[i + 1] = self.dat[i] + arr[i]

    def prod(self, l: int, r: int) -> T:
        assert 0 <= l <= r <= self.n
        return self.dat[r] - self.dat[l]
