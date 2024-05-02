from heapq import heapify, heappush, heappop


class Node:
    def __init__(self, val: int):
        self.val = val
        self.lt = None
        self.rt = None


class HuTucker:
    inf = float("inf")

    @staticmethod
    def meld(a: Node | None, b: Node | None) -> Node | None:
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            a, b = b, a
        a.rt = HuTucker.meld(a.rt, b)
        a.lt, a.rt = a.rt, a.lt
        return a

    @staticmethod
    def top(a: Node) -> int:
        return a.val

    @staticmethod
    def pop(a: Node) -> Node:
        return HuTucker.meld(a.lt, a.rt)

    @staticmethod
    def push(a: Node, x: int) -> Node:
        b = Node(x)
        return HuTucker.meld(a, b)

    @staticmethod
    def solve(w: list[int]) -> int:
        inf = HuTucker.inf
        meld, top, pop, push = HuTucker.meld, HuTucker.top, HuTucker.pop, HuTucker.push
        n = len(w)
        lt = [0] * n
        rt = [0] * n
        cost = [0] * (n - 1)
        heap = [None for _ in range(n - 1)]
        pq = []
        for i in range(n - 1):
            lt[i] = i - 1
            rt[i] = i + 1
            cost[i] = w[i] + w[i + 1]
            pq.append(cost[i] * n + i)
        heapify(pq)
        res = 0
        for _ in range(n - 1):
            while True:
                p = heappop(pq)
                c, i = divmod(p, n)
                if cost[i] == c and rt[i] >= 0:
                    break
            ml = mr = False
            if heap[i] is not None and w[i] + heap[i].val == c:
                heap[i] = pop(heap[i])
                ml = True
            elif w[i] + w[rt[i]] == c:
                ml = mr = True
            else:
                t = top(heap[i])
                heap[i] = pop(heap[i])
                if heap[i] is not None and top(heap[i]) + t == c:
                    heap[i] = pop(heap[i])
                else:
                    mr = True
            res += c
            heap[i] = push(heap[i], c)
            if ml:
                w[i] = inf
            if mr:
                w[rt[i]] = inf
            if ml and i > 0:
                j = lt[i]
                heap[j] = meld(heap[i], heap[j])
                rt[j] = rt[i]
                rt[i] = -1
                lt[rt[j]] = j
                i = j
            if mr and rt[i] + 1 < n:
                j = rt[i]
                heap[i] = meld(heap[i], heap[j])
                rt[i] = rt[j]
                rt[j] = -1
                lt[rt[i]] = i
            cost[i] = w[i] + w[rt[i]]
            if heap[i] is not None:
                t = top(heap[i])
                heap[i] = pop(heap[i])
                cost[i] = min(cost[i], w[i] + t, w[rt[i]] + t)
                if heap[i] is not None:
                    cost[i] = min(cost[i], top(heap[i]) + t)
                heap[i] = push(heap[i], t)
            heappush(pq, cost[i] * n + i)
        return res
