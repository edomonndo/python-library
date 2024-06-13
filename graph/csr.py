from typing import TypeVar, Union

T = TypeVar("T")


class CSR:
    def __init__(
        self,
        n: int,
        edges: list[tuple[int, int], tuple[int, int]],
        directed: bool = False,
    ) -> None:
        self.start = [0] * (n + 1)
        m = len(edges)
        self.elist = [0] * (m if directed else m * 2)
        self.idx = dict()

        for e in edges:
            self.start[e[0] + 1] += 1
            if not directed:
                self.start[e[1] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = self.start[:]
        for e in edges:
            u, v = e[0], e[1]
            self.elist[counter[u]] = v
            self.idx[u, v] = counter[u]
            counter[u] += 1
            if not directed:
                self.elist[counter[v]] = u
                self.idx[v, u] = counter[v]
                counter[v] += 1

    def __getitem__(self, i: int) -> Union[list[int], list[tuple[int, T]]]:
        l, r = self.start[i : i + 2]
        return self.elist[l:r]


class WeightedCSR:
    def __init__(
        self,
        n: int,
        edges: list[tuple[int, int, T]],
        directed: bool = False,
        e: T = 0,
    ) -> None:
        self.start = [0] * (n + 1)
        m = len(edges)
        self.elist = [0] * (m if directed else m * 2)
        self.w = [e] * (m if directed else m * 2)
        self.e = e
        self.idx = dict()

        for e in edges:
            self.start[e[0] + 1] += 1
            if not directed:
                self.start[e[1] + 1] += 1

        for i in range(1, n + 1):
            self.start[i] += self.start[i - 1]

        counter = self.start[:]
        for e in edges:
            u, v = e[0], e[1]
            self.elist[counter[u]] = v
            self.idx[u, v] = counter[u]
            self.w[counter[u]] = e[2]
            counter[u] += 1
            if not directed:
                self.elist[counter[v]] = u
                self.idx[v, u] = counter[v]
                self.w[counter[v]] = e[2]
                counter[v] += 1

    def __getitem__(self, i: int) -> Union[list[int], list[tuple[int, T]]]:
        l, r = self.start[i : i + 2]
        return [(self.elist[j], self.w[j]) for j in range(l, r)]

    def get(self, u: int, v: int) -> T:
        # assert self.weighted
        # assert (u, v) in self.idx
        return self.w[self.idx[u, v]]

    def set(self, u: int, v: int, w: T) -> None:
        # assert self.weighted
        # assert (u, v) in self.idx
        self.w[self.idx[u, v]] = w
