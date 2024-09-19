---
title: 中国余剰定理
documentation_of: //number_theory/chinese_remainder_theorem.py
---

$m1$と$m2$を互いに素な正の整数とする．  
$x \equiv b_1 \pmod {m_1}$  
$x \equiv b_2 \pmod {m_2}$  
を満たす$x$が$0$以上$m_1m_2$未満にただ1つ存在する．特にそれを$r$とすると，  

$x \equiv b_1 \pmod {m_1}, x \equiv b_2 \pmod {m_2} \Leftrightarrow x \equiv r \pmod {m_1m_2}$  
が成立する．

## 使用例

```
y, z = crt(r, m)
```
同じ長さの配列$r,m$を渡す．この配列の長さを$n$としたとき，  
$x \equiv r[i] \pmod {m[i]} \quad (0<=i<N)$　　
を解く．答えは$y,z \quad (0<=y<z=lcm(m[i]))$を用いて$x \equiv y \pmod z$の形で書けることが知られており，この$(y,z)$をタプルで返す．答えがない場合は，$(0,0)$を返す．

## 計算量

$O(n \log lcm(m[i]))$



