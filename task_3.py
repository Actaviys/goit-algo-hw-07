import Binary_Tree

tree = Binary_Tree.Node()

root = Binary_Tree.insert(tree, 3)
root = Binary_Tree.insert(tree, 2)
root = Binary_Tree.insert(tree, 4)
root = Binary_Tree.insert(tree, 7)
root = Binary_Tree.insert(tree, 6)
root = Binary_Tree.insert(tree, 8)

print(root)


# Рекурсивно знаходжу суму всіх значень у дереві
def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

print("Сума всіх значень:", sum_tree(root))