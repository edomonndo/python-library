from data_structure.basic.deque import Deque


class DequePalindromicTree:
    def __init__(self, n: int, base: str = "a", word_size: int = 26):
        n += 2
        self.n = n
        self.offset = ord(base)
        self.word_size = word_size
        self.to = [[0] * word_size for _ in range(n)]
        self.cnt = [0] * n
        self.size = [0] * n
        self.par = [0] * n
        self.link = [0] * n
        self.slink = [0] * n
        self.link[0] = self.slink[0] = 1
        self.size[1] = -1
        self.s = Deque(max_size=n)
        self.states = Deque([0])
        self.diffs = Deque()
        self.sz = 2
        self.active = 0

    def _get_link(self, v: int, c: int, back: bool = True) -> int:
        s, size, link, slink = self.s, self.size, self.link, self.slink
        while c != self._get(s, size[v] + 1, back):
            if c == self._get(s, size[link[v]] + 1, back):
                v = link[v]
            else:
                v = slink[v]
        return v

    def _make_to(self, last: int, c: int, back: bool = True) -> int:
        to, link, slink, par, size = self.to, self.link, self.slink, self.par, self.size
        last = self._get_link(last, c, back)
        if not to[last][c]:
            u = to[self._get_link(link[last], c, back)][c]
            sz = self.sz
            link[sz] = u
            par[sz] = last
            size[sz] = size[last] + 2
            if size[sz] - size[u] == size[u] - size[link[u]]:
                slink[sz] = slink[u]
            else:
                slink[sz] = u
            to[last][c] = sz
            self.sz += 1
        return to[last][c]

    def _get(self, d: Deque, idx: int, back: bool = True) -> int:
        if idx >= len(d):
            return -1
        if back:
            idx = ~idx
        return d[idx]

    def _push(self, d: Deque, c: int, back: bool = True):
        if back:
            d.append(c)
        else:
            d.appendleft(c)

    def _pop(self, d: Deque, back: bool = True):
        if back:
            d.pop()
        else:
            d.popleft()

    def _add_letter(self, c: str, back: bool = True):
        s, states, diffs, size = self.s, self.states, self.diffs, self.size
        c = ord(c) - self.offset
        self._push(s, c, back)
        pre = self._get(states, 0, back)
        last = self._make_to(pre, c, back)
        self.active += not (self.cnt[last])
        self.cnt[last] += 1
        D = 2 + size[pre] - size[last]
        while D + size[pre] <= size[last]:
            self._pop(states, back)
            if states:
                pre = self._get(states, 0, back)
                D += self._get(diffs, 0, back)
                self._pop(diffs, back)
            else:
                break
        if states:
            self._push(diffs, D, back)
        self._push(states, last, back)

    def _pop_letter(self, back: bool = True):
        cnt, link, size, par = self.cnt, self.link, self.size, self.par
        states, diffs = self.states, self.diffs
        last = self._get(states, 0, back)
        cnt[last] -= 1
        self.active -= not (cnt[last])
        self._pop(states, back)
        self._pop(self.s, back)
        cands = [(link[last], size[last] - size[link[last]]), (par[last], 0)]
        for state, diff in cands:
            if not states:
                states.append(state)
                diffs.append(diff)
            else:
                D = self._get(diffs, 0, back) - diff
                pre = self._get(states, 0, back)
                if D + size[state] > size[pre]:
                    self._push(states, state, back)
                    self._pop(diffs, back)
                    self._push(diffs, D, back)
                    self._push(diffs, diff, back)
        self._pop(diffs, back)

    def append(self, c: int):
        # assert 0 <= ord(c) - self.offset < self.word_size
        self._add_letter(c, True)

    def appendleft(self, c: int):
        # assert 0 <= ord(c) - self.offset < self.word_size
        self._add_letter(c, False)

    def pop(self):
        self._pop_letter(True)

    def popleft(self):
        self._pop_letter(False)

    def distinct(self):
        return self.active

    def max_prefix_size(self):
        return self.size[self._get(self.states, 0, False)]

    def max_suffix_size(self):
        return self.size[self._get(self.states, 0, True)]
