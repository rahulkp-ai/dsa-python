"""Stress tests with large inputs."""
import pytest, random, time
from src.sorting.sorting_algorithms import merge_sort, quick_sort, heap_sort
from src.searching.binary_search import binary_search, min_eating_speed
from src.graphs.graph_algorithms import bfs, dijkstra
from src.dynamic_programming.dp_algorithms import lis, coin_change


@pytest.mark.timeout(10)
def test_sort_10k():
    nums = random.sample(range(100000), 10000)
    assert merge_sort(nums) == sorted(nums)

@pytest.mark.timeout(10)
def test_quicksort_10k():
    nums = random.sample(range(100000), 10000)
    assert quick_sort(nums) == sorted(nums)

@pytest.mark.timeout(10)
def test_heapsort_10k():
    nums = random.sample(range(100000), 10000)
    assert heap_sort(nums) == sorted(nums)

@pytest.mark.timeout(5)
def test_binary_search_large():
    nums = list(range(100000))
    for target in random.sample(nums, 100):
        assert binary_search(nums, target) == target

@pytest.mark.timeout(5)
def test_bfs_large_graph():
    n = 1000
    g = {i: [(i+1)%n, (i+2)%n] for i in range(n)}
    result = bfs(g, 0)
    assert len(result) == n

@pytest.mark.timeout(5)
def test_dijkstra_dense():
    n = 200
    g = {i:[(j, abs(i-j)) for j in range(max(0,i-5),min(n,i+5)) if j!=i] for i in range(n)}
    d = dijkstra(g, 0)
    assert d[0]==0 and all(v>=0 for v in d.values())

@pytest.mark.timeout(5)
def test_lis_large():
    nums = random.sample(range(10000), 1000)
    result = lis(nums)
    assert 1 <= result <= 1000

@pytest.mark.timeout(5)
def test_coin_change_large():
    result = coin_change([1,5,10,25], 10000)
    assert result == 400  # 400 * 25

@pytest.mark.timeout(5)
def test_koko_large():
    piles = [random.randint(1,10**9) for _ in range(1000)]
    h = len(piles)
    speed = min_eating_speed(piles, h)
    import math
    assert sum(math.ceil(p/speed) for p in piles) <= h
