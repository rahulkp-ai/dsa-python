"""
Module: linked_list.py  Topic: Linked Lists
Singly Linked List, Doubly Linked List, and utility functions.
"""
from __future__ import annotations
from typing import Optional, Generator
from dataclasses import dataclass, field


@dataclass
class ListNode:
    val: int
    next: Optional["ListNode"] = field(default=None, repr=False)


class SinglyLinkedList:
    """Singly Linked List with all standard operations. O(n) space."""
    def __init__(self) -> None:
        self.head: Optional[ListNode] = None
        self.size: int = 0

    def __len__(self) -> int: return self.size
    def __repr__(self) -> str: return " -> ".join(str(v) for v in self) + " -> None"
    def __iter__(self) -> Generator:
        cur = self.head
        while cur: yield cur.val; cur = cur.next

    def insert_head(self, val: int) -> None:
        """O(1)"""
        n = ListNode(val); n.next = self.head; self.head = n; self.size += 1

    def insert_tail(self, val: int) -> None:
        """O(n)"""
        n = ListNode(val)
        if not self.head: self.head = n
        else:
            cur = self.head
            while cur.next: cur = cur.next
            cur.next = n
        self.size += 1

    def delete(self, val: int) -> bool:
        """Delete first occurrence. O(n)"""
        if not self.head: return False
        if self.head.val == val: self.head = self.head.next; self.size -= 1; return True
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next; self.size -= 1; return True
            cur = cur.next
        return False

    def reverse(self) -> None:
        """Reverse in-place. O(n) time, O(1) space."""
        prev, cur = None, self.head
        while cur:
            nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
        self.head = prev

    def find_middle(self) -> Optional[ListNode]:
        """Floyd's middle. O(n)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next  # type: ignore
        return slow

    def has_cycle(self) -> bool:
        """Floyd's cycle detection. O(n) time, O(1) space."""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next  # type: ignore
            if slow == fast: return True
        return False

    def to_list(self) -> list: return list(self)

    @classmethod
    def from_list(cls, values: list) -> "SinglyLinkedList":
        ll = cls()
        for v in reversed(values): ll.insert_head(v)
        return ll


@dataclass
class DListNode:
    val: int
    prev: Optional["DListNode"] = field(default=None, repr=False)
    next: Optional["DListNode"] = field(default=None, repr=False)


class DoublyLinkedList:
    """Doubly Linked List with sentinel nodes. O(1) insert/delete by node."""
    def __init__(self) -> None:
        self.head = DListNode(0); self.tail = DListNode(0)
        self.head.next = self.tail; self.tail.prev = self.head
        self.size = 0

    def __len__(self) -> int: return self.size

    def insert_after(self, node: DListNode, val: int) -> DListNode:
        """O(1)"""
        n = DListNode(val)
        n.next = node.next; n.prev = node
        node.next.prev = n; node.next = n  # type: ignore
        self.size += 1; return n

    def insert_head(self, val: int) -> DListNode: return self.insert_after(self.head, val)
    def insert_tail(self, val: int) -> DListNode: return self.insert_after(self.tail.prev, val)  # type: ignore

    def delete_node(self, node: DListNode) -> None:
        """O(1)"""
        node.prev.next = node.next; node.next.prev = node.prev  # type: ignore
        self.size -= 1


def merge_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists. O(n+m) time, O(1) space."""
    dummy = ListNode(0); cur = dummy
    while l1 and l2:
        if l1.val <= l2.val: cur.next = l1; l1 = l1.next
        else: cur.next = l2; l2 = l2.next
        cur = cur.next  # type: ignore
    cur.next = l1 or l2
    return dummy.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove nth from end in one pass. O(L) time."""
    dummy = ListNode(0); dummy.next = head
    fast = slow = dummy
    for _ in range(n + 1): fast = fast.next  # type: ignore
    while fast: slow = slow.next; fast = fast.next  # type: ignore
    slow.next = slow.next.next  # type: ignore
    return dummy.next


def is_palindrome(head: Optional[ListNode]) -> bool:
    """Check palindrome. O(n) time, O(1) space."""
    if not head or not head.next: return True
    slow = fast = head
    while fast and fast.next: slow = slow.next; fast = fast.next.next  # type: ignore
    prev, cur = None, slow
    while cur: nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
    p1, p2 = head, prev
    while p2:
        if p1.val != p2.val: return False  # type: ignore
        p1 = p1.next; p2 = p2.next  # type: ignore
    return True


if __name__ == "__main__":
    ll = SinglyLinkedList.from_list([1,2,3,4,5])
    print(ll); ll.reverse(); print(ll)
    print("Middle:", ll.find_middle())
    print("Has cycle:", ll.has_cycle())
    l1 = SinglyLinkedList.from_list([1,2,4]).head
    l2 = SinglyLinkedList.from_list([1,3,4]).head
    merged = merge_sorted_lists(l1, l2)
    res = []
    while merged: res.append(merged.val); merged = merged.next
    print("Merged:", res)
    pal = SinglyLinkedList.from_list([1,2,2,1])
    print("Palindrome [1,2,2,1]:", is_palindrome(pal.head))
