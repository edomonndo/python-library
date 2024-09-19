---
title: Suffix array
documentation_of: //str/suffix_array.py
---

Suffix arrayは文字列全てのsuffix（接尾辞）を辞書順でソートし,その開始位置を保持した配列.

#### 例
S=abracadabra

Sのすべてのsuffixとその開始位置,辞書順は,以下の通り.

|suffix|開始位置|辞書順|
|----|----|----|
|abracadabra|0|2|
|bracadabra|1|6|
|racadabra|2|10|
|acadabra|3|3|
|cadabra|4|7|
|adabra|5|4|
|dabra|6|8|
|abra|7|1|
|bra|8|5|
|ra|9|9|
|a|10|0|

よってSuffix arrayは `[10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]`

### `suffix_array_upper(s: List[int], upper: int)`

Listからsuffix arrayを求める.

### `suffix_array(s: str)`

文字列からsuffix arrayを求める.

### `lcp_array(s: str, sa: List[int])`

最長共通接頭辞(Longest common prefix)
を求める.Suffix arrayの前計算が必要.