"""
Module: dp_algorithms.py  Topic: Dynamic Programming
Fibonacci, Coin Change, 0/1 Knapsack, LCS, LIS, Edit Distance,
House Robber, Unique Paths, Word Break, Climbing Stairs, Max Product.
"""

import bisect
from typing import List


def fibonacci(n: int) -> int:
    """Fibonacci (space-optimised). O(n) time, O(1) space."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def coin_change(coins: List[int], amount: int) -> int:
    """Min coins for amount. O(amount*|coins|) time. -1 if impossible.
    >>> coin_change([1,5,6,9], 11)
    2
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return int(dp[amount]) if dp[amount] != float("inf") else -1


def coin_change_ways(coins: List[int], amount: int) -> int:
    """Count ways to make amount (unlimited coins).
    >>> coin_change_ways([1,2,5], 5)
    4
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] += dp[i - c]
    return dp[amount]


def knapsack_01(weights: List[int], values: List[int], cap: int) -> int:
    """0/1 Knapsack (space-optimised). O(n*cap) time, O(cap) space.
    >>> knapsack_01([2,3,4,5],[3,4,5,6],5)
    7
    """
    dp = [0] * (cap + 1)
    for i in range(len(weights)):
        for w in range(cap, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[cap]


def lcs(s1: str, s2: str) -> int:
    """Longest Common Subsequence length. O(m*n) time.
    >>> lcs("ABCBDAB", "BDCABA")
    4
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lcs_string(s1: str, s2: str) -> str:
    """Return actual LCS string."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            res.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))


def lis(nums: List[int]) -> int:
    """Longest Increasing Subsequence (patience sorting). O(n logn).
    >>> lis([10,9,2,5,3,7,101,18])
    4
    """
    tails: List[int] = []
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails):
            tails.append(n)
        else:
            tails[pos] = n
    return len(tails)


def edit_distance(w1: str, w2: str) -> int:
    """Levenshtein edit distance. O(m*n) time.
    >>> edit_distance("horse", "ros")
    3
    """
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


def house_robber(nums: List[int]) -> int:
    """Max money no adjacent houses. O(n) time, O(1) space.
    >>> house_robber([2,7,9,3,1])
    12
    """
    a = b = 0
    for n in nums:
        a, b = b, max(b, a + n)
    return b


def house_robber_ii(nums: List[int]) -> int:
    """House Robber circular. O(n) time."""

    def rob(h: List[int]) -> int:
        a = b = 0
        for v in h:
            a, b = b, max(b, a + v)
        return b

    if len(nums) == 1:
        return nums[0]
    return max(rob(nums[:-1]), rob(nums[1:]))


def unique_paths(m: int, n: int) -> int:
    """Unique paths in m*n grid (right/down only). O(m*n) time, O(n) space.
    >>> unique_paths(3,7)
    28
    """
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[n - 1]


def word_break(s: str, words: List[str]) -> bool:
    """Can string be segmented using dictionary. O(n^2).
    >>> word_break("leetcode", ["leet","code"])
    True
    """
    ws = set(words)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in ws:
                dp[i] = True
                break
    return dp[n]


def climbing_stairs(n: int) -> int:
    """Ways to climb n stairs (1 or 2 steps). O(n) time, O(1) space.
    >>> climbing_stairs(5)
    8
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def max_product_subarray(nums: List[int]) -> int:
    """Max product subarray. O(n) time, O(1) space.
    >>> max_product_subarray([2,3,-2,4])
    6
    """
    mx = mn = res = nums[0]
    for num in nums[1:]:
        cands = (num, mx * num, mn * num)
        mx, mn = max(cands), min(cands)
        res = max(res, mx)
    return res


def palindromic_substrings(s: str) -> int:
    """Count all palindromic substrings. O(n^2).
    >>> palindromic_substrings("abc")
    3
    """
    count = 0

    def expand(l: int, r: int) -> None:
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)
    return count


if __name__ == "__main__":
    print("Fibonacci(10):", fibonacci(10))
    print("Coin Change [1,5,6,9]->11:", coin_change([1, 5, 6, 9], 11))
    print("Ways [1,2,5]->5:", coin_change_ways([1, 2, 5], 5))
    print("Knapsack:", knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5))
    print("LCS:", lcs("ABCBDAB", "BDCABA"), lcs_string("ABCBDAB", "BDCABA"))
    print("LIS:", lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print("Edit Distance:", edit_distance("horse", "ros"))
    print("House Robber:", house_robber([2, 7, 9, 3, 1]))
    print("House Robber II:", house_robber_ii([2, 3, 2]))
    print("Unique Paths:", unique_paths(3, 7))
    print("Word Break:", word_break("leetcode", ["leet", "code"]))
    print("Climbing Stairs:", climbing_stairs(5))
    print("Max Product:", max_product_subarray([2, 3, -2, 4]))
    print("Palindromic Substrings:", palindromic_substrings("aaa"))
