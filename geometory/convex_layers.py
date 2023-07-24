def convex_hull(xy, multi=False):
    xy.sort(key=lambda x: (x[1], x[0]))
    res = []

    def cross3(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    if multi:

        def f(a, b, c):
            return cross3(a, b, c) > 0

    else:

        def f(a, b, c):
            return cross3(a, b, c) >= 0

    for p in xy:
        while len(res) > 1 and f(res[-1], res[-2], p):
            res.pop()
        res.append(p)

    le = len(res)
    for p in xy[::-1][1:]:
        while len(res) > le and f(res[-1], res[-2], p):
            res.pop()
        res.append(p)
    res.pop()
    return res
