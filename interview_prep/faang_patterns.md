# FAANG Interview Patterns

## The 14 Core Patterns

### 1. Sliding Window
**Use when:** Contiguous subarray/substring problems with a constraint.
```python
left = 0
for right in range(len(arr)):
    # expand: add arr[right] to window
    while window_invalid:
        # shrink: remove arr[left]; left += 1
    result = max(result, right - left + 1)
```
**Problems:** Longest substring no repeat, Min window substring, Max sum subarray K

---
### 2. Two Pointers (Opposite Ends)
**Use when:** Sorted array, pair sum, palindrome.
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition: return [left, right]
    elif too_small: left += 1
    else: right -= 1
```
**Problems:** Two Sum II, 3Sum, Container with Most Water, Trapping Rain Water

---
### 3. Fast & Slow Pointers
**Use when:** Cycle detection, middle of linked list, happy number.
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast: return True  # cycle
```

---
### 4. Binary Search on Answer
**Use when:** "Minimum X such that condition Y holds" — monotonic feasibility.
```python
left, right = min_possible, max_possible
while left < right:
    mid = (left + right) // 2
    if feasible(mid): right = mid   # try smaller
    else: left = mid + 1            # need larger
return left
```
**Problems:** Koko Bananas, Ship Packages, Min Days to Make Bouquets

---
### 5. BFS (Shortest Path / Level Order)
**Use when:** Shortest path in unweighted graph, level-by-level processing.
```python
from collections import deque
queue = deque([start]); visited = {start}
while queue:
    node = queue.popleft()          # process node
    for nb in graph[node]:
        if nb not in visited:
            visited.add(nb); queue.append(nb)
```

---
### 6. DFS + Backtracking
**Use when:** All permutations/combinations/subsets, constraint satisfaction.
```python
def backtrack(start, current):
    if base_case:
        result.append(current[:])
        return
    for i in range(start, n):
        if pruning_condition: continue
        current.append(choice[i])
        backtrack(i + 1, current)   # or i for reuse
        current.pop()               # undo
```

---
### 7. Dynamic Programming
**Decision tree:**
1. Define subproblem → dp[i] or dp[i][j]
2. Write recurrence relation
3. Identify base case
4. Build bottom-up (tabulation) or top-down (memoization)

**1D Pattern:**
```python
dp = [0] * (n + 1)
dp[0] = base
for i in range(1, n+1):
    dp[i] = f(dp[i-1], dp[i-2], ...)
```

**2D Pattern:**
```python
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
```

---
### 8. Monotonic Stack
**Use when:** Next greater/smaller element, largest rectangle.
```python
stack = []
for i in range(len(arr) - 1, -1, -1):  # right to left for NGE
    while stack and stack[-1] <= arr[i]: stack.pop()
    result[i] = stack[-1] if stack else -1
    stack.append(arr[i])
```

---
### 9. Top-K Elements (Heap)
**Use when:** Kth largest/smallest, top-K frequent.
```python
import heapq
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k: heapq.heappop(heap)
return heap[0]  # kth largest
```

---
### 10. Union-Find
**Use when:** Connected components, cycle detection (undirected), MST.
```python
parent = list(range(n))
def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    parent[find(x)] = find(y)
```

---
### 11. Merge Intervals
```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

---
### 12. Prefix Sum
**Use when:** Range sum queries, subarray sum equals K.
```python
prefix = [0] * (n + 1)
for i in range(n): prefix[i+1] = prefix[i] + nums[i]
range_sum = prefix[r+1] - prefix[l]
# Subarray sum = K:
seen = {0: 1}
for total in running_sums:
    count += seen.get(total - k, 0)
    seen[total] = seen.get(total, 0) + 1
```

---
### 13. Trie Patterns
**Use when:** Prefix search, autocomplete, word search II.
- Insert: O(L), Search: O(L), StartsWith: O(L)
- Word Search II: build Trie from words, DFS on board

---
### 14. Graph Topological Sort
**Use when:** Task scheduling, course prerequisites, dependency resolution.
- Kahn's (BFS): Start with in-degree-0 nodes
- DFS: Post-order gives reverse topological order

---

## ⏱️ Time Complexity Decision Tree
```
Is problem solved in constant lookups?     → O(1) HashMap
Is search space halved each step?          → O(log n) Binary Search
Single pass, linear scan?                  → O(n) Two Pointers/Sliding Window
Sorting involved?                          → O(n log n)
Nested loops, all pairs?                   → O(n²)
All subsets/power set?                     → O(2^n)
All permutations?                          → O(n!)
Graph traversal?                           → O(V + E)
Shortest path (weighted)?                  → O(E log V) Dijkstra
```

## 💡 Interview Tips
1. **Always clarify**: input size, duplicates, sorted, negative numbers, empty input
2. **State approach first**: brute force → optimization
3. **Write time/space complexity** before coding
4. **Test edge cases**: empty, single element, duplicates, negatives
5. **Talk out loud**: interviewers want to hear your thinking
6. **Start simple**: correct brute force > partially correct optimal
