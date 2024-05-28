def StaticRangeInversionQuery(
    A: list[int], queries: list[tuple[int, int]]
) -> list[int]:
    n, q = len(A), len(queries)
    # 座圧
    dA = {a: i for i, a in enumerate(sorted(set(A)))}
    A = [dA[a] for a in A]

    L, R = [0] * q, [0] * q
    for i, (l, r) in enumerate(queries):
        L[i], R[i] = l, r
    d = int(n**0.5)
    order = sorted(
        range(q),
        key=lambda i: (
            (L[i] // d) << 20 | R[i] if (L[i] // d) & 1 else ((L[i] // d) << 20) - R[i]
        ),
    )

    bit = [0] * (n + 1)
    l = r = score = 0
    ans = [0] * q
    for i in order:
        # Add
        while L[i] < l:
            l -= 1
            idx = A[l] + 1
            while idx <= n:
                bit[idx] += 1
                idx += idx & -idx
            idx = A[l]
            while idx:
                score += bit[idx]
                idx -= idx & -idx
        while r < R[i]:
            score += r - l
            idx = A[r] + 1
            while idx:
                score -= bit[idx]
                idx -= idx & -idx
            idx = A[r] + 1
            while idx <= n:
                bit[idx] += 1
                idx += idx & -idx
            r += 1
        # Remove
        while L[i] > l:
            idx = A[l]
            while idx:
                score -= bit[idx]
                idx -= idx & -idx
            idx = A[l] + 1
            while idx <= n:
                bit[idx] -= 1
                idx += idx & -idx
            l += 1
        while r > R[i]:
            r -= 1
            idx = A[r] + 1
            while idx <= n:
                bit[idx] -= 1
                idx += idx & -idx
            score -= r - l
            idx = A[r] + 1
            while idx:
                score += bit[idx]
                idx -= idx & -idx
        ans[i] = score
    return ans
