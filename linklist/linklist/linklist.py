

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
        if self.head is None:
           return "linked list is empty"

        else:
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
            return "linked list is empty"
        else:
            temp = self.head
            while temp:
                string_linklist+="{{{0}}}".format(temp.data) +" -->"+" "
                temp = temp.next
            string_linklist=string_linklist+"NULL"
            print(string_linklist)

    def append_linklist(self,value_add):
        """
        add a node at the end of the link list 
        input a data for the node that will add
        output a node placed at the end of link list 
        """
        if self.head is None:
            nd=Node(value_add)
            
            nd.next =self.head

            self.head=nd

        else:
            nd=Node(value_add)
            
            temp = self.head

            while temp.next:
                temp = temp.next
            temp.next=nd


    def insert_after(self,value_add_after,place):
        """
        add a node at after a specific node value in the link list 
        input a data for the node that will add and 
        the place (which is the value of the node that i will add the new node after it)
        output a node placed after a specific node in the link list 
        """
        nd=Node(value_add_after)

        temp = self.head

        while temp.data!=place and temp.next!=None:
            temp=temp.next

        if temp.data==place:
            nd.next=temp.next
            temp.next=nd
        else:
            print("no node value match the input")
        
    
    def insert_before(self,value_add_before,place):
        """
        add a node at before a specific node value in the link list 
        input a data for the node that will add and 
        the place (which is the value of the node that i will add the new node before it)
        output a node placed before a specific node in the link list 
        """
        if self.head.data == place:
            
            nd=Node(value_add_before)
            
            nd.next =self.head

            self.head=nd
        else:
            m=Node(value_add_before)

            temp = self.head
            ptr=temp
            while temp.data!=place and temp.next!=None:
                ptr=temp
                temp=temp.next
            if temp.data==place:
                m.next=ptr.next
                ptr.next=m
            else:
                print("no node value match the input")


        
        
        


            




if __name__=="__main__":
    #create the node data and pointer 

    linklist= Linklist()
    # print(Linklist())
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
    # ll.insert_begining("1")
    # ll.insert_begining("2")
    # ll.insert_begining("3")
    # ll.insert_begining("4")
    # ll.append_linklist("end")
    # ll.insert_after("k","1")
    # ll.insert_before("k","1")
    # ll.insert_before("k","k")
    # ll.insert_before("o","k")
    # ll.insert_after("hello","555")
    # ll.append_linklist("100")
    # ll.append_linklist("10000")
    ll.append_linklist("1")
    ll.append_linklist("2")
    ll.append_linklist("3")
    ll.append_linklist("4")
    ll.insert_after("last","4")
    print(ll.display())