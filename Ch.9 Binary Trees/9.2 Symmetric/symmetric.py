#code
def symmetric(tree):
    
    def check_symmetry(tree1, tree2):
        # Both empty
        if not tree1 and not tree2:
            return True
        # Both full
        elif tree1 and tree2:
            # Current nodes match and recursively their children
            return (tree1.data == tree2.data and check_symmetry(tree1.left,tree2.right) and check_symmetry(tree1.right,tree2.left))
        return False

    return not tree or check_symmetry(tree.left, tree.right)

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

tree1 = BinaryTreeNode(5, BinaryTreeNode(3, BinaryTreeNode(2, BinaryTreeNode(1, BinaryTreeNode(0))), BinaryTreeNode(4)), BinaryTreeNode(8))
tree2 = BinaryTreeNode(5, BinaryTreeNode(3, BinaryTreeNode(2), BinaryTreeNode(4)), BinaryTreeNode(3, BinaryTreeNode(4), BinaryTreeNode(2)))

# Test
print(symmetric(tree1))
print(symmetric(tree2))