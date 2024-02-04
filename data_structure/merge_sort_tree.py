from bisect import bisect_right, bisect_left
class MergeSortTree:
    def __init__(self, V):
        n = len(V)
        d = [None]*n*2
        cum = [None]*n*2
        for i,a in enumerate(V):
            d[n+i] = [a]
            cum[n+i] = [0,a]
        for i in reversed(range(1,n)):
            d[i] = d[i*2] + d[i*2+1]
            d[i].sort()
            cum[i]=[0]
            for a in d[i]:
              cum[i].append(cum[i][-1]+a)
        self.n = n
        self.d = d
        self.cum = cum

    def sum_le(self, l, r, x):
        assert 0 <= l and l <= r and r <= self.n
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                i = bisect_right(self.d[l],x)
                res += self.cum[l][i]
                l += 1
            if r & 1:
                r -= 1
                i = bisect_right(self.d[r],x)
                res += self.cum[r][i]
            l >>= 1
            r >>= 1
        return res
    
    def sum_lt(self, l, r, x):
        assert 0 <= l and l <= r and r <= self.n
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                i = bisect_left(self.d[l],x)
                res += self.cum[l][i]
                l += 1
            if r & 1:
                r -= 1
                i = bisect_left(self.d[r],x)
                res += self.cum[r][i]
            l >>= 1
            r >>= 1
        return res