"""
Module: heap.py  Topic: Heaps & Priority Queues
MinHeap (from scratch), MaxHeap, MedianFinder, K-largest, Merge K Sorted.
"""
from typing import List, Optional, Tuple
import heapq


class MinHeap:
    """Min-Heap from scratch. push/pop O(logn), peek O(1).
    >>> h = MinHeap(); [h.push(v) for v in [5,3,8,1]]; h.pop()
    1
    """
    def __init__(self) -> None: self._d: List[int] = []
    def __len__(self) -> int: return len(self._d)
    @property
    def peek(self) -> Optional[int]: return self._d[0] if self._d else None

    def push(self, v: int) -> None:
        self._d.append(v)
        i = len(self._d) - 1
        while i > 0:
            p = (i-1)//2
            if self._d[i] < self._d[p]: self._d[i],self._d[p] = self._d[p],self._d[i]; i=p
            else: break

    def pop(self) -> int:
        if not self._d: raise IndexError("empty heap")
        self._d[0], self._d[-1] = self._d[-1], self._d[0]
        v = self._d.pop(); i = 0; n = len(self._d)
        while True:
            s = i; l, r = 2*i+1, 2*i+2
            if l < n and self._d[l] < self._d[s]: s = l
            if r < n and self._d[r] < self._d[s]: s = r
            if s == i: break
            self._d[i],self._d[s] = self._d[s],self._d[i]; i = s
        return v

    @classmethod
    def heapify(cls, arr: List[int]) -> "MinHeap":
        """Build heap from array in O(n)."""
        h = cls(); h._d = arr.copy()
        for i in range(len(h._d)//2 - 1, -1, -1):
            j = i; n = len(h._d)
            while True:
                s = j; l, r = 2*j+1, 2*j+2
                if l < n and h._d[l] < h._d[s]: s = l
                if r < n and h._d[r] < h._d[s]: s = r
                if s == j: break
                h._d[j],h._d[s] = h._d[s],h._d[j]; j = s
        return h


class MaxHeap:
    """Max-Heap via negation of heapq."""
    def __init__(self) -> None: self._d: List[int] = []
    def push(self, v: int) -> None: heapq.heappush(self._d, -v)
    def pop(self) -> int: return -heapq.heappop(self._d)
    @property
    def peek(self) -> Optional[int]: return -self._d[0] if self._d else None
    def __len__(self) -> int: return len(self._d)


def kth_largest(nums: List[int], k: int) -> int:
    """Kth largest using min-heap of size k. O(n logk).
    >>> kth_largest([3,2,1,5,6,4], 2)
    5
    """
    h: List[int] = []
    for n in nums:
        heapq.heappush(h, n)
        if len(h) > k: heapq.heappop(h)
    return h[0]


def kth_smallest(nums: List[int], k: int) -> int:
    """Kth smallest using max-heap of size k. O(n logk)."""
    h: List[int] = []
    for n in nums:
        heapq.heappush(h, -n)
        if len(h) > k: heapq.heappop(h)
    return -h[0]


def merge_k_sorted(lists: List[List[int]]) -> List[int]:
    """Merge k sorted lists. O(N logk) time.
    >>> merge_k_sorted([[1,4,7],[2,5,8],[3,6,9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    res: List[int] = []; heap: List[Tuple] = []
    for i, lst in enumerate(lists):
        if lst: heapq.heappush(heap, (lst[0], i, 0))
    while heap:
        val, li, ei = heapq.heappop(heap); res.append(val)
        if ei + 1 < len(lists[li]): heapq.heappush(heap, (lists[li][ei+1], li, ei+1))
    return res


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Top k frequent elements using bucket sort. O(n).
    >>> top_k_frequent([1,1,1,2,2,3], 2)
    [1, 2]
    """
    from collections import Counter
    count = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums)+1)]
    for n, f in count.items(): buckets[f].append(n)
    res: List[int] = []
    for i in range(len(buckets)-1, -1, -1):
        res.extend(buckets[i])
        if len(res) >= k: break
    return res[:k]


class MedianFinder:
    """Running median via two heaps. add O(logn), find O(1).
    >>> mf=MedianFinder(); mf.add_num(1); mf.add_num(2); mf.find_median()
    1.5
    """
    def __init__(self) -> None:
        self.lo: List[int] = []   # max-heap (negated)
        self.hi: List[int] = []   # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        if self.hi and -self.lo[0] > self.hi[0]:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) > len(self.hi) + 1:
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self) -> float:
        if len(self.lo) > len(self.hi): return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0


def task_scheduler(tasks: List[str], n: int) -> int:
    """Min intervals to execute all tasks with cooldown n.
    >>> task_scheduler(["A","A","A","B","B","B"], 2)
    8
    """
    from collections import Counter
    freq = list(Counter(tasks).values())
    max_freq = max(freq)
    max_count = freq.count(max_freq)
    return max(len(tasks), (max_freq-1)*(n+1) + max_count)


if __name__ == "__main__":
    h = MinHeap()
    for v in [5,3,8,1,9,2]: h.push(v)
    print("MinHeap pops:", [h.pop() for _ in range(len(h))])
    mh = MaxHeap()
    for v in [5,3,8,1,9,2]: mh.push(v)
    print("MaxHeap pops:", [mh.pop() for _ in range(len(mh))])
    print("Kth largest(2):", kth_largest([3,2,1,5,6,4],2))
    print("Merge k sorted:", merge_k_sorted([[1,4,7],[2,5,8],[3,6,9]]))
    print("Top 2 frequent:", top_k_frequent([1,1,1,2,2,3],2))
    mf = MedianFinder()
    for x in [1,2,3,4,5]: mf.add_num(x); print(f"  After {x}: median={mf.find_median()}")
    print("Task scheduler:", task_scheduler(["A","A","A","B","B","B"],2))
