"""
Module: sliding_window.py  Topic: Sliding Window
Fixed and variable size window patterns.
"""
from typing import List, Optional
from collections import Counter, deque


def max_sum_subarray_k(nums: List[int], k: int) -> int:
    """Max sum subarray of size k. O(n).
    >>> max_sum_subarray_k([2,1,5,1,3,2], 3)
    9
    """
    window = sum(nums[:k]); best = window
    for i in range(k, len(nums)):
        window += nums[i]-nums[i-k]; best = max(best, window)
    return best


def longest_substring_k_distinct(s: str, k: int) -> int:
    """Longest substring with at most k distinct chars. O(n).
    >>> longest_substring_k_distinct("eceba", 2)
    3
    """
    window: dict = {}; l = res = 0
    for r, c in enumerate(s):
        window[c] = window.get(c,0)+1
        while len(window) > k:
            window[s[l]] -= 1
            if window[s[l]] == 0: del window[s[l]]
            l += 1
        res = max(res, r-l+1)
    return res


def longest_repeating_replacement(s: str, k: int) -> int:
    """Longest repeating char with at most k replacements. O(n).
    >>> longest_repeating_replacement("AABABBA", 1)
    4
    """
    count: dict = {}; max_count = l = res = 0
    for r, c in enumerate(s):
        count[c] = count.get(c,0)+1; max_count = max(max_count, count[c])
        while (r-l+1)-max_count > k:
            count[s[l]] -= 1; l += 1
        res = max(res, r-l+1)
    return res


def min_size_subarray_sum(nums: List[int], target: int) -> int:
    """Minimum length subarray with sum >= target. O(n).
    >>> min_size_subarray_sum([2,3,1,2,4,3], 7)
    2
    """
    l = total = 0; res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r-l+1); total -= nums[l]; l += 1
    return int(res) if res != float("inf") else 0


def check_inclusion(s1: str, s2: str) -> bool:
    """Permutation of s1 is substring of s2. O(n).
    >>> check_inclusion("ab","eidbaooo")
    True
    """
    if len(s1) > len(s2): return False
    c1, c2 = Counter(s1), Counter(s2[:len(s1)])
    if c1 == c2: return True
    for i in range(len(s1), len(s2)):
        c2[s2[i]] += 1
        old = s2[i-len(s1)]; c2[old] -= 1
        if c2[old] == 0: del c2[old]
        if c1 == c2: return True
    return False


def max_vowels_k(s: str, k: int) -> int:
    """Max vowels in any substring of length k. O(n).
    >>> max_vowels_k("abciiidef", 3)
    3
    """
    vowels = set("aeiou")
    count = sum(1 for c in s[:k] if c in vowels); best = count
    for i in range(k, len(s)):
        count += (s[i] in vowels) - (s[i-k] in vowels)
        best = max(best, count)
    return best


def subarray_product_less_k(nums: List[int], k: int) -> int:
    """Count subarrays with product < k. O(n).
    >>> subarray_product_less_k([10,5,2,6], 100)
    8
    """
    if k <= 1: return 0
    prod = 1; l = res = 0
    for r in range(len(nums)):
        prod *= nums[r]
        while prod >= k: prod //= nums[l]; l += 1
        res += r-l+1
    return res


if __name__ == "__main__":
    print("Max sum k=3:", max_sum_subarray_k([2,1,5,1,3,2],3))
    print("K distinct k=2:", longest_substring_k_distinct("eceba",2))
    print("Replacement k=1:", longest_repeating_replacement("AABABBA",1))
    print("Min subarray>=7:", min_size_subarray_sum([2,3,1,2,4,3],7))
    print("Inclusion:", check_inclusion("ab","eidbaooo"))
    print("Max vowels k=3:", max_vowels_k("abciiidef",3))
    print("Product < 100:", subarray_product_less_k([10,5,2,6],100))
