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
    Best ime to buy/sell stock (one transaction). O(n) time, O(1) space.
    max_profit([7,1,5,3,6,4])
    5
    """

    min_p, best = float("inf"), 0
    for p in prices:
        min_p= min(min_p, p)
        best = max(best, p - min_p)
    return best

"""
Product Except Self
The Goal: Given an array of numbers, return a new array where each element at index i 
is the product of all the numbers in the original array except the one at i. 
You cannot use division, and the solution must run in O(n) time.
The Example: For nums = [1, 2, 3, 4], the output is [24, 12, 8, 6].
At index 0: 2x3x4=24
At index 1: 1x3x4=12
At index 2: 1x2x4=8
At index 3: 1x2x3=6
"""

def product_expect_self(nums: List[int]) -> List[int]:
    """ Product of all elements except self. No Division, O(n) time, O(1) extra
    product_expect_self([1,2,3,4])
    [24,12, 8, 6]
    """
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    sufix =1
    for i in range(n-1, -1,-1):
        out[i] *= sufix
        sufix *= nums[i]
    return out 

"""
Trapping Rain water
The Goal: Given an array of non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it can trap after raining.
The Core Logic: Water can only be trapped on top of a bar if there are taller bars on both its left and right sides. 
The maximum height of water that can be trapped above any single bar i is determined by the shorter of the two tallest 
boundaries enclosing it, minus the height of the bar itself
Hard to understand
"""
def trap_rain_water(height: List[int]) -> int:
    """ Trapping rain water, two poinetrs. O(n) time, O(1) space.
    trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1])
    6
    """
    l, r = 0, len(height) - 1
    lmax = rmax = water = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= lmax: lmax = height[l]
            else: water += lmax - height[l]
            l += 1
        else:
            if height[r] >= rmax: rmax = height[r]
            else: water += rmax - height[r]
            r -= 1
    return water

"""
Three Sum
The Goal: Given an array of integers, find all unique triplets (groups of three numbers) 
that add up to exactly zero (a+b+c=0). The output must not contain duplicate triplets, 
even if the numbers appear multiple times in the input array.

The Core Logic: The most efficient way to solve this in O(n * 2) time is to first sort the array. 
Then, you iterate through the array using a loop to fix the first number (a). For the remaining part of the array, 
you use a Two-Pointer approach (one starting at the left, one at the right) to find two numbers (b and c) 
that match the target. Sorting makes it incredibly easy to skip duplicate numbers and avoid repeating triplets.
"""
def three_sum(nums: List[int]) -> List[List[int]]:
    """ Find all unique triplets summing to zero. O(n^2) time.
    three_sum([-1,0,1,2,-1,-4])
    [[-1,1,1], [-1,0,1]]
    """

    nums.sort(); result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1
                while l < r and nums[r] == nums[r - 1]: r -= 1
                l += 1; r -= 1
            elif s < 0: l += 1
            else: r -= 1
    return result

if __name__ == "__main__":
    print("Two Sum:", two_sun([2,11,7,15],9))
    print("Max subarray:", max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
    print("Max profit:", max_profit([7,1,5,3,6,4]))
    print("Product Expect Self:", product_expect_self([1,2,3,4]))
    print("Trap Rain Water:", trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
    print("3Sum:", three_sum([-1,0,1,2,-1,-4]))