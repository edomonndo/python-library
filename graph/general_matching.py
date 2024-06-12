from collections import deque


class GeneralMatching:
    def __init__(self, n: int, edges: list[tuple[int, int]]):
        self.n = n
        self.adj = adj = [[] for _ in range(n + 1)]
        self.edges = []
        cnt = n + 1
        for i, (u, v) in enumerate(edges, n + 1):
            u += 1
            v += 1
            adj[u].append((v, i))
            adj[v].append((u, i))
            self.edges.append((u, v))
        self.mate = [0] * (n + 1)
        self.label = [-1] * (n + 1)
        self.first = [0] * (n + 1)

    def _eval_first(self, x: int) -> int:
        label, first, _eval_first = self.label, self.first, self._eval_first
        if label[first[x]] < 0:
            return first[x]
        first[x] = _eval_first(first[x])
        return first[x]

    def _rematch(self, u: int, v: int) -> None:
        mate, label = self.mate, self.label
        st = [(u, v)]
        while st:
            u, v = st.pop()
            t = mate[u]
            mate[u] = v
            if mate[t] != u:
                continue
            if label[u] <= self.n:
                mate[t] = label[u]
                st.append((label[u], t))
            else:
                x, y = self.edges[label[u] - self.n - 1]
                st += [(y, x), (x, y)]

    def _assign(self, x: int, y: int, num: int) -> None:
        mate, label, first = self.mate, self.label, self.first
        dq, _eval_first = self.dq, self._eval_first
        r = _eval_first(x)
        s = _eval_first(y)
        join = 0
        if r == s:
            return
        label[r] = -num
        label[s] = -num
        while True:
            if s != 0:
                r, s = s, r
            r = _eval_first(label[mate[r]])
            if label[r] == -num:
                join = r
                break
            label[r] = -num
        v = first[x]
        while v != join:
            dq.append(v)
            label[v] = num
            first[v] = join
            v = first[label[mate[v]]]
        v = first[y]
        while v != join:
            dq.append(v)
            label[v] = num
            first[v] = join
            v = first[label[mate[v]]]
        return

    def _check(self, v: int) -> bool:
        dq, first, label, mate = self.dq, self.first, self.label, self.mate
        adj, _rematch, _assign = self.adj, self._rematch, self._assign
        first[v] = 0
        label[v] = 0
        dq.append(v)
        while dq:
            x = dq.popleft()
            for y, lb in adj[x]:
                if mate[y] == 0 and y != v:
                    mate[y] = x
                    _rematch(x, y)
                    return True
                elif label[y] >= 0:
                    _assign(x, y, lb)
                elif label[mate[y]] < 0:
                    label[mate[y]] = x
                    first[mate[y]] = y
                    dq.append(mate[y])
        return False

    def solve(self) -> list[tuple[int, int]]:
        mate, _check = self.mate, self._check
        for i in range(1, self.n + 1):
            self.dq = deque()
            if mate[i] != 0:
                continue
            if _check(i):
                self.label = [-1] * (self.n + 1)
        res = []
        for i in range(1, self.n + 1):
            if i < mate[i]:
                res.append((i - 1, mate[i] - 1))
        return res
