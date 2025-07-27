class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.traverse(new_val, self.root)
        pass
    
    def traverse(self, new_val, tree):
        if tree:
            if tree.value > new_val:
                if tree.left == None:
                    tree.left = Node(new_val)
                else:
                    self.traverse(new_val, tree.left)
                    
            elif tree.value <= new_val:
                if tree.right == None:
                    tree.right = Node(new_val)
                else:
                    self.traverse(new_val, tree.right)
                

    def search(self, find_val):
        self.result = False
        self.preorder_search(self.root,find_val)
        return self.result
    
    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                self.result = True
            self.preorder_search(start.left, find_val) 
            self.preorder_search(start.right, find_val)
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))