import atexit
import os
import sys


class Fastio:
    def __init__(self):
        self.ibuf = bytes()
        self.obuf = []
        self.pil = 0
        self.pir = 0
        atexit.register(self.flush)
        sys.stdin, sys.stdout = None, None

    def load(self):
        self.ibuf = self.ibuf[self.pil :]
        self.ibuf += os.read(0, 131072)
        self.pil = 0
        self.pir = len(self.ibuf)

    def flush(self):
        os.write(1, "".join(self.obuf).encode())

    def read(self):
        if self.pir - self.pil < 64:
            self.load()
        minus = 0
        x = 0
        while self.ibuf[self.pil] < 45:
            self.pil += 1
        if self.ibuf[self.pil] == 45:
            minus = 1
            self.pil += 1
        while self.pil < len(self.ibuf) and self.ibuf[self.pil] >= 48:
            x = x * 10 + (self.ibuf[self.pil] & 15)
            self.pil += 1
        if minus:
            x = -x
        return x

    def write(self, x):
        self.obuf.append(str(x))

    def writeln(self, x):
        self.obuf.append(str(x) + "\n")
