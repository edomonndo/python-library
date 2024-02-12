class PersistentArray:
    """64分木"""

    def __init__(self, n: int, init_val: int = 0, auto_update: bool = True):
        self.n = n
        self.auto_update = auto_update
        self.data = []
        self.children = []
        self.last = -1
        self.depth = 0
        self.offset = 0
        while n > 1:
            n = (n + 64 - 1) // 64  # 切り上げ除算
            self.offset += 64**self.depth
            self.depth += 1
        self.roots = []
        self._build([init_val] * self.n)

    def _build(self, V):
        assert len(V) == self.n
        self.roots.append(0)
        offset = 0
        for d in range(self.depth):
            for i in range(offset, offset + 64**d):
                self.data.append(None)
                self.children.append([0] * 64)
                for j in range(64):
                    self.children[i][j] = i * 64 + j + 1
            offset += 64**d
        for i in range(offset, offset + 64 * self.depth):
            if i - self.offset < self.n:
                self.data.append(V[i - self.offset])
            else:
                self.data.append(None)
            self.children.append(None)
        self.update()

    def get(self, t: int, p):
        assert -1 <= t <= self.last
        assert 0 <= p < self.n
        v = self.roots[t + 1]
        cur = p + self.offset
        order = []
        for _ in range(self.depth):
            cur, r = divmod(cur - 1, 64)
            order.append(r)
        for r in order[::-1]:
            v = self.children[v][r]
        return self.data[v]

    def set(self, t: int, p: int, x) -> int:
        assert -1 <= t <= self.last
        assert 0 <= p < self.n
        pv = self.roots[t + 1]
        nv = len(self.data)
        self.roots[self.last + 1] = nv
        cur = p + self.offset
        order = []
        for _ in range(self.depth):
            cur, r = divmod(cur - 1, 64)
            order.append(r)
        for r in order[::-1]:
            self.data.append(None)
            self.children.append(self.children[pv][:])
            self.children[nv][r] = nv = len(self.data)
            pv = self.children[pv][r]
        self.data.append(x)
        self.children.append(None)
        if self.auto_update:
            self.update()
        return self.last

    def update(self) -> int:
        self.roots.append(self.roots[-1])
        self.last += 1
        return self.last
