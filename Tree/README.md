# Trees
<!-- Short summary or background information -->
tree data structure is a kind of hierarchal data arranged in a tree-like structure. It consists of a central node, structural nodes, and sub nodes, which are connected via edges. We can also say that tree data structure has roots, branches, and leaves connected with one another.

- Node - A Tree node is a component which may contain its own values, and references to other nodes
- Root - The root is the node at the beginning of the tree
- K - A number that specifies the maximum number of children any node may have in a k-ary tree. In a binary tree, k = 2.
- Left - A reference to one child node, in a binary tree
- Right - A reference to the other child node, in a binary tree
- Edge - The edge in a tree is the link between a parent and child node
- Leaf - A leaf is a node that does not have any children
- Height - The height of a tree is the number of edges from the root to the furthest leaf

## Challenge
<!-- Description of the challenge -->
### **`Features`**

### **Node**

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

### **Binary Tree**

Create a Binary Tree class

Define a method for each of the depth first traversals:

- pre order
- in order
- post order which returns an array of the values, ordered appropriately.

        Pre-order: root >> left >> right
        In-order: left >> root >> right
        Post-order: left >> right >> root

Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

### **Binary Search Tree**

Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

### **Add**

    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.

### **Contains**

    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The Big O time complexity of a Binary Search Tree’s insertion and search operations is O(h), or O(height). In the worst case, we will have to search all the way down to a leaf, which will require searching through as many nodes as the tree is tall. In a balanced (or “perfect”) tree, the height of the tree is log(n). In an unbalanced tree, the worst case height of the tree is n.

The Big O space complexity of a BST search would be O(1). During a search, we are not allocating any additional space.

## API
<!-- Description of each method publicly available in each of your trees -->
- pre_order :

    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree Pre-order: root >> left >> right
- in_order :

    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree In-order: left >> root >> right
- post_order :

    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree **Post-order: left >> right >> root
- add:

    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
- contains :

    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
