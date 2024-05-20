---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unit_test/typical_problems_of_sum.test.py
    title: test/unit_test/typical_problems_of_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def solve1(A):\n    n = len(A)\n    Sn = sum(A)\n    res = Si = 0\n    for\
    \ i in range(n - 1):\n        Si += A[i]\n        res += A[i] * (Sn - Si)\n  \
    \  return res\n\n\ndef solve2(A):\n    n = len(A)\n    res = 0\n    for i, a in\
    \ enumerate(sorted(A), 1):\n        res += a * (n - i)\n    return res\n\n\ndef\
    \ solve3(A):\n    n = len(A)\n    Sn1 = Tn1 = 0\n    for i in range(n - 1):\n\
    \        Sn1 += A[i]\n        Tn1 += A[i] * Sn1\n    Sn = Sn1 + A[n - 1]\n   \
    \ Si = Ti = 0\n    res = 0\n    for i in range(n - 2):\n        Si += A[i]\n \
    \       Ti += A[i] * Si\n        res += A[i] * (Sn * (Sn1 - Si) - (Tn1 - Ti))\n\
    \    return res\n\n\ndef solve4(A):\n    n = len(A)\n    res = 0\n    for i, a\
    \ in enumerate(sorted(A), 1):\n        res += a * (n - i) * (n - 1 - i) // 2\n\
    \    return res\n\n\ndef solve5(A):\n    n = len(A)\n    cnt = [0] * 31\n    for\
    \ a in A:\n        for k in range(31):\n            if a >> k & 1:\n         \
    \       cnt[k] += 1\n    res = 0\n    for i, a in enumerate(A, 1):\n        for\
    \ k in range(31):\n            if a >> k & 1:\n                cnt[k] -= 1\n \
    \               res += (n - i - cnt[k]) * (1 << k)\n            else:\n      \
    \          res += cnt[k] * (1 << k)\n    return res\n\n\ndef solve6(A):\n    n\
    \ = len(A)\n    Sn = sum(A)\n    Tn = sum(a**2 for a in A)\n    res = 0\n    Si\
    \ = Ti = 0\n    for i, a in enumerate(A, 1):\n        Si += a\n        Ti += a**2\n\
    \        res += a * a * (n - i) - 2 * a * (Sn - Si) + Tn - Ti\n    return res\n\
    \n\ndef solve7(A):\n    n = len(A)\n    Sn = sum(A)\n    res = n * Sn\n    Si\
    \ = 0\n    for i, a in enumerate(sorted(A), 1):\n        Si += a\n        res\
    \ -= Si + a * (n - i)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/typical_problems_of_sum.py
  requiredBy: []
  timestamp: '2024-04-25 15:41:40+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unit_test/typical_problems_of_sum.test.py
documentation_of: math_/typical_problems_of_sum.py
layout: document
title: "\u5178\u578B\u554F\u984C\uFF08\u8DB3\u3057\u4E0A\u3052\uFF09"
---

制約:$\quad 1 \le N \le 2 \times 10^5, \quad 1 \le A_i \le 10^9$

$S_i := \displaystyle\sum^{i}_{j=1} A_jとする.$


## 1. ２項の積

$$
\begin{align}
\displaystyle\sum^{N-1}_{i=1} \sum^{N}_{j=i+1} A_i A_j &= \displaystyle\sum^{N-1}_{i=1} A_i (S_N - S_i)
\end{align}
$$


## 2. ２項の最小値

$A_i < A_j (i<j)$にソートし,昇順に寄与度を考える.

$$
\begin{align}
\displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} \min (A_i, A_j) &= \displaystyle\sum^{N-1}_{i=1} A_i ({N-i}) \\
&= \displaystyle\sum^{N}_{i=1} A_i ({N-i})
\end{align}
$$

## 3. ３項の積

$$
\begin{align}
\displaystyle \sum^{N-2}_{i=1} \sum^{N-1}_{j=i+1} \sum^{N}_{k=j+1} A_i A_j A_k &= \displaystyle\sum^{N-2}_{i=1}\sum^{N-1}_{j=i+1} A_iA_j(S_N-S_j) \\
&= \displaystyle\sum^{N-2}_{i=1} A_i \space ({S_N} \sum^{N-1}_{j=i+1} A_j - \sum^{N-1}_{j=i+1} A_j S_j) \\
&= \displaystyle\sum^{N-2}_{i=1} A_i \space (S_N (S_{N-1} - S_i)  - \sum^{N-1}_{j=i+1} A_j S_j)\\
&ここで, \displaystyle {T_i} := \sum^{i}_{j=1} A_j{S_j} とすると, \\
&= \displaystyle\sum^{N-2}_{i=1} A_i \space (S_N (S_{N-1} - S_i)  - (T_{N-1} - T_i))\\
\end{align}
$$

## 4. ３項の最小値

$A_i < A_j < A_k \quad (i<j<k)$にソートし、昇順に寄与度を考える.

$$
\begin{align}
\displaystyle \sum^{N-2}_{i=1} \sum^{N-1}_{j=i+1} \sum^{N}_{k=j+1} \min (A_i, A_j, A_k) &= \displaystyle\sum^{N}_{i=1} A_i \frac{(N-i)(N-1-i)}{2}
\end{align}
$$

## 5. 2項の排他的論理和

$A_{i,k}をA_iのkビット目とする.$

$A_{1,k},A_{2,k},...,A_{i,k}のうち, cnt0_{i,k}, cnt1_{i,k}をそれぞれ0と1の数とする.$

$$
\begin{align}
\displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} A_i \oplus A_j &= \displaystyle\sum^{N-1}_{i=1} (A_i \oplus A_{i+1}) + (A_i \oplus A_{i+2}) + ... + (A_i \oplus A_N) \\
&= \displaystyle\sum^{N-1}_{i=1}\sum^{}_{k=1}
\begin{cases}
2^{k-1} (cnt1_{N,k} - cnt1_{i,k}) &\quad A_{i,k} = 0 \\
2^{k-1} (cnt0_{N,k} - cnt0_{i,k}) &\quad A_{i,k} = 1 
\end{cases}
\end{align}
$$


## 6. 2項の差の二乗

$$
\begin{align}
\displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} (A_i - A_j)^2 &= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} A_i^2 - 2A_iA_j + A_j^2 \\
&= \displaystyle\sum^{N-1}_{i=1} A_i^2(N-i) -  2A_i(S_N - S_i) + (\sum^{N}_{j=1} A_j^2 - \sum^{i}_{j=1} A_j^2) \\
&ここで, \displaystyle T_i = \sum^{i}_{j=1} A_j^2とすると, \\
&= \displaystyle\sum^{N-1}_{i=1} A_i^2 \times (N-i) -  2A_i (S_N-S_i) + T_N - T_i \\
\end{align}
$$


## 7. 2項の差の絶対値

数列を並べ替えても答えは変わらないため、昇順にソートして考える.

$$
\begin{align}
\displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} \lvert A_i - A_j \rvert &= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} A_j - A_i \\
&= \displaystyle\sum^{N-1}_{i=1} S_n - S_i - A_i(N-i)  \\
&= \displaystyle\sum^{N}_{i=1} S_n - S_i - A_i(N-i)  \\
&= \displaystyle NS_N - \sum^{N}_{i=1} S_i + A_i (N-i)  \\
\end{align}
$$


## 8. 下限付きの２項の差

$$
\begin{align}
\displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} \max (A_j - A_i, 0)
&= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} \max (A_j,A_i) - A_i \\
&= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} \max (A_j,A_i) - \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} A_i \\
&= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} \max (A_i,A_j) - \displaystyle\sum^{N-1}_{i=1} A_i(N-i)
\end{align}
$$

なお,第1項は[2項の最小値](#2-２項の最小値)で求められる.


## 空でないAの部分列の和の総和

各項の寄与度を考えると,各項は$2^n-1$回足される.

$$
\begin{align}
(2^N-1) \displaystyle \sum^{N}_{i=1} A_i
\end{align}
$$

## 空でないAの連続部分列の和の総和

各項の寄与度を考えると，$i$番目の項は以下の数だけ足される．

$$
\begin{align}
\displaystyle \sum^{N}_{i=1} \begin{cases}
n + 2(i-1) &\quad i \le n/2 \\
2(n - i) &\quad i \gt n/2 
\end{cases}
\end{align}
$$

## 空でないAの部分列の積の総和$

TBD
