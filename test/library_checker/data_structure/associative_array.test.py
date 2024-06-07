# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array

from data_structure.basic.safe_int_dict import SafeIntDict

q = int(input())
dic = SafeIntDict()
for _ in range(q):
    # インプットを整数に変換するとTLEになる.strのままの方が速い.
    t, *qu = map(int, input().split())
    if t == 0:
        k, v = qu
        dic[k] = v
    else:
        k = qu[0]
        if k in dic:
            print(dic[k])
        else:
            print("0")
