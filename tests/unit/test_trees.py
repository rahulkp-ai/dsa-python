"""Unit tests for binary tree algorithms."""


from src.trees.binary_tree import (
    BST,
    TreeNode,
    deserialize,
    diameter,
    has_path_sum,
    height,
    inorder,
    is_balanced,
    is_symmetric,
    lca,
    level_order,
    postorder,
    preorder,
    serialize,
)


def make_bst(*vals):
    t = BST()
    for v in vals:
        t.insert(v)
    return t


def test_bst_inorder():
    assert make_bst(4, 2, 6, 1, 3, 5, 7).inorder() == [1, 2, 3, 4, 5, 6, 7]


def test_bst_search():
    t = make_bst(4, 2, 6)
    assert t.search(2) and not t.search(9)


def test_bst_delete():
    t = make_bst(4, 2, 6, 1, 3)
    t.delete(2)
    assert 2 not in t.inorder()


def test_bst_valid():
    assert make_bst(4, 2, 6).is_valid()


def test_preorder():
    assert preorder(make_bst(4, 2, 6, 1, 3, 5, 7).root)[0] == 4


def test_postorder():
    assert postorder(make_bst(4, 2, 6).root)[-1] == 4


def test_level_order():
    assert level_order(make_bst(4, 2, 6).root) == [[4], [2, 6]]


def test_height():
    assert height(make_bst(4, 2, 6, 1, 3, 5, 7).root) == 2


def test_height_empty():
    assert height(None) == -1


def test_height_single():
    assert height(TreeNode(1)) == 0


def test_diameter():
    assert diameter(make_bst(4, 2, 6, 1, 3, 5, 7).root) >= 4


def test_balanced():
    assert is_balanced(make_bst(4, 2, 6).root)


# def test_symmetric(): assert is_symmetric(make_bst(2,1,3).root)
def test_symmetric():
    # 1. Test a truly symmetric tree:
    #      1
    #     / \
    #    2   2
    #   /     \
    #  3       3
    sym_tree = TreeNode(1)
    sym_tree.left = TreeNode(2, left=TreeNode(3))
    sym_tree.right = TreeNode(2, right=TreeNode(3))
    assert is_symmetric(sym_tree) == True

    # 2. Test an asymmetric tree (like your BST example):
    asym_tree = TreeNode(2)
    asym_tree.left = TreeNode(1)
    asym_tree.right = TreeNode(3)
    assert is_symmetric(asym_tree) == False

    # 3. Test an empty tree (base case)
    assert is_symmetric(None) == True


def test_lca():
    t = make_bst(4, 2, 6, 1, 3, 5, 7)
    assert lca(t.root, 1, 3).val == 2


def test_has_path_sum():
    t = make_bst(4, 2, 6, 1, 3)
    assert has_path_sum(t.root, 7)  # 4->2->1
    assert not has_path_sum(t.root, 100)


def test_serialize_deserialize():
    t = make_bst(4, 2, 6, 1, 3)
    s = serialize(t.root)
    assert inorder(deserialize(s)) == inorder(t.root)


def test_serialize_empty():
    assert serialize(None) == ""


def test_deserialize_empty():
    assert deserialize("") is None
