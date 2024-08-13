from typing import Union, TypeVar

T = TypeVar("T")

from geometory.basic.point import Point


def arg_sort(ps: list[Union[Point, tuple[T, T]]]) -> list[Point]:
    def merge_sort(arr):
        if not arr:
            return
        n = len(arr)
        a = [arr, arr[:]]
        # 非再帰DFS
        st = [(0, n, 1, 0)]  # 区間[l,r),DFSのフラグf,対象のリスト
        while st:
            l, r, f, g = st.pop()
            m = (l + r) >> 1
            if f:
                st.append((l, r, 0, g))
                if m - l > 1:
                    st.append((l, m, 1, g ^ 1))
                if r - m > 1:
                    st.append((m, r, 1, g ^ 1))
            else:
                i, j, p, q = l, m, m - 1, r - 1
                a1 = a[g]
                a2 = a[g ^ 1]
                for k in range((r - l) >> 1):
                    xi, yi = a2[i]
                    xj, yj = a2[j]
                    if xj * yi - yj * xi > 0:
                        a1[l + k] = a2[j]
                        j += 1
                    else:
                        a1[l + k] = a2[i]
                        i += 1
                    xp, yp = a2[p]
                    xq, yq = a2[q]
                    if xq * yp - yq * xp > 0:
                        a1[r - 1 - k] = a2[p]
                        p -= 1
                    else:
                        a1[r - 1 - k] = a2[q]
                        q -= 1
                if (r - l) & 1:
                    a1[m] = a2[i] if i == p else a2[j]

    # ziは第i象限（ただしz5は原点）
    z1, z2, z3, z4, z5 = [], [], [], [], []
    for x, y in ps:
        if x == y == 0:
            z = z5
        elif y >= 0:
            z = z1 if x >= 0 else z2
        else:
            z = z3 if x < 0 else z4
        z.append(Point(x, y))

    for z in [z1, z2, z3, z4]:
        merge_sort(z)

    return z3 + z4 + z5 + z1 + z2
