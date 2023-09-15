from collections import deque


class ConvexHullTrick:
    def __init__(self):
        self.deq = deque()

    def _check(self, line1, line2, line3):
        return (line2[0] - line1[0]) * (line3[1] - line2[1]) >= (
            line2[1] - line1[1]
        ) * (line3[0] - line2[0])

    def _f(self, line_idx, x):
        a, b = self.deq[line_idx]
        return a * x + b

    def add_line(self, a, b):
        line = (a, b)
        while len(self.deq) >= 2 and self._check(self.deq[-2], self.deq[-1], line):
            self.deq.pop()
        self.deq.append(line)

    def query(self, x):
        while len(self.deq) >= 2 and self._f(0, x) >= self._f(1, x):
            self.deq.popleft()
        return self._f(0, x)
