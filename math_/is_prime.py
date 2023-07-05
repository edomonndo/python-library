from typing import List


def miller_rabin(n: int) -> bool:
    """Miller-Rabin: ≒ O(1)"""
    assert n <= 1 << 64
    if n == 2:
        return True
    if n < 2 or (n & 1) == 0:
        return False
    n1 = n - 1
    d, s = n1, 0
    while (d & 1) == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        t = pow(a, d, n)
        if t == 1 or t == n1:
            continue
        for _ in range(s):
            t = pow(t, 2, n)
            if t == n1:
                break
        else:
            return False
    return True


def eratosthenes(N: int) -> List[bool]:
    # テーブル
    isprime = [True] * (N + 1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N + 1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime
