"""
Module: binary_search.py  Topic: Searching
Classic binary search, search range, rotated array, peak element,
sqrt, 2D matrix, Koko bananas, ship packages, search insert position.
All O(logn) time, O(1) space unless noted.
"""
from typing import List
import math


def binary_search(nums: List[int], target: int) -> int:
    """Classic binary search. Returns index or -1.
    >>> binary_search([-1,0,3,5,9,12], 9)
    4
    """
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target: return mid
        elif nums[mid] < target: l = mid+1
        else: r = mid-1
    return -1


def search_range(nums: List[int], target: int) -> List[int]:
    """First and last occurrence. Two binary searches.
    >>> search_range([5,7,7,8,8,10], 8)
    [3, 4]
    """
    def lo() -> int:
        l, r, res = 0, len(nums)-1, -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target: res=m; r=m-1
            elif nums[m] < target: l=m+1
            else: r=m-1
        return res
    def hi() -> int:
        l, r, res = 0, len(nums)-1, -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target: res=m; l=m+1
            elif nums[m] < target: l=m+1
            else: r=m-1
        return res
    return [lo(), hi()]


def search_rotated(nums: List[int], target: int) -> int:
    """Search in rotated sorted array (no duplicates).
    >>> search_rotated([4,5,6,7,0,1,2], 0)
    4
    """
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target: return m
        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]: r = m-1
            else: l = m+1
        else:
            if nums[m] < target <= nums[r]: l = m+1
            else: r = m-1
    return -1


def find_peak(nums: List[int]) -> int:
    """Find any peak element index.
    >>> find_peak([1,2,3,1])
    2
    """
    l, r = 0, len(nums)-1
    while l < r:
        m = (l+r)//2
        if nums[m] < nums[m+1]: l = m+1
        else: r = m
    return l


def isqrt(x: int) -> int:
    """Integer square root (floor).
    >>> isqrt(8)
    2
    """
    if x < 2: return x
    l, r = 1, x//2
    while l <= r:
        m = (l+r)//2; sq = m*m
        if sq == x: return m
        elif sq < x: l = m+1
        else: r = m-1
    return r


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """Search sorted m*n matrix (treat as 1D). O(log(m*n)).
    >>> search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
    True
    """
    if not matrix: return False
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m*n-1
    while l <= r:
        mid = (l+r)//2; v = matrix[mid//n][mid%n]
        if v == target: return True
        elif v < target: l = mid+1
        else: r = mid-1
    return False


def min_eating_speed(piles: List[int], h: int) -> int:
    """Koko eating bananas. Binary search on answer. O(n logm).
    >>> min_eating_speed([3,6,7,11], 8)
    4
    """
    def ok(k: int) -> bool: return sum(math.ceil(p/k) for p in piles) <= h
    l, r = 1, max(piles)
    while l < r:
        m = (l+r)//2
        if ok(m): r = m
        else: l = m+1
    return l


def ship_days(weights: List[int], days: int) -> int:
    """Min ship capacity to deliver all in days. O(n log(sum)).
    >>> ship_days(list(range(1,11)), 5)
    15
    """
    def ok(cap: int) -> bool:
        d, load = 1, 0
        for w in weights:
            if load+w > cap: d += 1; load = 0
            load += w
        return d <= days
    l, r = max(weights), sum(weights)
    while l < r:
        m = (l+r)//2
        if ok(m): r = m
        else: l = m+1
    return l


def search_insert(nums: List[int], target: int) -> int:
    """Find index to insert target maintaining sort order.
    >>> search_insert([1,3,5,6], 2)
    1
    """
    l, r = 0, len(nums)
    while l < r:
        m = (l+r)//2
        if nums[m] < target: l = m+1
        else: r = m
    return l


def find_min_rotated(nums: List[int]) -> int:
    """Find min in rotated sorted array.
    >>> find_min_rotated([3,4,5,1,2])
    1
    """
    l, r = 0, len(nums)-1
    while l < r:
        m = (l+r)//2
        if nums[m] > nums[r]: l = m+1
        else: r = m
    return nums[l]


if __name__ == "__main__":
    print(binary_search([-1,0,3,5,9,12], 9))
    print(search_range([5,7,7,8,8,10], 8))
    print(search_rotated([4,5,6,7,0,1,2], 0))
    print(find_peak([1,2,3,1]))
    print(isqrt(8), isqrt(9))
    print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(min_eating_speed([3,6,7,11], 8))
    print(ship_days(list(range(1,11)), 5))
