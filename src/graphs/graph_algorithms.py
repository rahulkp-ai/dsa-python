"""
Module: graph_algorithms.py  Topic: Graphs
BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, Topological Sort,
Union-Find, Kruskal MST, Number of Islands, Clone Graph.
"""

import heapq
from collections import defaultdict, deque
from typing import Dict, List, Optional, Tuple


def bfs(graph: Dict, start: int) -> List[int]:
    """BFS traversal. O(V+E) time, O(V) space."""
    visited, queue, res = {start}, deque([start]), []
    while queue:
        n = queue.popleft()
        res.append(n)
        for nb in graph.get(n, []):
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    return res


def bfs_shortest_path(graph: Dict, start: int, end: int) -> Optional[List[int]]:
    """Shortest path (unweighted) via BFS. O(V+E)."""
    if start == end:
        return [start]
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for nb in graph.get(node, []):
            if nb not in visited:
                new_path = path + [nb]
                if nb == end:
                    return new_path
                visited.add(nb)
                queue.append((nb, new_path))
    return None


def dfs(graph: Dict, start: int) -> List[int]:
    """DFS iterative. O(V+E) time, O(V) space."""
    visited, stack, res = set(), [start], []
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            res.append(n)
            for nb in reversed(graph.get(n, [])):
                if nb not in visited:
                    stack.append(nb)
    return res


def dijkstra(graph: Dict, start: int) -> Dict[int, float]:
    """Dijkstra shortest path. O((V+E) logV). Non-negative weights only."""
    dist = {n: float("inf") for n in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def bellman_ford(n: int, edges: List[Tuple], start: int) -> Optional[Dict[int, float]]:
    """Bellman-Ford. O(VE). Handles negative weights, detects negative cycles."""
    dist: Dict[int, float] = {i: float("inf") for i in range(n)}
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None
    return dist


def floyd_warshall(n: int, edges: List[Tuple]) -> List[List[float]]:
    """All-pairs shortest path. O(V^3) time, O(V^2) space."""
    INF = float("inf")
    d = [[INF] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        d[u][v] = min(d[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


def topological_sort(n: int, edges: List[List[int]]) -> Optional[List[int]]:
    """Kahn's BFS topo sort. Returns None if cycle. O(V+E)."""
    indeg = [0] * n
    adj: Dict = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return res if len(res) == n else None


class UnionFind:
    """Disjoint Set Union with path compression + union by rank. ~O(1) per op."""

    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.p[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def kruskal_mst(n: int, edges: List[Tuple]) -> Tuple[int, List]:
    """Kruskal MST. O(E logE). Returns (total_weight, mst_edges)."""
    uf = UnionFind(n)
    mst: List = []
    total = 0
    for w, u, v in sorted(edges):
        if uf.union(u, v):
            mst.append((w, u, v))
            total += w
        if len(mst) == n - 1:
            break
    return total, mst


def num_islands(grid: List[List[str]]) -> int:
    """Count islands (DFS). O(M*N) time."""
    if not grid:
        return 0
    rows, cols, count = len(grid), len(grid[0]), 0

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    return count


def course_schedule(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Can finish all courses (cycle detection). O(V+E)."""
    return topological_sort(num_courses, prerequisites) is not None


def count_components(n: int, edges: List[List[int]]) -> int:
    """Count connected components. O(V+E)."""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.components


if __name__ == "__main__":
    g = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}
    print("BFS:", bfs(g, 0))
    print("DFS:", dfs(g, 0))
    print("Shortest 0->5:", bfs_shortest_path(g, 0, 5))
    wg = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    print("Dijkstra:", dijkstra(wg, 0))
    topo = topological_sort(6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]])
    print("Topo sort:", topo)
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print("0-2 connected:", uf.connected(0, 2))
    grid = [["1", "1", "0"], ["1", "1", "0"], ["0", "0", "1"]]
    print("Islands:", num_islands(grid))
