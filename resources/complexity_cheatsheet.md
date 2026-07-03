# Complexity Cheat Sheet

## Data Structure Operations

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | N/A | O(1)* | O(1)* | O(1)* | O(n) |
| BST | O(log n)* | O(log n)* | O(log n)* | O(log n)* | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(n) | O(n) | O(log n) | O(log n) | O(n) |
| Trie | N/A | O(L) | O(L) | O(L) | O(n·L) |
| Segment Tree | N/A | O(log n) | O(log n) | O(log n) | O(n) |

*Average case

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ | Early exit |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ | Best for small/nearly sorted |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Min swaps |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Divide & conquer |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | In-place, cache-friendly |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | In-place, not cache-friendly |
| Counting | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ | Integers only |
| Radix | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ | k = num digits |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | Python built-in |

## Graph Algorithms

| Algorithm | Time | Space | Use Case |
|-----------|------|-------|----------|
| BFS | O(V+E) | O(V) | Shortest path (unweighted), level order |
| DFS | O(V+E) | O(V) | Cycle detection, topological sort |
| Dijkstra | O((V+E) log V) | O(V) | SSSP non-negative weights |
| Bellman-Ford | O(V·E) | O(V) | SSSP negative weights |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| Kruskal MST | O(E log E) | O(V) | Minimum spanning tree |
| Prim MST | O((V+E) log V) | O(V) | Minimum spanning tree |
| Topological Sort | O(V+E) | O(V) | DAG ordering |
| Union-Find | O(α(n)) | O(n) | Connected components |

## Dynamic Programming Patterns

| Pattern | Time | Space (optimized) | Examples |
|---------|------|-------------------|---------|
| 1D Linear | O(n) | O(1) | Fibonacci, House Robber, Climbing Stairs |
| 1D Subarray | O(n) | O(n) | Coin Change, Word Break |
| 2D Grid | O(m×n) | O(n) | Unique Paths, Edit Distance, LCS |
| Interval | O(n²) | O(n²) | Matrix Chain, Burst Balloons |
| Tree DP | O(n) | O(h) | Diameter, Max Path Sum |
| Bitmask DP | O(2^n · n) | O(2^n) | TSP, Minimum Covers |
| Digit DP | O(d · S) | O(d · S) | Count numbers with property |

## Big-O Hierarchy

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n) < O(n!)
```

## Python Built-in Complexity

| Operation | List | Dict | Set | Deque |
|-----------|------|------|-----|-------|
| Access/Get | O(1) | O(1)* | N/A | O(1) endpoints |
| Append/Add | O(1)* | O(1)* | O(1)* | O(1) |
| Insert(0) | O(n) | N/A | N/A | O(1) |
| Pop(end) | O(1) | N/A | N/A | O(1) |
| Pop(0) | O(n) | N/A | N/A | O(1) |
| Search | O(n) | O(1)* | O(1)* | O(n) |
| Sort | O(n log n) | N/A | N/A | N/A |

*Average case
