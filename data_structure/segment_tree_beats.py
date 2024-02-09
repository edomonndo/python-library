class SegtreeBeats:
    inf = float("inf")

    def __init__(self, V):
        self.n = len(V)
        self.log = (self.n - 1).bit_length()
        self.size = size = 1 << self.log
        size2 = size << 1
        self.fmax = [-self.inf] * size2
        self.fmin = [self.inf] * size2
        self.smax = [-self.inf] * size2
        self.smin = [self.inf] * size2
        self.maxc = [0] * size2
        self.minc = [0] * size2
        self.sum = [0] * size2
        self.add = [0] * size2
        self.upd = [self.inf] * size2
        self.up = []
        self.down = []
        self.lt = [0] * size2
        self.rt = [0] * size2
        for i in range(self.n):
            self.lt[size + i] = i
            self.rt[size + i] = i + 1
        for i in reversed(range(size)):
            self.lt[i] = self.lt[i << i]
            self.rt[i] = self.rt[(i << 1) | 1]
        if V:
            for i, x in enumerate(V):
                self.fmax[size + i] = x
                self.fmin[size + i] = x
                self.maxc[size + i] = 1
                self.minc[size + i] = 1
                self.sum[size + i] = x
            for i in range(1, size):
                self._merge(i)

    def _merge(self, i):
        cl, cr = i << 1, (i << 1) | 1
        a, b = self.fmax[cl], self.fmax[cr]
        if a < b:
            self.fmax[i] = b
            self.maxc[i] = self.maxc[cr]
            self.smax[i] = max(a, self.smax[cr])
        elif a > b:
            self.fmax[i] = a
            self.maxc[i] = self.maxc[cl]
            self.smax[i] = max(b, self.smax[cl])
        else:
            self.fmax[i] = a
            self.maxc[i] = self.maxc[cl] + self.maxc[cr]
            self.smax[i] = max(self.smax[cl], self.smax[cr])
        a, b = self.fmin[cl], self.fmin[cr]
        if a > b:
            self.fmin[i] = b
            self.minc[i] = self.minc[cr]
            self.smin[i] = min(a, self.smin[cr])
        elif a < b:
            self.fmin[i] = a
            self.minc[i] = self.minc[cl]
            self.smin[i] = min(b, self.smin[cl])
        else:
            self.fmin[i] = a
            self.minc[i] = self.minc[cl] + self.minc[cr]
            self.smin[i] = min(self.smin[cl], self.smin[cr])

    def _up_merge(self):
        while self.up:
            i = self.up.pop()
            self._merge(i)

    def _update(self, i, x):
        a, b = self.lt[i], self.rt[i]
        self.fmax[i] = x
        self.smax[i] = -self.inf
        self.fmin[i] = x
        self.smin[i] = self.inf
        self.maxc[i] = b - a
        self.minc[i] = b - a
        self.sum[i] = x * (b - a)
        self.add[i] = 0
        self.upd[i] = x

    def _add(self, i, x):
        self.fmax[i] += x
        if self.smax[i] != -self.inf:
            self.smax[i] += x
        self.fmin[i] += x
        if self.smin[i] != self.inf:
            self.smin[i] += x
        self.sum[i] += x * (self.rt[i] - self.lt[i])
        if self.upd[i] != self.inf:
            self.upd[i] += x
        else:
            self.add[i] += x

    def _chmax(self, i, x):
        a = self.fmax[i]
        self.sum[i] += self.maxc[i] * (x - a)
        self.fmax[i] = x
        if a == self.fmin[i]:
            self.fmin[i] = x
        elif a == self.smin[i]:
            self.smin[i] = x
        a = self.upd[i]
        if a != self.inf and x < a:
            self.upd[i] = x

    def _chmin(self, i, x):
        a = self.fmin[i]
        self.sum[i] += self.minc[i] * (x - a)
        self.fmin[i] = x
        if a == self.fmax[i]:
            self.fmax[i] = x
        elif a == self.smax[i]:
            self.smax[i] = x
        a = self.upd[i]
        if a != self.inf and x > a:
            self.upd[i] = x

    def _down_propagate(self, i):
        if i >= self.size:
            return
        x = self.upd[i]
        cl, cr = i << 1, (i << 1) | 1
        if x != self.inf:
            self._update(cl, x)
            self._update(cr, x)
            self.add[i] = 0
        else:
            x = self.add[i]
            if x:
                self._add(cl, x)
                self._add(cr, x)
                self.add[i] = 0
            a, b = self.fmax[i], self.fmin[i]
            if a < self.fmax[cl]:
                self._chmax(cl, a)
            if b > self.fmin[cl]:
                self._chmin(cl, b)
            if a < self.fmax[cr]:
                self._chmax(cr, a)
            if b > self.fmin[cr]:
                self._chmin(cr, b)

    def range_ch_max(self, l, r, x):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l or x <= self.fmin[i]:
                continue
            if l <= self.lt[i] and self.rt[i] <= r and x < self.smin[i]:
                self._chmin(i, x)
                continue
            self._down_propagate(i)
            self.up.append(i)
        self._up_merge()

    def range_ch_min(self, l, r, x):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l or x >= self.fmax[i]:
                continue
            if l <= self.lt[i] and self.rt[i] <= r and x > self.smax[i]:
                self._chmax(i, x)
                continue
            self._down_propagate(i)
            self.up.append(i)
        self._up_merge()

    def range_add(self, l, r, x):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l:
                continue
            if l <= self.lt[i] and self.rt[i] <= r:
                self._add(i, x)
                continue
            self._down_propagate(i)
            self.up.append(i)
        self._up_merge()

    def range_update(self, l, r, x):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l:
                continue
            if l <= self.lt[i] and self.rt[i] <= r:
                self._update(i, x)
                continue
            self._down_propagate(i)
            self.up.append(i)
        self._up_merge()

    def get_max(self, l, r):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        res = -self.inf
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l:
                continue
            if l <= self.lt[i] and self.rt[i] <= r:
                res = max(res, self.fmax[i])
                continue
            self._down_propagate(i)
        return res

    def get_min(self, l, r):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        res = self.inf
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l:
                continue
            if l <= self.lt[i] and self.rt[i] <= r:
                res = min(res, self.fmin[i])
                continue
            self._down_propagate(i)
        return res

    def get_sum(self, l, r):
        assert 0 <= l and l < r and r <= self.n
        self.down.append(1)
        res = 0
        while self.down:
            i = self.down.pop()
            if r <= self.lt[i] or self.rt[i] <= l:
                continue
            if l <= self.lt[i] and self.rt[i] <= r:
                res += self.sum[i]
                continue
            self._down_propagate(i)
        return res

    def set(self, p, x):
        assert 0 <= p and p < self.n
        self.range_update(p, p + 1, x)

    def get(self, p):
        assert 0 <= p and p < self.n
        return self.get_sum(p, p + 1)

    def update(self, p, x):
        assert 0 <= p and p < self.n
        self.range_update(p, p + 1, x)

    def chmin(self, p, x):
        assert 0 <= p and p < self.n
        self.range_chmin(p, p + 1, x)

    def chmax(self, p, x):
        assert 0 <= p and p < self.n
        self.range_chmax(p, p + 1, x)

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])
