from typing import Union


class Tree:
    @staticmethod
    def from_input(n: int, is_1idx: bool = False) -> list[list[int]]:
        res = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = map(int, input().split())
            u -= is_1idx
            v -= is_1idx
            res[u].append(v)
            res[v].append(u)
        return res

    @staticmethod
    def from_input_weighted(
        n: int, is_1idx: bool = False
    ) -> list[list[tuple[int, int]]]:
        res = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v, w = map(int, input().split())
            u -= is_1idx
            v -= is_1idx
            res[u].append((v, w))
            res[v].append((u, w))
        return res

    @staticmethod
    def vis(adj: list[list[Union[int, tuple[int, int]]]]) -> None:
        n = len(adj)
        edges = set()
        for u in range(n):
            for e in adj[u]:
                if isinstance(e, int):
                    if u < e:
                        edges.add((u, e))
                    elif e < u:
                        edges.add((e, u))
                else:
                    v, w = e[0], e[1]
                    if u < v:
                        edges.add((u, v, w))
                    elif v < u:
                        edges.add((v, u, w))
        edges = sorted(edges)
        m = len(edges)
        assert n == m - 1
        print(n, m)
        for e in edges:
            print(*e)
