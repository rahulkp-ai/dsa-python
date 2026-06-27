"""
Module: stack_queue.py  Topic: Stacks & Queues
Stack, MinStack, Queue, Monotonic Stack.
Valid Parentheses, Daily Temperatures, Largest Rectangle, Sliding Window Max, Evaluate RPN.
"""

from collections import deque
from typing import List, Optional


class Stack:
    """Stack (LIFO). All ops O(1)."""

    def __init__(self) -> None:
        self._d: List = []

    def push(self, v: object) -> None:
        self._d.append(v)

    def pop(self) -> Optional[object]:
        return self._d.pop() if self._d else None

    def peek(self) -> Optional[object]:
        return self._d[-1] if self._d else None

    def is_empty(self) -> bool:
        return len(self._d) == 0

    def __len__(self) -> int:
        return len(self._d)


class MinStack:
    """Stack with O(1) get_min.
    >>> ms=MinStack(); ms.push(3); ms.push(1); ms.push(2); ms.get_min()
    1
    """

    def __init__(self) -> None:
        self.s: List[int] = []
        self.mn: List[int] = []

    def push(self, v: int) -> None:
        self.s.append(v)
        self.mn.append(v if not self.mn else min(v, self.mn[-1]))

    def pop(self) -> None:
        self.s.pop()
        self.mn.pop()

    def top(self) -> int:
        return self.s[-1]

    def get_min(self) -> int:
        return self.mn[-1]


class Queue:
    """Queue (FIFO). All ops O(1)."""

    def __init__(self) -> None:
        self._d: deque = deque()

    def enqueue(self, v: object) -> None:
        self._d.append(v)

    def dequeue(self) -> Optional[object]:
        return self._d.popleft() if self._d else None

    def front(self) -> Optional[object]:
        return self._d[0] if self._d else None

    def is_empty(self) -> bool:
        return len(self._d) == 0

    def __len__(self) -> int:
        return len(self._d)


class QueueFromStacks:
    """Implement queue using two stacks. Amortised O(1) per op."""

    def __init__(self) -> None:
        self.s1: List = []
        self.s2: List = []

    def push(self, v: object) -> None:
        self.s1.append(v)

    def pop(self) -> Optional[object]:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

    def peek(self) -> Optional[object]:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1] if self.s2 else None


def is_valid_parentheses(s: str) -> bool:
    """Balanced brackets check. O(n) time, O(n) space.
    >>> is_valid_parentheses("()[]{}")
    True
    """
    stack: List[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in pairs:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0


def daily_temperatures(temps: List[int]) -> List[int]:
    """Days until warmer temp (monotonic stack). O(n).
    >>> daily_temperatures([73,74,75,71,69,72,76,73])
    [1, 1, 4, 2, 1, 1, 0, 0]
    """
    res = [0] * len(temps)
    stack: List[int] = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res


def largest_rectangle_histogram(heights: List[int]) -> int:
    """Largest rectangle in histogram. O(n).
    >>> largest_rectangle_histogram([2,1,5,6,2,3])
    10
    """
    stack: List[tuple] = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        start = i
        while stack and stack[-1][1] > h:
            j, ht = stack.pop()
            max_area = max(max_area, ht * (i - j))
            start = j
        stack.append((start, h))
    return max_area


def sliding_window_max(nums: List[int], k: int) -> List[int]:
    """Max in every sliding window of size k. O(n).
    >>> sliding_window_max([1,3,-1,-3,5,3,6,7], 3)
    [3, 3, 5, 5, 6, 7]
    """
    dq: deque = deque()
    res: List[int] = []
    for i, n in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


def eval_rpn(tokens: List[str]) -> int:
    """Evaluate Reverse Polish Notation. O(n).
    >>> eval_rpn(["2","1","+","3","*"])
    9
    """
    stack: List[int] = []
    for t in tokens:
        if t in "+-*/":
            b, a = stack.pop(), stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]


def next_greater_element(nums: List[int]) -> List[int]:
    """Next greater element for each. O(n).
    >>> next_greater_element([2,1,2,4,3])
    [4, 2, 4, -1, -1]
    """
    res = [-1] * len(nums)
    stack: List[int] = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res


if __name__ == "__main__":
    ms = MinStack()
    for v in [5, 3, 7, 2]:
        ms.push(v)
    print("Min:", ms.get_min())
    print("Valid '()[]{}':", is_valid_parentheses("()[]{}"))
    print("Daily temps:", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("Histogram area:", largest_rectangle_histogram([2, 1, 5, 6, 2, 3]))
    print("Sliding max:", sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("RPN:", eval_rpn(["2", "1", "+", "3", "*"]))
    print("Next greater:", next_greater_element([2, 1, 2, 4, 3]))
