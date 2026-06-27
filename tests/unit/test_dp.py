"""Unit tests for dynamic programming."""


from src.dynamic_programming.dp_algorithms import (
    climbing_stairs,
    coin_change,
    coin_change_ways,
    edit_distance,
    fibonacci,
    house_robber,
    house_robber_ii,
    knapsack_01,
    lcs,
    lcs_string,
    lis,
    max_product_subarray,
    palindromic_substrings,
    unique_paths,
    word_break,
)


def test_fib():
    assert fibonacci(10) == 55


def test_fib_base():
    assert fibonacci(0) == 0 and fibonacci(1) == 1


def test_coin_change():
    assert coin_change([1, 5, 6, 9], 11) == 2


def test_coin_impossible():
    assert coin_change([2], 3) == -1


def test_coin_zero():
    assert coin_change([1, 2, 5], 0) == 0


def test_coin_ways():
    assert coin_change_ways([1, 2, 5], 5) == 4


def test_knapsack():
    assert knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7


def test_knapsack_zero():
    assert knapsack_01([1], [1], 0) == 0


def test_lcs():
    assert lcs("ABCBDAB", "BDCABA") == 4


def test_lcs_none():
    assert lcs("abc", "xyz") == 0


def test_lcs_string():
    assert lcs_string("ABCBDAB", "BDCABA") in ["BCBA", "BDAB", "BCAB"]


def test_lis():
    assert lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_lis_sorted():
    assert lis([1, 2, 3, 4, 5]) == 5


def test_lis_single():
    assert lis([5]) == 1


def test_edit():
    assert edit_distance("horse", "ros") == 3


def test_edit_same():
    assert edit_distance("abc", "abc") == 0


def test_edit_empty():
    assert edit_distance("", "abc") == 3


def test_robber():
    assert house_robber([2, 7, 9, 3, 1]) == 12


def test_robber_two():
    assert house_robber([2, 1]) == 2


def test_robber_ii():
    assert house_robber_ii([2, 3, 2]) == 3


def test_paths():
    assert unique_paths(3, 7) == 28


def test_paths_one():
    assert unique_paths(1, 1) == 1


def test_word_break():
    assert word_break("leetcode", ["leet", "code"])


def test_word_break_fail():
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])


def test_stairs():
    assert climbing_stairs(5) == 8


def test_stairs_1():
    assert climbing_stairs(1) == 1


def test_max_prod():
    assert max_product_subarray([2, 3, -2, 4]) == 6


def test_palindromic():
    assert palindromic_substrings("aaa") == 6
