from collections import defaultdict
import heapq


class DeletableMaxHeapQ:
    def __init__(self, X):
        self.H = []
        self.HC = defaultdict(int)
        if X:
            self.H = X
            heapq.heapify(self.H)
            for x in X:
                self.HC[x] += 1

    def hpush(self, x):
        heapq.heappush(self.H, -x)
        self.HC[x] += 1

    def hpop(self):
        t = -heapq.heappop(self.H)
        while not self.HC[t]:
            t = -heapq.heappop(self.H)
        self.HC[t] -= 1
        return t

    def hmax(self):
        t = -self.H[0]
        while not self.HC[t]:
            heapq.heappop(self.H)
            t = -self.H[0]
        return t

    def hdel(self, x):
        assert self.HC[x] > 0
        self.HC[x] -= 1

    def __contains__(self, x):
        return 1 if x in self.HC and self.HC[x] else 0


class DeletableMinHeapQ:
    def __init__(self, X):
        self.H = []
        self.HC = defaultdict(int)
        if X:
            self.H = X
            heapq.heapify(self.H)
            for x in X:
                self.HC[x] += 1

    def hpush(self, x):
        heapq.heappush(self.H, x)
        self.HC[x] += 1

    def hpop(self):
        t = heapq.heappop(self.H)
        while not self.HC[t]:
            t = heapq.heappop(self.H)
        self.HC[t] -= 1
        return t

    def hmin(self):
        t = self.H[0]
        while not self.HC[t]:
            heapq.heappop(self.H)
            t = self.H[0]
        return t

    def hdel(self, x):
        assert self.HC[x] > 0
        self.HC[x] -= 1

    def __contains__(self, x):
        return 1 if x in self.HC and self.HC[x] else 0
