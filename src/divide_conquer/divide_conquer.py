"""
Module: divide_conquer.py  Topic: Divide & Conquer
Merge Sort, Quick Sort, Binary Search, Maximum Subarray,
Closest Pair of Points, Matrix Multiplication (Strassen sketch).
"""
from typing import List, Tuple
import math


def max_subarray_dc(nums: List[int]) -> int:
    """Max subarray sum via Divide & Conquer. O(n logn).
    >>> max_subarray_dc([-2,1,-3,4,-1,2,1,-5,4])
    6
    """
    def cross(arr: List[int], l: int, m: int, r: int) -> int:
        left_sum = right_sum = float("-inf")
        total = 0
        for i in range(m, l-1, -1):
            total += arr[i]; left_sum = max(left_sum, total)
        total = 0
        for i in range(m+1, r+1):
            total += arr[i]; right_sum = max(right_sum, total)
        return left_sum + right_sum

    def solve(arr: List[int], l: int, r: int) -> int:
        if l == r: return arr[l]
        m = (l+r)//2
        return max(solve(arr, l, m), solve(arr, m+1, r), cross(arr, l, m, r))

    return solve(nums, 0, len(nums)-1)


def closest_pair(points: List[Tuple[float,float]]) -> float:
    """Closest pair of points. O(n logn).
    >>> import math; pts=[(0,0),(3,4),(1,1)]; closest_pair(pts) < 2
    True
    """
    def dist(p1: Tuple, p2: Tuple) -> float:
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def brute(pts: List) -> float:
        mn = float("inf")
        for i in range(len(pts)):
            for j in range(i+1, len(pts)):
                mn = min(mn, dist(pts[i], pts[j]))
        return mn

    def strip_closest(strip: List, d: float) -> float:
        strip.sort(key=lambda p: p[1]); mn = d
        for i in range(len(strip)):
            j = i+1
            while j < len(strip) and (strip[j][1]-strip[i][1]) < mn:
                mn = min(mn, dist(strip[i], strip[j])); j += 1
        return mn

    def rec(pts: List) -> float:
        n = len(pts)
        if n <= 3: return brute(pts)
        mid = n//2; mx = pts[mid][0]
        dl = rec(pts[:mid]); dr = rec(pts[mid:])
        d = min(dl, dr)
        strip = [p for p in pts if abs(p[0]-mx) < d]
        return min(d, strip_closest(strip, d))

    pts = sorted(points)
    return rec(pts)


def power_fast(base: float, exp: int) -> float:
    """Fast exponentiation D&C. O(logn).
    >>> power_fast(2, 10)
    1024.0
    """
    if exp == 0: return 1.0
    if exp % 2 == 0:
        half = power_fast(base, exp//2); return half * half
    return base * power_fast(base, exp-1)


def count_inversions(arr: List[int]) -> Tuple[List[int], int]:
    """Count inversions using modified merge sort. O(n logn).
    >>> _, count = count_inversions([3,1,2]); count
    2
    """
    if len(arr) <= 1: return arr, 0
    mid = len(arr)//2
    left, lc = count_inversions(arr[:mid])
    right, rc = count_inversions(arr[mid:])
    merged: List[int] = []; inv = lc + rc; i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: merged.append(left[i]); i += 1
        else: merged.append(right[j]); inv += len(left)-i; j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged, inv


def find_kth_smallest(nums: List[int], k: int) -> int:
    """QuickSelect — kth smallest. O(n) avg, O(n²) worst.
    >>> find_kth_smallest([7,2,1,6,5,3,4,8], 3)
    3
    """
    def partition(arr: List[int], l: int, r: int) -> int:
        pivot = arr[r]; i = l-1
        for j in range(l, r):
            if arr[j] <= pivot: i += 1; arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[r]=arr[r],arr[i+1]; return i+1

    def quickselect(arr: List[int], l: int, r: int, k: int) -> int:
        if l == r: return arr[l]
        pi = partition(arr, l, r)
        if pi == k: return arr[pi]
        elif pi < k: return quickselect(arr, pi+1, r, k)
        else: return quickselect(arr, l, pi-1, k)

    return quickselect(nums.copy(), 0, len(nums)-1, k-1)


if __name__ == "__main__":
    print("Max Subarray D&C:", max_subarray_dc([-2,1,-3,4,-1,2,1,-5,4]))
    print("Closest pair:", closest_pair([(0,0),(3,4),(1,1),(2,2)]))
    print("2^10:", power_fast(2,10))
    _, inv = count_inversions([3,1,2]); print("Inversions [3,1,2]:", inv)
    print("Kth smallest (k=3):", find_kth_smallest([7,2,1,6,5,3,4,8], 3))
