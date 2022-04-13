
from tree.queue import Queue
from tree.new_stack import Stack


class TNode:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:

    def __init__(self):
        self.root=None

    def pre_order(self):
        """
        Input: None
        doing: traverse a tree
        output: print values of the nodes of the tree Pre-order: root >> left >> right
        """
        list_pre=[]
        def _walk(node):
            
            #print(str(node.value) + "->", end='')
            list_pre.append(str(node.value))

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        
        _walk(self.root)
        
        return list_pre

        # stack = Stack()
        # current = self.root

        # stack.push(current)

        # while not stack.is_empty():
        #     current = stack.pop()
        #     print(current.value)

        #     if current.right:
        #         stack.push(current.right)

        #     if current.left:
        #         stack.push(current.left)
    def in_order(self):
        """
        Input: None
        doing: traverse a tree
        output: print values of the nodes of the tree In-order: left >> root >> right
        """
        list_in_or=[]
        def _walk(node):
            
            
            if node.left:
                _walk(node.left)
            #print(str(node.value) + "->", end='')
            list_in_or.append(str(node.value))
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return list_in_or
    def post_order(self):
        """
        Input: None
        doing: traverse a tree
        output: print values of the nodes of the tree **Post-order: left >> right >> root
        """
        list_post_or=[]
        def _walk(node):
            
            if node.left:
                _walk(node.left)
            
            if node.right:
                _walk(node.right)
            list_post_or.append(str(node.value))
            #print(str(node.value) + "->", end='')
        _walk(self.root)
        return list_post_or
        
    def max_value(self):
        """
        Find the maximum value stored in the tree
        Arguments: none
        Returns: number
        """
        stack = Stack()
        current = self.root
        maxv=current.value

        stack.push(current)

        while not stack.is_empty():
            current = stack.pop()
            if maxv <= current.value:
                maxv=current.value
            # print(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)
        return maxv
    def breadth_first(self,tree):
        """
        Traverse the input tree using a Breadth-first approach 
        Arguments: tree
        Return: list of all values in the tree, in the order they were encountered by level from left to right
        """
        list_breadth=[]
        breadth=Queue()
        breadth.enqueue(tree.root)

        while not breadth.is_empty():
            node_front=breadth.dequeue()
            list_breadth.append(node_front.value)
            # print(node_front.value)
            if node_front.left:
                breadth.enqueue(node_front.left)
            if node_front.right:
                breadth.enqueue(node_front.right)
        return list_breadth

class Binary_Search_Tree(BinaryTree):
    
    def add(self,value):
        """
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        """
        # def add(self, value): #function to add data items to the tree
        # check if there is no root
        node=TNode(value)
        if self.root == None:
            self.root = node
            return
        else:
            ptr_node = self.root
            while True:
                if value < ptr_node.value:
                
                    if ptr_node.left == None:
                        ptr_node.left = node
                        return 
                    else:
                        ptr_node = ptr_node.left
                elif value > ptr_node.value:
                    
                    if ptr_node.right == None:
                        ptr_node.right = node
                        return
                    else:
                        ptr_node = ptr_node.right

    def contains(self,value):
        """
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        ptr_node = self.root
        while True:
            if ptr_node == None:
                return False
            if ptr_node.value == value:
                return True
            elif value < ptr_node.value:
                ptr_node = ptr_node.left
            else:
                ptr_node = ptr_node.right
    


if __name__=="__main__":

    # node1 = TNode(1)
    # node2 = TNode(2)
    # node3 = TNode(3)
    # node4 = TNode(4)
    # node1.left = node2
    # node1.right = node3
    # node3.right = node4

    # tree = Binary_Search_Tree()
    # tree.root = node1

    
    # tree.add(6)
    # print(tree.contains(4))
    # print(tree.post_order())
    # print("1\n2\n3\n4")
    # print(tree.root.left.value)
    # print(tree.max_value())

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

    tree135 = BinaryTree()
    tree135.root=node1
    print(tree135.breadth_first(tree135))
    print(tree135.max_value())