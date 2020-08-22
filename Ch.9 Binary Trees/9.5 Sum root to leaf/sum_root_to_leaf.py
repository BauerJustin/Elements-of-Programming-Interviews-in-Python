#code
def sum_root_to_leaf(tree, partial_sum=0):
    if not tree:
        return 0
    
    partial_sum = partial_sum * 2 + tree.data
    if not tree.left and not tree.right:
        return partial_sum
    return sum_root_to_leaf(tree.left, partial_sum) + sum_root_to_leaf(tree.right, partial_sum)

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

tree = BinaryTreeNode(1, BinaryTreeNode(0, BinaryTreeNode(0, BinaryTreeNode(0), BinaryTreeNode(1)), BinaryTreeNode(1)))

# Test
print(sum_root_to_leaf(tree))