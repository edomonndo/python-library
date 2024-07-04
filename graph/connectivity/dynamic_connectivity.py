from typing import Callable, TypeVar

T = TypeVar("T")

from graph.connectivity.euler_tour_tree import EulerTourTree


class DynamicConnectivity:
    def __init__(self, n: int, op: Callable[[T, T], T], e: T):
        self.n = n
        self.ett = [EulerTourTree(n, op, e)]
        self.edges = [[set() for _ in range(n)]]
        self.depth = 1
        self.op = op
        self.e = e

    def link(self, u: int, v: int) -> bool:
        ett, edges = self.ett, self.edges
        if u == v:
            return False
        if ett[0].link(u, v):
            return True
        edges[0][u].add(v)
        edges[0][v].add(u)
        if len(edges[0][u]) == 1:
            ett[0].edge_connected_update(u, True)
        if len(edges[0][v]) == 1:
            ett[0].edge_connected_update(v, True)
        return False

    def same(self, u: int, v: int) -> bool:
        return self.ett[0].same(u, v)

    def size(self, v: int) -> int:
        return self.ett[0].size(v)

    def cut(self, u: int, v: int) -> bool:
        ett, edges = self.ett, self.edges
        if u == v:
            return False
        for i in range(self.depth):
            edges[i][u].discard(v)
            edges[i][v].discard(u)
            if len(edges[i][u]) == 0:
                ett[i].edge_connected_update(u, False)
            if len(edges[i][v]) == 0:
                ett[i].edge_connected_update(v, False)
        for i in range(self.depth - 1, -1, -1):
            if ett[i].cut(u, v):
                if self.depth - 1 == i:
                    self.depth += 1
                    ett.append(EulerTourTree(self.n, self.op, self.e))
                    edges.append([set() for _ in range(self.n)])
                return not self.try_reconnect(u, v, i)
        return False

    def try_reconnect(self, u: int, v: int, k: int) -> bool:
        ett, edges = self.ett, self.edges

        def op1(s: int, t: int) -> None:
            ett[i + 1].link(s, t)

        def op2(x: int) -> bool:
            arr = list(edges[i][x])
            for y in arr:
                edges[i][x].discard(y)
                edges[i][y].discard(x)
                if len(edges[i][x]) == 0:
                    ett[i].edge_connected_update(x, False)
                if len(edges[i][y]) == 0:
                    ett[i].edge_connected_update(y, False)
                if ett[i].same(x, y):
                    edges[i + 1][x].add(y)
                    edges[i + 1][y].add(x)
                    if len(edges[i + 1][x]) == 1:
                        ett[i + 1].edge_connected_update(x, True)
                    if len(edges[i + 1][y]) == 1:
                        ett[i + 1].edge_connected_update(y, True)
                else:
                    for j in range(i + 1):
                        ett[j].link(x, y)
                    return True
            return False

        for i in range(k):
            ett[i].cut(u, v)
        for i in range(k, -1, -1):
            if ett[i].size(u) > ett[i].size(v):
                u, v = v, u
            ett[i].edge_update(u, op1)
            if ett[i].try_reconnect(u, op2):
                return True
        return False

    def update(self, v: int, x: T) -> None:
        self.ett[0].update(v, x)

    def get_sum(self, v: int) -> T:
        return self.ett[0].get_sum(v)
