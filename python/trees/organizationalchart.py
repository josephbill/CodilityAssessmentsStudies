class TreeNode: 
    def __init__(self,employee_id,employee_name) -> None:
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.left = None
        self.right = None 


class OrganizationChart:
    def __init__(self) -> None:
        self.root = None
 
    # Insertion 
    def insert(self, employee_id, employee_name):
        self.root = self._insert(self.root, employee_id, employee_name)

    def _insert(self, node , employee_id,employee_name):
        # if no node 
        if not node: 
            return TreeNode(employee_id,employee_name)
        
        if employee_id < node.employee_id:
            node.left = self._insert(node.left, employee_id, employee_name)
        elif employee_id > node.employee_id:
            node.right = self._insert(node.right , employee_id,employee_name)
        
        return node
    
    # search
    def search(self, employee_id):
        return self._search(self.root, employee_id)
    
    def _search(self, node, employee_id):
        # when searching a tree : case for root : case left /right child nodes 
        if not node or node.employee_id == employee_id:
            return node 
        # recursively
        if employee_id < node.employee_id:
            return self._search(node.left, employee_id)
        else: 
            return self._search(node.right, employee_id)
        
    # find miminum child nodes for replacement in deletion process 
    def find_min(self,node):
        current = node 
        while current.left:
            current = current.left
        return current
        
    # delete 
    def delete(self, employee_id):
        self.root = self._delete(self.root, employee_id)

    def _delete(self, node ,employee_id):
        # recursively trasverse the tree to find the node with specified id 
        # delete if id is found 
        # node with no children , node with one child , node with two children
        # nodes that are not presented are normally tagged as null 
        if not node: 
            return node
        
        # comparing of employee ids 
        if employee_id < node.employee_id:
            node.left = self._delete(node.left, employee_id)
        elif employee_id > node.employee_id: 
            node.right = self._delete(node.right, employee_id)
        #  if employee id matches the current nodes id ,
        # case 1 : node to be deleted has no left child , thus return right child for deletion process 
        # case 2 : node to be deleted has no right child , thus return left child for deletion process 
        else:
            if not node.left:
                return node.right 
            elif not node.right:
                return node.left 
        
        # delete a node with two children
            temp = self.find_min(node.right)
            node.employee_id = temp.employee_id
            node.employee_name = temp.employee_name 
            node.right = self._delete(node.right, temp.employee_id)

        return node
    

    def inorder_traversal(self, node): 
        if node: 
            self.inorder_traversal(node.left)
            print(f"Employee ID : {node.employee_id}, Employee Name: {node.employee_name}")
            self.inorder_traversal(node.right)

# Example usage: Organization chart as a binary search tree
org_tree = OrganizationChart()
org_tree.insert(101, "John Doe")
org_tree.insert(105, "Alice Smith")
org_tree.insert(98, "Bob Johnson")
org_tree.insert(110, "Eve Williams")

# Display the organization chart (inorder traversal)
print("Organization Chart (Inorder Traversal):")
org_tree.inorder_traversal(org_tree.root)

# Search for an employee
search_employee_id = 989
search_result = org_tree.search(search_employee_id)
if search_result:
    print(f"\nEmployee found - Employee ID: {search_result.employee_id}, Employee Name: {search_result.employee_name}")
else:
    print(f"\nEmployee with ID {search_employee_id} not found")

# Delete an employee
delete_employee_id = 105
org_tree.delete(delete_employee_id)
print(f"\nDeleted employee with ID {delete_employee_id}")

# Display the updated organization chart (inorder traversal)
print("\nUpdated Organization Chart (Inorder Traversal):")
org_tree.inorder_traversal(org_tree.root)