"""Unit tests for heap implementations."""
import pytest
from src.heaps.heap import MinHeap, MaxHeap, kth_largest, kth_smallest, merge_k_sorted, top_k_frequent, MedianFinder, task_scheduler

def test_min_heap():
    h = MinHeap()
    for v in [5,3,8,1,9]: h.push(v)
    r = [h.pop() for _ in range(len(h))]
    assert r == sorted([5,3,8,1,9])

def test_max_heap():
    h = MaxHeap()
    for v in [5,3,8,1,9]: h.push(v)
    r = [h.pop() for _ in range(len(h))]
    assert r == sorted([5,3,8,1,9],reverse=True)

def test_min_heap_peek():
    h=MinHeap(); h.push(5); h.push(2); h.push(8)
    assert h.peek==2

def test_heapify():
    h = MinHeap.heapify([5,3,8,1,9,2])
    assert h.pop()==1

def test_kth_largest(): assert kth_largest([3,2,1,5,6,4],2)==5
def test_kth_smallest(): assert kth_smallest([3,2,1,5,6,4],2)==2

def test_merge_k(): assert merge_k_sorted([[1,4,7],[2,5,8],[3,6,9]])==list(range(1,10))

def test_top_k(): assert top_k_frequent([1,1,1,2,2,3],2)==[1,2]

def test_median_odd():
    mf=MedianFinder()
    for v in [1,2,3]: mf.add_num(v)
    assert mf.find_median()==2.0

def test_median_even():
    mf=MedianFinder()
    for v in [1,2]: mf.add_num(v)
    assert mf.find_median()==1.5

def test_task_scheduler(): assert task_scheduler(["A","A","A","B","B","B"],2)==8
