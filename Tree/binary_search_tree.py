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
    def minimum_value_node(root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def delete(root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = Node.delete(root.left, key)
        elif key > root.data:
            root.right = Node.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = Node.minimum_value_node(root.right)
            root.data = temp.data
            root.right = Node.delete(root.right, temp.data)
        return root


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
