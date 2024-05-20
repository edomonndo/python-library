class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val) -> None:
        cur = Node(val)
        if not self.head:
            self.head = cur
            self.tail = self.head
        else:
            self.tail.next = cur
            cur.prev = self.tail
            self.tail = cur
        self.length += 1

    def pop(self) -> Node:
        if not self.head:
            raise IndexError("pop from empty list")
        tail = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = tail.prev
            self.tail.next = None
            tail.prev = None
        self.length -= 1
        return tail

    def popleft(self) -> Node:
        if self.length == 0:
            raise IndexError("popleft from empty list")
        head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = head.next
        head.next = None
        self.length -= 1
        return head

    def appendleft(self, val) -> None:
        cur = Node(val)
        if self.length == 0:
            self.head = cur
            self.tail = cur
        else:
            self.head.prev = cur
            cur.next = self.head
            self.head = cur
        self.length += 1

    def __getitem__(self, index) -> Node:
        if (index < 0) or (index > self.length):
            raise IndexError
        halfOfLength = self.length // 2
        if index <= halfOfLength:
            cnt = 0
            cur = self.head
            while cnt != index:
                cur = cur.next
                cnt = cnt + 1
            return cur
        elif index > halfOfLength:
            cnt = self.length - 1
            cur = self.tail
            while cnt != index:
                cur = cur.prev
                cnt = cnt - 1
            return cur

    def __setitem__(self, index, val) -> None:
        targetNode = self.get(index)
        targetNode.val = val

    def insert(self, index, val) -> None:
        if (index < 0) or (index > self.length):
            raise IndexError
        if index == 0:
            self.appendleft(val)
        if index == self.length:
            self.append(val)
        pre = self.get(index - 1)
        cur = Node(val)
        nex = pre.next
        pre.next = cur
        cur.prev = pre
        nex.prev = cur
        cur.next = nex
        self.length += 1

    def remove(self, index) -> Node:
        if (index < 0) or (index >= self.length):
            raise IndexError
        if index == 0:
            self.popleft()
        if index == self.length - 1:
            self.pop()
        cur = self.get(index)
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur.next = None
        cur.prev = None
        self.length -= 1
        return cur

    def reverse(self) -> None:
        node = self.head
        self.head = self.tail
        self.tail = node
        tmpPrev = None
        tmpNext = None
        while node:
            tmpPrev = node.prev
            tmpNext = node.next
            node.next = tmpPrev
            node.prev = tmpNext
            node = node.prev

    def tolist(self) -> None:
        arr = []
        cur = self.head
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
        return arr
