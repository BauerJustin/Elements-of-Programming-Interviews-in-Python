#code
def exterior(tree):
    def leaf(node):
        return not node.left and not node.right

    def left(subtree, boundary):
        if not subtree:
            return []
        output = [subtree] if boundary or leaf(subtree) else []
        output += left(subtree.left, boundary)
        output += left(subtree.right, boundary and not subtree.left)
        return output

    def right(subtree, boundary):
        if not subtree:
            return []
        output = right(subtree.left, boundary and not subtree.right)
        output += right(subtree.right, boundary)
        output += [subtree] if boundary or leaf(subtree) else []
        return output

    return ([tree] + left(tree.left, True) + right(tree.right, True)) if tree else []

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

def print_list(A):
    for i in A:
        print(i.data)

tree = BinaryTreeNode(6, BinaryTreeNode(3, BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(2)), BinaryTreeNode(5)))

# Test
print_list(exterior(tree))