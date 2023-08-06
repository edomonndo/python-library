# verification-helper: PROBLEM https://judge.yosupo.jp/problem/associative_array

import sys

input = sys.stdin.readline

Q = int(input())
dic = dict()
for _ in range(Q):
    # インプットを整数に変換するとTLEになる.strのままの方が速い.
    query = input().split()
    if query[0] == "0":
        k, v = query[1], query[2]
        dic[k] = v
    elif query[0] == "1":
        k = query[1]
        if k in dic:
            print(dic[k])
        else:
            print("0")
