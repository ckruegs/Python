# A binary tree is a tree structure type where each node
# may have at most, two children. They are primarily used to
# represent heirarchial relationships such as records or families

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# inorder tree traversal
def printInorder(root):
    if root:
        # first recur on left
        printInorder(root.left)

        #print node data
        print(root.val),

        #recur on right
        printInorder(root.right)

# postorder tree traversal
def printPostorder(root):

    if root:
        # first recur on left
        printPostorder(root.left)

        #print node data
        print(root.val),

# preorder tree traversal
def printPreorder(root):
    if root:
        # print node data
        print(root.val),

        # recur on left
        printPreorder(root.left)

        # recur on right
        printPreorder(root.right)

# main driver code
root = Node(8)
root.left = Node(5)
root.right = Node(4)
root.right.right = Node(11)
root.right.right.left = Node(3)
root.left.left = Node(9)
root.left.right = Node(7)
root.left.right.left = Node(1)
root.left.right.right = Node(12)
root.left.right.right.left = Node(2)

print("Preorder traversal of binary tree:\n")
printPreorder(root)

print("Inorder traversal of binary tree:\n")
printInorder(root)

print("Postorder traversal of binary tree:\n")
printPostorder(root)