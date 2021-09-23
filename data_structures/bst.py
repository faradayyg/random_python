"""Binary Search Tree Practice."""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def print(self):
        self.print_helper(self.root)

    def print_helper(self, node):
        if node:
            print(node.value)
            self.print_helper(node.left)
            self.print_helper(node.right)

    def insert(self, new_val):
        if not self.root:
            self.root = Node(new_val)
            return

        parent = self.root
        print("Root: ", parent.value)
        while parent and parent.value:
            if parent.value >= new_val:
                if parent.left:
                    print("Proceeding to left child: ", parent.value)
                    parent = parent.left
                else:
                    print("Inserting Left: ", new_val)
                    parent.left = Node(new_val)
                    break
            else:
                if parent.right:
                    print("Proceeding to right child: ", parent.value)
                    parent = parent.right
                else:
                    print("Inserting Right: ", new_val)
                    parent.right = Node(new_val)
                    break

    def search(self, find_val):
        node = self.root
        while node and node.value:
            if node.value == find_val:
                return True
            else:
                if find_val > node.value:
                    node = node.right
                else:
                    node = node.left
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

tree.print()

# Check search
# Should be True
print(tree.search(4))
# # Should be False
print(tree.search(6))