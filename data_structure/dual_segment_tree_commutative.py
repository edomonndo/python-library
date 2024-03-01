class DualSegtreeCommutative:
    def __init__(self, V, OP, ID, GET, E):
        self.n = n = len(V)
        log = (n - 1).bit_length()
        self.size = 1 << log
        # 区間[0,self.size)を遅延伝播用，区間[self.size, self.size + n)が実データ
        self.d = [ID for _ in range(2 * self.size)]
        for i in range(n):
            self.d[self.size + i] = V[i]
        self.op = OP
        self.identity = ID
        self._get = GET
        self.e = E

    def get(self, p: int):
        assert 0 <= p and p < self.n
        res = self.e
        p += self.size
        while p:
            res = self._get(res, self.d[p])
            p >>= 1
        return res

    def apply(self, l: int, r: int, f):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                self.op(f, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                self.op(f, self.d[r])
            l >>= 1
            r >>= 1
