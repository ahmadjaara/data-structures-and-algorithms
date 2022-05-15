class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def get_level(self):
        """
        method to return the level for the elment in the tree 
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self):
        """
        method to print the tree elment in a tree shape 
        """
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        """
        method to add child element to the tree element inside it 
        """
        child.parent = self
        self.children.append(child)


def build_k_tree():
    """
        function to create K-ary tree 
    """
    root = TreeNode(1)

    levelelem1 = TreeNode(8)
    levelelem1.add_child(TreeNode(5))
    levelelem1.add_child(TreeNode(6))
    levelelem1.add_child(TreeNode(7))

    levelelem2 = TreeNode(9)
    levelelem2.add_child(TreeNode(8))
    levelelem2.add_child(TreeNode(9))
    levelelem2.add_child(TreeNode(10))

    levelelem3 = TreeNode(4)
    levelelem3.add_child(TreeNode(11))
    levelelem3.add_child(TreeNode(15))

    root.add_child(levelelem1)
    root.add_child(levelelem2)
    root.add_child(levelelem3)

    # root.print_tree()
    return root

def fizz_buzz_tree(root):
    """
    fizz buzz tree function
    Arguments: k-ary tree
    Return: new k-ary tree replace value inside the tree
    
    If the value is divisible by 3, replace the value with “Fizz”
    If the value is divisible by 5, replace the value with “Buzz”
    If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    If the value is not divisible by 3 or 5, simply turn the number into a String.


    """
    spaces = " " * root.get_level() * 4
    prefix = spaces + "|--" if root.parent else ""
    if root.data % 5 == 0 and root.data % 3 == 0:
        root.data = "FizzBuzz"
    elif root.data % 5 == 0:
        root.data = "Buzz"
    elif root.data % 3 == 0:
        root.data = "Fizz"
    else:
        root.data = str(root.data)
    print(prefix + str(root.data))
    if root.children:
        for child in root.children:
            fizz_buzz_tree(child)

if __name__ == '__main__':
    # ktree=build_k_tree()
    # fizz_buzz_tree(ktree)
    # k_tree=TreeNode()
    # k_tree.children()
    
    # root = TreeNode(1)

    # levelelem1 = TreeNode(2)
    # levelelem1.add_child(TreeNode(5))
    # levelelem1.add_child(TreeNode(6))
    # levelelem1.add_child(TreeNode(7))

    # levelelem2 = TreeNode(3)
    # levelelem2.add_child(TreeNode(8))
    # levelelem2.add_child(TreeNode(9))
    # levelelem2.add_child(TreeNode(10))

    # levelelem3 = TreeNode(4)
    # levelelem3.add_child(TreeNode(11))
    # levelelem3.add_child(TreeNode(12))

    # root.add_child(levelelem1)
    # root.add_child(levelelem2)
    # root.add_child(levelelem3)
    
    # print(root.print_tree())

    tree = build_k_tree()
    tree2 = build_k_tree()
    # root.add_child(KTreeNode(16))
    print(tree.print_tree())

    fizz_buzz_tree(tree)
    