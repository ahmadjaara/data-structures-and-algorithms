# Singly Linked List
<!-- Short summary or background information -->
A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail).

Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.

"defenetion from educative website"

## Challenge
<!-- Description of the challenge -->
`create a linklist data structure and
add a method to display all the data inside the linklist and a method to insert node at the begining of the linklist and a method to search for an element inside the linklist`
and another method like insert node after and before node insde the linklist and a method to search for
the K(index) for the node data
and a method to Zip two linked lists together into one so that the nodes alternate between the two lists

"
challenge feature :

Node

    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

Linked List

    Create a Linked List class
    Within your Linked List class, include a head property.
    Upon instantiation, an empty Linked List should be created.

"

## Feature Tasks

Write the following methods for the Linked List class:

- insert

    Arguments: value
    Returns: nothing
    Adds a new node with that value to the head of the list with an O(1) Time performance.

- includes

    Arguments: value
    Returns: Boolean
    Indicates whether that value exists as a Node’s value somewhere within the list.

- to string

    Arguments: none
    Returns: a string representing all the values in the Linked List, formatted as:
    "{ a } -> { b } -> { c } -> NULL"

- append method

    arguments: new value
    adds a new node with the given value to the end of the list

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
- append_linklist(self,value_add)

    add a node at the end of the link list
    input a data for the node that will add
    output a node placed at the end of link list

## white board  

![append pic](pic/append.jpg "append pic")
