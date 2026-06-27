"""
Module: two_pointers.py  Topic: Two Pointers
Opposite direction, same direction, fast/slow pointer patterns.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """Remove sorted-array duplicates in-place. O(n).
    >>> nums=[1,1,2,3,3]; remove_duplicates(nums)
    3
    """
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """Two sum on sorted array. O(n).
    >>> two_sum_sorted([2,7,11,15], 9)
    [1, 2]
    """
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1
    return []


def move_zeroes(nums: List[int]) -> List[int]:
    """Move zeros to end, maintain relative order. O(n).
    >>> move_zeroes([0,1,0,3,12])
    [1, 3, 12, 0, 0]
    """
    nums = nums.copy()
    k = 0
    for n in nums:
        if n != 0:
            nums[k] = n
            k += 1
    for i in range(k, len(nums)):
        nums[i] = 0
    return nums


def squares_sorted(nums: List[int]) -> List[int]:
    """Squares of sorted array in sorted order. O(n).
    >>> squares_sorted([-4,-1,0,3,10])
    [0, 1, 9, 16, 100]
    """
    n = len(nums)
    res = [0] * n
    l, r, p = 0, n - 1, n - 1
    while l <= r:
        ls, rs = nums[l] ** 2, nums[r] ** 2
        if ls > rs:
            res[p] = ls
            l += 1
        else:
            res[p] = rs
            r -= 1
        p -= 1
    return res


def three_sum_closest(nums: List[int], target: int) -> int:
    """3Sum closest to target. O(n^2).
    >>> three_sum_closest([-1,2,1,-4], 1)
    2
    """
    nums.sort()
    closest = float("inf")
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if abs(s - target) < abs(closest - target):
                closest = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return s
    return int(closest)


def long_ones_k_flip(nums: List[int], k: int) -> int:
    """Max consecutive 1s with at most k 0-flips. O(n).
    >>> long_ones_k_flip([1,1,0,0,1,1,1,0], 2)
    7
    """
    l = zeros = res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


def is_subsequence(s: str, t: str) -> bool:
    """Check if s is subsequence of t. O(n).
    >>> is_subsequence("abc","ahbgdc")
    True
    """
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def sort_colors(nums: List[int]) -> List[int]:
    """Dutch National Flag (sort 0,1,2 in-place). O(n).
    >>> sort_colors([2,0,2,1,1,0])
    [0, 0, 1, 1, 2, 2]
    """
    nums = nums.copy()
    lo = mid = 0
    hi = len(nums) - 1
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
    return nums


if __name__ == "__main__":
    print("Two sum sorted:", two_sum_sorted([2, 7, 11, 15], 9))
    print("Move zeroes:", move_zeroes([0, 1, 0, 3, 12]))
    print("Squares sorted:", squares_sorted([-4, -1, 0, 3, 10]))
    print("3Sum closest:", three_sum_closest([-1, 2, 1, -4], 1))
    print("Long ones k=2:", long_ones_k_flip([1, 1, 0, 0, 1, 1, 1, 0], 2))
    print("Is subsequence:", is_subsequence("abc", "ahbgdc"))
    print("Sort colors:", sort_colors([2, 0, 2, 1, 1, 0]))
