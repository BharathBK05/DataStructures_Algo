class Node:
    def __init__(self, data):
        self.data = data
        self.left : Node | None = None
        self.right : Node | None = None

def display(tree):
    if tree:
        display(tree.left)      
        print(tree.data)
        display(tree.right)     

def main():
    tree = Node(2)
    tree.left = Node(4)
    tree.right = Node(6)
    display(tree)

if __name__ == '__main__':
    try:
        main()

    except Exception as e:
        print(e)    