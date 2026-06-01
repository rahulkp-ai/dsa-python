"""
Module: array_algorithms.py Topic: Arrays
Two Sum,Kadane's, Max profit, Product Except Self, Trapping Rain water,
3Sum, Prefix Sum, Rotate Array, Container with Most Water, Find Min Rotated.
"""

from typing import List, Optional, Tuple

"""
Two Sum
The Goal: Find two numbers in an array that add up to a specific target number and return their indices.
The Trick: Instead of checking every pair, use a Hash Map (Dictionary). 
As you iterate through the array, calculate the complement (Target - Current Number). 
If the complement is already in your map, you've found your pair.
"""
def two_sun(nums: List[int], target: int) -> Optional[List[int]]:
    """ 
    Hash-map two sum. O(n) time, O(n) space.
    two_sum([2,7,11,15],9)
    [0,1]
    """

    seen : dict ={}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return None

"""
Kadane's Algorithm (Max Subarray / Max Profit)
The Goal: Find the contiguous subarray within an array that has the largest sum. 
(In stock trading terms, finding the best days to buy and sell).
The Trick: At each element, you make a choice: Is it better to add the current element to your 
existing running total, or start a brand-new subarray from the current element? 
You track the local_max at each step and update the global_max.
"""

def max_subarray(nums: List[int]) -> List[int]:
    """
    Kadane's Algoritm. O(n) time, O(1) space.
    max_subarray([-2,1,-3,4,-1,2,1,-5,4])
    6
    Current Streak(i) = max(nums[i],nums[i]+Current Streak(i-1))
    hard to mental calculation
    """

    max_s = curr = nums[0]
    for num in nums[1:]:
        curr = max(num, curr + num)
        max_s = max(max_s, curr)
    return max_s


"""
Max Profit
The Goal: Given an array of daily stock prices, find the maximum profit you can make from a single buy-and-sell transaction. 
You cannot sell a stock before you buy it.
The Example: For prices = [7, 1, 5, 3, 6, 4], the max profit is 5 (buy at 1 on day 2, sell at 6 on day 5).
"""

def max_profit(prices: List[int]) -> int:
    """
    Best ime to buy/sell stock (onr transaction). O(n) time, O(1) space.
    max_profit([7,1,5,3,6,4])
    5
    """

    min_p, best = float("inf"), 0
    for p in prices:
        min_p= min(min_p, p)
        best = max(best, p - min_p)
    return best


if __name__ == "__main__":
    print("Two Sum:", two_sun([2,11,7,15],9))
    print("Max subarray:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
    print("Max profit:", max_profit([7,1,5,3,6,4]))