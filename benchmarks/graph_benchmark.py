"""Benchmark: Graph Algorithms."""
import time, random, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.graphs.graph_algorithms import bfs, dfs, dijkstra, topological_sort

SIZES = [100, 500, 1000, 2000]

def make_graph(n, weighted=False):
    g = {}
    for i in range(n):
        nbs = random.sample([j for j in range(n) if j != i], min(5, n-1))
        g[i] = [(nb, random.randint(1, 10)) for nb in nbs] if weighted else nbs
    return g

def bench(fn, *args):
    t0 = time.perf_counter(); fn(*args); return (time.perf_counter()-t0)*1000

def benchmark():
    print("=== Graph Benchmark ===\n")
    print(f"{'n':<8}{'BFS':>10}{'DFS':>10}{'Dijkstra':>12}{'TopoSort':>12}")
    print("-"*52)
    for n in SIZES:
        g  = make_graph(n)
        wg = make_graph(n, weighted=True)
        edges = [[i,(i+1)%n] for i in range(n)]
        print(f"{n:<8}{bench(bfs,g,0):>9.2f}ms{bench(dfs,g,0):>9.2f}ms"
              f"{bench(dijkstra,wg,0):>10.2f}ms{bench(topological_sort,n,edges):>10.2f}ms")

if __name__ == "__main__":
    benchmark()
