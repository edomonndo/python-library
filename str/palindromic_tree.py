class PalindromicTree:
    def __init__(self, S: str, base: str = "a", word_size: int = 26):
        offset = ord(base)
        S = [ord(s) - offset for s in S]
        self.n = n = len(S) + 2

        self._init_node(n, word_size)
        self._update_node(0, -1, -1, 0, -1)
        self._update_node(1, 0, 0, 0, 0)

        link, length, to = self.link, self.length, self.to

        self.path = path = []
        p = 0
        sz = 2
        for i, s in enumerate(S):
            path.append(p)
            while p:
                j = i - 1 - length[p]
                ok = j >= 0 and S[j] == s
                if ok:
                    break
                p = link[p]

            if to[p][s] != -1:
                p = to[p][s]
                continue

            l = i - 1 - length[p]
            r = i + 1
            to[p][s] = sz

            if p == 0:
                t = 1
            else:
                while True:
                    p = link[p]
                    j = i - 1 - length[p]
                    ok = j >= 0 and S[j] == s
                    if ok:
                        break
                t = to[p][s]
                assert t != -1
            self._update_node(sz, t, r - l, l, r)
            p = sz
            sz += 1
        path.append(p)
        self._shrink_node()
        return

    def _init_node(self, n: int, word_size: int):
        self.link = [None] * n
        self.length = [None] * n
        self.pos = [None] * n
        self.to = [[-1 for _ in range(word_size)] for _ in range(n)]

    def _update_node(self, idx: int, link: int, length: int, l: int, r: int) -> None:
        self.link[idx] = link
        self.length[idx] = length
        self.pos[idx] = (l, r)

    def _shrink_node(self) -> None:
        while self.link[-1] is None:
            # assert self.length[-1] is None
            # assert self.pos[-1] is None
            self.link.pop()
            self.length.pop()
            self.pos.pop()
            self.to.pop()
        self.n = len(self.link)
        return

    def count(self) -> list[int]:
        cnt = [0] * len(self.n)
        for p in self.path:
            cnt[p] += 1
        for i, x in enumerate(self.link[1:], 1):
            cnt[x] += cnt[i]
        return cnt[2:]

    def solve(self) -> tuple[list[int], list[int], list[int]]:
        par = [-1] * self.n
        for i, js in enumerate(self.to):
            for j in js:
                if j != -1:
                    par[j] = i - 1

        suffix_link = [0] * self.n
        for i, j in enumerate(self.link[2:]):
            if j is not None:
                suffix_link[i] = j - 1

        max_palindromic_suffix = [p - 1 for p in self.path[1:]]
        return par[2:], suffix_link[:-2], max_palindromic_suffix
