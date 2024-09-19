---
title: 回文木
documentation_of: //str/palindromic_tree.py
---

$S$の空でない回文部分文字列からなる集合$P$に対して，以下を求める

- `n`: $|P|$.
- `par`: 頂点$v (0 <= v < n)$に対し， その親の頂点番号. ただし，|str($v$)|$=2$ならば親は$0$, |str($v$)|$=1$ならば，親は$-1$と定義する．
- `suffix_link`: 頂点$v (0 <= v < n)$に対し， $v$からのsuffix linkの行き先$s_v$ (str($v$)の空でない接尾辞回文のうち，str($v$)より短いもののうち最大のものに対応する頂点). ただし，そのような接尾辞回文が存在しない場合には$s_v = 0$と定義する．
- `max_palindromic_suffix`: $S$の長さ$i$の接尾辞$S_0 ⋯ S_{i-1}$の最大回文接尾辞に対する頂点番号$v_i$.

https://math314.hateblo.jp/entry/2016/12/19/005919