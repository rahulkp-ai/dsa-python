"""Unit tests for hashing patterns."""
import pytest
from src.hashing.hash_algorithms import (
    contains_duplicate, 
    longest_consecutive, 
    subarray_sum_k,
    top_k_frequent, 
    find_duplicates,
    LRUCache,
    two_sum, 
    group_anagrams, 
    ransom_note,
    TwoSum
)

def test_contains_dup():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3]) is False
    assert contains_duplicate([]) is False


def test_longest_consec():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0


def test_subarray_k():
    assert subarray_sum_k([1, 1, 1], 2) == 2
    assert subarray_sum_k([1, 2, 3], 3) == 2  # [1, 2] and [3]
    assert subarray_sum_k([9, 4, 20, 3, 10, 5], 33) == 2


def test_top_k():
    # Order inside the result sublists doesn't matter, but bucket sort returns sorted by freq
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]


def test_find_duplicates():
    assert find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]
    assert find_duplicates([1, 1, 2]) == [1]
    assert find_duplicates([1, 2, 3]) == []


def test_lru():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    
    lru.put(3, 3)          # Evicts key 2
    assert lru.get(2) == -1
    
    lru.put(4, 4)          # Evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    
    # Updating an existing key shouldn't alter capacity limit
    lru.put(3, 30)
    assert lru.get(3) == 30


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3], 7) is None


def test_group_anagrams():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort the inner lists and outer list to reliably assert equality
    sorted_res = sorted([sorted(group) for group in result])
    expected = sorted([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    assert sorted_res == expected


def test_ransom_note():
    assert ransom_note("a", "b") is False
    assert ransom_note("aa", "ab") is False
    assert ransom_note("aa", "aab") is True


def test_two_sum_class():
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    assert ts.find(4) is True   # 1 + 3
    assert ts.find(7) is False
    
    # Check item duplication edge cases
    ts2 = TwoSum()
    ts2.add(3)
    assert ts2.find(6) is False  # Cannot reuse the same element instance
    ts2.add(3)
    assert ts2.find(6) is True   # Can use two separate instances of '3'