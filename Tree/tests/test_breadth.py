from tree.tree import TNode, Binary_Search_Tree,BinaryTree
import pytest

def test_breadth_method1(tree2):

    assert tree2.breadth_first(tree2) == [2, 7, 5, 2, 6, 9, 5, 11, 4]

def test_breadth_method2():
    node1 = TNode(2)
    tree = BinaryTree()
    tree.root=node1
    assert tree.breadth_first(tree) == [2]

def test_breadth_method3():
    node1 = TNode(1)
    node2 = TNode("string")
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4

    tree = BinaryTree()
    tree.root = node1
    assert tree.breadth_first(tree) == [1,"string",3,4]

def test_breadth_method_left_only():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node2.left = node3
    node3.left = node4

    tree = BinaryTree()
    tree.root = node1
    assert tree.breadth_first(tree) == [1,2,3,4]

def test_breadth_method_right_only():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.right = node2
    node2.right = node3
    node3.right = node4

    tree = BinaryTree()
    tree.root = node1
    assert tree.breadth_first(tree) == [1,2,3,4]


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
    node9 = TNode(4)

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