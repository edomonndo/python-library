from collections import deque


class Grid:
    def __init__(self, h, w, C, sentinel="#"):
        self.h = h
        self.w = w + 1
        self.hw = self.h * self.w
        self.move = [1, self.w, -1, -self.w]
        self.C = []
        for row in C:
            for cell in row:
                self.C.append(cell)
            self.C.append(sentinel)
        self.sentinel = sentinel

    def __str__(self):
        res = []
        for i in range(self.h):
            for j in range(self.w - 1):
                res.append(self.C[i][j])
            res.append("\n")
        return "".join(res)

    def bfs(self, sx, sy, gx=None, gy=None):
        s = sx * self.w + sy
        if gx is not None and gy is not None:
            g = gx * self.w + gy
        else:
            g = None
        dist = [-1] * self.hw
        dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            if g and v == g:
                return dist[v]
            for dv in self.move:
                nv = v + dv
                if dist[nv] == -1 and self.C[nv] != self.sentinel:
                    dist[nv] = dist[v] + 1
                    q.append(nv)
        return dist
