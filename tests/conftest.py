"""Pytest configuration and shared fixtures."""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


@pytest.fixture
def small_sorted():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def small_unsorted():
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def single_element():
    return [42]


@pytest.fixture
def with_duplicates():
    return [3, 3, 1, 1, 2, 2]


@pytest.fixture
def with_negatives():
    return [-3, 1, -1, 2, 0]


@pytest.fixture
def sample_graph():
    return {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}


@pytest.fixture
def sample_weighted_graph():
    return {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}


@pytest.fixture
def sample_grid():
    return [["1", "1", "0"], ["1", "1", "0"], ["0", "0", "1"]]
