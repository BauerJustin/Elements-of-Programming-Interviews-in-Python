#code
def has_path_sum(tree, remaining):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining == tree.data
    return has_path_sum(tree.left, remaining-tree.data) or has_path_sum(tree.right, remaining-tree.data)

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

tree1 = BinaryTreeNode(2, BinaryTreeNode(3, BinaryTreeNode(6, BinaryTreeNode(1), BinaryTreeNode(1)), BinaryTreeNode(4)))
tree2 = BinaryTreeNode(2, BinaryTreeNode(3, BinaryTreeNode(5, BinaryTreeNode(1), BinaryTreeNode(1)), BinaryTreeNode(4)))

# Test
print(has_path_sum(tree1, 12))
print(has_path_sum(tree2, 12))