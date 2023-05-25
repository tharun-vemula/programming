class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)

    @staticmethod
    def inorder(root):
        if root:
            Node.inorder(root.left)
            print(root.data, end=" ")
            Node.inorder(root.right)

    @staticmethod
    def preorder(root):
        if root:
            print(root.data, end=" ")
            Node.preorder(root.left)
            Node.preorder(root.right)

    @staticmethod
    def postorder(root):
        if root:
            Node.postorder(root.left)
            Node.postorder(root.right)
            print(root.data, end=" ")

    @staticmethod
    def levelorder(root):
        from queue import Queue

        if root is None:
            return

        queue = Queue(25)
        queue.put(root)

        while not queue.empty():
            node = queue.get()
            print(node.data, end=" ")

            if node.left is not None:
                queue.put(node.left)
            if node.right is not None:
                queue.put(node.right)


root = Node(25)
# Inserting values in BST
root.insert(15)
root.insert(50)
root.insert(10)
root.insert(22)
root.insert(35)
root.insert(70)
root.insert(4)
root.insert(12)
root.insert(18)
root.insert(24)
root.insert(31)
root.insert(44)
root.insert(66)
root.insert(90)

# printing BST
print("Inorder Traversal:")
Node.inorder(root)
print("")
print("Preorder Traversal:")
Node.preorder(root)
print("")
print("Postorder Traversal:")
Node.postorder(root)
print("")
print("Level torder Traversal:")
Node.levelorder(root)
