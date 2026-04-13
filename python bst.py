class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert function
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# Find minimum value
def find_min(root):
    while root.left:
        root = root.left
    return root

# Delete function
def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        # Node found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Main program
root = None

# Insert values
nums = [50, 30, 70, 20, 40, 60, 80]
for n in nums:
    root = insert(root, n)

print("Before deletion:")
inorder(root)

# Delete a node
root = delete(root, 50)

print("\nAfter deletion:")
inorder(root)