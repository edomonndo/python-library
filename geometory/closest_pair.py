from typing import Union, TypeVar

T = TypeVar("T")


from geometory.basic.point import Point


def closest_pair(ps_: list[Union[Point, tuple[T, T]]]) -> tuple[float, Point, Point]:

    assert len(ps_) >= 2

    ps = sorted([Point(x, y) for x, y in ps_])
    if len(ps) == 2:
        return (ps[0] - ps[1]).abs(), ps[0], ps[1]

    n = len(ps)
    tmp = [None] * n
    min_dist2 = float("inf")
    up = vp = None
    ps_origin = ps[:]

    # 非再帰dfs
    st = [(0, n)]
    while st:
        l, r = st.pop()
        if l >= 0:
            m = (l + r) >> 1
            st.append((~l, r))
            if r - m > 1:
                st.append((m, r))
            if m - l > 1:
                st.append((l, m))
        else:
            l = ~l
            m = (l + r) >> 1
            mx = ps_origin[m].x
            i, j = l, m
            idx = 0
            while i < m and j < r:
                if Point.cmp(ps[i].y, ps[j].y, False) < 0:
                    tmp[idx] = ps[i]
                    i += 1
                else:
                    tmp[idx] = ps[j]
                    j += 1
                idx += 1
            for k in range(i, m):
                ps[l + idx + k - i] = ps[k]
            for k in range(l, l + idx):
                ps[k] = tmp[k - l]

            bs = []
            for cp in ps[l:r]:
                if Point.cmp((cp.x - mx) * (cp.x - mx), min_dist2, False) >= 0:
                    continue
                for bp in bs[::-1]:
                    dp = cp - bp
                    if Point.cmp(dp.y * dp.y, min_dist2, False) >= 0:
                        break
                    d = dp.norm()
                    if Point.cmp(d, min_dist2, False) < 0:
                        min_dist2, up, vp = d, cp, bp
                bs.append(cp)

    return min_dist2**0.5, up, vp
