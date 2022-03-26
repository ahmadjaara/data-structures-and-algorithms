class Node :
  def __init__(self,value):
    self.value=value
    self.next=None 

class Stack :
  def __init__(self,node=None):
    self.top = node 

  def push(self,value):
    node = Node(value)
    node.next = self.top
    self.top = node 

  def pop(self) :
    if self.top ==None:
      return "empty stack"
    
    temp = self.top
    self.top = self.top.next
    temp.next= None
    return temp.value

  def peek(self):
    if self.top == None:
      return "empty stack"
    
    return self.top.value
   
  def is_empty(self):
    """method to check if stack is impty
     return boolean
    """
    return self.top == None 
     # return self.top
if __name__=="__main__":
  p = Stack()
  print(p.top)