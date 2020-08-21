import collections

#code
def lca(node1, node2):
    Status = collections.namedtuple('Status', ('num', 'ancestor'))

    def lca_helper(tree, node1, node2):
        if not tree:
            return Status(0, None)

        left = lca_helper(tree.left,node1,node2)
        if left.num == 2:
            return left

        right = lca_helper(tree.right,node1,node2)
        if right.num == 2:
            return right

        temp = (left.num + right.num + int(tree is node1) + int(tree is node2))
        return Status(temp, tree if temp == 2 else None)

    tree = node1
    while tree.parent:
        tree = tree.parent

    return lca_helper(tree,node1, node2).ancestor.data

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

tree = BinaryTreeNode(5)
tree.left = BinaryTreeNode(3, None, None, tree)
tree.right = BinaryTreeNode(4, None, None, tree)

# Test
print(lca(tree.left, tree.right))