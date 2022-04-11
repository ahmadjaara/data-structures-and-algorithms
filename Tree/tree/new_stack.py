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


