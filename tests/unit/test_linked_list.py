
from src.linked_list.linked_list import (
    DoublyLinkedList,
    SinglyLinkedList,
    is_palindrome,
    merge_sorted_lists,
    remove_nth_from_end,
)


def make_ll(*vals):
    return SinglyLinkedList.from_list(list(vals))


# =====================================================================
# Singly Linked List Tests
# =====================================================================


def test_insert_tail():
    # Test inserting to an empty list
    ll = SinglyLinkedList()
    ll.insert_tail(1)
    assert ll.to_list() == [1]

    # Test inserting to a non-empty list
    ll.insert_tail(2)
    ll.insert_tail(3)
    assert ll.to_list() == [1, 2, 3]
    assert len(ll) == 3


def test_insert_head():
    ll = SinglyLinkedList()
    for v in [3, 2, 1]:
        ll.insert_head(v)
    assert ll.to_list() == [1, 2, 3]


def test_repr():
    ll = make_ll(1, 2, 3)
    assert repr(ll) == "1 -> 2 -> 3 -> None"


def test_delete():
    ll = make_ll(1, 2, 3, 4, 5)
    ll.delete(3)
    assert ll.to_list() == [1, 2, 4, 5]


def test_delete_head():
    ll = make_ll(1, 2, 3)
    assert ll.delete(1)
    assert ll.to_list() == [2, 3]


def test_delete_missing():
    ll = make_ll(1, 2, 3)
    assert not ll.delete(99)


def test_delete_empty():
    ll = SinglyLinkedList()
    assert not ll.delete(5)


def test_reverse():
    ll = make_ll(1, 2, 3, 4, 5)
    ll.reverse()
    assert ll.to_list() == [5, 4, 3, 2, 1]


def test_find_middle():
    ll = make_ll(1, 2, 3, 4, 5)
    assert ll.find_middle().val == 3

    # Even length check
    ll2 = make_ll(1, 2, 3, 4)
    assert ll2.find_middle().val == 3


def test_has_cycle_false():
    ll = make_ll(1, 2, 3, 4, 5)
    assert not ll.has_cycle()


def test_has_cycle_true():
    ll = make_ll(1, 2, 3)
    # Form a cycle: 3 -> 2
    ll.head.next.next.next = ll.head.next
    assert ll.has_cycle()


# =====================================================================
# Doubly Linked List Tests (Covers lines 94-96, 102-105, 112-113)
# =====================================================================


def test_doubly_linked_list_operations():
    dll = DoublyLinkedList()
    assert len(dll) == 0

    # Test insert_head
    node1 = dll.insert_head(10)
    assert len(dll) == 1
    assert dll.head.next.val == 10

    # Test insert_tail
    node2 = dll.insert_tail(20)
    assert len(dll) == 2
    assert dll.tail.prev.val == 20

    # Test insert_after
    node3 = dll.insert_after(node1, 15)
    assert len(dll) == 3
    assert node1.next.val == 15
    assert node3.prev.val == 10

    # Test delete_node
    dll.delete_node(node3)
    assert len(dll) == 2
    assert node1.next.val == 20
    assert node2.prev.val == 10


# =====================================================================
# Utility Functions Tests
# =====================================================================


def test_merge_sorted():
    l1 = make_ll(1, 2, 4).head
    l2 = make_ll(1, 3, 4).head
    merged = merge_sorted_lists(l1, l2)
    res = []
    while merged:
        res.append(merged.val)
        merged = merged.next
    assert res == [1, 1, 2, 3, 4, 4]


def test_remove_nth():
    ll = make_ll(1, 2, 3, 4, 5)
    head = remove_nth_from_end(ll.head, 2)
    res = []
    while head:
        res.append(head.val)
        head = head.next
    assert res == [1, 2, 3, 5]


def test_palindrome_true():
    assert is_palindrome(make_ll(1, 2, 2, 1).head)


def test_palindrome_false():
    assert not is_palindrome(make_ll(1, 2, 3).head)


def test_palindrome_single():
    assert is_palindrome(make_ll(1).head)


def test_palindrome_empty():
    assert is_palindrome(None)


# =====================================================================
# Main Block Coverage Execution
# =====================================================================


def test_main_block_execution(capsys):
    import runpy

    # Executes the file as if it ran directly from the CLI
    runpy.run_path("src/linked_list/linked_list.py", run_name="__main__")
    captured = capsys.readouterr()
    assert "Middle:" in captured.out
    assert "Merged:" in captured.out
