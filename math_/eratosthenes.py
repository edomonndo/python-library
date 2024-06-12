def eratosthenes(N: int) -> list[bool]:
    isprime = [True] * (N + 1)

    isprime[0], isprime[1] = False, False

    for p in range(2, N + 1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return isprime
