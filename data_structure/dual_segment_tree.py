class DualSegtree:
    def __init__(self, V, OP, E, MAPPING, COMPOSITION, ID):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        # 区間[0,self.size)を遅延伝播用，区間[self.size, self.size + n)が実データ
        self.d = [ID for i in range(self.size)] + [E for i in range(self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        # 遅延伝播用
        self.mapping = MAPPING
        self.composition = COMPOSITION
        self.identity = ID

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        # 遅延伝播
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = x

    def get(self, p):
        assert 0 <= p and p < self.n
        p += self.size
        # 遅延伝播
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        return self.d[p]

    def apply_point(self, p, f):
        assert 0 <= p and p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self._push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])

    def apply(self, l, r, f):
        assert 0 <= l and l <= r and r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                self._push(l >> i)
            if ((r >> i) << i) != r:
                self._push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                self._all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def _all_apply(self, k, f):
        if k < self.size:
            self.d[k] = self.composition(f, self.d[k])
        else:
            self.d[k] = self.mapping(f, self.d[k])

    def _push(self, k):
        self._all_apply(2 * k, self.d[k])
        self._all_apply(2 * k + 1, self.d[k])
        self.d[k] = self.identity
