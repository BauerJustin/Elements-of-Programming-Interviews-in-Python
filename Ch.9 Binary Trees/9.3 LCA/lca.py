import collections

#code
def lca(tree, node1, node2):
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

    return lca_helper(tree,node1, node2).ancestor.data

# Binary tree base code
class BinaryTreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

tree1 = BinaryTreeNode(5, BinaryTreeNode(3, BinaryTreeNode(2, BinaryTreeNode(1, BinaryTreeNode(0))), BinaryTreeNode(4)), BinaryTreeNode(8))
tree2 = BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(3))

# Test
print(lca(tree1, tree1.left.left.left, tree1.left.left))
print(lca(tree2, tree2.left, tree2.right))