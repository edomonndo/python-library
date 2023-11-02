class RadixHeap:
    def __init__(self, n: int, min_key: int = 0, max_key: int = 1 << 32):
        width = max_key - min_key
        assert width > 0
        self.data = [[] for _ in range(width.bit_length() + 1)]
        self.last = 0
        self.size = 0
        self.used = [0] * n

    def push(self, x: int, key: int) -> bool:
        if self.last <= x:
            self.size += 1
            self.data[(x ^ self.last).bit_length()].append((x, key))
            return True
        return False

    def pop(self) -> tuple[int, int]:
        if self.size <= 0:
            raise IndexError
        for i, d in enumerate(self.data):
            if d:
                break
        if i == 0:
            new_last, new_key = self.data[i].pop()
            self.used[new_key] = 1
            self.size -= 1
        else:
            new_last, new_key = min(d)
            self.used[new_key] = 1
            for x, key in d:
                if self.used[key]:
                    self.size -= 1
                    continue
                self.data[(x ^ new_last).bit_length()].append((x, key))
            self.last = new_last
            self.data[i] = []
        return new_last, new_key

    def __len__(self):
        return self.size
