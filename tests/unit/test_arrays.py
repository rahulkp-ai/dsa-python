"""Unit tests for array algorithms."""
import pytest
from src.arrays.array_algorithms import (
    two_sum, max_subarray, max_profit, product_except_self,
    trap_rain_water, three_sum, PrefixSum, rotate_array, max_area,
    find_min_rotated, max_product_subarray
)

def test_two_sum(): assert two_sum([2,7,11,15],9) == [0,1]
def test_two_sum_mid(): assert two_sum([3,2,4],6) == [1,2]
def test_two_sum_none(): assert two_sum([1,2,3],10) is None

def test_kadane(): assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
def test_kadane_all_neg(): assert max_subarray([-1,-2,-3]) == -1
def test_kadane_single(): assert max_subarray([5]) == 5

def test_max_profit(): assert max_profit([7,1,5,3,6,4]) == 5
def test_max_profit_no_gain(): assert max_profit([7,6,4,3,1]) == 0
def test_max_profit_empty(): assert max_profit([]) == 0

def test_product(): assert product_except_self([1,2,3,4]) == [24,12,8,6]
def test_product_zero(): assert product_except_self([0,1,2]) == [2,0,0]

def test_trap(): assert trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
def test_trap_flat(): assert trap_rain_water([1,1,1]) == 0
def test_trap_short(): assert trap_rain_water([1,2]) == 0

def test_three_sum():
    r = three_sum([-1,0,1,2,-1,-4])
    assert [-1,-1,2] in r and [-1,0,1] in r
def test_three_sum_empty(): assert three_sum([0,1,1]) == []

def test_prefix_sum():
    ps = PrefixSum([1,2,3,4,5])
    assert ps.range_sum(1,3)==9 and ps.range_sum(0,4)==15

def test_rotate(): assert rotate_array([1,2,3,4,5,6,7],3) == [5,6,7,1,2,3,4]
def test_rotate_k_zero(): assert rotate_array([1,2,3],0) == [1,2,3]

def test_max_area(): assert max_area([1,8,6,2,5,4,8,3,7]) == 49

def test_find_min_rotated(): assert find_min_rotated([3,4,5,1,2]) == 1
def test_find_min_not_rotated(): assert find_min_rotated([1,2,3,4,5]) == 1

def test_max_product(): assert max_product_subarray([2,3,-2,4]) == 6
def test_max_product_neg(): assert max_product_subarray([-2,0,-1]) == 0
