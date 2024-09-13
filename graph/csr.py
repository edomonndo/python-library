from typing import Optional


class CSR:
    def __init__(
        self,
        n: int = 0,
        start: Optional[list[int]] = None,
        elist: Optional[list[int]] = None,
    ):
        self.n = n
        self.start = start
        self.elist = elist

    @staticmethod
    def build(
        n: int,
        edges: list[tuple[int, int]],
        directed: bool = False,
    ) -> "CSR":
        start = [0] * (n + 1)
        m = len(edges)
        elist = [0] * (m if directed else m * 2)

        for e in edges:
            start[e[0] + 1] += 1
            if not directed:
                start[e[1] + 1] += 1

        for i in range(1, n + 1):
            start[i] += start[i - 1]

        counter = start[:]
        for e in edges:
            u, v = e[0], e[1]
            elist[counter[u]] = v
            counter[u] += 1
            if not directed:
                elist[counter[v]] = u
                counter[v] += 1
        return CSR(n, start, elist)

    def __len__(self) -> int:
        return self.n

    def __getitem__(self, i: int) -> list[int]:
        return self.elist[self.start[i] : self.start[i + 1]]
