from typing import Union, TypeVar

T = TypeVar("T")

from geometory.basic.point import Point


def convex_hull(
    ps_: list[Union[Point, tuple[T, T]]], multi: bool = False
) -> list[Point]:
    ps = [Point(x, y) for x, y in sorted(ps_)]
    if not ps:
        return []

    if not multi:
        tmp = [ps[0]]
        for p in ps[1:]:
            if p != tmp[-1]:
                tmp.append(p)
        ps = tmp

    n = len(ps)
    if n <= 2:
        return ps

    def cross3(a: Point, b: Point, c: Point) -> int:
        ax, ay = a
        bx, by = b
        cx, cy = c
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)

    res = []
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
