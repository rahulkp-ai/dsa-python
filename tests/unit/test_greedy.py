import pytest
from src.greedy.greedy_algorithms import (
    activity_selection, fractional_knapsack, can_jump, jump_game_ii, 
    can_complete_circuit, merge_intervals, insert_interval, 
    find_min_arrows, assign_cookies, partition_labels, huffman_coding
)

# =====================================================================
# 1. NEWLY UNCOVERED BASIC & JUMP GAME ALGORITHMS (Lines 40-44, 52-56)
# =====================================================================

def test_can_jump_true():
    assert can_jump([2, 3, 1, 1, 4]) is True

def test_can_jump_false():
    # Stranded at index 3 (value 0)
    assert can_jump([3, 2, 1, 0, 4]) is False

def test_jump_game_ii_standard():
    assert jump_game_ii([2, 3, 1, 1, 4]) == 2


# =====================================================================
# 2. INTERVAL & ARROW PACK (Lines 76-80, 85-93, 101-105)
# =====================================================================

def test_merge_intervals_standard():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_merge_intervals_no_overlap():
    assert merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

def test_insert_interval_middle():
    # Insert [2, 5] into [[1, 3], [6, 9]] -> [[1, 5], [6, 9]]
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

def test_insert_interval_at_start():
    assert insert_interval([[3, 5], [6, 9]], [1, 2]) == [[1, 2], [3, 5], [6, 9]]

def test_find_min_arrows_standard():
    assert find_min_arrows([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2

def test_find_min_arrows_empty():
    assert find_min_arrows([]) == 0


# =====================================================================
# 3. COOKIES, GAS, & STRINGS (Lines 87, 125-130)
# =====================================================================

def test_assign_cookies_standard():
    assert assign_cookies([1, 2, 3], [1, 1]) == 1
    assert assign_cookies([1, 2], [1, 2, 3]) == 2

def test_assign_cookies_unhappy():
    # Cookie sizes don't satisfy any child demand (Hits line 87 branch else conditions)
    assert assign_cookies([3], [1]) == 0

def test_can_complete_circuit_success():
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3

def test_can_complete_circuit_fail():
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1

def test_partition_labels_standard():
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]


# =====================================================================
# 4. MISSED CORE ALGORITHMS FROM PREVIOUS RUN
# =====================================================================

def test_activity_selection():
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    assert activity_selection(start, finish) == [0, 1, 3, 4]

def test_fractional_knapsack_standard():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    assert pytest.approx(fractional_knapsack(weights, values, 50)) == 240.0

def test_fractional_knapsack_zero_cap():
    assert fractional_knapsack([10], [60], 0) == 0.0

def test_huffman_coding_standard():
    text = "abracadabra"
    codes = huffman_coding(text)
    assert isinstance(codes, dict)
    assert set(codes.keys()) == set(text)
    assert len(codes['a']) < len(codes['b'])

def test_huffman_coding_single_char():
    assert huffman_coding("aaaa") == {"a": "0"}