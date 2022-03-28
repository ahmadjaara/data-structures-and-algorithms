from stackandqueue.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.stack1 =Stack()
        self.stack2=Stack()
    def enqueue(self,value):
        """add an element at the end of queue
        input value to add in the queue
    
        """

        while not self.stack1.is_empty():
            top=self.stack1.pop()
            self.stack2.push(top)
        
        self.stack1.push(value)
        
        while not self.stack2.is_empty():
            top=self.stack2.pop()
            self.stack1.push(top)
            
        
   
    def dequeue(self) :
        """
        delete first element enter queue
        output the deleted element form the queue
        """
        if self.stack1.is_empty():
            return("queue is empty")

        return self.stack1.pop()

if __name__=="__main__":
    queue = PseudoQueue()
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(2)
    # print( queue.dequeue(),queue.dequeue(),queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
