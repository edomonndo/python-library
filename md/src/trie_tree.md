---
title: Trie tree
documentation_of: //str/trie_tree.py
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