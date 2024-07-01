---
title: 典型問題（足し上げ）
documentation_of: ./typical_problems_of_sum.py
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
