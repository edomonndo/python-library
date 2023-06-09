---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py\n\
    \nimport math\nfrom bisect import bisect_left, bisect_right\nfrom typing import\
    \ Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional\n\nT = TypeVar(\"\
    T\")\n\n\nclass SortedMultiset(Generic[T]):\n    BUCKET_RATIO = 50\n    REBUILD_RATIO\
    \ = 170\n\n    def _build(self, a: Optional[List[T]] = None) -> None:\n      \
    \  \"Evenly divide `a` into buckets.\"\n        if a is None:\n            a =\
    \ list(self)\n        size = self.size = len(a)\n        bucket_size = int(math.ceil(math.sqrt(size\
    \ / self.BUCKET_RATIO)))\n        self.a = [\n            a[size * i // bucket_size\
    \ : size * (i + 1) // bucket_size]\n            for i in range(bucket_size)\n\
    \        ]\n\n    def __init__(self, a: Iterable[T] = []) -> None:\n        \"\
    Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)\"\n   \
    \     a = list(a)\n        if not all(a[i] <= a[i + 1] for i in range(len(a) -\
    \ 1)):\n            a = sorted(a)\n        self._build(a)\n\n    def __iter__(self)\
    \ -> Iterator[T]:\n        for i in self.a:\n            for j in i:\n       \
    \         yield j\n\n    def __reversed__(self) -> Iterator[T]:\n        for i\
    \ in reversed(self.a):\n            for j in reversed(i):\n                yield\
    \ j\n\n    def __eq__(self, other) -> bool:\n        return list(self) == list(other)\n\
    \n    def __len__(self) -> int:\n        return self.size\n\n    def __repr__(self)\
    \ -> str:\n        return \"SortedMultiset\" + str(self.a)\n\n    def __str__(self)\
    \ -> str:\n        s = str(list(self))\n        return \"{\" + s[1 : len(s) -\
    \ 1] + \"}\"\n\n    def _position(self, x: T) -> Tuple[List[T], int]:\n      \
    \  \"Find the bucket and position which x should be inserted. self must not be\
    \ empty.\"\n        for a in self.a:\n            if x <= a[-1]:\n           \
    \     break\n        return (a, bisect_left(a, x))\n\n    def __contains__(self,\
    \ x: T) -> bool:\n        if self.size == 0:\n            return False\n     \
    \   a, i = self._position(x)\n        return i != len(a) and a[i] == x\n\n   \
    \ def count(self, x: T) -> int:\n        \"Count the number of x.\"\n        return\
    \ self.index_right(x) - self.index(x)\n\n    def add(self, x: T) -> None:\n  \
    \      \"Add an element. / O(\u221AN)\"\n        if self.size == 0:\n        \
    \    self.a = [[x]]\n            self.size = 1\n            return\n        a,\
    \ i = self._position(x)\n        a.insert(i, x)\n        self.size += 1\n    \
    \    if len(a) > len(self.a) * self.REBUILD_RATIO:\n            self._build()\n\
    \n    def _pop(self, a: List[T], i: int) -> T:\n        ans = a.pop(i)\n     \
    \   self.size -= 1\n        if not a:\n            self._build()\n        return\
    \ ans\n\n    def discard(self, x: T) -> bool:\n        \"Remove an element and\
    \ return True if removed. / O(\u221AN)\"\n        if self.size == 0:\n       \
    \     return False\n        a, i = self._position(x)\n        if i == len(a) or\
    \ a[i] != x:\n            return False\n        self._pop(a, i)\n        return\
    \ True\n\n    def lt(self, x: T) -> Optional[T]:\n        \"Find the largest element\
    \ < x, or None if it doesn't exist.\"\n        for a in reversed(self.a):\n  \
    \          if a[0] < x:\n                return a[bisect_left(a, x) - 1]\n\n \
    \   def le(self, x: T) -> Optional[T]:\n        \"Find the largest element <=\
    \ x, or None if it doesn't exist.\"\n        for a in reversed(self.a):\n    \
    \        if a[0] <= x:\n                return a[bisect_right(a, x) - 1]\n\n \
    \   def gt(self, x: T) -> Optional[T]:\n        \"Find the smallest element >\
    \ x, or None if it doesn't exist.\"\n        for a in self.a:\n            if\
    \ a[-1] > x:\n                return a[bisect_right(a, x)]\n\n    def ge(self,\
    \ x: T) -> Optional[T]:\n        \"Find the smallest element >= x, or None if\
    \ it doesn't exist.\"\n        for a in self.a:\n            if a[-1] >= x:\n\
    \                return a[bisect_left(a, x)]\n\n    def __getitem__(self, i: int)\
    \ -> T:\n        \"Return the i-th element.\"\n        if i < 0:\n           \
    \ for a in reversed(self.a):\n                i += len(a)\n                if\
    \ i >= 0:\n                    return a[i]\n        else:\n            for a in\
    \ self.a:\n                if i < len(a):\n                    return a[i]\n \
    \               i -= len(a)\n        raise IndexError\n\n    def pop(self, i:\
    \ int = -1) -> T:\n        \"Pop and return the i-th element.\"\n        if i\
    \ < 0:\n            for a in reversed(self.a):\n                i += len(a)\n\
    \                if i >= 0:\n                    return self._pop(a, i)\n    \
    \    else:\n            for a in self.a:\n                if i < len(a):\n   \
    \                 return self._pop(a, i)\n                i -= len(a)\n      \
    \  raise IndexError\n\n    def index(self, x: T) -> int:\n        \"Count the\
    \ number of elements < x.\"\n        ans = 0\n        for a in self.a:\n     \
    \       if a[-1] >= x:\n                return ans + bisect_left(a, x)\n     \
    \       ans += len(a)\n        return ans\n\n    def index_right(self, x: T) ->\
    \ int:\n        \"Count the number of elements <= x.\"\n        ans = 0\n    \
    \    for a in self.a:\n            if a[-1] > x:\n                return ans +\
    \ bisect_right(a, x)\n            ans += len(a)\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/SortedMultiset.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/SortedMultiset.py
layout: document
title: SortedMultiset
---

SortedSet の多重集合版です。同じ要素を複数入れることができます。

ソート済み列をいくつかのバケット (`list`) に分割して管理します。このとき、(バケットの個数) : (バケット内の個数) ${} = 1 : 50$ くらいにします。(`list` の `insert` / `pop` の定数倍が軽く、バケット再構築の定数倍が重いため)  
あるバケットが空になったり、多すぎたりしたら、1 度まとめて、均等にバケットに分割します。  
基本的に、全ての操作が (要素数を $N$ として) $O(\sqrt N)$ 時間で、(どのバケットか探す時間) < (バケットの中を探す時間) < (バケットへの挿入・削除) の順に重くなります。

### `SortedSet(a=[])`

iterable から SortedSet を作ります。重複がなく、かつソートされていれば $O(N)$ 時間、そうでなければ $O(N \log N)$ 時間です。

### `s.a`

SortedSet の中身です。`list` の `list` になっていて、中には要素が昇順に並んでいます。各バケットには要素が存在することが保証されます。

### `len(s)`

$O(1)$ 時間

### `x in s` / `x not in s`

$O(\sqrt N)$ 時間

### `iter(s)` / `for _ in s`

要素を昇順に走査するイテレータです。走査の途中で要素の追加 / 削除をしてはいけません。

$O(1)$ 時間

### `reversed(s)`

要素を降順に走査するイテレータです。走査の途中で要素の追加 / 削除をしてはいけません。

$O(1)$ 時間

### `s.add(x)`

`x` が `s` に含まれているかどうかに関わらず `x` を追加します。償却 $O(\sqrt N)$ 時間

### `s.discard(x)`

`x` が `s` に含まれていれば `x` を **1 個** 削除し、`True` を返します。含まれていない場合は `False` を返します。

償却 $O(\sqrt N)$ 時間

(C++ の [std::multiset::erase](https://cpprefjp.github.io/reference/set/multiset/erase.html) には `x` を全て削除してしまうという罠があります。)

### `s.lt(x)` / `s.le(x)` / `s.gt(x)` / `s.ge(x)`

`x` より小さい / 以下 / より大きい / 以上 で 最小 / 最大 の要素を返します。存在しなければ `None` を返します。 $O(\sqrt N)$ 時間

### `s[i]`

下から `i` 番目 / 上から `~i` 番目 の要素を返します。存在しない場合は `IndexError` を返します。  
`abs(i)` が小さいと高速に動作します。 $O(\frac{|i|}{\sqrt N})$ 時間

### `s.pop(i=-1)`

下から `i` 番目 / 上から `~i` 番目 の要素を削除するとともに返します。存在しない場合は `IndexError` を返します。  
`abs(i)` が小さいと高速に動作します。 $O(\frac{|i|}{\sqrt N})$ 時間

### `s.index(x)`

`x` より小さい要素の数を返します。`x` が `s` に含まれている場合は `list(s).index(x)` に相当します。 $O(\sqrt N)$ 時間

### `s.index_right(x)`

`x` 以下の要素の数を返します。 $O(\sqrt N)$ 時間

### `s == t`, `s != t`

集合として同一かどうかを判定します。 $O(N)$ 時間

### `s.count(x)`

s に含まれる x の個数を返します。 $O(\sqrt N)$ 時間