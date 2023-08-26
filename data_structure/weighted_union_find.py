class WeightedUnionFind:
    def __init__(self, n, W=None):
        self.n = n
        self.parent_or_size = [-1] * n
        self.ng = [False] * n
        self.weight = [0] * n  # W_i - W_{P_i}
        self.group = n
        if W is None:
            self.W = [0] * n
        else:
            self.W = W

    # a = b + w
    def merge(self, a, b, w):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        w -= self.weight[a]
        w += self.weight[b]

        if x == y:
            if w != 0:
                self.ng[x] = True
            return x
        self.group -= 1
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            w *= -1
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        self.weight[y] = -w
        self.ng[x] |= self.ng[y]
        return x

    def same(self, a, b):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if self.parent_or_size[a] < 0:
            return a
        self.weight[a] += self.weight[self.parent_or_size[a]]
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def group_count(self):
        return self.group

    def groups(self):
        leader_buf = [0 for i in range(self.n)]
        group_size = [0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2 = []
        for i in range(self.n):
            if len(result[i]) > 0:
                result2.append(result[i])
        return result2

    def diff(self, a, b):
        if not self.same(a, b):
            return None
        else:
            return self.weight[a] - self.weight[b]

    def add(self, a, b):
        a = self.leader(a)
        self.W[a] += b

    def get(self, a):
        p = self.leader(a)
        return self.W[p] + self.diff(a, p)
