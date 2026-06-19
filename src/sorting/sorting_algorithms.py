"""
Module: sorting_algorithms.py
Topic: Sorting

All major sorting algorithms with type hints, docstrings, complexity analysis.

Algorithms:
    Bubble Sort     O(n²)     / O(1)
    Insertion Sort  O(n²)     / O(1)
    Selection Sort  O(n²)     / O(1)
    Merge Sort      O(n logn) / O(n)
    Quick Sort      O(n logn) / O(logn)
    Heap Sort       O(n logn) / O(1)
    Counting Sort   O(n+k)    / O(k)
    Radix Sort      O(nk)     / O(n+k)
"""
from typing import List, Optional
import random


def bubble_sort(arr: List[int]) -> List[int]:
    """Bubble Sort with early-exit optimisation. O(n²) time, O(1) space."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """Insertion Sort. O(n²) worst, O(n) best. O(1) space. Stable."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """Selection Sort. O(n²) always. O(1) space. Not stable."""
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """Merge Sort (Divide & Conquer). O(n logn) time, O(n) space. Stable."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[int]) -> List[int]:
    """Quick Sort. O(n logn) avg, O(n²) worst. O(logn) space."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def heap_sort(arr: List[int]) -> List[int]:
    """Heap Sort. O(n logn) always. O(1) space. Not stable."""
    arr = arr.copy()
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    return arr


def _heapify(arr: List[int], n: int, i: int) -> None:
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


def counting_sort(arr: List[int]) -> List[int]:
    """Counting Sort. O(n+k) time, O(k) space. Non-negative integers only."""
    if not arr: return []
    if min(arr) < 0:
        raise ValueError("Counting sort requires non-negative integers.")
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr: count[num] += 1
    result = []
    for i, freq in enumerate(count): result.extend([i] * freq)
    return result


def radix_sort(arr: List[int]) -> List[int]:
    """Radix Sort (LSD). O(nk) time, O(n+k) space."""
    if not arr: return []
    arr = arr.copy()
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_digit(arr: List[int], exp: int) -> List[int]:
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for num in arr: count[(num // exp) % 10] += 1
    for i in range(1, 10): count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1
    return output


if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original:       {sample}")
    print(f"Bubble Sort:    {bubble_sort(sample)}")
    print(f"Insertion Sort: {insertion_sort(sample)}")
    print(f"Selection Sort: {selection_sort(sample)}")
    print(f"Merge Sort:     {merge_sort(sample)}")
    print(f"Quick Sort:     {quick_sort(sample)}")
    print(f"Heap Sort:      {heap_sort(sample)}")
    print(f"Counting Sort:  {counting_sort(sample)}")
    print(f"Radix Sort:     {radix_sort(sample)}")
