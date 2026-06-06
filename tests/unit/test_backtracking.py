"""Unit tests for backtracking."""
import pytest
from src.backtracking.backtracking import (
    solve_n_queens, permutations, combinations, subsets,
    combination_sum, word_search, letter_combinations, palindrome_partition
)

def test_queens_4(): assert len(solve_n_queens(4))==2
def test_queens_1(): assert len(solve_n_queens(1))==1
def test_queens_valid():
    for sol in solve_n_queens(4):
        assert len(sol)==4 and all(r.count("Q")==1 for r in sol)

def test_perms(): assert len(permutations([1,2,3]))==6
def test_perms_empty(): assert permutations([])==[[]]

def test_combs(): assert len(combinations(4,2))==6 and [1,2] in combinations(4,2)

def test_subsets(): assert len(subsets([1,2,3]))==8 and [] in subsets([1,2,3])

def test_combo_sum():
    r = combination_sum([2,3,6,7],7)
    assert [2,2,3] in r and [7] in r

def test_word_search():
    b=[["A","B","C"],["S","F","C"],["A","D","E"]]
    assert word_search(b,"ABCCED")
    assert not word_search(b,"ABCB")

def test_letter_combos(): assert len(letter_combinations("23"))==9
def test_letter_empty(): assert letter_combinations("")==[]

def test_palindrome_partition():
    r = palindrome_partition("aab")
    assert ["a","a","b"] in r
