# Dummy class for defaultdict


class defaultdict(dict):
    def __init__(self, func):
        self.func = func

    def __getitem__(self, item):
        if item not in self:
            self[item] = self.func()
        return super().__getitem__(item)
