import Binary_Tree

tree = Binary_Tree.Node()

root = Binary_Tree.insert(tree, 3)
root = Binary_Tree.insert(tree, 2)
root = Binary_Tree.insert(tree, 4)
root = Binary_Tree.insert(tree, 7)
root = Binary_Tree.insert(tree, 6)
root = Binary_Tree.insert(tree, 8)

print(root)


# Функція для знаходження найменшого значення в дереві
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.val

print("Найменше значення:", find_min(root))