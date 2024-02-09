class BinaryTrie:
    def __init__(self, max_query=5 * 10**5, max_log=30):
        n = max_query * max_log
        self.nodes = [0] * (2 * n)
        self.size = [0] * n
        self.id = 0
        self.max_log = max_log

    def add(self, x):
        v = 0
        stack = [v]
        for i in reversed(range(self.max_log)):
            c = (x >> i) & 1
            if self.nodes[2 * v + c] == 0:
                self.id += 1
                self.nodes[2 * v + c] = self.id
            v = self.nodes[2 * v + c]
            stack.append(v)
        if self.size[v]:
            return
        for v in stack:
            self.size[v] += 1

    def remove(self, x):
        v = 0
        stack = [v]
        for i in reversed(range(self.max_log)):
            c = (x >> i) & 1
            if self.nodes[2 * v + c] == 0:
                return
            v = self.nodes[2 * v + c]
            stack.append(v)
        while len(stack) > 1:
            if self.size[stack[-1]] > 1:
                break
            v = stack.pop()
            nv = stack[-1]
            if self.nodes[2 * nv] == v:
                self.nodes[2 * nv] = 0
            else:
                self.nodes[2 * nv + 1] = 0
        for v in stack:
            self.size[v] -= 1

    def __contains__(self, item):
        v = 0
        for i in reversed(range(self.max_log)):
            c = (item >> i) & 1
            if self.nodes[2 * v + c] == 0:
                return False
            v = self.nodes[2 * v + c]
        return True

    def max(self):
        v = 0
        if self.size[v] == 0:
            return -1
        res = 0
        for i in reversed(range(self.max_log)):
            if self.nodes[2 * v + 1] == 0:
                v = self.nodes[2 * v]
            else:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
        return res

    def min(self):
        v = 0
        if self.size[v] == 0:
            return -1
        res = 0
        for i in reversed(range(self.max_log)):
            if self.nodes[2 * v] == 0:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
            else:
                v = self.nodes[2 * v]
        return res

    def xor_max(self, x):
        v = 0
        if self.size[v] == 0:
            return -1
        for i in reversed(range(self.max_log)):
            if self.nodes[2 * v + 1] == 0:
                v = self.nodes[2 * v]
                continue
            if self.nodes[v][0] == 0:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
                continue
            if (x >> i) & 1:
                v = self.nodes[2 * v]
            else:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
        return res

    def xor_min(self, x):
        v = 0
        if self.size[v] == 0:
            return -1
        res = 0
        for i in reversed(range(self.max_log)):
            if self.nodes[2 * v] == 0:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
                continue
            if self.nodes[2 * v + 1] == 0:
                v = self.nodes[2 * v]
                continue
            if (x >> i) & 1:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
            else:
                v = self.nodes[2 * v]
        return res

    def bisect_left(self, x):
        v = 0
        res = 0
        for i in reversed(range(self.max_log)):
            if (x >> i) & 1:
                if self.nodes[2 * v + 1] == 0:
                    return res + self.size[v]
                res += self.size[self.nodes[2 * v]]
                v = self.nodes[2 * v + 1]
            else:
                if self.nodes[2 * v] == 0:
                    return res
                v = self.nodes[2 * v]
        return res

    def bisect_right(self, x):
        return self.bisect_left(x + 1)

    # 小さいほうからk番目の値を取得
    def get_kth(self, k):
        v = 0
        if self.size[v] <= k:
            return -1
        res = 0
        for i in reversed(range(self.max_log)):
            if self.nodes[2 * v] == 0:
                v = self.nodes[2 * v + 1]
                res |= 1 << i
                continue
            if self.nodes[2 * v + 1] == 0:
                v = self.nodes[2 * v]
                continue
            if self.size[self.nodes[2 * v]] <= k:
                k -= self.size[self.nodes[2 * v]]
                v = self.nodes[2 * v + 1]
                res |= 1 << i
            else:
                v = self.nodes[2 * v]
        return res
