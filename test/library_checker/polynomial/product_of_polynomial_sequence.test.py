# verification-helper: PROBLEM https://judge.yosupo.jp/problem/product_of_polynomial_sequence

from convolution.formal_power_series import multiply

from collections import deque

n = int(input())
if n == 0:
    print(1)
    exit()
deq = deque()
for _ in range(n):
    _, *a = map(int, input().split())
    deq.append(a)
while len(deq) >= 2:
    deq.append(multiply(deq.popleft(), deq.popleft()))
print(*deq.pop())
