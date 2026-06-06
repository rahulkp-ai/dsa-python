"""Unit tests for bit manipulation."""
import pytest
from src.bit_manipulation.bit_tricks import (
    count_bits, is_power_of_two, single_number, missing_number,
    reverse_bits, get_bit, set_bit, clear_bit, flip_bit,
    count_bits_range, sum_no_plus, subsets_bitmask
)

def test_popcount(): assert count_bits(11)==3 and count_bits(0)==0
def test_power_two(): assert is_power_of_two(16) and not is_power_of_two(15)
def test_single_number(): assert single_number([4,1,2,1,2])==4
def test_missing(): assert missing_number([3,0,1])==2 and missing_number([0])==1
def test_get_bit(): assert get_bit(10,1)==1 and get_bit(10,0)==0
def test_set_bit(): assert set_bit(10,0)==11
def test_clear_bit(): assert clear_bit(11,0)==10
def test_flip_bit(): assert flip_bit(10,0)==11
def test_count_range(): assert count_bits_range(5)==[0,1,1,2,1,2]
def test_sum_no_plus(): assert sum_no_plus(3,5)==8 and sum_no_plus(0,0)==0
def test_subsets_bitmask(): assert len(subsets_bitmask([1,2,3]))==8
