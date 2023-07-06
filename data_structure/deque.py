class Deque:
    def __init__(self, src_arr=None, max_size=300000):
        if src_arr is None:
            src_arr = []
        self.N = max(max_size, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)
        # customize
        self.sum = sum(src_arr)

    def __index(self, i):
        l = len(self)
        if not -l <= i < l:
            raise IndexError("index out of range: " + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N

    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail + 1 : self.tail + 1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex

    def is_full(self):
        return len(self) >= self.N - 1

    def is_empty(self):
        return len(self) == 0

    def append(self, x):
        if self.is_full():
            self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N
        # customize
        self.sum += x

    def appendleft(self, x):
        if self.is_full():
            self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N
        # customize
        self.sum += x

    def pop(self):
        if self.is_empty():
            raise IndexError("pop() when buffer is empty")
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        # customize
        self.sum -= ret
        return ret

    def popleft(self):
        if self.is_empty():
            raise IndexError("popleft() when buffer is empty")
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        # customize
        self.sum -= ret
        return ret

    def __len__(self):
        return (self.tail - self.head) % self.N

    def __getitem__(self, key):
        return self.buf[self.__index(key)]

    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value

    def __str__(self):
        return "Deque({0})".format(str(list(self)))
