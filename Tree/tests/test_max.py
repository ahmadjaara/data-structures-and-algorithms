from tree.tree_code import TNode, Binary_Search_Tree,BinaryTree
from tree.new_stack import Node,Stack
import pytest

def test_max_method1(tree):
    assert tree.max_value() == 4

def test_max_method2(tree2):
    assert tree2.max_value() == 11

def test_max_method_negative():
    node1 = TNode(-1)
    node2 = TNode(-2)
    node3 = TNode(0)
    node4 = TNode(-10)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root=node1
    assert tree.max_value() == 0

def test_max_method_root():
    node1 = TNode(-1)
    tree = BinaryTree()
    tree.root=node1
    assert tree.max_value() == -1

@pytest.fixture
def tree():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root=node1
    return tree
@pytest.fixture
def tree2():
    node1 = TNode(2)
    node2 = TNode(7)
    node3 = TNode(5)
    node4 = TNode(2)
    node5 = TNode(6)
    node6 = TNode(5)
    node7 = TNode(11)
    node8 = TNode(9)
    node9=TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node8
    node2.left=node4
    node2.right=node5
    node5.left=node6
    node5.right=node7
    node8.left=node9

    tree = BinaryTree()
    tree.root=node1
    return tree