import pytest

from src.recursion import recursion_patterns as rp


def test_factorial_basic():
    assert rp.factorial(0) == 1
    assert rp.factorial(1) == 1
    assert rp.factorial(5) == 120


@pytest.mark.parametrize(
    "base,exp,expected",
    [
        (2, 10, 1024.0),
        (2, -2, 0.25),
        (5, 0, 1.0),
        (-2, 3, -8.0),
    ],
)
def test_power_various(base, exp, expected):
    assert rp.power(base, exp) == expected


def test_flatten():
    assert rp.flatten([1, [2, [3, [4]], 5]]) == [1, 2, 3, 4, 5]
    assert rp.flatten([]) == []
    assert rp.flatten([[], [1, []]]) == [1]


def test_tower_of_hanoi():
    assert rp.tower_of_hanoi(1) == ["Move disk 1: A -> C"]
    moves = rp.tower_of_hanoi(3)
    assert len(moves) == 7
    assert moves[0].startswith("Move disk")
    assert moves[-1].endswith("C")


def test_fibonacci_memo_and_cache():
    assert rp.fibonacci_memo(0) == 0
    assert rp.fibonacci_memo(1) == 1
    assert rp.fibonacci_memo(10) == 55
    # ensure it's decorated with lru_cache
    assert hasattr(rp.fibonacci_memo, "cache_info") and callable(
        rp.fibonacci_memo.cache_info
    )


def test_generate_parentheses():
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(rp.generate_parentheses(3)) == sorted(expected)
    assert rp.generate_parentheses(0) == [""]


def test_merge_sort_recursive():
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    assert rp.merge_sort_recursive(arr) == [1, 1, 2, 3, 4, 5, 6, 9]
    assert rp.merge_sort_recursive([]) == []
    assert rp.merge_sort_recursive([1]) == [1]


def test_binary_search_rec():
    arr = [1, 3, 5, 7, 9]
    assert rp.binary_search_rec(arr, 5) == 2
    assert rp.binary_search_rec(arr, 2) == -1
    # explicit bounds
    assert rp.binary_search_rec(arr, 7, 3, 4) == 3
