def convex_hull(xy: list[tuple[int, int]]):
    bs = 31
    msk = (1 << bs) - 1
    offset = 1_000_000_000

    ps = list(set(x + offset << bs | y + offset for x, y in xy))
    if len(ps) <= 2:
        return [((p >> bs) - offset, (p & msk) - offset) for p in ps]

    ps.sort()
    res = []

    def cross3(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
        ax, ay = a >> bs, a & msk
        bx, by = b >> bs, b & msk
        cx, cy = c >> bs, c & msk
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

    for p in ps:
        while len(res) > 1 and cross3(res[-1], res[-2], p) >= 0:
            res.pop()
        res.append(p)

    sz = len(res)
    for p in ps[::-1][1:]:
        while len(res) > sz and cross3(res[-1], res[-2], p) >= 0:
            res.pop()
        res.append(p)
    res.pop()
    return [((p >> bs) - offset, (p & msk) - offset) for p in res]
