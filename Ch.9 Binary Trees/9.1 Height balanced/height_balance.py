import collections

#code
def height_balanced(tree):
    Balanced = collections.namedtuple("Balanced", ("balanced", "height"))

    def check_balance(tree):
        if not tree:
            return Balanced(True, -1)
        
        left = check_balance(tree.left)
        if not left.balanced:
            return Balanced(False, 0)

        right = check_balance(tree.right)
        if not right.balanced:
            return Balanced(False, 0)

        return Balanced(abs(left.height - right.height) < 2, max(left.height, right.height) + 1)

    return check_balance(tree).balanced

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

tree1 = BinaryTreeNode(5, BinaryTreeNode(3, BinaryTreeNode(2, BinaryTreeNode(1, BinaryTreeNode(0))), BinaryTreeNode(4)), BinaryTreeNode(8))
tree2 = BinaryTreeNode(5, BinaryTreeNode(3, BinaryTreeNode(2), BinaryTreeNode(4)), BinaryTreeNode(8))

# Test
print(height_balanced(tree1))
print(height_balanced(tree2))