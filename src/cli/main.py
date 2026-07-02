"""
DSA-Python CLI — Run algorithms, benchmarks, and tests from the command line.
Usage: python -m src.cli.main --help
"""
import sys, time, random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    import typer
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

app = typer.Typer(
    help="DSA-Python CLI — Interactive algorithm runner",
    no_args_is_help=True,
) if HAS_RICH else None
console = Console() if HAS_RICH else None


def print_banner():
    if HAS_RICH:
        console.print(Panel(
            Text("🚀 DSA-Python", style="bold blue", justify="center"),
            subtitle="Data Structures & Algorithms in Python",
            border_style="blue"
        ))
    else:
        print("=== DSA-Python CLI ===")


def run_sort_demo():
    from src.sorting.sorting_algorithms import (
        bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort
    )
    arr = random.sample(range(100), 15)
    algos = {
        "Bubble Sort": bubble_sort, "Insertion Sort": insertion_sort,
        "Merge Sort":  merge_sort,  "Quick Sort":     quick_sort,
        "Heap Sort":   heap_sort,
    }
    if HAS_RICH:
        table = Table(title=f"Sorting Demo — Input: {arr}", show_header=True)
        table.add_column("Algorithm", style="cyan", width=20)
        table.add_column("Result", style="green")
        table.add_column("Time (ms)", justify="right", style="yellow")
        for name, fn in algos.items():
            t0 = time.perf_counter(); r = fn(arr); elapsed = (time.perf_counter()-t0)*1000
            table.add_row(name, str(r), f"{elapsed:.3f}")
        console.print(table)
    else:
        for name, fn in algos.items():
            t0 = time.perf_counter(); r = fn(arr); elapsed = (time.perf_counter()-t0)*1000
            print(f"{name:<20}: {r}  [{elapsed:.3f}ms]")


def run_graph_demo():
    from src.graphs.graph_algorithms import bfs, dfs, dijkstra
    g = {0:[1,2],1:[3,4],2:[5],3:[],4:[],5:[]}
    wg = {0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]}
    if HAS_RICH:
        table = Table(title="Graph Demo", show_header=True)
        table.add_column("Algorithm", style="cyan")
        table.add_column("Result", style="green")
        table.add_row("BFS from 0", str(bfs(g, 0)))
        table.add_row("DFS from 0", str(dfs(g, 0)))
        table.add_row("Dijkstra from 0", str(dijkstra(wg, 0)))
        console.print(table)
    else:
        print("BFS:", bfs(g, 0))
        print("DFS:", dfs(g, 0))
        print("Dijkstra:", dijkstra(wg, 0))


def run_dp_demo():
    from src.dynamic_programming.dp_algorithms import (
        fibonacci, coin_change, lcs, lis, climbing_stairs
    )
    if HAS_RICH:
        table = Table(title="DP Demo", show_header=True)
        table.add_column("Problem", style="cyan")
        table.add_column("Result", style="green")
        table.add_row("Fibonacci(10)", str(fibonacci(10)))
        table.add_row("Coin Change [1,5,6,9]→11", str(coin_change([1,5,6,9],11)))
        table.add_row("LCS('ABCBDAB','BDCABA')", str(lcs("ABCBDAB","BDCABA")))
        table.add_row("LIS([10,9,2,5,3,7,101,18])", str(lis([10,9,2,5,3,7,101,18])))
        table.add_row("Climbing Stairs(5)", str(climbing_stairs(5)))
        console.print(table)
    else:
        print("Fibonacci(10):", fibonacci(10))
        print("Coin Change:", coin_change([1,5,6,9],11))
        print("LCS:", lcs("ABCBDAB","BDCABA"))
        print("LIS:", lis([10,9,2,5,3,7,101,18]))


if HAS_RICH and app:
    @app.command()
    def demo(topic: str = typer.Argument("all", help="Topic: all|sort|graph|dp|tree")):
        """Run algorithm demos."""
        print_banner()
        if topic in ("all","sort"):   run_sort_demo()
        if topic in ("all","graph"):  run_graph_demo()
        if topic in ("all","dp"):     run_dp_demo()

    @app.command()
    def benchmark(algo: str = typer.Argument("sort", help="Algorithm group: sort|graph|dp")):
        """Run benchmarks."""
        print_banner()
        if algo == "sort":
            import subprocess; subprocess.run([sys.executable,"benchmarks/sorting_benchmark.py"])
        elif algo == "graph":
            import subprocess; subprocess.run([sys.executable,"benchmarks/graph_benchmark.py"])
        elif algo == "dp":
            import subprocess; subprocess.run([sys.executable,"benchmarks/dp_benchmark.py"])

    @app.command()
    def info():
        """Show repository info and algorithm counts."""
        print_banner()
        table = Table(title="DSA-Python Stats")
        table.add_column("Category", style="cyan")
        table.add_column("Algorithms", style="green", justify="right")
        rows=[("Sorting",8),("Arrays",12),("Linked List",6),("Trees",12),
              ("Graphs",10),("Dynamic Programming",14),("Backtracking",8),
              ("Greedy",9),("Heaps",6),("Tries",4),("Binary Search",10),
              ("Bit Manipulation",12),("Two Pointers",7),("Sliding Window",7),
              ("Strings",10),("Hashing",8),("Recursion",7),("Math",12)]
        total = 0
        for name, cnt in rows: table.add_row(name, str(cnt)); total += cnt
        table.add_row("[bold]TOTAL[/bold]", f"[bold]{total}[/bold]")
        console.print(table)

if __name__ == "__main__":
    if HAS_RICH and app:
        app()
    else:
        print_banner()
        run_sort_demo()
        run_graph_demo()
        run_dp_demo()
