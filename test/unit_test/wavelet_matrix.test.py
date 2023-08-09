# verification-helper: UNITTEST

if __name__ == "__main__":
    from pathlib import Path
    import sys

    sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
    from data_structure.wavelet_matrix import WaveletMatrix

    T = [5, 4, 5, 5, 2, 1, 5, 6, 1, 3, 5, 0]
    WM = WaveletMatrix(T)

    assert WM.n == len(T)
    assert WM.A == T

    # access
    for i, t in enumerate(T):
        assert t == WM.access(i), (t, WM.access(i))
        assert t == WM.accessFromB(i), (t, WM.accessFromB(i))

    # rank
    for l in range(len(T)):
        for r in range(l + 1, len(T)):
            for t in T:
                greedy_rank = T[l:r].count(t)
                assert greedy_rank == WM.rank(l, r, t), (
                    (l, r, t),
                    greedy_rank,
                    WM.rank(l, r, t),
                )

    # select
    def greedy_select(t, k):
        cnt = 0
        for i, a in enumerate(T):
            if a == t:
                if cnt == k:
                    return i
                cnt += 1
        return -1

    for t in set(T):
        for k in range(T.count(t)):
            assert greedy_select(t, k) == WM.select(t, k), (
                (t, k),
                greedy_select(t, k),
                WM.select(t, k),
            )

    # quantile
    def greedy_quantile(l, r, k):
        return sorted(T[l:r])[k]

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            for k in range(r - l):
                assert greedy_quantile(l, r, k) == WM.quantile(l, r, k), (
                    (l, r, k),
                    greedy_quantile(l, r, k),
                    WM.quantile(l, r, k),
                )

    # quantilerange
    def greedy_quantilerange(l, r, k):
        arr = sorted(T[l:r])
        val = arr[k]
        num = arr[: k + 1].count(val)
        cnt = 0
        for i, t in enumerate(T[l:r]):
            if t == val:
                cnt += 1
                if cnt == num:
                    idx = i
                    break
        return idx + l

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            for k in range(r - l):
                assert greedy_quantilerange(l, r, k) == WM.quantilerange(l, r, k), (
                    (l, r, k),
                    greedy_quantilerange(l, r, k),
                    WM.quantilerange(l, r, k),
                )

    # maxrange, minrange
    def greedy_maxrange(l, r):
        max_value = max(T[l:r])
        idx = -1
        for i, t in enumerate(T[l:r]):
            if t == max_value:
                idx = i
        return idx + l

    def greedy_minrange(l, r):
        min_value = min(T[l:r])
        idx = -1
        for i, t in enumerate(T[l:r]):
            if t == min_value:
                idx = i
                break
        return idx + l

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            assert greedy_maxrange(l, r) == WM.maxrange(l, r), (
                (l, r),
                greedy_maxrange(l, r),
                WM.maxrange(l, r),
            )
            assert greedy_minrange(l, r) == WM.minrange(l, r), (
                (l, r),
                greedy_minrange(l, r),
                WM.minrange(l, r),
            )

    # topk
    def greedy_topk(l, r, k):
        dic = dict()
        for t in T[l:r]:
            if t in dic:
                dic[t] += 1
            else:
                dic[t] = 1
        res = []
        for key, value in sorted(dic.items(), key=lambda x: (-x[1], x[0])):
            res.append((key, value))
        return res[:k]

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            for k in range(1, r - l + 1):
                assert greedy_topk(l, r, k) == WM.topk(l, r, k), (
                    (l, r, k),
                    greedy_topk(l, r, k),
                    WM.topk(l, r, k),
                )

    # rangesum
    def greedy_rangesum(l, r):
        return sum(T[l:r])

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            assert greedy_rangesum(l, r) == WM.rangesum(l, r)

    # intersect
    def greedy_intersect(l1, r1, l2, r2):
        S1 = set(T[l1:r1])
        S2 = set(T[l2:r2])
        S = S1 & S2
        res = []
        for s in S:
            t1 = T[l1:r1].count(s)
            t2 = T[l2:r2].count(s)
            res.append((s, t1, t2))
        return res

    for l1 in range(len(T)):
        for r1 in range(l + 1, len(T) + 1):
            for l2 in range(len(T)):
                for r2 in range(l + 1, len(T) + 1):
                    assert greedy_intersect(l1, r1, l2, r2) == WM.intersect(
                        l1, r1, l2, r2
                    ), (
                        (l1, r1, l2, r2),
                        greedy_intersect(l1, r1, l2, r2),
                        WM.intersect(l1, r1, l2, r2),
                    )

    # rangefreq_to, rangefreq
    def greedy_rangefreq_to(l, r, value):
        return len([t for t in T[l:r] if 0 <= t < value])

    def greedy_rangefreq(l, r, x, y):
        return len([t for t in T[l:r] if x <= t < y])

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            for y in range(max(T) + 2):
                assert greedy_rangefreq_to(l, r, y) == WM.rangefreq_to(l, r, y)
                for x in range(0, y):
                    assert greedy_rangefreq(l, r, x, y) == WM.rangefreq(l, r, x, y)

    # prevvalue, nextvalue (Not verified)
    def greedy_prevvalue(l, r, x, y):
        try:
            res = max(t for t in T[l:r] if x <= t < y)
        except ValueError:
            res = -1
        return res

    def greedy_nextvalue(l, r, x, y):
        try:
            res = min(t for t in T[l:r] if x <= t < y)
        except ValueError:
            res = -1
        return res

    for l in range(len(T)):
        for r in range(l + 1, len(T) + 1):
            for x in range(max(T)):
                for y in range(x + 1, max(T) + 2):
                    assert greedy_prevvalue(l, r, x, y) == WM.prevvalue(l, r, x, y), (
                        (l, r, x, y),
                        greedy_prevvalue(l, r, x, y),
                        WM.prevvalue(l, r, x, y),
                    )
                    assert greedy_nextvalue(l, r, x, y) == WM.nextvalue(l, r, x, y), (
                        (l, r, x, y),
                        greedy_nextvalue(l, r, x, y),
                        WM.nextvalue(l, r, x, y),
                    )
