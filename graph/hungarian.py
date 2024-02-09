def hungarian(A: list[list[int]]) -> tuple[int, list[int]]:
    inf = float("inf")
    n = len(A)
    row = [-1] * n
    col = [-1] * n
    pi = [0] * n
    residual = lambda i, j: A[i][j] - pi[j]
    transferrable = 0
    for j in range(n):
        i = 0
        for k in range(1, n):
            if A[i][j] > A[k][j]:
                i = k
        pi[j] = A[i][j]
        if row[i] == -1:
            row[i] = j
            col[j] = i
            transferrable |= 1 << i
        else:
            transferrable &= ~(1 << i)

    for i, c in enumerate(row):
        if (transferrable >> i) & 1 == 0:
            continue
        j = -1
        for k in range(n):
            if k != c and (j == -1 or residual(i, j) > residual(i, k)):
                j = k
        pi[c] -= residual(i, j)

    for _ in range(2):
        for i in range(n):
            if row[i] != -1:
                continue
            u1 = residual(i, 0)
            u2 = inf
            c1 = 0
            for j in range(n):
                u = residual(i, j)
                if u < u1 or (u == u1 and col[c1] != -1):
                    u2 = u1
                    u1 = u
                    c1 = j
                elif u < u2:
                    u2 = u
            if u1 < u2:
                pi[c1] -= u2 - u1
            if col[c1] != -1:
                row[col[c1]] = col[c1] = -1
            row[i] = c1
            col[c1] = i

    cols = [i for i in range(n)]
    for i in range(n):
        if row[i] != -1:
            continue
        dist = [residual(i, j) for j in range(n)]
        pred = [i] * n

        def f():
            scanned = labeled = last = 0
            while True:
                if scanned == labeled:
                    last = scanned
                    mn = dist[cols[scanned]]
                    for j in range(scanned, n):
                        c = cols[j]
                        if dist[c] <= mn:
                            if dist[c] < mn:
                                mn = dist[c]
                                labeled = scanned
                            cols[j], cols[labeled] = cols[labeled], cols[j]
                            labeled += 1
                    for j in range(scanned, labeled):
                        if col[cols[j]] == -1:
                            return cols[j], last
                c1 = cols[scanned]
                scanned += 1
                r1 = col[c1]
                for j in range(labeled, n):
                    c2 = cols[j]
                    ln = residual(r1, c2) - residual(r1, c1)
                    if dist[c2] > dist[c1] + ln:
                        dist[c2] = dist[c1] + ln
                        pred[c2] = r1
                        if ln == 0:
                            if col[c2] == -1:
                                return c2, last
                            cols[j], cols[labeled] = cols[labeled], cols[j]
                            labeled += 1

        c0, last = f()
        for j, c in enumerate(cols):
            if j == last:
                break
            pi[c] += dist[c] - dist[c0]

        t = c0
        while t != -1:
            j = t
            r = pred[j]
            col[j] = r
            row[r], t = t, row[r]

    tot = sum(A[i][row[i]] for i in range(n))

    return tot, row
