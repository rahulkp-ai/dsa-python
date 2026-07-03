# Python DSA Tricks & Tips

## Essential Imports
```python
from collections import Counter, defaultdict, deque, OrderedDict
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from functools import lru_cache, reduce
from itertools import combinations, permutations, product
import bisect  # binary search on sorted lists
import math    # floor, ceil, inf, gcd, lcm (3.9+)
```

## Collections Cheatsheet

### Counter
```python
c = Counter("aabbbcc")       # {"b":3,"a":2,"c":2}
c.most_common(2)              # [("b",3),("a",2)]
c["z"]                        # 0 (no KeyError)
c1 + c2                       # merge (sum)
c1 - c2                       # subtract (remove 0/neg)
```

### defaultdict
```python
d = defaultdict(list)         # d["x"].append(1) — no KeyError
d = defaultdict(int)          # d["x"] += 1
d = defaultdict(set)
d = defaultdict(lambda: float("inf"))
```

### deque (O(1) both ends)
```python
q = deque([1,2,3])
q.appendleft(0)               # [0,1,2,3]
q.popleft()                   # O(1) — use for BFS!
q.rotate(2)                   # [2,3,0,1]
```

### OrderedDict (for LRU Cache)
```python
od = OrderedDict()
od.move_to_end(key)           # move to right (recently used)
od.popitem(last=False)        # remove leftmost (LRU)
```

## Heap (heapq) — Min-Heap by Default
```python
h = [3,1,4,1,5]; heapify(h)  # O(n) min-heap in-place
heappush(h, 2)                # O(log n)
heappop(h)                    # O(log n) — returns minimum

# Max-heap trick
heappush(h, -val)
-heappop(h)

# K operations
nlargest(k, nums)             # O(n log k)
nsmallest(k, nums)            # O(n log k)
```

## bisect — Binary Search
```python
a = [1,3,5,7,9]
bisect.bisect_left(a, 5)      # 2 (first pos where 5 fits)
bisect.bisect_right(a, 5)     # 3 (after 5)
bisect.insort_left(a, 6)      # insert maintaining order
```

## Sorting Tricks
```python
arr.sort(key=lambda x: (x[0], -x[1]))  # multi-key
sorted(d, key=d.get, reverse=True)     # sort by dict value
arr.sort(key=abs)                        # by absolute value
```

## String Operations
```python
s[::-1]                       # reverse
"".join(reversed(s))          # also reverse
s.split()                     # split on whitespace
",".join(words)               # join with delimiter
s.count("sub")                # count occurrences
s.replace("a","b")            # replace all
ord("a")                      # 97, chr(97) = "a"
s.lower(), s.upper()
s.isalnum(), s.isdigit(), s.isalpha()
s.strip(), s.lstrip(), s.rstrip()
```

## List Comprehensions
```python
# Flatten 2D
[x for row in matrix for x in row]

# Filter
[x for x in nums if x > 0]

# Nested
[[i*j for j in range(5)] for i in range(5)]

# Generator (memory efficient)
sum(x**2 for x in range(1000))
```

## Common Patterns

### Two Pointers
```python
l, r = 0, len(arr)-1
while l < r:
    if condition: return True
    elif need_bigger: l += 1
    else: r -= 1
```

### Sliding Window
```python
l = 0
for r in range(len(arr)):
    # add arr[r] to window
    while window_invalid:
        # remove arr[l]; l += 1
    result = max(result, r-l+1)
```

### Prefix Sum with HashMap
```python
seen = {0: 1}; total = 0; count = 0
for n in nums:
    total += n
    count += seen.get(total - k, 0)
    seen[total] = seen.get(total, 0) + 1
```

### BFS Template
```python
from collections import deque
q = deque([start]); visited = {start}
while q:
    node = q.popleft()
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb); q.append(nb)
```

### DFS Recursive
```python
def dfs(node, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs(nb, visited)
```

### Backtracking Template
```python
def backtrack(start, current):
    if len(current) == k:
        result.append(current[:])
        return
    for i in range(start, n):
        current.append(nums[i])
        backtrack(i + 1, current)
        current.pop()
```

### Memoization
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i, j):
    if base_case: return value
    return f(dp(i-1, j), dp(i, j-1))
```

## Type Hints (always use in interviews)
```python
from typing import List, Dict, Set, Tuple, Optional, Any

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    ...

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    ...

class Node:
    def __init__(self, val: int, next: Optional["Node"] = None):
        ...
```

## Math Shortcuts
```python
float("inf"); float("-inf")    # infinity
n ** 0.5                       # square root
n ** (1/3)                     # cube root
math.floor(n); math.ceil(n)
abs(x); divmod(10, 3)          # (3, 1)
math.gcd(a, b)                 # Python 3.9+
math.lcm(a, b)                 # Python 3.9+
bin(n); hex(n); oct(n)         # string representations
n & (n-1) == 0                 # check power of 2
n & 1                          # check odd
n >> 1                         # divide by 2
```

## Interview Quick Reference
```python
# Check sorted
all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

# Swap without temp
a, b = b, a

# Multiple assignment
x = y = z = 0

# Walrus operator (Python 3.8+)
while (n := len(a)) > 1:
    ...

# Enumerate with start
for i, v in enumerate(arr, start=1):
    ...

# Zip and unzip
pairs = list(zip(keys, values))
keys, values = zip(*pairs)
```
