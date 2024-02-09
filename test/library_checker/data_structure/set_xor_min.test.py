# verification-helper: PROBLEM https://judge.yosupo.jp/problem/set_xor_min

from data_structure.binary_trie import BinaryTrie

q = int(input())
bt = BinaryTrie()
for _ in range(q):
    t, x = map(int, input().split())
    if t == 0:
        bt.add(x)
    elif t == 1:
        bt.remove(x)
    else:
        print(bt.xor_min(x) ^ x)
