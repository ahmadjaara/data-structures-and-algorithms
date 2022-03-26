# Stacks and Queues
<!-- Short summary or background information -->
**Stack** is a linear data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous

**Queue** is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).

## Challenge
<!-- Description of the challenge -->
stack

Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:

push

    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.

pop

    Arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack
    Should raise exception when called on empty stack

peek

    Arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack

is empty

    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.

Queue

Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:

enqueue

    Arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.

equeue

    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue

peek

    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack

is empty

    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
for stack methods : push(), pop(), isEmpty() and peek() all take O(1) time. since I dont run any loop in any of these operations.
push() take O(1) space since it add a node each time you use it

for Queue methods : enqueue(), dequeue(), isEmpty() and peek() all take O(1) time. since I dont run any loop in any of these operations.
enqueue() take O(1) space since it add one node each time you use it

## API
<!-- Description of each method publicly available to your Stack and Queue-->
Stack

push

    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.
pop

    Arguments: none
    Returns: the value from node from the top of the stack
peek

    Arguments: none
    Returns: Value of the node located at the top of the stack
is empty

    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.

Queue

enqueue

    Arguments: value
    adds a new node with that value to the back of the queue with an O(1) Time performance.

dequeue

    Arguments: none
    Returns: the value from node from the front of the queue

peek

    Arguments: none
    Returns: Value of the node located at the front of the queue

is empty

    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty
