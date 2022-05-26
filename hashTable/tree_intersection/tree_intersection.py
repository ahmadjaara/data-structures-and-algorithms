from hashtable.hash_table import *
from .tree_use import *

def intersection_tree(input1,input2):
    """
    take two binary tree as input and return the intersection between these two tree in a list
    input : two tree 
    output :list of common node between the trees 
    """
    list_inter=HashaTable()
    if input1.root==None or input2.root==None:
        return []
    def _walk(node,l):

        if node.left:

            _walk(node.left,l+"left")

        if node.right:
            _walk(node.right,l+"right")
        list_inter.set(l,str(node.value))

    _walk(input1.root,"root")
    _walk(input2.root,"root")
    list_common=[]
    for i in list_inter.keys():
        if len(list_inter[i][1])==2:
                if list_inter[i][1][0][1]==list_inter[i][1][1][1]:
                    list_common.append(list_inter[i][1][1][1])
        elif len(list_inter[i][1]) > 2:
                    dup = [x for j, x in enumerate(list_inter[i][1]) if x in list_inter[i][1][:j]]
    for i in dup:
        list_common.append(i[1])

    return list_common

if __name__ =="__main__":

    hgj=['3', '1', '5', '2', '4', '9']
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
    
    hgj312=['3', '1', '5', '2', '4', '9']
    node12 = TNode(100)
    node22 = TNode(5)
    node32 = TNode(4)
    node42 = TNode(3)
    node52 = TNode(2)
    node62 = TNode(5)
    node72 = TNode(11)
    node82 = TNode(9)
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

    print(intersection_tree(tree1,tree2))
