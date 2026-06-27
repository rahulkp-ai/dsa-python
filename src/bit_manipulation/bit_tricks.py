"""
Module: bit_tricks.py  Topic: Bit Manipulation
Popcount, power of two, XOR tricks, bit DP, bitwise ops.
"""

from typing import List


def count_bits(n: int) -> int:
    """Count 1-bits (Brian Kernighan). O(k) where k=set bits.
    >>> count_bits(11)
    3
    """
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def is_power_of_two(n: int) -> bool:
    """Check power of 2. O(1).
    >>> is_power_of_two(16)
    True
    """
    return n > 0 and (n & (n - 1)) == 0


def single_number(nums: List[int]) -> int:
    """Element appearing once (others twice). XOR. O(n).
    >>> single_number([4,1,2,1,2])
    4
    """
    res = 0
    for n in nums:
        res ^= n
    return res


def single_number_ii(nums: List[int]) -> int:
    """Element appearing once (others three times). O(n).
    >>> single_number_ii([2,2,3,2])
    3
    """
    ones = twos = 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones


def missing_number(nums: List[int]) -> int:
    """Find missing number 0..n via XOR. O(n).
    >>> missing_number([3,0,1])
    2
    """
    n = len(nums)
    res = n
    for i, v in enumerate(nums):
        res ^= i ^ v
    return res


def reverse_bits(n: int) -> int:
    """Reverse bits of 32-bit unsigned integer. O(1).
    >>> reverse_bits(43261596) == 964176192
    True
    """
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


def get_bit(n: int, i: int) -> int:
    """Get i-th bit."""
    return (n >> i) & 1


def set_bit(n: int, i: int) -> int:
    """Set i-th bit."""
    return n | (1 << i)


def clear_bit(n: int, i: int) -> int:
    """Clear i-th bit."""
    return n & ~(1 << i)


def flip_bit(n: int, i: int) -> int:
    """Toggle i-th bit."""
    return n ^ (1 << i)


def count_bits_range(n: int) -> List[int]:
    """Count set bits for 0..n using DP. O(n).
    >>> count_bits_range(5)
    [0, 1, 1, 2, 1, 2]
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


def sum_no_plus(a: int, b: int) -> int:
    """Add two ints without + operator. O(1).
    >>> sum_no_plus(3, 5)
    8
    """
    mask = 0xFFFFFFFF
    while b & mask:
        carry = a & b
        a ^= b
        b = carry << 1
    return a if b == 0 else a & mask


def subsets_bitmask(nums: List[int]) -> List[List[int]]:
    """Generate all subsets using bitmask. O(2^n * n).
    >>> len(subsets_bitmask([1,2,3]))
    8
    """
    n = len(nums)
    return [[nums[j] for j in range(n) if mask & (1 << j)] for mask in range(1 << n)]


def num_of_flips(start: int, goal: int) -> int:
    """Minimum bit flips to convert start to goal.
    >>> num_of_flips(10, 7)
    3
    """
    return count_bits(start ^ goal)


def max_xor(nums: List[int]) -> int:
    """Maximum XOR of two numbers. O(n) using trie.
    >>> max_xor([3,10,5,25,2,8])
    28
    """
    max_result = 0
    prefix = 0
    for i in range(31, -1, -1):
        prefix |= 1 << i
        prefixes = {n & prefix for n in nums}
        temp = max_result | (1 << i)
        if any(temp ^ p in prefixes for p in prefixes):
            max_result = temp
    return max_result


if __name__ == "__main__":
    print("Popcount(11):", count_bits(11))
    print("Power of 2 (16):", is_power_of_two(16))
    print("Single number:", single_number([4, 1, 2, 1, 2]))
    print("Missing number:", missing_number([3, 0, 1]))
    print("Bit ops on 10 (1010):")
    print("  get bit 1:", get_bit(10, 1))
    print("  set bit 0:", bin(set_bit(10, 0)))
    print("  clear bit 1:", bin(clear_bit(10, 1)))
    print("Count bits 0-5:", count_bits_range(5))
    print("Sum 3+5 (no +):", sum_no_plus(3, 5))
    print("Subsets [1,2,3]:", len(subsets_bitmask([1, 2, 3])))
