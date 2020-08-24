#code
def inorder_traversal(tree):
    s = []
    result = []

    while s or tree:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            result.append(tree.data)
            tree = tree.right
    
    return result

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

tree = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4, BinaryTreeNode(2), BinaryTreeNode(13)), BinaryTreeNode(7)))

# Test
print(inorder_traversal(tree))