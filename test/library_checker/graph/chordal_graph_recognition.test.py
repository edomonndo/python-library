# verification-helper: PROBLEM https://judge.yosupo.jp/problem/chordal_graph_recognition

from graph.chordal_graph import ChordalGraph

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
CG = ChordalGraph(n, edges)
if CG.is_chordal_graph():
    print("YES")
    print(*CG.get_perfect_elimination_order())
else:
    print("NO")
    ans = CG.find_induced_cycle()
    print(len(ans))
    print(*ans)
