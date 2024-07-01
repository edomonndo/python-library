def overlap(S: str, T: str) -> int:
    """
    Get overlapped string length by O(min(|S|,|T|)), when 'S','T' -> 'ST'.
    Algorithm is based on z-algorithm.
    'snuke' + 'kensho' -> 2
    """
    sn, tn = len(S), len(T)
    if sn == 0 or tn == 0:
        return 0
    # S,Tは短い方の長さに合わせる. Sは末尾, Tは先頭を保持する.
    if sn > tn:
        sn = tn
        S = S[-tn:]
    elif sn < tn:
        tn = sn
        T = T[:sn]
    n = sn + tn
    s = [ord(c) for c in (T + S)]
    # z-algorithm
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n
    for i in range(sn, 0, -1):
        # Sの末尾i文字とTの先頭i文字が合致するか
        if i == z[-i]:
            return i
    return 0
