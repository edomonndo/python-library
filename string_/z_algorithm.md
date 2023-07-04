---
title: Z algorithm
documentation_of: ./z_algorithm.py
---

z配列 $Z[i]$は、
文字列$S=S[0]+S[1]+⋯+S[|S|−1]$ と
文字列$S[i]+S[i+1]+⋯+S[|S|−1]$ の
**最長共通接頭辞の長さ**と表す。

### `z_algorithm(s: str)`

文字列からz配列を求める。