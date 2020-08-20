def tree_depth(tree):
    result = []
    if not tree:
        return result

    current = [tree]
    while current:
        result.append([node.data for node in current])
        current = [branch for node in current for branch in (node.left, node.right) if branch]
    return result