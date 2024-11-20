import matplotlib.pyplot as plt  
import networkx as nx  

class TreeNode:  
    def __init__(self, value):  
        self.value = value  
        self.left = None  
        self.right = None  

class BinarySearchTree:  
    def __init__(self):  
        self.root = None  

    def insert(self, value):  
        if self.root is None:  
            self.root = TreeNode(value)  
        else:  
            self._insert_recursively(self.root, value)  

    def _insert_recursively(self, node, value):  
        if value < node.value:  
            if node.left is None:  
                node.left = TreeNode(value)  
            else:  
                self._insert_recursively(node.left, value)  
        else:  
            if node.right is None:  
                node.right = TreeNode(value)  
            else:  
                self._insert_recursively(node.right, value)  

    def build_graph(self):  
        graph = nx.DiGraph()  
        self._build_graph(self.root, graph)  
        return graph  

    def _build_graph(self, node, graph):  
        if node is not None:  
            if node.left is not None:  
                graph.add_edge(node.value, node.left.value)  
                self._build_graph(node.left, graph)  
            if node.right is not None:  
                graph.add_edge(node.value, node.right.value)  
                self._build_graph(node.right, graph)  

    def visualize(self):  
        graph = self.build_graph()  
        pos = nx.spring_layout(graph)  # positions for all nodes  
        nx.draw(graph, pos, with_labels=True, arrows=True)  
        plt.title("Binary Search Tree Visualization")  
        plt.show()  

# Example usage  
if __name__ == "__main__":  
    bst = BinarySearchTree()  
    values = [7, 3, 9, 1, 5, 8, 10]  

    for value in values:  
        bst.insert(value)  

    print("Visualizing BST...")  
    bst.visualize()