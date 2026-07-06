"""Benchmark: Dynamic Programming algorithms."""
import time, random, string, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.dynamic_programming.dp_algorithms import fibonacci, coin_change, lcs, lis, edit_distance

def bench(fn, *args):
    t0 = time.perf_counter(); fn(*args); return (time.perf_counter()-t0)*1000

def benchmark():
    print("=== DP Benchmark ===\n")
    for n in [100, 500, 1000]:
        print(f"Fibonacci(n={n}):        {bench(fibonacci,n):.3f} ms")
    for amt in [500, 1000, 2000]:
        print(f"CoinChange(amount={amt}): {bench(coin_change,[1,5,10,25],amt):.3f} ms")
    for n in [50, 100, 200]:
        s1="".join(random.choices(string.ascii_lowercase,k=n))
        s2="".join(random.choices(string.ascii_lowercase,k=n))
        print(f"LCS(n={n}):              {bench(lcs,s1,s2):.3f} ms")
    for n in [500, 1000, 5000]:
        nums=random.sample(range(n*2),n)
        print(f"LIS(n={n}):             {bench(lis,nums):.3f} ms")
    for n in [50, 100, 200]:
        w1="".join(random.choices(string.ascii_lowercase,k=n))
        w2="".join(random.choices(string.ascii_lowercase,k=n))
        print(f"EditDistance(n={n}):     {bench(edit_distance,w1,w2):.3f} ms")

if __name__ == "__main__":
    benchmark()
