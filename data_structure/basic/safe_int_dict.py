class SafeIntDict(dict):
    def __init__(self):
        self.b = 5463325252
        super().__init__()

    def __getitem__(self, key):
        return super().__getitem__(key ^ self.b)

    def __setitem__(self, key, value):
        super().__setitem__(key ^ self.b, value)

    def __delitem__(self, key):
        return super().__delitem__(key ^ self.b)

    def get(self, key, default=None):
        return super().get(key ^ self.b, default)

    def pop(self, key, default=None):
        return super().pop(key ^ self.b, default)

    def __contains__(self, key):
        return super().__contains__(key ^ self.b)

    def __repr__(self):
        return str({k ^ self.b: v for k, v in super().items()})

    def __str__(self):
        return str({k ^ self.b: v for k, v in super().items()})
