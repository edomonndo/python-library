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
