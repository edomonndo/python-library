def nth_palindrome(n: int) -> str:
    """1-indexでn番目に小さい回文数"""
    assert n > 0
    if n == 1:
        return 0
    n -= 1
    sz, cnt = 1, 9
    while n > cnt:
        n -= cnt
        sz += 1
        cnt = 9 * (10 ** ((sz - 1) // 2))
    half = (sz + 1) // 2
    s = 10 ** (half - 1)
    num = s + (n - 1)
    res = str(num) + (str(num)[::-1] if sz & 1 == 0 else str(num)[-2::-1])
    return res


def count_palindrome(n: int, inf=10**20) -> int:
    """0以上n未満の整数における回文数の数"""

    def bin_seach(ok: int, ng: int, include_mid: bool):
        while abs(ok - ng) > 1:
            mid = (ok + ng) >> 1
            s = str(mid)
            t = "".join(reversed(s))
            if include_mid:
                tmp = int(s + t)
            else:
                tmp = int(s[:-1] + t)
            if tmp <= n:
                ok = mid
            else:
                ng = mid
        return ok

    res = bin_seach(0, inf, 0) + bin_seach(0, inf, 1)
    return res
