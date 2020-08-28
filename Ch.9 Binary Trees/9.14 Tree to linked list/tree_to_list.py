#code
def tree_to_list(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree.data]
    return tree_to_list(tree.left) + tree_to_list(tree.right)

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

tree = BinaryTreeNode(6, BinaryTreeNode(3, BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(2)), BinaryTreeNode(5)))

# Test
print(tree_to_list(tree))