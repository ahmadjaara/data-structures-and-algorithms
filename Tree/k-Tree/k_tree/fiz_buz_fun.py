class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def get_level(self):
        """
        method to return the level for the eelment in the tree 
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
        function to create tree 
    """
    root = TreeNode(1)

    levelelem1 = TreeNode(2)
    levelelem1.add_child(TreeNode(5))
    levelelem1.add_child(TreeNode(6))
    levelelem1.add_child(TreeNode(7))

    levelelem2 = TreeNode(3)
    levelelem2.add_child(TreeNode(8))
    levelelem2.add_child(TreeNode(9))
    levelelem2.add_child(TreeNode(10))

    levelelem3 = TreeNode(4)
    levelelem3.add_child(TreeNode(11))
    levelelem3.add_child(TreeNode(12))

    root.add_child(levelelem1)
    root.add_child(levelelem2)
    root.add_child(levelelem3)

    root.print_tree()
def  fizz_buzz_tree(k_tree):

    if (k % 5 == 0) and (k % 3 == 0):
        return "FizzBuzz"
    if k % 5 == 0:
        return "Buzz"
    if k % 3 == 0:
        return "Fizz"
    return str(k)
if __name__ == '__main__':
    # ktree=build_k_tree()
    # fizz_buzz_tree(ktree)
    # k_tree=TreeNode()
    # k_tree.children()
    
    root = TreeNode(1)

    levelelem1 = TreeNode(2)
    levelelem1.add_child(TreeNode(5))
    levelelem1.add_child(TreeNode(6))
    levelelem1.add_child(TreeNode(7))

    levelelem2 = TreeNode(3)
    levelelem2.add_child(TreeNode(8))
    levelelem2.add_child(TreeNode(9))
    levelelem2.add_child(TreeNode(10))

    levelelem3 = TreeNode(4)
    levelelem3.add_child(TreeNode(11))
    levelelem3.add_child(TreeNode(12))

    root.add_child(levelelem1)
    root.add_child(levelelem2)
    root.add_child(levelelem3)
    
    print(root.children)
    