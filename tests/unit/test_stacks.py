"""Unit tests for stacks and queues."""
import pytest
from src.stacks_queues.stack_queue import (
    Stack, MinStack, Queue, is_valid_parentheses,
    daily_temperatures, largest_rectangle_histogram,
    sliding_window_max, eval_rpn, next_greater_element
)

def test_stack():
    s=Stack(); s.push(1); s.push(2); s.push(3)
    assert s.pop()==3 and s.peek()==2 and len(s)==2

def test_min_stack():
    ms=MinStack()
    for v in [5,3,7,2,8]: ms.push(v)
    assert ms.get_min()==2; ms.pop(); ms.pop()
    assert ms.get_min()==3

def test_queue():
    q=Queue(); q.enqueue(1); q.enqueue(2); q.enqueue(3)
    assert q.dequeue()==1 and q.front()==2

def test_valid_parens():
    assert is_valid_parentheses("()[]{}") and is_valid_parentheses("([])")
    assert not is_valid_parentheses("(]") and not is_valid_parentheses("([)]")

def test_daily_temps():
    assert daily_temperatures([73,74,75,71,69,72,76,73])==[1,1,4,2,1,1,0,0]

def test_histogram(): assert largest_rectangle_histogram([2,1,5,6,2,3])==10
def test_histogram_single(): assert largest_rectangle_histogram([5])==5

def test_sliding_max(): assert sliding_window_max([1,3,-1,-3,5,3,6,7],3)==[3,3,5,5,6,7]

def test_rpn(): assert eval_rpn(["2","1","+","3","*"])==9
def test_rpn_div(): assert eval_rpn(["4","13","5","/","+"])==6

def test_next_greater(): assert next_greater_element([2,1,2,4,3])==[4,2,4,-1,-1]
