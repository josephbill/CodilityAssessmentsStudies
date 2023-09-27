class TreeNode: 
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None


class BinaryTree: 
    def __init__(self, root_value) -> None:
        self.root = TreeNode(root_value)
    #insert root value
    def insert(self,value): 
        self._insert(self.root, value)

    # _insert 
    def _insert(self, current_node, value):
        # checking if node is defined 
        if value < current_node.value:
            if current_node.left:
                self._insert(current_node.left, value)
            else:
                # then node is not defined 
                current_node.left = TreeNode(value)
        else:
            if current_node.right:
                self._insert(current_node.right, value)
            else:
                # then node is not defined 
                current_node.right = TreeNode(value) 

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, depth):
        if node:
            self._print_tree(node.right, depth + 1)
            print('   ' * depth + '|--', node.value)
            self._print_tree(node.left, depth + 1)


# creating an instance 
# root node 
binary_tree = BinaryTree(5)
binary_tree.insert(6)
binary_tree.insert(7)
binary_tree.insert(8)
binary_tree.insert(9)
binary_tree.insert(10)

print(binary_tree.print_tree())


# Binary Tree Structure:
#       |-- 10
#    |-- 9
#       |-- 8
# |-- 7
#       |-- 6
# |-- 5

# Insertion , deletion and searching of data.