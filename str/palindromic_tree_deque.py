from data_structure.basic.deque import Deque


class DequePalindromicTree:
    class Node:
        def __init__(self, par: int, link: int, length: int, size: int):
            self.par = par
            self.link = link
            self.length = length
            self.cnt = 0
            self.link_cnt = 0
            self.to = [-1 for _ in range(size)]
            self.direct_link = [-1 for _ in range(size)]

    def __init__(self, S: str, base: str = "a", word_size: int = 26):
        self.n = 0
        self.offset = ord(base)
        self.word_size = word_size
        self.free = []
        self.nodes = []
        self.nodes.append(self._new_node(-1, -1, -1))  # ODD
        self.nodes.append(self._new_node(-1, 0, 0))  # EVEN
        inf = float("inf")
        self.nodes[0].cnt = self.nodes[1].cnt = inf
        mod = 4
        while mod < word_size:
            mod *= 2
        self.mod = mod
        self.msk = mod - 1
        self.dat = [None] * (mod * 3)  # (c, left_surface, right_surface)
        self.L = self.R = 0

    def _new_node(self, par: int, link: int, length: int, c: int) -> int:
        self.n += 1
        node = self.Node(par, link, length, self.word_size)
        if link != -1:
            self.nodes[link].link_cnt + 1
        p = 0
        if len(self.free) == 0:
            p = len(self.nodes)
            self.nodes.append(node)
        else:
            p = self.free.pop()
            self.nodes[p] = node
        if par != -1:
            self.nodes[par].to[c] = p
        return p

    def _remove_node(self, idx: int, c: int) -> None:
        self.n -= 1
        pidx = self.nodes[idx].par
        # assert self.nodes[pidx].to[c] == idx
        self.nodes[pidx].to[c] = -1
        k = self.nodes[idx].link
        self.nodes[k].link_cnt -= 1
        if self.nodes[k].link_cnt == 0:
            self.free.append(idx)
        return

    def _suffix_node(self):
        if self.L == self.R:
            return self.nodes[1]
        return self.dat[((self.R - 1) & self.msk) * 3 + 1]

    def _prefix_node(self):
        if self.L == self.R:
            return self.nodes[1]
        return self.dat[(self.L & self.msk) * 3 + 2]

    def append(self, c: str):
        # assert len(c) == 1
        c = ord(c) - self.offset
        # assert 0 <= c < self.word_size
        v = self._suffix_node()
        self.dat[(self.R & self.msk) * 3] = c

        def dfs(v: int) -> int:
            w = self.nodes[v].direct_link[c]
            if w != -1:
                return w
            p = self.nodes[v].link
            j = self.R - 1 - self.nodes[p].length
            if self.L <= j and j <= self.R and self.dat[(j & self.msk) * 3] == c:
                self.nodes[v].direct_link[c] = p
                return p
            w = dfs(p)
            self.nodes[v].direct_link[c] = w
            return w

        j = self.R - 1 - self.nodes[v].length
        if not (self.L <= j and j <= self.R and self.dat[(j & self.msk) * 3] == c):
            v = dfs(v)
        if self.nodes[v].to[c] != -1:
            v = self.nodes[v].to[c]
        else:
            link = self.nodes[1] if v == self.nodes[0] else self.nodes[dfs(v)].to[c]
            v = self._new_node(v, link, self.nodes[v].length + 2, c)


q = int(input())
PT = DequePalindromicTree("a", 26)
for _ in range(q):
    t, *qu = input().split()
    if t == "0":
        PT.appendleft(qu[0])
    elif t == "1":
        PT.append(qu[0])
    elif t == "2":
        PT.popleft()
    elif t == "3":
        PT.pop()
    print(
        PT.count_distinct_palindrome(),
        PT.max_prefix_palindrome(),
        PT.max_suffix_palindrome(),
    )
