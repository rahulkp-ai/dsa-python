"""
Module: recursion_patterns.py  Topic: Recursion
Classic recursive patterns with memoization.
"""

from functools import lru_cache
from typing import List


def factorial(n: int) -> int:
    """n! recursive. O(n) time and space.
    >>> factorial(5)
    120
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def power(base: float, exp: int) -> float:
    """Fast exponentiation. O(logn).
    >>> power(2, 10)
    1024.0
    """
    if exp == 0:
        return 1.0
    if exp < 0:
        return 1.0 / power(base, -exp)
    half = power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return base * half * half


def flatten(nested: list) -> list:
    """Flatten arbitrarily nested list. O(n).
    >>> flatten([1,[2,[3,[4]],5]])
    [1, 2, 3, 4, 5]
    """
    result: list = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def tower_of_hanoi(n: int, src: str = "A", dst: str = "C", aux: str = "B") -> List[str]:
    """Tower of Hanoi moves. O(2^n).
    >>> len(tower_of_hanoi(3))
    7
    """
    if n == 1:
        return [f"Move disk 1: {src} -> {dst}"]
    moves: List[str] = []
    moves.extend(tower_of_hanoi(n - 1, src, aux, dst))
    moves.append(f"Move disk {n}: {src} -> {dst}")
    moves.extend(tower_of_hanoi(n - 1, aux, dst, src))
    return moves


@lru_cache(maxsize=None)
def fibonacci_memo(n: int) -> int:
    """Fibonacci with memoization. O(n).
    >>> fibonacci_memo(10)
    55
    """
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


def generate_parentheses(n: int) -> List[str]:
    """All valid parentheses of length 2n. O(4^n/sqrt(n)).
    >>> generate_parentheses(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    """
    res: List[str] = []

    def bt(s: str, o: int, c: int) -> None:
        if len(s) == 2 * n:
            res.append(s)
            return
        if o < n:
            bt(s + "(", o + 1, c)
        if c < o:
            bt(s + ")", o, c + 1)

    bt("", 0, 0)
    return res


def merge_sort_recursive(arr: List[int]) -> List[int]:
    """Recursive merge sort. O(n logn).
    >>> merge_sort_recursive([3,1,4,1,5,9,2,6])
    [1, 1, 2, 3, 4, 5, 6, 9]
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l = merge_sort_recursive(arr[:mid])
    r = merge_sort_recursive(arr[mid:])
    res: List[int] = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res.extend(l[i:])
    res.extend(r[j:])
    return res


def binary_search_rec(nums: List[int], target: int, l: int = 0, r: int = -1) -> int:
    """Recursive binary search. O(logn).
    >>> binary_search_rec([1,3,5,7,9], 5)
    2
    """
    if r == -1:
        r = len(nums) - 1
    if l > r:
        return -1
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_rec(nums, target, mid + 1, r)
    else:
        return binary_search_rec(nums, target, l, mid - 1)


if __name__ == "__main__":
    print("5! =", factorial(5))
    print("2^10 =", power(2, 10))
    print("Flatten:", flatten([1, [2, [3, [4]], 5]]))
    print("Hanoi 3:", tower_of_hanoi(3))
    print("Fib(10):", fibonacci_memo(10))
    print("Generate parens n=3:", generate_parentheses(3))
    print("Merge sort:", merge_sort_recursive([3, 1, 4, 1, 5, 9, 2, 6]))
