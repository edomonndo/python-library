from collections import deque


def topological_sort(N, G, deg):
    """トポロジカルソート

    有向グラフの順序を守るようにソートする
    閉路があるか判定も出来る
    計算量: O(E+V)

    Args:
        G (list): edge[i] = [a, b,...] iからa,b,...に辺が伸びている
        deg (list): deg[i] = iの入力辺の本数

    Returns:
        list or -1:閉路が存在しないとき
                      ソート済みのリスト
                   閉路が存在する時
                      -1
    """
    cands = [v for v in range(N) if deg[v] == 0]
    ans = []
    que = deque(cands)
    while que:
        v = que.popleft()
        if v in cands:
            ans.append(v)
        for u in G[v]:
            deg[u] -= 1
            if deg[u] == 0:
                que.append(u)
                ans.append(u)
    if len(ans) == N:
        return ans
    return -1
