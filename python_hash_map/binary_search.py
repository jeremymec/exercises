class Stack:

    def __init__(self):
        self.elements = []

    def insert(self, value):
        self.elements.append(value)
    
    def poll(self):
        return self.elements[-1]

    def pop(self):
        return self.elements.pop()

    def is_empty(self):
        if len(self.elements) <= 0:
            return True
        return False

class BSTNode:

    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    
class BST:

    def __init__(self):
        self.root_node = None

    def insert(self, key, value):
        
        current_node = self.root_node

        if (current_node is None):
            self.root_node = BSTNode(key, value, None, None)
            return

        previous_node = None
        while (True):
            previous_node = current_node
            if key < current_node.key:
                if (current_node.left is None):
                    current_node.left = BSTNode(key, value, None, None)
                    break
                current_node = current_node.left.key
            elif key > current_node.key:
                if (current_node.right is None):
                    current_node.right = BSTNode(key, value, None, None)
                    break
                current_node = current_node.right.key

    def __str__(self):
        stack = Stack()

        if (self.root_node is None):
            return ""

        stack.insert(self.root_node)

        pretty_print = ""
        
        while(not stack.is_empty()):
            node = stack.pop()
            pretty_print += str(node.key) + "\n"
            if (node.right is not None):
                stack.insert(node.right)
            if (node.left is not None):
                stack.insert(node.left)

        return pretty_print
                

if __name__ == "__main__":
    tree = BST()
    tree.insert(5, "Apple")
    tree.insert(8, "Banana")
    tree.insert(4, "Orange")
    print(str(tree))