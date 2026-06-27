"""Integration tests combining multiple modules."""
import pytest, random
from src.sorting.sorting_algorithms import merge_sort, quick_sort
from src.searching.binary_search import binary_search, search_range
from src.trees.binary_tree import BST, inorder, height
from src.graphs.graph_algorithms import bfs, dijkstra, UnionFind
from src.dynamic_programming.dp_algorithms import coin_change, word_break
from src.heaps.heap import MedianFinder, merge_k_sorted


def test_sort_then_search():
    nums = [64,34,25,12,22,11,90]
    s = merge_sort(nums)
    assert binary_search(s,25) >= 0
    assert binary_search(s,99) == -1

def test_sort_search_range():
    nums = random.sample(range(1000),100)
    s = quick_sort(nums)
    target = s[50]
    lo, hi = search_range(s, target)
    assert lo >= 0 and hi >= lo

def test_bst_always_sorted():
    vals = random.sample(range(100), 15)
    bst = BST()
    for v in vals: bst.insert(v)
    assert bst.inorder() == sorted(vals)

def test_graph_path_and_distance():
    g = {0:[1,2],1:[3],2:[3],3:[]}
    assert 3 in set(bfs(g, 0))
    wg = {0:[(1,1),(2,4)],1:[(3,1)],2:[(3,1)],3:[]}
    d = dijkstra(wg, 0)
    assert d[3] == 2  # 0->1->3

def test_dp_correctness():
    assert coin_change([1,5,10,25],36) == 3  # 25+10+1
    assert word_break("applepenapple",["apple","pen"])

def test_heap_median_stream():
    mf = MedianFinder()
    nums = list(range(1, 11))
    for i, n in enumerate(nums):
        mf.add_num(n)
        if (i+1) % 2 == 1:
            assert mf.find_median() == (i+1+1)/2
        else:
            assert mf.find_median() == (i+1)/2 + 0.5

def test_merge_k_equals_sort():
    import heapq
    lists = [[1,4,7],[2,5,8],[3,6,9]]
    expected = sorted(x for lst in lists for x in lst)
    assert merge_k_sorted(lists) == expected

def test_union_find_mst_connectivity():
    from src.graphs.graph_algorithms import kruskal_mst
    n = 5
    edges = [(1,0,1),(2,1,2),(3,0,3),(4,2,4),(5,3,4)]
    w, mst = kruskal_mst(n, edges)
    uf = UnionFind(n)
    for _, u, v in mst: uf.union(u, v)
    assert uf.components == 1  # all connected
