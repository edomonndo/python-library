def count_primes(n: int) -> int:
    """
    Count the number of primes no more than N.
    O(N**0.75 / logN)
    """
    if n < 2:
        return 0
    if n < 3:
        return 1
    if n < 5:
        return 2
    if n < 7:
        return 3
    if n < 11:
        return 4
    if n < 13:
        return 5
    if n < 17:
        return 6
    if n < 19:
        return 7
    if n < 23:
        return 8
    if n < 29:
        return 9

    v = int(n**0.5) - 1
    while True:
        if v * v > n:
            break
        v += 1

    smalls = [i + 1 >> 1 for i in range(v + 1)]
    s = v + 1 >> 1
    roughs = [i << 1 | 1 for i in range(s)]
    larges = [int(n / (i << 1 | 1) + 1) >> 1 for i in range(s)]
    skip = bytearray([0] * (v + 1))
    pc = 0
    for p in range(3, v + 1, 2):
        if skip[p]:
            continue
        q = p * p
        pc += 1
        if q * q > n:
            break
        skip[p] = 1
        for i in range(q, v + 1, p << 1):
            skip[i] = 1
        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]:
                continue
            d = i * p
            if d <= v:
                x = larges[smalls[d] - pc]
            else:
                x = smalls[int(n / d)]
            larges[ns] = larges[k] + pc - x
            roughs[ns] = i
            ns += 1
        s = ns
        i = v
        for j in range(int(v / p), p - 1, -1):
            c = smalls[j] - pc
            e = j * p
            while i >= e:
                smalls[i] -= c
                i -= 1
    ret = larges[0] + ((s + (pc - 1 << 1)) * (s - 1) >> 1) - sum(larges[1:s])

    for l in range(1, s):
        q = roughs[l]
        m = int(n / q)
        e = smalls[int(m / q)] - pc
        if e <= l:
            break
        t = 0
        for r in roughs[l + 1 : e + 1]:
            t += smalls[int(m / r)]
        ret += t - (e - l) * (pc + l - 1)
    return ret
