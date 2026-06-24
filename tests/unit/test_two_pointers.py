"""Unit tests for two pointers."""
import pytest
from src.two_pointers.two_pointers import (
    remove_duplicates, two_sum_sorted, move_zeroes,
    squares_sorted, long_ones_k_flip, is_subsequence, sort_colors
)

def test_remove_dupes():
    nums=[1,1,2,3,3]; k=remove_duplicates(nums)
    assert k==3 and nums[:k]==[1,2,3]

def test_two_sum_s(): assert two_sum_sorted([2,7,11,15],9)==[1,2]

def test_move_zeroes(): assert move_zeroes([0,1,0,3,12])==[1,3,12,0,0]

def test_squares(): assert squares_sorted([-4,-1,0,3,10])==[0,1,9,16,100]

def test_long_ones(): assert long_ones_k_flip([1,1,0,0,1,1,1,0],2)==7

def test_is_subseq(): assert is_subsequence("abc","ahbgdc") and not is_subsequence("axc","ahbgdc")

def test_sort_colors(): assert sort_colors([2,0,2,1,1,0])==[0,0,1,1,2,2]
