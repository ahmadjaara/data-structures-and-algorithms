from platform import node


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
                linklist_all+= str(temp.data)+" -->"
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
            
            m=Node(value_add_before)
            
            m.next =self.head

            self.head=m
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
    
    def kthFromEnd(self,k):
        """
        method for searching for the K th  element in the
        linklist which k start from the tail of the linklist 
        input: k to determine the index for the node
        output: the data or value of the K node  
        """
        len =0
        temp=self.head
        while temp:
            len+=1
            temp=temp.next
        print(len)
        index=0
        ptr=self.head
        newind=(len-1)-k
        print(newind)
        while ptr:
            # print(ptr.data)
            if (index==newind):
               return ptr.data
            index+=1
            ptr=ptr.next
        return("Exception")
        
    def zipLists(self,l1,l2):
        """
        
        """
        before_ptr=l1.head

        current_ptr=l2.head

        #to check if the first list is empty 
        if before_ptr==None:
            after_ptr=None
            current_ptr= None
            l1.head=l2.head
        elif current_ptr== None:
            after_ptr=None
            current_ptr= None
            l2.head=l1.head 
        else:
            after_ptr=before_ptr.next


        while (current_ptr!=None):
            
            before_ptr.next=current_ptr

            before_ptr=current_ptr

            current_ptr=after_ptr

            after_ptr=before_ptr.next
        
        #empty the second list
        l2.head=None 

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def panderrom(self):
        nums=[]
        temp=self.head
        while temp:
            nums.append(temp.data)
            temp=temp.next
        i=0
        j=len(nums)-1

        while i<=j:
            if nums[i]!=nums[j]:
                return False
            i+=1
            j-=1
        return True

def merge_sorted_list(l1,l2):
        curr=Linklist()

        while l1.head and l2.head:
            if l1.head.data < l2.head.data:
                curr.next=Node(l1.head.data)
                l1.head=l1.head.next
            else:
                curr.next=Node(l2.head)
                l2.head=l2.head.next
            curr=curr.next
        if l1:
            curr.next=l1.head
        elif l2:
            curr.next=l2.head
        return curr.display()




        

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
    ll2=Linklist()

    ll.append_linklist(1)
    ll.append_linklist(2)
    ll.append_linklist(3)
    ll.append_linklist(4)
    # ll.insert_after("last","4")
    # ll.append_linklist("41")
    # ll.append_linklist("42")
    # ll.append_linklist("43")

    # ll.append_linklist("2")
    # ll.append_linklist("2")
    ll2.append_linklist(1)
    ll2.append_linklist(8)
    ll2.append_linklist(9)
    ll2.append_linklist(10)
  
    # print(ll.display())
    # print(ll2.display())
    # ll.zipLists(ll,ll2)
    print(ll.display())
   
    # print(ll.panderrom())
    
    print(merge_sorted_list(ll2,ll))