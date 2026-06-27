"""Unit tests for sorting algorithms."""

import random

import pytest

from src.sorting.sorting_algorithms import (
    bubble_sort,
    counting_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    radix_sort,
    selection_sort,
)

ALGOS = [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort]


@pytest.mark.parametrize("algo", ALGOS)
def test_normal(algo):
    assert algo([64, 34, 25, 12, 22, 11, 90]) == sorted([64, 34, 25, 12, 22, 11, 90])


@pytest.mark.parametrize("algo", ALGOS)
def test_empty(algo):
    assert algo([]) == []


@pytest.mark.parametrize("algo", ALGOS)
def test_single(algo):
    assert algo([42]) == [42]


@pytest.mark.parametrize("algo", ALGOS)
def test_already_sorted(algo):
    assert algo([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("algo", ALGOS)
def test_reverse_sorted(algo):
    assert algo([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("algo", ALGOS)
def test_duplicates(algo):
    assert algo([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]


@pytest.mark.parametrize("algo", ALGOS)
def test_negatives(algo):
    assert algo([-3, 1, -1, 2, 0]) == sorted([-3, 1, -1, 2, 0])


@pytest.mark.parametrize("algo", ALGOS)
def test_large_random(algo):
    arr = random.sample(range(1000), 100)
    assert algo(arr) == sorted(arr)


def test_counting_sort():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]


def test_counting_sort_empty():
    assert counting_sort([]) == []


def test_counting_sort_negative():
    with pytest.raises(ValueError):
        counting_sort([-1, 2, 3])


def test_radix_sort():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == sorted(
        [170, 45, 75, 90, 802, 24, 2, 66]
    )


def test_radix_empty():
    assert radix_sort([]) == []
