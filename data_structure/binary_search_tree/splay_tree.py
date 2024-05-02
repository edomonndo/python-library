class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class SplayTree:
    def __init__(self):
        self.root = None

    def maximum(self, n: Node) -> Node:
        while n.right is not None:
            n = n.right
        return n

    def rotate_left(self, n: Node):
        rc = n.right
        n.right = rc.left
        if rc.left is not None:
            rc.left.parent = n

        rc.parent = n.parent
        if n.parent is None:  # x is root
            self.root = rc
        elif n == n.parent.left:  # x is left child
            n.parent.left = rc
        else:  # x is right child
            n.parent.right = rc

        rc.left = n
        n.parent = rc

    def rotate_right(self, n: Node):
        lc = n.left
        n.left = lc.right
        if lc.right is not None:
            lc.right.parent = n

        lc.parent = n.parent
        if n.parent is None:  # x is root
            self.root = lc
        elif n == n.parent.right:  # x is right child
            n.parent.right = lc
        else:  # x is left child
            n.parent.left = lc

        lc.right = n
        n.parent = lc

    def splay(self, n: Node):
        while n.parent is not None:  # temp is not root
            if n.parent == self.root:  # one rotation if temp is child of root
                if n == n.parent.left:
                    self.rotate_right(n.parent)
                else:
                    self.rotate_left(n.parent)

            else:
                p = n.parent
                pp = p.parent

                if p.left == n and pp.left == p:  # both are left children
                    self.rotate_right(pp)
                    self.rotate_right(p)
                elif p.right == n and pp.right == p:  # both are right children
                    self.rotate_left(pp)
                    self.rotate_left(p)
                elif p.right == n and pp.left == p:
                    self.rotate_left(p)
                    self.rotate_right(pp)
                elif p.left == n and pp.right == p:
                    self.rotate_right(p)
                    self.rotate_left(pp)

    def insert(self, key):
        n = Node(key)
        x = None
        temp = self.root
        while temp is not None:
            x = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        n.parent = x

        if x is None:  # newly added temp is root
            self.root = n
        elif n.data < x.data:
            x.left = n
        else:
            x.right = n

        self.splay(n)

    def search(self, n: Node, x):
        try:
            while x != n.data:
                if x < n.data:
                    n = n.left
                elif x > n.data:
                    n = n.right
                else:
                    return None
            self.splay(n)
            return n
        except AttributeError:
            return None

    def delete(self, key):
        n = Node(key)
        self.splay(n)

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root is not None:
            left_subtree.root.parent = None

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root is not None:
            right_subtree.root.parent = None

        if left_subtree.root is not None:
            m = left_subtree.maximum(left_subtree.root)
            left_subtree.splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root
        else:
            self.root = right_subtree.root

    def inorder(self, n: Node):
        if n is not None:
            self.inorder(n.left)
            print(n.data)
            self.inorder(n.right)
