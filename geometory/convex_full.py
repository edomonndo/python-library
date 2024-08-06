from geometory.basic.point import Point


def convex_hull(ps: list[Point]) -> list[Point]:

    ps = list(set(ps))
    if len(ps) <= 2:
        return ps

    ps.sort()
    res = []

    def cross3(a: Point, b: Point, c: Point) -> int:
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

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
    return res
