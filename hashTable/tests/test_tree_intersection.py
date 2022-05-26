from tree_intersection.tree_intersection import *
import pytest
def test_intersection_tree(tree):
    assert intersection_tree(tree[0],tree[1]) == ['3', '5', '2', '4', '9', '11']

def test_intersection_tree_nothing_match(treenothing_match):
    assert intersection_tree(treenothing_match[0],treenothing_match[1]) == []

def test_intersection_empty_tree(empty_tree):
    assert intersection_tree(empty_tree[0],empty_tree[1]) == []


@pytest.fixture
def tree():
    node1 = TNode(10)
    node2 = TNode(5)#common
    node3 = TNode(4)#common
    node4 = TNode(3)#common
    node5 = TNode(2)#common
    node6 = TNode(1)
    node7 = TNode(11)#common
    node8 = TNode(9)#common
    node9 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node8
    node2.left=node4
    node2.right=node5
    node5.left=node6
    node5.right=node7
    node8.left=node9

    tree1 = BinaryTree()
    tree1.root=node1
    # ['3', '5', '2', '4', '9', '11']
    node12 = TNode(100)
    node22 = TNode(5)#common
    node32 = TNode(4)#common
    node42 = TNode(3)#common
    node52 = TNode(2)#common
    node62 = TNode(5)
    node72 = TNode(11)#common
    node82 = TNode(9)#common
    node92 = TNode(12)
    node12.left = node22
    node12.right = node32
    node32.right = node82
    node22.left=node42
    node22.right=node52
    node52.left=node62
    node52.right=node72
    node82.left=node92

    tree2 = BinaryTree()
    tree2.root=node12

    return [tree1,tree2]

@pytest.fixture
def treenothing_match():
    node1 = TNode(10)
    node2 = TNode(5)
    node3 = TNode(4)
    node4 = TNode(3)
    node5 = TNode(2)
    node6 = TNode(1)
    node7 = TNode(11)
    node8 = TNode(9)
    node9 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node8
    node2.left=node4
    node2.right=node5
    node5.left=node6
    node5.right=node7
    node8.left=node9

    tree1 = BinaryTree()
    tree1.root=node1
    # ['3', '5', '2', '4', '9', '11']
    node12 = TNode(-100)
    node22 = TNode(-5)
    node32 = TNode(-4)
    node42 = TNode(-3)
    node52 = TNode(-2)
    node62 = TNode(-5)
    node72 = TNode(-11)
    node82 = TNode(-9)
    node92 = TNode(-12)
    node12.left = node22
    node12.right = node32
    node32.right = node82
    node22.left=node42
    node22.right=node52
    node52.left=node62
    node52.right=node72
    node82.left=node92

    tree2 = BinaryTree()
    tree2.root=node12

    return [tree1,tree2]
@pytest.fixture
def empty_tree():
    node1 = TNode(10)
    node2 = TNode(5)
    node3 = TNode(4)
    node4 = TNode(3)
    node5 = TNode(2)
    node6 = TNode(1)
    node7 = TNode(11)
    node8 = TNode(9)
    node9 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node8
    node2.left=node4
    node2.right=node5
    node5.left=node6
    node5.right=node7
    node8.left=node9

    tree1 = BinaryTree()
    tree1.root=node1
    

    tree2 = BinaryTree()
    tree2.root=None

    return [tree1,tree2]