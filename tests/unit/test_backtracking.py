"""Unit tests for backtracking."""
import pytest
from src.backtracking.backtracking import (
    solve_n_queens, permutations, combinations, combination_sum,
    combination_sum_ii, subsets, subsets_with_dup, word_search,
    letter_combinations, palindrome_partition, solve_sudoku
)

# --- N-Queens ---
def test_queens_4(): assert len(solve_n_queens(4)) == 2
def test_queens_1(): assert len(solve_n_queens(1)) == 1
def test_queens_valid():
    for sol in solve_n_queens(4):
        assert len(sol) == 4 and all(r.count("Q") == 1 for r in sol)

# --- Permutations ---
def test_perms(): assert len(permutations([1, 2, 3])) == 6
def test_perms_empty(): assert permutations([]) == [[]]

# --- Combinations ---
def test_combs(): assert len(combinations(4, 2)) == 6 and [1, 2] in combinations(4, 2)
def test_combs_prune(): assert combinations(3, 4) == []

# --- Combination Sum ---
def test_combo_sum():
    r = combination_sum([2, 3, 6, 7], 7)
    assert [2, 2, 3] in r and [7] in r

# --- Combination Sum II ---
def test_combo_sum_ii():
    r = combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8)
    assert [1, 1, 6] in r and [1, 2, 5] in r and [1, 7] in r and [2, 6] in r

# --- Subsets ---
def test_subsets(): assert len(subsets([1, 2, 3])) == 8 and [] in subsets([1, 2, 3])

# --- Subsets with Duplicates ---
def test_subsets_with_dup():
    r = subsets_with_dup([1, 2, 2])
    assert len(r) == 6 and [1, 2] in r and [1, 2, 2] in r

# --- Word Search ---
def test_word_search():
    b = [["A", "B", "C"], ["S", "F", "C"], ["A", "D", "E"]]
    assert word_search(b, "ABCCED")
    assert not word_search(b, "ABCB")

# --- Letter Combinations ---
def test_letter_combos(): assert len(letter_combinations("23")) == 9
def test_letter_empty(): assert letter_combinations("") == []

# --- Palindrome Partition ---
def test_palindrome_partition():
    r = palindrome_partition("aab")
    assert ["a", "a", "b"] in r and ["aa", "b"] in r

# --- Solve Sudoku ---
def test_sudoku():
    b = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert solve_sudoku(b)
    assert all(len(set(row)) == 9 for row in b)
    assert all(len(set(b[r][c] for r in range(9))) == 9 for c in range(9))