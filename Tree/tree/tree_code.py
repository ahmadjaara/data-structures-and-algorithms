# from tree.queue123 import Queue ,Nodeq
# from tree.new_stack import Stack,Node



class Nodeq:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self) :
        self.front=None
        self.rear=None
    
    def enqueue (self,value):
        node = Nodeq(value)

        if not self.front :
            self.rear = node 
            self.front = node 
        
        else:  
            self.rear.next = node 
            self.rear = node 
    def dequeue(self) :

        if not self.front :
            return "queue is empty"
        
        temp= self.front
        self.front=self.front.next 
        temp.next=None
        
        return temp.value

    def is_empty(self):
        return self.front == None 



class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:

    def __init__(self):
        self.top=None

    def push(self, value):
        """
            push will add a new Node to the stack

            input: value
            output: None

        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        input: none
        doing: pop the top node from the stack 
        output: popped node's value
        """
        if self.is_empty():
            raise Exception("Stack is empty !")
        
        temp=self.top
        self.top=self.top.next
        temp.next=None
        
        return temp.value
        
        
    def is_empty(self):
        if self.top == None:
            return True 
        return False





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
   
    



    def odd_sum(self):

        odd_sum_var=[]
        def _walk(node):

            if node.value%2 !=0:
                odd_sum_var.append(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)

        return sum(odd_sum_var)

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
    
def file_compare_structure(tree1,tree2):
    def file_num(var):
        list_breadth=[]
        breadth=Queue()
        breadth.enqueue(var.root)
        sum=0

        while not breadth.is_empty():
            node_front=breadth.dequeue()
            list_breadth.append(node_front.value)
            # print(node_front.value)
            if node_front.left:
                breadth.enqueue(node_front.left)
            if node_front.right:
                breadth.enqueue(node_front.right)
            if node_front.left==None & node_front.right==None:
                sum+=1

        return sum

    
    tree1=file_num(tree1)
    tree2=file_num(tree2)
    return tree1==tree2

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
    print(tree135.odd_sum())




    nodenew2 = TNode("Folder")
    nodenew1 = TNode("Folder")
    nodenew3 = TNode("file")
    nodenew4 = TNode("file")
    nodenew5 = TNode("file")
    nodenew6 = TNode("Folder")
    nodenew7 = TNode("file")
    nodenew8 = TNode("Folder")
    nodenew9 = TNode("file")
    nodenew1.left = nodenew2
    nodenew1.right = nodenew3
    nodenew3.right = nodenew8
    nodenew2.left=nodenew4
    nodenew2.right=nodenew5
    nodenew5.left=nodenew6
    nodenew5.right=nodenew7
    nodenew8.left=nodenew9

    
    nodenewsecond2 = TNode("file")
    nodenewsecond1 = TNode("file")
    nodenewsecond3 = TNode("file")
    nodenewsecond4 = TNode("file")
    nodenewsecond5 = TNode("file")
    nodenewsecond6 = TNode("Folder")
    nodenewsecond7 = TNode("file")
    nodenewsecond8 = TNode("Folder")
    nodenewsecond9 = TNode("file")
    nodenewsecond1.left = nodenewsecond2
    nodenewsecond1.right = nodenewsecond3
    nodenewsecond3.right = nodenewsecond8
    nodenewsecond2.left=nodenewsecond4
    nodenewsecond2.right=nodenewsecond5
    nodenewsecond5.left=nodenewsecond6
    nodenewsecond5.right=nodenewsecond7
    nodenewsecond8.left=nodenewsecond9

    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.root=nodenew1
    tree2.root=nodenew1

    print(file_compare_structure(tree1,tree2))