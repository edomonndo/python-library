class LefitistHeap:
    def __init__(self, rank: int, key: int, value: int, left: int, right: int):
        self.rank = rank
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def insert(a: "LefitistHeap", key: int, value: int):
        if not a or key < a.key:
            return LefitistHeap(1, key, value, a, None)
        l, r = a.left, LefitistHeap.insert(a.right, key, value)
        if not l or r.rank > l.rank:
            l, r = r, l
        return LefitistHeap((r.rank if r else 0) + 1, a.key, a.value, l, r)

    def __lt__(self, _):
        return False
