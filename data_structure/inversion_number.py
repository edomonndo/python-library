def inversion(A):
    def _add(i, x, bit):
        while i <= n:
            bit[i] += x
            i += i & -i

    def _sum(i, bit):
        total = 0
        while i > 0:
            total += bit[i]
            i -= i & -i
        return total

    n = len(A)
    bit = [0] * (n + 1)
    A = list(map({e: i for i, e in enumerate(sorted(set(A)), 1)}.__getitem__, A))

    ans = 0
    for i, a in enumerate(A):
        ans += i - _sum(a, bit)
        _add(a, 1, bit)
    return ans
