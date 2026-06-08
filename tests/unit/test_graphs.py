"""Unit tests for graph algorithms."""
import pytest
from src.graphs.graph_algorithms import (
    bfs, bfs_shortest_path, dfs, dijkstra, bellman_ford, floyd_warshall,
    topological_sort, UnionFind, kruskal_mst, num_islands,
    course_schedule, count_components
)

# Shared test setups
@pytest.fixture
def g(): return {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}

@pytest.fixture
def wg(): return {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}

# --- BFS & DFS Traversal ---
def test_bfs_starts(g): assert bfs(g, 0)[0] == 0
def test_bfs_all(g): assert set(bfs(g, 0)) == {0, 1, 2, 3, 4, 5}
def test_dfs_starts(g): assert dfs(g, 0)[0] == 0
def test_dfs_all(g): assert set(dfs(g, 0)) == {0, 1, 2, 3, 4, 5}

# --- Shortest Paths (Unweighted & Weighted) ---
def test_bfs_path(g):
    p = bfs_shortest_path(g, 0, 5)
    assert p == [0, 2, 5]
def test_bfs_path_none(g): assert bfs_shortest_path(g, 3, 5) is None

def test_dijkstra(wg):
    d = dijkstra(wg, 0)
    assert d[0] == 0 and d[1] == 3 and d[2] == 1 and d[3] == 4

def test_bellman_ford():
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    d = bellman_ford(4, edges, 0)
    assert d is not None and d[0] == 0 and d[1] == 3 and d[2] == 1 and d[3] == 4

def test_bellman_ford_neg_cycle():
    edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
    assert bellman_ford(3, edges, 0) is None

def test_floyd_warshall():
    edges = [(0, 1, 3), (1, 2, 1), (0, 2, 5)]
    d = floyd_warshall(3, edges)
    assert d[0][0] == 0 and d[0][1] == 3 and d[0][2] == 4

# --- Topological Sort & Schedule ---
def test_topo_dag():
    r = topological_sort(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
    assert r is not None
    pos = {v: i for i, v in enumerate(r)}
    assert pos[0] < pos[1] and pos[0] < pos[2] and pos[1] < pos[3] and pos[2] < pos[3]

def test_topo_cycle(): assert topological_sort(2, [[0, 1], [1, 0]]) is None
def test_course_schedule(): assert course_schedule(4, [[1, 0], [2, 0], [3, 1]])
def test_course_cycle(): assert not course_schedule(2, [[1, 0], [0, 1]])

# --- Union-Find & Components ---
def test_uf_connect():
    uf = UnionFind(5); uf.union(0, 1); uf.union(1, 2)
    assert uf.connected(0, 2) and not uf.connected(0, 3)

def test_uf_components():
    uf = UnionFind(4); uf.union(0, 1); uf.union(2, 3)
    assert uf.components == 2

def test_count_components(): assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2

# --- Kruskal's MST ---
def test_kruskal():
    edges = [(1, 0, 1), (2, 0, 2), (3, 1, 2)]
    w, mst = kruskal_mst(3, edges)
    assert w == 3 and len(mst) == 2

# --- Grid / Number of Islands ---
def test_islands(): assert num_islands([["1", "1", "0"], ["1", "1", "0"], ["0", "0", "1"]]) == 2
def test_islands_none(): assert num_islands([["0", "0"], ["0", "0"]]) == 0
def test_islands_all(): assert num_islands([["1", "1"], ["1", "1"]]) == 1