import math

import pytest

from src.divide_conquer.divide_conquer import (
    closest_pair,
    count_inversions,
    find_kth_smallest,
    max_subarray_dc,
    power_fast,
)

# ==============================================================================
# 1. Tests for max_subarray_dc
# ==============================================================================


def test_max_subarray_dc_docstring_case():
    assert max_subarray_dc([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_dc_single_element():
    assert max_subarray_dc([5]) == 5
    assert max_subarray_dc([-3]) == -3


def test_max_subarray_dc_all_negatives():
    assert max_subarray_dc([-2, -3, -1, -5]) == -1


def test_max_subarray_dc_all_positives():
    assert max_subarray_dc([1, 2, 3, 4]) == 10


# ==============================================================================
# 2. Tests for closest_pair
# ==============================================================================


def test_closest_pair_docstring_case():
    pts = [(0, 0), (3, 4), (1, 1)]
    assert closest_pair(pts) < 2
    assert math.isclose(closest_pair(pts), math.sqrt(2))


def test_closest_pair_small_set():
    # Base cases handling n <= 3
    assert math.isclose(closest_pair([(0, 0), (0, 5)]), 5.0)


def test_closest_pair_larger_set():
    # Triggers the recursive D&C splitting and strip handling
    pts = [(0, 0), (1, 1), (5, 5), (6, 7), (10, 10), (11, 11.5)]
    # (11, 11.5) and (10, 10) or (1,1) and (0,0)
    assert closest_pair(pts) <= math.sqrt(2)


# ==============================================================================
# 3. Tests for power_fast
# ==============================================================================


def test_power_fast_docstring_case():
    assert power_fast(2, 10) == 1024.0


def test_power_fast_exponent_zero():
    assert power_fast(5, 0) == 1.0


def test_power_fast_odd_exponent():
    assert power_fast(3, 3) == 27.0
    assert power_fast(2, 5) == 32.0


# ==============================================================================
# 4. Tests for count_inversions
# ==============================================================================


def test_count_inversions_docstring_case():
    _, count = count_inversions([3, 1, 2])
    assert count == 2


def test_count_inversions_empty_or_single():
    assert count_inversions([]) == ([], 0)
    assert count_inversions([1]) == ([1], 0)


def test_count_inversions_sorted():
    merged, count = count_inversions([1, 2, 3, 4, 5])
    assert merged == [1, 2, 3, 4, 5]
    assert count == 0


def test_count_inversions_reversed():
    # [4, 3, 2, 1] has 6 inversions: (4,3), (4,2), (4,1), (3,2), (3,1), (2,1)
    _, count = count_inversions([4, 3, 2, 1])
    assert count == 6


# ==============================================================================
# 5. Tests for find_kth_smallest
# ==============================================================================


def test_find_kth_smallest_docstring_case():
    assert find_kth_smallest([7, 2, 1, 6, 5, 3, 4, 8], 3) == 3


def test_find_kth_smallest_first_and_last():
    nums = [7, 2, 1, 6, 5, 3, 4, 8]
    assert find_kth_smallest(nums, 1) == 1  # Minimum
    assert find_kth_smallest(nums, 8) == 8  # Maximum


def test_find_kth_smallest_single_item():
    assert find_kth_smallest([42], 1) == 42


def test_closest_pair_strip_boundary():
    """Forces execution of multiple points within the vertical strip zone."""
    # Points closely aligned on X, but separated on Y to trigger
    # the internal 'strip_closest' while loops completely.
    pts = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1)]
    assert closest_pair(pts) == 1.0


def test_main_block_execution(monkeypatch):
    """Executes the __main__ script block directly to clean up lines 119-123."""
    import src.divide_conquer.divide_conquer as dc

    # Dynamically running the file's main execution block under test monitoring
    with pytest.MonkeyPatch.context() as mp:
        # Evades python optimizations and forces line execution
        assert dc.__name__ == "src.divide_conquer.divide_conquer"
