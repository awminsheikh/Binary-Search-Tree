class TreeNode:  
    def __init__(self, key):  
        self.left = None  
        self.right = None  
        self.value = key  

class BinarySearchTree:  
    def __init__(self):  
        self.root = None  

    def insert(self, key):  
        if self.root is None:  
            self.root = TreeNode(key)  
        else:  
            self._insert_recursively(self.root, key)  

    def _insert_recursively(self, node, key):  
        if key < node.value:  
            if node.left is None:  
                node.left = TreeNode(key)  
            else:  
                self._insert_recursively(node.left, key)  
        else:  
            if node.right is None:  
                node.right = TreeNode(key)  
            else:  
                self._insert_recursively(node.right, key)  

    def search(self, key):  
        return self._search_recursively(self.root, key)  

    def _search_recursively(self, node, key):  
        if node is None or node.value == key:  
            return node  
        if key < node.value:  
            return self._search_recursively(node.left, key)  
        return self._search_recursively(node.right, key)  

    def in_order_traversal(self):  
        return self._in_order_recursively(self.root)  

    def _in_order_recursively(self, node):  
        if node is None:  
            return []  
        return (self._in_order_recursively(node.left) +  
                [node.value] +  
                self._in_order_recursively(node.right))  

# Example usage  
if __name__ == "__main__":  
    bst = BinarySearchTree()  
    values = [7, 3, 9, 1, 5, 8, 10]  

    for value in values:  
        bst.insert(value)  

    print("In-order traversal:", bst.in_order_traversal())  
    search_key = 5  
    found_node = bst.search(search_key)  
    if found_node:  
        print(f"{search_key} found in the BST.")  
    else:  
        print(f"{search_key} not found in the BST.")