# Competitive Programming Guide

## Essential Algorithms for CP

### Number Theory

- Sieve of Eratosthenes — primes up to N: O(N log log N)
- Fast modular exponentiation: O(log n)
- Extended GCD, modular inverse
- Chinese Remainder Theorem
- Euler's totient function

### String Algorithms

- KMP (pattern matching): O(n+m)
- Z-algorithm: O(n)
- Rabin-Karp (rolling hash): O(n+˚m) avg
- Manacher's (all palindromes): O(n)
- Aho-Corasick (multiple patterns): O(n+m)
- Suffix Array: O(n log n)

### Graph Algorithms

- Dijkstra: O((V+E) log V)
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)
- Kruskal/Prim MST: O(E log E)
- Tarjan SCC: O(V+E)
- Bridges and Articulation Points: O(V+E)
- Bipartite Matching (Hungarian): O(VE)
- Max Flow (Dinic's): O(V² · E)

### Advanced Data Structures

- Segment Tree: O(log n) query/update
- Fenwick Tree (BIT): O(log n) query/update
- Sparse Table: O(n log n) build, O(1) RMQ
- Disjoint Set Union: O(α(n)) per op
- Persistent Data Structures

### Dynamic Programming

- Convex Hull Trick: O(n log n)
- Divide and Conquer DP: O(n log n)
- Knuth-Yao optimization: O(n²) → O(n log n)
- Bitmask DP: O(2^n · n)
- SOS DP (Sum over Subsets): O(n · 2^n)
- Digit DP

### Geometry

- Convex Hull (Graham Scan): O(n log n)
- Line intersection
- Point in polygon
- Closest pair of points: O(n log n)

## CP Templates

### Fast I/O (Python)

```python
import sys
input = sys.stdin.readline
print = sys.stdout.write
```

### Modular Arithmetic

```python
MOD = 10**9 + 7
def power(base, exp, mod=MOD):
    result = 1
    while exp > 0:
        if exp & 1: result = result * base % mod
        base = base * base % mod; exp >>= 1
    return result
def modinv(a, mod=MOD): return power(a, mod-2, mod)
```

### Union-Find

```python
parent = list(range(n)); rank = [0]*n
def find(x):
    while parent[x] != x: parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(x,y):
    x,y=find(x),find(y)
    if x==y: return False
    if rank[x]<rank[y]: x,y=y,x
    parent[y]=x
    if rank[x]==rank[y]: rank[x]+=1
    return True
```

### Segment Tree

```python
class SegTree:
    def __init__(self, n):
        self.n=n; self.tree=[0]*(4*n)
    def update(self, node, start, end, idx, val):
        if start==end: self.tree[node]=val; return
        mid=(start+end)//2
        if idx<=mid: self.update(2*node,start,mid,idx,val)
        else: self.update(2*node+1,mid+1,end,idx,val)
        self.tree[node]=self.tree[2*node]+self.tree[2*node+1]
    def query(self, node, start, end, l, r):
        if r<start or end<l: return 0
        if l<=start and end<=r: return self.tree[node]
        mid=(start+end)//2
        return self.query(2*node,start,mid,l,r)+self.query(2*node+1,mid+1,end,l,r)
```
