class FoldableDeque:
    def __init__(self, op, e):
        self.op = op
        self.e = e
        self.top = []
        self.bottom = []
        self.topfold = [e]
        self.bottomfold = [e]

    def _pushbottom(self, x):
        self.bottom.append(x)
        self.bottomfold.append(self.op(self.bottomfold[-1], x))

    def _popbottom(self):
        self.bottomfold.pop()
        return self.bottom.pop()

    def _pushtop(self, x):
        self.top.append(x)
        self.topfold.append(self.op(x, self.topfold[-1]))

    def _poptop(self):
        self.topfold.pop()
        return self.top.pop()

    def push(self, x):
        self._pushbottom(x)

    def pushleft(self, x):
        self._pushtop(x)

    def fold(self):
        return self.op(self.topfold[-1], self.bottomfold[-1])

    def popleft(self):
        if not self.top:
            stack = []
            while self.bottom:
                x = self._popbottom()
                stack.append(x)
            n = len(stack)
            stack = stack[::-1]
            stack1 = stack[: (n + 1) // 2]
            stack2 = stack[(n + 1) // 2 :][::-1]
            for _ in range((n + 1) // 2):
                self._pushtop(stack1.pop())
            for _ in range(n // 2):
                self._pushbottom(stack2.pop())
        if not self.top:
            return self.e
        else:
            return self._poptop()

    def pop(self):
        if not self.bottom:
            stack = []
            while self.top:
                x = self._poptop()
                stack.append(x)
            n = len(stack)
            stack1 = stack[: n // 2]
            stack2 = stack[n // 2 :][::-1]
            for _ in range((n + 1) // 2):
                self._pushbottom(stack2.pop())
            for _ in range(n // 2):
                self._pushtop(stack1.pop())
        if not self.bottom:
            return self.e
        else:
            return self._popbottom()
