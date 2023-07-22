class WeightedUnionFind:
    def __init__(self, n, W=[]):
        self.n = n
        self.parents = [-1] * n
        self.ng = [False] * n
        self.weight = [0] * n  # W_i - W_{P_i}
        self.group = n
        if W:
            self.W = W[:]
        else:
            self.W = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            p = self.find(self.parents[x])
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = p
            return self.parents[x]

    # x = y + w
    def union(self, x, y, w):
        xp = self.find(x)
        yp = self.find(y)
        w -= self.weight[x]
        x = xp
        w += self.weight[y]
        y = yp

        if x == y:
            if w != 0:
                self.ng[x] = True
            return False
        self.group -= 1

        if self.parents[x] > self.parents[y]:
            w *= -1
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.weight[y] = -w
        self.parents[y] = x
        self.ng[x] |= self.ng[y]
        return True

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        if not self.same(x, y):
            return None
        else:
            return self.weight[x] - self.weight[y]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return self.group

    def all_group_members(self):
        dic = {r: [] for r in self.roots()}
        for i in range(self.n):
            dic[self.find(i)].append(i)
        return dic

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())

    def add(self, a, b):
        a = self.find(a)
        self.W[a] += b

    def get(self, a):
        p = self.find(a)
        return self.W[p] + self.diff(a, p)
