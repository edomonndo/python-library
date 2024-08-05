from linear_algebra.matrix import Matrix


class MatrixTreeTheorem:
    def __init__(self, n: int, undirected: bool = True, r: int = None):
        self.n = n
        self.undirected = undirected
        self.root = r
        self.adjugate_lap_mat = [[0] * (n - 1) for _ in range(n - 1)]

    def add_edge(self, u: int, v: int) -> None:
        if u == v:
            return
        g = self.adjugate_lap_mat
        if self.undirected:
            if u == self.n - 1 and v == self.n - 1:
                pass
            if u == self.n - 1:
                g[v][v] += 1
            elif v == self.n - 1:
                g[u][u] += 1
            else:
                g[v][v] += 1
                g[u][v] -= 1
                g[u][u] += 1
                g[v][u] -= 1
        else:
            if u == self.root:
                dv = v > self.root
                g[v - dv][v - dv] += 1
            elif v == self.root:
                pass
            else:
                dv, du = v > self.root, u > self.root
                g[v - dv][v - dv] += 1
                g[u - du][v - dv] -= 1

    def solve(self) -> int:
        mat = Matrix(self.n - 1, self.n - 1, self.adjugate_lap_mat)
        return mat.determinant()
