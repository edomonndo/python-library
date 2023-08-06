# Trieノードを格納するクラス
class TrieTree:
    class Node:
        # 格納する文字列の種類(a-z)
        CHAR_SIZE = 26

        def __init__(self, char=""):
            self.char = char
            self.children = [None] * self.CHAR_SIZE
            self.word_finieshed = False
            self.matched_prefix_count = 0

        def __str__(self):
            return self.char

    def __init__(self):
        self.root = self.Node()

    def _convert_char_to_num(self, char):
        assert ord("a") <= ord(char) <= ord("z")
        return ord(char) - ord("a")

    def insert(self, key: str):
        # ルートノードから開始します
        curr = self.root
        for s in key:
            idx = self._convert_char_to_num(s)
            # 次のノードが存在しない場合に新しいノードを作成します
            if curr.children[idx] is None:
                curr.children[idx] = self.Node(s)
            # 次のノードに移動する
            curr = curr.children[idx]
            curr.matched_prefix_count += 1

        # 現在のノードをリーフとしてマークします
        curr.word_finieshed = True

    # Trie内のキーを検索するための反復関数.
    # キーと一致する単語がTrieで見つかった場合はTrueを返す.それ以外の場合は,Falseを返す.
    # 2つ目の返り値はキーと同じprefixを持つワードの数
    def search(self, key: str, prefix=False):
        curr = self.root
        for s in key:
            idx = ord(s) - ord("a")
            curr = curr.children[idx]
            if curr is None:
                return False, 0
        if prefix:
            return True, curr.matched_prefix_count
        return curr.word_finieshed, curr.matched_prefix_count

    # キーをprefixに持つ単語が存在するかを検索
    def starts_with(self, key: str):
        return self.search(key, prefix=True)


if __name__ == "__main__":
    trie = TrieTree()
    trie.insert("a")
    trie.insert("to")
    trie.insert("tea")
    trie.insert("ted")
    trie.insert("ten")
    trie.insert("i")
    trie.insert("in")
    trie.insert("inn")
    # (True, 1)
    print(trie.search("a"))
    # (False, 4)
    print(trie.search("t"))
    # (True, 1)
    print(trie.search("ted"))
    # (False, 0)
    print(trie.search("tel"))
    # (True, 2)
    print(trie.search("in"))
    # (True, 1)
    print(trie.search("inn"))
