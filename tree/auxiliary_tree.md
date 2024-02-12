---
title: Auxiliary tree
documentation_of: ./auxiliary_tree.py
---

木から、頂点集合$vs$とそれらのLCAからなる木を構築する
.
木の頂点数が圧縮され、$vs$の頂点数を$k$としたとき頂点数の上限は$2k-1$となる.

実装はEulerTour + Segment TreeでLCAを求めている.(前処理: $O(N)$, 構築: $O(k(logk + logN))$)

https://atcoder.jp/contests/abc340/tasks/abc340_g