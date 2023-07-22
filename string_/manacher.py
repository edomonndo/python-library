def manacher(s):
    """
    ある文字列Sが与えられているとする。
    Manacherでは,それぞれのiについて文字iを中心とする最長回文の半径を記録した配列を線形時間で構築する
    """
    if s == "":
        return (0, 1)
    n = len(s)
    t = "^#" + "#".join(s) + "#$"
    m = len(t)
    p = [0] * m
    c, d = 1, 1
    for i in range(2, m - 1):
        mirror = 2 * c - i
        p[i] = max(0, min(d - i, p[mirror]))
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > d:
            c = i
            d = i + p[i]
    # p[i]: ^#0#1#2...#n-1#$における位置iを中心とする最長回分の半径
    # p[2*(i+1)]//2: もとの文字列のiを中心とする最長回分の半径
    # p[2*(i+1)+1]//2: もとの文字列のi,i+1を中心とする最長回分の半径
    return [p[2 * (i + 1)] // 2 for i in range(n)], [
        p[2 * (i + 1) + 1] // 2 for i in range(n)
    ]
    # 最長回分の[s,t)が欲しい場合
    # k, i = max((p[i], i) for i in range(1, m - 1))
    # return (i - k) // 2, (i + k) // 2
