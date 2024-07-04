import random


class RandomSet:
    """0以上n未満の整数を集合で管理する. 集合に含まれる整数をランダムで出力する."""

    def __init__(self, n: int):
        """集合の上限値で初期化."""
        self.n = n
        self.size = 0
        self.dat = [-1] * n
        self.idx = [-1] * n
        self.order = []

    def __contains__(self, k: int) -> bool:
        assert 0 <= k < self.n
        return self.idx[k] != -1

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        self.count = 0
        if len(self.order) != self.size:
            self.order = [x for x in range(self.size)]
        random.shuffle(self.order)
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.size:
            raise StopIteration
        return self.dat[self.order[self.count - 1]]

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.dat[:self.size]})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(n={self.n}, size={self.size}, dat={self.dat}, idx={self.idx})"

    def add(self, k: int) -> bool:
        """集合に要素kを追加."""
        assert 0 <= k < self.n
        if self.idx[k] == -1:
            self.idx[k] = self.size
            self.dat[self.size] = k
            self.size += 1
            return True
        return False

    def remove(self, k: int) -> bool:
        """集合から要素kを削除."""
        assert 0 <= k < self.n
        if self.idx[k] != -1:
            last = self.dat[self.size - 1]
            self.dat[self.idx[k]] = last
            self.idx[last] = self.idx[k]
            self.idx[k] = -1
            self.dat[self.size - 1] = -1
            self.size -= 1
            return True
        return False

    def get(self) -> int:
        """集合からランダムに要素を取得."""
        assert self.size > 0
        return self.dat[random.randrange(0, self.size)]

    def pop(self) -> int:
        """集合からランダムに要素を取得し,集合から削除."""
        assert self.size > 0
        k = self.get()
        self.remove(k)
        return k
