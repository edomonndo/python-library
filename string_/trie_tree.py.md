---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Trie\u30CE\u30FC\u30C9\u3092\u683C\u7D0D\u3059\u308B\u30AF\u30E9\u30B9\n\
    class TrieTree:\n    class Node:\n        # \u683C\u7D0D\u3059\u308B\u6587\u5B57\
    \u5217\u306E\u7A2E\u985E(a-z)\n        CHAR_SIZE = 26\n\n        def __init__(self,\
    \ char=\"\"):\n            self.char = char\n            self.children = [None]\
    \ * self.CHAR_SIZE\n            self.word_finieshed = False\n            self.matched_prefix_count\
    \ = 0\n\n        def __str__(self):\n            return self.char\n\n    def __init__(self):\n\
    \        self.root = self.Node()\n\n    def _convert_char_to_num(self, char):\n\
    \        assert ord(\"a\") <= ord(char) <= ord(\"z\")\n        return ord(char)\
    \ - ord(\"a\")\n\n    def insert(self, key: str):\n        # \u30EB\u30FC\u30C8\
    \u30CE\u30FC\u30C9\u304B\u3089\u958B\u59CB\u3057\u307E\u3059\n        curr = self.root\n\
    \        for s in key:\n            idx = self._convert_char_to_num(s)\n     \
    \       # \u6B21\u306E\u30CE\u30FC\u30C9\u304C\u5B58\u5728\u3057\u306A\u3044\u5834\
    \u5408\u306B\u65B0\u3057\u3044\u30CE\u30FC\u30C9\u3092\u4F5C\u6210\u3057\u307E\
    \u3059\n            if curr.children[idx] is None:\n                curr.children[idx]\
    \ = self.Node(s)\n            # \u6B21\u306E\u30CE\u30FC\u30C9\u306B\u79FB\u52D5\
    \u3059\u308B\n            curr = curr.children[idx]\n            curr.matched_prefix_count\
    \ += 1\n\n        # \u73FE\u5728\u306E\u30CE\u30FC\u30C9\u3092\u30EA\u30FC\u30D5\
    \u3068\u3057\u3066\u30DE\u30FC\u30AF\u3057\u307E\u3059\n        curr.word_finieshed\
    \ = True\n\n    # Trie\u5185\u306E\u30AD\u30FC\u3092\u691C\u7D22\u3059\u308B\u305F\
    \u3081\u306E\u53CD\u5FA9\u95A2\u6570.\n    # \u30AD\u30FC\u3068\u4E00\u81F4\u3059\
    \u308B\u5358\u8A9E\u304CTrie\u3067\u898B\u3064\u304B\u3063\u305F\u5834\u5408\u306F\
    True\u3092\u8FD4\u3059.\u305D\u308C\u4EE5\u5916\u306E\u5834\u5408\u306F,False\u3092\
    \u8FD4\u3059.\n    # 2\u3064\u76EE\u306E\u8FD4\u308A\u5024\u306F\u30AD\u30FC\u3068\
    \u540C\u3058prefix\u3092\u6301\u3064\u30EF\u30FC\u30C9\u306E\u6570\n    def search(self,\
    \ key: str, prefix=False):\n        curr = self.root\n        for s in key:\n\
    \            idx = ord(s) - ord(\"a\")\n            curr = curr.children[idx]\n\
    \            if curr is None:\n                return False, 0\n        if prefix:\n\
    \            return True, curr.matched_prefix_count\n        return curr.word_finieshed,\
    \ curr.matched_prefix_count\n\n    # \u30AD\u30FC\u3092prefix\u306B\u6301\u3064\
    \u5358\u8A9E\u304C\u5B58\u5728\u3059\u308B\u304B\u3092\u691C\u7D22\n    def starts_with(self,\
    \ key: str):\n        return self.search(key, prefix=True)\n"
  dependsOn: []
  isVerificationFile: false
  path: string_/trie_tree.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: string_/trie_tree.py
layout: document
title: Trie tree
---

トライ木は文字列検索を高速にするための木構造.
一文字を1ノードとして木をつくる.

### `trie = TrieTree()`

初期化.

### `trie.insert(s: str)`

文字列$s$を辞書（トライ木）に登録する.

### `trie.search(s: str)`

文字列$s$が辞書（トライ木）に登録されているかを確認する.
2つ目の返り値は文字列$s$と同じprefixを持つワードの数.

### `trie.starts_with(s: str)`

文字列$s$を接頭辞にする単語が辞書（トライ木）に登録されているかを確認する.
2つ目の返り値は文字列$s$と同じprefixを持つワードの数.