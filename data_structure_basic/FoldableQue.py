class FoldableQue:
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

    def fold(self):
        return self.op(self.topfold[-1], self.bottomfold[-1])

    def pop(self):
        if not self.top:
            while self.bottom:
                x = self._popbottom()
                self._pushtop(x)
        if not self.top:
            return self.e
        else:
            return self._poptop()

    def front(self):
        if not self.top:
            while self.bottom:
                x = self._popbottom()
                self._pushtop(x)
        return self.top[-1]
