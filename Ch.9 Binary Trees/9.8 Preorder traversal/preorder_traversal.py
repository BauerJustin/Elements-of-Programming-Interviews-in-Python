#code
def preorder_traversal(tree):
    path = [tree]
    result = []
    while path:
        curr = path.pop()
        if curr:
            result.append(curr.data)
            path += [curr.right, curr.left]
    return result

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right

tree = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4, BinaryTreeNode(2), BinaryTreeNode(13)), BinaryTreeNode(7)))

# Test
print(preorder_traversal(tree))