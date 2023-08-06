# 競プロ用ライブラリ

[![Actions Status](https://github.com/edomonndo/python-library/workflows/verify/badge.svg)](https://github.com/edomonndo/python-library/actions)
[![GitHub Pages](https://img.shields.io/static/v1?label=GitHub+Pages&message=+&color=brightgreen&logo=github)](https://edomonndo.github.io/python-library/) 
[![edomondo](https://img.shields.io/endpoint?url=https%3A%2F%2Fatcoder-badges.now.sh%2Fapi%2Fatcoder%2Fjson%2Fedomondo)](https://atcoder.jp/users/edomondo)

## 必要なライブラリをインストールする

```
$ pip3 install online-judge-verify-helper
```

## verify自動実行

拡張子の前に`.test`をつけたファイルに,特定の方法でverify用問題のURLを書いておきます (たとえば Pythonであれば,`example.test.py`のようなファイルに`# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind`のような形で書きます.) このとき,次のコマンドでverifyできているかを確認してくれます.

```
$ oj-verify run
```

## ドキュメント生成

以下のコマンドを実行すると'.verify-helper/markdown/'にドキュメントが生成されます.例:'https://online-judge-tools.github.io/verification-helper/'

'''
$ oj-verify docs
'''

ドキュメント生成時に'Doxygen'風のコメントが見つかれば,それらは自動で利用されます. また,TeX記法の数式 (例: $O(N \sum_i A_i)$) の'MathJax'による表示にも対応しています. より詳しい説明はリファレンスにあります
