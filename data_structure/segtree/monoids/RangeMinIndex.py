inf = float("inf")


class S:
    def __init__(self, value=inf, index=0):
        self.value = value
        self.index = index

    def __lt__(self, other: "S") -> bool:
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False
        else:
            return self.index < other.index


def op(l: S, r: S) -> S:
    if l < r:
        return l
    return r
