#code
def kth_node(tree, k):
    while tree:
        if tree.data == k:
            return tree
        elif tree.data > k:
            tree = tree.left
        else:
            tree = tree.right
    return None

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

tree = BinaryTreeNode(6, BinaryTreeNode(3, BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(2)), BinaryTreeNode(5)))

# Test
print(kth_node(tree, 2))