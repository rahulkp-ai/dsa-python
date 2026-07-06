"""Benchmark: Sorting Algorithms — timing comparison with CSV export."""
import time, random, csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.sorting.sorting_algorithms import (
    bubble_sort, insertion_sort, selection_sort,
    merge_sort, quick_sort, heap_sort, counting_sort, radix_sort
)

ALGORITHMS = {
    "Bubble Sort":    bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort":     merge_sort,
    "Quick Sort":     quick_sort,
    "Heap Sort":      heap_sort,
}
SIZES = [100, 500, 1000, 2000, 5000]
RUNS  = 3

def benchmark(sizes=None, runs=RUNS):
    if sizes is None: sizes = SIZES
    results = []
    header = f"{'Algorithm':<20}" + "".join(f"  n={s:<7}" for s in sizes)
    print(header); print("-" * len(header))
    for name, algo in ALGORITHMS.items():
        row = {"algorithm": name}
        line = f"{name:<20}"
        for size in sizes:
            times = []
            for _ in range(runs):
                arr = random.sample(range(size * 10), size)
                t0 = time.perf_counter(); algo(arr); times.append(time.perf_counter() - t0)
            avg = sum(times) / len(times) * 1000
            line += f"  {avg:>6.2f}ms"; row[f"n={size}"] = f"{avg:.3f}"
        print(line); results.append(row)
    os.makedirs("benchmarks/results", exist_ok=True)
    csvpath = "benchmarks/results/sorting_benchmark.csv"
    with open(csvpath, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["algorithm"] + [f"n={s}" for s in sizes])
        w.writeheader(); w.writerows(results)
    print(f"\nSaved → {csvpath}")
    return results

if __name__ == "__main__":
    print("=== Sorting Benchmark ===\n"); benchmark()
