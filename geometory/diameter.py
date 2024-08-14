from typing import Union, Optional, TypeVar

T = TypeVar("T")

from geometory.basic.point import Point
from geometory.convex_full import convex_hull


def diameter(
    ps: list[Union[Point, tuple[T, T]]]
) -> Optional[tuple[float, Point, Point]]:

    ch = convex_hull(ps)
    n = len(ch)
    if n == 0:
        return None
    if n == 1:
        return 0, ch[0], ch[0]
    if n == 2:
        return (ch[0] - ch[1]).abs(), ch[0], ch[1]

    u = v = 0
    up = vp = ch[0]
    for i in range(n):
        if ch[u] > ch[i]:
            u = i
            up = ch[i]
        if ch[v] < ch[i]:
            v = i
            vp = ch[i]

    dist2, su, sv = 0, u, v
    loop = False
    while u != su or v != sv or not loop:
        loop = True
        d2 = (ch[u] - ch[v]).norm()
        if dist2 < d2:
            dist2 = d2
            up, vp = ch[u], ch[v]
        a = ch[(u + 1) % n] - ch[u]
        b = ch[(v + 1) % n] - ch[v]
        if a.cross(b) < 0:
            u = (u + 1) % n
        else:
            v = (v + 1) % n
    return dist2**0.5, up, vp
