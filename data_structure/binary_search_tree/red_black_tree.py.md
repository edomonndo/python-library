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
    - https://www.programiz.com/dsa/red-black-tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Implementing Red-Black Tree in Python\n# Adapted from https://www.programiz.com/dsa/red-black-tree\n\
    \nimport sys\nfrom typing import Type, TypeVar, Iterator\n\n\nT = TypeVar(\"T\"\
    , bound=\"Node\")\n\n\n# Node creation\nclass Node:\n\n    def __init__(self:\
    \ T, key: int) -> None:\n        self._key = key\n        self.parent = None\n\
    \        self.left = None\n        self.right = None\n        self._color = 1\n\
    \        self.value = None\n\n    def __repr__(self: T) -> str:\n        return\
    \ \"Key: \" + str(self._key) + \" Value: \" + str(self.value)\n\n    def get_color(self:\
    \ T) -> str:\n        return \"black\" if self._color == 0 else \"red\"\n\n  \
    \  def set_color(self: T, color: str) -> None:\n        if color == \"black\"\
    :\n            self._color = 0\n        elif color == \"red\":\n            self._color\
    \ = 1\n        else:\n            raise Exception(\"Unknown color\")\n\n    def\
    \ get_key(self: T) -> int:\n        return self._key\n\n    def is_red(self: T)\
    \ -> bool:\n        return self._color == 1\n\n    def is_black(self: T) -> bool:\n\
    \        return self._color == 0\n\n    def is_null(self: T) -> bool:\n      \
    \  return self._key is None\n\n    def depth(self: T) -> int:\n        return\
    \ 0 if self.parent is None else self.parent.depth() + 1\n\n    @classmethod\n\
    \    def null(cls: Type[T]) -> T:\n        node = cls(0)\n        node._key =\
    \ None\n        node.set_color(\"black\")\n        return node\n\n\nT = TypeVar(\"\
    T\", bound=\"RedBlackTree\")\n\n\nclass RedBlackTree:\n    def __init__(self:\
    \ T) -> None:\n        self.TNULL = Node.null()\n        self.root = self.TNULL\n\
    \        self.size = 0\n        self._iter_format = 0\n\n    # Dunder Methods\
    \ #\n    def __iter__(self: T) -> Iterator:\n        if self._iter_format == 0:\n\
    \            return iter(self.preorder())\n        if self._iter_format == 1:\n\
    \            return iter(self.inorder())\n        if self._iter_format == 2:\n\
    \            return iter(self.postorder())\n\n    def __getitem__(self: T, key:\
    \ int) -> int:\n        return self.search(key).value\n\n    def __setitem__(self:\
    \ T, key: int, value: int) -> None:\n        self.search(key).value = value\n\n\
    \    # Setters and Getters #\n    def get_root(self: T) -> Node:\n        return\
    \ self.root\n\n    def set_iteration_style(self: T, style: str) -> None:\n   \
    \     if style == \"pre\":\n            self._iter_format = 0\n        elif style\
    \ == \"in\":\n            self._iter_format = 1\n        elif style == \"post\"\
    :\n            self._iter_format = 2\n        else:\n            raise Exception(\"\
    Unknown style.\")\n\n    # Iterators #\n    def preorder(self: T) -> list:\n \
    \       return self.pre_order_helper(self.root)\n\n    def inorder(self: T) ->\
    \ list:\n        return self.in_order_helper(self.root)\n\n    def postorder(self:\
    \ T) -> list:\n        return self.post_order_helper(self.root)\n\n    def pre_order_helper(self:\
    \ T, node: Node) -> list:\n        \"\"\"\n        Perform a preorder tree traversal\
    \ starting at the\n        given node.\n        \"\"\"\n        output = []\n\
    \        if not node.is_null():\n            left = self.pre_order_helper(node.left)\n\
    \            right = self.pre_order_helper(node.right)\n            output.extend([node])\n\
    \            output.extend(left)\n            output.extend(right)\n        return\
    \ output\n\n    def in_order_helper(self: T, node: Node) -> list:\n        \"\"\
    \"\n        Perform a inorder tree traversal starting at the\n        given node.\n\
    \        \"\"\"\n        output = []\n        if not node.is_null():\n       \
    \     left = self.in_order_helper(node.left)\n            right = self.in_order_helper(node.right)\n\
    \            output.extend(left)\n            output.extend([node])\n        \
    \    output.extend(right)\n        return output\n\n    def post_order_helper(self:\
    \ T, node: Node) -> list:\n        output = []\n        if not node.is_null():\n\
    \            left = self.post_order_helper(node.left)\n            right = self.post_order_helper(node.right)\n\
    \            output.extend(left)\n            output.extend(right)\n         \
    \   output.extend([node])\n        return output\n\n    # Search the tree\n  \
    \  def search_tree_helper(self: T, node: Node, key: int) -> Node:\n        if\
    \ node.is_null() or key == node.get_key():\n            return node\n\n      \
    \  if key < node.get_key():\n            return self.search_tree_helper(node.left,\
    \ key)\n        return self.search_tree_helper(node.right, key)\n\n    # Balancing\
    \ the tree after deletion\n    def delete_fix(self: T, x: Node) -> None:\n   \
    \     while x != self.root and x.is_black():\n            if x == x.parent.left:\n\
    \                s = x.parent.right\n                if s.is_red():\n        \
    \            s.set_color(\"black\")\n                    x.parent.set_color(\"\
    red\")\n                    self.left_rotate(x.parent)\n                    s\
    \ = x.parent.right\n\n                if s.left.is_black() and s.right.is_black():\n\
    \                    s.set_color(\"red\")\n                    x = x.parent\n\
    \                else:\n                    if s.right.is_black():\n         \
    \               s.left.set_color(\"black\")\n                        s.set_color(\"\
    red\")\n                        self.right_rotate(s)\n                       \
    \ s = x.parent.right\n\n                    s.set_color(x.parent.get_color())\n\
    \                    x.parent.set_color(\"black\")\n                    s.right.set_color(\"\
    black\")\n                    self.left_rotate(x.parent)\n                   \
    \ x = self.root\n            else:\n                s = x.parent.left\n      \
    \          if s.is_red():\n                    s.set_color(\"black\")\n      \
    \              x.parent.set_color(\"red\")\n                    self.right_rotate(x.parent)\n\
    \                    s = x.parent.left\n\n                if s.left.is_black()\
    \ and s.right.is_black():\n                    s.set_color(\"red\")\n        \
    \            x = x.parent\n                else:\n                    if s.left.is_black():\n\
    \                        s.right.set_color(\"black\")\n                      \
    \  s.set_color(\"red\")\n                        self.left_rotate(s)\n       \
    \                 s = x.parent.left\n\n                    s.set_color(x.parent.get_color())\n\
    \                    x.parent.set_color(\"black\")\n                    s.left.set_color(\"\
    black\")\n                    self.right_rotate(x.parent)\n                  \
    \  x = self.root\n        x.set_color(\"black\")\n\n    def __rb_transplant(self:\
    \ T, u: Node, v: Node) -> None:\n        if u.parent is None:\n            self.root\
    \ = v\n        elif u == u.parent.left:\n            u.parent.left = v\n     \
    \   else:\n            u.parent.right = v\n        v.parent = u.parent\n\n   \
    \ # Node deletion\n    def delete_node_helper(self: T, node: Node, key: int) ->\
    \ None:\n        z = self.TNULL\n        while not node.is_null():\n         \
    \   if node.get_key() == key:\n                z = node\n\n            if node.get_key()\
    \ <= key:\n                node = node.right\n            else:\n            \
    \    node = node.left\n\n        if z.is_null():\n            # print(\"Cannot\
    \ find key in the tree\")\n            return\n\n        y = z\n        y_original_color\
    \ = y.get_color()\n        if z.left.is_null():\n            # If no left child,\
    \ just scoot the right subtree up\n            x = z.right\n            self.__rb_transplant(z,\
    \ z.right)\n        elif z.right.is_null():\n            # If no right child,\
    \ just scoot the left subtree up\n            x = z.left\n            self.__rb_transplant(z,\
    \ z.left)\n        else:\n            y = self.minimum(z.right)\n            y_original_color\
    \ = y.get_color()\n            x = y.right\n            if y.parent == z:\n  \
    \              x.parent = y\n            else:\n                self.__rb_transplant(y,\
    \ y.right)\n                y.right = z.right\n                y.right.parent\
    \ = y\n\n            self.__rb_transplant(z, y)\n            y.left = z.left\n\
    \            y.left.parent = y\n            y.set_color(z.get_color())\n     \
    \   if y_original_color == \"black\":\n            self.delete_fix(x)\n\n    \
    \    self.size -= 1\n\n    # Balance the tree after insertion\n    def fix_insert(self:\
    \ T, node: Node) -> None:\n        while node.parent.is_red():\n            if\
    \ node.parent == node.parent.parent.right:\n                u = node.parent.parent.left\n\
    \                if u.is_red():\n                    u.set_color(\"black\")\n\
    \                    node.parent.set_color(\"black\")\n                    node.parent.parent.set_color(\"\
    red\")\n                    node = node.parent.parent\n                else:\n\
    \                    if node == node.parent.left:\n                        node\
    \ = node.parent\n                        self.right_rotate(node)\n           \
    \         node.parent.set_color(\"black\")\n                    node.parent.parent.set_color(\"\
    red\")\n                    self.left_rotate(node.parent.parent)\n           \
    \ else:\n                u = node.parent.parent.right\n\n                if u.is_red():\n\
    \                    u.set_color(\"black\")\n                    node.parent.set_color(\"\
    black\")\n                    node.parent.parent.set_color(\"red\")\n        \
    \            node = node.parent.parent\n                else:\n              \
    \      if node == node.parent.right:\n                        node = node.parent\n\
    \                        self.left_rotate(node)\n                    node.parent.set_color(\"\
    black\")\n                    node.parent.parent.set_color(\"red\")\n        \
    \            self.right_rotate(node.parent.parent)\n            if node == self.root:\n\
    \                break\n        self.root.set_color(\"black\")\n\n    # Printing\
    \ the tree\n    def __print_helper(self: T, node: Node, indent: str, last: bool)\
    \ -> None:\n        if not node.is_null():\n            sys.stdout.write(indent)\n\
    \            if last:\n                sys.stdout.write(\"R----  \")\n       \
    \         indent += \"     \"\n            else:\n                sys.stdout.write(\"\
    L----   \")\n                indent += \"|    \"\n\n            s_color = \"RED\"\
    \ if node.is_red() else \"BLACK\"\n            print(str(node.get_key()) + \"\
    (\" + s_color + \")\")\n            self.__print_helper(node.left, indent, False)\n\
    \            self.__print_helper(node.right, indent, True)\n\n    def search(self:\
    \ T, key: int) -> Node:\n        return self.search_tree_helper(self.root, key)\n\
    \n    def minimum(self: T, node: Node = None) -> Node:\n        if node is None:\n\
    \            node = self.root\n        if node.is_null():\n            return\
    \ self.TNULL\n        while not node.left.is_null():\n            node = node.left\n\
    \        return node\n\n    def maximum(self: T, node: Node = None) -> Node:\n\
    \        if node is None:\n            node = self.root\n        if node.is_null():\n\
    \            return self.TNULL\n        while not node.right.is_null():\n    \
    \        node = node.right\n        return node\n\n    def successor(self: T,\
    \ x: Node) -> Node:\n        if not x.right.is_null():\n            return self.minimum(x.right)\n\
    \n        y = x.parent\n        while not y.is_null() and x == y.right:\n    \
    \        x = y\n            y = y.parent\n        return y\n\n    def predecessor(self:\
    \ T, x: Node) -> Node:\n        if not x.left.is_null():\n            return self.maximum(x.left)\n\
    \n        y = x.parent\n        while not y.is_null() and x == y.left:\n     \
    \       x = y\n            y = y.parent\n\n        return y\n\n    def left_rotate(self:\
    \ T, x: Node) -> None:\n        y = x.right\n        x.right = y.left\n      \
    \  if not y.left.is_null():\n            y.left.parent = x\n\n        y.parent\
    \ = x.parent\n        if x.parent is None:\n            self.root = y\n      \
    \  elif x == x.parent.left:\n            x.parent.left = y\n        else:\n  \
    \          x.parent.right = y\n        y.left = x\n        x.parent = y\n\n  \
    \  def right_rotate(self: T, x: Node) -> None:\n        y = x.left\n        x.left\
    \ = y.right\n        if not y.right.is_null():\n            y.right.parent = x\n\
    \n        y.parent = x.parent\n        if x.parent is None:\n            self.root\
    \ = y\n        elif x == x.parent.right:\n            x.parent.right = y\n   \
    \     else:\n            x.parent.left = y\n        y.right = x\n        x.parent\
    \ = y\n\n    def insert(self: T, key: int) -> None:\n        node = Node(key)\n\
    \        node.left = self.TNULL\n        node.right = self.TNULL\n        node.set_color(\"\
    red\")\n\n        y = None\n        x = self.root\n\n        while not x.is_null():\n\
    \            y = x\n            if node.get_key() < x.get_key():\n           \
    \     x = x.left\n            else:\n                x = x.right\n\n        node.parent\
    \ = y\n        if y is None:\n            self.root = node\n        elif node.get_key()\
    \ < y.get_key():\n            y.left = node\n        else:\n            y.right\
    \ = node\n\n        self.size += 1\n\n        if node.parent is None:\n      \
    \      node.set_color(\"black\")\n            return\n\n        if node.parent.parent\
    \ is None:\n            return\n\n        self.fix_insert(node)\n\n    def delete(self:\
    \ T, key: int) -> None:\n        self.delete_node_helper(self.root, key)\n\n \
    \   def print_tree(self: T) -> None:\n        self.__print_helper(self.root, \"\
    \", True)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/binary_search_tree/red_black_tree.py
  requiredBy: []
  timestamp: '2024-05-02 15:05:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/binary_search_tree/red_black_tree.py
layout: document
title: "\u5E73\u8861\u4E8C\u5206\u63A2\u7D22\u6728(\u8D64\u9ED2\u6728)"
---
