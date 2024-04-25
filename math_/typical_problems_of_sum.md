---
title: 典型問題（足し上げ）
documentation_of: ./typical_problems_of_sum.py
---

制約: $1 \le N \le 2 \times 10^5, \quad 1 \le A_i \le 10^9$

$S_i := \displaystyle\sum^{i}_{j=1} A_jとする.$

[1] $`\quad \displaystyle\sum^{N-1}_{i=1} \sum^{N}_{j=i+1} A_i A_j `$

$$
\begin{align}
与式 &= \displaystyle\sum^{N-1}_{i=1} A_i (S_N - S_i)
\end{align}
$$

 [2] $`\quad \displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} \min (A_i, A_j)`$

$A_i < A_j (i<j)$にソートし,昇順に寄与度を考える.

$$
\begin{align}
与式 &= \displaystyle\sum^{N-1}_{i=1} A_i ({N-i})
= \displaystyle\sum^{N}_{i=1} A_i ({N-i})
\end{align}
$$

 [3] $`\quad \displaystyle \sum^{N-2}_{i=1} \sum^{N-1}_{j=i+1} \sum^{N}_{k=j+1} A_i A_j A_k`$

$$
\begin{align}
与式 &= \displaystyle\sum^{N-2}_{i=1}\sum^{N-1}_{j=i+1} A_iA_j(S_N-S_j) \\
&= \displaystyle\sum^{N-2}_{i=1} A_i \space ({S_N} \sum^{N-1}_{j=i+1} A_j - \sum^{N-1}_{j=i+1} A_j S_j) \\
&= \displaystyle\sum^{N-2}_{i=1} A_i \space (S_N (S_{N-1} - S_i)  - \sum^{N-1}_{j=i+1} A_j S_j)\\
&ここで, \displaystyle {T_i} := \sum^{i}_{j=1} A_j{S_j} とすると, \\
&= \displaystyle\sum^{N-2}_{i=1} A_i \space (S_N (S_{N-1} - S_i)  - (T_{N-1} - T_i))\\
\end{align}
$$

 [4] $`\quad \displaystyle \sum^{N-2}_{i=1} \sum^{N-1}_{j=i+1} \sum^{N}_{k=j+1} \min (A_i, A_j, A_k)`$

$A_i < A_j < A_k \quad (i<j<k)$にソートし、昇順に寄与度を考える.

$$
\begin{align}
与式 &= \displaystyle\sum^{N}_{i=1} A_i \frac{(N-i)(N-1-i)}{2}
\end{align}
$$

 [5] $`\quad \displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} A_i \oplus A_j`$

$A_{i,k}をA_iのkビット目とする.$
$A_{1,k},A_{2,k},...,A_{i,k}のうち, cnt0_{i,k}, cnt1_{i,k}をそれぞれ0と1の数とする.$

$$
\begin{align}
与式 &= \displaystyle\sum^{N-1}_{i=1} (A_i \oplus A_{i+1}) + (A_i \oplus A_{i+2}) + ... + (A_i \oplus A_N) \\
&= \displaystyle\sum^{N-1}_{i=1}\sum^{}_{k=1}
\begin{cases}
2^{k-1} (cnt1_{N,k} - cnt1_{i,k}) \quad A_{i,k} = 0 \\
2^{k-1} (cnt0_{N,k} - cnt0_{i,k}) \quad A_{i,k} = 1 
\end{cases}
\end{align}
$$



 [6] $`$\quad \displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} (A_i - A_j)^2`$


$$
\begin{align}
与式 &= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} A_i^2 - 2A_iA_j + A_j^2 \\
&= \displaystyle\sum^{N-1}_{i=1} A_i^2(N-i) -  2A_i(S_N - S_i) + (\sum^{N}_{j=1} A_j^2 - \sum^{i}_{j=1} A_j^2) \\
&ここで, \displaystyle T_i = \sum^{i}_{j=1} A_j^2とすると, \\
&= \displaystyle\sum^{N-1}_{i=1} A_i^2 \times (N-i) -  2A_i (S_N-S_i) + T_N - T_i \\
\end{align}
$$

 [7] $`\quad \displaystyle \sum^{N-1}_{i=1} \sum^{N}_{j=i+1} \lvert A_i - A_j \rvert`$

数列を並べ替えても答えは変わらないため、昇順にソートして考える.

$$
\begin{align}
与式 &= \displaystyle\sum^{N-1}_{i=1}\sum^{N}_{j=i+1} A_j - A_i \\
&= \displaystyle\sum^{N-1}_{i=1} S_n - S_i - A_i(N-i)  \\
&= \displaystyle\sum^{N}_{i=1} S_n - S_i - A_i(N-i)  \\
&= \displaystyle NS_N - \sum^{N}_{i=1} S_i + A_i (N-i)  \\
\end{align}
$$

 [*] $`\quad 空でないAの部分列の和の総和`$

TBD

 [*] $`\quad 空でないAの連続部分列の和の総和`$

TBD

 [*] $`\quad 空でないAの部分列の積の総和(mod \space 998244353)`$

TBD