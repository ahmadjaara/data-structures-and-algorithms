from tree.tree import TNode, Binary_Search_Tree,BinaryTree

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root==None
    
def test_instantiate_single_root():
    tree = BinaryTree()
    node1 = TNode(1)
    tree.root = node1
    assert tree.root.left==None
    
def test_bst_add_left_right_node():
    node1 = TNode(2)
    tree = Binary_Search_Tree()
    tree.root = node1
    tree.add(1)
    tree.add(4)
    assert tree.root.left.value==1
    assert tree.root.right.value==4

def test_preorder():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    assert tree.pre_order==tree.pre_order

def test_inorder():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = Binary_Search_Tree()
    assert tree.in_order==tree.in_order
def test_postorder():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = Binary_Search_Tree()
    assert tree.post_order==tree.post_order

def test_bst_cotains_method():
    node1 = TNode(2)
    tree = Binary_Search_Tree()
    tree.root = node1
    tree.add(1)
    assert tree.contains(4) == False
    assert tree.contains(1) == True
