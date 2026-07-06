"""Benchmark: Memory usage comparison."""
import tracemalloc, random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

def measure_memory(fn, *args):
    tracemalloc.start()
    fn(*args)
    cur, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024  # KB

def benchmark():
    from src.sorting.sorting_algorithms import merge_sort, quick_sort, heap_sort
    from src.graphs.graph_algorithms import bfs, dijkstra
    n = 5000
    arr = random.sample(range(n*2), n)
    g = {i: [j for j in range(max(0,i-5),min(n,i+5)) if j!=i] for i in range(n)}
    wg = {i: [(j,1) for j in range(max(0,i-5),min(n,i+5)) if j!=i] for i in range(n)}

    print("=== Memory Benchmark (peak KB) ===\n")
    print(f"{'Algorithm':<25} {'Peak Memory':>15}")
    print("-"*42)
    tests = [
        ("Merge Sort", merge_sort, arr),
        ("Quick Sort", quick_sort, arr),
        ("Heap Sort",  heap_sort,  arr),
        ("BFS",        bfs,        g, 0),
        ("Dijkstra",   dijkstra,   wg, 0),
    ]
    for name, fn, *args in tests:
        mem = measure_memory(fn, *args)
        print(f"{name:<25} {mem:>12.2f} KB")

if __name__ == "__main__":
    benchmark()
