"""
Module: greedy_algorithms.py  Topic: Greedy Algorithms
Activity Selection, Fractional Knapsack, Jump Game I/II,
Gas Station, Assign Cookies, Merge Intervals, Min Arrows, Huffman.
"""
from typing import List, Tuple, Dict
import heapq


def activity_selection(start: List[int], finish: List[int]) -> List[int]:
    """Max non-overlapping activities (sort by finish). O(n logn).
    >>> activity_selection([1,3,0,5,8,5],[2,4,6,7,9,9])
    [0, 1, 3, 4]
    """
    acts = sorted(range(len(start)), key=lambda i: finish[i])
    sel = [acts[0]]; last = finish[acts[0]]
    for i in acts[1:]:
        if start[i] >= last: sel.append(i); last = finish[i]
    return sel


def fractional_knapsack(weights: List[float], values: List[float], cap: float) -> float:
    """Fractional Knapsack by value/weight ratio. O(n logn).
    >>> fractional_knapsack([10,20,30],[60,100,120],50)
    240.0
    """
    items = sorted(range(len(weights)), key=lambda i: values[i]/weights[i], reverse=True)
    total = 0.0; rem = cap
    for i in items:
        if rem <= 0: break
        take = min(weights[i], rem); total += take*(values[i]/weights[i]); rem -= take
    return total


def can_jump(nums: List[int]) -> bool:
    """Jump Game I — can reach last index? O(n).
    >>> can_jump([2,3,1,1,4])
    True
    """
    reach = 0
    for i, v in enumerate(nums):
        if i > reach: return False
        reach = max(reach, i+v)
    return True


def jump_game_ii(nums: List[int]) -> int:
    """Jump Game II — minimum jumps. O(n).
    >>> jump_game_ii([2,3,1,1,4])
    2
    """
    jumps = cur = far = 0
    for i in range(len(nums)-1):
        far = max(far, i+nums[i])
        if i == cur: jumps += 1; cur = far
    return jumps


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """Gas Station — find valid starting station. O(n).
    >>> can_complete_circuit([1,2,3,4,5],[3,4,5,1,2])
    3
    """
    total = tank = start = 0
    for i in range(len(gas)):
        gain = gas[i]-cost[i]; tank += gain; total += gain
        if tank < 0: start = i+1; tank = 0
    return start if total >= 0 else -1


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """Merge overlapping intervals. O(n logn).
    >>> merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    [[1, 6], [8, 10], [15, 18]]
    """
    intervals.sort(key=lambda x: x[0]); merged = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]: merged[-1][1] = max(merged[-1][1], e)
        else: merged.append([s, e])
    return merged


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """Insert and merge interval. O(n)."""
    res: List[List[int]] = []; i = 0; n = len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1]); i += 1
    res.append(new_interval)
    while i < n: res.append(intervals[i]); i += 1
    return res


def find_min_arrows(points: List[List[int]]) -> int:
    """Min arrows to burst all balloons. O(n logn).
    >>> find_min_arrows([[10,16],[2,8],[1,6],[7,12]])
    2
    """
    if not points: return 0
    points.sort(key=lambda x: x[1]); arrows = 1; shot = points[0][1]
    for s, e in points[1:]:
        if s > shot: arrows += 1; shot = e
    return arrows


def assign_cookies(g: List[int], s: List[int]) -> int:
    """Max satisfied children. O(n logn).
    >>> assign_cookies([1,2,3],[1,1])
    1
    """
    g.sort(); s.sort(); ci = si = 0
    while ci < len(g) and si < len(s):
        if s[si] >= g[ci]: ci += 1
        si += 1
    return ci


def partition_labels(s: str) -> List[int]:
    """Partition string so each letter in at most one part. O(n).
    >>> partition_labels("ababcbacadefegdehijhklij")
    [9, 7, 8]
    """
    last = {c: i for i, c in enumerate(s)}
    res: List[int] = []; start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end: res.append(end-start+1); start = i+1
    return res


class HuffmanNode:
    def __init__(self, char: str, freq: int) -> None:
        self.char = char; self.freq = freq
        self.left: "HuffmanNode|None" = None
        self.right: "HuffmanNode|None" = None
    def __lt__(self, other: "HuffmanNode") -> bool: return self.freq < other.freq


def huffman_coding(text: str) -> Dict[str, str]:
    """Build Huffman codes. O(n logn).
    >>> codes = huffman_coding("abracadabra"); len(codes) > 0
    True
    """
    from collections import Counter
    freq = Counter(text)
    heap = [HuffmanNode(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        l = heapq.heappop(heap); r = heapq.heappop(heap)
        m = HuffmanNode("", l.freq+r.freq); m.left=l; m.right=r
        heapq.heappush(heap, m)
    codes: Dict[str, str] = {}
    def build(node: HuffmanNode|None, code: str) -> None:
        if not node: return
        if node.char: codes[node.char] = code or "0"; return
        build(node.left, code+"0"); build(node.right, code+"1")
    if heap: build(heap[0], "")
    return codes


if __name__ == "__main__":
    print("Activity sel:", activity_selection([1,3,0,5,8,5],[2,4,6,7,9,9]))
    print("Frac knapsack:", fractional_knapsack([10,20,30],[60,100,120],50))
    print("Can jump:", can_jump([2,3,1,1,4]))
    print("Min jumps:", jump_game_ii([2,3,1,1,4]))
    print("Gas station:", can_complete_circuit([1,2,3,4,5],[3,4,5,1,2]))
    print("Merge intervals:", merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print("Min arrows:", find_min_arrows([[10,16],[2,8],[1,6],[7,12]]))
    print("Assign cookies:", assign_cookies([1,2,3],[1,1]))
    print("Partition labels:", partition_labels("ababcbacadefegdehijhklij"))
    print("Huffman:", huffman_coding("abracadabra"))
