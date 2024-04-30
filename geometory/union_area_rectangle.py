from atcoder.lazysegtree import LazySegTree

mask = (1 << 31) - 1


def op(x, y):
    x0, x1 = x >> 31, x & mask
    y0, y1 = y >> 31, y & mask
    if x0 < y0:
        return x
    elif x0 > y0:
        return y
    else:
        return (x0 << 31) + x1 + y1


def mapping(x, y):
    y0, y1 = y >> 31, y & mask
    return ((y0 + x) << 31) + y1


def composition(x, y):
    return x + y


def union_area(rectangles: list[tuple[int, int, int, int]]):
    """
    Rectangle := [x1, y1, x2, y2], where (x1,y1) is top-left, (x2,y2) is bottom-right of rectangle.
    O(nlogn)
    """
    A, X, Y = [], [], []
    for x1, y1, x2, y2 in rectangles:
        X += [x1, x2]
        Y += [y1, y2]
    X = list(set(X))
    X.sort()
    dX = {x: i for i, x in enumerate(X)}
    Y = list(set(Y))
    Y.sort()
    dY = {y: i for i, y in enumerate(Y)}
    L = [[] for _ in range(len(Y))]
    R = [[] for _ in range(len(Y))]
    for x1, y1, x2, y2 in rectangles:
        x1, y1, x2, y2 = dX[x1], dX[x2], dY[y1], dY[y2]
        L[y1].append((x1, x2))
        R[y2].append((x1, x2))

    v = [(X[i + 1] - X[i]) for i in range(len(X) - 1)]
    lst = LazySegTree(op, 1 << 61, mapping, composition, 0, v)
    s = X[-1] - X[0]
    res = 0
    for i in range(len(Y) - 1):
        for l, r in L[i]:
            lst.apply(l, r, 1)
        z = lst.all_prod()
        z0, z1 = z >> 31, z & mask
        z = s - z1 if z0 == 0 else s
        res += z * (Y[i + 1] - Y[i])
        for l, r in R[i + 1]:
            lst.apply(l, r, -1)
    return res
