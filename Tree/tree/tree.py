
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
        
        def _walk(node):
            
            print(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        
        _walk(self.root)
        
    

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
        def _walk(node):
            

            if node.left:
                _walk(node.left)
            print(node.value)
            if node.right:
                _walk(node.right)

        _walk(self.root)
    def post_order(self):
        """
        Input: None
        doing: traverse a tree
        output: print values of the nodes of the tree **Post-order: left >> right >> root
        """
        def _walk(node):
            
            if node.left:
                _walk(node.left)
            
            if node.right:
                _walk(node.right)
            
            print(node.value)
        _walk(self.root)
        

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
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4

    tree = Binary_Search_Tree()
    tree.root = node1

    
    # tree.add(6)
    # print(tree.contains(4))
    print(tree.post_order())
    # print("1\n2\n3\n4")
    # print(tree.root.left.value)
      