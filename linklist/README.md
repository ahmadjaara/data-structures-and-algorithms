# Singly Linked List
<!-- Short summary or background information -->
A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail).

Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.

"defenetion from educative website"
## Challenge
<!-- Description of the challenge -->
create a linklist data structure and 
add a method to display all the data inside the linklist and a method ato insert noe=de at the begining of the linklist and a method to search inside for an element inside the linklist 

"
challenge feature :

Node

    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

Linked List

    Create a Linked List class
    Within your Linked List class, include a head property.
    Upon instantiation, an empty Linked List should be created.

"
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- for insert method i use a o(1) 

- for diplay/search_ele/tostring methods i use a loop to do the functionality for these methods so it is o(n)


## API
<!-- Description of each method publicly available to your Linked List -->
- insert_begining method :        
    
    Arguments: data
    Adds a new node with value to the head of the list with an O(1) Time performance.

- search_ele method:

    Arguments: value to search for it inside the linklist 
    Returns: Boolean
    Indicates whether that value exists as a Node  value somewhere within the list.

- display method: 
    
    its a method to print the collecation for all the element inside the linked list 
        
- to_string(self):
        
    Returns: a string representing all the values in the Linked List, formatted as:
    "{ a } -> { b } -> { c } -> NULL"
        