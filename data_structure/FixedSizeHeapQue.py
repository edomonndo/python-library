class FixedSizeHeapQue:
    def __init__(self, arr=[], max_size=10**8):
        self.size = 0
        self.heap = arr
        self.max_size = max_size

        n = len(arr)
        self.size = n
        self.heapify()

    def heapify(self):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        for i in reversed(range(self.size // 2)):
            self._siftup(i)

    def push(self, item):
        """Push item onto heap, maintaining the heap invariant."""
        if self.size < self.max_size:
            self.heap.append(item)
            self.size += 1
            self._siftdown(0, self.size - 1)
        else:
            self._replace(item)

    def pop(self):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = self.heap.pop()  # raises appropriate IndexError if heap is empty
        self.size -= 1
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            _siftup(0)
            return returnitem
        return lastelt

    def pushpop(self, item):
        """Fast version of a heappush followed by a heappop."""
        if self.heap and self.heap[0] < item:
            item, self.heap[0] = self.heap[0], item
            self._siftup(0)
        return item

    def _replace(self, item):
        """Pop and return the current smallest value, and add the new item.

        This is more efficient than heappop() followed by heappush(), and can be
        more appropriate when using a fixed-size heap.  Note that the value
        returned may be larger than item!  That constrains reasonable uses of
        this routine unless written as part of a conditional replacement:

            if item > heap[0]:
                item = heapreplace(heap, item)
        """
        returnitem = self.heap[0]  # raises appropriate IndexError if heap is empty
        self.heap[0] = item
        self._siftup(0)
        return returnitem

    def _siftup(self, pos):
        endpos = self.size
        startpos = pos
        newitem = self.heap[pos]
        childpos = 2 * pos + 1
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1
        self.heap[pos] = newitem
        self._siftdown(startpos, pos)

    def _siftdown(self, startpos, pos):
        newitem = self.heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem
