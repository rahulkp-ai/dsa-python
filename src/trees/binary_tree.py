"""
Module: binary_tree.py  Topic: Trees
Binary Tree, BST, traversals, height, diameter, LCA, serialize/deserialize.
"""
from __future__ import annotations
from typing import Optional, List
from collections import deque
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = field(default=None, repr=False)
    right: Optional[TreeNode] = field(default=None, repr=False)


def inorder(root: Optional[TreeNode]) -> List[int]:
    """Left-Root-Right. O(n) time. BST gives sorted order."""
    res: List[int] = []
    def dfs(n: Optional[TreeNode]) -> None:
        if n: dfs(n.left); res.append(n.val); dfs(n.right)
    dfs(root); return res

def preorder(root: Optional[TreeNode]) -> List[int]:
    """Root-Left-Right. O(n)."""
    res: List[int] = []
    def dfs(n: Optional[TreeNode]) -> None:
        if n: res.append(n.val); dfs(n.left); dfs(n.right)
    dfs(root); return res

def postorder(root: Optional[TreeNode]) -> List[int]:
    """Left-Right-Root. O(n)."""
    res: List[int] = []
    def dfs(n: Optional[TreeNode]) -> None:
        if n: dfs(n.left); dfs(n.right); res.append(n.val)
    dfs(root); return res

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """BFS level-by-level. O(n) time, O(n) space."""
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft(); level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res

def height(root: Optional[TreeNode]) -> int:
    """Max depth (edges). O(n)."""
    if not root: return -1
    return 1 + max(height(root.left), height(root.right))

def diameter(root: Optional[TreeNode]) -> int:
    """Longest path between any two nodes. O(n)."""
    best = [0]
    def dfs(n: Optional[TreeNode]) -> int:
        if not n: return 0
        l, r = dfs(n.left), dfs(n.right)
        best[0] = max(best[0], l + r)
        return 1 + max(l, r)
    dfs(root); return best[0]

def is_balanced(root: Optional[TreeNode]) -> bool:
    """Height-balanced check. O(n)."""
    def chk(n: Optional[TreeNode]) -> int:
        if not n: return 0
        l = chk(n.left); r = chk(n.right)
        if l == -1 or r == -1 or abs(l - r) > 1: return -1
        return 1 + max(l, r)
    return chk(root) != -1

def is_symmetric(root: Optional[TreeNode]) -> bool:
    """Mirror check. O(n)."""
    def mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b: return True
        if not a or not b: return False
        return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root, root)

def lca(root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
    """Lowest Common Ancestor. O(n)."""
    if not root or root.val in (p, q): return root
    left = lca(root.left, p, q); right = lca(root.right, p, q)
    return root if left and right else left or right

def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """Root-to-leaf path with given sum. O(n)."""
    if not root: return False
    if not root.left and not root.right: return root.val == target
    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val)

def serialize(root: Optional[TreeNode]) -> str:
    """BFS serialization. O(n)."""
    if not root: return ""
    res, q = [], deque([root])
    while q:
        n = q.popleft()
        if n: res.append(str(n.val)); q.append(n.left); q.append(n.right)  # type: ignore
        else: res.append("null")
    while res and res[-1] == "null": res.pop()
    return ",".join(res)

def deserialize(data: str) -> Optional[TreeNode]:
    """BFS deserialization. O(n)."""
    if not data: return None
    vals = data.split(","); root = TreeNode(int(vals[0])); q = deque([root]); i = 1
    while q and i < len(vals):
        n = q.popleft()
        if i < len(vals) and vals[i] != "null":
            n.left = TreeNode(int(vals[i])); q.append(n.left)
        i += 1
        if i < len(vals) and vals[i] != "null":
            n.right = TreeNode(int(vals[i])); q.append(n.right)
        i += 1
    return root


class BST:
    """Binary Search Tree with insert, search, delete, validation."""
    def __init__(self) -> None: self.root: Optional[TreeNode] = None

    def insert(self, val: int) -> None:
        def _ins(n: Optional[TreeNode], v: int) -> TreeNode:
            if not n: return TreeNode(v)
            if v < n.val: n.left = _ins(n.left, v)
            elif v > n.val: n.right = _ins(n.right, v)
            return n
        self.root = _ins(self.root, val)

    def search(self, val: int) -> bool:
        n = self.root
        while n:
            if val == n.val: return True
            n = n.left if val < n.val else n.right
        return False

    def delete(self, val: int) -> None:
        def _del(n: Optional[TreeNode], v: int) -> Optional[TreeNode]:
            if not n: return None
            if v < n.val: n.left = _del(n.left, v)
            elif v > n.val: n.right = _del(n.right, v)
            else:
                if not n.left: return n.right
                if not n.right: return n.left
                mn = n.right
                while mn.left: mn = mn.left
                n.val = mn.val; n.right = _del(n.right, mn.val)
            return n
        self.root = _del(self.root, val)

    def is_valid(self) -> bool:
        def chk(n: Optional[TreeNode], lo: float, hi: float) -> bool:
            if not n: return True
            if not (lo < n.val < hi): return False
            return chk(n.left, lo, n.val) and chk(n.right, n.val, hi)
        return chk(self.root, float("-inf"), float("inf"))

    def inorder(self) -> List[int]: return inorder(self.root)


if __name__ == "__main__":
    bst = BST()
    for v in [4,2,6,1,3,5,7]: bst.insert(v)
    print("Inorder:", bst.inorder())
    print("Valid BST:", bst.is_valid())
    r = bst.root
    print("Height:", height(r), "Diameter:", diameter(r))
    print("Level order:", level_order(r))
    print("Balanced:", is_balanced(r), "Symmetric:", is_symmetric(r))
    print("LCA(1,3):", lca(r, 1, 3))
    s = serialize(r); print("Serial:", s)
    print("Restore inorder:", inorder(deserialize(s)))
