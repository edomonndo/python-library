from typing import List, Tuple


def sortPointsByArgument(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    def msort(arr):
        if not arr:
            return
        n = len(arr)
        a = [arr, arr[:]]
        # 非再帰DFS
        stack = [(0, n, 1, 0)]  # 区間[l,r),DFSのフラグf,対象のリスト
        while stack:
            l, r, f, g = stack.pop()
            m = (l + r) // 2
            if f:
                stack.append((l, r, 0, g))
                if m - l > 1:
                    stack.append((l, m, 1, g ^ 1))
                if r - m > 1:
                    stack.append((m, r, 1, g ^ 1))
            else:
                i, j, p, q = l, m, m - 1, r - 1
                a1 = a[g]
                a2 = a[g ^ 1]
                for k in range((r - l) // 2):
                    x, y = a2[i]
                    s, t = a2[j]
                    if s * y - t * x > 0:
                        a1[l + k] = a2[j]
                        j += 1
                    else:
                        a1[l + k] = a2[i]
                        i += 1
                    x, y = a2[p]
                    s, t = a2[q]
                    if s * y - t * x > 0:
                        a1[r - 1 - k] = a2[p]
                        p -= 1
                    else:
                        a1[r - 1 - k] = a2[q]
                        q -= 1
                if (r - l) & 1:
                    a1[m] = a2[i] if i == p else a2[j]

    # ziは第i象限（ただしz5は原点）
    z1, z2, z3, z4, z5 = [], [], [], [], []
    for x, y in points:
        if x == y == 0:
            z5.append((x, y))
        elif y >= 0:
            if x >= 0:
                z1.append((x, y))
            else:
                z2.append((x, y))
        else:
            if x < 0:
                z3.append((x, y))
            else:
                z4.append((x, y))

    msort(z1)
    msort(z2)
    msort(z3)
    msort(z4)

    return z3 + z4 + z5 + z1 + z2
