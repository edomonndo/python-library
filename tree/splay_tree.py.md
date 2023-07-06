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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Node:\n    def __init__(self, data):\n        self.data = data\n  \
    \      self.parent = None\n        self.left = None\n        self.right = None\n\
    \n    def __str__(self):\n        return str(self.data)\n\n\nclass SplayTree:\n\
    \    def __init__(self):\n        self.root = None\n\n    def maximum(self, n:\
    \ Node) -> Node:\n        while n.right is not None:\n            n = n.right\n\
    \        return n\n\n    def rotate_left(self, n: Node):\n        rc = n.right\n\
    \        n.right = rc.left\n        if rc.left is not None:\n            rc.left.parent\
    \ = n\n\n        rc.parent = n.parent\n        if n.parent is None:  # x is root\n\
    \            self.root = rc\n        elif n == n.parent.left:  # x is left child\n\
    \            n.parent.left = rc\n        else:  # x is right child\n         \
    \   n.parent.right = rc\n\n        rc.left = n\n        n.parent = rc\n\n    def\
    \ rotate_right(self, n: Node):\n        lc = n.left\n        n.left = lc.right\n\
    \        if lc.right is not None:\n            lc.right.parent = n\n\n       \
    \ lc.parent = n.parent\n        if n.parent is None:  # x is root\n          \
    \  self.root = lc\n        elif n == n.parent.right:  # x is right child\n   \
    \         n.parent.right = lc\n        else:  # x is left child\n            n.parent.left\
    \ = lc\n\n        lc.right = n\n        n.parent = lc\n\n    def splay(self, n:\
    \ Node):\n        while n.parent is not None:  # temp is not root\n          \
    \  if n.parent == self.root:  # one rotation if temp is child of root\n      \
    \          if n == n.parent.left:\n                    self.rotate_right(n.parent)\n\
    \                else:\n                    self.rotate_left(n.parent)\n\n   \
    \         else:\n                p = n.parent\n                pp = p.parent\n\
    \n                if p.left == n and pp.left == p:  # both are left children\n\
    \                    self.rotate_right(pp)\n                    self.rotate_right(p)\n\
    \                elif p.right == n and pp.right == p:  # both are right children\n\
    \                    self.rotate_left(pp)\n                    self.rotate_left(p)\n\
    \                elif p.right == n and pp.left == p:\n                    self.rotate_left(p)\n\
    \                    self.rotate_right(pp)\n                elif p.left == n and\
    \ pp.right == p:\n                    self.rotate_right(p)\n                 \
    \   self.rotate_left(pp)\n\n    def insert(self, n: Node):\n        x = None\n\
    \        temp = self.root\n        while temp is not None:\n            x = temp\n\
    \            if n.data < temp.data:\n                temp = temp.left\n      \
    \      else:\n                temp = temp.right\n\n        n.parent = x\n\n  \
    \      if x is None:  # newly added temp is root\n            self.root = n\n\
    \        elif n.data < x.data:\n            x.left = n\n        else:\n      \
    \      x.right = n\n\n        self.splay(n)\n\n    def search(self, n: Node, x):\n\
    \        try:\n            while x != n.data:\n                if x < n.data:\n\
    \                    n = n.left\n                elif x > n.data:\n          \
    \          n = n.right\n                else:\n                    return None\n\
    \            self.splay(n)\n            return n\n        except AttributeError:\n\
    \            return None\n\n    def delete(self, n: Node):\n        self.splay(n)\n\
    \n        left_subtree = SplayTree()\n        left_subtree.root = self.root.left\n\
    \        if left_subtree.root is not None:\n            left_subtree.root.parent\
    \ = None\n\n        right_subtree = SplayTree()\n        right_subtree.root =\
    \ self.root.right\n        if right_subtree.root is not None:\n            right_subtree.root.parent\
    \ = None\n\n        if left_subtree.root is not None:\n            m = left_subtree.maximum(left_subtree.root)\n\
    \            left_subtree.splay(m)\n            left_subtree.root.right = right_subtree.root\n\
    \            self.root = left_subtree.root\n        else:\n            self.root\
    \ = right_subtree.root\n\n    def inorder(self, n: Node):\n        if n is not\
    \ None:\n            self.inorder(n.left)\n            print(n.data)\n       \
    \     self.inorder(n.right)\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/splay_tree.py
  requiredBy: []
  timestamp: '2023-07-06 11:56:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/splay_tree.py
layout: document
redirect_from:
- /library/tree/splay_tree.py
- /library/tree/splay_tree.py.html
title: tree/splay_tree.py
---
