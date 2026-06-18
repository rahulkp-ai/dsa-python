"""Unit tests for sliding window."""
import pytest
from src.sliding_window.sliding_window import (
    max_sum_subarray_k, longest_substring_k_distinct,
    longest_repeating_replacement, min_size_subarray_sum,
    check_inclusion, max_vowels_k, subarray_product_less_k
)

def test_max_sum_k(): assert max_sum_subarray_k([2,1,5,1,3,2],3)==9
def test_k_distinct(): assert longest_substring_k_distinct("eceba",2)==3
def test_replacement(): assert longest_repeating_replacement("AABABBA",1)==4
def test_min_subarray(): assert min_size_subarray_sum([2,3,1,2,4,3],7)==2
def test_inclusion(): assert check_inclusion("ab","eidbaooo")
def test_max_vowels(): assert max_vowels_k("abciiidef",3)==3
def test_product_less(): assert subarray_product_less_k([10,5,2,6],100)==8
