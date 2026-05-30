"""Generate test datasets for benchmarking and testing."""
import random, json, os


def random_array(n: int, max_val: int = None) -> list:
    """Generate random integer array of size n."""
    if max_val is None: max_val = n * 10
    return [random.randint(0, max_val) for _ in range(n)]

def random_unique(n: int) -> list:
    """Generate array of n unique random integers."""
    return random.sample(range(n * 2), n)

def nearly_sorted(n: int, swaps: int = 10) -> list:
    """Nearly sorted array with `swaps` random swaps."""
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.randrange(n), random.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def reversed_array(n: int) -> list:
    """Reverse sorted array."""
    return list(range(n, 0, -1))

def random_graph(n: int, edge_prob: float = 0.3, weighted: bool = False) -> dict:
    """Generate random adjacency list graph."""
    g = {}
    for i in range(n):
        nbs = [j for j in range(n) if j != i and random.random() < edge_prob]
        g[i] = [(nb, random.randint(1,10)) for nb in nbs] if weighted else nbs
    return g

def generate_all(output_dir: str = "datasets") -> None:
    """Generate and save common test datasets."""
    os.makedirs(output_dir, exist_ok=True)
    data = {
        "random_100":    random_array(100),
        "random_1000":   random_array(1000),
        "random_10000":  random_array(10000),
        "unique_100":    random_unique(100),
        "sorted_100":    list(range(100)),
        "reversed_100":  reversed_array(100),
        "nearly_sorted": nearly_sorted(100, swaps=5),
        "duplicates":    [random.randint(0, 10) for _ in range(100)],
    }
    with open(f"{output_dir}/test_arrays.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {len(data)} datasets → {output_dir}/test_arrays.json")


if __name__ == "__main__":
    generate_all()
