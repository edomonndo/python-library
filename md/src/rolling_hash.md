---
title: ローリングハッシュ
documentation_of: //str/rolling_hash.py
---

文字列を高速に検索する.

### RollingHash(list, mod, base)

文字列は整数(>0)に変換しておくこと．(例：`LIST = [ord(s)-ord("a")+1 for s in S]`)

baseの指定がない場合，2以上mod未満の値からランダムに選択する.

### update(p, x)

0-indexでp番目の値をxに変更する.

### get(l, r)

区間$[l,r)$のハッシュを取得する．