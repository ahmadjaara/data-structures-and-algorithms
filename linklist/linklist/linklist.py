

class Node:
    """
    Node class create node which has two variable the value ==data
    and the pointer to the next node == next 
    """
    def __init__(self,data):
        self.data=data
        self.next= None
        

class Linklist:
    """
    LinkedList class create an empty Linked List 
    it contain a constructer for the head 
    a method to insert node at the begining of the Linked List "insert_begining"
    a method to search for element in the linkedlist and return boolean 
    a method to display all the data inside the linked list which call display 
    and a method to   Returns: a string representing all the values in the Linked List, formatted as:
    "{ a } -> { b } -> { c } -> NULL"
    """
    def __init__(self):
        #constructer for the linked list 
        self.head=None

    # def __str__ (self):
    #     return "create empty linked list "+"head==>"+f"{self.head}"


    def insert_begining(self,data):
        """
        Arguments: data
        Adds a new node with value to the head of the list with an O(1) Time performance.

        """
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    
    def search_ele(self,x):
        """
            Arguments: value to search for it inside the linklist 
            Returns: Boolean
            Indicates whether that value exists as a Node  value somewhere within the list.
        """
        temp =self.head
        is_found=False
        while temp:
            if temp.data==x:
                is_found=True
            temp=temp.next
        
        return is_found

    def display(self):
        """
        its a method to print the collecation for all the element inside the linked list 
        """
        if self.head is None:
           print("linked list is empty")
        
        else:
            linklist_all=""
            temp = self.head
            while temp:
                linklist_all+= temp.data+" -->"
                temp = temp.next
            linklist_all+="None"
            return linklist_all

    def to_string(self):
        """
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        string_linklist=" "
        if self.head is None:
            print("linked list is empty")  
        else:
            temp = self.head
            while temp:
                string_linklist+="{{{0}}}".format(temp.data) +" -->"+" "
                temp = temp.next
            string_linklist=string_linklist+"NULL"
            print(string_linklist)

if __name__=="__main__":
    #create the node data and pointer 

    linklist= Linklist()
    print(Linklist())
    # #create the linklist 

    # #create the node n
    # n=Node("1")
    # #create the pointer to node n from the head 
    # linklist.head=n
    # #create the node n1
    # n1=Node("2")
    # #create the pointer of node n to node n1
    # n.next=n1
    # #create the node n2
    # n2=Node("3")
    # #create the pointer of node n1 to node n2 
    # n1.next=n2


    # linklist.insert_begining("bg")
    # linklist.display()
    # print(linklist.search_ele("2"))
    # linklist.to_string()

    ll=Linklist()
    ll.insert_begining("1")
    ll.insert_begining("2")
    ll.insert_begining("3")
    ll.insert_begining("4")
    print(ll.display())
    
    '''
    else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node

    '''