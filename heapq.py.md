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
    - http://code.activestate.com/recipes/577573-compare-algorithms-for-heapqsmallest
    - http://en.wikipedia.org/wiki/Harmonic_series_(mathematics)#Rate_of_divergence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"Heap queue algorithm (a.k.a. priority queue).\n\nHeaps are arrays for\
    \ which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for\nall k, counting elements from\
    \ 0.  For the sake of comparison,\nnon-existing elements are considered to be\
    \ infinite.  The interesting\nproperty of a heap is that a[0] is always its smallest\
    \ element.\n\nUsage:\n\nheap = []            # creates an empty heap\nheappush(heap,\
    \ item) # pushes a new item on the heap\nitem = heappop(heap) # pops the smallest\
    \ item from the heap\nitem = heap[0]       # smallest item on the heap without\
    \ popping it\nheapify(x)           # transforms list into a heap, in-place, in\
    \ linear time\nitem = heappushpop(heap, item) # pushes a new item and then returns\n\
    \                               # the smallest item; the heap size is unchanged\n\
    item = heapreplace(heap, item) # pops and returns smallest item, and adds\n  \
    \                             # new item; the heap size is unchanged\n\nOur API\
    \ differs from textbook heap algorithms as follows:\n\n- We use 0-based indexing.\
    \  This makes the relationship between the\n  index for a node and the indexes\
    \ for its children slightly less\n  obvious, but is more suitable since Python\
    \ uses 0-based indexing.\n\n- Our heappop() method returns the smallest item,\
    \ not the largest.\n\nThese two make it possible to view the heap as a regular\
    \ Python list\nwithout surprises: heap[0] is the smallest item, and heap.sort()\n\
    maintains the heap invariant!\n\"\"\"\n\n# Original code by Kevin O'Connor, augmented\
    \ by Tim Peters and Raymond Hettinger\n\n__about__ = \"\"\"Heap queues\n\n[explanation\
    \ by Fran\xE7ois Pinard]\n\nHeaps are arrays for which a[k] <= a[2*k+1] and a[k]\
    \ <= a[2*k+2] for\nall k, counting elements from 0.  For the sake of comparison,\n\
    non-existing elements are considered to be infinite.  The interesting\nproperty\
    \ of a heap is that a[0] is always its smallest element.\n\nThe strange invariant\
    \ above is meant to be an efficient memory\nrepresentation for a tournament. \
    \ The numbers below are `k', not a[k]:\n\n                                   0\n\
    \n                  1                                 2\n\n          3       \
    \        4                5               6\n\n      7       8       9       10\
    \      11      12      13      14\n\n    15 16   17 18   19 20   21 22   23 24\
    \   25 26   27 28   29 30\n\n\nIn the tree above, each cell `k' is topping `2*k+1'\
    \ and `2*k+2'.  In\na usual binary tournament we see in sports, each cell is the\
    \ winner\nover the two cells it tops, and we can trace the winner down the tree\n\
    to see all opponents s/he had.  However, in many computer applications\nof such\
    \ tournaments, we do not need to trace the history of a winner.\nTo be more memory\
    \ efficient, when a winner is promoted, we try to\nreplace it by something else\
    \ at a lower level, and the rule becomes\nthat a cell and the two cells it tops\
    \ contain three different items,\nbut the top cell \"wins\" over the two topped\
    \ cells.\n\nIf this heap invariant is protected at all time, index 0 is clearly\n\
    the overall winner.  The simplest algorithmic way to remove it and\nfind the \"\
    next\" winner is to move some loser (let's say cell 30 in the\ndiagram above)\
    \ into the 0 position, and then percolate this new 0 down\nthe tree, exchanging\
    \ values, until the invariant is re-established.\nThis is clearly logarithmic\
    \ on the total number of items in the tree.\nBy iterating over all items, you\
    \ get an O(n ln n) sort.\n\nA nice feature of this sort is that you can efficiently\
    \ insert new\nitems while the sort is going on, provided that the inserted items\
    \ are\nnot \"better\" than the last 0'th element you extracted.  This is\nespecially\
    \ useful in simulation contexts, where the tree holds all\nincoming events, and\
    \ the \"win\" condition means the smallest scheduled\ntime.  When an event schedule\
    \ other events for execution, they are\nscheduled into the future, so they can\
    \ easily go into the heap.  So, a\nheap is a good structure for implementing schedulers\
    \ (this is what I\nused for my MIDI sequencer :-).\n\nVarious structures for implementing\
    \ schedulers have been extensively\nstudied, and heaps are good for this, as they\
    \ are reasonably speedy,\nthe speed is almost constant, and the worst case is\
    \ not much different\nthan the average case.  However, there are other representations\
    \ which\nare more efficient overall, yet the worst cases might be terrible.\n\n\
    Heaps are also very useful in big disk sorts.  You most probably all\nknow that\
    \ a big sort implies producing \"runs\" (which are pre-sorted\nsequences, which\
    \ size is usually related to the amount of CPU memory),\nfollowed by a merging\
    \ passes for these runs, which merging is often\nvery cleverly organised[1]. \
    \ It is very important that the initial\nsort produces the longest runs possible.\
    \  Tournaments are a good way\nto that.  If, using all the memory available to\
    \ hold a tournament, you\nreplace and percolate items that happen to fit the current\
    \ run, you'll\nproduce runs which are twice the size of the memory for random\
    \ input,\nand much better for input fuzzily ordered.\n\nMoreover, if you output\
    \ the 0'th item on disk and get an input which\nmay not fit in the current tournament\
    \ (because the value \"wins\" over\nthe last output value), it cannot fit in the\
    \ heap, so the size of the\nheap decreases.  The freed memory could be cleverly\
    \ reused immediately\nfor progressively building a second heap, which grows at\
    \ exactly the\nsame rate the first heap is melting.  When the first heap completely\n\
    vanishes, you switch heaps and start a new run.  Clever and quite\neffective!\n\
    \nIn a word, heaps are useful memory structures to know.  I use them in\na few\
    \ applications, and I think it is good to keep a `heap' module\naround. :-)\n\n\
    --------------------\n[1] The disk balancing algorithms which are current, nowadays,\
    \ are\nmore annoying than clever, and this is a consequence of the seeking\ncapabilities\
    \ of the disks.  On devices which cannot seek, like big\ntape drives, the story\
    \ was quite different, and one had to be very\nclever to ensure (far in advance)\
    \ that each tape movement will be the\nmost effective possible (that is, will\
    \ best participate at\n\"progressing\" the merge).  Some tapes were even able\
    \ to read\nbackwards, and this was also used to avoid the rewinding time.\nBelieve\
    \ me, real good tape sorts were quite spectacular to watch!\nFrom all times, sorting\
    \ has always been a Great Art! :-)\n\"\"\"\n\n__all__ = [\n    \"heappush\",\n\
    \    \"heappop\",\n    \"heapify\",\n    \"heapreplace\",\n    \"merge\",\n  \
    \  \"nlargest\",\n    \"nsmallest\",\n    \"heappushpop\",\n]\n\n\ndef heappush(heap,\
    \ item):\n    \"\"\"Push item onto heap, maintaining the heap invariant.\"\"\"\
    \n    heap.append(item)\n    _siftdown(heap, 0, len(heap) - 1)\n\n\ndef heappop(heap):\n\
    \    \"\"\"Pop the smallest item off the heap, maintaining the heap invariant.\"\
    \"\"\n    lastelt = heap.pop()  # raises appropriate IndexError if heap is empty\n\
    \    if heap:\n        returnitem = heap[0]\n        heap[0] = lastelt\n     \
    \   _siftup(heap, 0)\n        return returnitem\n    return lastelt\n\n\ndef heapreplace(heap,\
    \ item):\n    \"\"\"Pop and return the current smallest value, and add the new\
    \ item.\n\n    This is more efficient than heappop() followed by heappush(), and\
    \ can be\n    more appropriate when using a fixed-size heap.  Note that the value\n\
    \    returned may be larger than item!  That constrains reasonable uses of\n \
    \   this routine unless written as part of a conditional replacement:\n\n    \
    \    if item > heap[0]:\n            item = heapreplace(heap, item)\n    \"\"\"\
    \n    returnitem = heap[0]  # raises appropriate IndexError if heap is empty\n\
    \    heap[0] = item\n    _siftup(heap, 0)\n    return returnitem\n\n\ndef heappushpop(heap,\
    \ item):\n    \"\"\"Fast version of a heappush followed by a heappop.\"\"\"\n\
    \    if heap and heap[0] < item:\n        item, heap[0] = heap[0], item\n    \
    \    _siftup(heap, 0)\n    return item\n\n\ndef heapify(x):\n    \"\"\"Transform\
    \ list into a heap, in-place, in O(len(x)) time.\"\"\"\n    n = len(x)\n    #\
    \ Transform bottom-up.  The largest index there's any point to looking at\n  \
    \  # is the largest with a child index in-range, so must have 2*i + 1 < n,\n \
    \   # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so\n    #\
    \ j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is\n    #\
    \ (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.\n    for i in\
    \ reversed(range(n // 2)):\n        _siftup(x, i)\n\n\ndef _heappop_max(heap):\n\
    \    \"\"\"Maxheap version of a heappop.\"\"\"\n    lastelt = heap.pop()  # raises\
    \ appropriate IndexError if heap is empty\n    if heap:\n        returnitem =\
    \ heap[0]\n        heap[0] = lastelt\n        _siftup_max(heap, 0)\n        return\
    \ returnitem\n    return lastelt\n\n\ndef _heapreplace_max(heap, item):\n    \"\
    \"\"Maxheap version of a heappop followed by a heappush.\"\"\"\n    returnitem\
    \ = heap[0]  # raises appropriate IndexError if heap is empty\n    heap[0] = item\n\
    \    _siftup_max(heap, 0)\n    return returnitem\n\n\ndef _heapify_max(x):\n \
    \   \"\"\"Transform list into a maxheap, in-place, in O(len(x)) time.\"\"\"\n\
    \    n = len(x)\n    for i in reversed(range(n // 2)):\n        _siftup_max(x,\
    \ i)\n\n\n# 'heap' is a heap at all indices >= startpos, except possibly for pos.\
    \  pos\n# is the index of a leaf with a possibly out-of-order value.  Restore\
    \ the\n# heap invariant.\ndef _siftdown(heap, startpos, pos):\n    newitem = heap[pos]\n\
    \    # Follow the path to the root, moving parents down until finding a place\n\
    \    # newitem fits.\n    while pos > startpos:\n        parentpos = (pos - 1)\
    \ >> 1\n        parent = heap[parentpos]\n        if newitem < parent:\n     \
    \       heap[pos] = parent\n            pos = parentpos\n            continue\n\
    \        break\n    heap[pos] = newitem\n\n\n# The child indices of heap index\
    \ pos are already heaps, and we want to make\n# a heap at index pos too.  We do\
    \ this by bubbling the smaller child of\n# pos up (and so on with that child's\
    \ children, etc) until hitting a leaf,\n# then using _siftdown to move the oddball\
    \ originally at index pos into place.\n#\n# We *could* break out of the loop as\
    \ soon as we find a pos where newitem <=\n# both its children, but turns out that's\
    \ not a good idea, and despite that\n# many books write the algorithm that way.\
    \  During a heap pop, the last array\n# element is sifted in, and that tends to\
    \ be large, so that comparing it\n# against values starting from the root usually\
    \ doesn't pay (= usually doesn't\n# get us out of the loop early).  See Knuth,\
    \ Volume 3, where this is\n# explained and quantified in an exercise.\n#\n# Cutting\
    \ the # of comparisons is important, since these routines have no\n# way to extract\
    \ \"the priority\" from an array element, so that intelligence\n# is likely to\
    \ be hiding in custom comparison methods, or in array elements\n# storing (priority,\
    \ record) tuples.  Comparisons are thus potentially\n# expensive.\n#\n# On random\
    \ arrays of length 1000, making this change cut the number of\n# comparisons made\
    \ by heapify() a little, and those made by exhaustive\n# heappop() a lot, in accord\
    \ with theory.  Here are typical results from 3\n# runs (3 just to demonstrate\
    \ how small the variance is):\n#\n# Compares needed by heapify     Compares needed\
    \ by 1000 heappops\n# --------------------------     --------------------------------\n\
    # 1837 cut to 1663               14996 cut to 8680\n# 1855 cut to 1659       \
    \        14966 cut to 8678\n# 1847 cut to 1660               15024 cut to 8703\n\
    #\n# Building the heap by using heappush() 1000 times instead required\n# 2198,\
    \ 2148, and 2219 compares:  heapify() is more efficient, when\n# you can use it.\n\
    #\n# The total compares needed by list.sort() on the same lists were 8627,\n#\
    \ 8627, and 8632 (this should be compared to the sum of heapify() and\n# heappop()\
    \ compares):  list.sort() is (unsurprisingly!) more efficient\n# for sorting.\n\
    \n\ndef _siftup(heap, pos):\n    endpos = len(heap)\n    startpos = pos\n    newitem\
    \ = heap[pos]\n    # Bubble up the smaller child until hitting a leaf.\n    childpos\
    \ = 2 * pos + 1  # leftmost child position\n    while childpos < endpos:\n   \
    \     # Set childpos to index of smaller child.\n        rightpos = childpos +\
    \ 1\n        if rightpos < endpos and not heap[childpos] < heap[rightpos]:\n \
    \           childpos = rightpos\n        # Move the smaller child up.\n      \
    \  heap[pos] = heap[childpos]\n        pos = childpos\n        childpos = 2 *\
    \ pos + 1\n    # The leaf at pos is empty now.  Put newitem there, and bubble\
    \ it up\n    # to its final resting place (by sifting its parents down).\n   \
    \ heap[pos] = newitem\n    _siftdown(heap, startpos, pos)\n\n\ndef _siftdown_max(heap,\
    \ startpos, pos):\n    \"Maxheap variant of _siftdown\"\n    newitem = heap[pos]\n\
    \    # Follow the path to the root, moving parents down until finding a place\n\
    \    # newitem fits.\n    while pos > startpos:\n        parentpos = (pos - 1)\
    \ >> 1\n        parent = heap[parentpos]\n        if parent < newitem:\n     \
    \       heap[pos] = parent\n            pos = parentpos\n            continue\n\
    \        break\n    heap[pos] = newitem\n\n\ndef _siftup_max(heap, pos):\n   \
    \ \"Maxheap variant of _siftup\"\n    endpos = len(heap)\n    startpos = pos\n\
    \    newitem = heap[pos]\n    # Bubble up the larger child until hitting a leaf.\n\
    \    childpos = 2 * pos + 1  # leftmost child position\n    while childpos < endpos:\n\
    \        # Set childpos to index of larger child.\n        rightpos = childpos\
    \ + 1\n        if rightpos < endpos and not heap[rightpos] < heap[childpos]:\n\
    \            childpos = rightpos\n        # Move the larger child up.\n      \
    \  heap[pos] = heap[childpos]\n        pos = childpos\n        childpos = 2 *\
    \ pos + 1\n    # The leaf at pos is empty now.  Put newitem there, and bubble\
    \ it up\n    # to its final resting place (by sifting its parents down).\n   \
    \ heap[pos] = newitem\n    _siftdown_max(heap, startpos, pos)\n\n\ndef merge(*iterables,\
    \ key=None, reverse=False):\n    \"\"\"Merge multiple sorted inputs into a single\
    \ sorted output.\n\n    Similar to sorted(itertools.chain(*iterables)) but returns\
    \ a generator,\n    does not pull the data into memory all at once, and assumes\
    \ that each of\n    the input streams is already sorted (smallest to largest).\n\
    \n    >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))\n    [0, 1,\
    \ 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]\n\n    If *key* is not None, applies a\
    \ key function to each element to determine\n    its sort order.\n\n    >>> list(merge(['dog',\
    \ 'horse'], ['cat', 'fish', 'kangaroo'], key=len))\n    ['dog', 'cat', 'fish',\
    \ 'horse', 'kangaroo']\n\n    \"\"\"\n\n    h = []\n    h_append = h.append\n\n\
    \    if reverse:\n        _heapify = _heapify_max\n        _heappop = _heappop_max\n\
    \        _heapreplace = _heapreplace_max\n        direction = -1\n    else:\n\
    \        _heapify = heapify\n        _heappop = heappop\n        _heapreplace\
    \ = heapreplace\n        direction = 1\n\n    if key is None:\n        for order,\
    \ it in enumerate(map(iter, iterables)):\n            try:\n                next\
    \ = it.__next__\n                h_append([next(), order * direction, next])\n\
    \            except StopIteration:\n                pass\n        _heapify(h)\n\
    \        while len(h) > 1:\n            try:\n                while True:\n  \
    \                  value, order, next = s = h[0]\n                    yield value\n\
    \                    s[0] = next()  # raises StopIteration when exhausted\n  \
    \                  _heapreplace(h, s)  # restore heap condition\n            except\
    \ StopIteration:\n                _heappop(h)  # remove empty iterator\n     \
    \   if h:\n            # fast case when only a single iterator remains\n     \
    \       value, order, next = h[0]\n            yield value\n            yield\
    \ from next.__self__\n        return\n\n    for order, it in enumerate(map(iter,\
    \ iterables)):\n        try:\n            next = it.__next__\n            value\
    \ = next()\n            h_append([key(value), order * direction, value, next])\n\
    \        except StopIteration:\n            pass\n    _heapify(h)\n    while len(h)\
    \ > 1:\n        try:\n            while True:\n                key_value, order,\
    \ value, next = s = h[0]\n                yield value\n                value =\
    \ next()\n                s[0] = key(value)\n                s[2] = value\n  \
    \              _heapreplace(h, s)\n        except StopIteration:\n           \
    \ _heappop(h)\n    if h:\n        key_value, order, value, next = h[0]\n     \
    \   yield value\n        yield from next.__self__\n\n\n# Algorithm notes for nlargest()\
    \ and nsmallest()\n# ==============================================\n#\n# Make\
    \ a single pass over the data while keeping the k most extreme values\n# in a\
    \ heap.  Memory consumption is limited to keeping k values in a list.\n#\n# Measured\
    \ performance for random inputs:\n#\n#                                   number\
    \ of comparisons\n#    n inputs     k-extreme values  (average of 5 trials)  \
    \ % more than min()\n# -------------   ----------------  ---------------------\
    \   -----------------\n#      1,000           100                  3,317     \
    \          231.7%\n#     10,000           100                 14,046         \
    \       40.5%\n#    100,000           100                105,749             \
    \    5.7%\n#  1,000,000           100              1,007,751                 0.8%\n\
    # 10,000,000           100             10,009,401                 0.1%\n#\n# Theoretical\
    \ number of comparisons for k smallest of n random inputs:\n#\n# Step   Comparisons\
    \                  Action\n# ----   --------------------------   ---------------------------\n\
    #  1     1.66 * k                     heapify the first k-inputs\n#  2     n -\
    \ k                        compare remaining elements to top of heap\n#  3   \
    \  k * (1 + lg2(k)) * ln(n/k)   replace the topmost value on the heap\n#  4  \
    \   k * lg2(k) - (k/2)           final sort of the k most extreme values\n#\n\
    # Combining and simplifying for a rough estimate gives:\n#\n#        comparisons\
    \ = n + k * (log(k, 2) * log(n/k) + log(k, 2) + log(n/k))\n#\n# Computing the\
    \ number of comparisons for step 3:\n# -----------------------------------------------\n\
    # * For the i-th new value from the iterable, the probability of being in the\n\
    #   k most extreme values is k/i.  For example, the probability of the 101st\n\
    #   value seen being in the 100 most extreme values is 100/101.\n# * If the value\
    \ is a new extreme value, the cost of inserting it into the\n#   heap is 1 + log(k,\
    \ 2).\n# * The probability times the cost gives:\n#            (k/i) * (1 + log(k,\
    \ 2))\n# * Summing across the remaining n-k elements gives:\n#            sum((k/i)\
    \ * (1 + log(k, 2)) for i in range(k+1, n+1))\n# * This reduces to:\n#       \
    \     (H(n) - H(k)) * k * (1 + log(k, 2))\n# * Where H(n) is the n-th harmonic\
    \ number estimated by:\n#            gamma = 0.5772156649\n#            H(n) =\
    \ log(n, e) + gamma + 1 / (2 * n)\n#   http://en.wikipedia.org/wiki/Harmonic_series_(mathematics)#Rate_of_divergence\n\
    # * Substituting the H(n) formula:\n#            comparisons = k * (1 + log(k,\
    \ 2)) * (log(n/k, e) + (1/n - 1/k) / 2)\n#\n# Worst-case for step 3:\n# ----------------------\n\
    # In the worst case, the input data is reversed sorted so that every new element\n\
    # must be inserted in the heap:\n#\n#             comparisons = 1.66 * k + log(k,\
    \ 2) * (n - k)\n#\n# Alternative Algorithms\n# ----------------------\n# Other\
    \ algorithms were not used because they:\n# 1) Took much more auxiliary memory,\n\
    # 2) Made multiple passes over the data.\n# 3) Made more comparisons in common\
    \ cases (small k, large n, semi-random input).\n# See the more detailed comparison\
    \ of approach at:\n# http://code.activestate.com/recipes/577573-compare-algorithms-for-heapqsmallest\n\
    \n\ndef nsmallest(n, iterable, key=None):\n    \"\"\"Find the n smallest elements\
    \ in a dataset.\n\n    Equivalent to:  sorted(iterable, key=key)[:n]\n    \"\"\
    \"\n\n    # Short-cut for n==1 is to use min()\n    if n == 1:\n        it = iter(iterable)\n\
    \        sentinel = object()\n        result = min(it, default=sentinel, key=key)\n\
    \        return [] if result is sentinel else [result]\n\n    # When n>=size,\
    \ it's faster to use sorted()\n    try:\n        size = len(iterable)\n    except\
    \ (TypeError, AttributeError):\n        pass\n    else:\n        if n >= size:\n\
    \            return sorted(iterable, key=key)[:n]\n\n    # When key is none, use\
    \ simpler decoration\n    if key is None:\n        it = iter(iterable)\n     \
    \   # put the range(n) first so that zip() doesn't\n        # consume one too\
    \ many elements from the iterator\n        result = [(elem, i) for i, elem in\
    \ zip(range(n), it)]\n        if not result:\n            return result\n    \
    \    _heapify_max(result)\n        top = result[0][0]\n        order = n\n   \
    \     _heapreplace = _heapreplace_max\n        for elem in it:\n            if\
    \ elem < top:\n                _heapreplace(result, (elem, order))\n         \
    \       top, _order = result[0]\n                order += 1\n        result.sort()\n\
    \        return [elem for (elem, order) in result]\n\n    # General case, slowest\
    \ method\n    it = iter(iterable)\n    result = [(key(elem), i, elem) for i, elem\
    \ in zip(range(n), it)]\n    if not result:\n        return result\n    _heapify_max(result)\n\
    \    top = result[0][0]\n    order = n\n    _heapreplace = _heapreplace_max\n\
    \    for elem in it:\n        k = key(elem)\n        if k < top:\n           \
    \ _heapreplace(result, (k, order, elem))\n            top, _order, _elem = result[0]\n\
    \            order += 1\n    result.sort()\n    return [elem for (k, order, elem)\
    \ in result]\n\n\ndef nlargest(n, iterable, key=None):\n    \"\"\"Find the n largest\
    \ elements in a dataset.\n\n    Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]\n\
    \    \"\"\"\n\n    # Short-cut for n==1 is to use max()\n    if n == 1:\n    \
    \    it = iter(iterable)\n        sentinel = object()\n        result = max(it,\
    \ default=sentinel, key=key)\n        return [] if result is sentinel else [result]\n\
    \n    # When n>=size, it's faster to use sorted()\n    try:\n        size = len(iterable)\n\
    \    except (TypeError, AttributeError):\n        pass\n    else:\n        if\
    \ n >= size:\n            return sorted(iterable, key=key, reverse=True)[:n]\n\
    \n    # When key is none, use simpler decoration\n    if key is None:\n      \
    \  it = iter(iterable)\n        result = [(elem, i) for i, elem in zip(range(0,\
    \ -n, -1), it)]\n        if not result:\n            return result\n        heapify(result)\n\
    \        top = result[0][0]\n        order = -n\n        _heapreplace = heapreplace\n\
    \        for elem in it:\n            if top < elem:\n                _heapreplace(result,\
    \ (elem, order))\n                top, _order = result[0]\n                order\
    \ -= 1\n        result.sort(reverse=True)\n        return [elem for (elem, order)\
    \ in result]\n\n    # General case, slowest method\n    it = iter(iterable)\n\
    \    result = [(key(elem), i, elem) for i, elem in zip(range(0, -n, -1), it)]\n\
    \    if not result:\n        return result\n    heapify(result)\n    top = result[0][0]\n\
    \    order = -n\n    _heapreplace = heapreplace\n    for elem in it:\n       \
    \ k = key(elem)\n        if top < k:\n            _heapreplace(result, (k, order,\
    \ elem))\n            top, _order, _elem = result[0]\n            order -= 1\n\
    \    result.sort(reverse=True)\n    return [elem for (k, order, elem) in result]\n\
    \n\n# If available, use C implementation\ntry:\n    from _heapq import *\nexcept\
    \ ImportError:\n    pass\ntry:\n    from _heapq import _heapreplace_max\nexcept\
    \ ImportError:\n    pass\ntry:\n    from _heapq import _heapify_max\nexcept ImportError:\n\
    \    pass\ntry:\n    from _heapq import _heappop_max\nexcept ImportError:\n  \
    \  pass\n\n\nif __name__ == \"__main__\":\n    import doctest  # pragma: no cover\n\
    \n    print(doctest.testmod())  # pragma: no cover\n"
  dependsOn: []
  isVerificationFile: false
  path: heapq.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heapq.py
layout: document
redirect_from:
- /library/heapq.py
- /library/heapq.py.html
title: heapq.py
---
